# Concerns Workflow

## Overview

Technical debt, code smells, and risky trade-offs are logged to `docs/concerns/`, not fixed inline. This prevents subagents from destabilizing each other's worktrees and keeps human decision-makers in the loop.

## When to Log a Concern

**APPLIES TO:** Orchestrator AND all subagents (Executor, Researcher, Verifier, Explore).

When ANY agent discovers:
- Technical debt or code smell
- A risky trade-off with uncertain consequences
- A decision whose impact is hard to predict
- Architecture divergence from the approved spec

**Rule:** Log the concern, then continue the current task normally. Never stop work to fix something outside your task scope.

## How to Log

```
docs/concerns/{YYYYMMDD}-{short-title}.md
```

Use `templates/concern-template.md`.

Fields:
```
ID: CONCERN-{N}
Severity: High | Medium | Low
Status: open | resolved
Discovered by: {agent-name}
```

## When Orchestrator Checks Concerns

| Situation | Check? |
|---|---|
| After every doc-sync | ✅ |
| Before every action transition | ✅ |
| Before suggesting Version Release | ✅ |
| When user says "continue" | ✅ |
| When subagent reports a concern | ✅ |

## Resolution Flow

```
Concern logged (status: open)
    ↓
Orchestrator presents to user at next checkpoint
    ↓
User chooses: resolve | defer | reject
    ↓
resolve → spawn fix task → mark closed
defer → add to ROADMAP as a feature
reject → mark closed with note
```

## Version Release Gate

All open concerns MUST be reviewed before Version Release fires. If concerns exist, Orchestrator asks user before proceeding.
