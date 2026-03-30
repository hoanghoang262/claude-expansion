# Action: Debug

Triggered in VERIFY phase when failure blocks progress.

---

## Steps

1. Identify failure type:
   - Wrong output (misunderstood requirements) → loop back to UNDERSTAND
   - Broken implementation (code/logic error) → fix in BUILD
   - Environment/dependency issue → Tier 3 escalation if unresolvable

2. For implementation errors:
   - Collect error + context
   - Spawn implementer with specific fix task
   - Re-run verify after fix

3. If same failure recurs 3 times → escalate Tier 3 to user
   Format: issue · what was tried · options · recommendation
