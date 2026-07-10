# AWS Compliance Baseline

Controls: S3 public access prohibition, KMS encryption, CloudTrail enabled, AWS Config rules, Security Hub standards, MFA for privileged access.

Recommended Config rules:
- s3-bucket-public-read-prohibited
- s3-bucket-public-write-prohibited
- s3-bucket-server-side-encryption-enabled
- cloudtrail-enabled
- root-account-mfa-enabled
- restricted-ssh
