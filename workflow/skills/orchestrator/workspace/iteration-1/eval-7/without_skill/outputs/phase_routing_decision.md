# Routing Decision

## Input
"spec đã approve rồi, implement đi"

## Phase Routing
**Route to: `Plan Phase`** (`references/plan.md`)

## Reasoning

| Keyword in Input | Matches Rule | Target |
|------------------|--------------|--------|
| "spec đã approve rồi" | ✓ | `references/plan.md` |

Theo orchestrator SKILL.md (dòng 17):
> | "spec rồi", "có spec", "làm tiếp" | `references/plan.md` | "spec đã approve rồi" |

**Why Plan, not Execute?**

1. **Spec đã approve** = đã qua giai đoạn spec-form và đã được review/approve
2. **Flow chuẩn**: Spec → Plan → Execute
3. User nói "implement đi" nhưng:
   - Orchestrator pattern: khi có spec rồi → vào Plan trước
   - Plan phase sẽ break spec thành tasks
   - Sau đó Plan sẽ route sang Execute

**Note**: Nếu user muốn execute ngay (light track), Plan phase có thể skip detailed planning và forward ngay sang Execute (theo `plan.md` line 67-68: "Light: Skip detailed plan, go to execute"). Nhưng initial route vẫn phải là Plan.
