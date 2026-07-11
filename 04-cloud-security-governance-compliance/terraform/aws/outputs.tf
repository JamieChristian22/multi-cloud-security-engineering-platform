output "config_rule_name" { value = aws_config_config_rule.s3_public_read_prohibited.name }
output "budget_name" { value = aws_budgets_budget.monthly.name }
