# Routing Decision

## Input
"update docs cho feature login"

## Route to: Doc Sync Phase

### Reference: `references/doc-sync.md`

---

### Why Doc Sync Phase?

| Matching | Details |
|----------|---------|
| **Intent match** | Từ khóa "update docs" trong Intent Router → `references/doc-sync.md` |
| **Example match** | SKILL.md line 22: `"docs", "tài liệu" → references/doc-sync.md` với example "update docs" |
| **Phase purpose** | Doc Sync phase dành cho "Update documentation to reflect changes" - khớp hoàn toàn với task |

---

### Analysis

User wants to **update documentation for the login feature**. This is explicitly a documentation task, not:
- Building/implementing (→ execute)
- Creating new spec (→ spec-form)
- Fixing bugs (→ understand → execute)
- Planning tasks (→ plan)

The task is about **syncing docs** after/alongside feature development, which aligns with the Doc Sync phase.

---

### Doc Sync Approach

Based on `doc-sync.md` process:

1. **Identify Changed Areas**
   - Login feature → `docs/features/` (if exists)
   - May need to update: feature docs, API docs, or spec cross-references

2. **Update Docs**
   - Check if feature doc exists for login
   - Update relevant feature/architecture docs
   - Ensure cross-references are intact

3. **Final Sync**
   - Verify all docs reference each other correctly
   - Ready for merge

---

### Announce

```
[workflow:doc-sync] Updating: login feature docs
```
