# Phase Routing Decision

## Input
- **Prompt**: "project này dùng gì?"
- **Scope**: medium

## Decision

| | |
|---|---|
| **Phase** | **Understand** |
| **Reference** | `references/understand.md` |
| **Confidence** | High |

## Reasoning

Theo Intent Router trong `SKILL.md` (dòng 24):

| User says | Jump to |
|-----------|---------|
| "cần biết", "giải thích" | `references/understand.md` |

Câu hỏi "project này dùng gì?" là câu hỏi thuộc loại "cần biết/giải thích" (understand) về codebase. User muốn hiểu project đang làm gì, dùng công nghệ gì.

## Alternative Considered

- **Research**: Không phù hợp vì đây không phải câu hỏi cần investigate sâu
- **Plan/Spec**: Không phù hợp vì không có requirement cụ thể cần implement
