# Routing Decision

## Input
- **Prompt**: "tạo file test.txt"
- **Eval ID**: negative-eval-3 (from negative.json, id: 4)
- **Scope**: negative

## Decision

**Phase: none** — Should NOT trigger workflow orchestrator

## Rationale

This is a **simple one-off task** — a single file creation that doesn't require workflow orchestration.

According to the orchestrator skill:
- **NOT for**: simple one-off lookups like "read file X" or "what's in this folder"
- The prompt "tạo file test.txt" is a straightforward, single-step action
- No multi-step decision-making required
- No subagent coordination needed
- No context building or planning required

The task is correctly classified as a **negative case** — the orchestrator should **not** be invoked at all.
