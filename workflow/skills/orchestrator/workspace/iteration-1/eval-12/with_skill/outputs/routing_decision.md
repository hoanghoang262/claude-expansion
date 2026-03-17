# Routing Decision: Refactor toàn bộ payment system

## Task
"refactor toàn bộ payment system"

---

## Decision: Route to **Understand Phase**

### Reference: `references/understand.md`

### Reasoning

**1. Keyword Analysis**
- "refactor" is not explicitly in the router table, but semantically similar to "fix" - both involve analyzing and modifying existing code
- From SKILL.md line 18: `"fix", "bug", "lỗi", "sửa" → references/understand.md`
- Refactoring requires understanding the current structure before making changes

**2. Missing Context**
- No input files provided
- No specification exists for the payment system
- Unknown: codebase location, language, framework, current architecture

**3. Workflow Alignment**
- From CLAUDE.md: **Workflow:** Context → implement → validate
- Cannot implement (refactor) without first understanding the context
- Understand phase is the entry point for any work on existing systems

**4. Similar to Bug Fix**
- Refactoring is essentially restructuring existing code to improve quality
- Just like bug fixes, you need to analyze the current implementation first
- Understand phase will:
  - Identify all payment-related code/modules
  - Map dependencies and integrations
  - Analyze current architecture and issues
  - Document findings for next steps

---

## Next Phase After Understand

| Situation | Next Phase |
|-----------|------------|
| Issues identified needing new features | `spec-form.md` |
| Clear refactoring plan | `execute.md` |
| Need investigation | `research.md` |

---

## Summary

**Phase: Understand**

Refactoring an entire payment system requires deep understanding of the existing codebase first. The Understand phase will analyze the current payment system, identify components, dependencies, and issues before any refactoring work begins.
