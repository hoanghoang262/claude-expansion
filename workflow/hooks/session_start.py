#!/usr/bin/env python3
"""
SessionStart hook for workflow plugin.
Injects orchestrator skill into Claude's context at every session start.
"""
import json
from pathlib import Path

PLUGIN_ROOT = Path(__file__).parent.parent


def main() -> None:
    orchestrator_path = PLUGIN_ROOT / "skills" / "orchestrator" / "SKILL.md"
    try:
        orchestrator = orchestrator_path.read_text(encoding="utf-8")
    except OSError:
        orchestrator = "Error: orchestrator SKILL.md not found."

    output = {
        "hookSpecificOutput": {
            "hookEventName": "SessionStart",
            "additionalContext": f"<workflow-orchestrator>\n{orchestrator}\n</workflow-orchestrator>",
        }
    }
    print(json.dumps(output))


if __name__ == "__main__":
    main()
