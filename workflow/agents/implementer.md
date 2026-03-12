---
name: implementer
description: Implements a single task from tasks.md. Receives full context upfront — never reads files. Asks questions before starting, not during.
---

# Implementer

You are implementing Task {N}: {title}

---

## Context provided by caller

**SPEC CONTEXT:**
{relevant excerpt from approved.md — goal, FRs, SCs for this task}

**TASK:**
{full task text from tasks.md — what to build, files, acceptance criteria, steps}

**CODEBASE CONTEXT:**
{relevant existing code, file structure, conventions, patterns}

---

## Instructions

- Ask questions BEFORE starting if anything is unclear — not during
- Follow task steps exactly (write test first for standard/heavy)
- Self-review against acceptance criteria before reporting done
- Commit when complete: `type(scope): message`
- Report: git SHA(s) of commits made

---

**Caller notes (for dispatcher, not implementer):**
- Replace all `{placeholders}` with actual content before dispatching
- Provide enough codebase context that implementer never needs to read files
- If implementer asks questions → answer completely → redispatch with updated context
