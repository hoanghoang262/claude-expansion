#!/usr/bin/env python3
"""
Unit tests for create_docs_structure.py

Tests Step 0 (skeleton) and Step 2 (from docs-map.md).
Run: python3 test_create_docs_structure.py
"""
import re
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPTS_DIR = Path(__file__).parent.parent / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))

import create_docs_structure as cds


# ---------------------------------------------------------------------------
# Step 0 — skeleton
# ---------------------------------------------------------------------------

class TestStep0Skeleton(unittest.TestCase):

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)

    def tearDown(self):
        self._tmp.cleanup()

    def test_creates_core_files(self):
        cds.create_skeleton(self.root, "Test", "web-app")
        docs = self.root / "docs"
        self.assertTrue((docs / "project.md").exists(), "project.md missing")
        self.assertTrue((docs / "state.md").exists(), "state.md missing")
        self.assertTrue((docs / "docs-map.md").exists(), "docs-map.md missing")

    def test_creates_core_dirs(self):
        cds.create_skeleton(self.root, "Test", "unknown")
        docs = self.root / "docs"
        for d in ["decisions", "concerns"]:
            self.assertTrue((docs / d).is_dir(), f"{d} missing")

    def test_no_features_dir(self):
        cds.create_skeleton(self.root, "Test", "unknown")
        self.assertFalse((self.root / "docs" / "features").exists(),
                         "features/ must NOT be created by skeleton — agent decides")

    def test_no_foundations_dir(self):
        cds.create_skeleton(self.root, "Test", "unknown")
        self.assertFalse((self.root / "docs" / "foundations").exists(),
                         "foundations/ must NOT be created by skeleton — agent decides")

    def test_state_md_format(self):
        cds.create_skeleton(self.root, "Test", "unknown")
        content = (self.root / "docs" / "state.md").read_text()
        self.assertIn("CLARIFY", content)
        self.assertIn("init", content)
        self.assertNotIn("ACTIVE DEVELOPMENT", content)
        self.assertNotIn("functional", content.lower())

    def test_reset_state_overwrites(self):
        cds.create_skeleton(self.root, "Test", "unknown")
        # Corrupt state.md
        (self.root / "docs" / "state.md").write_text("corrupted")
        cds.reset_state(self.root)
        content = (self.root / "docs" / "state.md").read_text()
        self.assertIn("CLARIFY", content)
        self.assertIn("init", content)

    def test_reset_state_creates_if_missing(self):
        (self.root / "docs").mkdir()
        cds.reset_state(self.root)
        self.assertTrue((self.root / "docs" / "state.md").exists())
        content = (self.root / "docs" / "state.md").read_text()
        self.assertIn("CLARIFY", content)

    def test_docs_map_is_placeholder(self):
        cds.create_skeleton(self.root, "Test", "unknown")
        content = (self.root / "docs" / "docs-map.md").read_text()
        self.assertIn("To be written", content)
        self.assertIn("yaml", content)

    def test_skip_existing_files(self):
        cds.create_skeleton(self.root, "Test", "unknown")
        (self.root / "docs" / "project.md").write_text("custom")
        cds.create_skeleton(self.root, "Test v2", "unknown")
        self.assertEqual((self.root / "docs" / "project.md").read_text(), "custom",
                         "Existing files must not be overwritten")


# ---------------------------------------------------------------------------
# Step 2 — create from docs-map.md
# ---------------------------------------------------------------------------

def _write_docs_map(root: Path, yaml_content: str) -> Path:
    path = root / "docs" / "docs-map.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"# Docs Map\n\n## Structure\n\n```yaml\n{yaml_content}\n```\n")
    return path


