FROM python:3.11

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY app.py .

EXPOSE 8080

CMD ["opentelemetry-instrument", "--service_name", "backendpython","uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
