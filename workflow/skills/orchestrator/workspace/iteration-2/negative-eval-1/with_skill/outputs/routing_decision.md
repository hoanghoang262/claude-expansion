# Routing Decision

**Prompt**: "đọc file này giúp tôi"

**Phase**: none

**Why**:
- This is a simple file read request
- Single-action task - just reading a file, no complex workflow needed
- Does NOT require multiple steps, decision-making, or coordinating subagents
- Per SKILL.md: "NOT for: simple one-off lookups like 'read file X'"
- Per negative.json eval id=2: "Simple read - should NOT trigger"

**Conclusion**: Do NOT use the orchestrator skill. Handle directly as a simple file read.
