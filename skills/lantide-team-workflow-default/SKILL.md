---
name: lantide-team-workflow-default
description: Run team analysis through reviewable Lantide workflows.
version: 0.1.0
author: Lantide Data
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Lantide, Data Analysis, Team Workflow, Evidence]
    related_skills: []
---

# Lantide Team Workflow

Use this skill to decide when team analysis belongs in Lantide and to keep decisions, execution, evidence, and delivery in one reviewable workflow. This is an operating model, not a copy of Lantide's tool contract and not an authorization mechanism.

> **Customization boundary:** Keep this file unchanged. Adapt team policy only in `references/team/`. Live Lantide MCP guidance always governs current product behavior.

## When to Use

Use this skill when work may influence a decision, cite real data, require review, be updated later, or produce a durable deliverable.

Do not force Lantide onto a one-off arithmetic calculation, a general concept question, or a synthetic example with no need for evidence or retention. Read `references/team/usage-policy.md` before deciding borderline cases.

## Authority Order

When instructions differ, follow this order:

1. Current Lantide MCP tool schemas and structured errors.
2. The current `get_analysis_context` response.
3. The live `lantide://external_agent_playbook` resource when the context says it must be read.
4. Lantide runtime skills loaded through `load_skill`.
5. Approved team policy under `references/team/`.
6. General defaults in this skill.

Team policy may make review or evidence requirements stricter. It must never broaden MCP permissions, bypass approval, or weaken Lantide safeguards.

## Required Reading

Read only what the task needs:

1. Always read `references/00-lantide-overview.md`, `references/team/team-context.md`, and `references/team/usage-policy.md` when this skill first activates in a conversation.
2. Read `references/01-connection-and-readiness.md` when the connection is missing, new, unbound, stale, or unclear.
3. Read `references/team/roles-and-review.md` before requesting approval or assigning responsibility.
4. Read `references/team/evidence-policy.md` before analysis execution or citing a result.
5. Read `references/team/delivery-policy.md` before preparing or accepting a deliverable.
6. Select exactly one primary workflow under `references/workflows/`; read another only when the task genuinely changes class.

## Procedure

1. **Classify the request.** Apply the usage policy and state whether the task is outside Lantide, exploratory in Lantide, or formal in Lantide. The classification is complete when its reason and expected deliverable are explicit.
2. **Establish live context.** Follow the connection reference, call `get_analysis_context`, and resolve workspace selection or project identity before substantive work. Context is complete when the connection scope, access mode, workspace, and relevant artifact are known or explicitly absent.
3. **Choose the workflow.** Use:
   - `references/workflows/new-formal-analysis.md` for a new decision, contract, metric, source, or durable deliverable;
   - `references/workflows/update-existing-analysis.md` for refreshes, reproductions, or revisions of named existing artifacts;
   - `references/workflows/exploration-to-formal.md` when uncertainty should be explored before formal commitment.
4. **Apply team policy.** Identify the responsible roles, evidence boundary, and delivery bar. Ask only for material missing decisions; do not invent organization-specific policy.
5. **Use live Lantide methods.** Load every runtime skill recommended by `get_analysis_context` or required for the selected workflow. Search long-tail capabilities according to the live Playbook rather than relying on tool names remembered by this repository.
6. **Keep one authoritative analysis line.** Put formal scope, execution, evidence, findings, and limitations in Lantide artifacts. Use external chat for intent, concise progress, decisions, and handoffs—not as the only location of analysis facts.
7. **Verify completion.** Apply the selected workflow's completion criteria and `references/team/delivery-policy.md`. Do not report completion when the expected artifact, evidence link, review state, or limitation record is missing.

## Pitfalls

- Do not treat this skill as proof that Lantide is installed, connected, or authorized.
- Do not reproduce a full Plan or Report only in chat while leaving the Lantide artifact stale.
- Do not turn exploratory numbers into formal evidence without the formalization steps.
- Do not create a new Plan or Report merely because an existing artifact was not inspected.
- Do not hard-code credentials, local paths, workspace IDs, tool schemas, or version-specific capability lists in team files.
- Do not silently choose an approver, data classification, retention rule, or external-delivery channel when team policy does not define it.

## Verification

Before finishing, confirm all applicable statements:

- The task was classified using the team usage policy.
- Live Lantide context, not chat memory, determined the workspace and artifact state.
- The selected workflow matches the actual task.
- Formal claims and numbers are traceable to Lantide evidence or explicitly disclosed external evidence.
- The required reviewer or acceptance owner has a clear handoff.
- The deliverable and limitations are stored where team policy requires.
- No credential, secret, or unique authoritative result exists only in chat or an unmanaged temporary file.
