#!/usr/bin/env bash
set -euo pipefail

echo "Validating Google Cloud data protection controls..."
gcloud storage buckets describe "gs://$1"
gcloud secrets list --limit=5
gcloud logging read "protoPayload.serviceName:*" --limit=5
echo "Google Cloud validation complete."
