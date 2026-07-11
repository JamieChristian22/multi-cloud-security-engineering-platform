#!/usr/bin/env bash
set -euo pipefail
PROJECT="$(gcloud config get-value project)"
gcloud projects get-iam-policy "$PROJECT"
gcloud asset search-all-resources --scope="projects/$PROJECT" --limit=20
gcloud logging read 'logName:"cloudaudit.googleapis.com"' --limit=10
echo "Google Cloud governance validation complete."
