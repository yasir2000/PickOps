.PHONY: help setup start stop restart logs ps clean backup restore update health

# Default target
.DEFAULT_GOAL := help

# Stack name (override with: make start STACK=llmops)
STACK ?= llmops

# Colors
GREEN  := $(shell tput -Txterm setaf 2)
YELLOW := $(shell tput -Txterm setaf 3)
BLUE   := $(shell tput -Txterm setaf 4)
RESET  := $(shell tput -Txterm sgr0)

## help: Show this help message
help:
	@echo 'Usage:'
	@echo '  ${YELLOW}make${RESET} ${GREEN}<target>${RESET} ${BLUE}[STACK=<stack-name>]${RESET}'
	@echo ''
	@echo 'Targets:'
	@awk 'BEGIN {FS = ":.*##"; printf "\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  ${GREEN}%-15s${RESET} %s\n", $$1, $$2 } /^##@/ { printf "\n${YELLOW}%s${RESET}\n", substr($$0, 5) } ' $(MAKEFILE_LIST)
	@echo ''
	@echo 'Available Stacks:'
	@echo '  llmops, devops, genaiops, agentops, ragops, mlops,'
	@echo '  secops, devsecops, aiops, iotops, blockchain, web3,'
	@echo '  dataops, finops, awsops, lambdaops, azureops, itops,'
	@echo '  webops, wasmops, gitops, appops, sagaops, eventops, dddops,'
	@echo '  almops, servicemeshops, datameshops, microservicesops,'
	@echo '  govops, agriops, poliops, muniops, transops, airops,'
	@echo '  aviops, mariops, logiops, mediops, healthops, drugops,'
	@echo '  eduops, landops, realops, homeops, socioops, civilops,'
	@echo '  waterops, enerops, autoops, enterops, technoops, commops,'
	@echo '  servops, petops, wearops, manuops, foodops, farmops,'
	@echo '  poultryops, dairyops, fishops, taxops, bankops, bizops,'
	@echo '  animops, constops, archiops, qualiops, interops, tradeops,'
	@echo '  workops, pubops, foresops, defops, spaceops, loveops,'
	@echo '  hygenops, machiops, chemiops, sciops, researops, furnops,'
	@echo '  electops, retaiops, wastops, kidsops, elderops, reliops,'
	@echo '  humanops, sporops, psychops, musicops, moneyops, codeops,'
	@echo '  womenops, nationops, compops, lawops'
	@echo ''
	@echo 'Examples:'
	@echo '  ${YELLOW}make start STACK=llmops${RESET}'
	@echo '  ${YELLOW}make logs STACK=devops${RESET}'
	@echo '  ${YELLOW}make backup STACK=mlops${RESET}'

##@ Setup

## setup: Initial setup for all stacks
setup:
	@echo "${GREEN}Setting up PickOps...${RESET}"
	@./scripts/setup-all.sh

## init: Initialize a specific stack
init:
	@echo "${GREEN}Initializing $(STACK)...${RESET}"
	@./manage.sh $(STACK) init

##@ Stack Management

## start: Start a stack
start:
	@echo "${GREEN}Starting $(STACK)...${RESET}"
	@./manage.sh $(STACK) start

## stop: Stop a stack
stop:
	@echo "${YELLOW}Stopping $(STACK)...${RESET}"
	@./manage.sh $(STACK) stop

## restart: Restart a stack
restart:
	@echo "${YELLOW}Restarting $(STACK)...${RESET}"
	@./manage.sh $(STACK) restart

## logs: View stack logs
logs:
	@./manage.sh $(STACK) logs

## ps: Show running containers
ps:
	@./manage.sh $(STACK) ps

##@ Maintenance

## pull: Pull latest images
pull:
	@echo "${BLUE}Pulling latest images for $(STACK)...${RESET}"
	@./manage.sh $(STACK) pull

## build: Build custom images
build:
	@echo "${BLUE}Building images for $(STACK)...${RESET}"
	@./manage.sh $(STACK) build

## update: Update and restart stack
update:
	@echo "${BLUE}Updating $(STACK)...${RESET}"
	@./manage.sh $(STACK) update

## health: Check stack health
health:
	@./manage.sh $(STACK) health

##@ Data Management

## backup: Create backup
backup:
	@echo "${GREEN}Creating backup for $(STACK)...${RESET}"
	@./manage.sh $(STACK) backup

## restore: Restore from backup (specify BACKUP_FILE)
restore:
	@echo "${YELLOW}Restoring $(STACK)...${RESET}"
	@./manage.sh $(STACK) restore $(BACKUP_FILE)

##@ Cleanup

## clean: Remove containers and volumes
clean:
	@echo "${YELLOW}Cleaning up $(STACK)...${RESET}"
	@./manage.sh $(STACK) clean

## prune: Remove all unused Docker resources
prune:
	@echo "${YELLOW}Pruning Docker resources...${RESET}"
	@docker system prune -a --volumes -f

##@ Multi-Stack Operations

## start-all: Start all stacks
start-all:
	@echo "${GREEN}Starting all stacks...${RESET}"
	@./manage.sh all start

## stop-all: Stop all stacks
stop-all:
	@echo "${YELLOW}Stopping all stacks...${RESET}"
	@./manage.sh all stop

## update-all: Update all stacks
update-all:
	@echo "${BLUE}Updating all stacks...${RESET}"
	@./manage.sh all update

## health-all: Check health of all stacks
health-all:
	@echo "${BLUE}Checking health of all stacks...${RESET}"
	@./manage.sh all health

##@ Development

## shell: Open shell in stack container
shell:
	@docker-compose -f $(STACK)/docker-compose.yml exec $(SERVICE) /bin/bash

## test: Run tests (if available)
test:
	@echo "${BLUE}Running tests for $(STACK)...${RESET}"
	@cd $(STACK) && ./scripts/test.sh 2>/dev/null || echo "No tests configured"

##@ Information

## version: Show Docker and compose versions
version:
	@echo "${BLUE}Docker version:${RESET}"
	@docker --version
	@echo "${BLUE}Docker Compose version:${RESET}"
	@docker-compose --version

## list: List all available stacks
list:
	@echo "${GREEN}Available PickOps Stacks:${RESET}"
	@ls -d */ | grep -v scripts | sed 's|/||'
