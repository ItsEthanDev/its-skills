# Plan

Use this stage when the accepted target leaves consequential approach, dependency, contract, or verification decisions unresolved. A separate planning stage is unnecessary when those decisions are already clear enough for authorized implementation.

Read the current target, project constraints, relevant interfaces, code, and tests. Investigate unknowns that could change the approach. A technical choice within accepted intent may be resolved here; an agent-proposed material behavior change requires user direction before changing the target.

Identify the smallest sufficient approach, contracts consumers rely on, dependencies, and direct evidence for the intended behavior. When interface depth, seams, or testability materially affect the design, read [Design Deep Modules](../../../principles/principle-design-deep-modules/SKILL.md). Use [Project Documentation](../../../techniques/project-documentation/SKILL.md) for contract, plan, or task ownership. These references do not expand design or implementation authority.

Record a plan or checklist only when it adds distinct value under project conventions. Resolve consumer-facing contracts before dependent work where the project requires that agreement.

The boundary is an approach with justified work, sufficient planned evidence, and no silently introduced product obligation. Report blockers and ownership conflicts. Proceed to Implement only when implementation is within the assignment; planning does not itself grant that permission.
