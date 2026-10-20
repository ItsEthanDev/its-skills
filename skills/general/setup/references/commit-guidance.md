# Commit guidance

Establish agent commit guidance for this Git-managed project. This applies to prose, research, learning materials, and software alike. A project that does not use Git does not need commit guidance.

Read existing project and personal instructions before proposing changes. Preserve explicit policy unless changing it is in scope. The agent-navigation seed supplies the proposed automatic-commit and staging-scope instructions for Git projects; keep those in the harness-loaded entry point, not in a second copy here.

Ask what is not already settled:

- Commit-message format, including whether to use Conventional Commits or the project's own format.
- Required verification or review, and what to do when a prerequisite is blocked.
- Branch restrictions and how commit requests differ from permission to push.
- How changes to these conventions are approved.

Use the commit-guidance seed to write instructions for agents. Default to `docs/agents/commits.md`, preserving an existing agent-guidance owner where appropriate. Index the guide under Agent documentation and add a direct consultation trigger in the agent entry point. Reference existing project-wide commit conventions rather than duplicate them.

Preserve the safeguards against redundant checks, inferring conventions from incidental history, and treating a commit request as push authorization. Keep the result-reporting instruction so agents report the commit hash and subject or the exact reason the commit failed.

Don't impose a message format merely because this skill has a preference. Surface conflicts with applicable instructions; a project file cannot silently override higher-priority constraints.

Document push/deployment effects by reference to their owners. Commit guidance is not permission to push or bypass protected-branch and deployment rules. Creating it does not authorize committing unrelated work during setup.
