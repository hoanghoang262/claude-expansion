# Thought Process Protocol

Run this before every action transition — no tool calls until the `<thought_process>` block is fully written.

```xml
<blocking_thinking>
Before every action transition: output this structure. No tool calls, no actions, no code until this block appears.
</blocking_thinking>
```

```xml
<thought_process>
  <current_state>Read STATE.md. One sentence: current action + feature + wave.</current_state>
  <user_intent>One sentence: what does the user want right now?</user_intent>
  <artifact_check>What exists in docs/? What is missing?</artifact_check>
  <checkpoint_present>Yes/No. If yes: which checkpoint and what it requires.</checkpoint_present>
  <concerns>Any open concerns in docs/concerns/?</concerns>
  <risks>Missing docs? Corrupted state? Dependency on previous wave?</risks>
  <decision>"Running [action] because [reason]."</decision>
</thought_process>
```

**Rule:** If `artifact_check` and `decision` contradict each other → STOP. Re-read docs. Resolve before proceeding.
