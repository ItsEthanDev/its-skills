---
name: propose-first
description: Propose a solution and pause before implementing when asked to "propose first" or explain a recommended approach before making changes.
---

# Propose First

When asked to propose first, explain a recommended change before implementing it. This is an opt-in pause before implementation, not a pause before investigation or a general approval gate for other requests.

1. **Investigate.** Find facts relevant to the request by reading, inspecting, and running checks within applicable project and action boundaries. Retrieve information and perform authorized discovery yourself rather than asking the user to do it. Use available, authorized subagents for independent discovery when useful. Continue unblocked investigation before asking for anything only the user can supply.
2. **Recommend.** Propose one proportionate solution grounded in the findings. State its scope and what you will implement and verify after approval. Include reasoning, assumptions, and alternatives only when they could change the decision. Mark the recommendation as provisional if missing user input could change it.
3. **Request.** Explicitly request the information, decisions, or actions needed from the user to continue, including actions outside your reach. Omit inapplicable categories and do not request secrets in chat. End with one question:
   - **Blocked:** Ask for the next missing input or offer to walk the user through the required action. A "yes" to an offer of help is not implementation approval.
   - **Ready:** Say: "No additional information or action is needed from you." Ask: "Do you approve this recommendation so I can implement it?" A "yes" to this question approves the described change.
4. **Wait.** Do not implement until blockers are resolved and the recommendation is approved. Continue investigation or discussion as needed. If new information changes the approach, present the revised recommendation and request approval. Supplied facts and follow-up questions alone are not approval.

Present the proposal under these headings in order:

- **Findings:** Briefly state relevant facts and unresolved uncertainties.
- **Recommendation:** State the proposed solution, scope, and consequential reasoning.
- **Next Steps:** Always include this section. State what the user needs to supply or do, or that nothing is needed beyond approval. Place the closing question here.

Approval of the proposal covers only the described change.
