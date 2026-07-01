import logging
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
from prometheus_client import Counter, generate_latest
from fastapi.responses import Response

logging.basicConfig(
    filename="api.log",
    level=logging.INFO,
    format="%(asctime)s %(message)s"
)

app = FastAPI(
    title="Loan Risk Prediction API",
    version="1.0"
)

REQUEST_COUNT = Counter(
    "prediction_requests_total",
    "Total Prediction Requests"
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
    logging.info(f"Prediction request: {data}")

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
    REQUEST_COUNT.inc()

    prediction = model.predict(input_df)[0]

    return {
        "prediction": int(prediction),
        "result": "Approved" if prediction == 1 else "Rejected"
    }
logging.basicConfig(
    filename="api.log",
    level=logging.INFO,
    format="%(asctime)s %(message)s"
)
@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type="text/plain")