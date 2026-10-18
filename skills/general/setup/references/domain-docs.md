# Domain language

Default to **single-context** (one root `GLOSSARY.md`). Preserve an existing `GLOSSARY-MAP.md` layout or equivalent linked owner. Offer **multi-context** only when exploration found genuinely distinct domain contexts; then confirm the layout and paths with the user.

Identify a small set of domain terms from existing docs and work products. Distinguish candidate definitions from definitions already agreed in a glossary; flag contradictions rather than silently resolving them. Use `domain-language` when available to help resolve the terminology; the resulting project guidance must explain its own maintenance conventions.

Propose the candidate terms and definitions, following the glossary seed. Confirm them with the user before writing. Seed the glossary with agreed terms, not generic programming vocabulary or implementation details. If no terms can be established yet and the user wants the glossary in place, use only the context heading, its description, and an empty `## Language` section. In a multi-context project, establish the mapped glossaries rather than duplicating their terms at the root.

Record layout and consumer rules in the project's domain guidance. Use the domain seed to explain when to consult the glossary, use its vocabulary, and confirm new terms before recording them. Link the glossary or map from the documentation index.

Decision records are a separate feature. If selected, link to their agreed index rather than prescribing an ADR directory as part of language setup. A writing or learning project can have domain language without architectural decisions.
