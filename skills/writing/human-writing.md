# Human writing

Write technical prose that a tired engineer can understand on the first read. Prefer clarity and precision over compliance with a mechanical style rule.

## Choose the document mode

For documentation, choose one dominant Diátaxis mode before drafting:

- **Tutorial:** Help a learner build something through a sequence of visible results. State what they will build, give concrete steps, and show expected output. Keep explanation brief and link to it when needed.
- **How-to:** Help a competent reader reach a specific goal. Lead with the task, provide the necessary steps and decision points, and leave background material elsewhere.
- **Reference:** Provide facts for lookup. Mirror the structure of the system described and cover its options, limits, errors, and defaults without persuasion.
- **Explanation:** Help the reader understand one bounded topic. Address why it works this way, including context, constraints, alternatives, and tradeoffs.

Split and link when substantial sections serve different modes. PR descriptions, commit messages, RFCs, and ADRs have their own established forms; do not force them into Diátaxis.

## Use the repository's language

- Use real symbols, paths, commands, flags, and product terms.
- Call one thing by one name throughout the artifact.
- Prefer a short, familiar word unless a technical term is more precise.
- Define necessary domain terms on first use. Do not invent a synonym for an established term.
- Verify changing facts against code, configuration, tests, or another authoritative source.

## Write direct sentences

- Address the reader as “you” when giving guidance.
- Use present tense for current behavior.
- Name the actor and action. Prefer “the compiler checks the type” to “the type is checked.”
- Write instructions as commands.
- Put a condition before the action it controls: “To delete the cache, run...”
- Present the common case before exceptions.
- Keep one main thought or instruction in each sentence. Split a sentence when its clauses require separate attention.
- Place modifiers such as “only” and “not” next to what they modify.
- Make every pronoun point to one obvious noun. Repeat the noun when needed.
- Break up noun strings that a reader could group in multiple ways.
- Remove filler, throat-clearing, unnecessary hedging, and words that repeat the sentence's meaning.
- Vary sentence length when it improves rhythm. Do not sacrifice clarity to a word-count target.

## Make structure carry meaning

- Lead with the information or action the reader needs.
- Use headings that state the point or task, not merely its broad topic.
- Use numbered lists for sequences and bullets for unordered sets.
- Introduce a list with a complete sentence and keep its items grammatically parallel.
- Use descriptive link text that identifies the destination.
- Put code, commands, paths, and symbols in code formatting.
- Include expected output when it helps the reader determine whether a step worked.
- Keep examples realistic, minimal, and consistent with the current repository.

## Respect the artifact

- A tutorial teaches through successful action.
- A how-to stays focused on accomplishing the task.
- Reference material remains complete and easy to scan.
- Explanation takes a position when interpreting tradeoffs.
- An RFC makes the problem, constraints, alternatives, and unresolved decisions visible.
- An ADR preserves the consequential choice and why it won.
- A PR description explains user or maintainer impact, the chosen approach, and verification.
- A commit message states what changed and why; it does not narrate the editing process.

Follow an established project template or voice before these defaults.

## Completion checklist

- Is the intended reader and purpose evident from the opening?
- Does each section serve that reader and purpose?
- Are instructions direct, ordered, and guarded by conditions where necessary?
- Can any sentence be read in two materially different ways?
- Does each concept have one consistent name?
- Are headings, lists, examples, and links useful rather than decorative?
- Are all symbols, paths, commands, outputs, and factual claims accurate now?
- Can any sentence or section be removed without losing useful meaning?
