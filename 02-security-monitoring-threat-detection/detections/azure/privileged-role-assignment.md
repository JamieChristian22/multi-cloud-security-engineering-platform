# Azure Privileged Role Assignment Detection

Signal: Activity Log event for roleAssignments/write.

High-risk roles:
- Owner
- User Access Administrator
- Contributor
- Security Admin

Response: verify approval, review actor, remove unauthorized assignment, and inspect related activity.
