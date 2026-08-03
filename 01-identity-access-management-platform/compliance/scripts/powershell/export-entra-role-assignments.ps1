[CmdletBinding()]
param(
    [string]$OutputPath = ".\entra-role-assignments.csv"
)

$ErrorActionPreference = "Stop"

if (-not (Get-Module -ListAvailable Microsoft.Graph)) {
    throw "Microsoft.Graph PowerShell module is required."
}

Connect-MgGraph -Scopes "RoleManagement.Read.Directory","Directory.Read.All"

$assignments = Get-MgRoleManagementDirectoryRoleAssignment -All -ExpandProperty Principal,RoleDefinition
$report = foreach ($assignment in $assignments) {
    [pscustomobject]@{
        AssignmentId = $assignment.Id
        PrincipalId = $assignment.PrincipalId
        RoleDefinitionId = $assignment.RoleDefinitionId
        DirectoryScopeId = $assignment.DirectoryScopeId
        PrincipalDisplayName = $assignment.Principal.AdditionalProperties.displayName
        RoleDisplayName = $assignment.RoleDefinition.DisplayName
    }
}

$report | Sort-Object RoleDisplayName, PrincipalDisplayName |
    Export-Csv -NoTypeInformation -Encoding UTF8 -Path $OutputPath

Write-Host "Exported $($report.Count) role assignments to $OutputPath"
