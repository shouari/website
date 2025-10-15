FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y unzip && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir reflex

RUN reflex export

CMD ["reflex", "run", "--production", "--port", "8080", "--host", "0.0.0.0"]
