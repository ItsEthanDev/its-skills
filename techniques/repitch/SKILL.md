---
name: repitch
description: Re-pitch an explanation when the user asks to repitch or says "wait what" as a clarification request. Re-pitch the complete preceding response unless the user names, quotes, or numbers a specific target.
---

# Repitch

The explanation did not land. Replace it with a simpler explanation rather than extending or defending it. Apply this skill to requests to repitch an explanation or to `wait what` used as a clarification request, not discussion of the phrase or skill.

1. Select the scope:
   - A standalone `repitch` or `wait what` targets the complete preceding assistant response.
   - In a numbered reply, `2. repitch` or `2. wait what` targets the complete question 2. A quotation or named reference similarly targets that complete item.
2. Retain the conversational state of every unaffected answer and decision without repeating them. Keep the target unresolved and do not advance dependent work.
3. Re-pitch the target from the beginning:
   - Give enough context to orient the user.
   - Present the ideas again in a simpler conceptual order.
   - Cover every core idea, relationship, decision, and question needed to retain the target's meaning.
   - Use ASD-STE100 Simplified Technical English and the ubiquitous language from the applicable `CONTEXT.md`; follow `CONTEXT-MAP.md` when the repository has more than one context.
   - Use concrete examples when they make the idea easier to understand.
4. Stop after the replacement explanation.

A re-pitch is not a summary of one selected point, an explanation of why the prior answer said something, or extra detail appended to it. It is a fresh, simpler explanation of the complete selected scope.
