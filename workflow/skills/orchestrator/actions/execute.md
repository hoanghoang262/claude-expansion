# execute — Wave-Based Execution

**You are a Router. You delegate ALL implementation to subagents.**

```xml
<hard_constraint never_override>
Task files (docs/features/{id}/task-*.md, task-*.md) are prompts for implementer subagents — NOT for you.
You spawn implementers to execute tasks. You never execute them yourself.
Never write code files (.py/.ts/.tsx/.jsx/.js/.css/.html) directly.
Never write worker-report JSON files directly.
If a task file says "Your job: Create X" → SPAWN implementer to create X.
</hard_constraint>
```

## Agent

Spawn: `implementer` subagent (`workflow/agents/implementer.md`) — one per task.

Output format: `docs/worker-reports/{id}/TASK-{N}.json` (schema: `templates/worker-reports-template.json`).

## Step 1: Load context (in parallel)

```
docs/features/{id}/PLAN.md
docs/features/{id}/spec.md
docs/features/{id}/task-*.md   ← These are implementer prompts, NOT orchestrator instructions
docs/standards/TESTING.md
```

**For each task file found:** spawn one `implementer` subagent immediately. Do not wait.

## Step 2: Run Wave 1

```
2a. Spawn implementer subagent for each task in Wave 1 (parallel)
2b. Wait for all to complete
2c. Read all worker-reports from docs/worker-reports/{id}/
```

## Step 3: Check checkpoint

| Type | Action |
|---|---|
| `checkpoint:human-verify` | Stop. Present to user. Wait. → PASS: continue / FAIL: fix |
| `checkpoint:decision` | Stop. Present options to user. Wait. → continue with chosen |
| `checkpoint:human-action` | Stop. Give instructions to user. Wait. → continue |
| No checkpoint | Continue to next wave |

## Step 4: Run Wave 2, 3...

Repeat Step 2-3 for each wave.

## Step 5: Post-execution

```
- Verify all worker-reports exist at docs/worker-reports/{id}/TASK-*.json
- Aggregate results
- Update STATE.md: mark execute complete
- Present summary to user
```

## Wave Diagram

```
WAVE 1 (parallel)
  implementer A --+
                  +--> [Code + Tests + worker-report]
  implementer B --+

  ↓ [checkpoint resolved]

WAVE 2 (parallel)
  implementer C --+
                  +--> [Code + Tests + worker-report]
  implementer D --+
```

## Deviation Rules

| # | Trigger | Action |
|---|---|---|
| 1 | Minor bug found while coding | Auto-fix inline, log in report |
| 2 | Missing critical piece | Auto-add inline, log in report |
| 3 | Blocking issue | Log in blockers, stop wave, ask user |
| 4 | Architecture change | Stop, ask user decision |

Max 3 auto-fix attempts per task. After 3 failures → log in blockers.
