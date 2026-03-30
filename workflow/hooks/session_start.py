#!/usr/bin/env python3
"""
SessionStart hook for workflow plugin.
Loads orchestrator context. Pre-injects init.md when docs/ is missing.
"""
import json
from pathlib import Path

PLUGIN_ROOT = Path(__file__).parent.parent
ORCHESTRATOR_DIR = PLUGIN_ROOT / "skills" / "orchestrator"
ACTIONS_DIR = ORCHESTRATOR_DIR / "actions"


def read_file(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError:
        return f"[Error: {path.name} not found]"


def find_project_root() -> Path | None:
    """Walk up from cwd to find project root (has package.json or .git/)."""
    cwd = Path.cwd()
    for candidate in [cwd, cwd.parent, cwd.parent.parent]:
        if (candidate / "package.json").exists() or (candidate / ".git").exists():
            return candidate
    return cwd


def check_docs(project_root: Path) -> bool:
    """Check if docs/project.md exists."""
    return (project_root / "docs" / "project.md").exists()


def main() -> None:
    skill_text = read_file(ORCHESTRATOR_DIR / "SKILL.md")

    project_root = find_project_root()
    has_docs = check_docs(project_root) if project_root else False

    # If no docs → also inject init.md so AI doesn't need to find it
    init_section = ""
    if not has_docs:
        init_text = read_file(ACTIONS_DIR / "init.md")
        init_section = (
            f"\n\n<init-action-preloaded>\n{init_text}\n</init-action-preloaded>"
            "\n\n<important-reminder>"
            "IN YOUR FIRST REPLY AFTER SEEING THIS MESSAGE YOU MUST:\n"
            "1. Announce: 🎯 **Personal Assistant active** — running init\n"
            "2. Try reading docs/project.md — it will fail (docs/ missing)\n"
            "3. Do a quick scan (ls, check .git/, package.json)\n"
            "4. Then IMMEDIATELY run init from the preloaded init action above\n"
            "5. init MUST spawn general-purpose agent — PA does NOT read code\n"
            "DO NOT skip init. DO NOT read source code yourself.\n"
            f"Project types at: {ORCHESTRATOR_DIR}/project-types/\n"
            "</important-reminder>"
        )

    context = (
        "<EXTREMELY_IMPORTANT>\n"
        "You are the Personal Assistant (PA). You coordinate, delegate, manage memory.\n"
        "You do NOT read source code or analyze implementations — agents do that.\n\n"
        f"{skill_text}\n\n"
        f"actions_dir: {ACTIONS_DIR}\n"
        f"project_types_dir: {ORCHESTRATOR_DIR}/project-types\n"
        f"scripts_dir: {ORCHESTRATOR_DIR}/scripts\n"
        f"project_root: {project_root}\n"
        f"docs_exist: {str(has_docs).lower()}\n"
        f"{init_section}\n"
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
