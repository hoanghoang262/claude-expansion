# Review Model

Three layers. Issues caught at smallest scope = cheapest to fix.

## Layer 1 — Per Task

After each task. Two stages for standard/heavy:

**Stage 1 — Spec compliance (spec-reviewer):**
Verifies implementation against each Success Criteria independently.

Required output — SC Verification Table:

| # | Success Criteria (exact from spec) | Status | Evidence |
|---|------------------------------------|--------|----------|
| 1 | {SC text} | ✅ / ❌ / ⚠️ | file:line |

- ✅ verified with evidence
- ❌ not found → task **cannot** be marked DONE
- ⚠️ partial — exists but missing test or edge case

Every finding must cite `file:line`. No "looks correct" without evidence.

**Stage 2 — Code quality (quality-reviewer):**
Checks: tests verify behavior, no unnecessary complexity, follows conventions.
Severity: Critical/Important → must fix. Minor → note and proceed.

**Light track:** subagent self-review only.

## Layer 2 — Per Group

After a cluster of tasks forming a meaningful capability. Checks: tasks integrate correctly, behavior consistent end-to-end, no gaps between individually-passing tasks.

**Standard/Heavy only.**

## Layer 3 — Final Integration

After all tasks. Checks: full implementation delivers spec, no regressions, all docs updated.

**Light:** skip. **Standard:** optional if coverage solid. **Heavy:** required.

## Escalation

If review finds: spec scope change needed, design flaw, unexpected long-term risk, or decision requiring user judgment → escalate with: what was found, why it matters, recommendation, request for decision.

Review does not expand scope, introduce new requirements, or block on style.
