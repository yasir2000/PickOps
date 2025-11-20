#!/usr/bin/env bash

set -euo pipefail

GREEN='\033[0;32m'
NC='\033[0m'

echo -e "${GREEN}Stopping LLMOps Stack...${NC}"

docker-compose down

echo -e "${GREEN}LLMOps Stack stopped successfully!${NC}"
