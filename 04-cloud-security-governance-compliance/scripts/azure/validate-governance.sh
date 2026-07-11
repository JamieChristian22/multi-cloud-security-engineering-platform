#!/usr/bin/env bash
set -euo pipefail
az account show
az policy assignment list -o table
az monitor activity-log list --max-events 10
az resource list -o table
echo "Azure governance validation complete."
