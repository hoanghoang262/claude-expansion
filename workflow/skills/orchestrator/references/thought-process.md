# Self-Question Protocol

Run before every action transition. Answer each question with evidence label.

## Before selecting an action

1. What is the current phase? (CLARIFY or IMPLEMENT) `[fact from state.md]`
2. What does the user actually need right now? `[fact/infer]`
3. What docs exist? What docs are missing? `[fact]`
4. Am I about to violate any hard constraint? `[self-check]`
5. Is there an open Tier 3 concern I haven't resolved? `[fact from concerns/]`

## Before dispatching subagents

1. Do I have the full task text ready to pass (not a file path)? `[check]`
2. Do I have the relevant spec excerpt (not the full spec)? `[check]`
3. What is the success condition for this subagent? `[must be explicit]`
4. What do I do if it fails? `[must have a plan]`

## Before reporting to user

1. Do I have test evidence for every claim? `[no evidence = no claim]`
2. Are there open concerns the user should know about? `[check concerns/]`
3. What is the recommended next step? `[always provide one]`
