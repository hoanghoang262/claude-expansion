# Execute

```
[workflow:execute] Starting — <slug> | {N} tasks | track: <track>
```

**Setup (once):** Read `docs/specs/<slug>/spec.md` + relevant codebase.

Initialize summary if not exists:

```
.workflow/specs/<slug>/log/summary.md
```

---

## Per task loop

### 1. Task Brief

```
[workflow:execute] Task {N}/{total} — <title>
```

Produce Task Brief — canonical format in orchestrator SKILL.md.
HIGH risk → wait for input before dispatching.

### 2. Dispatch implementer

→ Load `workflow:agents/implementer` — pack spec excerpt, task, relevant codebase context.

Implementer asks questions → answer completely → reload.
Done → result in `.workflow/specs/<slug>/log/task-{N}.md`.

### 3. Review

**Light:** self-review only → proceed.

**Standard/Heavy:**

```
[workflow:review] ⏳ Task {N} — spec compliance
```

→ Load `workflow:agents/spec-reviewer`

- ✅ → quality review
- ❌ → re-implement with issues → re-review

```
[workflow:review] ⏳ Task {N} — code quality
```

→ Load `workflow:agents/quality-reviewer` — scope: per-task

- ✅ → task approved
- ❌ Critical/Important → re-implement → re-review
- ❌ Minor → note, proceed

**Circuit breaker:** If the same task fails review twice → stop and surface to user:

```
[workflow:review] ⚠️ Task {N} — blocked after 2 attempts
Issue: <what keeps failing>
Options: A) retry with different approach  B) relax requirement  C) skip task
```

### 4. Complete

```
[workflow:review] ✅ Task {N} — approved
```

Append to `.workflow/specs/<slug>/log/summary.md` tasks table:

```
| {N} | <title> | ✅ | <key output — 1 phrase> | <issues or none> |
```

---

## Parallel tasks

Tasks in same parallel group (no shared files) → dispatch concurrently.
Each task still goes through full review loop independently.

---

## All tasks done

```
[workflow:execute] All {N} tasks complete
```

→ Final review (see orchestrator SKILL.md: Phase: Final Review).
→ Doc sync (see orchestrator SKILL.md: Phase: Doc Sync).
→ Run merge gate (below).

---

## Merge Gate

Run after doc sync. Do not merge without passing.

```
[workflow:merge-gate] Checking <branch>
```

Check:

- [ ] All tasks in summary.md are ✅
- [ ] `git diff main..HEAD` — no debug code, hardcoded values, leftover TODOs
- [ ] Tests pass (if project has test runner)
- [ ] Doc sync complete

Pass → report:

```
[workflow:done] <branch> ready to merge.
Changes: <git diff --stat summary>
Merge into main?
```

Fail → list what's missing. Do not merge.
