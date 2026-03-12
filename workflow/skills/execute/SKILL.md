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

Before dispatching any subagent, output:

```
[workflow:execute] Task {N}/{total} — <title>

[Task Brief]
Plan: <1-2 sentences — what + how>
Risk: NONE | LOW: <detail> | HIGH: <detail>
Action: proceeding | ⚠️ need input: <single question>
```

HIGH risk → wait for user input before dispatching.
LOW/NONE → dispatch immediately after brief.

---

## Step 2 — Pick next task

From `tasks.md`, pick next unblocked task.
Parallel-safe tasks (`[P]` in same group) can be dispatched concurrently — never dispatch two tasks touching the same files.

---

## Step 3 — Dispatch implementer subagent

```
[workflow:execute] ⏳ Task {N} — dispatching implementer
```

Give subagent everything upfront:

```
You are implementing Task {N}: {title}

SPEC CONTEXT:
{relevant excerpt from approved.md}

TASK:
{full task text from tasks.md}

CODEBASE CONTEXT:
{relevant existing code, file structure, conventions}

Instructions:
- Follow task steps exactly
- Write tests first (standard/heavy)
- Self-review before reporting done
- Commit when complete: `type(scope): message`
- Ask questions BEFORE starting, not during
```

If subagent asks questions → answer completely, then redispatch.

---

## Step 4 — Review

**Light:** Self-review from subagent is sufficient.

**Standard/Heavy:** Two-stage review after each task.

### Stage 1 — Spec compliance

```
[workflow:execute] ⏳ Task {N} — spec compliance review
```

Dispatch fresh reviewer:
```
Review Task {N} for spec compliance.

SPEC: {approved.md excerpt}
TASK: {task definition}
Commits: {git SHAs}

Check:
- Every acceptance criterion met?
- Anything built NOT in spec?
- Any spec requirement missing?

Output: ✅ Compliant | ❌ Issues: [list]
```

Issues → implementer fixes → Stage 1 re-review. Never proceed to Stage 2 with open Stage 1 issues.

### Stage 2 — Code quality

```
[workflow:execute] ⏳ Task {N} — code quality review
```

Dispatch fresh reviewer:
```
Review Task {N} for code quality.

Commits: {git SHAs}
Conventions: {from PROJECT.md}

Check:
- Tests exist and meaningful
- No magic numbers, unclear names, dead code
- No unnecessary complexity
- Follows project conventions

Output: ✅ Approved | Issues: [Critical | Important | Minor]
```

Critical/Important → implementer fixes → re-review.
Minor → note, proceed.

---

## Step 5 — Mark complete + continue

After review passes:

```
[workflow:execute] ✅ Task {N}/{total} complete
```

Mark `[x] done` in `tasks.md`.

Update STATE.md:
```
next-action: Task {N+1} — {title}
```

Move to next task. Repeat until all done.

---

## Step 6 — Final review + handoff

```
[workflow:execute] All {N} tasks complete — final review
```

**Light:** Skip — per-task self-review sufficient.
**Standard:** Skip if tasks were low-risk and test coverage solid.
**Heavy:** Required.

Final review prompt:
```
Review complete implementation against approved spec.

approved.md: {full text}
All commits since task-breakdown: {SHAs}

Check: does full implementation deliver the spec?
Any integration issues between tasks?
```

Then:
```
[workflow:execute] Complete — {N} tasks done
Next: doc-sync → finishing-a-development-branch
```

Update STATE.md:
```
phase: review
next-action: Run doc-sync then finishing-a-development-branch
```
