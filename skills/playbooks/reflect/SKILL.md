---
name: reflect
description: Reflect on selected work and propose reusable improvements.
disable-model-invocation: true
---

# Reflect

Use only when the user explicitly requests reflection, including as a named step in a requested workflow. Completion, a correction, or a reference alone is not an invocation.

## Examine the selected work

Identify the task or session being examined and the evidence actually available. Use the supplied scope or a clearly identified current task; ask only when ambiguity would materially change the examination. Read relevant artifacts and observations rather than reconstruct missing history. State consequential evidence gaps.

Identify any explicit update request and its permitted destinations. Without one, prepare proposals only. Do not edit maintained content or persist a retrospective, backlog, or personal memory as part of proposal-only reflection.

Extract candidate lessons from observed failures, recurring friction, or successful practices. For each, identify the concrete observation, supporting source, and proposed interpretation. Label hypotheses. A single incident can justify a local correction without establishing a universal rule; do not promote an incidental preference or circumstance into general policy without sufficient evidence or explicit direction.

Inspect relevant project and user-level steering files and skills when they contributed to the selected work. Trace the guidance actually used; do not inventory unrelated global material. Keep project-specific lessons with project guidance; propose changes to user-level guidance or reusable skills only when the evidence supports their broader scope.

## Investigate improvement opportunities

Use these prompts where the evidence warrants them; do not require a finding in every category.

- **Navigation:** When finding information took excessive exploration, examine missing pointers, hidden file dependencies, and unclear authoritative owners. Propose navigation that would have shortened the observed search.
- **Automated checks:** When a mistake could be caught mechanically, read the project's existing check commands and CI configuration first. Distinguish missing coverage from checks that were broken, not run, or not wired into the workflow. Prefer a deterministic check for fixed syntax, banned APIs, import patterns, or file-placement rules; retain judgment-dependent guidance in prose.
- **Steering placement:** When project or global `AGENTS.md` files are large, identify instructions better placed in automated checks, skills, references, or the existing `CONSTITUTION.md`. Reserve the constitution for durable policy and constraints, not procedural detail. Preserve useful navigation pointers and follow established owners rather than creating a new standards file by default.
- **Tool economy:** When tool calls were expensive or produced excessive output, examine repeated exploration and token-heavy CLI or MCP interfaces. Propose narrower queries, bounded output, or reusable tooling that would reduce the observed cost.
- **No-op instructions:** When steering files are unwieldy, identify duplicate, stale, or behavior-neutral instructions. Support proposed deletion with evidence; preserve safety and authority constraints even when the session did not exercise them.
- **Information access:** When crucial information was unavailable, consider accessible logs, diagnostics, documentation, or read-only service access. Name the missing information and how access would help. Propose access changes without connecting to services, exposing secrets, or changing configuration.

## Filter and route candidates

Compare each candidate with existing guidance and project constraints. Distinguish a missing instruction from an instruction that was ignored, a selection or execution failure, and a tool or environment problem. Do not add a duplicate rule merely because an existing one was missed. Reject unsupported generalizations and permit a result with no worthwhile proposals.

Read `principle-encode-lessons-in-structure` when deciding whether a feasible mechanism would address the problem better than more prose.

When the durable destination is unclear, use `project-documentation` to select the owner. For proposed artifact wording, use `writing`. Preserve existing activation, composition, and authority constraints. Exclude secrets, unnecessary personal details, personality judgments, and inferred personal traits from proposed durable records.

## Return proposals and update scope

Order retained proposals by expected impact and evidence strength; include implementation cost when it affects priority. For each, state the problem or practice, evidence, proposed change and destination, expected benefit, and any unresolved decision or permission. Include rejected candidates only when their disposition explains the result. Keep the response proportionate to the work; do not fill a quota or create a report file by default.

Return proposals and control to the caller. If updates were explicitly requested, include the bounded edits and destinations already authorized for caller application under the appropriate authoring workflow. The caller can apply covered changes without requesting the same permission again. Return unclear edit boundaries or consequential policy choices as unresolved decisions before application. Do not apply recommendations merely because reflection was requested.
