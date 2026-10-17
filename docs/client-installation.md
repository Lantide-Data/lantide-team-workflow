# Client 安裝方式

這個 repo 發布標準 Agent Skill 目錄，但不同 client 的搜尋路徑、安裝命令與重新載入方式可能不同。優先使用 client 官方支援的 plugin／skill 安裝機制。

## 標準來源與安裝單位

官方來源固定為：

```text
repository: https://github.com/Lantide-Data/lantide-team-workflow
path: skills/lantide-team-workflow-default
skill name: lantide-team-workflow-default
ref: main（開始下載前解析為完整 commit SHA）
```

供支援 GitHub 子目錄來源的 client 安裝器使用的入口：

<https://github.com/Lantide-Data/lantide-team-workflow/tree/main/skills/lantide-team-workflow-default>

安裝的最小單位是完整的 `skills/lantide-team-workflow-default/`，包含 `SKILL.md`、`references/`、`agents/` 與 `LICENSE`。保留所有相對路徑，安裝結果為 `<client skill directory>/lantide-team-workflow-default/SKILL.md`，不要多包一層 repo 或 `skills/`，也不要只下載 `SKILL.md`。

一般安裝只拉取這個子目錄的檔案，不 clone 整個 repo、不下載整包 repo ZIP，也不拉取 repo 的 `docs/`、`examples/`、`tests/` 或 Git history。維護者開發與企業 fork 不受這項安裝慣例限制。

## 標準拉取方式

1. 優先使用目前 client 已有、且支援指定 repo 子目錄的官方安裝器，傳入上述 repository 與 path。若安裝器只能下載整個 repo，改採下述子目錄下載方式。不要為了安裝此 Skill 額外安裝第三方套件管理器。
2. 沒有適用安裝器時，使用 GitHub REST API 解析 ref，再列出並下載 skill 子目錄。所有目錄與檔案請求必須固定到同一個 commit SHA，避免下載期間 `main` 更新造成版本混用。
3. 先下載到暫存目錄，保留完整相對路徑；確認檔案齊全、`SKILL.md` 的 name 正確且 references 可解析後，才安裝到 client 的 skill 目錄。
4. 目的地依目前 client 官方規範與使用者指定的 user／project scope 決定，不能套用其他 client 的路徑。安裝時記錄 repository、path、完整 commit SHA 與目的地；若安裝器已有來源記錄機制，沿用該機制。
5. 同名目錄已存在時先辨識版本及本機客製化，避免直接覆寫；同一版本且內容相同可直接視為已安裝。下載失敗或不完整時保留現有安裝，不留下半套 Skill。

GitHub API 的讀取順序如下；`COMMIT_SHA` 是第一步回傳的完整 `sha`，不是固定寫死的版本：

```text
GET https://api.github.com/repos/Lantide-Data/lantide-team-workflow/commits/main
GET https://api.github.com/repos/Lantide-Data/lantide-team-workflow/contents/skills/lantide-team-workflow-default?ref=COMMIT_SHA
```

對回傳的每個子目錄，以相同 `ref=COMMIT_SHA` 遞迴列出內容，再下載該 commit 下的每個一般檔案。Contents API 的 `download_url` 應即時取得，不作為永久安裝來源保存。只接受指定 skill 子目錄內的檔案，不跟隨 symlink、submodule 或路徑越界。Contents API 可能解參照 symlink，因此自訂下載器還需用同一 commit 的 Git Trees metadata 核對檔案 mode，只接受一般檔案（`100644`／`100755`）；遇到無法完整列舉、限流或下載錯誤時回報失敗，不悄悄退回整包下載。

這是公開 repo，正常讀取不需 credential。API 行為依 [GitHub Contents API](https://docs.github.com/en/rest/repos/contents#get-repository-content) 與 [Commits API](https://docs.github.com/en/rest/commits/commits#get-a-commit) 為準。

## 安裝完成與驗證

1. 依 client 能力重新載入 skills、建立新 Agent session 或重新啟動 client。
2. 詢問 Agent「哪些任務會觸發 Lantide team workflow」，確認它能讀到 usage policy。檔案已下載不等於目前 session 已載入。
3. 優先使用既有 Lantide MCP connection；尚未連線才進行下方 handoff。Skill 本身不包含或建立 credential。

## Desktop handoff

支援新版 handoff contract 的 Lantide Desktop 定義三個 provider-neutral deep link；它們只負責請求啟動／聚焦 App 與開啟對應 UI，不代表 MCP 已 ready。正式安裝包的可用性仍依 Desktop 發布版本與平台驗證結果為準：

- `lantidedata://agent-integration/pair?source=team-workflow`：首次配對或明確建立新 connection。
- `lantidedata://agent-integration`：既有 connection 失敗時開啟管理頁。
- `lantidedata://open`：單純開啟或切回 Lantide，不進入配對。

Codex 可在 GUI 核准的前提下使用 `client=codex&action=configure`；其他 client 使用通用 pairing，再依其官方 MCP 設定方式完成安裝。配對完成、修改設定，或既有 connection 在當前 session 仍不可用時，依 client 能力重載 MCP；不支援即時重載則重新啟動 client 或建立新 session，再重新載入 Skill 與 MCP connection。不要把單一 Agent 回報的失敗字樣寫死成診斷。

若 deep link 無法開啟，使用人工 fallback：開啟 **Lantide Data → Agent Integration**。Web-only client 只能提供連結或操作指引，不得宣稱已啟動本機 App。

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
