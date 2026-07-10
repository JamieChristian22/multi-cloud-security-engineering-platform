# Runbook: Public Storage Exposure Response

## Trigger

A storage bucket or container is found to allow public access.

## Response Steps

1. Identify the affected cloud provider and storage resource.
2. Immediately disable public access.
3. Review access logs for unauthorized downloads.
4. Identify sensitive data stored in the resource.
5. Rotate exposed credentials if needed.
6. Notify security leadership if regulated data was exposed.
7. Document root cause and corrective actions.

## Closure Criteria

Public access is disabled, logs are reviewed, and the storage control is validated.
