# Review Model

Review is not a single gate at the end of delivery. It is structured across three levels, each checking for different things.

---

## Why Multi-Layer Review

A single final review catches integration issues but misses task-level defects early. Catching problems late is expensive — the work must be unwound across multiple tasks.

By reviewing at each level, issues are caught at the smallest possible scope, where they are cheapest to fix.

---

## Layer 1 — Task Review

**When:** After each task is completed by its assigned agent.

**Checks:**
- Does the implementation satisfy the task's verification criteria?
- Is the code consistent with the approved spec for this section?
- Are edge cases handled?
- Are tests sufficient for this task's scope?
- Are relevant docs updated?

**Owner:** The executing agent performs self-review. For higher-risk tasks, a separate review agent is assigned.

**Outcome:** Task is marked DONE or returned with specific issues to fix.

---

## Layer 2 — Group Review

**When:** After a cluster of tasks that together form a meaningful capability or workflow.

**Checks:**
- Do the individual tasks integrate correctly end-to-end?
- Is the behavior consistent across the full capability?
- Are there gaps between tasks that individually passed but collectively miss something?
- Does the combined result match the capability described in the approved spec?

**Owner:** Orchestrator, potentially with a dedicated review agent for large groups.

**Outcome:** Group is approved to move to integration, or specific tasks are flagged for rework.

---

## Layer 3 — Final Integration Review

**When:** After all tasks are complete and the full change is assembled.

**Checks:**
- Does the complete implementation satisfy the approved spec?
- Are there regression risks introduced by this change?
- Is the system internally consistent after this change?
- Are all required docs updated and accurate?
- Are there any issues that need to be escalated to the user before delivery?

**Owner:** Orchestrator, with a full integration review perspective.

**Outcome:** Change is approved for delivery, or specific issues are raised. Significant issues are escalated to the user with a clear explanation and recommendation.

---

## Review Is Not Perfection-Seeking

The purpose of review is to verify that the change does what it was supposed to do, within the agreed scope, without introducing new problems.

Review does not:
- Expand scope
- Introduce new requirements
- Refactor work that was not in scope
- Block delivery over style preferences

If review discovers something genuinely important that was not in the approved spec, it surfaces it as a separate finding — not as a blocker to the current delivery.

---

## Escalation

When a review finds something that:
- Changes the scope of the approved spec
- Reveals a design flaw in the foundation
- Introduces unexpected long-term risk
- Cannot be resolved without a user decision

...the orchestrator escalates to the user with:
1. A clear description of what was found
2. Why it matters
3. A specific recommendation or set of options
4. A request for a decision

Escalation is not failure — it is the review system working correctly.
