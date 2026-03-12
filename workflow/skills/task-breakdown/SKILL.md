---
name: task-breakdown
description: Decompose approved spec into independently verifiable tasks with parallelization map.
---

# Task Breakdown

```
[workflow:task-breakdown] Decomposing: <slug>
```

Turn `approved.md` into `tasks.md`. Each task = smallest unit that can be independently committed and verified.

---

## Step 0 — Read inputs

1. `approved.md` — locked contract
2. `PROJECT.md` — tech stack, conventions, constraints
3. Existing codebase state — understand before decomposing

---

## Step 1 — Decompose

Rules:
- One concern per task
- Each task independently testable
- Every task maps to specific FR or SC — no tasks without spec backing
- Order: infrastructure → features → integration

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

**Heavy track extras:**
```markdown
#### Risk notes
- Risk: <what could go wrong>
- Mitigation: <how to handle>
```

---

## Step 2 — Parallelization map

```markdown
## Execution Order

Sequential:
- Task 1 → Task 2 (Task 2 needs Task 1's output)

Parallel group A (after Task 1):
- Task 3 [P]
- Task 4 [P]

Sequential:
- Task 5 (integrates A)
```

Heavy: add dependency graph after map.

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
[workflow:task-breakdown] {N} tasks across {M} parallel groups → tasks.md
Next: execute
```

---

## Scale

| Track | Behavior |
|-------|----------|
| `light` | 1–3 tasks, no steps section, no parallelization map |
| `standard` | Full format, steps section, parallelization map |
| `heavy` | Full format + dependency graph + risk notes |
