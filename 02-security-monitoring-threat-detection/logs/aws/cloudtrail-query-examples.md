# AWS Log Query Examples

Unauthorized calls:
`fields @timestamp, userIdentity.arn, sourceIPAddress, eventName, errorCode | filter errorCode like /AccessDenied|Unauthorized/`

IAM changes:
`fields @timestamp, eventName, userIdentity.arn | filter eventSource="iam.amazonaws.com"`

S3 policy changes:
`fields @timestamp, eventName, requestParameters.bucketName | filter eventName in ["PutBucketPolicy","DeleteBucketPolicy"]`
