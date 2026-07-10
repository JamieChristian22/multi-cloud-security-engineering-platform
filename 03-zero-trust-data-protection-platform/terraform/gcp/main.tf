terraform {
  required_version = ">= 1.6.0"
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }
}

provider "google" {
  project = var.project_id
  region  = var.region
}

resource "google_storage_bucket" "protected_data" {
  name                        = var.bucket_name
  location                    = var.region
  uniform_bucket_level_access = true
  public_access_prevention    = "enforced"
}

resource "google_secret_manager_secret" "application_secret" {
  secret_id = "enterprise-application-secret"

  replication {
    auto {}
  }
}

resource "google_kms_key_ring" "security" {
  name     = "zero-trust-keyring"
  location = var.region
}

resource "google_kms_crypto_key" "data_protection" {
  name     = "data-protection-key"
  key_ring = google_kms_key_ring.security.id
}
