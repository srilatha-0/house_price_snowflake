import pandas as pd
import streamlit as st


def show_prediction(model, selected_model, house_details):

    st.subheader("🔮 House Price Prediction")

    st.write(
        f"Selected Model: **{selected_model}**"
    )

    if st.button(
        "Predict Price",
        use_container_width=True
    ):

        input_data = pd.DataFrame([house_details])

        prediction = model.predict(input_data)[0]

        st.success(
            f"🏠 Estimated House Price: ₹{prediction:,.0f}"
        )