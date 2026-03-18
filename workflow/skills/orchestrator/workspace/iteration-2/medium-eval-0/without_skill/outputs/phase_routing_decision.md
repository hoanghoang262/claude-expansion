# Phase Routing Decision

## Input
- **Prompt:** "spec đã approve rồi, implement đi"
- **Scope:** medium

## Decision

**Phase:** `plan`

## Reasoning

| Signal | Analysis |
|--------|----------|
| "spec đã approve" | Spec đã hoàn tất, cần chuyển sang phase tiếp theo |
| "implement đi" | Yêu cầu thực hiện, nhưng cần plan trước |

Theo SKILL.md line 18:
> `"spec rồi", "có spec", "làm tiếp"` → `references/plan.md`

## Expected
- **Expected:** `plan`
- **Match:** ✅ Yes
