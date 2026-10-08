from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler


CATEGORICAL = [
    "MAINROAD",
    "GUESTROOM",
    "BASEMENT",
    "HOTWATERHEATING",
    "AIRCONDITIONING",
    "PREFAREA",
    "FURNISHINGSTATUS"
]

NUMERICAL = [
    "AREA",
    "BEDROOMS",
    "BATHROOMS",
    "STORIES",
    "PARKING"
]


def create_preprocessor():
    return ColumnTransformer(
        transformers=[
            (
                "categorical",
                OneHotEncoder(handle_unknown="ignore"),
                CATEGORICAL
            ),
            (
                "numerical",
                StandardScaler(),
                NUMERICAL
            )
        ]
    )