# spec — Technical Design

## Agent

Use: `researcher` subagent (`workflow/agents/researcher.md`) if technology research is needed.

## Step 1: Load context (in parallel)

```
docs/features/{id}/requirement.md
docs/PROJECT.md
docs/standards/CONVENTIONS.md
docs/standards/STRUCTURE.md
```

## Step 2: Detect ambiguities

```
Ambiguous user stories?
Missing edge cases?
Observable acceptance criteria?
Technical constraints unclear?
```

→ Ambiguities found → ask user max 5 questions (all at once)
→ Clear → Step 3

## Step 3: Draft spec.md

Use `templates/spec-template.md` as skeleton.

Required sections:
```
- Overview (2-3 sentences)
- Data model (entities, fields, types)
- API endpoints (if applicable)
- Component design (if applicable)
- File changes (create/modify/delete)
- Verification criteria (observable behaviors)
```

## Step 4: Present to user

Display the full spec. Request `status: approved` in frontmatter to mark done.

If user requests changes → update spec.md → re-present.

## Step 5: Archive non-obvious decisions

```
Non-obvious tech decisions → docs/research/
```
