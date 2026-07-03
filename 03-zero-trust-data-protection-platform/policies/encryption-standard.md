# Encryption Standard

## Requirements

- Customer-managed keys are required for sensitive workloads.
- Key rotation must be enabled where supported.
- Secrets must be stored in AWS Secrets Manager, Azure Key Vault, or GCP Secret Manager.
- Plaintext secrets must not be committed to source control.
- TLS is required for data in transit.
