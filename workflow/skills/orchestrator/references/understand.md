# Clarify — Understand

Phase 1: Analyze context, understand codebase, clarify requirements.

---

## 1. Load Context

1. `docs/PROJECT.md`
2. `docs/specs/<slug>/spec.md` (if exists)
3. Relevant source files

---

## 2. Philosophy

**Dream Extraction** — not requirement gathering.

- Think Partner, not Q&A
- Make vague → concrete
- Follow what excites/frustrates user most

---

## 3. Explore Themes

One theme at a time.

| Theme        | Explore                                      |
| ------------ | -------------------------------------------- |
| **Goal**     | Success criteria, key outcome               |
| **Problem**  | Pain point, current workaround               |
| **Users**    | Who, struggles, needs                        |
| **Constraints** | Tech, deadline, must-not-fail            |
| **Value**    | Why, what if we don't                        |

### Make Concrete

- "Fast" → "1s response or 1M records?"
- "Simple" → "Fewer clicks or minimal UI?"
- "Better" → "Faster, more features, fewer bugs?"

### Reverse Thinking

- Opposite solution?
- Simplest version that works?
- What are you NOT building?

---

## 4. Propose Options

Present 2-3 approaches:

```
Option A: <name>
- What: <brief>
- Pros/Cons: ...

→ Recommended: Option X because <reason>
```

**AskUserQuestion:** Offer 2-4 options. Always include "Other" → switch to text if chosen.

---

## 5. Core Principles

- **YAGNI** — Cut nice-to-have
- **KISS** — Simpler = less buggy
- **MVP** — V1 only
- **SoC** — One component, one thing

---

## 6. Anti-Patterns

- Ask mechanically → ignores answers
- Buzzwords → confuses not clarifies
- No synthesis → fire without responding
- Rush to code → picture unclear

---

## 7. Bug Fix

1. Reproduce
2. Find root cause
3. Identify affected files

---

## Document

Template: [templates/understand-findings.md](templates/understand-findings.md)
