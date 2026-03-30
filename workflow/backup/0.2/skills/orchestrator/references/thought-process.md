# Thought Process

Sanity check before transitions. A habit to catch mistakes — not a mechanical checklist.

---

## Before any action

1. **Which pattern am I in?** UNDERSTAND actions don't spawn implementers. ACT actions don't ask requirement questions.
2. **Does docs/ exist?** No docs/ → clarify detects → init creates. Always.
3. **Is there an unresolved Tier 3 concern?** Yes → address before anything else.

## Before recognizing pattern (RESPOND / DIRECT / BUILD)

1. **What does the user actually want?** Not what they said — what they mean and what would help.
2. **What does "done" look like here?** Each pattern has a different success shape.
3. **Am I going shallow when I should go deep?** When in doubt → BUILD, not DIRECT.

## Before asking user

1. **Can I answer this myself?** Check docs/, rules/, existing knowledge. Don't waste user's time.
2. **Am I recommending an answer?** Every question must include a recommendation with reasoning. Never present a blank question.

## Before dispatching subagents

1. **Am I passing full context?** Task + relevant docs excerpt + conventions. Agent never reads plan/spec directly.
2. **What's the success condition?** Must be explicit and verifiable.
3. **What if it fails?** Have a recovery plan before dispatching.

## Before reporting to user

1. **Do I have evidence?** No output/test result = no claim of completion.
2. **What's next?** Always provide the recommended next step.

## After completing any work loop

1. **Anything worth saving to LTM?** Strategic insight, decision, pattern, user preference?
2. **Yes →** save to appropriate `docs/` location (1 Write call).
3. **No →** move on. Most RESPOND/DIRECT loops = nothing to save.
