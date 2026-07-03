# Incident Response Runbook

## Purpose

This runbook explains how to investigate and respond to a security event related to Security Monitoring & Threat Detection.

## Severity Levels

| Severity | Description | Example |
|---|---|---|
| Critical | Active compromise or sensitive data exposure | Unauthorized admin activity |
| High | Confirmed suspicious control-plane change | New privileged role assignment |
| Medium | Misconfiguration with exposure potential | Public storage policy changed |
| Low | Informational or hygiene issue | Missing tag or stale user |

## Triage Steps

1. Identify the alert source.
2. Confirm affected cloud provider and resource.
3. Review timestamps, principal, source IP, user agent, and API action.
4. Determine whether activity was authorized.
5. Check for related events in the previous 24 hours.
6. Assign severity.

## Containment

- Disable compromised credentials.
- Remove unauthorized role assignments.
- Revoke exposed keys.
- Block suspicious network paths.
- Snapshot logs and evidence before changes.

## Eradication

- Rotate secrets and keys.
- Remove malicious resources.
- Reapply known-good policy state.
- Confirm no persistence mechanisms remain.

## Recovery

- Restore secure configuration.
- Validate monitoring and alerts.
- Notify stakeholders.
- Document root cause.

## Lessons Learned

- What failed?
- Which detection worked?
- Which control should be improved?
- What automation can prevent recurrence?
