# Routing Decision

**Task**: "spec đã approve rồi, implement đi"

## Phase: **Plan**

## Reasoning

1. **Intent Classification**: User says "spec đã approve rồi" (spec is already approved) — this matches the Intent Router pattern:
   - "spec rồi", "có spec", "làm tiếp" → Jump to `references/plan.md`

2. **Workflow Logic**: After spec is approved, the natural next step is to break the spec into executable tasks before implementation begins.

3. **Eval Reference**: This matches eval-7 in evals.json where the expected phase is "plan".

## Next Action

Load the existing spec from `docs/specs/<slug>/spec.md` and proceed to Plan phase to break it into executable tasks.
