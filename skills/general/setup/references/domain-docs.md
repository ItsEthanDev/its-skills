# Domain language

Default to **single-context** (one root `GLOSSARY.md`). Preserve an existing `GLOSSARY-MAP.md` layout or equivalent linked owner. Offer **multi-context** only when exploration found genuinely distinct domain contexts; then confirm the layout and paths with the user.

Identify a small set of domain terms from existing docs and work products. Distinguish candidate definitions from definitions already agreed in a glossary; flag contradictions rather than silently resolving them. Use the active practice and definition guidance in the domain seed as a proposed starting point, not as policy automatically imposed on an existing project.

Propose the candidate terms and definitions, following the glossary seed. Confirm them with the user before writing. Seed the glossary with agreed terms, not generic programming vocabulary or implementation details. If no terms can be established yet and the user wants the glossary in place, use only the context heading, its description, and an empty `## Language` section. In a multi-context project, establish the mapped glossaries rather than duplicating their terms at the root.

Record layout and consumer rules in the project's domain guidance. Preserve the seed's active discipline where applicable: challenge conflicting terms, sharpen fuzzy language, discuss concrete scenarios, cross-reference project work, and capture resolved terms inline. Confirm the definition format and any explicit additional approval requirements. Agreement on a definition should authorize recording it without another approval round unless the project deliberately requires more. Link the glossary or map and its domain guidance from the documentation index; each glossary links back to that guidance using its actual relative path.

Decision records are a separate feature. If selected, link to their agreed index rather than prescribing an ADR directory as part of language setup. A writing or learning project can have domain language without architectural decisions.
