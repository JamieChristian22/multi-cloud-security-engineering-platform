terraform { required_providers { google = { source="hashicorp/google", version="~> 5.0" } } }
provider "google" { project = var.project_id region = var.region }
resource "google_service_account" "security_auditor" { account_id="security-auditor-sa" display_name="Security Auditor Service Account" }
resource "google_project_iam_member" "security_reviewer" { project=var.project_id role="roles/iam.securityReviewer" member="serviceAccount:${google_service_account.security_auditor.email}" }
