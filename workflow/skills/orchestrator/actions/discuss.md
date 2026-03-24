# discuss

**Phase:** CLARIFY — Gathering requirements

## Purpose

Understand the user's requirement completely through wave-based questioning.

## Iron Law

`DO NOT PROPOSE SOLUTIONS BEFORE UNDERSTANDING THE PROBLEM.`

---

## Wave-Based Questioning

Ask questions in waves. Each wave builds on the previous.

**Wave 1 — Overview** (always ask):
- What is the goal? (one sentence: "I want to...")
- Who is the user/system that benefits?
- What does "done" look like? How will you know it works?

**Wave 2 — Constraints** (if Wave 1 answers are clear):
- Any integration with existing systems?
- Performance, security, or scale requirements?
- Tech stack constraints (must use X, cannot use Y)?

**Wave N — Edge cases** (only if needed):
- What happens when [boundary condition]?
- What should fail gracefully vs fail loudly?

### Rules

- Group related questions together. Never ask one at a time.
- Prioritize questions that affect later questions.
- Max 3 waves before moving to spec. If still unclear, mark [NEEDS CLARIFICATION] and move on.
- Update `docs/state.md` after each wave.

---

## Output

After waves complete:
1. Write `docs/features/{name}/spec.md` with requirements section only (user stories + FR-xxx)
2. Mark any unresolved items as `[NEEDS CLARIFICATION: specific question]`
3. Update `docs/state.md` → Phase: CLARIFY, Action: spec
4. Route to `spec`

Leave technical design sections empty — `spec` action fills those.
