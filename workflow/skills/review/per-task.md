---
name: review/per-task
description: Two-stage review after each implemented task. Spec compliance first, then code quality.
---

# Per-Task Review

## Stage 1 — Spec compliance

```
[workflow:review] ⏳ Task {N} — spec compliance
```

Use prompt template: `./spec-reviewer.md`

- ✅ → proceed to Stage 2
- ❌ → return issues to execute, implementer fixes, re-run Stage 1
- Never proceed to Stage 2 while Stage 1 has open issues

## Stage 2 — Code quality

```
[workflow:review] ⏳ Task {N} — code quality
```

Use prompt template: `./quality-reviewer.md`

- ✅ → review complete
- Critical/Important → return to execute, implementer fixes, re-run Stage 2
- Minor → note, proceed

## On completion

```
[workflow:review] ✅ Task {N} — approved
```

Return result to execute: ✅ approved | ❌ issues: [list]