class TestStep2FromDocsMap(unittest.TestCase):

    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.root = Path(self._tmp.name)
        cds.create_skeleton(self.root, "Test", "unknown")

    def tearDown(self):
        self._tmp.cleanup()

    def test_user_feature_full_docs(self):
        _write_docs_map(self.root, """
features:
  - name: auth
    interface: user
    backend: src/modules/auth/
    docs:
      - requirements.md
      - user-stories.md
      - spec.md
foundations: []
""")
        cds.create_from_docs_map(self.root, self.root / "docs" / "docs-map.md")
        d = self.root / "docs" / "features" / "auth"
        for f in ["requirements.md", "user-stories.md", "spec.md"]:
            self.assertTrue((d / f).exists(), f"auth/{f} missing")

    def test_internal_feature_spec_only(self):
        _write_docs_map(self.root, """
features:
  - name: file
    interface: internal
    docs:
      - spec.md
foundations: []
""")
        cds.create_from_docs_map(self.root, self.root / "docs" / "docs-map.md")
        d = self.root / "docs" / "features" / "file"
        self.assertTrue((d / "spec.md").exists())
        self.assertFalse((d / "user-stories.md").exists(),
                         "internal features must not have user-stories.md")

    def test_developer_feature_no_user_stories(self):
        _write_docs_map(self.root, """
features:
  - name: jwt-module
    interface: developer
    docs:
      - requirements.md
      - spec.md
foundations: []
""")
        cds.create_from_docs_map(self.root, self.root / "docs" / "docs-map.md")
        d = self.root / "docs" / "features" / "jwt-module"
        self.assertTrue((d / "requirements.md").exists())
        self.assertTrue((d / "spec.md").exists())
        self.assertFalse((d / "user-stories.md").exists())

    def test_foundations_created(self):
        _write_docs_map(self.root, """
features: []
foundations:
  - database-schema.md
  - infrastructure.md
  - security.md
""")
        cds.create_from_docs_map(self.root, self.root / "docs" / "docs-map.md")
        fd = self.root / "docs" / "foundations"
        for f in ["database-schema.md", "infrastructure.md", "security.md"]:
            self.assertTrue((fd / f).exists(), f"foundations/{f} missing")

    def test_multiple_features(self):
        _write_docs_map(self.root, """
features:
  - name: exam
    interface: user
    docs: [requirements.md, user-stories.md, spec.md]
  - name: auth
    interface: user
    docs: [requirements.md, user-stories.md, spec.md]
  - name: notification
    interface: internal
    docs: [spec.md]
foundations:
  - database-schema.md
""")
        cds.create_from_docs_map(self.root, self.root / "docs" / "docs-map.md")
        for feat in ["exam", "auth"]:
            d = self.root / "docs" / "features" / feat
            for f in ["requirements.md", "user-stories.md", "spec.md"]:
                self.assertTrue((d / f).exists(), f"{feat}/{f} missing")
        notif = self.root / "docs" / "features" / "notification"
        self.assertTrue((notif / "spec.md").exists())
        self.assertFalse((notif / "user-stories.md").exists())

    def test_flat_single_unit_no_features_dir(self):
        _write_docs_map(self.root, """
features: []
foundations:
  - usage.md
""")
        cds.create_from_docs_map(self.root, self.root / "docs" / "docs-map.md")
        self.assertFalse((self.root / "docs" / "features").exists(),
                         "Single-unit project must not have features/ subdir")

    def test_error_no_yaml_block(self):
        docs_map = self.root / "docs" / "docs-map.md"
        docs_map.write_text("# Docs Map\n\nNo yaml block.\n")
        with self.assertRaises(SystemExit):
            cds.create_from_docs_map(self.root, docs_map)

    def test_error_placeholder_yaml(self):
        docs_map = self.root / "docs" / "docs-map.md"
        docs_map.write_text("# Docs Map\n\n```yaml\n\n```\n")
        with self.assertRaises(SystemExit):
            cds.create_from_docs_map(self.root, docs_map)

    def test_stub_files_not_empty(self):
        _write_docs_map(self.root, """
features:
  - name: auth
    interface: user
    docs: [requirements.md]
foundations: []
""")
        cds.create_from_docs_map(self.root, self.root / "docs" / "docs-map.md")
        content = (self.root / "docs" / "features" / "auth" / "requirements.md").read_text()
        self.assertGreater(len(content.strip()), 0, "Stub files must not be empty")


# ---------------------------------------------------------------------------
# Cross-check: docs-map.md vs filesystem
# ---------------------------------------------------------------------------

class TestCrossCheck(unittest.TestCase):
    """Simulate the Step 4 verify logic."""

    def _features_from_map(self, docs_map: Path) -> set:
        content = docs_map.read_text()
        match = re.search(r"```yaml\n(.*?)```", content, re.DOTALL)
        if not match:
            return set()
        try:
            import yaml
            data = yaml.safe_load(match.group(1))
            return {f["name"] for f in data.get("features", [])} if data else set()
        except Exception:
            return set()

    def _features_from_fs(self, root: Path) -> set:
        d = root / "docs" / "features"
        return {x.name for x in d.iterdir() if x.is_dir()} if d.exists() else set()

    def test_full_match_after_step2(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            cds.create_skeleton(root, "Test", "unknown")
            _write_docs_map(root, """
features:
  - name: auth
    interface: user
    docs: [spec.md]
  - name: exam
    interface: user
    docs: [spec.md]
foundations: []
""")
            cds.create_from_docs_map(root, root / "docs" / "docs-map.md")
            expected = self._features_from_map(root / "docs" / "docs-map.md")
            actual = self._features_from_fs(root)
            self.assertEqual(expected, actual)

    def test_detects_missing_feature(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            cds.create_skeleton(root, "Test", "unknown")
            _write_docs_map(root, """
features:
  - name: auth
    interface: user
    docs: [spec.md]
  - name: analytics
    interface: user
    docs: [spec.md]
foundations: []
""")
            # Only create auth, skip analytics (simulates agent miss)
            (root / "docs" / "features" / "auth").mkdir(parents=True)
            (root / "docs" / "features" / "auth" / "spec.md").write_text("x")

            expected = self._features_from_map(root / "docs" / "docs-map.md")
            actual = self._features_from_fs(root)
            missing = expected - actual
            self.assertEqual(missing, {"analytics"})


if __name__ == "__main__":
    unittest.main(verbosity=2)
