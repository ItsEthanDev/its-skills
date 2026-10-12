---
name: propose-first
description: Propose a solution and pause before implementing when asked to "propose first" or explain a recommended approach before making changes.
---

# Propose First

When asked to propose first, explain a recommended change before implementing it. This is an opt-in pause before implementation, not a pause before investigation or a general approval gate for other requests.

1. **Investigate.** Find facts relevant to the request by reading, inspecting, and running checks within applicable project and action boundaries. Retrieve information and perform authorized discovery yourself rather than asking the user to do it. Use available, authorized subagents for independent discovery when useful. Continue unblocked investigation before asking for anything only the user can supply. Do not make the proposed change yet.
2. **Recommend.** Propose one proportionate solution grounded in the findings. State its scope and what you will implement and verify after approval. Include reasoning, assumptions, and alternatives only when they could change the decision. Mark the recommendation as provisional if missing user input could change it.
3. **Next Steps.** Always include this section. Explicitly request the information, decisions, or actions needed from the user to continue, including actions outside your reach. Omit inapplicable categories and do not request secrets in chat. If nothing is needed beyond approval, say: "No additional information or action is needed from you."
4. **Stop.** End with one question and wait. If there are no user blockers, ask: "Do you approve this recommendation so I can implement it?" A "yes" to this question approves the described change. If user input or action is blocking, ask for the next missing input or offer to walk the user through the required action. A "yes" to an offer of help is not implementation approval. Resolve blockers, revise the recommendation if needed, and request approval before implementing. Supplied facts and follow-up questions alone are not approval.

Present the proposal under `Investigate`, `Recommend`, and `Next Steps` headings in that order. Keep findings brief and place the closing question at the end of `Next Steps`. Stop is a behavior, not an output section.

Approval of the proposal covers only the described change.
