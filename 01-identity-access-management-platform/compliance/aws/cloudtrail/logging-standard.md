# AWS Identity Logging Standard

CloudTrail must capture management events in every governed account. Logs are centralized, encrypted, access-controlled, and protected from deletion.

## Events of Interest

- CreateUser, DeleteUser, UpdateLoginProfile
- AttachUserPolicy, AttachRolePolicy, PutRolePolicy
- CreateAccessKey, UpdateAccessKey, DeleteAccessKey
- CreateRole, UpdateAssumeRolePolicy, DeleteRole
- AddUserToGroup, RemoveUserFromGroup
- CreatePolicyVersion, SetDefaultPolicyVersion
- ConsoleLogin
- AssumeRole

## Review

Critical identity changes are reviewed immediately. Consolidated identity change reports are reviewed weekly.
