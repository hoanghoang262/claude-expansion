# Phase [N] — Plan [M]: [Name]

## Objective

[What this plan achieves]

## Context

- Feature: {id}-{name}
- Spec: [link to spec.md]
- Phase: {N}

## Tasks

### TASK-{N}: [Name]
**Type:** auto | checkpoint:human-verify | checkpoint:decision | checkpoint:human-action
**Files:** [create/modify]
**Action:**
```
[Detailed step-by-step instructions]
```
**Verify:**
```
[How to verify completion]
```
**Requirements:** REQ-01, REQ-02

### TASK-{N+1}: [Name]
**Type:** auto
...

## Dependencies

```
TASK-1 ─┬─→ TASK-3 ──→ TASK-5
         └→ TASK-4 ──→ TASK-5
```

## Wave Assignment

| Wave | Tasks | Parallel? | Checkpoints |
|------|-------|-----------|-------------|
| 1 | TASK-1, TASK-2 | ✓ (independent) | - |
| 2 | TASK-3, TASK-4 | ✓ (after TASK-1) | - |
| 3 | TASK-5 | - | checkpoint:human-verify |

## Effort Estimate

| Task | Estimate |
|------|----------|
| TASK-1 | ~15 min |
| TASK-2 | ~10 min |
| **Total** | ~45 min |
