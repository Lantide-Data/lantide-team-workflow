# Client 安裝方式

這個 repo 發布標準 Agent Skill 目錄，但不同 client 的搜尋路徑、安裝命令與重新載入方式可能不同。優先使用 client 官方支援的 plugin／skill 安裝機制。

## 通用安裝

安裝的最小單位是：

```text
skills/lantide-team-workflow-default/
```

該目錄必須保持完整，包含 `SKILL.md`、`references/` 與 client 可選用的 `agents/` metadata。不要只複製 `SKILL.md`，否則工作流和團隊政策無法載入。

## 建議流程

1. 將 repo clone 或下載到受信任的位置。
2. 使用 client 的官方方法，安裝或連結 `lantide-team-workflow-default` 目錄。
3. 重新啟動或建立新 Agent session，讓 client 重新掃描 skills。
4. 詢問 Agent「哪些任務會觸發 Lantide team workflow」，確認它能讀到 usage policy。
5. 再建立 Lantide MCP connection。Skill 本身不包含或建立 credential。

## Client-specific 注意事項

- **Codex／OpenAI plugin surface**：可使用 `agents/openai.yaml` 作為顯示與 starter prompt metadata；以當前官方 plugin 文件為準。
- **Claude Code、Cursor、Hermes 或其他 Agent**：安裝到該 client 宣告的 user 或 project skill 目錄；不要假設其他 client 使用 Codex 的路徑。
- 若 client 不支援 Agent Skills，仍可把 repo 當作團隊操作規範，但無法保證自動觸發或漸進載入。

## 更新

更新後通常要開新 session 才會載入新版。企業 fork 應先依 `customization-guide.md` 保留 `references/team/`，再合併上游變更並執行驗證。

## 安全

- 不把 Lantide bearer credential 寫入 Skill、安裝腳本或環境範例。
- 不以未知來源腳本修改 Agent 的全域設定。
- 不讓安裝 Skill 被誤解為授予 Lantide Admin 權限。
- MCP 配對仍由使用者在 Lantide Agent Integration 中確認。
