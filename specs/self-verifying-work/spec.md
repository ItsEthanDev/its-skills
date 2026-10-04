# Self-Verifying Work

## Outcome

Agents exercise their work, use observed findings to guide authorized corrections, and support completion claims with appropriate evidence. Verification applies across the collection, with methods proportionate to the task. It does not impose software execution on conversational or documentation-only work.

The [constitution](../../CONSTITUTION.md), [skill roles](../skill-roles/spec.md), and [progressive disclosure](../progressive-disclosure/spec.md) govern this feature.

## Requirements

### SV-001: Two reusable skills

The collection MUST provide:

- **Verifying Work**, a technique selected when checking delivered behavior, investigating whether a change works, or preparing a completion claim.
- **Authoring Project Verification**, a playbook for an explicitly requested creation or maintenance of project-local verification guidance.

The playbook MUST use Authoring Skills for general skill-writing guidance and add only verification-specific discovery, protocol construction, validation, and maintenance instructions. A generated project verification skill SHOULD be a technique unless its actual operation requires another role.

### SV-002: Authoritative instruction owners

Assign shared guidance to these owners. Other skills MUST reference the owner where operational composition permits, rather than maintain competing versions of its rules.

| Owner | Guidance |
| --- | --- |
| Prove It Works | Evidence validity, matching an observation to a claim, and limits on completion claims |
| Verifying Work | Selecting and executing proportionate checks, preparing verification state, classifying findings, and reporting results |
| Verifying Work's automated-test resources | General test quality, test seams and their approval, assertions, examples, and dependency substitution |
| TDD | Red-green development cadence, one behavioral slice at a time, and separately authorized refactoring |
| Authoring Skills | General activation, skill structure, role classification, composition, disclosure, and portable script-writing guidance |
| Authoring Project Verification | Discovering project needs, creating or maintaining its verification protocol, and proving the resulting instructions |
| Project-local verification skill | Concrete commands, prerequisites, environments, fixtures, user interactions, expected observations, and cleanup |
| Implementation workflow | Correcting findings within the assignment and repeating verification after a correction |
| Diagnosing Bugs | Reproduction, minimization, causal investigation, instrumentation, and authorized repair |
| Project requirements and contracts | Intended behavior and consumer-facing agreements |
| Calling Web APIs | Permission and safeguards for real remote API operations |
| Show Me | Presentation of work for feedback |
| Development Review | Explicitly authorized independent judgment of a development target |
| Project Documentation | Durable artifact selection and reconciliation |
| Sequence Verifiable Units | Choosing independently checkable work units and delivery order |
| ItsSkills repository guidance and Nix-backed script specification | Dependency policy for scripts bundled and distributed by this collection |

Ownership explanations belong in authoring guidance and specifications, not scope metacommentary in runtime skills.

### SV-003: Claims before checks

Verifying Work MUST identify the requested result, affected behavior or artifacts, and authoritative expected observations before selecting checks. Check selection MUST consider plausible failures and the boundaries relevant to the claim. It MUST NOT derive the expected result solely from the implementation being checked.

The technique MUST use user direction, project conventions, and suitable existing harnesses before proposing new tooling. It MAY recommend technologies such as Vitest for suitable JavaScript or TypeScript tests and Playwright for browser interactions. A recommendation MUST NOT itself authorize dependency installation or configuration changes.

### SV-004: Exercise the relevant result

Checks MUST exercise the artifact or behavior relevant to their claim. A build supports a build claim, not proof of user-facing behavior. UI claims may require browser interaction; integration claims may require observation across the relevant boundary. Documentation checks may instead inspect sources, links, or executable examples.

Verification MUST capture enough of the action and resulting observation to interpret the result. It MUST distinguish a failed behavior check, an invalid check, missing prerequisites, and ambiguous intended behavior. An inconclusive result or a check on the wrong surface MUST NOT be reported as a pass.

### SV-005: Bounded execution and feedback

Verification MUST respect the assignment's permissions, maintenance limits, and external-access requirements. Read-only assignments MUST NOT acquire repair authority through verification. Running local code MUST NOT be assumed to exclude real service access.

An implementation workflow SHOULD correct failures within the existing assignment without another approval pause and then repeat the affected check and relevant regression checks. It MUST return broader changes, requirement ambiguity, and new external effects for an authorized decision. Persistent failure without new evidence MUST lead to a precise blocker or diagnosis finding rather than unbounded retries or weakened assertions.

### SV-006: Shared automated-test guidance

General test-quality and seam guidance MUST reside with Verifying Work, not be copied into TDD or the authoring playbook. TDD MUST reference that guidance while retaining its test-first cadence. Writing or running a verification test MUST NOT automatically activate a red-green development workflow.

Existing approval of a seam, including approval through a plan, MUST be reused. A new or changed seam requires confirmation before writing maintained tests. Temporary observation and existing test execution MUST NOT create a new universal seam-approval pause.

