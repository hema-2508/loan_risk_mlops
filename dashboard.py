import streamlit as st
import joblib
import pandas as pd

st.set_page_config(
    page_title="Loan Risk Prediction",
    page_icon="🏦",
    layout="centered"
)

st.title("🏦 Loan Risk Prediction Dashboard")

st.write("Enter the applicant details below.")

model = joblib.load("models/model.pkl")

gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["No", "Yes"])
dependents = st.selectbox("Dependents", [0, 1, 2, 3])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["No", "Yes"])

income = st.number_input("Applicant Income", 0.0, 100000.0, 5000.0)

co_income = st.number_input("Coapplicant Income", 0.0, 100000.0, 0.0)

loan_amount = st.number_input("Loan Amount", 0.0, 1000.0, 120.0)

loan_term = st.number_input("Loan Term", 0.0, 480.0, 360.0)

credit_history = st.selectbox("Credit History", [0, 1])

property_area = st.selectbox(
    "Property Area",
    ["Rural", "Semiurban", "Urban"]
)

gender = 1 if gender == "Male" else 0
married = 1 if married == "Yes" else 0
education = 1 if education == "Graduate" else 0
self_employed = 1 if self_employed == "Yes" else 0

property_map = {
    "Rural": 0,
    "Semiurban": 1,
    "Urban": 2
}

property_area = property_map[property_area]

if st.button("Predict Loan Status"):

    input_df = pd.DataFrame([{
        "Gender": gender,
        "Married": married,
        "Dependents": dependents,
        "Education": education,
        "Self_Employed": self_employed,
        "ApplicantIncome": income,
        "CoapplicantIncome": co_income,
        "LoanAmount": loan_amount,
        "Loan_Amount_Term": loan_term,
        "Credit_History": credit_history,
        "Property_Area": property_area
    }])

    prediction = model.predict(input_df)[0]

    if prediction == 1:
        st.success("✅ Loan Approved")
    else:
        st.error("❌ Loan Rejected")