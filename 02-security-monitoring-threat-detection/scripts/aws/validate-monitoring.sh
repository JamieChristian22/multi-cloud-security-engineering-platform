#!/usr/bin/env bash
set -euo pipefail

echo "Validating AWS monitoring services..."
aws sts get-caller-identity
aws cloudwatch describe-alarms --max-records 10
aws logs describe-log-groups --limit 10
aws cloudtrail lookup-events --max-results 5
aws guardduty list-detectors || true
echo "AWS monitoring validation complete."
