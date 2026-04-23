FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir agentscope langchain redis psutil psycopg2-binary python-dotenv structlog

COPY . /app/agentscope/

ENV PYTHONPATH=/app
EXPOSE 12001
CMD ["python", "-u", "agentscope/ops_pipeline.py"]
