---
name: review
description: Review skills index. Callers load sub-files directly — no routing needed.
---

# Review

Callers load directly — do not route through this file.

| Sub-skill | Loaded by | When |
|-----------|-----------|------|
| `./per-task.md` | `workflow:execute` | After each task is implemented |
| `./final.md` | `workflow:orchestrator` | After all tasks complete |

Supporting prompts: `./spec-reviewer.md` · `./quality-reviewer.md`
