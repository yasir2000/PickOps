#!/usr/bin/env bash
# Universal stop script for all PickOps stacks

set -euo pipefail

# Source common functions
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
if [ -f "${SCRIPT_DIR}/../../scripts/common.sh" ]; then
    source "${SCRIPT_DIR}/../../scripts/common.sh"
fi

# Get stack name from directory
STACK_NAME=$(basename "$(pwd)")

echo -e "${GREEN}================================${NC}"
echo -e "${GREEN}Stopping ${STACK_NAME} Stack${NC}"
echo -e "${GREEN}================================${NC}"

# Stop services
stop_services

echo -e "${GREEN}${STACK_NAME} Stack Stopped!${NC}"
