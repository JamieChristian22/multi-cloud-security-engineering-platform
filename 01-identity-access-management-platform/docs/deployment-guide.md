# Deployment Guide

## Prerequisites

- AWS CLI configured with a sandbox account.
- Azure CLI configured with a sandbox subscription.
- Google Cloud CLI configured with a sandbox project.
- Terraform installed.
- GitHub account for repository hosting.

## AWS Deployment

```bash
cd terraform/aws
terraform init
terraform fmt
terraform validate
terraform plan
```

## Azure Deployment

```bash
cd terraform/azure
terraform init
terraform fmt
terraform validate
terraform plan
```

## GCP Deployment

```bash
cd terraform/gcp
terraform init
terraform fmt
terraform validate
terraform plan
```

## Validation

Run the project validation script:

```bash
bash scripts/validate.sh
```

## Evidence Collection

After deployment, capture screenshots of:

- IAM roles or RBAC assignments
- logging configuration
- policy assignments
- alerts or findings
- encryption keys
- dashboards

Store screenshots inside `evidence/screenshots/`.
