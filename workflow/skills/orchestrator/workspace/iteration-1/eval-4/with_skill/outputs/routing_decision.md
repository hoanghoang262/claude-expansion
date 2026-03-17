# Routing Decision

## Input
"review code này giúp tôi"

## Route to: Verify Phase

### Reference: `references/verify.md`

---

### Why Verify Phase?

| Matching | Details |
|----------|---------|
| **Intent match** | Từ khóa "review" trong Intent Router → `references/verify.md` |
| **Example match** | SKILL.md line 21: `"review", "kiểm tra" → references/verify.md` với example "review code này" |
| **Phase purpose** | Verify phase dành cho "Test, review, validate implementation" - khớp hoàn toàn với task |

---

### Verification Approach

Sử dụng **Light verification** (self-review only) vì:
- Không có spec/task log được cung cấp
- User yêu cầu review đơn thuần

**Self-review checklist:**
- [ ] Completeness: Every FR met?
- [ ] Quality: Follows patterns?
- [ ] Testing: Edge cases covered?
- [ ] Discipline: No extra features?

---

### Announce

```
[workflow:verify] Reviewing: code
```
