# Interview Talking Points

## Problem

Organizations frequently manage identities separately across AWS, Azure, and GCP, creating inconsistent privilege, logging, and evidence practices.

## Solution

I built a provider-neutral compliance operating model with cloud-specific enforcement, automated evidence collection, policy-as-code, control mapping, runbooks, and executive reporting.

## Key Engineering Decisions

- Used federated identity and short-lived credentials as the target state.
- Separated control intent from provider implementation.
- Added hashes to evidence to preserve integrity.
- Built CI to validate Terraform, JSON, and security configuration.
- Created risk-based remediation rather than treating every finding equally.

## What I Would Add in Production

- Central SIEM ingestion
- Real HR-driven joiner/mover/leaver automation
- Secrets manager integration
- Formal exception workflow
- Scheduled access certifications
- Ticketing-system integration
