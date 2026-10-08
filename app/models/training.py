from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

from models.preprocessing import create_preprocessor


def train_models(df):

    X = df.drop("PRICE", axis=1)
    y = df["PRICE"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    models = {
        "Linear Regression": LinearRegression(),
        "Random Forest": RandomForestRegressor(
            n_estimators=200,
            random_state=42
        ),
        "Gradient Boosting": GradientBoostingRegressor(
            n_estimators=200,
            learning_rate=0.05,
            max_depth=3,
            random_state=42
        )
    }

    trained_models = {}
    results = []

    for name, regressor in models.items():

        pipeline = Pipeline(
            steps=[
                ("preprocessor", create_preprocessor()),
                ("regressor", regressor)
            ]
        )

        pipeline.fit(X_train, y_train)

        y_pred = pipeline.predict(X_test)

        mae = mean_absolute_error(y_test, y_pred)
        mse = mean_squared_error(y_test, y_pred)
        rmse = mse ** 0.5
        r2 = r2_score(y_test, y_pred)

        trained_models[name] = pipeline

        results.append({
            "Model": name,
            "MAE": mae,
            "RMSE": rmse,
            "R²": r2
        })

    return trained_models, results