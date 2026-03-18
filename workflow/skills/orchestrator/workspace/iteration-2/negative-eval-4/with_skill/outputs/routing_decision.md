# Routing Decision

**Input:** npm install

**Phase:** none

## Reasoning

This is a **negative eval case** - a simple command execution that should NOT trigger the workflow orchestrator.

- The orchestrator skill is designed for tasks requiring: building, changing, fixing, refactoring, brainstorming, researching, reviewing, planning, or understanding a codebase
- "npm install" is a simple, one-off command that doesn't require multi-step decision-making or subagent coordination
- Per the negative.json eval definition: "Simple command - should NOT trigger"

## Conclusion

**Route to:** No phase (none) - handle directly as a simple command execution.
