# [Project Name] — State

## Project

Name: [project name]
Path: [path]
**Lifespan: SESSION (session-scoped) — RESET after each phase**

## Session Continuity

Last session: [timestamp]
Stopped at: [phase], [plan]
Status: ready | in-progress | waiting
Resume file: [path if in-progress]

## Current Position

Current Phase: [N]
Current Plan: [N]
Phase Status: not-started | in-progress | complete
Plans in phase: [total]
Plans completed: [completed]

## Progress

```
Phase 1: [██████░░░░] 60%
Phase 2: [░░░░░░░░░░] 0%
```

## Decisions (accumulated)

| Decision | Rationale | Phase |
|----------|-----------|-------|
| | | |

## Blockers

| Blocker | Phase | Status |
|---------|-------|--------|
| | | pending |

---

## ⚠️ Memory Policy

**RESET AFTER EACH SUCCESSFUL PHASE (doc-sync)**

After doc-sync completes:
1. Keep header above
2. Clear old Decisions, Blockers, Progress
3. Reset to: Status = ready, Current Phase = [next]

**DO NOT rely on this file as memory.**

Source of truth: docs/features/*, docs/standards/*, docs/ROADMAP.md
