#!/usr/bin/env bash
# Common utility functions for PickOps stacks

set -euo pipefail

# Colors
export RED='\033[0;31m'
export GREEN='\033[0;32m'
export YELLOW='\033[1;33m'
export BLUE='\033[0;34m'
export NC='\033[0m' # No Color

# Logging functions
log_info() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

log_warn() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

log_debug() {
    if [ "${DEBUG:-0}" = "1" ]; then
        echo -e "${BLUE}[DEBUG]${NC} $1"
    fi
}

# Check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Check prerequisites
check_prerequisites() {
    log_info "Checking prerequisites..."

    if ! command_exists docker; then
        log_error "Docker is not installed"
        exit 1
    fi

    if ! command_exists docker-compose; then
        log_error "Docker Compose is not installed"
        exit 1
    fi

    if ! docker info >/dev/null 2>&1; then
        log_error "Docker daemon is not running"
        exit 1
    fi

    log_info "All prerequisites met"
}

# Check if .env exists
check_env_file() {
    if [ ! -f .env ]; then
        log_warn "No .env file found"
        if [ -f .env.example ]; then
            log_info "Creating .env from .env.example"
            cp .env.example .env
            log_warn "Please edit .env file with your configuration"
            return 1
        else
            log_error "No .env.example file found"
            exit 1
        fi
    fi
    return 0
}

# Wait for service to be healthy
wait_for_service() {
    local service=$1
    local url=$2
    local max_attempts=${3:-30}
    local attempt=1

    log_info "Waiting for $service to be ready..."

    while [ $attempt -le $max_attempts ]; do
        if curl -sf "$url" > /dev/null 2>&1; then
            log_info "$service is ready"
            return 0
        fi

        log_debug "Attempt $attempt/$max_attempts failed, retrying in 5s..."
        sleep 5
        ((attempt++))
    done

    log_error "$service failed to start after $max_attempts attempts"
    return 1
}

# Create directories
create_directories() {
    local dirs=("$@")
    for dir in "${dirs[@]}"; do
        if [ ! -d "$dir" ]; then
            mkdir -p "$dir"
            log_info "Created directory: $dir"
        fi
    done
}

# Pull latest images
pull_images() {
    log_info "Pulling latest images..."
    docker-compose pull
}

# Start services
start_services() {
    log_info "Starting services..."
    docker-compose up -d
}

# Stop services
stop_services() {
    log_info "Stopping services..."
    docker-compose down
}

# Restart services
restart_services() {
    stop_services
    start_services
}

# Show service logs
show_logs() {
    local service=${1:-}
    if [ -z "$service" ]; then
        docker-compose logs -f
    else
        docker-compose logs -f "$service"
    fi
}

# Check service health
check_health() {
    log_info "Checking service health..."
    docker-compose ps
}

# Cleanup volumes
cleanup_volumes() {
    log_warn "This will remove all volumes and data!"
    read -p "Are you sure? (yes/no): " confirm
    if [ "$confirm" = "yes" ]; then
        docker-compose down -v
        log_info "Volumes cleaned up"
    else
        log_info "Cleanup cancelled"
    fi
}

# Backup data
backup_data() {
    local backup_dir="./backups"
    local timestamp=$(date +%Y%m%d_%H%M%S)
    local backup_file="${backup_dir}/backup_${timestamp}.tar.gz"

    create_directories "$backup_dir"

    log_info "Creating backup: $backup_file"

    # Stop services
    docker-compose stop

    # Create backup
    docker-compose run --rm \
        -v "$(pwd)/data:/source" \
        -v "$(pwd)/${backup_dir}:/backup" \
        alpine tar czf "/backup/backup_${timestamp}.tar.gz" -C /source .

    # Start services
    docker-compose start

    log_info "Backup completed: $backup_file"
}

# Restore data
restore_data() {
    local backup_file=$1

    if [ ! -f "$backup_file" ]; then
        log_error "Backup file not found: $backup_file"
        exit 1
    fi

    log_warn "This will replace existing data!"
    read -p "Are you sure? (yes/no): " confirm
    if [ "$confirm" != "yes" ]; then
        log_info "Restore cancelled"
        return
    fi

    log_info "Restoring from: $backup_file"

    # Stop services
    docker-compose stop

    # Restore backup
    docker-compose run --rm \
        -v "$(pwd)/data:/target" \
        -v "$(pwd)/$(dirname "$backup_file"):/backup" \
        alpine sh -c "rm -rf /target/* && tar xzf /backup/$(basename "$backup_file") -C /target"

    # Start services
    docker-compose start

    log_info "Restore completed"
}

# Export functions
export -f log_info log_warn log_error log_debug
export -f command_exists check_prerequisites check_env_file
export -f wait_for_service create_directories
export -f pull_images start_services stop_services restart_services
export -f show_logs check_health cleanup_volumes
export -f backup_data restore_data
