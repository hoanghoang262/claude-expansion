# Concerns Workflow

Rules for logging concerns. Applies to **all agents** (Orchestrator + subagents).

## When to Log

When ANY agent discovers:
- Technical debt or code smell
- A risky trade-off with uncertain consequences
- Architecture divergence from the approved spec

**Rule:** Log the concern, then continue your current task. Never stop work to fix something outside your scope.

## How to Log

File: `docs/concerns/{YYYYMMDD}-{short-title}.md`
Template: `templates/concern-template.md`

```
ID: CONCERN-{N}
Severity: High | Medium | Low
Status: open | resolved | deferred | closed
Discovered by: {agent-name}
```

## Resolution

Orchestrator handles resolution — see `actions/review-concerns.md`.
Subagents only log. Never resolve concerns yourself.
