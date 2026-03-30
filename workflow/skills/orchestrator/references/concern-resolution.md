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

See `templates/concern.md`. Key fields:

- **Status:** `open` → `investigating` → `resolved`
- **Affects:** which phase or component — PA uses this to skip irrelevant concerns when scanning
- **Escalate if:** condition that would make this Tier 3 — makes escalation criteria explicit

---

## Concern lifecycle

```
Discovered → Tier 1 attempt → still blocking?
  NO → log briefly in docs/.pa/state.md → continue
  YES → write CONCERN-{topic}.md in docs/.pa/concerns/ (Tier 2) → continue

At next session start → PA reads docs/.pa/concerns/ → checks Status field
PA begins working it → update Status: investigating
Resolved in context → update Status: resolved, fill Resolution
Still blocking after Tier 2 → escalate Tier 3 → AskUserQuestion
```

Concerns are **internal** — user never sees Tier 1 or Tier 2. Only Tier 3 surfaces to user.
