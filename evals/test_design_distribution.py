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
