---
name: execute
description: Implement tasks from tasks.md using fresh subagents. Each task gets full context, two-stage review, and a commit before moving on.
---

# Execute

Implement the approved spec task by task.
Fresh subagent per task. Review before moving on. Update state as you go.

---

## Step 0 — Load context (once)

Read these files once before dispatching any subagent. Never make subagents read them.

1. `approved.md` — the spec (what must be built)
2. `tasks.md` — all tasks with full text
3. Current codebase state — enough to give subagents accurate context

Cache everything. Subagents receive context as text, not file references.

---

## Step 1 — Pick next task

From `tasks.md`, pick the next unblocked task in order.
Parallel-safe tasks (`[P]` in same group) can be dispatched concurrently — but never dispatch two tasks that touch the same files.

---

## Step 2 — Dispatch implementer subagent

Give the subagent everything it needs upfront:

```
You are implementing Task {N}: {title}

SPEC CONTEXT:
{relevant excerpt from approved.md}

TASK:
{full task text from tasks.md}

CODEBASE CONTEXT:
{relevant existing code, file structure, conventions}

Instructions:
- Follow the steps in the task exactly
- Write tests first (standard/heavy track)
- Self-review before reporting done
- Commit when complete: `type(scope): message`
- Ask questions BEFORE starting, not during
```

If subagent asks questions → answer completely, then redispatch. Never rush them into implementation.

---

## Step 3 — Review

**Light track:** Self-review from subagent is sufficient. Skip formal review.

**Standard/Heavy track:** Two-stage review after each task.

### Stage 1 — Spec compliance

Dispatch a fresh reviewer subagent:
```
Review Task {N} for spec compliance.

SPEC (approved.md excerpt): {text}
TASK definition: {text}
Commits to review: {git SHAs}

Check:
- Does implementation match every acceptance criterion?
- Anything built that's NOT in the spec?
- Any spec requirement missing from the implementation?

Output: ✅ Compliant | ❌ Issues: [list]
```

If issues → implementer subagent fixes → Stage 1 re-review.
Never proceed to Stage 2 while Stage 1 has open issues.

### Stage 2 — Code quality

Dispatch a fresh reviewer subagent:
```
Review Task {N} for code quality.

Commits to review: {git SHAs}
Project conventions: {from PROJECT.md}

Check:
- Tests exist and are meaningful (not just passing)
- No magic numbers, unclear names, dead code
- No unnecessary complexity or premature abstraction
- Follows project conventions

Output: ✅ Approved | Issues: [Critical | Important | Minor] [list]
```

Critical/Important issues → implementer fixes → Stage 2 re-review.
Minor issues → note, proceed.

---

## Step 4 — Mark complete + continue

After both review stages pass (or self-review for light):

Update `tasks.md` — mark task as `[x] done`.

Update STATE.md:
```
next-action: Task {N+1} — {title}
```

Move to next task. Repeat until all tasks done.

---

## Step 5 — Final review + handoff

After all tasks complete:

Dispatch one final reviewer across the full implementation:
```
Review the complete implementation against the approved spec.

approved.md: {full text}
All commits since task-breakdown: {SHAs}

Check end-to-end: does the full implementation deliver the spec?
Any integration issues between tasks?
```

Then:
```
[Execute complete] All {N} tasks done.
Next: doc-sync → finishing-a-development-branch
```

Update STATE.md:
```
phase: review
next-action: Run doc-sync then finishing-a-development-branch
```
