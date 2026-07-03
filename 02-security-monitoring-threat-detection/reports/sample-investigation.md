# Sample Investigation

## Alert

AWS Root Account Login detected.

## Findings

- Principal: Root
- Event: ConsoleLogin
- Risk: Root use bypasses normal role-based workflows.
- Status: Suspicious until approved by account owner.

## Actions

1. Confirm MFA was used.
2. Review source IP and user agent.
3. Check subsequent API activity.
4. Rotate credentials if unauthorized.
5. Document evidence and lessons learned.
