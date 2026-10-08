import streamlit as st


def get_house_details():

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

    return {
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
    }