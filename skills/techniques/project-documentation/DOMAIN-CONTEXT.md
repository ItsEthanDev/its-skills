# Domain Context

Read established project language when it affects the task. Create `CONTEXT.md` when the first consequential project-specific term or context boundary needs a durable definition, including early in specification work. Do not wait for a terminology dispute or large glossary; do not create a file for generic vocabulary. Use the repository's established location, otherwise use root `CONTEXT.md`. Create `CONTEXT-MAP.md` only when distinct contexts need explicit ownership and relationships.

When defining a term, compare how the user, current docs, and code use it. Test ordinary and edge cases that distinguish it from neighboring concepts. If two plausible meanings conflict, ask which is intended rather than inventing a synonym. Record the resolved meaning concisely in its owning context. Keep feature requirements, operational values, and technical choices in their own owners. For a consequential boundary tradeoff whose rationale must outlive the plan, use [decision records](DECISION-RECORDS.md).

The [context starter](templates/context.md) is optional; remove unused structure.
