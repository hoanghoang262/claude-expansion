#!/usr/bin/env python3
"""
Create docs/ structure for a project.

Step 0 — skeleton:
  python3 create_docs_structure.py --project-root /path --project-name "Name"
  Creates: project.md, state.md, docs-map.md (placeholder), decisions/, concerns/

Step 2 — structure from docs-map:
  python3 create_docs_structure.py --project-root /path --docs-map docs/docs-map.md
  Reads YAML block in docs-map.md → creates feature dirs + empty stubs

Reset state:
  python3 create_docs_structure.py --project-root /path --reset-state
  Overwrites docs/state.md with default CLARIFY state (use when state.md is missing or corrupted)
"""
import argparse
import re
import sys
from pathlib import Path

try:
    import yaml
    HAS_YAML = True
except ImportError:
    HAS_YAML = False

# ---------------------------------------------------------------------------
# Templates
# ---------------------------------------------------------------------------

PROJECT_MD = """\
# {name}

## Identity
- **Type:** {project_type}
- **Purpose:** _To be filled by agent._
- **Path:** {project_root}

## Architecture
_To be filled by agent._

## Tech Stack
_To be filled by agent._

## Modules
_To be filled by agent._

## Run
_To be filled by agent._
"""

STATE_MD = """\
# State

Orchestrator tracking only. NOT project status.

## Phase
CLARIFY

## Action
init

## Feature
none

## Wave
n/a
"""

DOCS_MAP_PLACEHOLDER = """\
# Docs Map

_To be written by Step 1 agent._

## Reasoning

{agent explains: project type, detection method, key signals used}

## Structure

```yaml
features:
  - name: {feature-name}
    interface: user        # user | developer | internal
    backend: {path}
    frontend: {path}       # omit if none
    docs:
      - requirements.md
      - user-stories.md    # omit if interface: developer or internal
      - spec.md

foundations:
  - database-schema.md
  - infrastructure.md
```
"""

STUB_CONTENT = "# {title}\n\n_To be filled by agent._\n"

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        print(f"  [skip]   {path}")
        return
    path.write_text(content, encoding="utf-8")
    print(f"  [create] {path}")


def make_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def reset_state(project_root: Path) -> None:
    docs_dir = project_root / "docs"
    state_path = docs_dir / "state.md"
    state_path.parent.mkdir(parents=True, exist_ok=True)
    state_path.write_text(STATE_MD, encoding="utf-8")
    print(f"  [reset]  {state_path}")

# ---------------------------------------------------------------------------
# Step 0 — skeleton
# ---------------------------------------------------------------------------

SKELETON_DIRS = ["decisions", "concerns"]


def create_skeleton(project_root: Path, project_name: str, project_type: str) -> None:
    docs_dir = project_root / "docs"

    for d in SKELETON_DIRS:
        make_dir(docs_dir / d)
        print(f"  [dir]    {docs_dir / d}")

    write_file(
        docs_dir / "project.md",
        PROJECT_MD.format(
            name=project_name,
            project_type=project_type,
            project_root=str(project_root),
        ),
    )
    write_file(docs_dir / "state.md", STATE_MD)
    write_file(docs_dir / "docs-map.md", DOCS_MAP_PLACEHOLDER)

    print(f"\n[done] Skeleton at {docs_dir}")

# ---------------------------------------------------------------------------
# Step 2 — structure from docs-map.md
# ---------------------------------------------------------------------------

def extract_yaml_block(docs_map_path: Path) -> str:
    content = docs_map_path.read_text(encoding="utf-8")
    match = re.search(r"```yaml\n(.*?)```", content, re.DOTALL)
    if not match:
        print(f"[error] No ```yaml block found in {docs_map_path}", file=sys.stderr)
        print("        Step 1 agent must write docs-map.md with a fenced yaml block first.", file=sys.stderr)
        sys.exit(1)
    return match.group(1)


def create_from_docs_map(project_root: Path, docs_map_path: Path) -> None:
    if not HAS_YAML:
        print("[error] PyYAML required: pip install pyyaml", file=sys.stderr)
        sys.exit(1)

    yaml_text = extract_yaml_block(docs_map_path)
    data = yaml.safe_load(yaml_text)

    if not data:
        print("[error] YAML block is empty or still a placeholder.", file=sys.stderr)
        sys.exit(1)

    docs_dir = project_root / "docs"
    features = data.get("features", [])
    foundations = data.get("foundations", [])

    # Feature dirs + stubs
    for f in features:
        name = f.get("name", "unknown")
        interface = f.get("interface", "user")
        docs = f.get("docs", ["spec.md"])

        if interface == "internal" and not docs:
            docs = ["spec.md"]

        feature_dir = docs_dir / "features" / name
        make_dir(feature_dir)
        print(f"  [dir]    {feature_dir}")

        for doc in docs:
            label = doc.replace(".md", "").replace("-", " ").title()
            title = f"{name.title()} — {label}"
            write_file(feature_dir / doc, STUB_CONTENT.format(title=title))

    # Foundation stubs
    if foundations:
        foundations_dir = docs_dir / "foundations"
        make_dir(foundations_dir)
        print(f"  [dir]    {foundations_dir}")
        for fname in foundations:
            title = fname.replace(".md", "").replace("-", " ").title()
            write_file(foundations_dir / fname, STUB_CONTENT.format(title=title))

    print(f"\n[done] {len(features)} features, {len(foundations)} foundations")

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(description="Create docs/ structure")
    parser.add_argument("--project-root", required=True, help="Absolute path to project root")
    parser.add_argument("--project-name", default="Project", help="Project name (Step 0)")
    parser.add_argument("--project-type", default="unknown", help="Project type hint (Step 0)")
    parser.add_argument("--docs-map", help="Path to docs-map.md (triggers Step 2)")
    parser.add_argument("--reset-state", action="store_true", help="Overwrite state.md with default CLARIFY state")
    args = parser.parse_args()

    project_root = Path(args.project_root).resolve()

    if args.reset_state:
        reset_state(project_root)
    elif args.docs_map:
        docs_map_path = Path(args.docs_map)
        if not docs_map_path.is_absolute():
            docs_map_path = project_root / docs_map_path
        create_from_docs_map(project_root, docs_map_path)
    else:
        create_skeleton(project_root, args.project_name, args.project_type)


if __name__ == "__main__":
    main()
