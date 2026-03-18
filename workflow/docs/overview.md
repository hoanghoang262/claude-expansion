# Workflow Plugin — Overview

A structured AI-driven development framework. Intent-driven workflow orchestrator.

## Core Thesis

> AI owns execution. User owns intent and strategic direction.
> Plan before acting. Docs is xương sống — xuyên suốt, không phải phase cuối.

## Intent Router

| User says | Jump to |
|-----------|---------|
| "build", "implement", "thêm" | spec-form.md |
| "fix", "bug", "sửa" | understand.md |
| "research", "tìm hiểu" | research.md |
| "review", "check" | verify.md |
| "docs", "tài liệu" | doc-sync.md |

## Phases

| Phase | Reference | Purpose |
|-------|-----------|---------|
| Understand | `references/understand.md` | Analyze context |
| Spec | `references/spec-form.md` | Create spec |
| Plan | `references/plan.md` | Break into tasks |
| Execute | `references/execute.md` | Implement |
| Verify | `references/verify.md` | Test & review |
| Doc Sync | `references/doc-sync.md` | Update docs |

## Agents

| Agent | Role | Tools |
|-------|------|-------|
| implementer | Write code | Read, Grep, Glob, Write, Edit, Bash |
| spec-reviewer | Verify spec compliance | Read, Grep, Glob, Bash |
| quality-reviewer | Code quality | Read, Grep, Glob, Bash |
| researcher | Investigation | Read, Grep, Glob, WebSearch, WebFetch, Bash |
| doc-syncer | Update docs | Read, Grep, Glob, Write, Edit, Bash |

## Task Scope

| Scope | Effort | Mode |
|-------|--------|------|
| Small | <30 min | Do yourself or single subagent |
| Medium | 30-120 min | 1-2 subagents |
| Large | >120 min | Agent team |

## Project State

```
docs/
├── PROJECT.md                    # constraints, tech stack
├── specs/<slug>/spec.md          # feature spec
└── features/                     # feature docs

.workflow/
├── understand/                   # analysis logs
└── specs/<slug>/log/            # execution logs
```

## Docs is Xương Sống

Every phase MUST update relevant docs — not just at the end.

| Phase | Docs to update |
|-------|----------------|
| Understand | PROJECT.md (if needed) |
| Spec | docs/specs/<slug>/spec.md |
| Plan | docs/specs/<slug>/plan.md |
| Execute | Spec + code comments |
| Verify | docs/specs/<slug>/spec.md (SC results) |
| Research | docs/architecture/ hoặc docs/features/ |
| Doc Sync | All relevant docs |
