import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("customer_churn.pkl")

st.title("Customer Churn Prediction")

# Inputs

# Gender
gender = st.selectbox("Gender", ["Female", "Male"])
gender = 0 if gender == "Female" else 1

# Senior Citizen
SeniorCitizen = st.selectbox("Senior Citizen", ["No", "Yes"])
SeniorCitizen = 0 if SeniorCitizen == "No" else 1

# Partner
Partner = st.selectbox("Partner", ["No", "Yes"])
Partner = 0 if Partner == "No" else 1

# Dependents
Dependents = st.selectbox("Dependents", ["No", "Yes"])
Dependents = 0 if Dependents == "No" else 1

# Tenure
tenure = st.number_input("Tenure", min_value=0)

# Phone Service
PhoneService = st.selectbox("Phone Service", ["No", "Yes"])
PhoneService = 0 if PhoneService == "No" else 1

# Multiple Lines
MultipleLines = st.selectbox("Multiple Lines", ["No phone service", "No", "Yes"])
MultipleLines = {
    "No phone service": 0,
    "No": 1,
    "Yes": 2
}[MultipleLines]

# Internet Service
InternetService = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
InternetService = {
    "DSL": 0,
    "Fiber optic": 1,
    "No": 2
}[InternetService]

# Online Security
OnlineSecurity = st.selectbox("Online Security", ["No internet service", "No", "Yes"])
OnlineSecurity = {
    "No internet service": 0,
    "No": 1,
    "Yes": 2
}[OnlineSecurity]

# Online Backup
OnlineBackup = st.selectbox("Online Backup", ["No internet service", "No", "Yes"])
OnlineBackup = {
    "No internet service": 0,
    "No": 1,
    "Yes": 2
}[OnlineBackup]

# Device Protection
DeviceProtection = st.selectbox("Device Protection", ["No internet service", "No", "Yes"])
DeviceProtection = {
    "No internet service": 0,
    "No": 1,
    "Yes": 2
}[DeviceProtection]

# Tech Support
TechSupport = st.selectbox("Tech Support", ["No internet service", "No", "Yes"])
TechSupport = {
    "No internet service": 0,
    "No": 1,
    "Yes": 2
}[TechSupport]

# Streaming TV
StreamingTV = st.selectbox("Streaming TV", ["No internet service", "No", "Yes"])
StreamingTV = {
    "No internet service": 0,
    "No": 1,
    "Yes": 2
}[StreamingTV]

# Streaming Movies
StreamingMovies = st.selectbox("Streaming Movies", ["No internet service", "No", "Yes"])
StreamingMovies = {
    "No internet service": 0,
    "No": 1,
    "Yes": 2
}[StreamingMovies]

# Contract
Contract = st.selectbox(
    "Contract",
    ["Month-to-month", "One year", "Two year"]
)
Contract = {
    "Month-to-month": 0,
    "One year": 1,
    "Two year": 2
}[Contract]

# Paperless Billing
PaperlessBilling = st.selectbox("Paperless Billing", ["No", "Yes"])
PaperlessBilling = 0 if PaperlessBilling == "No" else 1

# Payment Method
PaymentMethod = st.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)
PaymentMethod = {
    "Electronic check": 0,
    "Mailed check": 1,
    "Bank transfer (automatic)": 2,
    "Credit card (automatic)": 3
}[PaymentMethod]

# Monthly Charges
MonthlyCharges = st.number_input("Monthly Charges", min_value=0.0)

# Total Charges
TotalCharges = st.number_input("Total Charges", min_value=0.0)


if st.button("Predict"):

    data = pd.DataFrame({
        "gender":[gender],
        "SeniorCitizen":[SeniorCitizen],
        "Partner":[Partner],
        "Dependents":[Dependents],
        "tenure":[tenure],
        "PhoneService":[PhoneService],
        "MultipleLines":[MultipleLines],
        "InternetService":[InternetService],
        "OnlineSecurity":[OnlineSecurity],
        "OnlineBackup":[OnlineBackup],
        "DeviceProtection":[DeviceProtection],
        "TechSupport":[TechSupport],
        "StreamingTV":[StreamingTV],
        "StreamingMovies":[StreamingMovies],
        "Contract":[Contract],
        "PaperlessBilling":[PaperlessBilling],
        "PaymentMethod":[PaymentMethod],
        "MonthlyCharges":[MonthlyCharges],
        "TotalCharges":[TotalCharges],
        
    })

    prediction = model.predict(data)

    probability = model.predict_proba(data)

    if prediction[0] == 1:
        st.error("Customer is likely to Churn")
    else:
        st.success("Customer is not likely to Churn")

    st.write("Probability:", probability)