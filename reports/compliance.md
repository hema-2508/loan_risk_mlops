# Compliance Report

## Security Measures

- Docker image scanned using Trivy/Docker Scout.
- API secrets stored using GitHub Secrets.
- Environment variables stored in `.env`.
- `.env` excluded from Git using `.gitignore`.
- No credentials committed to the repository.

## Sensitive Data Handling

- Loan dataset processed locally.
- No sensitive personal information stored in source code.
- Model and data versioned using Git and DVC.