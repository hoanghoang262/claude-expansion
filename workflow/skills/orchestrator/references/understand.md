# Understand Phase

Analyze context, understand codebase, constraints before taking action.

## Inputs Needed

1. **User intent** - What user describes
2. **Relevant codebase** - Files related to the issue
3. **Existing docs** - `docs/PROJECT.md`, relevant specs
4. **Context** - Previous conversation if any

## Process

### 1. Load Context

```
Read in order:
1. docs/PROJECT.md — constraints, tech stack, key decisions
2. docs/specs/<slug>/spec.md — if relevant spec exists
3. Relevant source files
```

### 2. Analyze Issue

For bug fixes:
- Reproduce the issue if possible
- Identify root cause
- Find affected files/components

For understanding:
- Summarize relevant codebase sections
- Identify key patterns

### 3. Document Findings

Create/Update `.workflow/understand/<slug>.md`:

```markdown
# Understanding: <title>

## Intent
<what user wants>

## Context Loaded
- docs/PROJECT.md
- <relevant files>

## Analysis
<findings>

## Next Action
- If bug found → execute.md (with fix plan)
- If unclear → ask user
- If need spec → spec-form.md
```

## Docs Responsibility

| Action | Docs to update |
|--------|----------------|
| New constraint found | `docs/PROJECT.md` |
| Architecture insight | `docs/architecture/overview.md` |
| Bug analysis | `.workflow/understand/<slug>.md` |

## Output

- Clear understanding of what needs to be done
- If bug: identified root cause + fix approach
- If research: summary of findings
- Next phase determined

## Jump to Next Phase

| Situation | Next Phase |
|-----------|-------------|
| Bug fix ready | `execute.md` |
| Need to create spec | `spec-form.md` |
| Need plan | `plan.md` |
| Need research | `research.md` |
| Unclear | Ask user |
