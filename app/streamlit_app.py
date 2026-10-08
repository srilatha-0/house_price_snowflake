import streamlit as st

from utils.data_loader import load_housing_data
from models.training import train_models
from components.dataset import show_dataset_and_models
from components.house_form import get_house_details
from components.prediction import show_prediction


st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="wide"
)

st.title("🏠 House Price Prediction")

df = load_housing_data()

trained_models, results = train_models(df)

tab1, tab2, tab3 = st.tabs([
    "📊 Dataset & Models",
    "🏠 House Details",
    "🔮 Prediction"
])

with tab1:
    selected_model = show_dataset_and_models(
        df,
        results,
        trained_models
    )

with tab2:
    house_details = get_house_details()

with tab3:
    show_prediction(
        trained_models[selected_model],
        selected_model,
        house_details
    )