variable "project_id" {
  description = "Google Cloud project ID."
  type        = string
}

variable "region" {
  description = "Google Cloud region."
  type        = string
  default     = "us-central1"
}

variable "bucket_name" {
  description = "Globally unique Cloud Storage bucket name."
  type        = string
}
