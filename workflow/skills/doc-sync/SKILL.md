---
name: doc-sync
description: Update project docs to reflect what was built. Runs after execute, before branch completion.
---

# Doc Sync

```
[workflow:doc-sync] Assessing changes: <slug>
```

Update only what changed. Don't create docs for their own sake.

---

## Step 1 — Assess

Compare built (approved.md + commits) against existing `docs/`.

Per changed area:
- Existing doc describes this behavior? → update it
- New architectural decision? → create ADR
- Project overview changed? → update overview
- API/interface changed? → update reference

Skip unaffected docs. Skip docs that restate code.

---

## Step 2 — Update

| Change type | Doc to update |
|-------------|---------------|
| New feature behavior | `docs/overview.md` if it changes big picture |
| Architecture decision | New ADR: `docs/adr/YYYY-MM-DD-<decision>.md` |
| API or interface change | Relevant reference doc |
| Bug fix | Nothing unless it reveals design correction |
| Refactor | Nothing unless it changes public behavior |

**ADR format:**
```markdown
# ADR: <decision title>

Date: YYYY-MM-DD
Status: accepted

## Context
<why this decision was needed>

## Decision
<what was decided>

## Consequences
<what this enables, what it constrains>
```

---

## Step 3 — Announce

```
[workflow:doc-sync] Complete
Updated: <list>
Created: <list>
Skipped: <what and why>
```

Update STATE.md:
```
phase: done
next-action: Run superpowers:finishing-a-development-branch
```

---

## Memory rule

| Content | Where |
|---------|-------|
| Long-term architectural knowledge | `docs/` |
| Current project state | `.workflow/STATE.md` |
| Spec details | `.workflow/specs/<slug>/approved.md` |
| Session working notes | Nowhere — discard after session |

---

## Scale

| Track | Behavior |
|-------|----------|
| `light` | Usually nothing. Skip unless public behavior changed. |
| `standard` | Update affected docs. Add ADR if architectural. |
| `heavy` | Full assessment — overview, ADRs, references as needed. |
