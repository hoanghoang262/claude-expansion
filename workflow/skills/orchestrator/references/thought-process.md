# Thought Process Protocol

Run **before every action transition**. No tool calls until this block is fully written.

```xml
<thought_process>
  <current_state>
    Read STATE.md. One sentence: current action + feature + wave.
  </current_state>

  <user_intent>
    One sentence: what does the user want right now?
  </user_intent>

  <artifact_check>
    What exists in docs/? What is missing? Any risks (corrupted state, missing deps)?
    Label each: [fact] | [infer] | [assume].
  </artifact_check>

  <checkpoint_present>
    Yes/No. If yes: which checkpoint and what it requires.
  </checkpoint_present>

  <concerns>
    Any open CONCERN-*.md that affects this transition?
  </concerns>

  <decision>
    "DELEGATE [next action] because [reason]."
    Must not contradict artifact_check. Contradiction found → STOP → re-read docs → resolve.
  </decision>
</thought_process>
```

## Rules

1. Skip this = invalid transition.
2. `artifact_check` contradicts `decision` → STOP → re-read docs → resolve.
3. Every claim in `artifact_check` must carry a label.
