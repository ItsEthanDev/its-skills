# Agent writing

Treat an agent-facing document as executable guidance. Optimize for reliable selection, correct sequencing, and observable completion rather than literary polish.

## Design the context pointer

A context pointer is text already in an agent's context that tells it when to read other material. Skill descriptions and references in instruction files such as `AGENTS.md` are context pointers.

A pointer must state:

1. What capability or guidance it leads to.
2. The distinct task branches that should trigger reading it.

Front-load the words most likely to match the task. Name each genuine branch once instead of listing synonyms. Keep pointers short because they consume context even when they do not fire.

Choose invocation according to who must find the skill:

- Use model invocation when the agent should select the skill autonomously. Give it a precise, model-facing description with concrete triggers.
- Use human invocation when a person should explicitly select the skill. Keep its human-facing summary concise.
- Use a router when one discoverable skill can select among bundled references or leaf skills.

Configure that choice using the harness's supported metadata. In harnesses that recognize `disable-model-invocation`, omit it for model invocation and set it to `true` for human invocation.

## Build an information hierarchy

Place material according to when the agent needs it:

1. **In-file steps:** ordered actions required on every run.
2. **In-file reference:** rules and definitions used by most branches.
3. **Disclosed reference:** branch-specific material loaded through an explicit pointer.

Inline what every branch needs. Move branch-specific detail behind a pointer. Keep each concept's definition, rules, and caveats together after choosing its level.

Keep material together by default. Split when the new file has a distinct invocation condition, isolates a branch, or prevents later steps from distracting from the current one.

## Write executable steps

- Put actions in the order they must occur.
- Begin each step with a direct verb.
- State required inputs and relevant constraints before the action.
- End each step with a completion criterion that distinguishes done from not done.
- Make completion criteria observable and exhaustive where the task requires coverage.
- Keep reference material from burying the primary sequence.
- Describe the required result rather than narrating desirable qualities such as “be careful” or “be thorough.”

A criterion such as “all modified configuration keys appear in the migration table” creates a stronger bound than “produce a migration table.”

## Prefer positive, concrete instructions

Describe the behavior the agent should perform. Reserve prohibitions for hard guardrails, and pair each one with the desired alternative.

Prefer established terms that already carry useful meaning. Define a compact term when it replaces repeated explanation across the document. Require every new term to make an instruction shorter or more precise.

Use concrete artifacts and observable actions:

- “Run the parser test and confirm it fails with the reported input.”
- “Read `package.json` to find the test command.”
- “List every changed caller before editing the interface.”

Tie completion to an artifact, command result, enumerated set, or other observable evidence.

## Preserve sources of truth

- Keep each instruction in one authoritative location and point to it elsewhere.
- Treat code, configuration, command help, and directory structure as sources of truth.
- Copy cheaply retrievable facts only when representative tasks show that retrieval is unreliable or disproportionately expensive.
- Document conventions, rationale, and non-obvious hazards that the environment cannot reveal.
- Remove stale branches, duplicated meanings, and instructions that no longer alter behavior.

An instruction is useful only if it changes behavior relative to the model's default. When uncertain, run representative tasks and keep the instruction only when the results justify it.

## Control scope and load

- Keep always-loaded descriptions and instruction-file pointers especially small.
- Route specialized detail to references.
- Prefer one router with clear branches over many overlapping automatic skills.
- Scope automatic invocation to the durable artifacts the skill governs.
- Keep project facts in project context and reusable process guidance in skills.

## Completion checklist

- Does each pointer name its material and every distinct trigger branch?
- Can the agent select a branch, load only its specialized detail, and find related rules together?
- Do required steps appear in order with observable, sufficiently exhaustive completion criteria?
- Does each instruction state concrete target behavior, with representative tasks used when its effect is uncertain?
- Do factual claims point to authoritative sources, with copied facts justified by retrieval evidence?
- Has every duplicated, stale, or behavior-neutral instruction been removed?
