# Routing Decision

**Prompt:** "viết document cho API mới"

## Analysis

| Keyword Detected | Match |
|-----------------|-------|
| "document", "tài liệu" | ✓ |

## Intent Classification

- **Primary Intent**: Documentation — user wants to write documentation for a new API
- **Scope**: Medium (new API documentation)

## Routing

**Phase:** `doc-sync`

## Reasoning

1. The user explicitly mentions "document" — this maps to doc-sync phase in the Intent Router (Step 1: "docs", "tài liệu" → `references/doc-sync.md`)

2. This is NOT:
   - `spec-form` — There's no mention of creating a new spec or building new features
   - `execute` — Not implementing code
   - `verify` — Not reviewing or testing existing code

3. The task involves writing documentation for a NEW API, which fits the Doc Sync phase:
   - Creating/updating feature documentation
   - API documentation
   - Ensuring docs reflect the new API

## Reference

- `references/doc-sync.md` — Update documentation to reflect new API
