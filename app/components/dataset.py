import pandas as pd
import streamlit as st


def show_dataset_and_models(df, results, trained_models):

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

    st.success(f"Selected Model: **{selected_model}**")

    return selected_model