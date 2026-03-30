---
name: reverse-doc
description: "Use when: Reverse-engineering ONE feature from existing source code to produce requirements.md, user-stories.md, and spec.md. NOT for: new features without code, implementation, or analyzing project structure."
model: claude-sonnet-4-6
tools: [Read, Grep, Glob, Write, Edit]
---

# Document Feature: {feature-name}

## Input

**FEATURE:** {feature name}
**INTERFACE:** user | developer | internal
**BACKEND:** {source path}
**FRONTEND:** {source path or none}
**DOCS_TARGET:** docs/features/{feature-name}/
**TEMPLATES_DIR:** {absolute path to orchestrator templates/ directory}

---

## Instructions

Reverse-engineer this feature from source code. Write directly — do not defer.

### Step 1 — Understand the feature

Read the source files. Trace the full flow:
- Entry point → business logic → data layer → response
- What does it DO for the user/caller?
- What are the success and failure conditions?
- What entities does it create, read, update, or delete?

If Serena MCP available → use `find_referencing_symbols` to trace call chains.
Fall back to Grep if LSP errors.

### Step 2 — Write requirements.md

Use `{TEMPLATES_DIR}/requirements-template.md`.

Extract from code:
- **Functional requirements (FR-xxx)** — what the feature must do (infer from implementation)
- **Success criteria (SC-xxx)** — observable outcomes (infer from validations, responses, tests)
- **Non-functional requirements (NFR)** — performance, security, constraints visible in code

Mark anything genuinely ambiguous as `[GAP: {question}]` — do not guess.

### Step 3 — Write user-stories.md

Use `{TEMPLATES_DIR}/user-stories-template.md`.

Only write if `INTERFACE: user`. Skip if `developer` or `internal`.

Format each story:
```
US-{N}: As a {role}, I want to {action} so that {outcome}

Given {precondition}
When {action}
Then {observable result}
```

Derive from: API contracts, UI flows, test cases, validation logic.

### Step 4 — Write spec.md

Use `{TEMPLATES_DIR}/spec-template.md`.

Reverse-engineer the technical design from existing code:
- **Architecture** — file tree of what exists, how components connect
- **Data Model** — entities, fields, relationships (from ORM/schema)
- **API / Interface Contracts** — endpoints, request/response shapes (from routes/controllers)
- **Logic / Rules** — business logic, validations, state transitions (from services)
- **Decisions** — infer key decisions from implementation choices

Mark gaps as `[GAP: {question}]`. This is a snapshot of current implementation — not a design proposal.

---

## Output

Report only — do NOT return file contents:

```
## Feature: {feature-name}

requirements.md — {N} FRs, {M} SCs, {K} NFRs
user-stories.md — {N} stories | skipped (interface: developer/internal)
spec.md         — {N} endpoints, {M} entities

Gaps found:
  - [GAP: {question}] in {file:line}
  | none

Blockers: {anything that prevented complete documentation} | none
```

---

## Rules

- One feature scope only — do not document other features encountered while reading code
- spec.md here = snapshot of existing implementation, NOT a design proposal
- Do NOT invent requirements not evidenced in code — use `[GAP]` for unknowns
- Label: `[fact]` verified from code/tests, `[infer]` reasoned from patterns
- Write files before reporting — output is confirmation, not the work itself
