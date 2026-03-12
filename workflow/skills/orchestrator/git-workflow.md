---
name: orchestrator/git-workflow
description: Git branch + worktree rules. Loaded when spec is approved and when ready to merge.
---

# Git Workflow

Every feature or fix lives on its own branch. Never implement on main.

---

## Starting a feature

When spec approved → create branch + worktree:

```bash
git worktree add ../<slug> -b feat/<slug>
```

```
[workflow:git] Branch feat/<slug> created — working in ../<slug>/
```

All agents work inside the worktree. Every commit lands on `feat/<slug>`.

Branch naming:
- New feature → `feat/<slug>`
- Bug fix → `fix/<slug>`
- Experiment → `exp/<slug>`

---

## Parallel tasks

Independent task groups → separate worktrees on same branch:

```bash
git worktree add ../<slug>-taskN feat/<slug>
```

No shared files between parallel tasks = no conflicts.
Merge worktree commits back to `feat/<slug>` after each task group completes.

---

## Merging to main

After final review + doc sync:

```
[workflow:git] Ready to merge — feat/<slug> → main
```

Checklist before merging:
1. Full test suite passes on `feat/<slug>`
2. `git diff main...feat/<slug>` — review what's going in
3. No open issues in `.workflow/log/`
4. User confirms

Then: use `superpowers:finishing-a-development-branch`.

---

## Cleanup

After merge:
```bash
git worktree remove ../<slug>
```
