import streamlit as st
import pandas as pd

from snowflake.snowpark.context import get_active_session

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="wide"
)

st.title("🏠 House Price Prediction")


# Load data

session = get_active_session()

df = session.table(
    "ML_WORKFLOW_DB.ML_SCHEMA.HOUSING"
).to_pandas()


# Features and target

X = df.drop("PRICE", axis=1)
y = df["PRICE"]


categorical = [
    "MAINROAD",
    "GUESTROOM",
    "BASEMENT",
    "HOTWATERHEATING",
    "AIRCONDITIONING",
    "PREFAREA",
    "FURNISHINGSTATUS"
]

numerical = [
    "AREA",
    "BEDROOMS",
    "BATHROOMS",
    "STORIES",
    "PARKING"
]


# Preprocessing

preprocessor = ColumnTransformer(
    transformers=[
        (
            "categorical",
            OneHotEncoder(handle_unknown="ignore"),
            categorical
        ),
        (
            "numerical",
            StandardScaler(),
            numerical
        )
    ]
)


# Train-test split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Models

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


# Train models

trained_models = {}
results = []

for name, regressor in models.items():

    pipeline = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
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


# Tabs

tab1, tab2, tab3 = st.tabs([
    "📊 Dataset & Models",
    "🏠 House Details",
    "🔮 Prediction"
])


# Dataset and models tab

with tab1:

    st.subheader("Housing Dataset")

    st.dataframe(
        df.head(),
        use_container_width=True,
        hide_index=True
    )

    st.subheader("Model Comparison")

    results_df = pd.DataFrame(results)

    st.dataframe(
        results_df.style.format({
            "MAE": "₹{:,.0f}",
            "RMSE": "₹{:,.0f}",
            "R²": "{:.4f}"
        }),
        use_container_width=True,
        hide_index=True
    )

    st.subheader("Select Model")

    selected_model = st.selectbox(
        "Choose a model for prediction",
        list(trained_models.keys())
    )

    model = trained_models[selected_model]

    st.success(f"Selected Model: **{selected_model}**")


# House details tab

with tab2:

    st.subheader("Enter House Details")

    col1, col2 = st.columns(2)

    with col1:

        area = st.number_input(
            "Area (sq ft)",
            min_value=0,
            value=3000
        )

        bedrooms = st.number_input(
            "Bedrooms",
            min_value=0,
            value=3
        )

        bathrooms = st.number_input(
            "Bathrooms",
            min_value=0,
            value=2
        )

        stories = st.number_input(
            "Stories",
            min_value=0,
            value=2
        )

        parking = st.number_input(
            "Parking",
            min_value=0,
            value=1
        )

        mainroad = st.selectbox(
            "Main Road",
            ["yes", "no"]
        )

        guestroom = st.selectbox(
            "Guest Room",
            ["yes", "no"]
        )

    with col2:

        basement = st.selectbox(
            "Basement",
            ["yes", "no"]
        )

        hotwaterheating = st.selectbox(
            "Hot Water Heating",
            ["yes", "no"]
        )

        airconditioning = st.selectbox(
            "Air Conditioning",
            ["yes", "no"]
        )

        prefarea = st.selectbox(
            "Preferred Area",
            ["yes", "no"]
        )

        furnishingstatus = st.selectbox(
            "Furnishing Status",
            ["furnished", "semi-furnished", "unfurnished"]
        )


# Prediction tab

with tab3:

    st.subheader("🔮 House Price Prediction")

    st.write(
        f"Selected Model: **{selected_model}**"
    )

    if st.button(
        "Predict Price",
        use_container_width=True
    ):

        input_data = pd.DataFrame([{
            "AREA": area,
            "BEDROOMS": bedrooms,
            "BATHROOMS": bathrooms,
            "STORIES": stories,
            "MAINROAD": mainroad,
            "GUESTROOM": guestroom,
            "BASEMENT": basement,
            "HOTWATERHEATING": hotwaterheating,
            "AIRCONDITIONING": airconditioning,
            "PARKING": parking,
            "PREFAREA": prefarea,
            "FURNISHINGSTATUS": furnishingstatus
        }])

        prediction = model.predict(input_data)[0]

        st.success(
            f"🏠 Estimated House Price: ₹{prediction:,.0f}"
        )
