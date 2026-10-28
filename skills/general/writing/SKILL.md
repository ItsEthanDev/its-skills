---
name: writing
description: Plan, draft, revise, or review durable technical prose for humans or coding agents. Use when choosing an artifact's audience or structure, proposing its wording in chat, or writing documentation, READMEs, specifications, RFCs, ADRs, PR descriptions, commit messages, AGENTS.md, CLAUDE.md, prompts, or skills.
---

# Writing

Write for the artifact's eventual reader, not the conversation that produced it. State the chosen conventions, decisions, status, and requirements directly, including in drafts presented in chat. Remove planning residue: rejected alternatives, reminders of debates, and caveats that require the conversation to make sense. Keep rationale when it helps future decisions.

Give each rule, convention, or procedure one authoritative home with a recognizable purpose. Link to it where readers need it, so they can find the guidance without already knowing where it lives. Maintain the guidance in its owning document rather than repeat it elsewhere.

Write proposed artifact text in the artifact's voice. Write “The plan is accepted,” not “The owner accepts the plan.” Name a person only when their identity is necessary to the artifact's meaning or accountability; keep incidental conversation attribution in the source record that owns provenance, when one exists.

Write maintained documentation as a coherent description of the current design, not as layers of amendments to earlier designs. When the design changes, revise the affected guidance in place so readers need no knowledge of its predecessors. Preserve useful history in artifacts intended for that purpose, such as decision records, changelogs, migration guides, and the issue tracker.

## Choose the reader

- For prose that people read, including documentation, READMEs, RFCs, ADRs, PR descriptions, and commit messages, read [human-writing.md](human-writing.md).
- For instructions that coding agents consume, including `AGENTS.md`, `CLAUDE.md`, prompts, and skills, read [agent-writing.md](agent-writing.md).
  Load one reference for a single-audience artifact. Load both references for a mixed-audience artifact.
