# Routing Decision

**Task:** "fix cái bug login không đăng nhập được"

## Phase Selected: `understand` (references/understand.md)

## Reasoning

### Intent Classification
- **Keywords detected:** "fix", "bug"
- **Step 1 → Step 2:** Intent matches "fix" category

### Scope Assessment
| Factor | Assessment |
|--------|------------|
| Bug type | Login/authentication system |
| Root cause | Unknown - requires investigation |
| System complexity | Multiple components (frontend, backend, DB, auth) |
| Scope | Unknown - depends on codebase context |

### Decision: Understand Phase

**Why not execute directly?**
- Login bug is a **complex fix** (not a simple typo or single-file change)
- Root cause is unclear - could be API endpoint, auth logic, database, session handling, token validation
- Need to analyze codebase first to understand how login flow works

**Why Understand phase?**
- Follows the workflow: Context → implement → validate
- Allows investigation of login flow in the specific codebase
- Will identify root cause before attempting fix
- Prevents potential "shotgun debugging" approach

## Next Steps

After Understand phase, route to:
- `references/execute.md` - Once root cause is identified
- May need `references/verify.md` - After fix implementation
