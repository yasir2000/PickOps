#!/usr/bin/env bash
# Universal health check script for all PickOps stacks

set -euo pipefail

# Source common functions
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
if [ -f "${SCRIPT_DIR}/../../scripts/common.sh" ]; then
    source "${SCRIPT_DIR}/../../scripts/common.sh"
fi

STACK_NAME=$(basename "$(pwd)")

echo -e "${GREEN}Checking ${STACK_NAME} Stack Health${NC}"
echo ""

# Check container status
check_health

echo ""
log_info "To view logs: docker-compose logs -f [service-name]"
log_info "To restart: docker-compose restart [service-name]"
