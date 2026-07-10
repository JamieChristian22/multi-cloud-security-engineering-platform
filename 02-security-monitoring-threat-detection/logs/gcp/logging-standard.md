# Google Cloud Logging Standard

Required sources:
- Admin Activity logs
- Data Access logs for sensitive services
- VPC Flow Logs
- Cloud Run logs
- Security Command Center findings
- Organization Policy changes

Retention:
- Default operational retention as configured
- Security logs retained for at least 365 days
- Export critical logs to dedicated log buckets or Cloud Storage
