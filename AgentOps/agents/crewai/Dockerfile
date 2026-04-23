FROM python:3.12-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl git docker-cli \
    && rm -rf /var/lib/apt/lists/*

COPY ../../agents/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir crewai crewai-tools langchain langchain-community langchain-openai redis psycopg2-binary python-dotenv structlog

COPY . /app/crewai/

ENV PYTHONPATH=/app
CMD ["python", "-u", "crewai/ops_team.py"]
