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
        cls.connection = (SKILL_ROOT / "references/01-connection-and-readiness.md").read_text(encoding="utf-8").lower()
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

    def test_existing_connection_is_tried_before_desktop_handoff(self) -> None:
        self.assertIn("try the existing mcp connection first", self.connection)
        self.assertIn("get_analysis_context", self.connection)

    def test_first_onboarding_uses_pairing_handoff(self) -> None:
        self.assertIn("lantidedata://agent-integration/pair", self.connection)
        self.assertIn("source=team-workflow", self.connection)
        self.assertIn("wait for the user", self.connection)

    def test_existing_connection_failure_opens_management_without_new_profile(self) -> None:
        recovery_rule = "**existing connection fails:** open `lantidedata://agent-integration`."
        self.assertIn(recovery_rule, self.connection)
        self.assertIn("do not infer", self.connection)
        self.assertIn("do not create a replacement profile", self.connection)

    def test_daily_open_does_not_start_pairing(self) -> None:
        daily_open_rule = (
            "**user only wants to open, return to, or inspect lantide:** "
            "open `lantidedata://open`. do not use the pairing route"
        )
        self.assertIn(daily_open_rule, self.connection)

    def test_only_codex_uses_configure_action(self) -> None:
        configure_rule = "use `action=configure` only for codex"
        fallback_rule = "other clients must use the generic pairing route without that action"
        self.assertIn(configure_rule, self.connection)
        self.assertIn(fallback_rule, self.connection)

    def test_web_only_and_protocol_failure_have_manual_fallbacks(self) -> None:
        self.assertIn("web-only", self.connection)
        self.assertIn("do not claim that the app opened", self.connection)
        self.assertIn("do not scan", self.connection)
        self.assertIn("manual fallback", self.connection)

    def test_credentials_stay_out_of_chat_argv_repo_and_logs(self) -> None:
        for phrase in ("ordinary chat", "command arguments", "repository", "ordinary logs"):
            self.assertIn(phrase, self.connection)

    def test_retry_is_bounded_and_respects_client_reload(self) -> None:
        self.assertIn("at most three", self.connection)
        self.assertIn("2 seconds, 4 seconds, then 8 seconds", self.connection)
        self.assertIn("restart or a new session", self.connection)
        self.assertIn("do not poll", self.connection)

    def test_deep_link_is_not_readiness_evidence(self) -> None:
        self.assertIn("not readiness evidence", self.connection)
        self.assertIn("mcp initialization succeeds", self.connection)

    def test_cancelled_pairing_stops_without_reopening(self) -> None:
        self.assertIn("cancels pairing", self.connection)
        self.assertIn("do not reopen the deep link", self.connection)


if __name__ == "__main__":
    unittest.main()
