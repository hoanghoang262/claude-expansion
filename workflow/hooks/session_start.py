#!/usr/bin/env python3
"""
SessionStart hook for workflow plugin.

Injects into Claude's context:
1. Orchestrator skill content (always)
2. .workflow/STATE.md from project root (if present)
"""
import json
import sys
from pathlib import Path

PLUGIN_ROOT = Path(__file__).parent.parent
CWD = Path.cwd()


def read_file(path: Path):
    try:
        return path.read_text(encoding="utf-8")
    except OSError:
        return None


def build_context() -> str:
    parts = []

    orchestrator = read_file(PLUGIN_ROOT / "skills" / "orchestrator" / "SKILL.md")
    if orchestrator is None:
        orchestrator = "Error: orchestrator SKILL.md not found."
    parts.append(f"<workflow-orchestrator>\n{orchestrator}\n</workflow-orchestrator>")

    state = read_file(CWD / ".workflow" / "STATE.md")
    if state is not None:
        parts.append(f"<workflow-state>\n{state}\n</workflow-state>")

    return "\n\n".join(parts)


def main() -> None:
    context = build_context()
    output = {
        "hookSpecificOutput": {
            "hookEventName": "SessionStart",
            "additionalContext": context,
        }
    }
    print(json.dumps(output))


if __name__ == "__main__":
    main()
