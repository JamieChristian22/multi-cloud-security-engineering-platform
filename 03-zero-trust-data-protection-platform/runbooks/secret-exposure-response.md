# Runbook: Secret Exposure Response

## Trigger

A secret, API key, credential, or token is exposed or accessed unexpectedly.

## Response Steps

1. Identify the exposed secret.
2. Disable or rotate the secret immediately.
3. Review access logs.
4. Identify affected applications.
5. Update dependent workloads with the new secret.
6. Confirm no unauthorized activity occurred.
7. Document containment and recovery actions.

## Closure Criteria

Secret is rotated, workloads are stable, and no unauthorized use remains active.
