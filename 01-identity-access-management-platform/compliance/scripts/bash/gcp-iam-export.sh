#!/usr/bin/env bash
set -euo pipefail

OUTPUT_DIR="${1:-gcp-iam-evidence}"
mkdir -p "$OUTPUT_DIR"

ORG_ID="$(gcloud organizations list --format='value(ID)' --limit=1)"
if [[ -z "$ORG_ID" ]]; then
  echo "No accessible Google Cloud organization was found." >&2
  exit 1
fi

gcloud organizations get-iam-policy "$ORG_ID" --format=json \
  > "$OUTPUT_DIR/organization-iam-policy.json"

gcloud projects list --format='value(projectId)' | while read -r project_id; do
  [[ -z "$project_id" ]] && continue
  gcloud projects get-iam-policy "$project_id" --format=json \
    > "$OUTPUT_DIR/${project_id}-iam-policy.json"
done

echo "IAM evidence exported to $OUTPUT_DIR"
