---
name: authoring-skills
description: Create or revise an agent skill.
disable-model-invocation: true
---

# Authoring Skills

Create or revise a skill that changes how an agent acts on a recognizable task. Read the target project's governance, specifications, and skill conventions before writing. Read the existing skill and nearby capabilities when revising one; identify overlap before adding a new one. Keep the work within the authorized assignment and surface conflicts with project rules rather than silently overriding them.

## Choose a role

Choose one primary role by the decision the skill owns. Apply the same classification to imported and adapted skills:

- **Stage:** Define the enclosing workflow's work state, prerequisites, transition gates, and transition authority. Leave the strategy for solving a particular problem to a playbook.
- **Playbook:** Provide a reusable strategy for a problem or outcome, including internal checkpoints. Leave the enclosing workflow's stage transitions to stages.
- **Technique:** Define a bounded, reusable operation and its result. Leave the purpose and strategy of the larger task to its playbook or requester.
- **Principle:** Constrain judgment so a choice can change or be rejected. Do not turn the principle into a task sequence.

Ask which decision an overlapping instruction makes, then put it with that decision's owner. For example, readiness to leave an implementation stage is a stage gate; requiring reproduction before patching can be a diagnosis playbook checkpoint; tracing a code path is a technique.

For this collection, place each skill at `<role-directory>/<skill-name>/SKILL.md`, using `stages`, `playbooks`, `techniques`, or `principles`. Role does not require a router or determine invocation. A stage may be an individual skill or a router for multiple stages.

## Choose activation

Define the skill's own activation conditions. Decide whether the agent should select it or a person should invoke it explicitly.

For agent selection, write a description that names the capability and distinct positive cases that should trigger it. Lead with words a request is likely to use; describe each case once rather than listing synonyms or exclusions.

For explicit invocation, use the target harness's supported manual-invocation metadata and a short human-facing description. Check supported frontmatter rather than assuming one format works everywhere.

Make special pause or question behavior clear when it affects execution. State a stopping condition where the skill needs one; do not impose a uniform interaction mode or completion report.

## Shape the skill

Put guidance needed on every invocation in the main file. Place branch-specific detail in supporting resources with clear instructions for when to read them. Require the selected branch's resources before relying on their instructions, not unconditional loading of every reference.

Keep one skill when the material shares an invocation and purpose. A distinct reason for independent invocation may justify a separate skill. Use a router when it improves selection among related material; keep it focused on selection and leave detailed instructions with their owners. Directory nesting alone does not hide discovered skill descriptions.

Write reusable procedure in the skill. Find project policy, paths, commands, and other local facts in the target project's own sources rather than treating one environment as universal.

Omit scope metacommentary from the skill and its supporting references. Do not narrate its role, what it owns, or which responsibilities belong elsewhere. Let its name, activation conditions, and instructions establish scope. Use the role model to decide what to write, not as prose to insert into the finished skill. Preserve concrete activation, handoff, authorization, and safety instructions that change behavior.

## Check operational references

Treat an instruction to load, invoke, or follow another skill as an operational reference. Apply these allowed directions to both the main file and supporting resources:

- Stages may reference stages, playbooks, techniques, and principles.
- Playbooks may reference playbooks, techniques, and principles.
- Techniques may reference techniques and principles.
- Principles may reference principles.

Explanatory mentions do not create operational dependencies. Refer to an instruction's owner rather than copy its rules, but only when that operational reference is permitted.

Preserve the caller's authorized boundary on every call, including cross-role calls; a narrower assignment is allowed. References do not grant execution authority or bypass activation conditions. Avoid circular invocation or delegation chains. Return results and control to the caller; report broader needs rather than initiating a forbidden workflow or expanding scope without an authorized decision.

## Delegate mechanics to scripts

Put repeatable execution in a script when it makes the operation more reliable. Keep invocation criteria, authorization decisions, and unresolved judgment in the skill. Let the script own its interface and implemented behavior; point to its help instead of duplicating arguments, defaults, checks, or execution steps.

When adding or revising a bundled script, read [Writing skill scripts](references/scripts.md). Bundled scripts require Nix and obtain tool dependencies through repository-owned declarations. Guidance-only skills remain usable without Nix.

## Prune and check

When in doubt, delete. Keep prose that changes a decision or action. Remove scope narration and self-description that add no operational instruction. Skip the reason unless the rule would be confusing without it. Match tone and detail to scope.

Check the role, source location, activation setting, operational references, bundled resources, and links. Check the target harness's required frontmatter and supported invocation behavior. For an agent-selected skill, compare its description with representative requests; for an explicitly invoked skill, check its loading path or command where available.

Provide representative cases for the maintainer to evaluate. Distinguish structural checks from observed agent behavior, and report what was checked and what remains unverified. When installation paths are available, verify that both retain the skill's required resources.
