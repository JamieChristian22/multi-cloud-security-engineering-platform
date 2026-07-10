# Google Cloud Log Query Examples

IAM changes:
`protoPayload.methodName:"SetIamPolicy"`

Service account keys:
`protoPayload.methodName:"google.iam.admin.v1.CreateServiceAccountKey"`

Storage IAM changes:
`resource.type="gcs_bucket" protoPayload.methodName:"SetIamPolicy"`

Denied access:
`protoPayload.status.code=7`
