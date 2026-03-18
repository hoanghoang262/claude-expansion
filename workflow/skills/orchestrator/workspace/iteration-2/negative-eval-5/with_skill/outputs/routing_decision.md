# Routing Decision

**Phase: None (Not a workflow task)**

## Analysis

| Factor | Value |
|--------|-------|
| Intent | Greeting / Casual conversation |
| Keywords detected | None - this is a friendly greeting |
| Existing spec | N/A |
| Scope | N/A - not a task |

## Why No Workflow Phase?

Following the orchestrator's routing logic:

1. **Step 1 - Intent Detection**: The phrase "Hello, how are you?" contains no intent keywords that map to any workflow phase:
   - No "build", "implement", "thêm", "tạo" → NOT spec-form
   - No "spec rồi", "có spec" → NOT plan
   - No "fix", "bug", "lỗi", "sửa" → NOT fix flow
   - No "brainstorm", "suy nghĩ" → NOT brainstorming
   - No "research", "tìm hiểu" → NOT research
   - No "review", "kiểm tra" → NOT verify
   - No "docs", "tài liệu" → NOT doc-sync
   - No "cần biết", "giải thích" → NOT understand
   - No "plan", "chia task" → NOT plan

2. **Not a workflow task**: This is a simple greeting/acknowledgment. The orchestrator skill states: "NOT for: simple one-off lookups like 'read file X' or 'what's in this folder'." A greeting falls into the same category - it's not a task requiring orchestration.

3. **Direct response appropriate**: The user is simply expressing a greeting. This should be handled as a normal conversational response, not routed through any workflow phase.

## Recommendation

Do NOT route to any workflow phase. This is a greeting that warrants a friendly, conversational response. The orchestrator is designed for tasks that require:
- Multiple steps
- Decision-making
- Coordinating subagents
- Codebase analysis, building, fixing, planning, etc.

"Hello, how are you?" is none of these - it's a social greeting that should be responded to directly without invoking any workflow phase.
