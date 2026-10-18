# ItsSkills

ItsSkills is a collection of reusable agent instructions and their supporting resources.

## Skills

**Skill**:
A reusable set of agent instructions with a defined invocation boundary.

**Skill bundle**:
A skill's instructions together with its supporting resources, provenance,
and license notices.

**Task domain**:
The kind of work a skill supports, such as software engineering or learning.
Cross-domain skills support work across multiple task domains.

## Planning and tracking

**Issue**:
A tracker record that can hold a plan or a ticket.

**Plan**:
A description of an intended outcome. It may be broken down into tickets
that define the work toward that outcome.

**Ticket**:
A bounded unit of work toward a plan's outcome, with explicit completion criteria.
A ticket describes and tracks the work; it is distinct from performing that work.

## Wayfinding

**Wayfinding**:
The process of resolving questions and uncertainties to reach a decision
or set of decisions.

**Wayfinding map**:
A plan whose intended outcome is a decision or set of decisions.
Its decision tickets resolve questions needed to reach that outcome.

**Decision ticket**:
A ticket whose completion resolves a question needed to advance a wayfinding map,
or completes prerequisite work that unblocks such a question.
Its type—alignment, research, prototype, or task—prescribes how it is worked.

## Engineering

**Spec**:
A plan defining an intended change and the criteria for accepting its implementation.
Its implementation tickets deliver and verify parts of that change.

**Implementation ticket**:
A ticket whose completion delivers and verifies a bounded part of a specified change.

## Learning

**Learning objective**:
What the learner wants to understand or be able to do.

**Learning map**:
A plan for achieving a learning objective through learning activities.
It adapts until the learner confirms that their objective has been achieved.

**Learning ticket**:
A ticket describing and tracking a learning activity that advances a learning objective.
Completing the ticket does not by itself establish achievement of the objective.

**Learning activity**:
Something the learner performs to advance their learning objective,
optionally with agent assistance.
