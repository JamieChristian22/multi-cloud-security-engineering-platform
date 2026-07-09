# Runbook: Unauthorized API Activity

## Trigger

Repeated unauthorized API calls or failed privileged operations.

## Response Steps

1. Identify principal, source IP, and attempted action.
2. Review IAM/RBAC permissions.
3. Confirm whether the user was performing expected work.
4. Disable credentials if compromise is suspected.
5. Document root cause and remediation.

## Escalation

Escalate immediately when activity involves administrative permissions.
