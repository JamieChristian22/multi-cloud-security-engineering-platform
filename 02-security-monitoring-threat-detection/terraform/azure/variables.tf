variable "resource_group_name" {
  description = "Azure resource group used for monitoring resources."
  type        = string
  default     = "rg-security-platform-prod"
}

variable "location" {
  description = "Azure region."
  type        = string
  default     = "East US"
}
