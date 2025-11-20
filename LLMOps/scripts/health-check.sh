#!/usr/bin/env bash

set -euo pipefail

GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'

echo "Checking LLMOps service health..."

check_service() {
    local service=$1
    local url=$2

    if curl -sf "$url" > /dev/null 2>&1; then
        echo -e "${GREEN}✓ $service is healthy${NC}"
        return 0
    else
        echo -e "${RED}✗ $service is not responding${NC}"
        return 1
    fi
}

# Check services
check_service "vLLM" "http://localhost:8000/health" || true
check_service "MLflow" "http://localhost:5000/health" || true
check_service "Qdrant" "http://localhost:6333/healthz" || true
check_service "Grafana" "http://localhost:3000/api/health" || true
check_service "Prometheus" "http://localhost:9090/-/healthy" || true

# Check containers
echo ""
echo "Container status:"
docker-compose ps
