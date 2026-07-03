terraform { required_providers { azurerm = { source="hashicorp/azurerm", version="~> 3.0" } } }
provider "azurerm" { features {} }
resource "azurerm_resource_group" "iam" { name="rg-security-iam-platform" location="eastus" }
resource "azurerm_user_assigned_identity" "automation" { name="id-security-automation" location=azurerm_resource_group.iam.location resource_group_name=azurerm_resource_group.iam.name }
