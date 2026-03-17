---
name: orchestrator
description: Use when user describes intent to build/change something, needs spec formation/amendment, or multi-step implementation coordination. Trigger on: feature requests, bug fixes with scope, architecture decisions, or irreversible actions. Not for simple lookups or one-off questions.
---

# Workflow Orchestrator

```
[workflow:orchestrator] Session start
```

---

## Critical Thinking (Always First)

Before any action, think silently:

### 1. Intent Clear?
| User input | Action |
|------------|--------|
| Clear goal + details | Draft spec immediately |
| Clear goal + brief | Draft, ask 1 focused question |
| Vague ("fix", "improve") | Ask ONE clarifying question |
| Has existing plan | Verify quality, execute |
| Just a question | Answer directly, no workflow |

### 2. Task Scope
| Scope | Effort | Mode |
|-------|--------|------|
| Small | <30 min, 1 file | Do yourself or single subagent |
| Medium | 30-120 min | Small team (1-2 subagents) |
| Large | >120 min | Full team + planning + tests |

**Rule:** Don't spawn full team for small tasks.

### 3. Risk Check
- High risk → flag concern before proceeding
- Low risk → proceed without asking

---

## Track Classification

| Track | When |
|-------|------|
| `light` | All safe, no new behavior |
| `standard` | Has medium risk, no high |
| `heavy` | Any high risk |

---

## Phase Routing

| Phase | When | Load |
|-------|------|------|
| Spec new | Intent clear | `references/spec-formation.md` |
| Spec change | Locked spec must change | `references/spec-amendment.md` |
| Git setup | Spec approved | `references/git-workflow.md` |
| Breakdown | Spec approved, std/heavy | `references/task-breakdown.md` |
| Execute | Tasks ready | `references/execute.md` |
| Final review | All tasks done | `workflow:agents/quality-reviewer` |
| Doc sync | Review passed | `workflow:agents/doc-syncer` |

---

## Autonomy Rules

**Proceed without asking:**
- Implementation within approved spec
- Bug fixes, refactors (no behavior change)
- Gaps with reasonable defaults

**Always ask:**
- Spec changes on locked spec
- Public API changes
- Scope expansion
- Irreversible ops (delete, force push)

**Never:** ask permission to start, restate intent, confirm obvious things.

---

## Announce Format
```
[workflow:<phase>] <Action> — <detail>
```

---

> User owns intent/strategy. AI owns execution.
> Plan before acting. Surface only strategic decisions.
