# review-concerns — Concern Check & Resolution

## When to Run

- After **every action transition** (before selecting the next action)
- After **doc-sync** completes
- Before suggesting **version-release**
- When user says "continue"
- When a subagent reports a concern

## Step 1: Scan for open concerns

```
Read: docs/concerns/*.md
Filter: status: open
```

No open concerns → done. Proceed to next action.

## Step 2: Present to user

```
Open concerns found ({count}):

{CONCERN-1}: {title} | Severity: {level} | Status: {status}
  {1-line summary}
  Discovered by: {agent}

{CONCERN-2}: ...

Resolution options:
  1. resolve → spawn fix task immediately
  2. defer   → add to ROADMAP as a feature
  3. reject  → mark closed with note (explain why)
```

Present all at once — do not interrupt the main flow.

## Step 3: Apply resolution

| Choice | Action |
|--------|--------|
| `resolve` | Spawn implementer subagent → mark concern `status: resolved` after fix |
| `defer` | Add to ROADMAP.md → mark concern `status: deferred` |
| `reject` | Add note → mark concern `status: closed` |

## Step 4: Continue

After applying all resolutions → proceed to next action.

## Rules

- Never skip this check. It protects the main flow from accumulating debt.
- Never stop the main flow to fix a concern — resolve in parallel or defer.
- If a concern is `Severity: high` and user is absent → log but proceed with caution.
