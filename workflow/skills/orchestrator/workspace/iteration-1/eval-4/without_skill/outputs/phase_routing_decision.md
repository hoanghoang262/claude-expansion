# Phase Routing Decision

**Input:** "review code này giúp tôi"

**Phase:** Verify

## Rationale

| Analysis | Value |
|----------|-------|
| Intent keyword | "review" |
| Matching rule | "review" → `references/verify.md` |
| Phase definition | Test, review, validate |
| Confidence | HIGH |

## Why Verify?

1. **Direct match:** Từ khóa "review" trong câu "review code này" trùng khớp với rule trong Intent Router:
   - `"review", "kiểm tra" | references/verify.md`

2. **Context appropriate:** Đây là yêu cầu review/kiểm tra code, không phải:
   - Build/implement → spec-form
   - Fix bug → understand
   - Research → research
   - Brainstorm → brainstorming

3. **Action:** Jump directly to `references/verify.md` to start verification workflow.
