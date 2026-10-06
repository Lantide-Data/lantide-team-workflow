# Lantide overview

Lantide Data is a local-first AI analysis workspace for work that should remain reviewable, reproducible, and useful beyond one chat session. It brings the analysis contract, executed SQL, evidence, reports, and activity history into one managed environment while an external Agent can remain the conversational interface.

## Artifact roles

- **Plan:** records the question, scope, metric definitions, assumptions, checkpoints, and expected deliverable before formal execution.
- **SQL and execution steps:** record what actually ran and provide evidence for reported numbers.
- **Markdown Report:** holds the decision-facing narrative, findings, limitations, and analysis appendix.
- **HTML Report:** is a managed presentation derived from a review-ready Markdown Report, not a substitute for weak or missing evidence.
- **Reference:** preserves project-specific authority such as definitions, policies, or source material.
- **External MCP Activity and audit:** show factual tool and lifecycle activity; they are not copies of the external conversation.

## Surface boundary

Use the external conversation to clarify intent, ask for decisions, report concise progress, and coordinate handoffs. Keep the formal Plan, executed evidence, durable findings, Report, and limitations in Lantide. A chat summary is not the authoritative deliverable for formal analysis.

This repository defines a team operating model. It does not grant permissions, change access mode, approve a Plan, or replace live Lantide methodology. After connecting, use the current MCP context, Playbook, runtime skills, tool schemas, and structured errors as the product source of truth.

## Official documentation

Use these pages when more product detail is needed instead of guessing or expanding this reference into a second product manual:

- Documentation hub: <https://lantidedata.com/en/docs>
- Product overview: <https://lantidedata.com/en/what-is-lantide-data>
- User guide introduction: <https://lantidedata.com/en/docs/user-guide/welcome>
- External Agent setup: <https://lantidedata.com/en/docs/learn/platform-admin/external-agent-integration>
- External Agent reference: <https://lantidedata.com/en/docs/user-guide/external-agent>
- External Agent workflow background: <https://lantidedata.com/en/blog/why-lantide-with-claude-code-codex>

Prefer the live MCP resource when documentation and the connected Desktop version differ on runtime behavior.
