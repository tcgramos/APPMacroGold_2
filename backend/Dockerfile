FROM python:3.12-slim
WORKDIR ./backend/app
COPY pyproject.toml ./backend/app/
RUN pip install --no-cache-dir fastapi uvicorn[standard] pydantic-settings sqlalchemy psycopg[binary] redis celery pandas numpy httpx
COPY app ./backend/app/
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
