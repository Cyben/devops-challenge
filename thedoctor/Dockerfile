FROM python:3.11-slim

ENV APP_PATH=/app

WORKDIR /app
COPY ${APP_PATH}/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000

COPY ${APP_PATH} .
CMD ["python", "main.py"]
