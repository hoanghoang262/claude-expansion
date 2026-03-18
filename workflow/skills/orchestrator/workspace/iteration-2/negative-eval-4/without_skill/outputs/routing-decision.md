# Routing Decision for "npm install"

## Phase: none

## Rationale

1. **Simple single command**: "npm install" is a straightforward, single-step operation that doesn't require multi-step orchestration.

2. **Negative eval definition**: In `negative.json`, the eval for "npm install" (ID 5) specifies:
   - `expected: "none"`
   - `phase: "none"`
   - Note: "Simple command - should NOT trigger"

3. **Design principle**: Negative evals test cases where the orchestrator should NOT activate. Simple commands like:
   - File reads ("đọc file này giúp tôi")
   - Basic CLI operations ("chmod 755 script.sh", "ls -la")
   - Simple file creation ("tạo file test.txt")
   - Package manager commands ("npm install")

   ...should all be handled directly by the base Claude Code model without invoking any workflow phase.

## Conclusion

Route to: **none** (no phase, do not trigger orchestrator)
