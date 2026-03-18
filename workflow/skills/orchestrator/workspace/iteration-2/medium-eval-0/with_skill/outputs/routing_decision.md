# Routing Decision

**Phase:** `plan`

## Reasoning

User says: "spec đã approve rồi, implement đi"

Based on SKILL.md Step 1 - Intent Router:

| User says | Jump to |
|------------|---------|
| "spec rồi", "có spec", "làm tiếp" | `references/plan.md` |

This matches the keyword "spec rồi" (spec already done/approved).

## Analysis

1. **Intent detected:** User has a completed/approved spec and wants to proceed with implementation
2. **Workflow context:** The orchestrator workflow follows: Understand → Brainstorm → Spec → **Plan** → Execute → Verify
3. **Current state:** Spec is approved, next logical step is to create a plan for implementation

## Decision

Route to **plan** phase to break the implementation into tasks before executing.

## Reference

- `references/plan.md` — Break into tasks
