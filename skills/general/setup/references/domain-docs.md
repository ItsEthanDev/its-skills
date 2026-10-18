# Domain docs

Default to **single-context** (one root `GLOSSARY.md` + `docs/adr/`). Preserve an existing `GLOSSARY-MAP.md` layout. Offer **multi-context** only when exploration found genuinely distinct domain contexts; then confirm the layout and paths with the user.

Propose the candidate terms and definitions, following [glossary.md](../assets/glossary.md). Confirm them with the user before writing. Seed the glossary with agreed terms, not generic programming vocabulary or implementation details. If no terms can be established yet, use only the context heading, its description, and an empty `## Language` section. In a multi-context repo, establish the mapped glossaries rather than duplicating their terms in a root glossary.

Record layout and consumer rules in `docs/agents/domain.md`. Establish the ADR location without creating placeholder ADRs or empty directories. Decisions get records only when there is a consequential, agreed trade-off to capture.
