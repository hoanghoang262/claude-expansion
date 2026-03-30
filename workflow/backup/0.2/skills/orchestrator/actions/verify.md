# verify

**Phase:** ACT — Final verification against acceptance criteria.

<hard_constraint never_override>
DO NOT say "complete" without test output evidence.
</hard_constraint>

---

## Steps

### Step 1 — Build acceptance checklist

Extract all acceptance scenarios from `docs/features/{name}/user-stories.md` (Given/When/Then).
Also read `docs/features/{name}/requirements.md` for SC-xxx (success criteria).

### Step 2 — Run verification

For each acceptance scenario:
1. Run the test/check
2. Mark: ✅ PASS (with evidence: output/file:line) or ❌ FAIL (with reason)

Also run:
- Full test suite (unit + integration)
- Regression check: does anything else break?

### Step 3 — Evaluate results

**All PASS:**
```
Feature {name} — Verification complete

✅ US-001: {scenario} — {evidence}
✅ US-002: {scenario} — {evidence}
✅ SC-001: {criteria} — {evidence}
...

All [{N}] acceptance criteria passed. Ready to ship.
```

Update `docs/state.md` → Phase: UNDERSTAND, Action: clarify, Feature: none, Wave: n/a.
Ask user: next feature or done?

**Any FAIL:**
```
❌ US-003: {scenario} — {reason}

Routing to debug.
```
Read `actions/debug.md`, then route → `debug`.

### Step 4 — After complete

- Write learnings to `docs/learnings/{date}-{pattern}.md` using `templates/learning-template.md` if patterns found
- Review if `.claude/rules/` need updating → ask user before changing
- Clean up: spec.md can stay or be removed (working file, git has history)
- Update `docs/state.md` (same reset as Step 3 if not yet done): Phase: UNDERSTAND, Action: clarify, Feature: none, Wave: n/a
