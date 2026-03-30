# spec

**Phase:** UNDERSTAND — Write technical design. Requirements + user stories already exist from clarify.

<hard_constraint never_override>
- Read requirements.md + user-stories.md from clarify FIRST. Do NOT rewrite them.
- spec.md = technical design ONLY (HOW to build). WHAT is in requirements/user-stories.
- Mark ambiguity as `[NEEDS CLARIFICATION: question]` — never guess. Max 3 markers.
- If more than 3 markers → go back to clarify, not enough was understood.
- spec.md is a WORKING file — useful during implementation, may go stale after. Not permanent docs.
</hard_constraint>

---

## What already exists (from clarify)

```
docs/features/{name}/
├── requirements.md    ← WHAT (FR-xxx, SC-xxx, NFR) — from clarify
├── user-stories.md    ← WHO does WHAT (US-xxx, Given/When/Then) — from clarify
└── spec.md            ← HOW (this action writes it)
```

## Steps

### Step 1 — Read requirements + user stories

Read `requirements.md` and `user-stories.md`. These are the input. Do not modify them.

### Step 2 — Research (if needed)

For technical unknowns:
- Spawn `researcher` via Agent tool for: library choices, architecture patterns, performance approaches
- Resolve any `[NEEDS CLARIFICATION]` that PM can answer from context or research
- Remaining ones that need user → batch into one AskUserQuestion round

### Step 3 — Write spec.md (technical design)

Read `templates/spec-template.md` and fill it out for this feature.

Note: for cross-cutting concerns (DB schema, common middleware) also update `docs/foundations/*.md` — especially if this is the first feature being spec'd.

### Step 4 — Quality gate

- [ ] Zero `[NEEDS CLARIFICATION]` markers
- [ ] Architecture covers every FR-xxx from requirements
- [ ] Data model covers every entity from user stories
- [ ] Tech choices follow `.claude/rules/constitution.md`
- [ ] No speculative features (YAGNI)

### Step 5 — Present for approval

```
📋 Spec: docs/features/{name}/spec.md

🏗️ Architecture: {summary}
📊 Data model: {N} entities
🔌 API: {N} endpoints
💡 Key decisions:
  - {decision 1}
  - {decision 2}

Reply "approved" to begin implementation.
```

Do NOT proceed until user explicitly approves.
