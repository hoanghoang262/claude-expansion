---
name: task-breakdown
description: Decompose an approved spec into independently verifiable tasks with explicit dependencies and parallelization.
---

# Task Breakdown

Turn `approved.md` into an executable `tasks.md`.
Each task must be independently verifiable — implementing just one task delivers real value.

---

## Step 0 — Read inputs

1. `approved.md` — the locked contract
2. `PROJECT.md` — tech stack, conventions, constraints
3. Any existing code — understand current state before decomposing

---

## Step 1 — Decompose

Break the spec into tasks. A task is the **smallest unit that can be independently committed and verified**.

Rules:
- One concern per task — don't bundle unrelated changes
- Each task is testable in isolation
- Tasks must map to specific FRs or SCs from the spec — no tasks without spec backing
- Order by dependency: infrastructure first, features second, integration last

**Task format:**

```markdown
### Task {N} — {title}
**Spec ref:** FR-{N} / SC-{N}
**Parallel:** yes | no
**Depends on:** Task {N} | none

#### What to build
<one paragraph — behavior, not implementation>

#### Files
- Create: `path/to/file`
- Modify: `path/to/existing:L10-L50`
- Test: `path/to/test`

#### Acceptance
- [ ] <specific verifiable outcome>
- [ ] <specific verifiable outcome>

#### Steps (standard/heavy only)
1. Write failing test for <behavior>
2. Run → confirm FAIL
3. Implement minimal code
4. Run → confirm PASS
5. Commit: `type(scope): message`
```

---

## Step 2 — Mark parallelization

After all tasks are listed, identify groups that can run in parallel (no shared state, no output-input dependency).

```markdown
## Execution Order

Sequential:
- Task 1 → Task 2 (Task 2 needs Task 1's output)

Parallel group A (after Task 1):
- Task 3 [P]
- Task 4 [P]
- Task 5 [P]

Sequential:
- Task 6 (integrates A)
```

---

## Step 3 — Save + update state

Save to `.workflow/specs/<slug>/tasks.md`.

Update STATE.md:
```
phase: execute
next-action: Begin Task 1
```

Announce:
```
[Tasks ready] {N} tasks across {M} parallel groups → .workflow/specs/<slug>/tasks.md
Next: execute
```

---

## Scale

| Track | Behavior |
|-------|----------|
| `light` | 1–3 tasks, no steps section, no parallelization map needed |
| `standard` | Full task format, steps section, parallelization map |
| `heavy` | Full format + dependency graph + risk notes per task |
