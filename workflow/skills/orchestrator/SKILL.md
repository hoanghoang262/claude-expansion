---
name: orchestrator
description: Loaded at every session start — routes AI to the right workflow skill based on intent and complexity.
---

# Workflow Orchestrator

Your routing guide. Read at session start, act accordingly.

---

## First Action Every Session

1. Check if `<workflow-state>` was injected into context.
   - **Yes → verify state consistency before resuming:**
     - `phase: spec` → does `.workflow/specs/<slug>/working.md` exist? If not, restart spec-formation.
     - `phase: planning` → does `approved.md` exist? If not, surface the inconsistency.
     - `phase: execute` → does `tasks.md` exist? If not, run task-breakdown first.
     - State consistent → resume from `next-action`.
   - **No → fresh project or new task.** Read user's first message.
2. Classify intent → pick track → route.

---

## Track Classification

| Track | Signals |
|-------|---------|
| `light` | Single file, obvious fix, no behavior change, no unknowns |
| `standard` | New feature, multi-behavior, some unknowns |
| `heavy` | Architecture change, multi-system, security/scale concerns, breaking change |

When in doubt → `standard`.

---

## Skill Routing

| Situation | Skill |
|-----------|-------|
| Intent vague, user doesn't know what to build | `workflow:brainstorming` |
| Intent clear (any track) → write spec + resolve gaps inline | `workflow:spec-formation` |
| Approved spec exists → break into tasks | `workflow:task-breakdown` |
| Tasks ready → implement | `workflow:execute` |
| All tasks done → sync docs | `workflow:doc-sync` |
| Approved spec must change | `workflow:spec-amendment` |
| Bug or unexpected failure | `superpowers:systematic-debugging` |
| About to claim done | `superpowers:verification-before-completion` |
| All tasks done, ready to merge | `superpowers:finishing-a-development-branch` |

**Decision flow:**

```
New task?
  └─ Intent vague → brainstorming
  └─ Intent clear
       ├─ light  → spec-formation (fast) → execute
       └─ standard/heavy → spec-formation → task-breakdown → execute → review → doc-sync

Resume?
  └─ Read STATE.md → jump directly to current phase skill
```

---

## Autonomy Boundaries

**Act without asking:**
- Implementation details within approved spec
- Test coverage, bug fixes within scope
- Refactors that don't change external behavior

**Always ask before acting:**
- Changing approved spec → use spec-amendment
- New dependencies or architecture changes
- Scope expansion beyond approved
- Anything contradicting a previous user decision

---

## STATE.md Format

Update on every phase transition:

```
phase: <brainstorm|spec|planning|execute|review|done>
active-spec: <slug or "none">
track: <light|standard|heavy>
next-action: <one sentence>
blocked-by: <description or "none">
last-updated: YYYY-MM-DD
```

---

## Core Principle

> Standard flow always runs. Ceremony scales with complexity.
> AI owns execution. User owns intent and strategic direction.
