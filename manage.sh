#!/usr/bin/env bash
# Makefile alternative - Common operations for all stacks

set -euo pipefail

show_help() {
    cat << EOF
PickOps Management Script

Usage: ./manage.sh [STACK] [COMMAND]

Stacks:
  llmops, devops, genaiops, agentops, ragops, mlops,
  secops, devsecops, aiops, iotops, blockchain, web3,
  dataops, finops, awsops, lambdaops, azureops, itops,
  webops, wasmops, gitops, appops, sagaops, eventops, dddops,
  almops, servicemeshops, datameshops, microservicesops

Commands:
  start         Start the stack
  stop          Stop the stack
  restart       Restart the stack
  logs          Show logs (optionally specify service)
  ps            Show running containers
  pull          Pull latest images
  build         Build custom images
  health        Check service health
  backup        Create backup
  restore       Restore from backup
  clean         Remove containers and volumes
  update        Pull images and restart

Examples:
  ./manage.sh llmops start
  ./manage.sh devops logs jenkins
  ./manage.sh mlops backup
  ./manage.sh all pull

EOF
}

# Convert stack name to directory name
get_stack_dir() {
    case "${1,,}" in
        llmops) echo "LLMOps" ;;
        devops) echo "DevOps" ;;
        genaiops) echo "GenAIOps" ;;
        agentops) echo "AgentOps" ;;
        ragops) echo "RAGOps" ;;
        mlops) echo "MLOps" ;;
        secops) echo "SecOps" ;;
        devsecops) echo "DevSecOps" ;;
        aiops) echo "AIOps" ;;
        iotops) echo "IoTOps" ;;
        blockchain|blockchainops) echo "BlockchainOps" ;;
        web3|web3ops) echo "Web3Ops" ;;
        dataops) echo "DataOps" ;;
        finops) echo "FinOps" ;;
        awsops) echo "AWSOps" ;;
        lambdaops) echo "LambdaOps" ;;
        azureops) echo "AzureOps" ;;
        itops) echo "ITOps" ;;
        webops) echo "WebOps" ;;
        wasmops) echo "WASMOps" ;;
        gitops) echo "GitOps" ;;
        appops) echo "AppOps" ;;
        sagaops) echo "SagaOps" ;;
        eventops) echo "EventOps" ;;
        dddops) echo "DDDOps" ;;
        almops) echo "ALMOps" ;;
        servicemeshops) echo "ServiceMeshOps" ;;
        datameshops) echo "DataMeshOps" ;;
        microservicesops) echo "MicroservicesOps" ;;
        *) echo "" ;;
    esac
}

# Execute command in stack directory
exec_in_stack() {
    local stack_dir=$1
    local command=$2
    shift 2
    local args="$@"

    if [ ! -d "$stack_dir" ]; then
        echo "Error: Stack directory not found: $stack_dir"
        return 1
    fi

    cd "$stack_dir"

    case "$command" in
        start)
            docker-compose up -d
            ;;
        stop)
            docker-compose down
            ;;
        restart)
            docker-compose restart $args
            ;;
        logs)
            docker-compose logs -f $args
            ;;
        ps)
            docker-compose ps
            ;;
        pull)
            docker-compose pull
            ;;
        build)
            docker-compose build $args
            ;;
        health)
            docker-compose ps
            ;;
        backup)
            if [ -f "scripts/backup.sh" ]; then
                ./scripts/backup.sh
            else
                echo "Backup script not found"
            fi
            ;;
        restore)
            if [ -f "scripts/restore.sh" ]; then
                ./scripts/restore.sh $args
            else
                echo "Restore script not found"
            fi
            ;;
        clean)
            read -p "Remove all containers and volumes? (yes/no): " confirm
            if [ "$confirm" = "yes" ]; then
                docker-compose down -v
            fi
            ;;
        update)
            docker-compose pull
            docker-compose up -d
            ;;
        *)
            echo "Unknown command: $command"
            show_help
            return 1
            ;;
    esac

    cd - > /dev/null
}

# Main
if [ $# -lt 2 ]; then
    show_help
    exit 1
fi

STACK=$1
COMMAND=$2
shift 2
ARGS="$@"

if [ "$STACK" = "all" ]; then
    # Execute command for all stacks
    STACKS=(LLMOps DevOps GenAIOps AgentOps RAGOps MLOps SecOps DevSecOps AIOps IoTOps BlockchainOps Web3Ops DataOps FinOps AWSOps LambdaOps AzureOps ITOps)
    for stack_dir in "${STACKS[@]}"; do
        echo "=== $stack_dir ==="
        exec_in_stack "$stack_dir" "$COMMAND" $ARGS
        echo ""
    done
else
    STACK_DIR=$(get_stack_dir "$STACK")
    if [ -z "$STACK_DIR" ]; then
        echo "Error: Unknown stack: $STACK"
        show_help
        exit 1
    fi
    exec_in_stack "$STACK_DIR" "$COMMAND" $ARGS
fi
