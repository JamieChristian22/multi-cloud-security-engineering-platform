# SOC 2 IAM Control Narrative

## Logical Access

Access to cloud resources is authorized by job responsibility and approved through a documented workflow.

## Authentication

MFA is required for administrative access. Federated authentication and temporary credentials are preferred over static secrets.

## Provisioning and Deprovisioning

New access is granted after approval. Departing users are disabled promptly, sessions are revoked, and residual permissions are reviewed.

## Privileged Access

Privileged roles are restricted, logged, reviewed quarterly, and assigned separately from standard access.

## Monitoring

Authentication failures, policy changes, privilege escalation, and suspicious identity activity are monitored and investigated.

## Evidence

Evidence consists of policy exports, access-review records, role-assignment reports, cloud audit logs, and remediation records.
