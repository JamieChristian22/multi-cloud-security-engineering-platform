param location string = resourceGroup().location
resource keyVault 'Microsoft.KeyVault/vaults@2023-07-01' = {
  name: 'kv-zero-trust-lab-secure'
  location: location
  properties: {
    tenantId: subscription().tenantId
    sku: { family: 'A', name: 'standard' }
    enableRbacAuthorization: true
    publicNetworkAccess: 'Disabled'
  }
}
