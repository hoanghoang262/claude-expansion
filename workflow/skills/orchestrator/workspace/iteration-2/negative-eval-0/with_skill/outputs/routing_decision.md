# Routing Decision

**Prompt**: "Xem version hiện tại của app là gì?"

**Phase**: none

**Why**:
- This is a simple information lookup request
- Single-action task - just asking for version information
- Does NOT require multiple steps, decision-making, or coordinating subagents
- Per SKILL.md: "NOT for: simple one-off lookups"
- Per negative.json eval id=1: "Simple lookup - should NOT trigger workflow"

**Conclusion**: Do NOT use the orchestrator skill. Handle directly as a simple lookup.
