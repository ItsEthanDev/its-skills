# Documentation discovery

Make the project's guidance discoverable by purpose, without requiring people or skills to know its filenames.

## README index

Add or update a documentation section in the README. Use recognizable roles as link labels: Quickstart, Deployment, Issue tracker, Domain language, Decision records, Constitution, Coding standards, Commit guidance. Include the selected features, not a list of broken links to documents that might exist someday.

Link to the canonical owner of each topic. A guide can own several topics; don't split it merely to match the feature list. Preserve useful existing content and links. When moving an owner, reconcile affected pointers and consumers rather than leaving two competing policies.

If the user explicitly declines a workflow that later agents might otherwise expect, record that choice briefly in existing guidance. "This project does not use an issue tracker" is enough; it does not need its own file.

## Agent entry point

Edit root `AGENTS.md` if it exists; create it if the user wants agent guidance and it does not. Use the project's harness equivalent when appropriate. If an `## Agent skills` block already exists, update its contents in-place rather than appending a duplicate. Preserve user edits and unrelated sections.

Use the agent-navigation seed as a starting point. Point to the actual README documentation section and name the conditions for consulting the linked guidance. Keep the procedures in their owning docs rather than copying them into the entry point.

A missing document is not permission to invent policy. Tell agents how to handle required guidance that cannot be found, and distinguish it from guidance the project explicitly does not use. Optional guidance must not block unrelated work.

## Self-contained conventions

Each selected guide should explain its purpose, when to use it, and how accepted changes are recorded. Record the project's approval requirements where applicable. An agent maintaining an existing guide should not need to reconstruct the conventions from the setup skill that created it.

The user may later invoke scoped setup to establish a feature they did not select initially. Agents are not responsible for guaranteeing that every possible guidance document eventually exists.
