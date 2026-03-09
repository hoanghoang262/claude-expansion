#!/usr/bin/env python3
"""
Initialize .workflow/ directory in the current project.

Usage:
    python3 <plugin-root>/scripts/init_workflow.py

Run once per project. Creates .workflow/STATE.md, .workflow/PROJECT.md,
and .workflow/specs/ directory.
"""
from pathlib import Path
from datetime import date

CWD = Path.cwd()
WORKFLOW_DIR = CWD / ".workflow"
SPECS_DIR = WORKFLOW_DIR / "specs"

STATE_TEMPLATE = f"""# Workflow State

phase: clarify
active-spec: none
track: none
next-action: Start by describing what you want to build.
blocked-by: none
last-updated: {date.today()}
"""

PROJECT_TEMPLATE = """# Project

## Identity
[Project name and one-sentence description]

## Goals
[What this project is trying to achieve]

## Constraints
[Technical constraints, non-negotiables, conventions]

## Key Decisions
[Architecture or design decisions already locked in]
"""


def main() -> None:
    if WORKFLOW_DIR.exists():
        print(f".workflow/ already exists at {WORKFLOW_DIR}")
        return

    SPECS_DIR.mkdir(parents=True)
    (WORKFLOW_DIR / "STATE.md").write_text(STATE_TEMPLATE, encoding="utf-8")
    (WORKFLOW_DIR / "PROJECT.md").write_text(PROJECT_TEMPLATE, encoding="utf-8")
    print(f"Initialized .workflow/ at {WORKFLOW_DIR}")
    print("Next: fill in .workflow/PROJECT.md with your project context.")


if __name__ == "__main__":
    main()
