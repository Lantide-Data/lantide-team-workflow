#!/usr/bin/env python3
"""驗證 Lantide Team Workflow 的結構與安全不變量。"""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = ROOT / "skills" / "lantide-team-workflow-default"
SKILL_FILE = SKILL_ROOT / "SKILL.md"
NAME = "lantide-team-workflow-default"
REQUIRED_TEAM_FILES = (
    "team-context.md",
    "usage-policy.md",
    "roles-and-review.md",
    "evidence-policy.md",
    "delivery-policy.md",
)
REQUIRED_WORKFLOW_FILES = (
    "new-formal-analysis.md",
    "update-existing-analysis.md",
    "exploration-to-formal.md",
)
FORBIDDEN_PATTERNS = {
    "待填 placeholder": re.compile(r"\[(?:TODO|TBD)\]|\b(?:TODO|TBD)\b", re.IGNORECASE),
    "bearer credential": re.compile(r"Authorization\s*:\s*Bearer\s+\S+", re.IGNORECASE),
    "macOS 使用者絕對路徑": re.compile(r"/Users/[^/\s]+/"),
    "Linux 使用者絕對路徑": re.compile(r"/home/[^/\s]+/"),
}


def fail(message: str) -> None:
    raise ValueError(message)


def read(path: Path) -> str:
    if not path.is_file():
        fail(f"缺少必要檔案：{path.relative_to(ROOT)}")
    text = path.read_text(encoding="utf-8")
    if not text.strip():
        fail(f"檔案不可為空：{path.relative_to(ROOT)}")
    return text


def parse_frontmatter(text: str) -> dict[str, str]:
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        fail("SKILL.md 必須從 YAML frontmatter 開始")
    try:
        end = lines.index("---", 1)
    except ValueError as error:
        raise ValueError("SKILL.md frontmatter 未結束") from error
    metadata: dict[str, str] = {}
    for line in lines[1:end]:
        if not line or line.startswith(" "):
            continue
        if ":" in line:
            key, value = line.split(":", 1)
            metadata[key.strip()] = value.strip().strip('"')
    return metadata


def validate_structure() -> None:
    skill = read(SKILL_FILE)
    metadata = parse_frontmatter(skill)
    if metadata.get("name") != NAME:
        fail(f"Skill name 必須是 {NAME}")
    description = metadata.get("description", "")
    if not description or len(description) > 60 or not description.endswith("."):
        fail("Skill description 必須是 60 字元內且以句號結尾")
    if "references/team/" not in skill or "Keep this file unchanged" not in skill:
        fail("SKILL.md 必須明示穩定核心與 team 客製化邊界")
    if "get_analysis_context" not in skill or "external_agent_playbook" not in skill:
        fail("SKILL.md 必須將 live Lantide context 與 Playbook 納入權威順序")

    overview = read(SKILL_ROOT / "references" / "00-lantide-overview.md")
    for url in (
        "https://lantidedata.com/en/docs",
        "https://lantidedata.com/en/what-is-lantide-data",
        "https://lantidedata.com/en/docs/user-guide/welcome",
    ):
        if url not in overview:
            fail(f"Lantide overview 缺少官方文件連結：{url}")

    connection = read(SKILL_ROOT / "references" / "01-connection-and-readiness.md")
    required_connection_rules = (
        "**First onboarding or an explicit request for a new connection:** open `lantidedata://agent-integration/pair?source=team-workflow`.",
        "**Existing connection fails:** open `lantidedata://agent-integration`.",
        "**User only wants to open, return to, or inspect Lantide:** open `lantidedata://open`.",
        "Use `action=configure` only for Codex.",
        "other clients must use the generic pairing route without that action",
    )
    for rule in required_connection_rules:
        if rule.lower() not in connection.lower():
            fail(f"connection reference 缺少完整 Desktop handoff 規則：{rule}")
    for phrase in (
        "not readiness evidence",
        "MCP initialization succeeds",
        "action=configure` only for Codex",
        "after explicit GUI approval",
        "runtime's available input",
        "treat it as a secret",
        "do not quote or summarize it",
        "command arguments",
        "repository",
        "ordinary logs",
        "without unnecessary disclosure",
        "client's own MCP settings",
    ):
        if phrase.lower() not in connection.lower():
            fail(f"connection reference 缺少安全或 readiness 規則：{phrase}")
    forbidden_connection_contracts = (
        "lantide status",
        "lantide start",
        "/usr/local/bin",
        "fixed backend port",
    )
    for phrase in forbidden_connection_contracts:
        if phrase.lower() in connection.lower():
            fail(f"connection reference 不得引入未支援的 launcher contract：{phrase}")

    team_root = SKILL_ROOT / "references" / "team"
    for name in REQUIRED_TEAM_FILES:
        text = read(team_root / name)
        for marker in ("Customization status: Default", "Safe to edit: Yes", "Required: Yes"):
            if marker not in text:
                fail(f"{name} 缺少客製化標記：{marker}")

    workflow_root = SKILL_ROOT / "references" / "workflows"
    for name in REQUIRED_WORKFLOW_FILES:
        text = read(workflow_root / name)
        for heading in ("## Use when", "## Procedure", "## Completion criteria"):
            if heading not in text:
                fail(f"{name} 缺少必要段落：{heading}")


def validate_content() -> None:
    checked_roots = (SKILL_ROOT, ROOT / "docs", ROOT / "examples")
    for checked_root in checked_roots:
        for path in sorted(checked_root.rglob("*")):
            if not path.is_file() or path.suffix not in {".md", ".yaml", ".yml"}:
                continue
            text = path.read_text(encoding="utf-8")
            for label, pattern in FORBIDDEN_PATTERNS.items():
                if pattern.search(text):
                    fail(f"{path.relative_to(ROOT)} 含有禁止內容：{label}")

    evidence = read(SKILL_ROOT / "references" / "team" / "evidence-policy.md")
    for phrase in ("one authoritative analysis line", "only location", "external computation"):
        if phrase.lower() not in evidence.lower():
            fail(f"預設 evidence policy 缺少核心規則：{phrase}")

    delivery = read(SKILL_ROOT / "references" / "team" / "delivery-policy.md")
    if "not the sole deliverable" not in delivery:
        fail("預設 delivery policy 必須禁止以 chat 作為唯一正式交付")


def main() -> int:
    validate_structure()
    validate_content()
    print(f"Validated {NAME}: 5 team policies and 3 workflows.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError) as error:
        print(f"validation failed: {error}", file=sys.stderr)
        raise SystemExit(1)
