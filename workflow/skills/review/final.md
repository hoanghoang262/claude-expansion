---
name: review/final
description: Final integration review after all tasks complete. Checks end-to-end delivery against spec.
---

# Final Integration Review

**Light:** skip — per-task self-review sufficient.
**Standard:** skip if tasks were low-risk and test coverage solid.
**Heavy:** required.

```
[workflow:review] ⏳ Final integration review
```

Use prompt template: `./quality-reviewer.md` (final integration mode).

## On completion

```
[workflow:review] ✅ Final review complete — ready for doc-sync
```

Update STATE.md:
```
phase: review
next-action: Run doc-sync then finishing-a-development-branch
```

If issues found → surface to user with clear description + recommendation before proceeding.
