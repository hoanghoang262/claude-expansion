# debug

**Phase:** Optional — triggered by verify failure or execute task failure (3+ attempts)

## Purpose

Find and fix root cause. Not a brute-force retry loop.

## Iron Law

`DO NOT FIX WITHOUT ROOT CAUSE. 3+ FAILURES = ARCHITECTURAL PROBLEM.`

---

## Trigger Conditions

| Trigger                              | Entry point         | Return to  |
|--------------------------------------|---------------------|------------|
| `verify` fails on AC item            | From verify         | verify     |
| Execute task fails 3rd time          | From execute        | execute    |
| Implementer escalates blocked task   | From execute        | Tier 3     |

---

## Steps

### Step 1 — Root cause analysis

```
Symptom: [what failed, exact error or test output]
    ↓
Trace: [where does the failure originate? file:line]
    ↓
Pattern: [is this isolated or systemic?]
    ↓
Hypothesis: [why is this happening?]
    ↓
Fix: [minimal change that addresses root cause]
```

### Step 2 — Assess scope

- **Isolated** (1 file, clear fix) → spawn implementer with specific fix task + root cause context
- **Systemic** (3+ failures, same pattern) → STOP. This is an architectural problem.
  - Write concern: `docs/concerns/CONCERN-{id}.md`
  - Tier 3 escalation: present to user with options

### Step 3 — After fix

- Spawn spec-reviewer + quality-reviewer on the fix (same as execute flow)
- Return to trigger:
  - Came from verify → return to verify (re-run full checklist)
  - Came from execute → return to execute (retry task)

### Step 4 — Write learning

After any debug session (success or failure):
- Write to `docs/learnings/{date}-{pattern}.md`:
  - What failed, root cause, fix applied, lesson
  - Does this indicate a rule needs updating? (e.g., testing-strategy.md)
  - If yes → flag for rules update (do NOT update rules mid-session, wait until verify complete)
