# Validation Checklist

## AWS

- S3 bucket blocks public access.
- S3 bucket encryption is enabled.
- IAM policies follow least privilege.
- Secrets are stored in Secrets Manager.
- CloudTrail records data access activity.

## Azure

- Storage account public access is disabled.
- Storage encryption is enabled.
- Key Vault is created for secrets.
- RBAC assignments are reviewed.
- Defender for Cloud recommendations are reviewed.

## Google Cloud

- Cloud Storage bucket has public access prevention enabled.
- Uniform bucket-level access is enabled.
- Secret Manager stores secrets securely.
- IAM permissions are reviewed.
- Cloud Audit Logs are visible.
