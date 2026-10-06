from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = ROOT / "skills" / "lantide-team-workflow-default"


class RepositoryContractTests(unittest.TestCase):
    def test_validator_passes(self) -> None:
        result = subprocess.run(
            [sys.executable, "scripts/validate.py"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("5 team policies and 3 workflows", result.stdout)

    def test_skill_references_every_required_policy_and_workflow(self) -> None:
        skill = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8")
        expected = (
            "team-context.md",
            "usage-policy.md",
            "roles-and-review.md",
            "evidence-policy.md",
            "delivery-policy.md",
            "new-formal-analysis.md",
            "update-existing-analysis.md",
            "exploration-to-formal.md",
        )
        for name in expected:
            self.assertIn(name, skill)

    def test_default_policy_is_not_an_empty_template(self) -> None:
        team_root = SKILL_ROOT / "references" / "team"
        for path in team_root.glob("*.md"):
            text = path.read_text(encoding="utf-8")
            self.assertGreater(len(text), 700, path.name)
            self.assertNotIn("[TODO]", text)
            self.assertNotIn("[TBD]", text)


if __name__ == "__main__":
    unittest.main()
