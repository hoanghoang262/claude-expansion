---
name: doc-sync
description: Update project docs to reflect what was actually built. Runs after execute, before branch completion.
---

# Doc Sync

Keep docs honest. Update only what changed. Don't create docs for their own sake.

---

## Step 1 — Assess what changed

Compare what was built (approved.md + commits) against existing docs in `docs/`.

Ask per changed area:
- Does any existing doc describe this behavior? → update it
- Is this a new architectural decision? → create ADR
- Does this change the project overview? → update overview
- Is there an API/interface change? → update relevant reference

Skip docs that are unaffected. Skip docs that would just restate the code.

---

## Step 2 — Update

**What to update (by type):**

| Change type | Doc to update |
|-------------|---------------|
| New feature behavior | `docs/overview.md` if it changes the big picture |
| Architecture decision | New ADR: `docs/adr/YYYY-MM-DD-<decision>.md` |
| API or interface change | Relevant reference doc |
| Bug fix | Nothing unless it reveals a design correction |
| Refactor | Nothing unless it changes public behavior |

**ADR format (when needed):**
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

## Step 3 — Memory rule

| Content | Where |
|---------|-------|
| Long-term architectural knowledge | `docs/` |
| Current project state | `.workflow/STATE.md` |
| Spec details | `.workflow/specs/<slug>/approved.md` |
| Session working notes | Nowhere — discard after session |

Do not write session thinking into docs. Docs capture decisions and outcomes, not process.

---

## Step 4 — Announce

```
[Doc sync complete]
Updated: <list of files touched>
Created: <list of new files>
Skipped: <what was assessed but not changed, and why>
```

Update STATE.md:
```
phase: done
next-action: Run superpowers:finishing-a-development-branch
```

---

## Scale

| Track | Behavior |
|-------|----------|
| `light` | Usually nothing. Skip unless a public behavior changed. |
| `standard` | Update affected docs. Add ADR if architectural. |
| `heavy` | Full assessment. Overview, ADRs, reference docs as needed. |
