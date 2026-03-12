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

## Brainstorm Suggestion

Brainstorming is a **standalone independent session** — not part of the main workflow.
User can start it anytime via `/brainstorm`.

**When to suggest (AI judges based on signals):**

| Signal | Suggest? |
|--------|----------|
| User uses vague goal words: "better", "cleaner", "improve", "rethink" without a concrete target | Yes |
| User mentions multiple conflicting directions in one message | Yes |
| User asks "what should I do?" or "where do I start?" | Yes |
| User is describing a problem, not a solution | Yes |
| Task is clear and concrete | Never |

**How to suggest — light touch, one line:**
```
Bạn có muốn brainstorm trước để làm rõ hướng không? Tôi có thể bắt đầu ngay.
```

**If user agrees → invoke `workflow:brainstorming` immediately.**
**If user declines → proceed with what they said, go to spec-formation.**

Never suggest more than once per session. Never push if declined.

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
| Intent clear (any track) | `workflow:spec` → `./formation.md` |
| Approved spec exists → break into tasks | `workflow:task-breakdown` |
| Tasks ready → implement | `workflow:execute` |
| Task implemented → review it | `workflow:review` |
| All tasks done → final review | `workflow:review` (final mode) |
| Final review passed → sync docs | `workflow:doc-sync` |
| Approved spec must change | `workflow:spec` → `./amendment.md` |
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
