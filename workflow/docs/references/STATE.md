# STATE.md Reference

## Purpose

Tracks current position of the session workflow. **Lifespan: SESSION (session-scoped) — RESET after each phase.**

## Lifecycle

```
Created by:
  ├── initialize (initial creation)
  └── doc-sync (after each phase completes → reset)

Updated by:
  └── Orchestrator during workflow

Deleted by:
  └── doc-sync (actually: reset content, not delete file)
```

## Structure

```markdown
# [Project Name] — State

## Project

Name: [project name]
Path: [path]
Lifespan: SESSION — RESET after each phase

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
| Use PostgreSQL | Scalability needed | 1 |
| JWT auth | Industry standard | 1 |

## Blockers

| Blocker | Phase | Status |
|---------|-------|--------|
| Need API key | 2 | pending |
```

## Field Meanings

| Field | What to Set |
|-------|-------------|
| Last session | Current timestamp |
| Stopped at | Last phase/plan worked on |
| Status | ready = ready to work, in-progress = working, waiting = blocked, complete = done |
| Resume file | Path to file being worked on (if in-progress) |
| Current Phase | Phase number currently on |
| Current Plan | Plan number currently on |

## Update Rules

1. **Read at session start** — Always know position
2. **Update at phase complete** — Mark phase done → doc-sync
3. **Update at plan complete** — Advance plan counter
4. **Update at blocker** — Add to blockers list
5. **Update at decision** — Add to decisions table

## ⚠️ Reset Policy

**After doc-sync (phase complete):**

```
CLEAR ALL content, KEEP HEADER:

# [Project Name] — State

## Project
Name: [name]
Path: [path]
Last Reset: [date]

## Session Continuity
Last session: [timestamp]
Status: ready
Current Phase: [next_phase]
```

**After Version Release:**
STATE.md is kept (not deleted) — it will self-reset when the next phase starts.
