---
name: writing
description: Plan, draft, revise, or review durable technical prose for humans or coding agents. Use when choosing an artifact's audience or structure, proposing its wording in chat, or writing documentation, READMEs, specifications, RFCs, ADRs, PR descriptions, commit messages, AGENTS.md, CLAUDE.md, prompts, or skills.
---

# Writing

Write for the artifact's reader and purpose. When `project-documentation` applies, use it to select the artifact, canonical owner, schema, and maintenance rules before improving the information hierarchy and prose.

Write proposed artifact text in the artifact's voice, even when presenting a draft in chat. State its decisions, status, and requirements directly instead of narrating the conversation that produced them. Write “The plan is accepted,” not “The owner accepts the plan.” Name a person only when their identity is necessary to the artifact's meaning or accountability; keep incidental conversation attribution in the source record that owns provenance, when one exists.

## Choose the reader

- For prose that people read, including documentation, READMEs, RFCs, ADRs, PR descriptions, and commit messages, read [human-writing.md](human-writing.md).
- For instructions that coding agents consume, including `AGENTS.md`, `CLAUDE.md`, prompts, and skills, read [agent-writing.md](agent-writing.md).
- For an artifact that serves both readers, separate the human explanation from the agent instructions when practical. When they must share an artifact, read both references and make each section's audience explicit.

Load one reference for a single-audience artifact. Load both references for a mixed-audience artifact.

## Process

1. Identify the reader, the artifact, and the job the writing must perform. Complete this step when one sentence names all three.
2. Inspect the repository for its terminology, conventions, and authoritative facts. Complete this step when each relevant convention and factual claim has a known source.
3. Read the applicable reference and draft or revise the artifact. Complete this step when every section serves the named reader and job.
4. Verify every changed symbol, path, command, example, link, and factual claim against its source. Complete this step when each item has been checked and executable examples have been exercised when practical.
5. Review the result using the applicable reference's completion checklist. Complete this step when every item passes or the final response names a justified exception.

The work is complete when all five completion criteria are satisfied.
