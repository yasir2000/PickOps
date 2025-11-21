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
  almops, servicemeshops, datameshops, microservicesops,
  govops, agriops, poliops, muniops, transops, airops,
  aviops, mariops, logiops, mediops, healthops, drugops,
  eduops, landops, realops, homeops, socioops, civilops,
  waterops, enerops, autoops, enterops, technoops, commops,
  servops, petops, wearops, manuops, foodops, farmops,
  poultryops, dairyops, fishops, taxops, bankops, bizops,
  animops, constops, archaops, archiops, qualiops, interops, tradeops,
  workops, pubops, foresops, defops, spaceops, loveops,
  hygenops, machiops, chemiops, sciops, researops, furnops,
  electops, retaiops, wastops, kidsops, elderops, reliops,
  humanops, sporops, psychops, musicops, moneyops, codeops,
  womenops, nationops, compops, lawops

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
        govops) echo "GovOps" ;;
        agriops) echo "AgriOps" ;;
        poliops) echo "PoliOps" ;;
        muniops) echo "MuniOps" ;;
        transops) echo "TransOps" ;;
        airops) echo "AirOps" ;;
        aviops) echo "AviOps" ;;
        mariops) echo "MariOps" ;;
        logiops) echo "LogiOps" ;;
        mediops) echo "MediOps" ;;
        healthops) echo "HealthOps" ;;
        drugops) echo "DrugOps" ;;
        eduops) echo "EduOps" ;;
        landops) echo "LandOps" ;;
        realops) echo "RealOps" ;;
        homeops) echo "HomeOps" ;;
        socioops) echo "SocioOps" ;;
        civilops) echo "CivilOps" ;;
        waterops) echo "WaterOps" ;;
        enerops) echo "EnerOps" ;;
        autoops) echo "AutoOps" ;;
        enterops) echo "EnterOps" ;;
        technoops) echo "TechnoOps" ;;
        commops) echo "CommOps" ;;
        servops) echo "ServOps" ;;
        petops) echo "PetOps" ;;
        wearops) echo "WearOps" ;;
        manuops) echo "ManuOps" ;;
        foodops) echo "FoodOps" ;;
        farmops) echo "FarmOps" ;;
        poultryops) echo "PoultryOps" ;;
        dairyops) echo "DairyOps" ;;
        fishops) echo "FishOps" ;;
        taxops) echo "TaxOps" ;;
        bankops) echo "BankOps" ;;
        bizops) echo "BizOps" ;;
        animops) echo "AnimOps" ;;
        constops) echo "ConstOps" ;;
        archaops) echo "ArchaOps" ;;
        archiops) echo "ArchiOps" ;;
        qualiops) echo "QualiOps" ;;
        interops) echo "InterOps" ;;
        tradeops) echo "TradeOps" ;;
        workops) echo "WorkOps" ;;
        pubops) echo "PubOps" ;;
        foresops) echo "ForesOps" ;;
        defops) echo "DefOps" ;;
        spaceops) echo "SpaceOps" ;;
        loveops) echo "LoveOps" ;;
        hygenops) echo "HygenOps" ;;
        machiops) echo "MachiOps" ;;
        chemiops) echo "ChemiOps" ;;
        sciops) echo "SciOps" ;;
        researops) echo "ResearOps" ;;
        furnops) echo "FurnOps" ;;
        electops) echo "ElectOps" ;;
        retaiops) echo "RetaiOps" ;;
        wastops) echo "WastOps" ;;
        kidsops) echo "KidsOps" ;;
        elderops) echo "ElderOps" ;;
        reliops) echo "ReliOps" ;;
        humanops) echo "HumanOps" ;;
        sporops) echo "SporOps" ;;
        psychops) echo "PsychOps" ;;
        musicops) echo "MusicOps" ;;
        moneyops) echo "MoneyOps" ;;
        codeops) echo "CodeOps" ;;
        womenops) echo "WomenOps" ;;
        nationops) echo "NationOps" ;;
        compops) echo "CompOps" ;;
        lawops) echo "LawOps" ;;
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
