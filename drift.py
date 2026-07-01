import numpy as np

# Compatibility patch for Evidently 0.4.16 with NumPy 2.x
if not hasattr(np, "float_"):
    np.float_ = np.float64

if not hasattr(np, "int_"):
    np.int_ = np.int64

if not hasattr(np, "complex_"):
    np.complex_ = np.complex128

if not hasattr(np, "bool_"):
    np.bool_ = bool

import pandas as pd
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset

# Load datasets
reference = pd.read_csv("data/raw/loan.csv")
current = pd.read_csv("data/raw/loan.csv")

# Create drift report
report = Report(metrics=[DataDriftPreset()])

# Run report
report.run(
    reference_data=reference,
    current_data=current,
)

# Save report
report.save_html("drift_report.html")

print("Drift report generated successfully.")