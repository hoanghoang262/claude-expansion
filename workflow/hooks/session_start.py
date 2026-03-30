#!/usr/bin/env python3
"""
SessionStart hook for workflow plugin.
Injects PA skill context and project root into session.
"""
import json
from pathlib import Path

PLUGIN_ROOT = Path(__file__).parent.parent
ORCHESTRATOR_DIR = PLUGIN_ROOT / "skills" / "orchestrator"


def read_file(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError:
        return f"[Error: {path.name} not found]"


def find_project_root() -> Path:
    """Walk up from cwd to find project root (has .git/ or package.json)."""
    cwd = Path.cwd()
    for candidate in [cwd, cwd.parent, cwd.parent.parent]:
        if (candidate / ".git").exists() or (candidate / "package.json").exists():
            return candidate
    return cwd


def main() -> None:
    skill_text = read_file(ORCHESTRATOR_DIR / "SKILL.md")
    project_root = find_project_root()

    context = (
        "<EXTREMELY_IMPORTANT>\n"
        "You are the Personal Assistant (PA). You coordinate, delegate, manage memory.\n"
        "You do NOT read source code or analyze implementations — agents do that.\n\n"
        f"{skill_text}\n\n"
        f"project_root: {project_root}\n"
        "</EXTREMELY_IMPORTANT>"
    )

    output = {
        "hookSpecificOutput": {
            "hookEventName": "SessionStart",
            "additionalContext": context,
        }
    }
    print(json.dumps(output))


if __name__ == "__main__":
    main()
