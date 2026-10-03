# Implementation review

Review delivered work against intent, project authority, concrete correctness, maintainability, and direct evidence. Keep these axes distinct while returning one unified report; strength on one axis does not cancel a finding on another.

## Establish the selection

Use the scope requested by the user. A review may cover a supplied base, branch, working tree, selected files, complete feature, or another bounded implementation. Inspect version-control status and include untracked files when they belong to an uncommitted review. Do not require a comparison base when the request concerns a complete feature or artifact.

Read applicable governance, accepted behavior, technical design, execution state, repository standards, changed source, callers, callees, types, tests, and verification commands. State exclusions and any uncertainty about the selected surface.

## Inspect each axis

### Intent

- Every accepted requirement is delivered without missing behavior, incorrect interpretation, undocumented deviation, or scope creep.
- Delivered documentation and lifecycle state agree with actual behavior.

### Governance

- The implementation satisfies applicable project rules and documented standards.
- Tool-enforced style is left to the tool unless its configuration or result is itself under review.

### Correctness

- Normal, boundary, failure, retry, and recovery paths preserve the required behavior.
- Errors, mutable state, concurrency, authorization, validation, and external inputs are handled at the appropriate interface.
- A suspected defect traces a feasible execution or data path; generic possibilities remain hypotheses.

### Maintainability

- The change integrates with existing ownership and dependency direction rather than bolting on a parallel path.
- Complexity, dependencies, configuration, abstractions, and compatibility layers earn their place for the accepted scope.
- Interfaces preserve locality and testability, and names use established domain language.
- Debugging and operation remain understandable when the changed behavior fails.

### Evidence

- Tests and checks exercise observable behavior rather than implementation trivia or a proxy for the real result.
- Each accepted requirement has direct passing evidence, including meaningful integration paths and regressions where applicable.
- Reported command outcomes reflect commands the reviewer executed or durable records the reviewer inspected, not an agent's self-report.

## Keep the boundary

Keep main findings attributable to the reviewed selection. Report a pre-existing issue separately only when this work worsens it, depends on it, or makes proceeding unsafe. Security, performance, and operational findings must identify the concrete input, workload, failure path, or violated requirement that makes them relevant.

## Complete the lens

Account for each accepted requirement and each materially changed public interface in the selected implementation. Run direct checks within the main skill's maintained-content and generated-output limits when source inspection cannot prove behavior. Route behavioral disagreement, design disagreement, governance conflict, terminology conflict, and code or evidence defects to the project's corresponding canonical owners. Identify actual artifacts or locations rather than prescribe stages.
