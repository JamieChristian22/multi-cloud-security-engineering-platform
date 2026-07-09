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

resource "google_monitoring_notification_channel" "email" {
  display_name = "Enterprise Security Alerts"
  type         = "email"

  labels = {
    email_address = var.notification_email
  }
}
