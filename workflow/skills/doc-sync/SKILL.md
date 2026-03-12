---
name: doc-sync
description: Update project docs to reflect what was built. Delegates to doc-syncer agent. Runs after execute, before branch completion.
---

# Doc Sync

```
[workflow:doc-sync] Starting — <slug>
```

Delegate to `workflow:agents/doc-syncer` with:
- `SPEC_PATH`: `.workflow/specs/<slug>/approved.md`
- `COMMITS`: git SHAs built since task-breakdown
- `TRACK`: light | standard | heavy (from STATE.md)

Agent handles: reading `related:` frontmatter, updating/creating docs, reporting.

On completion, update STATE.md:
```
phase: done
next-action: Run superpowers:finishing-a-development-branch
```
