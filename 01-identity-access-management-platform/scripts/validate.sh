#!/usr/bin/env bash
set -euo pipefail

echo "Validating Identity & Access Management Platform..."
required=(README.md docs/architecture.md docs/deployment-guide.md docs/risk-register.md runbooks/incident-response.md evidence/evidence-log-template.md)
for file in "${required[@]}"; do
  if [[ ! -f "$file" ]]; then
    echo "Missing required file: $file"
    exit 1
  fi
done

echo "Checking for obvious placeholder markers..."
if grep -R "TODO\|TBD\|PLACEHOLDER\|changeme" . --exclude-dir=.terraform; then
  echo "Placeholder text found. Review required."
  exit 1
fi

echo "Validation passed."
