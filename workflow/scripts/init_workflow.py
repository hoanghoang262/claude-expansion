#!/usr/bin/env python3
"""
Initialize workflow directories in the current project.

Usage:
    python3 <plugin-root>/scripts/init_workflow.py

Run once per project. Creates:
- docs/  — long-term project memory
- .workflow/ — short-term working space
"""
from pathlib import Path

CWD = Path.cwd()
DOCS_DIR = CWD / "docs"
WORKFLOW_DIR = CWD / ".workflow"

PROJECT_TEMPLATE = """# Project

## Identity
[Project name and one-sentence description]

## Goals
[What this project is trying to achieve]

## Stack
[Languages, frameworks, key libraries]

## Constraints
[Technical constraints, non-negotiables, existing conventions]

## Key Decisions
[Architecture or design decisions already locked in]
"""

OVERVIEW_TEMPLATE = """# Overview

[What this system does and how — updated as features are delivered]
"""


def init_docs() -> None:
    if DOCS_DIR.exists():
        print(f"docs/ already exists at {DOCS_DIR}")
        return

    (DOCS_DIR / "specs").mkdir(parents=True)
    (DOCS_DIR / "features").mkdir()
    (DOCS_DIR / "use-cases").mkdir()
    (DOCS_DIR / "adr").mkdir()
    (DOCS_DIR / "architecture").mkdir()
    (DOCS_DIR / "research").mkdir()
    (DOCS_DIR / "PROJECT.md").write_text(PROJECT_TEMPLATE, encoding="utf-8")
    (DOCS_DIR / "overview.md").write_text(OVERVIEW_TEMPLATE, encoding="utf-8")
    print(f"Created docs/ at {DOCS_DIR}")


def init_workflow() -> None:
    if WORKFLOW_DIR.exists():
        print(f".workflow/ already exists at {WORKFLOW_DIR}")
        return

    (WORKFLOW_DIR / "brainstorm").mkdir(parents=True)
    (WORKFLOW_DIR / "log").mkdir()
    (WORKFLOW_DIR / "brainstorm" / ".gitkeep").touch()
    (WORKFLOW_DIR / "log" / ".gitkeep").touch()
    print(f"Created .workflow/ at {WORKFLOW_DIR}")


def main() -> None:
    init_docs()
    init_workflow()
    print("\nNext: fill in docs/PROJECT.md with your project context.")


if __name__ == "__main__":
    main()
