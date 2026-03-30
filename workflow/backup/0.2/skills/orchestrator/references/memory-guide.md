# Memory Guide — Adaptive docs/ Structure

How to create and grow docs/. Load during init.

---

## Baseline (every project — always create)

```
docs/project.md        ← identity: user, goals, project type, success criteria
docs/state.md          ← STM: current phase/action (clear after work cycle)
docs/decisions/        ← committed choices (create when first decision made)
docs/concerns/         ← open issues (create when first concern arises)
docs/learnings/        ← insights (create when first learning captured)
.claude/rules/memory-structure.md  ← navigation guide (always in context)
```

Start minimal. Create directories only when there is actual content to put in them.

---

## Detail Layer — PM Decides

Beyond the baseline, docs/ must **mirror the project's natural structure** — not follow a template.

**The rule:** look at what the project *is*, then ask "what structure would let me navigate this efficiently in a future session?"

```
Self-ask before creating any folder/file:
  - What is the primary unit of this project? (feature / component / finding / concept / script)
  - If I return in 2 weeks, what would I need to find instantly?
  - Does this folder reflect the project, or does it reflect a generic template?
```

**Examples of how structure emerges from project type:**

| Project type | Natural unit | docs/ grows toward |
|---|---|---|
| Web / mobile app | Feature | `docs/features/{name}/` — requirements, current behavior |
| Plugin / tool | Component | `docs/components/{name}.md` — what it does, interfaces |
| Research | Finding | `docs/findings/`, `docs/sources/` |
| Learning | Concept | `docs/concepts/`, `docs/progress/` |
| Config / system | Current state | `docs/current-state.md`, `docs/changes/` |
| Script | Usage | `docs/usage.md`, `docs/scripts/` |

These are examples, not rules. The same project type at different scales or shapes may need a different structure.

**Key principle:** docs/ is a **living mirror** of the current project. When something changes, update the relevant doc. When a version is released, write a decision entry explaining what changed and why — the component doc itself just reflects the new current state.

---

## project.md — What to Capture

The PM's accumulated understanding of the user and project:

```
## Identity
- What is this project? What problem does it solve? For whom?
- Project type (inferred — can evolve)

## User Context
- Role, background, expertise level
- Working style and preferences (observed over time)
- What matters most: quality / speed / learning / shipping

## Goals
- Success in 1 month? 3 months?
- Current milestone

## Constraints
- Tech stack (if applicable)
- Non-negotiables, known limitations
```

Update project.md whenever PM gains new understanding — not just at init.

---

## STM vs LTM — Quick Reference

| Ask yourself | Answer → |
|---|---|
| "Will I need this in a future session?" | YES → LTM |
| "Is this only relevant to the current task?" | YES → STM or skip |
| "Did I make a decision with lasting implications?" | YES → decisions/ |
| "Did I discover a pattern worth remembering?" | YES → learnings/ |
| "Is there an issue that might affect future work?" | YES → concerns/ |
| "Is this just working data?" | YES → worker-reports/ or state.md |

---

## Consolidation Triggers

After any completed work loop — PM asks: "anything worth saving?"

- RESPOND/DIRECT (small) → usually nothing → move on (0 cost)
- Research session → findings summary → docs/findings/ or docs/learnings/
- BUILD verify done → full review: learnings + decisions + clear worker-reports
- Session end → reflect: what did this session add to the project's understanding?
