terraform {
  required_version = ">= 1.6.0"
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 6.0"
    }
  }
}

provider "google" {
  project = var.project_id
  region  = var.region
}

resource "google_project_service" "required" {
  for_each = toset([
    "cloudresourcemanager.googleapis.com",
    "iam.googleapis.com",
    "logging.googleapis.com",
    "securitycenter.googleapis.com"
  ])
  service            = each.value
  disable_on_destroy = false
}

resource "google_logging_project_sink" "iam_audit" {
  name        = "iam-audit-sink"
  destination = "logging.googleapis.com/projects/${var.project_id}/locations/global/buckets/_Default"
  filter      = "protoPayload.serviceName=("iam.googleapis.com" OR "cloudresourcemanager.googleapis.com")"
}
