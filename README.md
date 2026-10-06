# Lantide Team Workflow

A ready-to-use, enterprise-customizable Agent Skill that helps teams decide when to use Lantide Data, keeping every formal analysis — Plan, execution evidence, Report, and constraints — on a single auditable workflow.

The default skill is `lantide-team-workflow-default`. Even with zero modifications, it addresses three common problems: over-engineering one-off questions, mistaking exploration numbers for formal evidence, and leaving formal deliverables stranded in external agent chats or temp files.

---

# Lantide Team Workflow

這是一套可直接使用、也可由企業客製化的 Agent Skill，協助團隊判斷何時使用 Lantide Data，並讓正式分析的 Plan、執行證據、Report 與限制維持在同一條可審閱的工作流中。

預設 Skill 是 `lantide-team-workflow-default`。即使不修改任何內容，它也會改善三個常見問題：避免把一次性問題過度流程化、避免把探索數字誤當正式證據、避免正式成果只留在外部 Agent 對話或暫存檔。

## Repo 結構

```text
skills/lantide-team-workflow-default/
├── SKILL.md                         # 穩定入口，通常不要修改
├── agents/openai.yaml               # OpenAI 顯示資訊
└── references/
    ├── 00-lantide-overview.md       # Lantide 心智與官網文件入口
    ├── 01-connection-and-readiness.md
    ├── team/                        # 企業主要客製化區
    └── workflows/                   # 三種預設分析工作流
```

## 直接使用

將 `skills/lantide-team-workflow-default/` 安裝到支援 Agent Skills 的本機 Agent。實際目錄與重新載入方式依 client 而異，見 [`docs/client-installation.md`](docs/client-installation.md)。

這份 Skill 不包含 MCP credential，也不會自行取得 Lantide 權限。Lantide Desktop、Agent Integration 與 live MCP context 仍是連線和執行能力的來源。

## 企業客製化

一般客製化只修改下列五份文件；不要先修改 `SKILL.md`：

| 想調整的內容 | 文件 |
| --- | --- |
| 團隊背景、資料類型與使用目的 | `references/team/team-context.md` |
| 哪些工作必須、建議或不必使用 Lantide | `references/team/usage-policy.md` |
| 誰確認口徑、審 Plan 與接受 Report | `references/team/roles-and-review.md` |
| 正式證據要留在哪裡、外部運算如何回綁 | `references/team/evidence-policy.md` |
| 哪種產物才算完成、如何對外交付 | `references/team/delivery-policy.md` |

完整步驟見 [`docs/customization-guide.md`](docs/customization-guide.md)，可參考 [`examples/`](examples/) 的情境差異。

## 預設工作流

- **New formal analysis**：新的問題、指標、資料邊界或正式交付。
- **Update existing analysis**：更新、重現或修訂明確的既有 artifact。
- **Exploration to formal**：先降低不確定性，只有在結果需要引用、決策或交付時才正式化。

## 設計邊界

優先級由高到低為：live tool schema／structured error、`get_analysis_context`、live External Agent Playbook、Lantide runtime skills、團隊政策、通用預設。團隊政策可以更嚴格，但不能放寬 Lantide 權限、略過審批或取代 runtime contract。

## 驗證

需要 Python 3.9 以上，不需第三方套件：

```bash
python3 scripts/validate.py
python3 -m unittest discover -s tests -p 'test_*.py'
```

## 文件

- [客製化指南](docs/customization-guide.md)
- [導入指南](docs/adoption-guide.md)
- [設計原則](docs/design-principles.md)
- [Client 安裝方式](docs/client-installation.md)
- [Lantide 官方文件](https://lantidedata.com/en/docs)

## License

[MIT](LICENSE) © 2026 Lantide Data