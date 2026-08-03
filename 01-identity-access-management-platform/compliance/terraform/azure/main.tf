terraform {
  required_version = ">= 1.6.0"
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 4.0"
    }
  }
}

provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "iam" {
  name     = "${var.prefix}-iam-compliance-rg"
  location = var.location
}

resource "azurerm_log_analytics_workspace" "iam" {
  name                = "${var.prefix}-iam-law"
  location            = azurerm_resource_group.iam.location
  resource_group_name = azurerm_resource_group.iam.name
  sku                 = "PerGB2018"
  retention_in_days   = 90
}

resource "azurerm_monitor_action_group" "security" {
  name                = "${var.prefix}-security-alerts"
  resource_group_name = azurerm_resource_group.iam.name
  short_name          = "iamsec"
}
