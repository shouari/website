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

# Compile le site en mode production
RUN reflex export --env prod

# Lance l'app

EXPOSE 8080

CMD ["reflex", "run", "--env", "prod", "--single-port", "--backend-host", "0.0.0.0", "--backend-port", "8080"]

# This docker file is intended to be used with container hosting services
#
# After deploying this image, get the URL pointing to the backend service
# and run API_URL=https://path-to-my-container.example.com reflex export frontend
# then copy the contents of `frontend.zip` to your static file server (github pages, s3, etc).
#
# Azure Static Web App example:
#    npx @azure/static-web-apps-cli deploy --env production --app-location .web/build/client
#
# For dynamic routes to function properly, ensure that 404s are redirected to /404 on the
# static file host (for github pages, this works out of the box; remember to create .nojekyll).
#
# For azure static web apps, add `staticwebapp.config.json` to to `.web/build/client` with the following:
#  {
#     "responseOverrides": {
#        "404": {
#            "rewrite": "/404.html"
#        }
#     }
#  }
#
# Note: many container hosting platforms require amd64 images, so when building on an M1 Mac
# for example, pass `docker build --platform=linux/amd64 ...`

# Stage 1: init
FROM python:3.13 as init

ARG uv=/root/.local/bin/uv

# Install `uv` for faster package bootstrapping
ADD --chmod=755 https://astral.sh/uv/install.sh /install.sh
RUN /install.sh && rm /install.sh

# Copy local context to `/app` inside container (see .dockerignore)
WORKDIR /app
COPY . .
RUN mkdir -p /app/data /app/uploaded_files

# Create virtualenv which will be copied into final container
ENV VIRTUAL_ENV=/app/.venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN $uv venv

# Install app requirements and reflex inside virtualenv
RUN $uv pip install -r requirements.txt

# Deploy templates and prepare app
RUN reflex init

# Stage 2: copy artifacts into slim image 
FROM python:3.13-slim
WORKDIR /app
RUN adduser --disabled-password --home /app reflex
COPY --chown=reflex --from=init /app /app
# Install libpq-dev for psycopg (skip if not using postgres).
RUN apt-get update -y && apt-get install -y libpq-dev && rm -rf /var/lib/apt/lists/*
USER reflex
ENV PATH="/app/.venv/bin:$PATH" PYTHONUNBUFFERED=1

# Needed until Reflex properly passes SIGTERM on backend.
STOPSIGNAL SIGKILL

# Always apply migrations before starting the backend.
CMD [ -d alembic ] && reflex db migrate; \
    exec reflex run --env prod --backend-only --backend-port ${PORT:-8000}