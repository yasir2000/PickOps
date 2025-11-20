#!/usr/bin/env bash

set -euo pipefail

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${GREEN}Starting LLMOps Stack...${NC}"

# Check if .env exists
if [ ! -f .env ]; then
    echo -e "${YELLOW}No .env file found. Creating from .env.example...${NC}"
    cp .env.example .env
    echo -e "${RED}Please edit .env file with your configuration before starting.${NC}"
    exit 1
fi

# Check for NVIDIA GPU
if ! command -v nvidia-smi &> /dev/null; then
    echo -e "${YELLOW}Warning: nvidia-smi not found. GPU services may not work.${NC}"
fi

# Create necessary directories
mkdir -p data logs configs/grafana/dashboards configs/grafana/datasources

# Pull latest images
echo -e "${GREEN}Pulling latest images...${NC}"
docker-compose pull

# Start services
echo -e "${GREEN}Starting services...${NC}"
docker-compose up -d

# Wait for services to be healthy
echo -e "${GREEN}Waiting for services to be ready...${NC}"
sleep 10

# Check health
./scripts/health-check.sh

echo -e "${GREEN}LLMOps Stack started successfully!${NC}"
echo -e "${GREEN}Access points:${NC}"
echo -e "  - vLLM API: http://localhost:8000"
echo -e "  - Text Gen Inference: http://localhost:8001"
echo -e "  - Ollama: http://localhost:11434"
echo -e "  - MLflow: http://localhost:5000"
echo -e "  - Qdrant: http://localhost:6333"
echo -e "  - Grafana: http://localhost:3000 (admin/admin)"
echo -e "  - Prometheus: http://localhost:9090"
