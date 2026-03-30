# Memory Structure

This file is always in context (auto-loaded from `.claude/rules/`). It is the single source of truth for navigating project memory. Updated by `init` after discovery — always reflects current project structure.

## Lifecycle

### [PERMANENT] — never delete
- `docs/project.md` — project identity, architecture, tech stack, run commands
- `docs/features/{name}/` — per-feature docs (see Features section below)
- `docs/foundations/` — cross-cutting: DB schema, infra, NFRs
- `docs/decisions/` — architecture decision records (ADRs)
- `docs/concerns/` — open/resolved issues found during work

### [SESSION] — reset each phase
- `docs/state.md` — orchestrator tracking: phase, action, feature, wave

### [VERSION] — delete on Version Release Event
- `docs/worker-reports/` — implementer JSON reports per feature/task

## Project Structure

> Updated by `init` after discovery. This is what actually exists in this project.

### Features

| Feature | Interface | Docs |
|---------|-----------|------|
| {name} | user \| developer \| internal | requirements, user-stories, spec |

### Foundations

- `docs/foundations/database-schema.md`
- `docs/foundations/infrastructure.md`

## Rules
- `.claude/rules/constitution.md` — project principles
- `.claude/rules/memory-structure.md` — this file
- `.claude/rules/conventions.md` — code style, naming, patterns
- `.claude/rules/git-workflow.md` — branch strategy, commit format

---

> `docs/docs-map.md` — machine-readable YAML for tooling only. Read this file instead for navigation.
