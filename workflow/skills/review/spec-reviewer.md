---
name: review/spec-reviewer
description: Prompt template for spec compliance reviewer subagent. Runs after implementer — checks what was built against what was specced.
---

# Spec Compliance Reviewer Prompt

```
Review Task {N} for spec compliance.

SPEC: {approved.md excerpt relevant to this task}
TASK definition: {full task text from tasks.md}
Commits to review: {git SHAs}

Check:
- Every acceptance criterion met?
- Anything built NOT in spec?
- Any spec requirement missing from implementation?

Output: ✅ Compliant | ❌ Issues: [list each issue clearly]
```

**Rules:**
- ✅ only when ALL criteria are met and nothing extra was built
- If ❌ → implementer fixes → this reviewer runs again
- Never skip re-review after fixes
- Never proceed to quality-reviewer while spec issues are open
