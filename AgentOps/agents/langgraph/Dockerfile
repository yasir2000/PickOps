FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir langgraph langchain langchain-core langchain-community langchain-openai fastapi uvicorn redis psycopg2-binary python-dotenv structlog

COPY . /app/langgraph/

ENV PYTHONPATH=/app
EXPOSE 8001
CMD ["uvicorn", "langgraph.ops_workflow:app", "--host", "0.0.0.0", "--port", "8001"]
