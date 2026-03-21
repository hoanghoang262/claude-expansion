# Orchestrator Guide

## Role

**Orchestrator = Router + Session Manager, NEVER a Worker.**

Orchestrator is the "coordinator" — communicates with you, reads docs, spawns subagents, updates memory.

## Three Memory Layers

```
PERMANENT  (never delete)
  PROJECT.md, features/*, standards/*, research/*, concerns/*

VERSION    (delete on Version Release)
  ROADMAP.md, worker-reports/*

SESSION    (reset after each phase)
  STATE.md
```

## Phase Chain

```
initialize → discuss-phase → plan-phase → execute-phase → verify-work → doc-sync
                                                                              ↓
  ← ← ← ← ← ← ← ← ← ← ← ← ← ← ← (loop) ← ← ← ← ← ← ← ← ← ← ← ← ← ← ←
```

## What Each Phase Does

| Phase | Role | Main Output |
|-------|------|------------|
| initialize | Set up project | PROJECT.md, ROADMAP.md, STATE.md |
| discuss-phase | Gather requirements | features/*/requirement.md, spec.md |
| plan-phase | Create plan | features/*/PLAN.md |
| execute-phase | Deploy | Code + worker-reports/ |
| verify-work | Test | features/*/UAT.md |
| doc-sync | Sync docs | All docs updated, STATE.md reset |

## When to ASK vs Do It Yourself

| Situation | Action |
|-----------|--------|
| New project, greenfield | ASK user |
| Project with existing code, brownfield | Explore agents |
| New feature, vague | ASK user |
| New feature, clear | Create spec directly |
| Don't know how to implement | Research agents |
| Small bug | Fix yourself |
| Complex bug | Research + plan |

## Memory Policy

```
⚠️  INTERRUPTION CAN HAPPEN AT ANY TIME

1. Important decision → WRITE to docs IMMEDIATELY
2. Phase done → doc-sync RIGHT AWAY → reset STATE.md
3. DO NOT rely on conversation history
4. docs/ is the sole source of truth
```

## Quick Reference

```
Want to know where you are?     → Read docs/STATE.md
Want to know what the project is? → Read docs/PROJECT.md
Want to know current phase?     → Read docs/ROADMAP.md
Want to know a specific feature? → Read docs/features/{id}/spec.md
```

See `references/` for detailed memory lifecycle and phase documentation.
