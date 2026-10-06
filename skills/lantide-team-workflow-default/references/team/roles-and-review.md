# Roles and review

> Customization status: Default
> Safe to edit: Yes
> Required: Yes
> Purpose: Define responsibility for scope, execution, review, and acceptance.

## Default roles

- **Requester:** owns the decision question and explains the intended use.
- **Analysis owner:** converts the question into a bounded analysis and maintains the evidence chain.
- **Plan reviewer:** confirms scope, metric definitions, assumptions, and checkpoints before formal execution.
- **Report approver:** decides whether findings and limitations are sufficient for the intended audience.
- **Platform administrator:** manages connections, workspaces, sensitive destinations, and high-trust operations.

One person may hold several roles in a small team, but the Agent must still distinguish which responsibility is being exercised.

## Default review policy

- The requester or delegated reviewer must resolve material ambiguity in scope or business definitions.
- Formal execution follows the current Lantide Plan lifecycle and access-mode rules.
- Admin access does not remove the need for an explicit user decision where the live contract requires one.
- A Report is accepted only by someone who understands its intended use and limitations.
- High-trust setup, credential, filesystem, workspace, or external-delivery decisions belong to the platform administrator or an explicitly authorized delegate.

## Escalation

Ask for a decision when ownership is unclear and the next action would change scope, expose data, authorize execution, overwrite or deprecate an artifact, or distribute a result. Do not fabricate a reviewer or treat silence as approval.

## Organization customization

Replace role labels with actual teams or job functions if useful. Define any required separation of duties, second-person review, service-level expectation, or exception process here—not in `SKILL.md`.
