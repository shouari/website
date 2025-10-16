FROM python:3.11-slim

WORKDIR /app

# Installe les dépendances système nécessaires
RUN apt-get update && apt-get install -y \
    unzip \
    curl \
    gnupg \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Installe bun manuellement
RUN curl -fsSL https://bun.sh/install | bash

# Ajoute bun au PATH
ENV PATH="/root/.bun/bin:$PATH"

# Copie ton projet dans le conteneur
COPY . .

# Installe Reflex
RUN pip install --no-cache-dir -r requirements.txt


# Lance l'app
HOST
EXPOSE 3000

CMD ["reflex", "run", "--env", "prod", "--single-port", "--backend-host", "0.0.0.0"]
