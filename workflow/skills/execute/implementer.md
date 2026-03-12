---
name: execute/implementer
description: Prompt template for implementer subagent. Provide full context upfront — subagent never reads files itself.
---

# Implementer Subagent Prompt

```
You are implementing Task {N}: {title}

SPEC CONTEXT:
{relevant excerpt from approved.md}

TASK:
{full task text from tasks.md}

CODEBASE CONTEXT:
{relevant existing code, file structure, conventions}

Instructions:
- Follow task steps exactly
- Write tests first (standard/heavy track)
- Self-review before reporting done
- Commit when complete: `type(scope): message`
- Ask questions BEFORE starting, not during
```

**Before dispatching:**
- Replace all `{placeholders}` with actual content
- Include enough codebase context that subagent never needs to read files
- If subagent asks questions → answer completely → redispatch with updated context
