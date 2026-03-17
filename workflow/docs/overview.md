# Workflow Plugin — Overview

A structured AI-driven development framework. Solves AI's primary failure: acting before understanding. Enforces intent clarity before execution, gives AI high autonomy within those bounds, keeps spec/code/docs in sync.

## Core Thesis

> AI owns execution. User owns intent and strategic direction.
> Plan before acting. Surface only irreversible or strategic decisions.

## How It Works

Every session, the orchestrator skill is injected at start. It routes to the right skill based on current phase and intent.

```
User request
  ├─ Strategic ambiguity? → brainstorming → direction locked
  └─ Intent clear → spec-formation → approved spec
                         ↓
                   task-breakdown → tasks.md
                         ↓
                      execute → subagents implement + review
                         ↓
                     doc-sync → docs updated
                         ↓
                   merge gate → confirm before merging to main
```

## Skills

| Skill | Role |
|-------|------|
| `orchestrator` | Session router — injects at start, routes by intent + track |
| `brainstorming` | Optional — for strategic ambiguity only |
| `spec-formation` | Draft → clarify → lock. Two phases: clarify and lock |
| `task-breakdown` | Decompose approved spec into parallel-safe tasks |
| `execute` | Task Brief + subagent per task + two-stage review + merge gate |
| `doc-sync` | Update only affected docs after delivery |
| `spec-amendment` | Guarded process for changing locked spec |

## Slash Commands

| Command | Action |
|---------|--------|
| `/brainstorm [topic]` | Force brainstorming |
| `/spec [topic]` | Force spec-formation |
| `/tasks` | Force task-breakdown |
| `/execute` | Force execute |
| `/amend <change>` | Force spec-amendment |

Commands bypass orchestrator judgment. Use when you want to explicitly assign a phase.

## Task Brief

AI outputs a **Task Brief** before every task with explicit reasoning:
```
[Task Brief]
Track: STANDARD
Reasoning:
  - reversibility: ✅ code only, revert safe
  - blast_radius:  ⚠️ affects 2 modules
  - coordination:  ✅ none
  - testability:   ✅ unit test sufficient
Plan: <what + how>
Risk: NONE | LOW | HIGH
Action: proceeding | ⚠️ need input: <question>
```

HIGH risk = asks first. LOW/NONE = proceeds immediately.

## Project State

Project state is split across two locations:

```
docs/specs/<slug>/
└── spec.md                       # locked contract (long-term, source of truth)

.workflow/
├── PROJECT.md                    # identity, constraints, key decisions
├── brainstorm/
│   └── <N>-<topic>.md
└── specs/<slug>/                 # one folder per feature, named by slug
    ├── tasks.md                  # execution breakdown
    └── log/
        ├── summary.md            # ← read this first — task status + decisions
        ├── task-1.md             # implementer output
        ├── task-2.md
        ├── review-1.md           # reviewer output
        └── review-2.md
```

`summary.md` is the index per feature: AI reads it at session start to resume context without parsing all log files.

## Docs

| Doc | Content |
|-----|---------|
| `principles.md` | Core beliefs + responsibility split + AI operating principles |
| `spec-lifecycle.md` | Spec states: draft → approved |
| `task-model.md` | What a task is and how it's structured |
| `orchestration.md` | Orchestrator + subagent model |
| `review-model.md` | Two-stage review + SC Verification |
| `docs-architecture.md` | Long-term vs temp docs, promote rules |

## Hook

`hooks/session_start.py` — injects orchestrator skill at every session start.

## Init Script

`scripts/init_workflow.py` — scaffolds `.workflow/` in user projects.
