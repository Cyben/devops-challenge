# INSTRUCTIONS.md

Welcome to the **thedoctor** DevOps challenge project!

This guide will walk you through cloning, running, testing, and deploying the app locally or in CI/CD.

## 🔧 Requirements

- Docker & Docker Compose installed
- Python 3.11+ (for local testing)
- GitHub account (if you're testing GitHub Actions)
- `.env` file with AWS credentials and parameters

## 📦 Setup

1. **Clone the repository**

```bash
git clone https://github.com/Cyben/devops-challenge.git
cd devops-challenge/thedoctor
```

2. **Create a .env file at the root of the project**

```env
AWS_ACCESS_KEY_ID=your-access-key
AWS_SECRET_ACCESS_KEY=your-secret-key
AWS_REGION=eu-west-1
CODE_NAME=thedoctor
```
> ✅ Make sure .env is listed in .gitignore so secrets are not committed.


## 🚀 Run the App Locally (Docker Compose)

```bash
docker-compose up
```

This will:
- Load environment variables from .env
- Build the Docker container
- Expose the Flask app on: http://localhost:5000

Test the endpoints:
- GET /secret → { "secret_code": "..." }
- GET /health → { status, container, project }

## 🧪 Run Tests Locally

```bash
pip install -r requirements.txt
pip install pytest
pytest thedoctor/test
```