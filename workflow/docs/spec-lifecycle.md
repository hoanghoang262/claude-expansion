# Spec Lifecycle

Spec is the central artifact of this framework. It is what converts ambiguous intent into a reliable contract for execution.

A spec is not a requirements document written once and forgotten. It evolves through three distinct layers, each serving a different purpose.

---

## Three Layers

### Layer 1 — Idea Summary

**Purpose:** Capture the origin of the request.

This is a short record of:
- The problem being solved
- The initial goal as stated by the user
- Relevant context or constraints available at the start

It preserves the intent as it was first expressed, before it gets refined or reframed through clarification.

**When it's created:** At the start of spec-formation, or at the end of brainstorming if that skill ran first. Captured as `idea.md`.

**Who owns it:** AI creates it by summarizing the user's stated intent or the brainstorm summary.

---

### Layer 2 — Working Spec

**Purpose:** The active thinking surface.

This is where AI and user work together to:
- Probe and clarify the requirement
- Identify ambiguities and resolve them
- Explore scope boundaries
- Surface trade-offs and open questions
- Draft design assumptions

This document is intentionally fluid. It changes as understanding deepens. It does not need to be perfect — it needs to be useful as a thinking tool.

**When it's created:** After the idea summary, during the clarification phase.

**Who owns it:** AI drives it; user corrects, approves, and adds constraints.

**What it is not:** It is not the final contract. Alternatives, open questions, and trade-off notes belong here, not in the approved spec.

---

### Layer 3 — Approved Spec

**Purpose:** The execution contract.

Once the working spec has been validated and the user has approved it (explicitly or through sufficient clarification), it becomes the approved spec. This is what AI delivers against.

**Mandatory contents:**

| Section | What it captures |
|---|---|
| Objective | What this change is for and why |
| Scope | Exactly what is in and what is out |
| Capabilities / Change Areas | The features, behaviors, or system areas being modified |
| Definition of Done | What must be true for this to be considered complete |
| Design Decisions | Key technical or behavioral choices that constrain implementation |
| Testing Expectations | What must be tested and at what level |
| Docs to Update | Which documentation must be updated as part of delivery |

**What does NOT belong in the approved spec:**
- Trade-off analysis (lives in working spec)
- Alternative options that were considered but rejected (lives in working spec or ADR)
- Open questions that have not been resolved (must be resolved before approval)
- Implementation detail beyond what is needed to constrain AI execution

---

## State Transitions

```
User intent
    |
    ├─ vague → brainstorming skill
    |               └─ [End brainstorm] summary → idea.md
    |
    └─ clear → spec-formation skill
                    ├─ creates idea.md (captures raw intent)
                    ├─ drafts working.md (marks gaps inline)
                    ├─ resolves gaps with user (max 5 questions)
                    ├─ user approves
                    ├─ working.md → approved.md (locked)
                    └─ working.md deleted
                                  |
                                  v
                    task-breakdown → tasks.md
                                  |
                                  v
                    execute → code + review + commit
                                  |
                                  v
                    doc-sync → docs updated
```

---

## Rules

- **No execution before approved spec.** A working spec is not sufficient for task breakdown or implementation.
- **Approved spec changes require user approval.** AI cannot unilaterally modify an approved spec during delivery. If new information requires a spec change, AI must surface it and get explicit approval.
- **Scope in approved spec is binding.** If implementation reveals a need to go beyond the approved scope, that is a new request — not a reason to silently expand.
- **Ambiguity in approved spec is a blocker.** If the approved spec is unclear on a point needed for implementation, AI must ask before proceeding, not guess.
