#!/usr/bin/env python3
"""
Execute a Version Release Event for the workflow orchestrator.

This script automates the 5-step release described in the orchestrator skill:

    1. Read ROADMAP.md → summarize all phases
    2. Create docs/versions/v{x}.md
    3. DELETE docs/worker-reports/
    4. CLEAR ROADMAP.md entirely
    5. KEEP docs/features/* unchanged

Usage:
    python3 create_version_release.py --version 1.2.0
    python3 create_version_release.py --version 1.2.0 --dry-run
    python3 create_version_release.py --version 1.2.0 --cwd /path/to/project

Options:
    --version   Version string (e.g. 1.2.0) — required
    --cwd       Project root (default: current directory)
    --dry-run   Show what would be done without making changes
    --confirm   Skip confirmation prompt and proceed
"""

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path


UTC_NOW = datetime.now(timezone.utc).strftime("%Y-%m-%d")


# ---------------------------------------------------------------------------
# Discovery
# ---------------------------------------------------------------------------

def find_docs_root(cwd: Path) -> Path:
    for candidate in [cwd, cwd.parent, cwd.parent.parent]:
        docs = candidate / "docs"
        if docs.exists():
            return docs
    print(f"Error: docs/ not found near {cwd}", file=sys.stderr)
    sys.exit(1)


def find_versions_dir(docs: Path) -> Path:
    vd = docs / "versions"
    vd.mkdir(parents=True, exist_ok=True)
    return vd


def detect_next_version(versions_dir: Path) -> str:
    existing = sorted(versions_dir.glob("v*.md"))
    if not existing:
        return "v0.1.0"
    try:
        last = existing[-1].stem
        parts = last.lstrip("v").split(".")
        parts[-1] = str(int(parts[-1]) + 1)
        return "v" + ".".join(parts)
    except (IndexError, ValueError):
        return "v0.1.0"


# ---------------------------------------------------------------------------
# Artifact discovery
# ---------------------------------------------------------------------------

def discover_artifacts(docs: Path) -> dict:
    roadmap = docs / "ROADMAP.md"
    wr_dir = docs / "worker-reports"
    return {
        "roadmap": roadmap if roadmap.exists() else None,
        "worker_reports": sorted(wr_dir.rglob("*.json")) if wr_dir.exists() else [],
        "features": [d for d in (docs / "features").iterdir() if d.is_dir()]
                      if (docs / "features").exists() else [],
    }


# ---------------------------------------------------------------------------
# Content gathering
# ---------------------------------------------------------------------------

def gather_roadmap_content(roadmap: Path | None) -> str:
    if not roadmap or not roadmap.exists():
        return "(no ROADMAP.md found — manual summary needed)"
    return roadmap.read_text(encoding="utf-8", errors="ignore")


def gather_features_status(docs: Path) -> list[dict]:
    results = []
    feat_dir = docs / "features"
    if not feat_dir.exists():
        return results
    for fd in sorted(feat_dir.iterdir()):
        if not fd.is_dir():
            continue
        uat = fd / "UAT.md"
        spec = fd / "spec.md"
        plan = fd / "PLAN.md"
        uat_status = "unknown"
        if uat.exists():
            text = uat.read_text(encoding="utf-8", errors="ignore")
            if "FAIL" in text or "❌" in text:
                uat_status = "fail"
            elif "PASS" in text or "✓" in text:
                uat_status = "pass"
        results.append({
            "name": fd.name,
            "has_spec": spec.exists(),
            "has_plan": plan.exists(),
            "uat_status": uat_status,
        })
    return results


def gather_outstanding_bugs(worker_reports: list[Path]) -> list[dict]:
    bugs = []
    for wr in worker_reports:
        try:
            data = json.loads(wr.read_text(encoding="utf-8", errors="ignore"))
            for b in data.get("outstanding_bugs", []):
                b["_source"] = str(wr.relative_to(wr.parents[2]))
                bugs.append(b)
        except Exception:
            pass
    return bugs


# ---------------------------------------------------------------------------
# Report generation
# ---------------------------------------------------------------------------

