# Evidence policy

> Customization status: Default
> Safe to edit: Yes
> Required: Yes
> Purpose: Keep formal analysis claims traceable and prevent evidence from scattering across tools.

## Single authoritative analysis line

For one formal question, maintain one authoritative analysis line in Lantide. The Plan records the contract, formal execution records what ran, evidence supports the numbers, and the Report records findings and limitations.

External chat may carry intent, concise progress, decisions, and handoffs. It must not become the only location of a changed definition, executed SQL, material number, conclusion, or limitation.

## Default requirements

- Keep formal queries and their result provenance in Lantide whenever the connected tools support the work.
- Record agreed scope, metrics, denominators, filters, assumptions, and checkpoints in the Plan before execution.
- Treat exploratory queries as non-report evidence until they are formally rerun or incorporated through the live Lantide evidence contract.
- Read the current named artifact and evidence lineage before revising, explaining, reproducing, or distributing prior work.
- Do not run a parallel external analysis for the same formal question and then paste only its conclusion into Lantide.
- Do not let a notebook, scratch SQL file, downloaded result, or chat attachment become the unique authoritative copy.
- Never reconstruct missing values, query text, approvals, or artifact state from memory.

## Necessary external computation

When a required method cannot run inside Lantide:

1. Explain why external execution is necessary before relying on it.
2. Use only an approved environment and data handling path.
3. Preserve the method, inputs or input identity, output, validation, and limitations.
4. Import, reference, or disclose that evidence in Lantide using the current supported workflow.
5. Mark any break in lineage clearly; do not imply Lantide executed or verified work it did not perform.

## Team extensions

Organizations may add prohibited tools, required validation tests, sensitive-field handling, retention rules, or minimum evidence thresholds. Added policy may be stricter than Lantide defaults but cannot weaken live permissions or approval requirements.
