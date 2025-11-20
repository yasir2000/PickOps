"""
Azure Resource Deployment with Terraform
Demonstrates: Infrastructure as Code, Azure resources, Terraform automation
"""

import os
import subprocess
import json
from typing import Dict, List

class AzureTerraformDeployer:
    """Deploy Azure infrastructure using Terraform"""

    def __init__(self, workspace_dir: str = "./terraform"):
        self.workspace_dir = workspace_dir
        os.makedirs(workspace_dir, exist_ok=True)

    def generate_terraform_config(self):
        """Generate Terraform configuration files"""

        print("📝 Generating Terraform configuration...")

        # Main configuration
        main_tf = """
terraform {
  required_version = ">= 1.0"

  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
  }
}

provider "azurerm" {
  features {}
}

# Resource Group
resource "azurerm_resource_group" "main" {
  name     = var.resource_group_name
  location = var.location

  tags = var.tags
}

# Virtual Network
resource "azurerm_virtual_network" "main" {
  name                = "${var.prefix}-vnet"
  address_space       = ["10.0.0.0/16"]
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name

  tags = var.tags
}

# Subnet
resource "azurerm_subnet" "main" {
  name                 = "${var.prefix}-subnet"
  resource_group_name  = azurerm_resource_group.main.name
  virtual_network_name = azurerm_virtual_network.main.name
  address_prefixes     = ["10.0.1.0/24"]
}

# Storage Account
resource "azurerm_storage_account" "main" {
  name                     = "${var.prefix}storage${random_string.suffix.result}"
  resource_group_name      = azurerm_resource_group.main.name
  location                 = azurerm_resource_group.main.location
  account_tier             = "Standard"
  account_replication_type = "LRS"

  tags = var.tags
}

# App Service Plan
resource "azurerm_service_plan" "main" {
  name                = "${var.prefix}-asp"
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name
  os_type             = "Linux"
  sku_name            = "B1"

  tags = var.tags
}

# Web App
resource "azurerm_linux_web_app" "main" {
  name                = "${var.prefix}-webapp-${random_string.suffix.result}"
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name
  service_plan_id     = azurerm_service_plan.main.id

  site_config {
    application_stack {
      python_version = "3.9"
    }
  }

  app_settings = {
    "WEBSITES_PORT" = "8000"
  }

  tags = var.tags
}

# Random string for unique names
resource "random_string" "suffix" {
  length  = 6
  special = false
  upper   = false
}
"""

        # Variables
        variables_tf = """
variable "resource_group_name" {
  description = "Name of the resource group"
  type        = string
  default     = "rg-terraform-demo"
}

variable "location" {
  description = "Azure region"
  type        = string
  default     = "eastus"
}

variable "prefix" {
  description = "Prefix for resource names"
  type        = string
  default     = "demo"
}

variable "tags" {
  description = "Tags to apply to resources"
  type        = map(string)
  default = {
    Environment = "Development"
    ManagedBy   = "Terraform"
    Project     = "AzureOps"
  }
}
"""

        # Outputs
        outputs_tf = """
output "resource_group_name" {
  value = azurerm_resource_group.main.name
}

output "webapp_url" {
  value = "https://${azurerm_linux_web_app.main.default_hostname}"
}

output "storage_account_name" {
  value = azurerm_storage_account.main.name
}

output "virtual_network_id" {
  value = azurerm_virtual_network.main.id
}
"""

        # Write files
        with open(f"{self.workspace_dir}/main.tf", 'w') as f:
            f.write(main_tf.strip())

        with open(f"{self.workspace_dir}/variables.tf", 'w') as f:
            f.write(variables_tf.strip())

        with open(f"{self.workspace_dir}/outputs.tf", 'w') as f:
            f.write(outputs_tf.strip())

        print("✅ Terraform files generated")

    def run_command(self, command: List[str], capture_output: bool = True) -> Dict:
        """Run terraform command"""

        result = subprocess.run(
            command,
            cwd=self.workspace_dir,
            capture_output=capture_output,
            text=True
        )

        return {
            'returncode': result.returncode,
            'stdout': result.stdout,
            'stderr': result.stderr
        }

    def terraform_init(self):
        """Initialize Terraform"""

        print("\n🔧 Running terraform init...")
        result = self.run_command(['terraform', 'init'])

        if result['returncode'] == 0:
            print("✅ Terraform initialized")
        else:
            print(f"❌ Init failed: {result['stderr']}")
            raise Exception("Terraform init failed")

    def terraform_plan(self) -> str:
        """Run terraform plan"""

        print("\n📋 Running terraform plan...")
        result = self.run_command(['terraform', 'plan', '-out=tfplan'])

        if result['returncode'] == 0:
            print("✅ Plan created")
            print("\nPlan output:")
            print(result['stdout'][-1000:])  # Last 1000 chars
            return "tfplan"
        else:
            print(f"❌ Plan failed: {result['stderr']}")
            raise Exception("Terraform plan failed")

    def terraform_apply(self, plan_file: str = None):
        """Apply terraform configuration"""

        print("\n🚀 Running terraform apply...")

        cmd = ['terraform', 'apply']
        if plan_file:
            cmd.extend([plan_file])
        else:
            cmd.extend(['-auto-approve'])

        result = self.run_command(cmd, capture_output=False)

        if result['returncode'] == 0:
            print("\n✅ Infrastructure deployed!")
        else:
            print(f"\n❌ Apply failed")
            raise Exception("Terraform apply failed")

    def terraform_output(self) -> Dict:
        """Get terraform outputs"""

        print("\n📊 Getting outputs...")
        result = self.run_command(['terraform', 'output', '-json'])

        if result['returncode'] == 0:
            outputs = json.loads(result['stdout'])

            print("\nOutputs:")
            for key, value in outputs.items():
                print(f"  {key}: {value['value']}")

            return outputs
        else:
            print("❌ Failed to get outputs")
            return {}

    def terraform_destroy(self):
        """Destroy infrastructure"""

        print("\n🗑️  Running terraform destroy...")
        result = self.run_command(
            ['terraform', 'destroy', '-auto-approve'],
            capture_output=False
        )

        if result['returncode'] == 0:
            print("\n✅ Infrastructure destroyed")
        else:
            print("\n❌ Destroy failed")

