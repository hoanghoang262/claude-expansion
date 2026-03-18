# Verify Phase

Test, review, validate implementation against spec.

## Inputs Needed

1. **Spec** - `docs/specs/<slug>/spec.md`
2. **Implementation** - Code that was implemented
3. **Tasks log** - `.workflow/specs/<slug>/log/`

## Process

### 1. Load Context

```
Read:
1. docs/specs/<slug>/spec.md
2. All implemented files
3. Task log
```

### 2. Verify Against Spec

Check each SC:

```
SC-001: <criteria>
- [ ] Verified: <how tested>
- [ ] Result: pass/fail
```

### 3. Test

**If project has test runner:**
```
Run tests: <test command>
```

**If no tests:**
```
Manual verification:
- [ ] Test case 1
- [ ] Test case 2
```

### 4. Code Review

**Self-review:**
- Completeness: Every FR met?
- Quality: Follows patterns?
- Testing: Edge cases covered?
- Discipline: No extra features?

**If user requests or heavy track:**
→ Use `workflow/agents/quality-reviewer.md`

### 4.5. Regression Check

Before merge gate, check:

1. **Existing tests**: Run full test suite if project has
   - Pass → proceed to merge gate
   - Fail → check which tests fail, is it due to new feature?

2. **Scope check**: `git diff --stat`
   - Only files in task scope → OK
   - Files outside scope changed → need explanation

3. **Lint** (if project has): must pass before merge

### 5. Merge Gate

Check before merge:
- [ ] All tasks ✅
- [ ] All SCs verified ✅
- [ ] No debug code / TODOs
- [ ] Tests pass
- [ ] Docs updated

### 6. Report

```
[workflow:verify] ✅ <slug> verified

SC Results:
- SC-001: ✅
- SC-002: ✅

Tests: <pass/fail>
Ready to merge: yes/no
```

## Verification Types

| Type | When | Method |
|------|------|--------|
| Light | Light track | Self-review only |
| Standard | Standard track | Self-review + SC verification |
| Heavy | Heavy track | Full review + tests |

## Docs Responsibility

| Action | Docs to update |
|--------|----------------|
| SC verified | `docs/specs/<slug>/spec.md` (add verification notes) |
| Test results | `docs/specs/<slug>/test-results.md` |
| Issues found | `docs/specs/<slug>/issues.md` |

## Output

- Verification report
- Ready to merge: yes/no
- Issues list (if any)

## Jump to Next Phase

| Situation | Next Phase |
|-----------|-------------|
| Verified, ready | `doc-sync.md` |
| Issues found | Return to `execute.md` |
| Major issues | Surface to user |
