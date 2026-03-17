# Phase Routing Decision: "research về các auth options"

## Recommended Phase: Research

### Rationale:

The task **"research về các auth options"** (research about authentication options) clearly maps to the **Research** phase for the following reasons:

1. **Intent Match**: The task explicitly contains the keyword "research" which directly maps to `references/research.md` in the orchestrator's intent router table.

2. **Task Nature**: This is an investigation/analysis task, not:
   - A build/implementation request (would be `spec-form.md` or `execute.md`)
   - A bug fix (would be `understand.md`)
   - A brainstorming session (would be `brainstorming/SKILL.md`)
   - A plan/task breakdown (would be `plan.md`)

3. **No Premature Implementation**: The user is asking to explore options before deciding on a specific authentication approach. This is exactly what the Research phase is designed for — investigating options, analyzing tradeoffs, and providing recommendations.

4. **Decision Support**: Research phase will output findings with recommendations, which can then feed into:
   - A spec formation (if a choice is made)
   - A brainstorming session (if more exploration of ideas is needed)
   - Stay in research (if more investigation is needed)

### Next Steps in Research Phase:
- Define research questions (what auth methods to compare, what criteria)
- Investigate options (OAuth, password-based, magic links, biometric, etc.)
- Document findings with pros/cons for each option
- Provide recommendations based on context
- Identify next action (spec? implementation? more research?)
