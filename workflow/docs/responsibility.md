# Responsibility Model

This document defines what the user owns, what AI owns, and where the decision boundary lies between them.

---

## User Responsibilities

The user is responsible for:

- **Initial goal** — providing the starting intent, problem, or desired outcome
- **Clarification participation** — answering questions and resolving ambiguities during spec formation
- **Strategic approvals** — signing off on decisions with long-term or architectural consequences
- **Direction** — correcting course when the project is heading the wrong way
- **Priority** — deciding what matters most when trade-offs must be made

The user does **not** need to:
- Manage implementation details
- Monitor step-by-step AI execution
- Approve routine code decisions
- Trigger doc updates manually
- Coordinate between tasks

---

## AI Responsibilities

AI is responsible for:

- **Requirement analysis** — reading and understanding what the user actually needs
- **Clarifying questions** — identifying and resolving ambiguity before spec is finalized
- **Spec formation** — driving the working spec and producing the approved spec
- **Task breakdown** — decomposing approved spec into independently verifiable tasks
- **Implementation** — writing code that delivers against the approved spec
- **Testing** — creating and running tests appropriate to the spec
- **Review** — conducting task, group, and integration review
- **Doc sync** — updating relevant documentation as part of every delivery
- **Proactive proposal** — surfacing improvements, risks, and issues discovered during execution
- **Delivery tracking** — maintaining awareness of task state, dependencies, and completion

---

## Decision Boundaries

### AI can decide and act autonomously (report after):

- Bugfixes within the current implementation
- Code quality improvements within the current scope
- Test coverage improvements
- Security hardening within the current design
- Refactoring that does not change external behavior
- Implementation choices that are consistent with the approved spec

### AI must ask before acting:

| Situation | Why |
|---|---|
| Approved spec needs to change | Spec is a locked contract; changes require re-approval |
| Architecture or foundational design change | Long-term consequences that user must own |
| New dependencies or significant new complexity | Affects maintainability and future choices |
| Scope expansion beyond what was approved | User has not committed to this work |
| Behavior visible to users is changing unexpectedly | User must understand and approve UX changes |
| Anything that contradicts a previous user decision | Cannot override user's expressed choices silently |

---

## The Core Principle

> **Users own intent, goals, and strategic direction.**
> **AI owns execution.**

This is not a symmetrical split. AI is trusted with a wide and deep execution domain. In return, it must not cross into the user's domain — which is the "why" and the long-term consequences of decisions.

The framework is designed so that users rarely need to be involved in execution. When they are pulled in, it should be because a decision genuinely requires their judgment — not because AI is uncertain about something it could resolve itself.
