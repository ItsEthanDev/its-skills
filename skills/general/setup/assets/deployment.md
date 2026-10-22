# Deployment

<What is deployed or distributed, to which platform, and through which workflow. For a project with neither deployment nor distribution, replace this template with a brief statement of that fact.>

## Environments and access

<Environments, their purpose, and required permissions. Name secret/configuration sources without including secret values. Explain how configuration reaches each environment and which changes require separate remote action.>

## Deploy or release

<What triggers a release: branch push, tag, pull-request merge, CI action, or manual command. Identify consequential branch/remote targets so contributors can assess a proposed push. Give the exact procedure or link to its authoritative runbook. Include required checks and approvals.>

<Identify the source workflow or infrastructure configuration rather than copying its implementation here.>

## Verify

<Where to check rollout status, which smoke checks to run, and what success looks like.>

## Roll back or recover

<How to select and restore a known-good version, or link to the authoritative recovery procedure. Note constraints such as irreversible migrations. If no recovery procedure is established, state that gap explicitly.>

## Verification limits and maintenance

<Standing limits of the verification procedure, any procedures not yet verified, and who approves changes to this workflow. Keep run-specific results and transitional context out of this runbook.>

Documented procedures do not grant permission to push, publish, deploy, or change remote configuration. Obtain the authorization required by the project and applicable instructions.

<!-- Seed instructions: document the current workflow, not a history of deployments or setup checks. Report setup results in the completion response; retained historical evidence belongs in the configured issue tracker. Standing documentation links to the tracker only for general discovery, not to specific issues or pull requests or topic-specific searches. Keep the runbook usable without the tracker. Replace placeholders with observed facts or explicit gaps. If no deployment or distribution applies, a brief statement in existing guidance may replace this file. Remove this comment before writing. -->
