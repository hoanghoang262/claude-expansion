---
name: execute
description: Implement tasks from tasks.md using fresh subagents. Task Brief before each task. Two-stage review for standard/heavy. Commit per task.
---

# Execute

```
[workflow:execute] Starting execution — <slug> | {N} tasks | track: <track>
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
[workflow:execute] ⏳ Task {N} — dispatching implementer
```

Use prompt template: `./implementer.md`
If subagent asks questions → answer completely, then redispatch.

---

## Step 4 — Review

**Light:** subagent self-review sufficient — skip formal review.

**Standard/Heavy:** two-stage review after each task.

### Stage 1 — Spec compliance

```
[workflow:execute] ⏳ Task {N} — spec compliance review
```

Use prompt template: `./spec-reviewer.md`
Issues → implementer fixes → re-review. Never proceed to Stage 2 with open Stage 1 issues.

### Stage 2 — Code quality

```
[workflow:execute] ⏳ Task {N} — code quality review
```

Use prompt template: `./quality-reviewer.md`
Critical/Important → implementer fixes → re-review. Minor → note, proceed.

---

## Step 5 — Mark complete + continue

```
[workflow:execute] ✅ Task {N}/{total} complete
```

Mark `[x] done` in `tasks.md`. Update STATE.md: `next-action: Task {N+1} — {title}`
Repeat until all tasks done.

---

## Step 6 — Final review + handoff

```
[workflow:execute] All {N} tasks complete — final review
```

**Light:** skip. **Standard:** skip if low-risk + solid coverage. **Heavy:** required.

Use prompt template: `./quality-reviewer.md` with full implementation scope.

```
[workflow:execute] Complete — {N} tasks done
Next: doc-sync → finishing-a-development-branch
```

Update STATE.md:
```
phase: review
next-action: Run doc-sync then finishing-a-development-branch
```
