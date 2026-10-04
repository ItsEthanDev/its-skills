# Implement

Use this stage for authorized delivery when the intended behavior and approach are sufficiently clear. The approach may be captured in a plan, established by project conventions, or resolved directly for a small change. Separate Plan work and planning files are not universal prerequisites.

Read the current target, applicable approach, work state, and affected implementation. Use an appropriate playbook or technique when its activation conditions apply; otherwise follow the accepted approach and project rules. Let those owners supply the execution method rather than prescribe a universal baseline/change/check loop here.

For authorized behavior-preserving structural work, use `refactoring`. Keep discovered defects and feature opportunities separate unless the assignment covers their implementation.

Apply the verification obligations and completion gates established by the project and accepted assignment. Use `verifying-work` for direct checks of delivered work. Correct findings within the existing implementation assignment without another approval pause, then repeat the affected check and relevant regression checks. Return requirement ambiguity, broader repairs, or new external effects for an authorized decision instead of expanding the assignment. Record task completion only after its result is verified. Inspect delivered artifacts and direct evidence, including delegated work, and report checks, results, and limitations. A completed task list alone is not evidence that the intended behavior was delivered.

When implementation reveals a changed premise, distinguish a technical adjustment, material target change, and operational value. Reconcile affected owners through `project-documentation`. A user-directed change needs no second approval; an agent-proposed material target change requires direction. An out-of-scope need is a finding to return, not authority to start another stage.

Use `development-review` only when explicitly requested or scheduled by an authoritative project artifact at this boundary. One scheduled review authorizes one pass. Implementation, delegation, a failed check, or stage completion alone does not authorize formal review.

The boundary is delivered behavior compared against the current target, with evidence and unmet obligations explicit. Return results and control to the caller. Do not conceal gaps with a status change or infer permission to publish or deploy.
