# Azure KQL Query Examples

Administrative failures:
`AzureActivity | where ActivityStatusValue == "Failure"`

Role assignments:
`AzureActivity | where OperationNameValue has "roleAssignments"`

Policy changes:
`AzureActivity | where OperationNameValue has "policyAssignments"`

Storage updates:
`AzureActivity | where ResourceProviderValue == "MICROSOFT.STORAGE"`
