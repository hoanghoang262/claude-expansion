# Routing Decision

## Task
"sửa lỗi typo trong README"

## Phase to Route
**Understand Phase** (`references/understand.md`)

## Why

Based on the Intent Router in SKILL.md:

| User says | Jump to |
|-----------|---------|
| "fix", "bug", "lỗi", "sửa" | `references/understand.md` |

The task contains:
- **"sửa"** (fix) — keyword matching the fix/bug pattern
- **"lỗi"** (error/bug) — additional confirmation of bug-fix intent

Even though this is a simple typo fix, the orchestrator routes all "fix" tasks to the Understand phase first to analyze the context and understand what needs to be fixed before jumping to execution.
