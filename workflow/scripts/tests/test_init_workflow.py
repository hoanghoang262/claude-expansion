import subprocess
import sys
from pathlib import Path
from datetime import date

SCRIPT = Path(__file__).parent.parent / "init_workflow.py"


def run_script(cwd):
    result = subprocess.run(
        [sys.executable, str(SCRIPT)],
        capture_output=True, text=True, cwd=str(cwd)
    )
    return result


def test_creates_workflow_dir(tmp_path):
    run_script(tmp_path)
    assert (tmp_path / ".workflow").is_dir()
    assert (tmp_path / ".workflow" / "specs").is_dir()


def test_creates_state_md(tmp_path):
    run_script(tmp_path)
    state = (tmp_path / ".workflow" / "STATE.md").read_text()
    for key in ["phase:", "active-spec:", "track:", "next-action:", "blocked-by:", "last-updated:"]:
        assert key in state


def test_creates_project_md(tmp_path):
    run_script(tmp_path)
    project = (tmp_path / ".workflow" / "PROJECT.md").read_text()
    assert "# Project" in project


def test_exit_zero_on_success(tmp_path):
    result = run_script(tmp_path)
    assert result.returncode == 0


def test_idempotent_does_not_overwrite(tmp_path):
    run_script(tmp_path)
    # Modify STATE.md
    state_path = tmp_path / ".workflow" / "STATE.md"
    state_path.write_text("custom content")
    # Run again
    result = run_script(tmp_path)
    assert result.returncode == 0
    assert "already exists" in result.stdout
    # Content should not be overwritten
    assert state_path.read_text() == "custom content"
