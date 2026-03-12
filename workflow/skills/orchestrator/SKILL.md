---
name: orchestrator
description: Loaded at every session start. Single source of truth for all workflow phases.
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

## Phase: Spec

```
[workflow:spec] Formation | Amendment — <slug>
```

**New spec:** Load `workflow:skills/spec/formation.md`
**Change locked spec:** Load `workflow:skills/spec/amendment.md`

Spec lives at: `docs/specs/<slug>/spec.md`

---

## Phase: Task Breakdown

**Light track → skip. Go directly to Execute.**

```
[workflow:task-breakdown] Decomposing: <slug>
```

Read: `docs/specs/<slug>/spec.md`, `docs/PROJECT.md`, relevant codebase.

Create tasks using Claude Code task tool (TodoWrite). Each task:

```
Title: Task N — <name>
Body:
  Spec ref: FR-N / SC-N
  What to build: <one paragraph — behavior not implementation>
  Files:
    Create: path/to/file
    Modify: path/to/existing:L10-L50
    Test: path/to/test
  Acceptance:
    - [ ] specific verifiable outcome
  Steps (standard/heavy):
    1. Write failing test
    2. Run → confirm FAIL
    3. Implement minimal code
    4. Run → confirm PASS
    5. Commit: type(scope): message
```

Heavy: add Risk notes per task.

**Parallelization map** (standard/heavy): identify which tasks can run concurrently (no shared files, no dependencies).

Announce:
```
[workflow:task-breakdown] {N} tasks created. Next: execute
```

---

## Phase: Execute

```
[workflow:execute] Starting — <slug> | {N} tasks | track: <track>
```

**Setup (once):** Read `docs/specs/<slug>/spec.md` + relevant codebase. Cache — subagents get content as text, not file refs.

**Per task:**

1. Task Brief (announce before starting)

2. Dispatch `workflow:agents/implementer`:
   - SPEC: spec.md excerpt for this task
   - TASK: full task text
   - CODEBASE: relevant code, patterns, conventions

   Implementer asks questions → answer → redispatch.
   Implementer done → writes result to `.workflow/log/task-N.md` (SHA + what built).

3. Review (by track):
   - `light` → self-review only
   - `standard/heavy`:
     - Dispatch `workflow:agents/spec-reviewer` (SPEC + TASK + COMMITS)
       - ✅ → dispatch `workflow:agents/quality-reviewer` (COMMITS + CONVENTIONS + SCOPE: per-task)
         - ✅ → approved
         - ❌ Critical/Important → new implementer with issues → re-review
         - ❌ Minor → note, proceed
       - ❌ → new implementer with issues list → re-run spec-reviewer
     - Reviewer writes result to `.workflow/log/review-N.md`

4. Mark task done in Claude Code task tool. Read log files when needed — don't hold all results in context.

**Parallel tasks:** same group, no shared files → dispatch concurrently.

**All tasks done:**
```
[workflow:execute] All {N} tasks complete
```

---

## Phase: Final Review

**Light:** skip. **Standard:** skip if low-risk. **Heavy:** required.

```
[workflow:review] ⏳ Final integration review
```

Dispatch `workflow:agents/quality-reviewer`:
- COMMITS: all commits since task-breakdown
- CONVENTIONS: from docs/PROJECT.md
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

Every phase entry, major step, completion. User always knows what AI is doing.

---

> AI owns execution. User owns intent and strategic direction.
> Plan before acting. Surface only irreversible or strategic decisions.
