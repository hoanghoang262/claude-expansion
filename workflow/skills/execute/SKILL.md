---
name: execute
description: Implement tasks from tasks.md. One fresh subagent per task. Task Brief before each dispatch. Commit per task. Hand off to review after each task.
---

# Execute

```
[workflow:execute] Starting — <slug> | {N} tasks | track: <track>
```

---

## Step 0 — Load context (once)

Read once. Never make subagents read these files.

1. `approved.md` — what must be built
2. `tasks.md` — all tasks with full text
3. Current codebase — enough to give subagents accurate context

Cache everything. Subagents receive context as text, not file references.

---

## Step 1 — Task Brief (before every task)

```
[workflow:execute] Task {N}/{total} — <title>

[Task Brief]
Plan: <1-2 sentences — what + how>
Risk: NONE | LOW: <detail> | HIGH: <detail>
Action: proceeding | ⚠️ need input: <single question>
```

HIGH risk → wait for user input. LOW/NONE → dispatch immediately.

---

## Step 2 — Pick next task

From `tasks.md`, pick next unblocked task.
Parallel-safe tasks (`[P]` in same group) → dispatch concurrently, never two tasks touching same files.

---

## Step 3 — Dispatch implementer

```
[workflow:execute] ⏳ Task {N} — implementing
```

Use prompt template: `./implementer.md`
If subagent asks questions → answer completely → redispatch.

---

## Step 4 — Hand off to review

After implementer commits:

```
[workflow:execute] ✅ Task {N} implemented — handing to review
```

**Light:** skip — self-review sufficient. Mark task done, continue.
**Standard/Heavy:** load `workflow:review/per-task` for this task, wait for result.

- Review ✅ → mark `[x] done` in `tasks.md`, update STATE.md, next task
- Review ❌ → implementer fixes, re-invoke `workflow:review`

---

## Step 5 — All tasks done

```
[workflow:execute] All {N} tasks implemented
```

Update STATE.md:
```
phase: review
next-action: Run workflow:review final — then doc-sync
```
