import json
import joblib
import pandas as pd

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)

# Load test data
X_test = pd.read_csv("data/processed/X_test.csv")
y_test = pd.read_csv("data/processed/y_test.csv").values.ravel()

# Load trained model
model = joblib.load("models/model.pkl")

# Prediction
prediction = model.predict(X_test)

metrics = {
    "accuracy": accuracy_score(y_test, prediction),
    "precision": precision_score(y_test, prediction),
    "recall": recall_score(y_test, prediction),
    "f1_score": f1_score(y_test, prediction)
}

with open("metrics.json", "w") as f:
    json.dump(metrics, f, indent=4)

print(metrics)