# AWS Logging Standard

Required sources:
- CloudTrail management events
- CloudTrail data events for sensitive S3 buckets
- VPC Flow Logs
- CloudWatch Logs for Lambda and applications
- GuardDuty findings
- Security Hub findings

Retention:
- Operational logs: 90 days
- Security logs: 365 days
- Long-term archive: S3 with lifecycle policies

Protection:
- KMS encryption
- Restricted write/delete permissions
- Log file validation for CloudTrail
