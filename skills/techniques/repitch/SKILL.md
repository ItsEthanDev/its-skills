---
name: repitch
description: Re-pitch an message or part of a message. Use when the user asks you to rexplain yourself, re-pitch or says "wait what"
---

# Repitch

The explanation did not land. Replace it with a simpler explanation rather than extending or defending it.

1. Select the scope:
   - A standalone `repitch` targets the complete preceding assistant response.
   - In a sectioned reply, `repitch` targets only that section.
2. Retain the conversational state of every unaffected answer and decision without repeating them. Keep the target unresolved and do not advance dependent work.
3. Re-pitch the target from the beginning. Give the user a bit of context, talk in ASD-STE100 Simplified Technical English, and use the ubiquitous language from GLOSSARY.md (follow GLOSSARY-MAP.md to the right one if the repo has more than one).
4. Stop after the replacement explanation.
