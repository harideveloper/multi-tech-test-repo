FROM python:3.10-slim

WORKDIR /app

COPY backend/requirements.txt .
RUN pip install -r requirements.txt

COPY backend .

# BUG: Port conflict - using common port 8080
EXPOSE 8080
CMD ["python", "app.py"]
