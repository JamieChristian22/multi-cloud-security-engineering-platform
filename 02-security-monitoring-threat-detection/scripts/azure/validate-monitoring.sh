#!/usr/bin/env bash
set -euo pipefail

echo "Validating Azure monitoring services..."
az account show
az monitor activity-log list --max-events 5
az monitor metrics list-definitions --resource "$(az group show -n rg-security-platform-prod --query id -o tsv)" || true
echo "Azure monitoring validation complete."
