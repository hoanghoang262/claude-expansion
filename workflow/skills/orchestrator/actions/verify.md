# verify

**Phase:** IMPLEMENT — Final verification

## Purpose

Confirm the full feature works end-to-end against acceptance criteria.

## Iron Law

`DO NOT SAY "COMPLETE" WITHOUT TEST OUTPUT.`

---

## Steps

### Step 1 — Build acceptance checklist

Extract all AC-xxx items from `docs/features/{name}/spec.md` → Technical Design → Acceptance Criteria.

### Step 2 — Run verification

For each AC item:
1. Run the test/check specified
2. Mark: ✅ PASS (with evidence: output/file:line) or ❌ FAIL (with reason)

Also run:
- Full test suite (unit + integration)
- Regression check: does anything else break?

### Step 3 — Evaluate results

**All PASS:**
→ Present summary to user:
```
Feature {name} — Verification complete

✅ AC-001: [description] — [evidence]
✅ AC-002: [description] — [evidence]
...

All [N] acceptance criteria passed. Ready to ship.
```
→ Update `docs/state.md` → verified: true
→ Ask user: new feature or done?

**Any FAIL:**
→ Route to `debug`:
```
Verification failed:
❌ AC-003: [description] — [reason]

Routing to debug.
```

### Step 4 — After user confirms complete

- Write learnings (if any patterns found) to `docs/learnings/{date}-{pattern}.md` [PERMANENT]
- Review if any `rules/` need updating → notify user before updating
- Update `docs/state.md` → Phase: done
