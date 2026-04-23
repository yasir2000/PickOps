FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir pyautogen langchain langchain-openai redis python-dotenv structlog

COPY . /app/autogen/

ENV PYTHONPATH=/app
CMD ["python", "-u", "autogen/ops_group_chat.py"]
