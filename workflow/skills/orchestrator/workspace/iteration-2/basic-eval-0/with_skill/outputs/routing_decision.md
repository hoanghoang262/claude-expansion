# Routing Decision

**Phase: Spec (spec-form.md)**

## Analysis

| Factor | Value |
|--------|-------|
| Intent | Build/Add new feature |
| Keywords detected | "Add" → maps to "build", "implement", "thêm", "tạo" |
| Existing spec | None mentioned |
| Scope | Medium-Large (OAuth2 involves security, multiple providers, frontend+backend) |

## Why Spec Phase?

Following the orchestrator's routing logic:

1. **Step 1 - Intent Detection**: The keyword "Add" maps to "build" which routes to `references/spec-form.md`

2. **Not Plan**: There's no existing spec mentioned ("spec rồi", "có spec"), so we cannot jump to plan

3. **Not Execute**: While OAuth2 is a known pattern, it involves:
   - Selecting OAuth providers (Google, GitHub, etc.)
   - Defining the frontend auth flow
   - Backend token handling
   - Security considerations
   - User experience design

   These require specification before implementation to ensure alignment and avoid rework.

4. **Not Understand**: The task is clear - add OAuth2 login. There's no ambiguity about what needs to be built.

## Recommendation

Route to `references/spec-form.md` to create an auth spec that defines:
- OAuth2 providers to support
- Frontend React integration approach
- Backend callback handling
- Token storage strategy
- User session management
- Security requirements
