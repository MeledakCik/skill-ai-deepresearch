"""Compare the design skills an agent will load with a clean build of the specification."""

import io
import json
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

from scripts import sync


def text_files(directory):
    return {
        path.relative_to(directory): path.read_text(encoding="utf-8")
        for path in directory.rglob("*")
        if path.is_file()
    }


class DesignDistributionTests(unittest.TestCase):
    def test_screenshot_workflow_is_available_from_design_and_migration(self):
        body, _ = sync.frontmatter(sync.SRC.read_text(encoding="utf-8"))
        reference = sync.sections(body)["U5"]
        relative = Path("references") / sync.ref_filename("U5", reference)
        for base in ["skills", *sync.NATIVE_DIRS]:
            for name in ["web-ui-design", "platform-migration"]:
                with self.subTest(skill=name, distribution=base):
                    skill = sync.ROOT / base / name
                    self.assertIn(relative.as_posix(), (skill / "SKILL.md").read_text(encoding="utf-8"))
                    self.assertEqual((skill / relative).read_text(encoding="utf-8").rstrip(), reference)

    def test_published_design_skills_match_source(self):
        root = sync.ROOT
        body, version = sync.frontmatter(sync.SRC.read_text(encoding="utf-8"))
        design = {name: sync.SKILLS[name] for name in ("web-ui-design", "ui-component-motion")}
        with tempfile.TemporaryDirectory() as temporary:
            build = Path(temporary)
            with patch.object(sync, "ROOT", build), patch.object(sync, "SKILLS", design), redirect_stdout(io.StringIO()):
                sync.build_skills(body, version)
            for name in design:
                expected = text_files(build / "skills" / name)
                for base in ["skills", *sync.NATIVE_DIRS]:
                    with self.subTest(skill=name, distribution=base):
                        self.assertEqual(text_files(root / base / name), expected)

        manifest = json.loads((root / ".codex-plugin/plugin.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["version"], version)
        self.assertEqual((root / manifest["skills"]).resolve(), root / "skills")
