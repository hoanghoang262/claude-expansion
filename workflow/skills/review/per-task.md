---
name: review/per-task
description: Orchestrate two-stage review for a single task. Launches spec-reviewer agent, then quality-reviewer agent.
---

# Per-Task Review

## Stage 1 — Spec compliance

```
[workflow:review] ⏳ Task {N} — spec compliance
```

Launch `workflow:agents/spec-reviewer` with:
- `SPEC`: approved.md excerpt for this task
- `TASK`: full task definition + acceptance criteria
- `COMMITS`: git SHAs from implementer

- ✅ → proceed to Stage 2
- ❌ → return issues to execute → implementer fixes → re-launch spec-reviewer
- Never proceed to Stage 2 while Stage 1 has open issues

## Stage 2 — Code quality

```
[workflow:review] ⏳ Task {N} — code quality
```

Launch `workflow:agents/quality-reviewer` with:
- `COMMITS`: git SHAs
- `CONVENTIONS`: from PROJECT.md
- `SCOPE`: per-task

- ✅ → review complete
- Critical/Important → return to execute → implementer fixes → re-launch quality-reviewer
- Minor → note, proceed

## On completion

```
[workflow:review] ✅ Task {N} — approved
```

Return to execute: ✅ approved | ❌ issues: [list]
