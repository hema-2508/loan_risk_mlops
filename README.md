# Loan Risk Prediction MLOps Pipeline

## Project Overview

This project demonstrates an end-to-end MLOps pipeline for Loan Risk Prediction using modern DevOps and MLOps tools.

The pipeline automates data preprocessing, model training, evaluation, deployment, monitoring, CI/CD automation, and security validation.

---

## Technologies Used

- Python
- Scikit-Learn
- DVC
- MLflow
- FastAPI
- Docker
- GitHub Actions
- Prometheus
- Evidently AI
- Trivy
- Git

---

## Project Structure

```
loan-risk-mlops/
│
├── data/
├── models/
├── reports/
├── src/
│   ├── preprocess.py
│   ├── train.py
│   ├── evaluate.py
│   └── app.py
│
├── .github/workflows/
├── Dockerfile
├── dvc.yaml
├── params.yaml
├── requirements.txt
├── README.md
```

---

## Workflow

1. Data Ingestion
2. Data Preprocessing
3. Model Training
4. Model Evaluation
5. MLflow Experiment Tracking
6. Docker Deployment
7. FastAPI Prediction Service
8. GitHub Actions CI/CD
9. Monitoring using Prometheus
10. Drift Detection using Evidently AI
11. Security Scan using Trivy

---

## API Endpoints

GET /

Returns application status.

POST /predict

Returns Loan Approval Prediction.

GET /metrics

Returns Prometheus Metrics.

---

## Docker

Build

```
docker build -t loan-risk-api .
```

Run

```
docker run -d -p 8000:8000 --name loan-api loan-risk-api
```

---

## CI/CD

GitHub Actions automatically

- installs dependencies
- runs tests
- builds Docker image

---

## Monitoring

Prometheus metrics are available at

```
http://localhost:8000/metrics
```

---

## Security

- GitHub Secrets
- Trivy Scan
- .env ignored

---

