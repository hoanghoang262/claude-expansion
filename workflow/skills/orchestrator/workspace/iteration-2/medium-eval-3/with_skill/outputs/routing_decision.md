# Routing Decision

**Task:** "project này dùng gì?"

## Phase: Understand

## Why?

| Intent Keywords | Matches |
|-----------------|---------|
| "cần biết", "giải thích" | ✅ "project này dùng gì?" |

According to SKILL.md - Intent Router:

> | User says | Jump to | Example |
> |-----------|---------|---------|
> | "cần biết", "giải thích" | `references/understand.md` | "project này dùng gì?" |

The question asks for understanding what the project is used for — this is a **knowledge/query intent**, not a build/fix/brainstorm intent.

## Reference

`references/understand.md` — Analyze context, understand codebase, constraints before taking action.

### Understand Phase Process:
1. Load context: Read `docs/PROJECT.md`, relevant source files
2. Analyze: Summarize relevant codebase sections, identify key patterns
3. Document findings: Create `.workflow/understand/<slug>.md`
4. Output: Clear understanding of the project

## Next Phase

After Understand phase completes, depending on user's need:
- If user wants to build something → `spec-form.md`
- If user wants to fix something → `execute.md`
- If unclear → ask user
