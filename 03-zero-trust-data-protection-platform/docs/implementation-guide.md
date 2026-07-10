# Implementation Guide

## AWS

- Create S3 bucket with block public access enabled.
- Enable default encryption with KMS.
- Store secrets in AWS Secrets Manager.
- Create least-privilege IAM policies.
- Enable CloudTrail and Security Hub validation.

## Azure

- Create a secure Storage Account.
- Disable public blob access.
- Use Microsoft Entra ID and Azure RBAC.
- Store secrets in Azure Key Vault.
- Enforce controls with Azure Policy.
- Review Defender for Cloud recommendations.

## Google Cloud

- Create a Cloud Storage bucket with public access prevention.
- Use Uniform Bucket-Level Access.
- Store secrets in Secret Manager.
- Use Cloud IAM for least privilege.
- Enforce Organization Policy constraints.
- Review Security Command Center findings.
