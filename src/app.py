from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI(
    title="Loan Risk Prediction API",
    version="1.0"
)

model = joblib.load("models/model.pkl")


class LoanData(BaseModel):
    Gender: int
    Married: int
    Dependents: int
    Education: int
    Self_Employed: int
    ApplicantIncome: float
    CoapplicantIncome: float
    LoanAmount: float
    Loan_Amount_Term: float
    Credit_History: float
    Property_Area: int


@app.get("/")
def home():
    return {"message": "Loan Risk Prediction API is running"}


@app.post("/predict")
def predict(data: LoanData):

    input_df = pd.DataFrame([data.model_dump()])

    # Ensure column order matches training
    input_df = input_df[
        [
            "Gender",
            "Married",
            "Dependents",
            "Education",
            "Self_Employed",
            "ApplicantIncome",
            "CoapplicantIncome",
            "LoanAmount",
            "Loan_Amount_Term",
            "Credit_History",
            "Property_Area",
        ]
    ]

    prediction = model.predict(input_df)[0]

    return {
        "prediction": int(prediction),
        "result": "Approved" if prediction == 1 else "Rejected"
    }