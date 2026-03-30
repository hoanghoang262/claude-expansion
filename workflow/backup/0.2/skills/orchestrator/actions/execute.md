# execute

**Phase:** ACT — Dispatch tasks, review, track progress.

<hard_constraint never_override>
- PM never fixes code. Reviewer fails → re-dispatch implementer.
- Evidence before claims. Run tests before saying "done".
- Pass full context to subagents — never tell them to read files themselves.
- spec-review before quality-review. Both required.
- No parallel implementers on the same task.
- No next wave while current wave has incomplete tasks.
- Max 3 fix attempts per task → Tier 3.
- worker-report created by implementer, not PM.
</hard_constraint>

---

## Wave Execution

**Dispatch all tasks in a wave simultaneously — single message, multiple Agent calls.**

```
Wave N:
  ┌─ TASK-1 pipeline ──────────────────────────┐
  │  implementer → spec-review → quality-review │  ← runs in parallel
  └─────────────────────────────────────────────┘
  ┌─ TASK-2 pipeline ──────────────────────────┐
  │  implementer → spec-review → quality-review │  ← runs in parallel
  └─────────────────────────────────────────────┘
  ┌─ TASK-N ...                                 ┐
  └─────────────────────────────────────────────┘
        ↓ ALL complete
  Wave Completion → next wave
```

<hard_constraint never_override>
All independent tasks in a wave dispatch in ONE message (multiple Agent tool calls together).
Sequential only when task has explicit DEPENDS_ON another task in the same wave.
Max 5 concurrent. If wave has more → batch into groups of 5.
</hard_constraint>

---

## Per-Task Pipeline

Each task runs this pipeline independently:

```
dispatch implementer
  context: task text + spec excerpt (from docs/) + conventions (from .claude/rules/) + "TASK-N, wave W of T"
  source files: pass file PATHS only — implementer reads them directly
    ↓
implementer asks questions? → answer → re-dispatch (never proceed with gap)
    ↓
implementer writes code + tests + worker-report → reports done
    ↓
PM reads worker-report → dispatch spec-reviewer
  pass: task text + spec AC + files_modified
    ↓
spec ✅ → dispatch quality-reviewer (pass: same)
spec ❌ → re-dispatch implementer with ISSUES_TO_FIX
    ↓
quality ✅ → TaskUpdate: complete
quality ❌ → re-dispatch implementer with ISSUES_TO_FIX
```

**Re-dispatch when reviewer fails:**
```
[original context]

ISSUES_TO_FIX:
{full reviewer output}

Fix ONLY listed issues. Update worker-report after.
```

---

## Wave Completion

After ALL tasks in wave complete:
- Read all `docs/worker-reports/{feature-id}/` → check escalated + failed
- Escalated → Tier 3. Failed → retry once (Tier 3 after 3 failures).
- All complete → update state.md → next wave

After all waves → read `actions/verify.md` → route to `verify`.

---

## Worker Report

Written by implementer to `docs/worker-reports/{feature-id}/TASK-{N}.json`. PM reads only.

Use `files_modified` → build reviewer context. Use `status` → detect escalations.
Missing after implementer done → re-dispatch: "Write worker-report before reporting complete."
