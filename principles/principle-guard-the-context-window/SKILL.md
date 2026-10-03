---
name: principle-guard-the-context-window
description: "Apply when large outputs, long documents, repeated reads, or parallel exploration threaten useful context. Keep decision-relevant evidence accessible without flooding the main conversation."
disable-model-invocation: true
---

# Guard the Context Window

Context is limited. Large irrelevant payloads can displace the information needed for a sound decision, and summarization can lose important detail. Every loaded resource should serve the current work.

- Read selectively by relevance. Avoid loading material that cannot affect the assignment.
- Bound verbose output and retain a retrievable source for detail that may matter later.
- Use delegation when it is available, authorized, and cheaper or more reliable than handling the payload directly. Require enough evidence in the summary to support the decision.
- Without suitable delegation, prefer targeted reads, filtering, and concise summaries rather than assume a particular agent facility exists.
- Keep guidance needed on every invocation in the main skill. Disclose specialized branches only when relevant.
- Consider selection and retrieval costs as well as raw token count. A summary that hides decisive uncertainty is not an improvement.

This principle constrains context use; it does not prescribe phase sizes, turn budgets, mandatory delegation, or authority to launch work.
