 
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
