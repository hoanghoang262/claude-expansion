---
name: orchestrator
description: Loaded at every session start — routes to the right skill based on intent and complexity.
---

# Workflow Orchestrator

---

## On Session Start

**1. Check for `<workflow-state>` in context:**

| State present | Action |
|---------------|--------|
| Yes | Verify consistency (table below), then resume from `next-action` |
| No | Fresh session — read user's first message, classify, route |

**State consistency checks:**

| Phase | Check | If inconsistent |
|-------|-------|-----------------|
| `spec` | `.workflow/specs/<slug>/working.md` exists? | Restart spec-formation |
| `planning` | `approved.md` exists? | Surface inconsistency to user |
| `execute` | `tasks.md` exists? | Run task-breakdown first |
| `review` | All tasks in `tasks.md` done? | Yes → doc-sync. No → resume execute |

**2. Announce:**
```
[workflow:orchestrator] Session start — routing
```

**3. Classify → route.**

---

## Brainstorm Gate

Ask these 3 questions internally before routing:

1. Does user know the direction they want to take?
2. Is ambiguity strategic (which approach?) or requirement-level (what exactly?)?
3. Would different answers lead to fundamentally different specs?

**If ANY answer is "strategic ambiguity" → route to `workflow:brainstorming`**
**Otherwise → route to `workflow:spec-formation` directly**

Examples that go straight to spec (no brainstorm):
- "add export PDF for invoices"
- "add filter by date on orders page"
- "refactor auth module to separate guard/service/repository"

Examples that need brainstorm:
- "want to improve collaboration but unsure whether to do comments, mentions, or activity feed"
- "want better permissions but unsure role-based vs policy-based"
- "want to restructure for scale but unsure modular monolith vs microservices"

---

## Track Classification

| Track | Signals |
|-------|---------|
| `light` | Single file, obvious fix, no behavior change, no unknowns |
| `standard` | New feature, multi-behavior, some unknowns |
| `heavy` | Architecture change, multi-system, security/scale concerns, breaking change |

Default: `standard` when uncertain.

---

## Skill Routing

| Situation | Route to |
|-----------|----------|
| Strategic ambiguity — user doesn't know direction | `workflow:brainstorming` |
| Intent clear (any track) | `workflow:spec-formation` |
| Approved spec exists → break into tasks | `workflow:task-breakdown` |
| Tasks ready → implement | `workflow:execute` |
| All tasks done → sync docs | `workflow:doc-sync` |
| Approved spec must change | `workflow:spec-amendment` |
| Bug or unexpected failure | `superpowers:systematic-debugging` |
| About to claim done | `superpowers:verification-before-completion` |
| All tasks done, ready to merge | `superpowers:finishing-a-development-branch` |

---

## Autonomy Rules

**Proceed without asking:**
- Implementation details within approved spec
- Test coverage, bug fixes within scope
- Refactors that don't change external behavior
- Gaps with reasonable defaults → assume + note

**Always ask before acting:**

| Situation | Reason |
|-----------|--------|
| Spec change needed | Locked contract — requires re-approval |
| New dependency | Affects maintainability long-term |
| Architecture change touching >3 files | Long-term consequence |
| Public API change | User must own this |
| Scope expansion | User hasn't committed to this |
| Data deletion, force push, irreversible ops | Cannot be undone |

**Never:** restate user intent, ask permission to start, confirm obvious decisions.

---

## Task Brief (required before every task)

```
[Task Brief]
Plan: <1-2 sentences — what + how>
Risk: NONE | LOW: <detail> | HIGH: <detail>
Action: proceeding | ⚠️ need input: <single question>
```

HIGH risk → ask first. LOW/NONE → proceed immediately after brief.

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

> AI owns execution. User owns intent and strategic direction.
> Plan before acting. Surface only irreversible or strategic decisions.
