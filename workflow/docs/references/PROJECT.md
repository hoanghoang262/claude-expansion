# PROJECT.md Reference

## Purpose

Project vision, goals, why. **Lifespan: PERMANENT — NEVER DELETE.**

## Lifecycle

```
Created by:
  └── initialize (once)

Updated by:
  └── doc-sync (when product meaningfully changes)

Never deleted.
```

## Structure

```markdown
# [Project Name]

## What This Is

[2-3 sentences: What, who for]

## Why

[Problem it solves]

## Core Value

[ONE sentence: Most important thing]

## Goals

- [Goal 1]
- [Goal 2]

## Constraints

- [Constraints]

## Key Decisions

| Decision | Rationale | Outcome | Phase |
|---------|-----------|---------|-------|
| PostgreSQL | Scalability | Better query perf | 1 |

## Requirements Status

| Requirement | Status | Phase |
|-------------|--------|-------|
| | | |
```

## Related Docs

| Doc | Purpose | Lifespan |
|-----|---------|----------|
| CONVENTIONS.md | Coding style, naming | PERMANENT |
| STRUCTURE.md | Folder structure | PERMANENT |
| STACK.md | Tech stack, libraries | PERMANENT |
| TESTING.md | Testing approach | PERMANENT |
| CONCERNS.md | Technical debt, risks | PERMANENT |
| ROADMAP.md | Phases & milestones | VERSION |
| STATE.md | Session state | SESSION |

## Update Rules

Update when:
- Product meaningfully changes
- New major decisions made
- Core value evolves

**Write directly to file — don't store decisions in memory.**
