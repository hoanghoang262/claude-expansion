# plan

**Phase:** ACT — Break spec into tasks, organize waves, track in state.md.

<hard_constraint never_override>
Every task MUST have test criteria before implement. No exceptions.
Do NOT create a separate plan file. Plan lives in state.md + TaskCreate tool.
Tasks = implementation steps ONLY. spec-review and quality-review are NOT tasks — they are PM coordination steps inside execute flow. Never create a task for them.
</hard_constraint>

---

## Steps

### Step 1 — Read inputs

- `docs/features/{name}/requirements.md` — what to build
- `docs/features/{name}/user-stories.md` — acceptance criteria
- `docs/features/{name}/spec.md` — technical design (architecture, data model, API)
- `docs/foundations/` — cross-cutting tasks (DB setup, common services)

### Step 2 — Decompose into tasks

Each task must:
- Take ~2-5 minutes for an implementer
- Touch at most 1-2 files
- Be independently verifiable (has runnable test)
- Have explicit dependencies

Use `TaskCreate` tool for each task:
```
TaskCreate({
  subject: "TASK-{N}: {name}",
  description: "ACTION: create|modify|test\nFILES: {paths}\nWHAT: {what to implement}\nTEST: {how to verify}\nDEPENDS: {task IDs or none}"
})
```

### Step 3 — Group into waves

- Wave 1: Foundations (DB schema, project setup, common services) — no feature dependencies
- Wave 2+: Feature tasks organized by user story (US-001, US-002...)
- Within each wave: tasks run parallel (max 5 concurrent)
- Set task dependencies via `TaskUpdate` addBlockedBy

### Step 4 — Update state.md

Use the exact header format from `templates/state-template.md`:

```markdown
## Phase
ACT

## Action
execute

## Feature
{name}

## Wave
1/{total}
```

Route → `execute`. Read `actions/execute.md` before proceeding.

---

## Output

```
📋 Plan ready

⚡ {N} tasks in {M} waves
🔹 Wave 1: Foundations ({count} tasks)
🔹 Wave 2: {user story} ({count} tasks)
...

➡️ Next: execute — Wave 1
```
