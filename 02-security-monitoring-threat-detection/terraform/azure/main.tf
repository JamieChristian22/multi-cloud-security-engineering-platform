terraform {
  required_version = ">= 1.6.0"
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.100"
    }
  }
}

provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "monitoring" {
  name     = var.resource_group_name
  location = var.location
}

resource "azurerm_monitor_action_group" "security_alerts" {
  name                = "enterprise-security-alerts"
  resource_group_name = azurerm_resource_group.monitoring.name
  short_name          = "SecAlerts"
}
