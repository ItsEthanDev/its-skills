---
name: tdd
description: Develop features or repairs test-first through a red-green loop. Use when test-first development or red-green-refactor is requested or an accepted implementation approach requires it.
---

# Test-Driven Development

Use the red → green loop for the authorized implementation. Before writing tests, read [Automated tests](../verifying-work/references/automated-tests.md) for test quality, seam approval, and dependency substitution guidance. Reuse existing approval rather than ask again for each cycle.

## Run one behavioral slice

1. Write one focused test for the next selected behavior at an approved seam.
2. Run it and confirm that it fails for the missing or incorrect behavior, not a broken harness or unrelated error.
3. Implement only enough to pass that test. Do not anticipate future tests or add speculative features.
4. Run the test and relevant existing checks. Let the result inform the next slice.

Repeat for the next behavior within the assignment. Handle refactoring as separately authorized work under project rules, not as an implicit third step of the loop.

## Avoid horizontal slicing

Do not write all tests first and then all implementation. Bulk tests commit to imagined behavior and test structure before the last cycle has taught you what matters. Work in vertical slices: one test, one minimal implementation, then the next informed cycle.
