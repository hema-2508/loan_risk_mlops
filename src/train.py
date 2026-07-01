import os
import joblib
import yaml
import mlflow
import mlflow.sklearn
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

with open("params.yaml") as f:
    params = yaml.safe_load(f)

X_train = pd.read_csv("data/processed/X_train.csv")
X_test = pd.read_csv("data/processed/X_test.csv")
y_train = pd.read_csv("data/processed/y_train.csv").values.ravel()
y_test = pd.read_csv("data/processed/y_test.csv").values.ravel()

mlflow.set_experiment("Loan Risk Prediction")

with mlflow.start_run():

    model = RandomForestClassifier(
        n_estimators=params["model"]["n_estimators"],
        max_depth=params["model"]["max_depth"],
        random_state=params["model"]["random_state"],
    )

    model.fit(X_train, y_train)

    pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, pred)

    mlflow.log_param("n_estimators", params["model"]["n_estimators"])
    mlflow.log_param("max_depth", params["model"]["max_depth"])
    mlflow.log_metric("accuracy", accuracy)

    os.makedirs("models", exist_ok=True)

    joblib.dump(model, "models/model.pkl")

    mlflow.sklearn.log_model(
    sk_model=model,
    name="loan_model")

    print("Accuracy:", accuracy)