#!/usr/bin/env python3
"""
Search version reports for keywords, bug IDs, feature names, or decision notes.

This script scans docs/versions/v*.md — the archive created by each
Version Release Event. Use it to recover context from past releases.

Usage:
    python3 search_version.py -q "authentication"
    python3 search_version.py -q "bug-42" --cwd /path/to/project
    python3 search_version.py -q "dashboard" -r           # show matching lines
    python3 search_version.py --list                     # list all versions

Options:
    -q, --query      Search term (keyword, bug ID, feature name)
    -r, --regex      Treat query as a regex pattern
    -l, --list       List all version files without searching
    -w, --workers    Glob pattern for worker-reports to also search (default: *.json)
    --cwd            Project root (default: current directory)
"""

import argparse
import json
import re
import sys
from pathlib import Path


DEFAULT_WORKER_GLOB = "*.json"


def find_docs_root(cwd: Path) -> Path:
    for candidate in [cwd, cwd.parent]:
        docs = candidate / "docs"
        if docs.exists():
            return docs
    print(f"Error: docs/ not found near {cwd}", file=sys.stderr)
    sys.exit(1)


def list_versions(versions_dir: Path) -> list[Path]:
    if not versions_dir.exists():
        return []
    return sorted(versions_dir.glob("v*.md"), reverse=True)


def search_file(path: Path, pattern: re.Pattern, show_lines: bool) -> list[tuple[int, str]]:
    """Return list of (line_num, line) matches in a file."""
    matches = []
    try:
        for i, line in enumerate(path.read_text(encoding="utf-8", errors="ignore").splitlines(), 1):
            if pattern.search(line):
                matches.append((i, line.strip()))
    except Exception as e:
        print(f"  Warning: could not read {path}: {e}", file=sys.stderr)
    return matches


def search_version_reports(docs: Path, pattern: re.Pattern, show_lines: bool) -> None:
    versions_dir = docs / "versions"
    versions = list_versions(versions_dir)

    if not versions:
        print("No version reports found in docs/versions/")
        return

    found_any = False
    for vp in versions:
        matches = search_file(vp, pattern, show_lines)
        if matches:
            found_any = True
            print(f"\n## {vp.stem}")
            if show_lines:
                for lineno, line in matches:
                    print(f"  L{lineno}: {line}")
            else:
                for _, line in matches:
                    print(f"  {line}")

    if not found_any:
        print(f"No matches found for: {pattern.pattern!r}")


def search_worker_reports(docs: Path, pattern: re.Pattern, show_lines: bool) -> None:
    wr_dir = docs / "worker-reports"
    if not wr_dir.exists():
        return

    found_any = False
    for wr in wr_dir.rglob("*.json"):
        try:
            content = wr.read_text(encoding="utf-8")
            # Search raw JSON text
            matched_lines = []
            for i, line in enumerate(content.splitlines(), 1):
                if pattern.search(line):
                    matched_lines.append((i, line.strip()))

            if matched_lines:
                found_any = True
                rel = wr.relative_to(docs)
                print(f"\n## {rel}")
                if show_lines:
                    for lineno, line in matched_lines:
                        print(f"  L{lineno}: {line}")
                else:
                    for _, line in matched_lines[:5]:  # cap output
                        print(f"  {line}")
                    if len(matched_lines) > 5:
                        print(f"  ... and {len(matched_lines) - 5} more matches")
        except Exception as e:
            print(f"  Warning: could not read {wr}: {e}", file=sys.stderr)

    if not found_any:
        print(f"\nNo worker-report matches found for: {pattern.pattern!r}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Search version reports and worker reports."
    )
    parser.add_argument(
        "-q", "--query", type=str,
        help="Search term or pattern"
    )
    parser.add_argument(
        "-r", "--regex", action="store_true",
        help="Treat --query as a regex pattern"
    )
    parser.add_argument(
        "-l", "--list", action="store_true",
        help="List all version files without searching"
    )
    parser.add_argument(
        "--workers", action="store_true",
        help="Also search worker-reports/ (default: search version reports only)"
    )
    parser.add_argument(
        "--cwd", type=Path, default=Path.cwd(),
        help="Project root (default: current directory)"
    )
    args = parser.parse_args()

    docs = find_docs_root(args.cwd)
    versions_dir = docs / "versions"

    # --list: just show available versions
    if args.list:
        versions = list_versions(versions_dir)
        if not versions:
            print("No version reports found.")
        else:
            print(f"Found {len(versions)} version report(s):\n")
            for vp in versions:
                title = vp.read_text(encoding="utf-8", errors="ignore").splitlines()[0].lstrip("# ").strip()
                print(f"  {vp.stem}  —  {title}")
        sys.exit(0)

    if not args.query:
        parser.print_help()
        sys.exit(1)

    flags = re.IGNORECASE if not args.regex else re.IGNORECASE
    pattern = re.compile(args.query, flags)

    show_lines = True

    print(f"Searching docs/ for: {args.query!r}\n")
    search_version_reports(docs, pattern, show_lines)

    if args.workers:
        search_worker_reports(docs, pattern, show_lines)


if __name__ == "__main__":
    main()
