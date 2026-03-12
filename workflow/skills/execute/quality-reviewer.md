---
name: execute/quality-reviewer
description: Prompt template for code quality reviewer subagent. Runs after spec compliance is confirmed.
---

# Code Quality Reviewer Prompt

## Per-task review

```
Review Task {N} for code quality.

Commits: {git SHAs}
Project conventions: {from PROJECT.md}

Check:
- Tests exist and are meaningful (not just passing)
- No magic numbers, unclear names, dead code
- No unnecessary complexity or premature abstraction
- Follows project conventions

Output: ✅ Approved | Issues: [Critical | Important | Minor] — [list]
```

## Final integration review (Step 6)

```
Review complete implementation against approved spec.

approved.md: {full text}
All commits since task-breakdown: {SHAs}
Project conventions: {from PROJECT.md}

Check:
- Full implementation delivers the spec end-to-end?
- Integration issues between tasks?
- No regressions introduced?
- All required docs updated?

Output: ✅ Ready to ship | ❌ Issues: [list]
```

**Severity guide:**
- **Critical** — broken behavior, security issue, spec violated → must fix before proceeding
- **Important** — poor design, missing tests, hard to maintain → must fix before proceeding
- **Minor** — style, naming, small improvements → note and proceed
