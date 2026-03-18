# Routing Decision

## Prompt
"check xem code có vấn đề gì không"

## Analysis

### Intent Detection (Step 1)
- Keyword "check" → matches "review", "kiểm tra" in intent router table
- Router mapping: `"review", "kiểm tra" | references/verify.md`

### Routing Decision

**Phase: `verify`**

### Reason
The skill's intent router explicitly maps:
- "review", "kiểm tra" → `references/verify.md`

This aligns with the expected phase in the eval definition (verify).

---

## Code Analysis - Issues Found

### Issue 1: Path Reference Inconsistency
**Location:** SKILL.md lines 20, 47
- Line 20: `"brainstorm", "suy nghĩ", "ý tưởng" | skills/brainstorming/SKILL.md`
- Line 47: `"Brainstorm | skills/brainstorming/SKILL.md"`

**Problem:** The skill references `skills/brainstorming/SKILL.md`, but in the workflow plugin structure, there's no `skills/` subfolder - only `references/`. The brainstorming skill exists in the parent `resource/superpowers/skills/` directory, not within the workflow plugin.

### Issue 2: Verification Phase Assumption
**Location:** `references/verify.md` lines 6-9
```markdown
## When to Enter
- All tasks implemented
- User says: "review", "verify", "check", "test"
- Before merge
```

**Problem:** The verify phase assumes there are already implemented tasks to verify against a spec. However, "check xem code có vấn đề gì không" could be:
1. A pre-implementation code review (should route to understand)
2. A post-implementation verification (correctly routes to verify)

The skill doesn't distinguish these cases in Step 1.

### Issue 3: Missing Phase for Code Analysis
**Problem:** There's no dedicated "code review" or "analysis" phase. The skill forces:
- "check" → verify (assumes implementation exists)
- But user might want static analysis without spec

This creates a mismatch between user intent and workflow phase.
