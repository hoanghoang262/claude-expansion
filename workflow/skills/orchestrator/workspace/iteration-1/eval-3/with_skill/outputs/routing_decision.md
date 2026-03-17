# Routing Decision

## Task
"research về các auth options"

## Phase: Research

**Reference**: `references/research.md`

## Why

1. **Explicit intent match**: The user explicitly says "research" - this directly matches the Intent Router rule: `"research", "tìm hiểu"` → `references/research.md`

2. **Investigation phase**: The task is about exploring authentication options before making a decision. This is precisely what the Research phase is designed for - investigation, analysis, and exploration of options.

3. **Pre-decision work**: The user wants to understand auth options first (likely to make an informed decision later about which auth solution to implement).

## Next Steps After Research

Based on the Research phase's "Jump to Next Phase" guidance:
- If decision is made → route to `spec-form.md` (create spec for chosen auth)
- If need to plan → route to `plan.md`
- If more research needed → stay in Research
