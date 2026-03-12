---
name: review/final
description: Final integration review after all tasks complete. Launches quality-reviewer agent in full integration scope.
---

# Final Integration Review

**Light:** skip. **Standard:** skip if low-risk + solid coverage. **Heavy:** required.

```
[workflow:review] ⏳ Final integration review
```

Launch `workflow:agents/quality-reviewer` with:
- `COMMITS`: all commits since task-breakdown
- `CONVENTIONS`: from PROJECT.md
- `SCOPE`: final integration

```
[workflow:review] ✅ Final review complete
```

Update STATE.md:
```
phase: review
next-action: Run doc-sync then finishing-a-development-branch
```

If issues found → surface to user with description + recommendation before proceeding.