### SV-007: Project-local protocols

The authoring playbook MUST inspect the target project's requirements, skill conventions, documented commands, tests, dependencies, and permissions before constructing guidance. It MUST ask only for consequential facts or decisions that cannot be established from those sources.

The resulting skill MUST provide concrete, usable instructions for the relevant project branches, including:

- Launch or build commands and observable readiness or health checks.
- Suitable interaction surfaces and stable handles for automation.
- Relevant fixtures, authentication prerequisites, and isolated runtime state.
- Expected observations linked to authoritative behavior sources.
- Evidence capture and its useful lifetime.
- Cleanup of resources created by verification, including failed attempts.

Branch-specific feature recipes MAY form a small feature map when repeated use justifies one. The map MUST describe how to verify behavior without becoming a second requirements owner. It MUST expose coverage limits rather than imply exhaustive coverage from one exercised feature.

### SV-008: Maintenance distinguishes drift from regression

Maintenance MUST compare affected protocols with authoritative intent, implementation, and actual execution. A stale command or selector is protocol or harness drift; behavior contrary to accepted intent is a product regression. The playbook MUST NOT rewrite expected behavior merely to make a broken application pass.

Maintenance MUST remain within its authorized edit boundary. A request to maintain verification guidance does not itself authorize product repairs. Changed executable procedures MUST be exercised again before they are reported as verified.

### SV-009: Prove the authored procedure

The authoring playbook MUST execute the generated instructions for a representative feature, or the affected branches during maintenance, through setup, checks, evidence capture, and cleanup. A failed attempt MUST receive its own authorized cleanup. Reusable helpers MUST expose their invocation and observable success or failure.

Unexecuted branches MUST be identified as unverified. Missing tools, credentials, or permissions MUST be reported precisely. Partial proof MAY be delivered as a draft with explicit gaps, not as complete verification of the protocol.

### SV-010: Project conventions determine generated dependencies

Scripts created in another project MUST follow that project's tooling conventions and declare actual prerequisites. The [Nix-backed script requirements](../nix-backed-scripts/spec.md) apply only to scripts bundled and distributed by ItsSkills, not to code or skills generated in another project.

General Authoring Skills guidance MUST NOT prescribe ItsSkills paths, installation interfaces, or Nix dependency policy. Repository-local guidance MUST direct ItsSkills contributors to those requirements.

### SV-011: Acyclic composition

The intended operational directions are:

- Authoring Project Verification to Authoring Skills and Verifying Work.
- TDD to Verifying Work for automated-test quality and seam guidance.
- Verifying Work to Prove It Works, Calling Web APIs when needed, and a selected project-local verification technique.
- Implementation, diagnosis, and other authorized callers to Verifying Work where its checks apply.

A generated project-local verification skill MUST NOT invoke Verifying Work back. The generic technique MUST NOT initiate Authoring Project Verification, Diagnosing Bugs, a stage transition, or a formal review when it discovers a gap. It returns the finding to its caller. Composition MUST preserve activation conditions and the skill-role reference restrictions.

### SV-012: Proportionate resources and honest reporting

Verification SHOULD prefer deterministic, agent-runnable checks where they provide useful evidence. It MUST NOT require a universal test suite, mandatory retained report, feature map, browser session, or permanent harness for every task.

Reports MUST distinguish passed, failed, blocked, and unverified claims, with enough command or artifact context to locate the evidence. Temporary outputs MUST follow project conventions and confidentiality rules. Cleanup MUST NOT destroy evidence still needed to interpret or hand off a finding.

## Acceptance cases

- A browser-visible form change is checked through the relevant interaction; a passing build alone does not prove submission works.
- A documentation-only change uses applicable source, link, and example checks without launching an irrelevant browser or test suite.
- A local test that could reach a real API is checked against Calling Web APIs permissions before execution.
- A failure inside an authorized implementation assignment is corrected and rechecked; a read-only verification assignment reports the same finding without changing maintained content.
- A new maintained test uses shared test-quality guidance and existing seam approval without forcing test-first development.
- A project with an existing runner keeps its convention instead of adopting Vitest or Playwright solely because a skill mentions them.
- A generated project skill follows the target project's dependency conventions without requiring Nix solely because its authoring playbook comes from ItsSkills.
- A generated protocol is exercised through cleanup; unexecuted feature branches remain explicitly unverified.
- A maintenance run repairs a stale interaction recipe but reports a product regression without changing expected behavior.
- Shared test guidance has one source, and the operational reference graph contains no invocation cycle.

## Boundaries

This feature does not install consumer tooling, add a mandatory skill-evaluation framework, prescribe automatic formal review, or authorize publication, deployment, or real service effects. Platform-specific browser tooling and ItsSkills installation interfaces require their own verification.
