# Action: Spec

Triggered in DEFINE phase when task is complex enough to need formal definition before building.

---

## When to trigger

- Multiple agents will be involved
- Work spans more than one session
- Ambiguity exists about what "done" looks like
- Risk of building the wrong thing is high

## Steps

1. Write spec covering:
   - Goal: what this achieves and why
   - Scope: what is included, what is explicitly not included
   - Acceptance criteria: testable conditions for "done"
   - Constraints: tech, time, approach limits
2. Save to `docs/[detail layer]/` — appropriate location per project type
3. Present to user for approval
4. Wait for explicit approval before proceeding to BUILD
5. Spec is frozen after approval — no requirement changes accepted in BUILD
