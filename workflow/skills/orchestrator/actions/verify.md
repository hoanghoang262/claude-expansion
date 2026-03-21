# verify — UAT & Quality Gate

## Step 1: Load context (in parallel)

```
docs/features/{id}/spec.md
docs/features/{id}/requirement.md
docs/features/{id}/PLAN.md
docs/worker-reports/{id}/*.json     ← all worker-reports
```

## Step 2: Create or review UAT checklist

```
UAT.md exists?
  → YES → review each entry against worker-reports
  → NO  → create from spec.md §Verification Criteria using templates/uat-template.md
```

## Step 3: Present to user

Display UAT checklist.
→ User marks each criterion PASS or FAIL.

## Step 4: Fix loop (if any FAIL)

```
Identify the last FAIL entry.
→ Reproduce the failure.
→ Spawn Executor to fix.
→ Re-run verification for that entry.
→ Repeat until all PASS.
```

## Step 5: All PASS

```
→ doc-sync
```
