# 🏠 House Price Prediction

A machine learning web application that predicts house prices using housing data stored in Snowflake. The application trains and compares multiple regression models and allows users to enter house details and get an estimated price.

## 🚀 Project Overview

This project uses Snowflake for data storage and Streamlit for the user interface.

The application:

1. Loads housing data from Snowflake.
2. Preprocesses numerical and categorical features.
3. Splits the data into training and testing sets.
4. Trains three machine learning models.
5. Compares the models using MAE, RMSE, and R².
6. Allows the user to select a model.
7. Predicts the estimated house price based on user input.

## 🤖 Machine Learning Models

The following models are trained and compared:

- Linear Regression
- Random Forest Regressor
- Gradient Boosting Regressor

### Evaluation Metrics

- **MAE** – Mean Absolute Error
- **RMSE** – Root Mean Squared Error
- **R²** – R-squared score

## 🗃️ Dataset

The housing dataset is stored in Snowflake.

The application uses the following features:

### Numerical Features

- Area
- Bedrooms
- Bathrooms
- Stories
- Parking

### Categorical Features

- Main Road
- Guest Room
- Basement
- Hot Water Heating
- Air Conditioning
- Preferred Area
- Furnishing Status

### Target

- Price

The dataset is not included in this repository.

## 🛠️ Technologies Used

- Python
- Snowflake
- Snowpark
- Streamlit
- Pandas
- Scikit-learn
- Git
- GitHub

## 📂 Project Structure

```text
house_price_snowflake/
│
├── app/
│   └── streamlit_app.py
│
├── README.md
├── requirements.txt
└── .gitignore