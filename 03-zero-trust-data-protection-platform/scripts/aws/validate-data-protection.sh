#!/usr/bin/env bash
set -euo pipefail

echo "Validating AWS data protection controls..."
aws s3api get-public-access-block --bucket "$1"
aws s3api get-bucket-encryption --bucket "$1"
aws secretsmanager list-secrets --max-results 5
aws cloudtrail lookup-events --max-results 5
echo "AWS validation complete."
