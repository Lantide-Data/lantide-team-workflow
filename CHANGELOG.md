# Changelog

本專案依語意化版本管理預設 Skill。

## Unreleased

- 將 client MCP reload／restart 從首次配對步驟提升為通用就緒規則：Desktop handoff 之後仍以當前 Agent 的 MCP 可用性為準，不把單一錯誤字樣寫死成診斷。

## 0.2.0

- 加入 provider-neutral Lantide Desktop deep-link handoff 流程與未支援版本的人工 fallback。
- 區分首次 pairing、既有 connection 管理與單純開啟 App。
- 加入 bounded retry、client reload、web-only fallback 與 credential handling 規則。
- 加入 onboarding、故障恢復與安全邊界的 golden scenarios。

## 0.1.0

- 建立可直接使用的 `lantide-team-workflow-default`。
- 分離穩定主文件、五份團隊政策與三種分析工作流。
- 提供企業客製化、導入、設計與 client 安裝指南。
- 加入結構、內容與行為驗收。
