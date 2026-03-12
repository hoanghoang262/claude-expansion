---
name: orchestrator/task-breakdown
description: Decompose approved spec into tasks. Loaded when entering task breakdown phase.
---

# Task Breakdown

**Light track → skip. Go directly to execute.**

```
[workflow:task-breakdown] Decomposing: <slug>
```

Read: `docs/specs/<slug>/spec.md`, `docs/PROJECT.md`, relevant codebase.

---

## Task format

Create tasks using Claude Code task tool (TodoWrite):

```
Title: Task N — <name>

Spec ref: FR-N / SC-N
What to build: <one paragraph — behavior not implementation>

Files:
  Create: path/to/file
  Modify: path/to/existing:L10-L50
  Test: path/to/test

Acceptance:
  - [ ] specific verifiable outcome

Steps (standard/heavy only):
  1. Write failing test
  2. Run → confirm FAIL
  3. Implement minimal code
  4. Run → confirm PASS
  5. Commit: type(scope): message

Risk notes (heavy only):
  Risk: <what could go wrong>
  Mitigation: <how to handle>
```

Every task must map to a specific FR or SC. No tasks without spec backing.

---

## Parallelization (standard/heavy)

Identify task groups with no shared files and no dependencies. Note in task body:
```
Parallel: yes — no shared files with Task N
Depends on: Task N | none
```

---

## Completion

```
[workflow:task-breakdown] {N} tasks created. Next: execute
```

| Track | Behavior |
|-------|----------|
| `light` | Skip entirely |
| `standard` | Full format + steps |
| `heavy` | Full format + steps + risk notes |
