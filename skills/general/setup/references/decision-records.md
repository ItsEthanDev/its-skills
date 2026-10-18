# Decision records

Establish where consequential decisions and their rationale belong when the user wants decision records. Keep this separate from the glossary: the glossary owns what terms mean; decision records own what was decided and why.

Preserve an existing location and format. Otherwise, propose a location such as `docs/adr/`, naming and numbering conventions, status handling, and how later decisions supersede earlier ones. Confirm who accepts decisions and what kinds of trade-off warrant a record. Use the criteria, examples, and short format in the decision-record index seed as a proposed starting point. Preserve existing project choices or obtain approval for changed conventions; do not impose the seed's defaults merely because they are newer.

Use the decision-record index seed to record these conventions and maintenance instructions. Link that index from the README. Create the index when this feature is selected, not placeholder ADRs. Decisions get individual records only when there is a consequential, agreed trade-off to capture.

The generated index must contain or link the actual chosen criteria, naming, acceptance, format, and supersession procedure inside the project, not refer contributors back to a skill or this seed. Keep relevant examples and the rationale for offering records sparingly. Match the project's own format; a short title and a paragraph can be enough when the user wants a minimal record. Don't invent decisions to populate an empty index.

If the project has multiple contexts, establish system-wide and context-specific locations only where needed. Future contributors should read records relevant to their work and surface contradictions rather than silently override an accepted decision.
