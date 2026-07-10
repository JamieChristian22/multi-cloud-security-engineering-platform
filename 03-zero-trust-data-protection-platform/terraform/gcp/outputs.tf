output "bucket_name" {
  value = google_storage_bucket.protected_data.name
}

output "kms_key_id" {
  value = google_kms_crypto_key.data_protection.id
}
