#!/usr/bin/env bash
set -euo pipefail

echo "Validating Azure data protection controls..."
az storage account show --name "$1" --resource-group "$2" --query "{name:name, allowBlobPublicAccess:allowBlobPublicAccess, encryption:encryption}"
az keyvault list --resource-group "$2" -o table
az monitor activity-log list --max-events 5
echo "Azure validation complete."
