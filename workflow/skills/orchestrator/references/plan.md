# Plan Phase

Break spec into executable tasks.

## Inputs Needed

1. **Spec** - `docs/specs/<slug>/spec.md`
2. **Track** - light, standard, heavy

## Process

### 1. Load Spec

```
Read: docs/specs/<slug>/spec.md
```

### 2. Analyze Requirements

For each FR:
- What files need changes?
- What's the implementation approach?
- Any dependencies between FRs?

### 3. Create Tasks

Create `docs/specs/<slug>/plan.md`:

```markdown
# Plan: <slug>

## Overview
<summary>

## Tasks

### Task 1 — <title>
- **FR**: FR-001
- **What**: <one paragraph — behavior not implementation>
- **Files**:
  - Create: path/to/file
  - Modify: path/to/existing:L10-L50
- **Acceptance**:
  - [ ] <verifiable outcome>
- **Parallel**: yes/no — <reason>
- **Depends on**: Task N | none

### Task 2 — <title>
...

## Parallelization

Tasks that can run in parallel (no shared files):
- Task 1 + Task 3
- Task 2 + Task 4
```

## Git Strategy

### Branch
When spec approved → create feature branch:
```bash
git checkout -b feat/<slug>
```

### Worktree for parallel tasks
Each parallel group needs own worktree to avoid conflict:

```bash
# Create worktree per group
git worktree add .worktrees/<slug>-g1 -b feat/<slug>-g1
git worktree add .worktrees/<slug>-g2 -b feat/<slug>-g2
```

### Worktree for agent team
Each teammate needs own worktree by domain:

```bash
git worktree add .worktrees/<slug>-be -b feat/<slug>-be
git worktree add .worktrees/<slug>-fe -b feat/<slug>-fe
```

### Conflict avoidance
When splitting tasks into groups — ensure no 2 tasks/teammates edit same file.
If forced to share file → do sequential, not parallel.

AI decides — small conflicts merge normally. Big conflicts surface to user.

| Track | Behavior |
|-------|----------|
| Light | Skip detailed plan, go to execute |
| Standard | Full plan with files + acceptance |
| Heavy | Full plan + risk notes |

## Task Format

Every task must:
- Map to specific FR(s)
- Have clear acceptance criteria
- Specify files (create/modify)
- Note dependencies

## Docs Responsibility

| Action | Docs to update |
|--------|----------------|
| Plan created | `docs/specs/<slug>/plan.md` |
| Related specs | `docs/specs/<other>/spec.md` (nếu có dependencies) |

## Output

- Task list in `docs/specs/<slug>/plan.md`
- Clear dependencies identified
- Parallel groups identified

## Jump to Next Phase

| Situation | Next Phase |
|-----------|-------------|
| Plan ready | `execute.md` |
| Need clarification | Ask user |
| Plan is simple | Go to execute.md directly (light track) |
