# Feature: {name} — Plan

## Objective
[1 sentence: What this plan achieves]

## Context
- Feature: {id}-{name}
- Spec: docs/features/{id}/spec.md

## Wave Assignment

| Wave | Tasks | Parallel? | Checkpoints |
|------|-------|-----------|-------------|
| 1 | TASK-1, TASK-2 | ✓ (independent) | - |
| 2 | TASK-3, TASK-4 | ✓ (after TASK-1) | - |
| 3 | TASK-5 | - | checkpoint:human-verify |

## Tasks

### TASK-{N}: {Name}
**Type:** auto | checkpoint:human-verify | checkpoint:decision | checkpoint:human-action
**Files:** {path} ({action})
**Action:**
```
{Detailed step-by-step instructions}
```
**Verify:**
```
{How to verify completion}
```
**Requirements:** REQ-01, REQ-02

### TASK-{N+1}: {Name}
...

## Dependencies

```
TASK-1 ─┬─→ TASK-3 ──→ TASK-5
         └─→ TASK-4 ──→ TASK-5
```

## Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| ... | ... | ... |

## Effort Estimate

| Task | Estimate |
|------|----------|
| TASK-1 | ~15 min |
| TASK-2 | ~10 min |
| ... | ... |
| **Total** | ~45 min |
