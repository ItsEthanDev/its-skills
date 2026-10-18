# Decision records

Establish where consequential decisions and their rationale belong when the user wants decision records. Keep this separate from the glossary: the glossary owns what terms mean; decision records own what was decided and why.

Preserve an existing location and format. Otherwise, propose a location such as `docs/adr/`, naming and numbering conventions, status handling, and how later decisions supersede earlier ones. Confirm who accepts decisions and what kinds of trade-off warrant a record. Use `decision-records` when available to help assess or draft an actual ADR; it owns that reusable method.

Use the decision-record index seed to record these conventions and maintenance instructions. Link that index from the README. Create the index when this feature is selected, not placeholder ADRs. Decisions get individual records only when there is a consequential, agreed trade-off to capture.

The index must explain how to add and maintain records without requiring an installed skill or its template. Match the project's own format; a short title and a paragraph can be enough when the user wants a minimal record. Don't invent decisions to populate an empty index.

If the project has multiple contexts, establish system-wide and context-specific locations only where needed. Future contributors should read records relevant to their work and surface contradictions rather than silently override an accepted decision.
