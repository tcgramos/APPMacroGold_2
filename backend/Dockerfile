FROM python:3.12-slim

# Define o diretório de trabalho no container
WORKDIR /app

# Copia o pyproject.toml do diretório atual (backend) para o /app do container
COPY pyproject.toml .

# Copia a pasta 'app' do diretório atual (backend) para o /app do container
COPY app/ ./app/

RUN pip install --no-cache-dir fastapi uvicorn[standard] pydantic-settings sqlalchemy psycopg[binary] redis celery pandas numpy httpx

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
