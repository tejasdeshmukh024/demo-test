FROM python:3.12-slim

WORKDIR /app

RUN useradd -m appuser && chown -R appuser:appuser /app

USER appuser

COPY --chown=appuser:appuser gist_fetcher.py .

RUN pip install --no-cache-dir requests

EXPOSE PORT 8080
CMD ["python", "gist_fetcher.py"]
