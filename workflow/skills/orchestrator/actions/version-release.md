# version-release — Archive & Cleanup

## Trigger

All conditions must be true:
- All worker-reports completed
- UAT all PASS
- All open concerns reviewed (resolved, deferred, or rejected)
- User confirmed release

## Step 1: Load context (in parallel)

```
docs/ROADMAP.md
docs/features/          ← all feature specs
docs/worker-reports/    ← all reports
docs/concerns/          ← verify none are status: open
docs/versions/          ← find next version number
```

## Step 2: Verify release gate

```
Open concerns exist?
  → YES → STOP → run review-concerns first
  → NO → continue

Incomplete worker-reports?
  → YES → STOP → report to user
  → NO → continue
```

## Step 3: Create version archive

```
1. Read ROADMAP.md → summarize phases completed
2. Create docs/versions/v{x}.md using templates/release-report-template.md
   Include:
   - Features delivered (from features/)
   - Decisions made (from PROJECT.md)
   - Concerns resolved (from concerns/)
   - Deviations from plan (from worker-reports)
```

## Step 4: Cleanup VERSION-scoped files

```
DELETE: docs/worker-reports/       ← all reports
CLEAR:  docs/ROADMAP.md           ← reset for next version

KEEP (never delete):
  docs/features/                  ← [PERMANENT]
  docs/standards/                 ← [PERMANENT]
  docs/concerns/                  ← [PERMANENT]
  docs/research/                  ← [PERMANENT]
  docs/versions/                  ← [ARCHIVE]
```

See lifecycle labels: `references/docs-structure.md`

## Step 5: Reset for next version

```
1. Run scripts/create_version_release.py (if available)
2. Reset STATE.md using templates/state-template.md
3. Present summary to user:
   - Version released
   - What was delivered
   - What was deferred (concerns with status: deferred)
4. → orient (ready for next cycle)
```

## Script

Optional automation: `scripts/create_version_release.py`
If script unavailable → execute steps manually.
