# Docs Architecture

Docs are the project's living memory. They are not generated once and left to rot — they are actively maintained as a reflection of the real system.

---

## Two Zones

### Long-Term Docs

High-authority. Contains knowledge that persists across all sessions and all contributors.

**What lives here:**

| Document Type | Purpose |
|---|---|
| `overview.md` | Project identity, goals, current state |
| `architecture.md` | System design, major components, relationships |
| `requirements.md` | What the system must do (high level) |
| `specs/` | Approved specs (one per feature/change) |
| `features/` | Feature map — what exists and what it does |
| `use-cases/` | Concrete use cases and expected behavior |
| `adr/` | Architecture Decision Records — decisions and their reasoning |
| `dev/` | Developer guide — setup, conventions, contribution rules |
| `testing.md` | Testing strategy and quality expectations |
| `status.md` | Current project state, in-progress work, known issues |

**Rules for long-term docs:**
- Content must be accurate at the time of writing
- Must be updated as part of any delivery that changes what is documented
- Must not contain speculation or aspirational statements presented as fact
- Must be kept concise enough to be read — if a doc becomes too long, split it

---

### Temp / Session Docs

Low-authority. Workspace for thinking during a session or delivery cycle.

**What lives here:**

| Content Type | Purpose |
|---|---|
| Brainstorm notes | Exploring ideas before spec is formed |
| Working spec drafts | Spec layers 1 and 2 before approval |
| Scratch analysis | Understanding existing code or behavior |
| Agent working notes | Intermediate state during task execution |
| Session summaries | What happened in a working session |

**Rules for temp docs:**
- Created freely during work — no overhead
- Discarded after the session or delivery cycle unless promoted
- Never treated as a source of truth
- Not linked from long-term docs

---

## The Promote Rule

Content moves from temp to long-term only if it satisfies at least one of these criteria:

1. **It has long-term value** — it will be needed in future sessions or by future contributors
2. **It affects how the system is understood** — removing it would leave someone confused about the project
3. **It reflects a change in requirement, spec, or design** — it represents what the project has committed to
4. **It is a decision that needs traceability** — it answers "why was this built this way"
5. **It is needed to maintain the system** — future AI or human contributors will need it to work safely

If content does not meet any of these criteria, it does not get promoted.

---

## Doc Sync Is Part of Done

Doc updates are not optional. They are part of the definition of done for every task.

When a task changes behavior, architecture, or constraints, the relevant docs must be updated in the same delivery. A change is not complete until the docs reflect it.

The orchestrator checks doc sync status during group review and final integration review.

---

## Doc Ownership

AI is responsible for:
- Identifying which docs need updating for a given task
- Making the updates as part of task delivery
- Proposing new docs when new capabilities or decisions are introduced

Users are responsible for:
- Approving changes to high-stakes docs (architecture, requirements, ADRs)
- Correcting inaccuracies when they notice them
- Deciding whether a new doc category is needed

---

## ADR Convention

Architecture Decision Records live in `docs/adr/`. Each ADR covers one decision.

**ADR format:**

```
# ADR-NNN: [Decision Title]

## Status
[Proposed | Accepted | Superseded by ADR-NNN]

## Context
What situation or problem forced this decision.

## Decision
What was decided.

## Consequences
What becomes easier, harder, or different as a result.
```

ADRs are written when:
- A foundational design choice is made
- A technology or approach was chosen over a meaningful alternative
- A constraint is established that will affect future decisions
- A past decision is being reversed or superseded
