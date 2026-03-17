# Routing Decision

## Phase: **Understand**

## Why?

The user's task is: **"fix cái bug login không đăng nhập được"**

According to the orchestrator's Intent Router in `SKILL.md`:

| User says | Jump to |
|-----------|---------|
| "fix", "bug", "lỗi", "sửa" | `references/understand.md` |

This task contains:
- ✅ Keyword **"fix"**
- ✅ Keyword **"bug"**
- ✅ Context: login functionality

The Understand phase is appropriate because:
1. It's a **bug fix** task - requires analysis before implementation
2. The bug description is vague ("login không đăng nhập được" - can't log in) - needs clarification on:
   - What exactly happens when trying to login?
   - Any error messages?
   - Recent changes to the codebase?
   - Which authentication system/module is affected?

The Understand phase will analyze the context and gather necessary information before proceeding to fix the bug.
