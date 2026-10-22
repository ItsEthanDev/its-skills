# Decision records

Establish where consequential decisions and their rationale belong when the user wants decision records. Keep this separate from the glossary: the glossary owns what terms mean; decision records own what was decided and why.

Preserve an existing location and format. Otherwise, propose a location such as `docs/adr/`, naming and numbering conventions, status handling, and how later decisions supersede earlier ones. Confirm who accepts decisions and what kinds of trade-off warrant a record. Use the criteria, examples, and short format in the decision-record guidance seed as a proposed starting point. Preserve existing project choices or obtain approval for changed conventions; do not impose the seed's defaults merely because they are newer.

Generate two outputs: a human-facing index linking the actual records, and an agent guide containing the creation criteria, examples, format, locations, approval, and maintenance procedure. Link them to each other. Put the index under Project documentation in the README, and the guide under Agent documentation. The index can say "No decisions recorded yet"; do not create a placeholder decision to populate it.

The generated guide must contain or link the actual chosen criteria, naming, acceptance, format, and supersession procedure inside the project, not refer contributors back to a skill or this seed. Keep relevant examples and the rationale for offering records sparingly. Match the project's own format; a short title and a paragraph can be enough when the user wants a minimal record. Don't invent decisions to populate an empty index.

If the project has multiple contexts, establish system-wide and context-specific locations only where needed. Future contributors should read records relevant to their work and surface contradictions rather than silently override an accepted decision.
