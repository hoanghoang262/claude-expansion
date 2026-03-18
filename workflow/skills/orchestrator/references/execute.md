# Execute Phase

Implement tasks using subagents or agent teams.

## When to Enter

- Plan ready → need to implement
- After understand (for bug fixes)
- User says: "implement", "làm đi", "code"

## Routing: Subagent vs Agent Team

Choose based on task complexity:

| Situation | Solution | Why |
|-----------|----------|-----|
| Single task, simple | Subagent (implementer) | Fast, cheap |
| Single task, complex bug | Agent team (researcher + implementer) | Parallel investigation |
| Multiple tasks, independent | Multiple subagents in parallel | Speed |
| Multiple tasks, complex | Agent team (multi-implementer) | Parallel work |
| Review needed | Subagent (spec/quality reviewer) | Enough |

### Decision Guide

| Scenario | Use | Why |
|----------|-----|-----|
| Task < 5 min, trivial (typo, rename) | Do yourself | Too small, spawn agent wastes resources |
| 1 clear task (add 1 component, 1 API) | Subagent | Small scope, focused |
| Multiple independent tasks same type | Parallel subagents | No dependency → fast + cheap |
| Multiple dependent tasks, different domains | Agent team | Need sync: merge intermediate, wait |
| Review (spec or quality) | Subagent | Always 1 scope, 1 purpose |
| Research | Subagent | 1-way: ask → answer, no collab needed |

### Summary
```
Do yourself:       task < 5 min, trivial
Subagent:          1 clear task, no coordination needed
Parallel subagents: multiple INDEPENDENT tasks
Agent Team:        multiple DEPENDENT tasks, different domains, need sync
```

## Process

### 1. Load Context

```
Read:
1. docs/specs/<slug>/spec.md (goal, FRs, SCs)
2. docs/specs/<slug>/plan.md (tasks)
3. Relevant codebase
```

### 2. Route Execution

**Simple → Subagent:**
```
Use subagent with agent definition at:
workflow/agents/implementer.md

Task: {specific task}
Context: {spec excerpt, relevant files}
```

**Complex → Agent Team:**
```
Create agent team:
- Teammate 1: researcher (workflow/agents/researcher.md) — investigate approach
- Teammate 2: implementer (workflow/agents/implementer.md) — build

When teammates done → aggregate results
```

### 3. Per Task Loop

#### Task Brief

```
[workflow:execute] Task {N}/{total} — <title>
```

Produce Task Brief:
- Title, FR mapping
- Files to create/modify
- Acceptance criteria
- Risk notes (if heavy)

#### Dispatch Implementer

→ Use `workflow/agents/implementer.md`

Pack context:
- Relevant spec excerpt
- Full task text
- Codebase patterns

Implementer asks questions → answer completely → reload

#### Review

**Light:** Self-review only → proceed

**Standard/Heavy:**

```
[workflow:review] Task {N} — spec compliance
```
→ Use `workflow/agents/spec-reviewer.md`

- ✅ → quality review
- ❌ → re-implement → re-review

```
[workflow:review] Task {N} — code quality
```
→ Use `workflow/agents/quality-reviewer.md`

- ✅ → approved
- ❌ Critical → re-implement → re-review
- ❌ Minor → note, proceed

#### Complete

```
[workflow:review] ✅ Task {N} — approved
```

Update task log:

```markdown
| {N} | <title> | ✅ | <output> | <issues or none> |
```

### 4. Parallel Tasks

Tasks with no shared files → dispatch concurrently:

```
[workflow:execute] Dispatching parallel: Task 1, 3, 5
```

Each task still goes through review independently.

### 5. All Done

```
[workflow:execute] All {N} tasks complete
```

→ Verify phase
→ Doc sync (update spec with completion)

## Agent Team Pattern

For features requiring multiple expertise or dependent layers.

### When to use:
- Feature needs BE + FE integration
- Refactor multiple related modules
- Full-stack: DB + API + UI

### Setup:
- Lead: orchestrator (you)
- Teammates: split by domain/layer, each gets own worktree

### Flow:
1. Lead splits scope → each teammate gets work + own worktree
2. Teammates work PARALLEL
3. Teammate A finishes → merge into feature branch
4. Teammate B needs resource from A → pull from feature branch → continue
5. Repeat until done
6. Final merge → verify

### Example: Build login feature
```
Teammate A (BE): auth API, JWT, DB schema
  → worktree: .worktrees/login-be

Teammate B (FE): login form, validation, API integration
  → worktree: .worktrees/login-fe

Flow:
  A + B run parallel
  A finishes API endpoints → merge to feat/login
  B pulls feat/login → integrate with API
  B finishes → merge to feat/login
  → verify → done
```

### DO NOT use agent team for:
- Independent tasks → use parallel subagents (cheaper)
- Research → use subagent researcher (1-way task)
- Review → use subagent reviewer (1 scope)

## Docs Responsibility

| Action | Docs to update |
|--------|----------------|
| Implementation done | `docs/specs/<slug>/spec.md` (SC marked done) |
| Code patterns | Code comments |
| Findings | `.workflow/log/` |

## Output

- All tasks implemented
- Review passed
- Commits made

## Jump to Next Phase

| Situation | Next Phase |
|-----------|-------------|
| All tasks done | `verify.md` |
| Task failed 2x | Surface to user |
| Need more info | Ask user |
