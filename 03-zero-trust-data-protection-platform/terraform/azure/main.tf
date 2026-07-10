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

resource "azurerm_resource_group" "security" {
  name     = var.resource_group_name
  location = var.location
}

resource "azurerm_storage_account" "protected_data" {
  name                            = var.storage_account_name
  resource_group_name             = azurerm_resource_group.security.name
  location                        = azurerm_resource_group.security.location
  account_tier                    = "Standard"
  account_replication_type        = "LRS"
  allow_nested_items_to_be_public = false
  min_tls_version                 = "TLS1_2"
}

resource "azurerm_key_vault" "security" {
  name                     = var.key_vault_name
  location                 = azurerm_resource_group.security.location
  resource_group_name      = azurerm_resource_group.security.name
  tenant_id                = var.tenant_id
  sku_name                 = "standard"
  purge_protection_enabled = false
}
