# Routing Decision

## Task
"project này dùng gì?" (What is this project used for?)

## Phase: Understand (`references/understand.md`)

## Reasoning

The Intent Router in SKILL.md explicitly maps this query pattern:

| User says | Jump to | Example |
|-----------|---------|---------|
| "cần biết", "giải thích" | `references/understand.md` | "project này dùng gì?" |

The example given in the skill is **exactly** this task: "project này dùng gì?" is the example used to demonstrate routing to the Understand phase.

This query falls under the category of:
- **"cần biết"** (need to know) — user wants to understand what the project is for
- **"giải thích"** (explain) — user is asking for an explanation

The Understand phase is designed for:
- Analyzing context
- Understanding codebase
- Explaining what things are

This is NOT:
- A bug fix → would route to understand for different reasons
- A build/implement request → would route to spec-form
- A research request → would route to research

## Next Action

Route to `references/understand.md` to:
1. Load context from `docs/PROJECT.md`
2. Analyze the project structure
3. Provide a clear explanation of what the project is used for
