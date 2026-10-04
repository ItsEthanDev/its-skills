---
name: commit
description: Stage and commit changes, defaulting to Conventional Commits. Push only when the user explicitly requests it.
---

# Commit

1. Use the current task context to identify the completed work. Inspect Git status and diffs only as needed to select its paths and write the message; do not repeat checks or perform a review unless the user explicitly requests it.
2. Stage only the changes belonging to that work. Ask only when unrelated changes make the intended commit scope materially ambiguous.
3. Create a concise Conventional Commit message that states the purpose of the change, unless the user requests another format or explicit project guidance specifies one. Do not infer a competing convention merely from ad hoc commit history.
4. Report the commit hash and subject, or the exact reason the commit failed.

Push only when the user explicitly requests it. A request to commit does not imply permission to push. Before pushing, verify the branch and remote.
