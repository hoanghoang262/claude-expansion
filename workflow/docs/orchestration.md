# Orchestration Model

## Structure

Orchestrator (main Claude agent) + specialized subagents.

**Orchestrator:** holds full picture, routes skills, drives spec formation, assigns tasks to subagents, tracks state, escalates strategic decisions to user.

**Subagents:** receive a task + full context → implement → test → self-review → commit → return result. Never modify spec, never make strategic decisions.

## Flow

```
User → Orchestrator (reads orchestrator skill + STATE.md at session start)
  ├─ Strategic ambiguity? → brainstorming
  ├─ Intent clear → spec-formation
  ├─ Approved spec → task-breakdown → tasks.md
  ├─ Tasks ready → execute (subagents per task, two-stage review)
  ├─ All done → doc-sync
  └─ Ready to ship → finishing-a-development-branch
```

Track controls ceremony: `light` = fast + minimal review. `standard` = full spec + two-stage review. `heavy` = full spec + NFRs + ADRs + mandatory final review.

## Context Handoff

Orchestrator provides subagents: approved spec excerpt, task definition, project context, decisions already made.

Subagents do not read conversation history. Orchestrator must be thorough in handoffs.

## Natural Language First

Users speak naturally. Orchestrator infers phase from context and STATE.md. Slash commands exist for explicit overrides — not the default.
