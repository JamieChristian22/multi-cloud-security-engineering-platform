output "audit_sink_writer_identity" {
  value = google_logging_project_sink.iam_audit.writer_identity
}
