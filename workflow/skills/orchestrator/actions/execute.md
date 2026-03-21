# execute — Wave-Based Execution

## Step 1: Load context (in parallel)

```
docs/features/{id}/PLAN.md
docs/features/{id}/spec.md
docs/standards/TESTING.md
```

## Step 2: Run Wave 1

```
2a. Spawn Executor subagent for each task in Wave 1 (in parallel)
2b. Wait for all to complete
2c. Aggregate worker-reports

Executor prompt uses templates/worker-reports-template.json for output format.
```

## Step 3: Check checkpoint

```
checkpoint:human-verify → Stop. Present to user. Wait for feedback.
  → PASS → continue to next wave
  → FAIL → create fix plan → execute fix

checkpoint:decision → Stop. Present options to user. Wait for decision.
  → Continue with chosen option

checkpoint:human-action → Stop. Provide instructions to user. Wait for action.
  → Continue

No checkpoint → continue to next wave
```

## Step 4: Run Wave 2, 3... (sequentially)

Repeat Step 2-3 for each wave.

## Step 5: Post-execution

```
├── Verify all worker-reports written to docs/worker-reports/{id}/*.json
├── Aggregate results
├── Update STATE.md: mark execute complete
└── Present summary to user
```

## Wave Diagram

```
WAVE 1 (parallel)
  Executor A --+
               +--> [Code + Tests + worker-report]
  Executor B --+

  ↓ [checkpoint resolved]

WAVE 2 (parallel)
  Executor C --+
               +--> [Code + Tests + worker-report]
  Executor D --+
```

## Deviation Rules

| Rule | Trigger | Action |
|------|---------|--------|
| 1 | Minor bug found while coding | Auto-fix inline, log in report |
| 2 | Missing critical piece | Auto-add inline, log in report |
| 3 | Blocking issue | Log in blockers, stop wave, ask user |
| 4 | Architecture change | Stop, ask user decision |

Max 3 auto-fix attempts per task. After 3 failures → log in blockers.
