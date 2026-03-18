# Routing Decision

**Task:** "tôi muốn thêm tính năng chat real-time"

## Selected Phase

### `spec-form.md` (Spec Formation)

## Reasoning

| Step | Analysis |
|------|----------|
| **Intent Detection** | Từ khóa **"thêm"** (thêm tính năng) ánh xạ đến `spec-form.md` theo Intent Router |
| **Task Type** | Đây là yêu cầu xây dựng tính năng mới, không phải fix bug hay refactor |
| **Auto-suggest Brainstorm** | Không cần - user đã có ý định cụ thể ("chat real-time"), không mơ hồ hay "not sure" |
| **Scope** | Medium-Large (real-time chat là tính năng phức tạp cần WebSocket/SSE, database, UI) |

## Next Action

Jump to `references/spec-form.md` để tạo specification cho tính năng chat real-time.
