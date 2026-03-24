# spec

**Phase:** CLARIFY — Technical design

## Purpose

Transform requirements into a complete, unambiguous technical spec. The spec is a living document — it starts with requirements and evolves to include full technical design.

## Iron Law

`DO NOT GUESS. MARK [NEEDS CLARIFICATION]. DEFINE ACCEPTANCE CRITERIA BEFORE TECHNICAL DESIGN.`

---

## The Living Document

`docs/features/{name}/spec.md` is the single source of truth for a feature. It contains:
1. **Requirements** (from discuss) — user stories, FR-xxx, success criteria
2. **Technical Design** (from this action) — data model, API, components, file changes
3. **Acceptance Criteria** — defined BEFORE implementation, used by verify

This file absorbs what was previously `requirement.md`. There is no separate requirement file.

---

## Steps

### Step 1 — Read current spec

- Does `docs/features/{name}/spec.md` exist?
  - Yes → read it, find all [NEEDS CLARIFICATION] markers
  - No → create from template `templates/spec-template.md`

### Step 2 — Resolve ambiguities

For each [NEEDS CLARIFICATION]:
- Can PM resolve from existing docs/rules? → resolve + mark [fact]
- Needs user input? → group all into one question batch → ask user
- Needs research? → spawn `researcher` agent → update spec with findings

### Step 3 — Write technical design sections

After all clarifications resolved:

```
## Technical Design

### Data Model
[entities, relationships, schema changes]

### API / Interface
[endpoints, function signatures, contracts]

### Components / Files
[what files change, what gets created, what gets deleted]

### Acceptance Criteria
[testable, measurable — these become verify checklist]
- AC-001: Given [state], when [action], then [outcome]
- AC-002: ...

### Decisions
[non-obvious tech choices with rationale]
[complex decisions → also write to docs/decisions/{date}-{title}.md]
```

### Step 4 — Compliance gate

Before marking spec as approved, check:
- [ ] No [NEEDS CLARIFICATION] markers remain
- [ ] All acceptance criteria are testable and measurable
- [ ] Tech choices follow `rules/constitution.md` principles
- [ ] Simplicity gate: no speculative features, no over-engineering

### Step 5 — Get user approval

Present spec summary to user:
```
Spec ready for review: docs/features/{name}/spec.md

Key decisions:
- [decision 1]
- [decision 2]

Acceptance criteria: [count] items

Reply "approved" to proceed to IMPLEMENT phase.
```

Do NOT proceed to plan until user explicitly approves.

---

## Project Type Heuristics

See `references/docs-heuristics.md` for spec patterns by project type (web app, CLI, library, data pipeline).
