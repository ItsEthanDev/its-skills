# Documentation discovery

Make the project's guidance discoverable without requiring people or skills to know its filenames. The README indexes guidance by purpose; the agent entry point indexes it by consultation trigger. Repeating destinations is intentional. Keep procedures in their canonical owners rather than duplicate them in either index.

## README index

Add or update Project documentation and Agent documentation sections in the README. Put human-facing artifacts in Project documentation; put harness instructions and procedural guides in Agent documentation. Use recognizable roles as link labels: Quickstart, Deployment, Glossary, Decision records, Constitution, Domain guidance. Include the selected features and existing guidance, not a list of broken links to documents that might exist someday. Preserve links to existing coding standards, commit guidance, and tool documentation; these are not separate setup features.

Link to the canonical owner of each topic. A guide can own several topics; don't split it merely to match the feature list. Preserve useful existing content and links. When moving an owner, reconcile affected pointers and consumers rather than leaving two competing policies.

If the user explicitly declines a workflow that later agents might otherwise expect, record that choice briefly in existing guidance. "This project does not use an issue tracker" is enough; it does not need its own file.

## Agent entry point

Edit root `AGENTS.md` if it exists; create it if the user wants agent guidance and it does not. Use the project's harness equivalent when appropriate. Preserve user edits and unrelated sections.

Use the agent-navigation seed as a starting point. Point to the actual README sections and include direct, conditional links to each selected guide in the instruction file the harness actually loads. Adapt links relative to that file. Keep the procedures in their owning docs rather than copying them into the entry point.

For projects that use Git, propose the seed's inline Commits section with the rest of the agent instructions; it does not require a separate commit-guidance document. Omit it when the project does not use Git; do not initialize a repository merely to install the instruction. Preserve existing explicit policy unless changing it is in scope. On scoped runs, update only the requested feature and necessary discovery links rather than replacing unrelated operating instructions.

## Self-contained conventions

Each selected guide should explain its purpose, when to use it, and how accepted changes are recorded. Record the project's approval requirements where applicable. An agent maintaining an existing guide should not need to reconstruct the conventions from the setup skill that created it.
