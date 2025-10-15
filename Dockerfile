FROM python:3.13-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir reflex

RUN reflex export 

CMD ["reflex", "run", "--production", "--port", "8080", "--host", "0.0.0.0"]
