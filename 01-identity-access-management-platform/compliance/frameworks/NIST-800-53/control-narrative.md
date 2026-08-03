# NIST SP 800-53 Rev. 5 IAM Control Narrative

## AC-2 Account Management

Cloud identities are created only through an approved request. Workforce access is group-based, time-bounded where practical, and removed when employment or contract status changes. Quarterly reviews identify inactive, orphaned, privileged, and noncompliant accounts.

## AC-3 Access Enforcement

AWS IAM policies, Azure role assignments and Conditional Access, and Google Cloud IAM bindings enforce approved access decisions. Direct user permissions are discouraged in favor of groups and roles.

## AC-5 Separation of Duties

Administration, security review, and audit responsibilities are separated. The same individual should not request, approve, and validate privileged access.

## AC-6 Least Privilege

Permissions are limited to documented job functions. Broad administrator roles require approved exceptions, MFA, and enhanced monitoring.

## IA-2 Identification and Authentication

MFA is required for privileged and interactive workforce access. Strong authentication is combined with federation and temporary credentials where supported.

## IA-4 Identifier Management

Identity identifiers are unique, traceable, and not reused. Service identities use purpose-specific names and documented owners.

## IA-5 Authenticator Management

Static credentials are minimized. Keys are rotated, secrets are stored in approved secret-management services, and stale credentials are disabled.

## AU-2 Event Logging

Identity events include sign-ins, policy changes, role changes, failed authentication, and service-account activity.

## AU-6 Audit Record Review

High-risk identity events are reviewed through cloud-native findings and centralized reports. Critical events are escalated according to the incident runbook.

## CA-7 Continuous Monitoring

Automated scripts and native compliance services continuously evaluate IAM controls. Findings are recorded, assigned, and tracked to closure.
