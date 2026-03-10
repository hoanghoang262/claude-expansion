# Orchestration Model

The system is structured around a single orchestrator and multiple specialized sub-agents.

---

## The Orchestrator

In the current environment, the Claude Code main agent acts as the orchestrator.

**The orchestrator is responsible for:**

- Holding the full picture of the current request and project state
- Routing to the right skill based on intent and track (light/standard/heavy)
- Driving spec formation — including inline clarification of gaps
- Decomposing approved spec into tasks
- Assigning tasks to sub-agents
- Tracking dependencies and task state
- Triggering review at each level
- Ensuring doc sync happens as part of delivery
- Escalating to the user when strategic decisions are needed

**The orchestrator does not:**
- Execute implementation tasks directly (it delegates)
- Hold opinions about implementation details (it respects spec)
- Silently change approved spec during execution

The orchestrator's job is coordination and direction — not execution.

---

## Sub-Agents

Sub-agents are specialized execution units. They receive a task, execute it, and return a result.

**Sub-agents are responsible for:**
- Implementing the assigned task according to the approved spec
- Running tests relevant to their task
- Performing task-level self-review before returning
- Updating docs impacted by their task
- Reporting completion status and any issues discovered

**Sub-agents do not:**
- Modify approved spec
- Make strategic decisions
- Assign work to other agents without orchestrator coordination
- Change scope beyond what their task defines

Sub-agents can be specialized by role: implementation agents, review agents, doc-sync agents. The orchestrator assigns work based on the agent's capability and the nature of the task.

---

## Flow

```
User → Orchestrator (reads STATE.md + orchestrator skill at session start)
         |
         ├─ Intent vague? → brainstorming skill
         |
         ├─ spec-formation skill
         |     ├─ Draft spec immediately
         |     ├─ Mark gaps inline → resolve with user (max 5 questions)
         |     └─ User approves → approved.md locked
         |
         ├─ task-breakdown skill → tasks.md (with parallel groups)
         |
         ├─ execute skill → assigns to Sub-Agents
         |     Sub-Agent: implement → test → self-review → commit
         |       ├─ Stage 1: spec compliance review
         |       └─ Stage 2: code quality review
         |
         ├─ doc-sync skill → update only affected docs
         └─ finishing-a-development-branch (superpowers)
```

**Track determines ceremony:**
- `light` — spec-formation fast, self-review only, minimal doc-sync
- `standard` — full spec, two-stage review, relevant doc updates
- `heavy` — full spec + NFRs, two-stage review, ADRs if needed

---

## Natural Language Is the Primary Interface

Users should not need to know which agent is running or which phase the system is in. The orchestrator infers the current phase from context, docs, and user input, then selects the appropriate flow automatically.

Commands exist for explicit overrides and deliberate control — not as the default way to drive the system.

When AI needs to surface a decision, it surfaces it directly in conversation. The user responds in natural language. The system updates its state accordingly.

---

## Context Handoff

When the orchestrator spawns a sub-agent, it provides:

1. The approved spec (or the relevant section)
2. The assigned task definition
3. Relevant project context (architecture, dependencies, conventions)
4. Any decisions already made that affect the task

Sub-agents do not read the full conversation history. They operate from the handoff context they receive. This means the orchestrator must be thorough in what it includes in handoffs.
