# Domain Docs

How agents should consume this repo's domain documentation when exploring the codebase.

## Before exploring, read these

- **`GLOSSARY.md`** at the repo root, or
- **`GLOSSARY-MAP.md`** at the repo root if it exists: it points at one `GLOSSARY.md` per context. Read each one relevant to the topic.
- **`docs/adr/`**: read ADRs that touch the area you're about to work in. In multi-context repos, also check the context-specific ADR locations listed below.

If any of these files don't exist, proceed silently. Create domain records when terms or consequential decisions are resolved, not merely because a directory is missing.

## File structure

<Replace this paragraph with the agreed layout: root GLOSSARY.md and docs/adr/ for a single context, or GLOSSARY-MAP.md, its glossary paths, and the system-wide and context-specific ADR locations for multiple contexts. ADR directories need not exist until the first record is written.>

## Use the glossary's vocabulary

When your output names a domain concept (in an issue title, a refactor proposal, a hypothesis, a test name), use the term as defined in the relevant `GLOSSARY.md`. Don't drift to synonyms the glossary explicitly avoids.

If the concept you need isn't in the glossary yet, reconsider whether you're inventing language the project doesn't use or identifying a real gap. Use `domain-language` when available to resolve and record terms; otherwise confirm the definition with the user before adding it. Keep the glossary free of implementation details.

## Flag ADR conflicts

If your output contradicts an existing ADR, surface it explicitly rather than silently overriding:

> Contradicts ADR-0007 (event-sourced orders), but worth reopening because…

Use `decision-records` when available to record consequential decisions. Create an ADR only for an agreed trade-off that is hard to reverse and surprising without context; follow the repo's existing record format.
