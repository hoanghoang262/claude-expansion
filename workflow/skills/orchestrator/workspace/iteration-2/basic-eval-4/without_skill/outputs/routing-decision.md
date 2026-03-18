# Routing Decision

**Phase: Verify (verify.md)**

## Analysis

| Factor | Value |
|--------|-------|
| Intent | Review/Inspect existing code |
| Keywords detected | "review", "code" |
| Existing spec | N/A - not relevant for review task |
| Scope | Small (review task) |

## Why Verify Phase?

Following the orchestrator's routing logic:

1. **Intent Detection**: The keyword "review code" clearly maps to verification/review activity, which routes to `references/verify.md`

2. **Not Spec (spec-form)**: This is not a build/implement task - no new feature creation requested

3. **Not Plan**: No spec mentioned, but this is also not about planning a new feature - it's about reviewing existing code

4. **Not Execute**: This is not an implementation task

5. **Not Research**: Not asking to research/understand something new - existing code is already there to be reviewed

6. **Not Understand**: Not asking to understand or investigate a problem - specifically asking to "review" which implies verification/inspection

7. **Verify fits perfectly**: The phrase "review code" directly maps to the verify phase which handles code review, inspection, and validation activities

## Recommendation

Route to `references/verify.md` to perform code review on the provided code.
