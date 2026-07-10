output "storage_account_name" {
  value = azurerm_storage_account.protected_data.name
}

output "key_vault_uri" {
  value = azurerm_key_vault.security.vault_uri
}
