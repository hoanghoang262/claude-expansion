# Routing Decision: Brainstorm Auth

## Input
- **User request**: "brainstorm về cách làm auth"
- **Task context**: None (no input files)

## Analysis

### Intent Classification
| Indicator | Value |
|-----------|-------|
| Keywords | "brainstorm", "auth" |
| Intent type | Creative/exploratory |
| Orchestrator mapping | `brainstorm` → `skills/brainstorming/SKILL.md` |

### Brainstorming Skill Output
From the brainstorming skill (`resource/superpowers/skills/brainstorming/SKILL.md`):

> **The terminal state is invoking writing-plans.** Do NOT invoke frontend-design, mcp-builder, or any other implementation skill. The ONLY skill you invoke after brainstorming is writing-plans.

> **Implementation:**
> - Invoke the writing-plans skill to create a detailed implementation plan
> - Do NOT invoke any other skill. writing-plans is the next step.

## Decision

**Phase: `writing-plans`**

### Why?
1. **Hard-gate in brainstorming skill**: The skill explicitly mandates that after the design phase is complete and approved, `writing-plans` is the ONLY skill to invoke next
2. **Workflow logic**: Brainstorming → Design → Implementation Plan is a linear flow
3. **Orchestrator alignment**: The orchestrator also routes to phases, and after brainstorming, the logical next phase is planning the implementation
4. **Output alignment**: The task asks for the "final answer" - the brainstorming has already been done (see `without_skill/outputs/auth-brainstorm.md`), so the next actionable step is creating the implementation plan

This follows the documented workflow: brainstorm ideas → create design → write implementation plan → execute.
