---
name: orchestrator
description: Loaded at every session start. Routing, autonomy rules, core protocols.
---

# Workflow Orchestrator

```
[workflow:orchestrator] Session start
```

Read user's message → classify intent → route to correct phase.

---

## Autonomy Rules

**Proceed without asking:**
- Implementation details within approved spec
- Test coverage, bug fixes within scope
- Refactors that don't change external behavior
- Gaps with reasonable defaults → assume + note

**Always ask first:**

| Situation | Why |
|-----------|-----|
| Spec change needed | Locked contract |
| New dependency | Long-term impact |
| Architecture change touching >3 files | Long-term consequence |
| Public API change | User must own this |
| Scope expansion | Not committed by user |
| Irreversible ops (delete, force push) | Cannot undo |

**Never:** restate intent, ask permission to start, confirm obvious decisions.

---

## Task Brief (before every task)

```
[Task Brief]
Plan: <1-2 sentences — what + how>
Risk: NONE | LOW: <detail> | HIGH: <detail>
Action: proceeding | ⚠️ need input: <single question>
```

HIGH → wait. NONE/LOW → proceed immediately.

---

## Track Classification

| Track | Signals |
|-------|---------|
| `light` | Single file, obvious fix, no behavior change |
| `standard` | New feature, multi-behavior, some unknowns |
| `heavy` | Architecture change, multi-system, security/scale, breaking |

Default: `standard` when uncertain.

---

## Brainstorm Gate

Suggest only when ALL true:
- User doesn't know which direction to take
- Different answers → fundamentally different specs

```
Bạn có muốn brainstorm trước để làm rõ hướng không?
```

Agree → load `workflow:brainstorming`, save output to `.workflow/brainstorm/<N>-<topic>.md`.
Decline → go to spec formation.
Never suggest more than once per session.

---

## Phase Routing

| Phase | When | Load |
|-------|------|------|
| Spec — new | Intent is clear | `./spec-formation.md` |
| Spec — change | Locked spec must change | `./spec-amendment.md` |
| Git setup | Spec just approved | `./git-workflow.md` |
| Task breakdown | Spec approved, standard/heavy | `./task-breakdown.md` |
| Execute | Tasks ready | `./execute.md` |
| Final review | All tasks done | see below |
| Doc sync | Review passed | see below |

---

## Phase: Final Review

**Light:** skip. **Standard:** skip if low-risk. **Heavy:** required.

```
[workflow:review] ⏳ Final integration review
```

Dispatch `workflow:agents/quality-reviewer`:
- COMMITS: all commits since task-breakdown
- CONVENTIONS: from `docs/PROJECT.md`
- SCOPE: final integration

Issues → surface to user before proceeding.

```
[workflow:review] ✅ Final review complete
```

---

## Phase: Doc Sync

```
[workflow:doc-sync] Starting — <slug>
```

Dispatch `workflow:agents/doc-syncer`:
- SPEC_PATH: `docs/specs/<slug>/spec.md`
- COMMITS: all implementation commits
- TRACK: current track

---

## Announce Format

```
[workflow:<phase>] <Action> — <detail>
```

Every phase entry, major step, completion.

---

> AI owns execution. User owns intent and strategic direction.
> Plan before acting. Surface only irreversible or strategic decisions.
