#!/usr/bin/env bash
set -euo pipefail
aws sts get-caller-identity
aws configservice describe-config-rules
aws cloudtrail describe-trails
aws resourcegroupstaggingapi get-resources
echo "AWS governance validation complete."
