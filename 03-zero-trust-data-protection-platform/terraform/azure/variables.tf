variable "resource_group_name" {
  type    = string
  default = "rg-zero-trust-data-protection"
}

variable "location" {
  type    = string
  default = "East US"
}

variable "storage_account_name" {
  description = "Globally unique lowercase Azure Storage Account name."
  type        = string
}

variable "key_vault_name" {
  description = "Globally unique Azure Key Vault name."
  type        = string
}

variable "tenant_id" {
  description = "Azure tenant ID."
  type        = string
}
