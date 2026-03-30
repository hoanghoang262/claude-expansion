# Action: Plan

Triggered in BUILD phase when execution needs task breakdown.

---

## When to trigger

- Multiple independent tasks can run in parallel
- Work is too large for a single agent in one pass
- Dependencies between tasks need to be explicit

## Steps

1. Break work into tasks:
   - Each task: clear description + success criteria + assigned agent type
   - Identify dependencies — what must complete before what
   - Group independent tasks into parallel waves
2. Save plan to `docs/.pa/state.md` or `docs/.pa/worker-reports/plan.md`
3. Execute wave by wave — dispatch parallel agents per wave
4. After each wave: collect outputs → verify → proceed or debug