def main():
    """Run Azure Terraform deployment demo"""

    print("☁️  Azure Terraform Deployment")
    print("=" * 60)

    deployer = AzureTerraformDeployer()

    try:
        # Generate config
        deployer.generate_terraform_config()

        # Initialize
        deployer.terraform_init()

        # Plan
        plan_file = deployer.terraform_plan()

        # Ask for confirmation
        print("\n" + "=" * 60)
        response = input("Apply this plan? (yes/no): ")

        if response.lower() == 'yes':
            # Apply
            deployer.terraform_apply(plan_file)

            # Get outputs
            outputs = deployer.terraform_output()

            # Summary
            print("\n" + "=" * 60)
            print("📊 Deployment Summary")
            print("=" * 60)

            if outputs:
                webapp_url = outputs.get('webapp_url', {}).get('value', 'N/A')
                rg_name = outputs.get('resource_group_name', {}).get('value', 'N/A')

                print(f"\nResource Group: {rg_name}")
                print(f"Web App URL: {webapp_url}")
                print("\n✅ Infrastructure ready!")

                # Ask about cleanup
                print("\n" + "=" * 60)
                cleanup = input("Destroy infrastructure? (yes/no): ")

                if cleanup.lower() == 'yes':
                    deployer.terraform_destroy()
        else:
            print("\n⏸️  Deployment cancelled")

    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        print("\n⚠️  Make sure:")
        print("   1. Terraform is installed: terraform --version")
        print("   2. Azure CLI is installed: az --version")
        print("   3. You're logged in: az login")

if __name__ == "__main__":
    # Install: pip install (no dependencies needed)
    # Prerequisites: terraform, az cli
    main()
