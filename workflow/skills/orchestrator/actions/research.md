# Action: Research

Triggered in UNDERSTAND phase when deeper information is needed to proceed.

---

## Steps

1. Define what exactly needs to be found — one clear question
2. Choose approach:
   - Codebase: spawn codebase-surveyor with specific query
   - External: spawn researcher agent with search query
   - Both: dispatch in parallel
3. Receive output → extract what's relevant to the current question
4. Update `docs/.pa/state.md` with finding or `[GAP]` if still unclear
5. Return to UNDERSTAND — check if clarity is sufficient to proceed
