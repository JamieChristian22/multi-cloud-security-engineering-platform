#!/usr/bin/env bash
set -euo pipefail

echo "Validating Google Cloud monitoring services..."
gcloud config list
gcloud logging logs list --limit=10
gcloud monitoring policies list --limit=5 || true
echo "Google Cloud monitoring validation complete."
