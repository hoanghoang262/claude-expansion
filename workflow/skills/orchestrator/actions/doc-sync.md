# doc-sync — Docs Sync & Reset

## Step 1: Update permanent docs (in parallel)

```
1a. docs/features/{id}/spec.md
    ├── Mark implemented items
    └── Log deviations

1b. docs/ROADMAP.md
    ├── Mark action ✓ in milestone table
    └── Add completion date

1c. docs/PROJECT.md (if new decisions made)
    └── Add to Key Decisions table
```

## Step 2: Check concerns

```
docs/concerns/ has open entries?
  → YES → present to user before proceeding (see references/concerns-workflow.md)
  → NO  → Step 3
```

## Step 3: Reset STATE.md

```
→ CLEAR ALL CONTENT
→ Write minimal form using templates/state-template.md
```

## Step 4: Present summary

```
- What completed
- Decisions recorded
- Open concerns (if any)
- Next action
```

## What KEEP vs DELETE

```
KEEP until Version Release:
  ├── docs/features/{id}/           ← spec, requirement, UAT, plan
  ├── docs/worker-reports/         ← All reports
  ├── docs/ROADMAP.md            ← Until release
  └── docs/standards/*             ← Always

DELETE on Version Release ONLY:
  ├── docs/worker-reports/
  └── docs/ROADMAP.md

NEVER DELETE:
  ├── docs/features/
  ├── docs/standards/
  ├── docs/research/
  ├── docs/concerns/
  └── docs/versions/
```

## Next

```
Next feature in ROADMAP?
  → YES → orient → then discuss for next feature

No features in ROADMAP?
  → Ask user: "Plan a new feature?" or "Version Release?"

Version Release:
  → Run scripts/create_version_release.py
  → orient
```
