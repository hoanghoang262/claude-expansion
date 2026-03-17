# Routing Decision

## Task
"fix cái bug login không đăng nhập được"

## Route To
**`references/understand.md`** — Understand Phase

## Why

| Factor | Analysis |
|--------|----------|
| **Keyword match** | User says "fix" (sửa) — triggers `references/understand.md` |
| **Example match** | SKILL.md lists "fix cái bug login" as example → exact match |
| **Intent type** | Bug fix — requires analysis before action |
| **Phase appropriateness** | Understand phase is designed for: "fix bug", "sửa lỗi" — analyze context, identify root cause |

## Reasoning

1. The Intent Router in SKILL.md explicitly maps "fix", "bug", "lỗi", "sửa" to `references/understand.md`
2. The provided example "fix cái bug login" matches the user's input pattern almost exactly
3. Bug fixes require the Understand phase to:
   - Analyze the codebase context
   - Reproduce the issue
   - Identify root cause
   - Determine fix approach before executing

## Next Step
After Understand phase completes, the workflow will either:
- Proceed to `execute.md` if root cause is identified
- Ask user for clarification if unclear
- Route to `research.md` if investigation needed
