# Team context

> Customization status: Default
> Safe to edit: Yes
> Required: Yes
> Purpose: Describe why this team uses Lantide and the environment in which analysis is performed.

## Default context

This team uses Lantide for analysis that should be reviewed, reproduced, updated, or retained as organizational evidence. Typical inputs may include local CSV, Excel, Parquet, databases, and governed MCP data sources. Typical readers include requesters, analysts, operators, product owners, and decision-makers.

The default policy assumes no specific industry, data classification, retention period, or regulator. When one of those facts materially changes the work and is not defined below, the Agent must ask the user rather than infer a rule.

## Team-specific values

Organizations may replace the defaults in this section:

- **Team or business unit:** General analytics team.
- **Common decisions supported:** Product, operational, customer, and business-performance decisions.
- **Common data sources:** Team-approved local files, databases, and MCP sources available through Lantide.
- **Typical deliverables:** Reviewable Markdown reports, managed HTML reports, validated tables, or reusable workspace assets.
- **Sensitive-data boundary:** Use only sources and destinations the user and organization have approved. Keep credentials out of prompts, reports, and repository files.
- **Required external systems:** None by default. Document an external delivery system only when the team has approved one.

## Unknown-policy rule

Do not invent company policy. If data sensitivity, ownership, retention, approval, or distribution requirements are unclear and affect the next action, pause at the decision boundary and ask the user or designated role.
