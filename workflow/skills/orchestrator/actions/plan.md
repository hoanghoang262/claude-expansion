# plan — Wave-Based Task Planning

## Step 1: Load context (in parallel)

```
docs/features/{id}/spec.md
docs/features/{id}/requirement.md
docs/standards/TESTING.md
```

## Step 2: Decompose into micro-tasks

Break the spec into the smallest independently actionable tasks:
- One task = one file or one function
- No task takes more than one subagent-session to complete
- Estimate: 2-5 minutes per task

For each task:
```
ACTION       — what to do (imperative: "Create", "Implement", "Add")
FILES        — which files to touch
VERIFY       — how to verify this is done
DEPENDENCIES — what must complete first
REQUIREMENTS  — any constraints from spec
```

## Step 3: Assign waves

Group tasks into waves. Tasks within a wave run in parallel.

```
WAVE 1: Tasks with no dependencies → parallel
WAVE 2: Tasks that depend only on Wave 1 → parallel
WAVE 3: Tasks that depend only on Wave 2 → parallel
...
```

## Step 4: Identify blockers

If a task depends on something outside the team's control:

```
Add checkpoint at the wave boundary:
  checkpoint:human-verify → stop and ask user to confirm before proceeding
  checkpoint:decision     → stop and present options to user
  checkpoint:human-action → stop, provide instructions to user, wait for action
```

## Step 5: Validate plan

```
No circular dependencies between tasks?
No task is too large (>1 subagent-session)?
All blockers identified and marked with checkpoints?
Wave assignments are correct?
```

## Output

Create: `docs/features/{id}/PLAN.md` using `templates/plan-template.md`.
