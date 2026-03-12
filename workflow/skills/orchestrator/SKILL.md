---
name: orchestrator
description: Loaded at every session start — orients AI within the workflow, guides what to do next, surfaces the right skill at the right time.
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

## Brainstorm Detection

Assess internally: is the user's intent strategically ambiguous?

Signals of strategic ambiguity:
- User is choosing between fundamentally different approaches
- "Better", "cleaner", "scale" without defining what that means
- Multiple valid directions with meaningfully different trade-offs

**If detected → suggest brainstorming, don't force it:**
```
Tôi thấy bạn đang phân vân về <X>. Bạn có muốn brainstorm để làm rõ hướng đi trước không,
hay bạn đã có hướng và muốn đi thẳng vào spec?
```

User can decline → proceed to spec-formation directly.
User accepts → invoke `workflow:brainstorming`.

**No ambiguity detected → go straight to spec-formation. Never suggest brainstorm for clear tasks.**

Examples — no brainstorm needed:
- "add export PDF for invoices"
- "add filter by date on orders page"
- "refactor auth module to separate guard/service/repository"

Examples — suggest brainstorm:
- "muốn cải thiện collaboration nhưng chưa biết nên làm gì"
- "muốn permission tốt hơn nhưng chưa rõ hướng"
- "muốn restructure để scale nhưng chưa chắc cách tiếp cận"

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

| Situation | Next step |
|-----------|-----------|
| Strategic ambiguity detected | Suggest brainstorming → user decides |
| User accepts brainstorm | `workflow:brainstorming` |
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
