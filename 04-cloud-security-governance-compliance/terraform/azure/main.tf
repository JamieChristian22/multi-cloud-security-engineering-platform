terraform {
  required_version = ">= 1.6.0"
  required_providers { azurerm = { source = "hashicorp/azurerm", version = "~> 3.100" } }
}
provider "azurerm" { features {} }

resource "azurerm_resource_group" "governance" {
  name = var.resource_group_name
  location = var.location
  tags = {
    Environment = "Production"
    Owner = "CloudSecurity"
    Project = "ComplianceGovernance"
    Compliance = "Required"
    CostCenter = "CC-1001"
  }
}
