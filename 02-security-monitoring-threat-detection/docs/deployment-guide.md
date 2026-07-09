# Deployment Guide

## Prerequisites

- AWS CLI configured for the target account.
- Azure CLI authenticated to the target subscription.
- Google Cloud CLI authenticated to the target project.
- Terraform installed locally.

## Recommended Order

1. Deploy AWS monitoring resources.
2. Deploy Azure monitoring resources.
3. Deploy Google Cloud monitoring resources.
4. Validate alerts, logs, dashboards, and security findings.
5. Capture evidence screenshots for the portfolio.

## Safety Notes

Use low-cost test metrics and avoid enabling paid premium security plans unless intentionally testing them.
