---
name: review
description: Review implemented tasks — spec compliance first, then code quality. Also runs final integration review after all tasks complete.
---

# Review

Two modes. Load the relevant guide:

| Mode | When | Guide |
|------|------|-------|
| Per-task review | After each task is implemented | `./per-task.md` |
| Final integration review | After all tasks complete | `./final.md` |

**Order is strict:** spec compliance must pass before quality review runs.

```
[workflow:review] Starting — Task {N} | mode: per-task
```
or
```
[workflow:review] Starting — final integration review
```
