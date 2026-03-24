# execute

**Phase:** IMPLEMENT — Task execution

## Purpose

Dispatch implementer subagents per task, run two-stage review, track progress.

## Iron Laws

`EVIDENCE BEFORE CLAIMS. RUN TESTS BEFORE SAYING "DONE".`
`CONTROLLER PROVIDES FULL CONTEXT. SUBAGENT DOES NOT READ PLAN FILE.`

---

## Execution Model

Per wave: dispatch all tasks in parallel (max 5 concurrent).
Per task: implementer → spec-review → quality-review → mark complete.

### Subagent Context Protocol

**CRITICAL:** Do NOT tell subagent to read PLAN.md or spec.md. Extract and pass directly:

```
Dispatch implementer with:
- Full task text (ACTION, FILES, WHAT, TEST, DEPENDS_ON)
- Relevant spec excerpt (only the sections this task touches)
- Rules summary (coding-standards + testing-strategy key points)
- Context: "You are implementing TASK-N of feature {name}. This is wave W of T."
```

### Per-Task Flow

```
dispatch implementer (with full context above)
    ↓
implementer asks questions? → answer completely before proceeding
    ↓
implementer implements + writes tests + self-reviews + reports
    ↓
dispatch spec-reviewer (with: task text + spec acceptance criteria + git SHAs)
    ↓
spec compliant? → No → implementer fixes → re-review
                → Yes → dispatch quality-reviewer
    ↓
quality approved? → No → implementer fixes → re-review
                 → Yes → mark TASK-N complete in state.md
```

### Wave Completion

After all tasks in wave complete:
- Read all worker reports from `docs/worker-reports/{feature}/`
- Check for escalated tasks → Tier 3 if any
- Check for failed tasks → retry once (Tier 3 after 3 failures)
- All complete → update state.md → dispatch next wave

### After All Waves

Dispatch final code reviewer for full integration check. Then route to `verify`.

---

## Red Flags

<hard_constraint never_override>
Never do these:
- Tell subagent to read plan/spec file — extract and pass the text directly
- Skip spec-review before quality-review (wrong order)
- Skip quality-review (both stages are required)
- Dispatch multiple implementers for same task in parallel
- Accept spec-reviewer ✅ when reviewer found open issues
- Move to next wave while current wave has incomplete tasks
- Mark task done without test evidence
- Attempt same task fix more than 3 times without escalating Tier 3
</hard_constraint>

---

## Worker Report

Save to `docs/worker-reports/{feature}/TASK-{N}.json` [VERSION]. Schema defined in `agents/implementer.md`.

Required fields: task_id, status (completed|failed|blocked|escalated), files_modified, test_evidence, escalation_note.
