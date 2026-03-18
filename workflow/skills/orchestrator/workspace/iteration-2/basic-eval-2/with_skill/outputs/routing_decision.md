# Routing Decision

**Task:** "build login feature"

**Phase:** `references/spec-form.md` (Spec Form)

**Reasoning:**

The orchestrator skill's **Intent Router** (Step 1) specifies:

| User says | Jump to |
|-----------|---------|
| "build", "implement", "thêm", "tạo" | `references/spec-form.md` |

The keyword **"build"** triggers routing to the **Spec Form** phase because:

1. **New feature work** - Building a login feature is a new feature implementation, not a fix or refactor
2. **Requires specification** - Before implementing, a spec should be created to define login requirements, authentication flow, security considerations, etc.
3. **Follows workflow** - The orchestrator workflow mandates: Context → Spec → Plan → Execute → Verify

**Announcement:**
```
[workflow:spec-form] Creating: login feature specification
```
