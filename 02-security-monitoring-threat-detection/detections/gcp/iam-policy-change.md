# Google Cloud IAM Policy Change Detection

Signal: Audit Log event containing SetIamPolicy.

Escalate when:
- Owner or Editor is granted
- Organization-level roles change
- Service account impersonation permissions are added
- External identities are introduced
