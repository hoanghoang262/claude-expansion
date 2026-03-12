---
name: orchestrator/execute
description: Execute tasks one by one. Task Brief, dispatch implementer, review, mark done. Loaded when entering execute phase.
---

# Execute

```
[workflow:execute] Starting — <slug> | {N} tasks | track: <track>
```

**Setup (once):** Read `docs/specs/<slug>/spec.md` + relevant codebase. Cache content — subagents receive text, not file refs.

---

## Per task loop

### 1. Task Brief

```
[workflow:execute] Task {N}/{total} — <title>

[Task Brief]
Plan: ...
Risk: ...
Action: proceeding | ⚠️ need input: ...
```

HIGH risk → wait for input before dispatching.

### 2. Dispatch implementer

Send `workflow:agents/implementer` with:
- **SPEC**: spec.md excerpt for this task (goal, relevant FRs, SCs)
- **TASK**: full task text
- **CODEBASE**: relevant existing code, patterns, conventions

Implementer asks questions → answer completely → redispatch.
Implementer done → writes result to `.workflow/log/task-{N}.md`.

### 3. Review

**Light:** self-review only → proceed.

**Standard/Heavy:**

```
[workflow:review] ⏳ Task {N} — spec compliance
```
Dispatch `workflow:agents/spec-reviewer` (SPEC + TASK + COMMITS from log):
- ✅ → proceed to quality review
- ❌ → dispatch new implementer with issues list → re-run spec-reviewer

```
[workflow:review] ⏳ Task {N} — code quality
```
Dispatch `workflow:agents/quality-reviewer` (COMMITS + CONVENTIONS + SCOPE: per-task):
- ✅ → task approved
- ❌ Critical/Important → dispatch new implementer with issues → re-review
- ❌ Minor → note, proceed

Reviewers write result to `.workflow/log/review-{N}.md`.
Read log files when needed — don't hold all results in context.

### 4. Complete

```
[workflow:review] ✅ Task {N} — approved
```

Mark task done in Claude Code task tool. Move to next task.

---

## Parallel tasks

Tasks in same parallel group (no shared files) → dispatch concurrently.
Each task still goes through full review loop independently.

---

## All tasks done

```
[workflow:execute] All {N} tasks complete
```

→ Load final review (see orchestrator SKILL.md).
