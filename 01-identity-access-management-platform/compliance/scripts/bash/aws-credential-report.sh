#!/usr/bin/env bash
set -euo pipefail

OUTPUT_DIR="${1:-aws-iam-evidence}"
mkdir -p "$OUTPUT_DIR"

aws iam generate-credential-report >/dev/null

for attempt in {1..20}; do
  state="$(aws iam get-credential-report --query State --output text 2>/dev/null || true)"
  if [[ "$state" == "COMPLETE" ]]; then
    aws iam get-credential-report --query Content --output text |
      base64 --decode > "$OUTPUT_DIR/credential-report.csv"
    aws iam get-account-summary > "$OUTPUT_DIR/account-summary.json"
    aws accessanalyzer list-analyzers > "$OUTPUT_DIR/access-analyzers.json"
    echo "AWS IAM evidence exported to $OUTPUT_DIR"
    exit 0
  fi
  sleep 3
done

echo "Credential report did not complete in time." >&2
exit 1
