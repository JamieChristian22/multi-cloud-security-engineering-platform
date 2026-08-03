# Runbook: Suspected Credential Compromise

## Immediate Actions

1. Disable or suspend the affected identity.
2. Revoke active sessions and temporary tokens.
3. Disable or rotate access keys and secrets.
4. Preserve sign-in, audit, and authorization logs.
5. Review recent role, policy, MFA, and credential changes.
6. Search for lateral movement and persistence.
7. Restore access using a verified identity and clean authenticator.
8. Document root cause, impact, and preventive actions.

## Provider Actions

- **AWS:** deactivate access keys, remove console password if necessary, revoke role sessions through policy changes, review CloudTrail.
- **Azure:** block sign-in, revoke sessions, reset credentials, review Entra sign-in and audit logs.
- **GCP:** suspend the account, delete compromised service account keys, review Cloud Audit Logs and Security Command Center.
