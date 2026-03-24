# Project Constitution

> This file contains immutable architectural principles. Do NOT edit without explicit user approval and documented rationale.

## Article I — Test-First

No implementation code before acceptance criteria are defined and tests are written.
Tests must FAIL before implementation begins (RED phase).

## Article II — Simplicity

Maximum 3 new dependencies per feature. Additional require documented justification.
No future-proofing. Build for current requirements only.

## Article III — Evidence

Every claim about system behavior must cite file:line or test output.
"It should work" is not evidence.

## Article IV — Delegation

Orchestrator never writes complex code. All implementation via subagents.
Reviewers are independent — never the same subagent that implemented.

---

_Amendments require: explicit user approval + rationale documented here._
