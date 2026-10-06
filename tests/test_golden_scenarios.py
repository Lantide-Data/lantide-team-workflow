from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = ROOT / "skills" / "lantide-team-workflow-default"


class GoldenScenarioContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.skill = (SKILL_ROOT / "SKILL.md").read_text(encoding="utf-8").lower()
        cls.usage = (SKILL_ROOT / "references/team/usage-policy.md").read_text(encoding="utf-8").lower()
        cls.evidence = (SKILL_ROOT / "references/team/evidence-policy.md").read_text(encoding="utf-8").lower()
        cls.update = (SKILL_ROOT / "references/workflows/update-existing-analysis.md").read_text(encoding="utf-8").lower()
        cls.explore = (SKILL_ROOT / "references/workflows/exploration-to-formal.md").read_text(encoding="utf-8").lower()

    def test_one_off_calculation_is_not_forced_into_lantide(self) -> None:
        self.assertIn("one-off arithmetic calculation", self.usage)
        self.assertIn("outside lantide", self.usage)

    def test_decision_metric_requires_formal_workflow(self) -> None:
        self.assertIn("influence a business", self.usage)
        self.assertIn("lantide formal analysis", self.usage)

    def test_exploratory_result_is_formalized_before_distribution(self) -> None:
        self.assertIn("cited, distributed, used for a decision", self.explore)
        self.assertIn("new-formal-analysis.md", self.explore)

    def test_existing_analysis_is_read_before_update(self) -> None:
        self.assertIn("read the current artifact and its evidence lineage", self.update)
        self.assertIn("choosing the latest file silently", self.update)

    def test_external_only_evidence_is_rejected(self) -> None:
        self.assertIn("parallel external analysis", self.evidence)
        self.assertIn("unique authoritative copy", self.evidence)

    def test_live_contract_beats_team_policy(self) -> None:
        self.assertIn("current lantide mcp tool schemas", self.skill)
        self.assertIn("team policy may make", self.skill)
        self.assertIn("must never broaden mcp permissions", self.skill)


if __name__ == "__main__":
    unittest.main()
