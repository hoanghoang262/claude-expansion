---
description: Show current workflow state
---

Read `.workflow/STATE.md` and display:

```
[workflow:status]
Phase: <phase>
Spec: <active-spec>
Track: <track>
Next: <next-action>
Blocked: <blocked-by>
Updated: <last-updated>
```

If no STATE.md found: "No active workflow. Start with /spec <topic> or describe what you want to build."