def generate_version_report(version: str, docs: Path, artifacts: dict) -> str:
    features = gather_features_status(docs)
    bugs = gather_outstanding_bugs(artifacts["worker_reports"])

    # Features section
    if features:
        feat_lines = []
        for f in features:
            badge = {"pass": "✓", "fail": "✗", "unknown": "?"}[f["uat_status"]]
            feat_lines.append(f"  - [{badge}] {f['name']}")
            if not f["has_spec"]:
                feat_lines.append(f"    WARNING: no spec.md")
            if not f["has_plan"]:
                feat_lines.append(f"    WARNING: no PLAN.md")
        features_section = "\n".join(feat_lines)
    else:
        features_section = "  (no features found)"

    # Roadmap section — first 60 non-blank lines
    roadmap_text = gather_roadmap_content(artifacts["roadmap"])
    roadmap_snippet = "\n".join(
        line for line in roadmap_text.splitlines()[:60] if line.strip()
    )

    # Bugs section
    if bugs:
        bug_lines = []
        for b in bugs:
            sev = b.get("severity", "?")
            sev_label = {"high": "🔴 HIGH", "medium": "🟡 MEDIUM", "low": "🟢 LOW"}.get(sev, sev.upper())
            bug_lines.append(f"  {sev_label} | {b.get('description','')} | {b.get('_source','')}")
        bugs_section = "\n".join(bug_lines)
    else:
        bugs_section = "  (no outstanding bugs reported)"

    return f"""# Version {version}

**Released:** {UTC_NOW} | **Released by:** orchestrator script

---

## Roadmap Summary

```
{roadmap_snippet or '(empty)'}
```

---

## Features Delivered

{features_section}

---

## Outstanding Bugs

{bugs_section}

---

## Release Checklist

- [ ] All features verified by user (UAT pass)
- [ ] Version report reviewed and committed
- [ ] Features/* committed to repository
- [ ] Project memory (docs/) synced to shared location
"""


# ---------------------------------------------------------------------------
# Dry run / describe
# ---------------------------------------------------------------------------

def describe_actions(version: str, docs: Path, artifacts: dict, dry_run: bool) -> None:
    tag = "Would" if dry_run else "Will"
    print(f"\n{'='*52}")
    print(f"  Version Release Event — {version}")
    print(f"{'='*52}\n")
    print(f"  {tag} CREATE: docs/versions/{version}.md")
    print(f"  {tag} CLEAR:  docs/ROADMAP.md")
    n_wr = len(artifacts["worker_reports"])
    if n_wr:
        print(f"  {tag} DELETE: {n_wr} worker-report(s) in docs/worker-reports/")
        for wr in artifacts["worker_reports"][:3]:
            print(f"           - {wr.relative_to(docs)}")
        if n_wr > 3:
            print(f"           ... and {n_wr - 3} more")
    else:
        print(f"  {tag} DELETE: docs/worker-reports/ (absent or empty)")
    print(f"  {tag} KEEP:   docs/features/ ({len(artifacts['features'])} feature(s))")
    print(f"\n  {'DRY RUN — no changes made.' if dry_run else 'Ready to execute.'}")


# ---------------------------------------------------------------------------
# Execution
# ---------------------------------------------------------------------------

def execute(version: str, docs: Path, artifacts: dict, dry_run: bool) -> None:
    versions_dir = find_versions_dir(docs)

    # 1. Generate + write version report
    report = generate_version_report(version, docs, artifacts)
    version_file = versions_dir / f"{version}.md"
    if dry_run:
        print(f"  [DRY RUN] Would write: {version_file}")
    else:
        version_file.write_text(report, encoding="utf-8")
        print(f"  ✓ Created: {version_file}")

    # 2. Clear ROADMAP.md
    roadmap = artifacts["roadmap"]
    if roadmap:
        if dry_run:
            print(f"  [DRY RUN] Would clear: {roadmap}")
        else:
            roadmap.write_text("", encoding="utf-8")
            print(f"  ✓ Cleared: {roadmap}")

    # 3. Delete worker-reports/
    if artifacts["worker_reports"]:
        if dry_run:
            print(f"  [DRY RUN] Would delete {len(artifacts['worker_reports'])} worker-report(s)")
        else:
            for wr in artifacts["worker_reports"]:
                wr.unlink()
            wr_dir = docs / "worker-reports"
            if wr_dir.exists() and not any(wr_dir.iterdir()):
                wr_dir.rmdir()
            print(f"  ✓ Deleted: {len(artifacts['worker_reports'])} worker-report(s)")

    # 4. Features kept — nothing to do
    print(f"  ✓ Kept: docs/features/ ({len(artifacts['features'])} feature(s))")


def main() -> None:
    parser = argparse.ArgumentParser(description="Execute a Version Release Event.")
    parser.add_argument("--version", "-v", help="Version string (e.g. 1.2.0). Auto-detected if omitted.")
    parser.add_argument("--cwd", type=Path, default=Path.cwd(), help="Project root.")
    parser.add_argument("--dry-run", action="store_true", help="Preview without changes.")
    parser.add_argument("--confirm", action="store_true", help="Skip confirmation.")
    args = parser.parse_args()

    docs = find_docs_root(args.cwd)
    versions_dir = find_versions_dir(docs)
    artifacts = discover_artifacts(docs)
    version = args.version or detect_next_version(versions_dir)

    describe_actions(version, docs, artifacts, args.dry_run)

    if args.dry_run:
        sys.exit(0)

    if not args.confirm:
        response = input("\nProceed? [y/N] ").strip().lower()
        if response not in ("y", "yes"):
            print("Aborted.")
            sys.exit(0)

    execute(version, docs, artifacts, dry_run=False)
    print(f"\nVersion {version} released successfully.")


if __name__ == "__main__":
    main()
