---
name: orchestrator
description: Loaded at every session start. Single source of truth for all workflow phases — no routing to intermediate skills.
---

# Workflow Orchestrator

---

## On Session Start

```
[workflow:orchestrator] Session start
```

1. Check `<workflow-state>` in context:
   - Present → verify consistency (table below), resume from `next-action`
   - Absent → read user message, classify, proceed

2. State consistency checks:

| Phase | Check | If inconsistent |
|-------|-------|-----------------|
| `spec` | `working.md` exists? | Restart spec-formation |
| `planning` | `approved.md` exists? | Surface to user |
| `execute` | `tasks.md` exists? | Run task-breakdown first |
| `review` | All tasks done in `tasks.md`? | Yes → doc-sync. No → resume execute |

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
| Data deletion, force push, irreversible ops | Cannot undo |

**Never:** restate intent, ask permission to start, confirm obvious decisions.

---

## Task Brief (required before every task)

```
[Task Brief]
Plan: <1-2 sentences — what + how>
Risk: NONE | LOW: <detail> | HIGH: <detail>
Action: proceeding | ⚠️ need input: <single question>
```

HIGH risk → wait for input. NONE/LOW → proceed immediately after brief.

---

## Track Classification

| Track | Signals |
|-------|---------|
| `light` | Single file, obvious fix, no behavior change, no unknowns |
| `standard` | New feature, multi-behavior, some unknowns |
| `heavy` | Architecture change, multi-system, security/scale, breaking change |

Default: `standard` when uncertain.

---

## Brainstorm Gate

Suggest brainstorming only when ALL true:
- User doesn't know which direction to take
- Different answers → fundamentally different specs
- Not a spec detail question

```
Bạn có muốn brainstorm trước để làm rõ hướng không? Tôi có thể bắt đầu ngay.
```

User agrees → load `workflow:brainstorming`. User declines → go to spec-formation.
Never suggest more than once per session.

---

## Phase: Spec

```
[workflow:spec] Formation | Amendment — <slug>
```

**New spec:** Load `workflow:skills/spec/formation.md` — follow it exactly.
**Change locked spec:** Load `workflow:skills/spec/amendment.md` — follow it exactly.

---

## Phase: Task Breakdown

```
[workflow:task-breakdown] Decomposing: <slug>
```

Read once: `approved.md`, `PROJECT.md`, relevant codebase files.

**Task format:**
```markdown
### Task {N} — {title}
**Spec ref:** FR-{N} / SC-{N}
**Parallel:** yes | no
**Depends on:** Task {N} | none

#### What to build
<one paragraph — behavior, not implementation>

#### Files
- Create: `path/to/file`
- Modify: `path/to/existing:L10-L50`
- Test: `path/to/test`

#### Acceptance
- [ ] <specific verifiable outcome>

#### Steps  ← standard/heavy only
1. Write failing test
2. Run → confirm FAIL
3. Implement minimal code
4. Run → confirm PASS
5. Commit: `type(scope): message`
```

Heavy track: add `#### Risk notes` per task.

**Parallelization map** (standard/heavy):
```markdown
## Execution Order
Sequential: Task 1 → Task 2
Parallel group A (after Task 1): Task 3 [P], Task 4 [P]
Sequential: Task 5 (integrates A)
```

Save to `.workflow/specs/<slug>/tasks.md`. Update STATE.md `phase: execute`.

```
[workflow:task-breakdown] {N} tasks → tasks.md. Next: execute
```

| Track | Behavior |
|-------|----------|
| `light` | 1–3 tasks, no steps, no parallelization map |
| `standard` | Full format + steps + parallelization map |
| `heavy` | Full format + dependency graph + risk notes |

---

## Phase: Execute

```
[workflow:execute] Starting — <slug> | {N} tasks | track: <track>
```

**Setup (once):** Read `approved.md` + `tasks.md` + relevant codebase. Cache everything — subagents receive content as text, not file references.

**Per task loop:**

1. Task Brief:
```
[workflow:execute] Task {N}/{total} — <title>
[Task Brief]
Plan: ...
Risk: ...
Action: proceeding | ⚠️ need input: ...
```

2. Dispatch `workflow:agents/implementer` with:
   - `SPEC`: approved.md excerpt for this task
   - `TASK`: full task text from tasks.md
   - `CODEBASE`: relevant existing code, file structure, conventions

   If implementer asks questions → answer completely → redispatch.

3. Review (by track):
   - `light` → skip, self-review sufficient
   - `standard/heavy` → dispatch `workflow:agents/spec-reviewer` (SPEC + TASK + COMMITS)
     - ✅ → dispatch `workflow:agents/quality-reviewer` (COMMITS + CONVENTIONS + SCOPE: per-task)
       - ✅ → task approved
       - ❌ Critical/Important → implementer fixes → re-review
       - ❌ Minor → note, proceed
     - ❌ → implementer fixes → re-run spec-reviewer

4. Mark task `[x] done` in tasks.md. Update STATE.md. Next task.

**Parallel tasks:** same [P]-group with no shared files → dispatch concurrently.

**All tasks done:**
```
[workflow:execute] All {N} tasks implemented
```
Update STATE.md: `phase: review | next-action: final review then doc-sync`

---

## Phase: Final Review

**Light:** skip. **Standard:** skip if low-risk + solid coverage. **Heavy:** required.

```
[workflow:review] ⏳ Final integration review
```

Dispatch `workflow:agents/quality-reviewer` with:
- `COMMITS`: all commits since task-breakdown
- `CONVENTIONS`: from PROJECT.md
- `SCOPE`: final integration

Issues found → surface to user with description + recommendation before proceeding.

```
[workflow:review] ✅ Final review complete
```

Update STATE.md: `phase: doc-sync`

---

## Phase: Doc Sync

```
[workflow:doc-sync] Starting — <slug>
```

Dispatch `workflow:agents/doc-syncer` with:
- `SPEC_PATH`: `.workflow/specs/<slug>/approved.md`
- `COMMITS`: all implementation commits
- `TRACK`: from STATE.md

Update STATE.md:
```
phase: done
next-action: Run superpowers:finishing-a-development-branch
```

---

## STATE.md Format

```
phase: <spec|planning|execute|review|doc-sync|done>
active-spec: <slug | none>
track: <light|standard|heavy>
next-action: <one sentence>
blocked-by: <description | none>
last-updated: YYYY-MM-DD
```

Update on every phase transition.

---

## Announce Format

```
[workflow:<phase>] <Action> — <detail>
```

Every phase entry, major step, and completion. User always knows what AI is doing.

---

> AI owns execution. User owns intent and strategic direction.
> Plan before acting. Surface only irreversible or strategic decisions.
