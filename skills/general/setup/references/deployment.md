# Deployment and distribution

Establish how a change reaches a deployed environment or a distributed release, how to verify it, and how to roll it back. Deployment guidance is for people and agents, not just a release checklist.

Read release workflows and infrastructure configuration before asking about facts the project already records. Establish:

- What is deployed or distributed, where, and from which source revision.
- What triggers a release: a branch push, tag, pull-request merge, CI action, or manual command. Identify which targets have consequential effects; don't describe a push as safe without checking them.
- Required checks, approval, access, and configuration sources. Name secrets without including their values.
- How environment variables and other configuration reach each environment. Distinguish local edits from remote configuration changes and identify who must perform them.
- How to observe success, which smoke checks apply, and how to select and restore a known-good version.

Ask about missing operational facts; do not invent infrastructure or release procedures. Identify the source workflow or runbook instead of copying its implementation. If no recovery procedure is established, state that gap explicitly.

Use the deployment seed template as a starting point. If the project is not deployed, document its distribution workflow. If neither applies, a brief statement in existing guidance may be enough; create a dedicated file only when the user wants one.

If a local change needs a separate production configuration change, document the dependency and propose a task through the configured tracker when appropriate. Do not create a remote issue or change production merely to complete setup without authorization.

Keep the runbook about the current workflow: prerequisites, commands, expected results, standing verification limits, and maintenance. Distinguish those limits from evidence about a particular run. Report setup verification results in the completion response; retain historical receipts and transitional work in the configured tracker under the standing-documentation rules in the setup process. Do not copy revision-specific results, completed-migration narratives, or topic-specific tracker pointers into the runbook.

Documenting procedures does not grant permission to push, deploy, publish, or change environment configuration. Verification during setup stays within approved effects; state any unverified procedure without adding a run history. Retaining evidence in the tracker requires separate authorization for any tracker writes.
