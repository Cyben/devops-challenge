## Overview

This project was built as part of a DevOps challenge, codenamed **thedoctor**. It demonstrates the ability to securely extract secrets from AWS DynamoDB and expose them through a Dockerized Flask API with CI/CD via GitHub Actions.

---

## Project Structure

```
.
├── app/  
│ ├── requirements.txt # Python dependencies  
│ └── main.py # Flask app with /secret and /health routes  
├── tests/  
│ └── test_app.py # Unit tests using pytest + monkeypatch
├── .env # AWS credentials and config (excluded from git)
├── Dockerfile # Builds the Flask app image
├── docker-compose.yml # Simplifies local testing
├── .github/workflows/ci.yml # GitHub Actions workflow (tests + build + push)
├── TROUBLE.md # Described difficulties
├── INSTRUCTIONS.md # Running and testing instructions
└── SUMMARY.md # This file
```

## Development Steps

### 1. Set up the Flask App

- Created `main.py` with two endpoints: `/secret` and `/health`

### 2. DynamoDB Integration

- Used `boto3` to query a specific DynamoDB table (`devops-challenge`)

### 3. Testing

- Wrote tests with `pytest` and `monkeypatch` to mock `boto3.resource()`
- Verified success and failure scenarios for both endpoints

### 4. Containerization

- Wrote a `Dockerfile` to package the app
- Used `docker-compose.yml` to load `.env` and run locally with a single command

### 5. CI/CD

- Switched from TravisCI to **GitHub Actions**
- Created `.github/workflows/ci.yml`:
  - Runs tests on every push to `master`
  - Builds and pushes Docker image to Docker Hub on success