# Phase Routing Decision: "build login feature"

## Recommended Phase: Requirements/Analysis Phase

### Rationale:

Given the task "build login feature" with **no additional input files or context** provided, the most appropriate phase to route to is **Requirements/Analysis** for the following reasons:

1. **Insufficient Context**: The task provides only the feature name ("login feature") but no details about:
   - The technology stack (web, mobile, API?)
   - Authentication method (password, OAuth, SSO?)
   - User requirements or acceptance criteria
   - Existing system architecture

2. **Risk Mitigation**: Building without requirements leads to:
   - Rework and wasted effort
   - Misaligned deliverables
   - Missing edge cases (password reset, session management, security)

3. **Follows Development Principles**: Per the CLAUDE.md workflow principle: "Context → implement → validate" — starting with context (requirements) before implementation prevents the "build first, ask questions later" anti-pattern.

4. **Standard Engineering Practice**: Even for a seemingly simple feature like login, proper analysis ensures:
   - Security considerations are addressed
   - User experience is consistent
   - Integration points are clear

### Next Steps in Requirements Phase:
- Gather technical context (stack, existing auth systems)
- Define functional requirements (registration, login, logout, password recovery)
- Identify non-functional requirements (security, performance, accessibility)
- Document acceptance criteria before implementation begins
