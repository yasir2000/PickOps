#!/usr/bin/env bash
# Universal start script for all PickOps stacks

set -euo pipefail

# Source common functions
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
if [ -f "${SCRIPT_DIR}/../../scripts/common.sh" ]; then
    source "${SCRIPT_DIR}/../../scripts/common.sh"
fi

# Get stack name from directory
STACK_NAME=$(basename "$(pwd)")

echo -e "${GREEN}================================${NC}"
echo -e "${GREEN}Starting ${STACK_NAME} Stack${NC}"
echo -e "${GREEN}================================${NC}"

# Check prerequisites
check_prerequisites

# Check environment file
if ! check_env_file; then
    exit 1
fi

# Create necessary directories
create_directories "data" "logs" "configs" "backups"

# Pull latest images
pull_images

# Start services
start_services

# Wait a bit for services to initialize
log_info "Waiting for services to initialize..."
sleep 10

# Check health
check_health

echo -e "${GREEN}================================${NC}"
echo -e "${GREEN}${STACK_NAME} Stack Started!${NC}"
echo -e "${GREEN}================================${NC}"
echo ""
log_info "Access points:"
echo "  - Check the README.md for service URLs"
echo "  - View logs: docker-compose logs -f"
echo "  - Stop stack: ./scripts/stop.sh"
