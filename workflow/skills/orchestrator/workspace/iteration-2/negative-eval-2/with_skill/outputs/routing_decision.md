# Routing Decision

**Prompt**: "chmod 755 script.sh"

**Phase**: none

**Why**:
- This is a simple shell command execution
- Single-action task - just changing file permissions
- Does NOT require multiple steps, decision-making, or coordinating subagents
- Per SKILL.md: "NOT for: simple one-off lookups"
- Per negative.json eval id=3: "Simple command - should NOT trigger workflow"

**Conclusion**: Do NOT use the orchestrator skill. Handle directly as a simple command execution.
