# Workflow Plugin — Overview

This plugin implements a **structured AI-driven development framework** for Claude Code.

It solves a specific problem: AI tends to act before it understands. The result is misaligned output, rework cycles, and eroded trust. This framework fixes that by enforcing intent clarity before execution, giving AI high autonomy within those bounds, and keeping spec, code, and docs in sync throughout.

## Core Thesis

> Empower AI to own execution, but require it to understand correctly first, respect strategic decision points, and keep spec, code, and docs reliably in sync.

## The Ten Beliefs

1. AI must not start with code — it must start with understanding.
2. Spec is the axis that connects intent to software.
3. Not every task needs the same level of rigor — the process must adapt.
4. After clarity is established, AI must be proactive in delivery.
5. Users own direction and strategy; AI owns execution.
6. Docs are the project's living memory — not an afterthought.
7. Not all generated content deserves to be permanent.
8. Tasks are units of delivery, not units of thought.
9. Review is multi-layered, not a single final gate.
10. A change is only done when code, spec, and docs are aligned.

## Document Map

| Document | What it covers |
|---|---|
| [philosophy.md](./philosophy.md) | Core beliefs expanded |
| [spec-lifecycle.md](./spec-lifecycle.md) | Three layers of spec and what each contains |
| [task-model.md](./task-model.md) | What a task is and how it's structured |
| [responsibility.md](./responsibility.md) | What the user owns vs what AI owns, decision boundaries |
| [orchestration.md](./orchestration.md) | Orchestrator + sub-agent model |
| [review-model.md](./review-model.md) | Three-layer review process |
| [docs-architecture.md](./docs-architecture.md) | Long-term docs vs temp workspace, promote rules |

## Implementation

**Skills** (`skills/`):
| Skill | Role |
|-------|------|
| `orchestrator` | Session-start router — reads STATE.md, routes to right skill |
| `brainstorming` | Facilitated direction alignment for vague intent |
| `spec-formation` | Draft + inline clarify + approve → locked `approved.md` |
| `task-breakdown` | Decompose approved spec into parallel-safe tasks |
| `execute` | Subagent per task, two-stage review, commit per task |
| `doc-sync` | Update only affected docs after delivery |
| `spec-amendment` | Guarded process for changing a locked spec |

**Hook:** `hooks/session_start.py` — injects orchestrator skill + project `STATE.md` at every session start.

**Script:** `scripts/init_workflow.py` — scaffolds `.workflow/` in user projects.

**Project state** (`.workflow/` in user's project):
```
.workflow/
├── STATE.md              # current phase, active spec, next action
├── PROJECT.md            # identity, constraints, key decisions
└── specs/<slug>/
    ├── idea.md           # brainstorm output (persistent)
    ├── working.md        # spec in progress (deleted after approval)
    ├── approved.md       # locked contract
    └── tasks.md          # execution breakdown
```

The default surface is **natural language** — the orchestrator infers phase and routes automatically.
