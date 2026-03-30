# Decision: PA Core Architecture

Date: 2026-03-30

## Conversational vs Operational split

**Decision:** One question separates all work: "Does the output need to persist and be verifiable?"

- NO → handle directly in one response, no phases, no agents
- YES → run full phase cycle: UNDERSTAND → BUILD → VERIFY → CLOSE

**Why:** Claude Code is input/output only — no idle state. Forcing every request into a pipeline wastes cycles and breaks flow. Forcing complex work into a single response loses verifiability. The split maps cleanly to how humans actually think about work.

---

## Phase vs Action separation

**Decision:** Phases are mandatory cognitive states (UNDERSTAND → BUILD → VERIFY → CLOSE). Actions are optional procedures triggered by situation within a phase (init, research, spec, plan, debug).

**Why:** A flat list of steps collapses under complexity. Phases give PA a stable mental model regardless of project type. Actions provide specific procedures only when needed — not every task needs a spec, not every failure needs a debug protocol.

