# Commit guidance

Contributors consult this guidance before committing project changes.

## When to commit

<Agreed policy for human and agent commits: on request, at checkpoints, after completed work, or another policy.>

## Prerequisites

<Required verification or review and what to do if a prerequisite is blocked. Link to the owning check guidance rather than duplicating commands.>

## Procedure

1. Use the current task context to identify the work eligible for a commit under the policy above. Inspect Git status and the relevant diffs to select its paths.
2. Stage only the changes belonging to that work. Ask when unrelated changes make the intended scope materially ambiguous.
3. Create a concise message using <the agreed message format and any required metadata>.
4. Report the commit hash and subject, or the exact reason the commit failed.

## Branches and publication

<Branch restrictions, review requirements, and where push/deployment effects and authorization are documented.>

A request to commit does not imply permission to push. Before an authorized push, verify the branch, remote, and documented consequential effects. Surface conflicting instructions rather than treating this document as an override of higher-priority constraints.

## Maintenance

Changes to this policy require <the agreed approval process>. Record the approved change here and reconcile affected project instructions.

<!-- Seed instructions: confirm timing, format, prerequisites, and approval requirements. Do not adopt automatic commits or Conventional Commits by default. Replace placeholders and remove this comment before writing. -->
