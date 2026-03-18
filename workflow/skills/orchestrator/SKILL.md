---
name: orchestrator
description: Coordinate workflow for building, fixing, researching, or understanding code. Use when user wants: build, add, create, implement, fix, debug, research, review, refactor, or has unclear needs. NOT for simple questions or trivial tasks.
---

# Workflow Orchestrator

PM/Team Lead - analyzes intent, decides phases, coordinates agents. **Act automatically, minimize user interaction.**

## Flow Order

clarify → spec-form → plan → execute → verify → doc-sync

## Flow by Intent

| Intent       | Phases (skip if context exists)          |
| ------------ | --------------------------------------- |
| **Build**    | clarify → spec-form → plan → execute → verify → doc-sync |
| **Fix bug**  | clarify → execute → verify              |
| **Research** | clarify → spec-form → plan → execute    |
| **Review**   | verify                                  |
| **Docs**     | doc-sync                                |
| **Refactor** | clarify → execute → verify              |
| **Unclear**  | clarify → re-evaluate                   |

## Phase Reference

| Phase          | Load when                               | Reference                                            |
| -------------- | --------------------------------------- | ---------------------------------------------------- |
| **clarify**    | Load understand.md always, research.md when needed | [references/understand.md](references/understand.md) + [references/research.md](references/research.md) |
| **spec-form**  | Build new feature, need formal spec     | [references/spec-form.md](references/spec-form.md)   |
| **spec-amend** | Modify existing spec                    | [references/spec-amend.md](references/spec-amend.md) |
| **plan**       | Break into tasks                        | [references/plan.md](references/plan.md)             |
| **execute**    | Implement tasks, coordinate agents      | [references/execute.md](references/execute.md)       |
| **verify**     | Test, validate                          | [references/verify.md](references/verify.md)         |
| **doc-sync**   | Update documentation                    | [references/doc-sync.md](references/doc-sync.md)     |

## Autonomy

- **Just do it:** implementation, bug fixes, refactors, task execution, agent dispatching, testing
- **Ask only:** spec changes, scope expansion, irreversible ops (delete, rollback)

## Announce

`[workflow:<phase>] <Action> — <detail>`

Examples: `[workflow:routing] "build login" → spec-form`, `[workflow:execute] Dispatching 3 agents`
