# Review Model

Three layers. Issues caught at smallest scope = cheapest to fix.

## Layer 1 — Per Task

After each task. Checks: acceptance criteria met, spec compliant, edge cases handled, tests sufficient.

**Light:** subagent self-review only.
**Standard/Heavy:** separate spec-compliance reviewer subagent, then code-quality reviewer subagent.

## Layer 2 — Per Group

After a cluster of tasks forming a meaningful capability. Checks: tasks integrate correctly, behavior consistent end-to-end, no gaps between individually-passing tasks.

**Standard/Heavy only.**

## Layer 3 — Final Integration

After all tasks. Checks: full implementation delivers spec, no regressions, all docs updated.

**Light:** skip. **Standard:** optional if coverage solid. **Heavy:** required.

## Escalation

If review finds: spec scope change needed, design flaw, unexpected long-term risk, or decision requiring user judgment → escalate with: what was found, why it matters, recommendation, request for decision.

Review does not expand scope, introduce new requirements, or block on style.
