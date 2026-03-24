# plan

**Phase:** IMPLEMENT — Task breakdown

## Purpose

Break approved spec into micro-tasks grouped into execution waves.

## Iron Law

`EVERY TASK MUST HAVE TEST CRITERIA BEFORE IMPLEMENT. NO EXCEPTIONS.`

---

## Steps

### Step 1 — Read inputs

- `docs/features/{name}/spec.md` (approved) — acceptance criteria, components, file changes
- `docs/rules/` — git-workflow, coding-standards, testing-strategy
- `docs/state.md` — current wave progress (if resuming)

### Step 2 — Decompose into tasks

Each task must:
- Take ~2-5 minutes for an implementer
- Touch at most 1-2 files
- Be independently verifiable (has runnable test)
- Have no implicit dependencies (dependencies are explicit)

Task format:
```
### TASK-{N}: {name}

ACTION: [create | modify | delete | test]
FILES: [list of files]
WHAT: [what to implement — reference spec section]
TEST: [specific test that proves this task is done]
DEPENDS_ON: [TASK-N, TASK-M or "none"]
```

### Step 3 — Group into waves

- Wave 1: Tasks with no dependencies
- Wave 2: Tasks that depend only on Wave 1
- Wave N: Tasks that depend on Wave N-1

Max 5 tasks per wave (parallel execution limit).

### Step 4 — Write PLAN.md

Write to `docs/features/{name}/PLAN.md`:
```
# Plan: {feature name}

## Objective
[one sentence]

## Waves

### Wave 1 (parallel)
- TASK-1: ...
- TASK-2: ...

### Wave 2 (parallel, after Wave 1)
- TASK-3: ...

## Task Details
[full task definitions]

## Dependencies Diagram
[ASCII or list]

## Risks
[what could go wrong, mitigation]
```

### Step 5 — Update state

Update `docs/state.md`:
```
Phase: IMPLEMENT
Action: execute
Feature: {name}
Wave: 1/{total}
Tasks: [ ] TASK-1 [ ] TASK-2 ...
```

Route to `execute`.
