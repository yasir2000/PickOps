#!/usr/bin/env bash
# Quick setup script for all PickOps stacks

set -euo pipefail

echo "PickOps Quick Setup"
echo "==================="
echo ""
echo "This script will set up all PickOps stacks with default configurations."
echo ""

# Array of all stacks
STACKS=(
    "LLMOps"
    "DevOps"
    "GenAIOps"
    "AgentOps"
    "RAGOps"
    "MLOps"
    "SecOps"
    "DevSecOps"
    "AIOps"
    "IoTOps"
    "BlockchainOps"
    "Web3Ops"
    "DataOps"
    "FinOps"
    "AWSOps"
    "LambdaOps"
    "AzureOps"
    "ITOps"
)

# Function to setup a stack
setup_stack() {
    local stack=$1
    echo ""
    echo "Setting up $stack..."

    if [ -d "$stack" ]; then
        cd "$stack"

        # Copy .env.example to .env if it doesn't exist
        if [ -f ".env.example" ] && [ ! -f ".env" ]; then
            cp .env.example .env
            echo "  ✓ Created .env file"
        fi

        # Create necessary directories
        mkdir -p data logs configs scripts
        echo "  ✓ Created directories"

        # Make scripts executable
        if [ -d "scripts" ]; then
            chmod +x scripts/*.sh 2>/dev/null || true
            echo "  ✓ Made scripts executable"
        fi

        cd ..
    else
        echo "  ✗ Directory not found: $stack"
    fi
}

# Ask user which stacks to setup
echo "Available stacks:"
for i in "${!STACKS[@]}"; do
    echo "  $((i+1)). ${STACKS[$i]}"
done
echo ""
echo "Options:"
echo "  - Enter stack numbers (e.g., 1 2 3)"
echo "  - Enter 'all' to setup all stacks"
echo "  - Press Enter to exit"
echo ""
read -p "Select stacks: " selection

if [ -z "$selection" ]; then
    echo "Setup cancelled"
    exit 0
fi

if [ "$selection" = "all" ]; then
    for stack in "${STACKS[@]}"; do
        setup_stack "$stack"
    done
else
    for num in $selection; do
        if [ "$num" -ge 1 ] && [ "$num" -le "${#STACKS[@]}" ]; then
            setup_stack "${STACKS[$((num-1))]}"
        else
            echo "Invalid selection: $num"
        fi
    done
fi

echo ""
echo "Setup complete!"
echo ""
echo "Next steps:"
echo "  1. Edit .env files in each stack directory"
echo "  2. Run: cd <StackName> && ./scripts/start.sh"
echo "  3. Check README.md in each stack for details"
