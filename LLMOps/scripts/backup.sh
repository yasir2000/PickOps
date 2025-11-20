#!/usr/bin/env bash

set -euo pipefail

BACKUP_DIR="./backups"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_FILE="${BACKUP_DIR}/llmops_backup_${TIMESTAMP}.tar.gz"

mkdir -p "${BACKUP_DIR}"

echo "Creating backup: ${BACKUP_FILE}"

# Stop services
docker-compose stop

# Backup volumes
docker run --rm \
  -v llmops_mlflow_data:/mlflow \
  -v llmops_qdrant_storage:/qdrant \
  -v "$(pwd)/${BACKUP_DIR}":/backup \
  alpine tar czf "/backup/llmops_backup_${TIMESTAMP}.tar.gz" /mlflow /qdrant

# Start services
docker-compose start

echo "Backup completed: ${BACKUP_FILE}"
