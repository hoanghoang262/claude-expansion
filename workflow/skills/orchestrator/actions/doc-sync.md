# doc-sync — Docs Sync & Reset

## Agent

Use: `doc-syncer` subagent (`workflow/agents/doc-syncer.md`).

## Step 1: Update permanent docs (in parallel)

```
docs/features/{id}/spec.md   — mark implemented items, log deviations
docs/ROADMAP.md             — mark action ✓ in milestone table, add completion date
docs/PROJECT.md             — add new decisions to Key Decisions table (if any)
```

## Step 2: Reset STATE.md

```
→ CLEAR ALL CONTENT
→ Write minimal form using templates/state-template.md
```

## Step 3: Present summary

```
- What completed
- Decisions recorded
- Open concerns (if any)
- Next action
```

## What KEEP vs DELETE

```
KEEP until Version Release:
  docs/features/{id}/           ← spec, requirement, UAT, plan
  docs/worker-reports/         ← All reports
  docs/ROADMAP.md            ← Until release
  docs/standards/*             ← Always

DELETE on Version Release ONLY:
  docs/worker-reports/
  docs/ROADMAP.md

NEVER DELETE:
  docs/features/
  docs/standards/
  docs/research/
  docs/concerns/
  docs/versions/
```

## Next

```
Next feature in ROADMAP?
  → YES → orient → discuss for next feature

No features in ROADMAP?
  → Ask user: "Plan a new feature?" or "Version Release?"

Version Release?
  → See: actions/version-release.md
```
