terraform {
  required_version = ">= 1.6.0"
  required_providers { google = { source = "hashicorp/google", version = "~> 5.0" } }
}
provider "google" { project = var.project_id, region = var.region }

resource "google_storage_bucket" "governance_evidence" {
  name = var.evidence_bucket_name
  location = var.region
  uniform_bucket_level_access = true
  public_access_prevention = "enforced"
  labels = {
    environment = "production"
    owner = "cloudsecurity"
    project = "compliance-governance"
    compliance = "required"
    costcenter = "cc1001"
  }
}
