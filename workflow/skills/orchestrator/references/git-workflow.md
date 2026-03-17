# Git Workflow

Every feature or fix lives on its own branch. Never implement on main.

---

## Starting a feature

When spec approved → create branch + worktree inside repo:

```bash
git worktree add .worktrees/<slug> -b feat/<slug>
```

```
[workflow:git] Branch feat/<slug> created — working in .worktrees/<slug>/
```

`.worktrees/` must be in `.gitignore`. All agents work inside the worktree. Every commit lands on `feat/<slug>`.

Branch naming:
- New feature → `feat/<slug>`
- Bug fix → `fix/<slug>`
- Experiment → `exp/<slug>`

---

## Parallel tasks

Independent task groups → separate branch + worktree per group:

```bash
git worktree add .worktrees/<slug>-g1 -b feat/<slug>-g1
git worktree add .worktrees/<slug>-g2 -b feat/<slug>-g2
```

Git does not allow two worktrees on the same branch simultaneously.
Each group branch is a short-lived child of `feat/<slug>`.

After group completes → merge into `feat/<slug>` → remove worktree + branch:

```bash
git -C .worktrees/<slug> merge feat/<slug>-g1
git worktree remove .worktrees/<slug>-g1
git branch -d feat/<slug>-g1
```

---

## Merging to main

After final review + doc sync:

```
[workflow:git] Ready to merge — feat/<slug> → main
```

Checklist before merging:
1. Full test suite passes on `<branch>`
2. `git diff main...<branch>` — review what's going in
3. No open issues in `.workflow/log/`
4. User confirms

Then merge:
```bash
git checkout main
git merge --no-ff <branch> -m "<type>(<slug>): <summary>"
```

---

## Cleanup

After merge:
```bash
git worktree remove .worktrees/<slug>
git branch -d <branch>
```
