# Workflow Plugin — Overview

A structured AI-driven development framework. Solves AI's primary failure: acting before understanding. Enforces intent clarity before execution, gives AI high autonomy within those bounds, keeps spec/code/docs in sync.

## Core Thesis

> AI owns execution. User owns intent and strategic direction.
> Plan before acting. Surface only irreversible or strategic decisions.

## How It Works

Every session, the orchestrator skill is injected at start. It reads STATE.md (if present) and routes to the right skill based on current phase and intent.

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
              finishing-a-development-branch
```

## Skills

| Skill | Role |
|-------|------|
| `orchestrator` | Session router — injects at start, routes by intent + track |
| `brainstorming` | Optional — for strategic ambiguity only |
| `spec-formation` | Draft → clarify → lock. Two phases: clarify and lock |
| `task-breakdown` | Decompose approved spec into parallel-safe tasks |
| `execute` | Task Brief + subagent per task + two-stage review |
| `doc-sync` | Update only affected docs after delivery |
| `spec-amendment` | Guarded process for changing locked spec |

## Slash Commands

| Command | Action |
|---------|--------|
| `/brainstorm [topic]` | Force brainstorming |
| `/spec [topic]` | Force spec-formation |
| `/tasks` | Force task-breakdown |
| `/execute` | Force execute |
| `/status` | Show STATE.md |
| `/amend <change>` | Force spec-amendment |

Commands bypass orchestrator judgment. Use when you want to explicitly assign a phase.

## Smart Autonomy

AI outputs a **Task Brief** before every task:
```
[Task Brief]
Plan: <what + how>
Risk: NONE | LOW | HIGH
Action: proceeding | ⚠️ need input: <question>
```

HIGH risk = asks first. LOW/NONE = proceeds immediately. AI only interrupts for irreversible or strategic decisions.

## Project State

`.workflow/` in user's project:
```
.workflow/
├── STATE.md              # current phase, active spec, next action
├── PROJECT.md            # identity, constraints, key decisions
└── specs/<slug>/
    ├── idea.md           # brainstorm output (persistent)
    ├── working.md        # spec in progress (temp)
    ├── approved.md       # locked contract
    └── tasks.md          # execution breakdown
```

## Docs

| Doc | Content |
|-----|---------|
| `principles.md` | Core beliefs + responsibility split |
| `spec-lifecycle.md` | Three layers: idea → working → approved |
| `task-model.md` | What a task is and how it's structured |
| `orchestration.md` | Orchestrator + subagent model |
| `review-model.md` | Three-layer review process |
| `docs-architecture.md` | Long-term vs temp docs, promote rules |

## Hook

`hooks/session_start.py` — injects orchestrator skill + project STATE.md at every session start.

## Init Script

`scripts/init_workflow.py` — scaffolds `.workflow/` in user projects.
