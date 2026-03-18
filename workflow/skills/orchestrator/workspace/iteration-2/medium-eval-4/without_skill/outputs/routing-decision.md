# Phase Routing Decision

**User Request:** "tôi muốn thêm tính năng chat real-time"

---

## Analysis

### Intent Classification

| Keyword | Matches | Phase |
|---------|---------|-------|
| "thêm" (add) | ✅ Yes | spec-form |
| "build", "implement" | ✅ Yes | spec-form |
| "fix", "sửa lỗi" | ❌ No | - |
| "research", "tìm hiểu" | ❌ No | - |
| "plan", "chia task" | ❌ No | - |

### Context Assessment

1. **New Feature Request** — User wants to add a new feature ("chat real-time")
2. **No Existing Spec** — No spec mentioned or provided
3. **Intent Clear** — "thêm tính năng" = add feature
4. **Build Intent** — This is a "build" type request, not a bug fix or research

---

## Routing Decision

### → SPEC-FORM PHASE

**Rationale:**
- User wants to **add** a new feature (matches `spec-form.md`: "thêm", "tạo", "create")
- No existing specification for this feature exists
- Intent is clear: build real-time chat functionality
- This is a **feature development** task, not a bug fix

**Phase Flow:**
```
spec-form → plan → execute → verify
```

**Track Recommendation:** Standard (medium-risk feature - involves real-time communication, potential WebSocket/socket.io complexity, user management, message persistence)

---

## Required Inputs for Next Phase

To proceed with spec-form, user needs to provide:
1. **Context:** `docs/PROJECT.md` (tech stack, constraints)
2. **Clarification questions:**
   - Tech stack preference? (WebSocket, Socket.io, Firebase, etc.)
   - User authentication required?
   - One-on-one or group chat?
   - Message persistence needed?
   - Any existing backend services to integrate with?
