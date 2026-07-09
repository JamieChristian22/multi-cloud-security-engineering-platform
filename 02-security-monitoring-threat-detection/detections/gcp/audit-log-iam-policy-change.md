# Google Cloud Detection: IAM Policy Change

## Signal

Cloud Audit Logs event showing IAM policy binding creation, deletion, or modification.

## Severity

High when privileged roles are involved.

## Response

1. Identify actor and target resource.
2. Review role granted or removed.
3. Verify approval.
4. Remove unauthorized binding.
5. Review additional activity by the actor.
