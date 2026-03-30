# Concern Resolution

How PA handles issues — from self-fix to user escalation.

---

## Three tiers

| Tier | When | Action |
|------|------|--------|
| 1 — Self-resolve | Minor, fixable in context | Fix → log briefly → continue. Never stop work. |
| 2 — Concern | Non-blocking gap, may affect future work | Write `docs/.pa/concerns/CONCERN-{topic}.md` → continue |
| 3 — User notify | Blocker that cannot be resolved without user input | AskUserQuestion with: issue · what was tried · options · recommendation |

Always try Tier 1 before Tier 2. Always try Tier 2 before Tier 3.

**Tier 3 only for:** external dependency failure · spec gap discovered mid-execute · irreversible risk.
**Not Tier 3:** minor bugs (Tier 1) · code smell (Tier 2) · missing spec detail → "Spec does not cover X. Updating spec before continuing."

---

## Concern file format

```
docs/.pa/concerns/CONCERN-{topic}.md

# Concern: {title}
Status: open | resolved
Tier: 2
Discovered: {when}

## Issue
{what the problem is}

## Impact
{what it affects}

## Resolution
{how it was resolved — fill when done}
```

---

## Concern lifecycle

```
Discovered → Tier 1 attempt → still blocking?
  NO → log briefly in docs/.pa/state.md → continue
  YES → write CONCERN-*.md in docs/.pa/concerns/ (Tier 2) → continue

At next session start → PA reads docs/.pa/concerns/ → checks status
Resolved in context → update CONCERN file → mark resolved
Still blocking after Tier 2 → escalate Tier 3 → AskUserQuestion
```

Concerns are **internal** — user never sees Tier 1 or Tier 2. Only Tier 3 surfaces to user.
