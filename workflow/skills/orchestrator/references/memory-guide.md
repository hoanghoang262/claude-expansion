# Memory Guide

How PA interacts with the memory system.

---

## Two-tier memory

```
STM  docs/.pa/state.md, docs/.pa/worker-reports/   reset each session
LTM  docs/project.md, docs/decisions/,             never deleted
     docs/.pa/learnings/, docs/.pa/concerns/,
     docs/[organic layer]/
```

---

## PA's direct responsibilities

PA reads and writes these directly — no dispatch needed:

| Operation | When |
|-----------|------|
| Read `docs/project.md` | Session start — orient to project |
| Read `docs/.pa/state.md` | Session start — orient to phase |
| Scan `docs/.pa/concerns/` | Session start — check open issues |
| Update `docs/.pa/state.md` | Mid-session — track progress, blockers |
| Log concern to `docs/.pa/concerns/` | Mid-session — Tier 2 issue discovered |

---

## memory-architect's responsibilities

Dispatch `memory-architect` agent for anything structural:

| Operation | When to dispatch |
|-----------|-----------------|
| `op=init` | No `docs/project.md` — create full BASE structure + `.claude/rules/` |
| `op=close` | End of operational session — sync docs/, write learnings/decisions/concerns, reset STM |

All file creation, template use, and `.claude/rules/memory-structure.md` generation goes through memory-architect.

---

## STM vs LTM

| Question | Answer |
|----------|--------|
| Will I need this next session? | YES → LTM (dispatch memory-architect at CLOSE) |
| Only relevant now? | YES → STM or skip |
| Important choice? | `decisions/{date}-{topic}.md` |
| Pattern discovered? | `.pa/learnings/{topic}.md` |
| Issue that may affect future? | `.pa/concerns/CONCERN-{topic}.md` |
| Agent output? | `.pa/worker-reports/{task}.md` |

---

## concern lifecycle

```
Discovered → Tier 1 attempt → still blocking?
  NO  → brief note in state.md → continue
  YES → write CONCERN-{topic}.md (Tier 2) → continue

Session start → PA scans concerns/ → checks Status field
Resolved → update Status: resolved, fill Resolution
Still blocking after Tier 2 → Tier 3 → AskUserQuestion
```

Status: `open` → `investigating` → `resolved`
