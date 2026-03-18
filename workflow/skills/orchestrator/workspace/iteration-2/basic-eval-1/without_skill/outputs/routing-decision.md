# Phase Routing Decision

## Task: "fix cái bug login không đăng nhập được"

## Phase: **Understand** (`references/understand.md`)

---

## Reasoning

### Task Analysis

| Aspect | Value |
|--------|-------|
| Task Type | Bug Fix |
| Keywords detected | "fix", "bug", "login", "đăng nhập" |
| Input files | None provided |

### Why Understand Phase?

**1. Bug Fix Classification**
- Task chứa keyword **"fix"** và **"bug"** → theo Intent Router rule trong SKILL.md:
  - `"fix", "bug", "lỗi", "sửa" | references/understand.md`
- Đây là bug fix task, cần phân tích trước khi implement

**2. Insufficient Context**
- Không có input files được cung cấp
- Không có error messages, logs, hay stack traces
- Mô tả bug quá chung chung: "login không đăng nhập được" - cần xác rõ:
  - Chính xác điều gì xảy ra khi đăng nhập?
  - Có error message không? Nội dung gì?
  - Thay đổi gì gần đây trong codebase?
  - Hệ thống auth nào đang dùng?

**3. Workflow Principle**
- Theo CLAUDE.md: **"Context → implement → validate"**
- Với bug fix, phase đầu tiên là **Understand** để:
  - Reproduce được bug
  - Identify root cause
  - Xác định scope ảnh hưởng
  - Đề xuất solution trước khi fix

---

## Conclusion

**Route to: Understand Phase**

Phase này sẽ thu thập context cần thiết trước khi tiến hành sửa bug, đảm bảo:
- Hiểu rõ vấn đề thực sự là gì
- Có đủ thông tin để reproduce bug
- Tránh fix sai nguyên nhân gốc rễ
