# 企業客製化指南

本指南的目標是讓企業調整工作規範，同時保持 Skill 的執行核心可安全升級。

## 原則

- 不需要客製化也能直接使用預設版。
- 一般情況不要修改 `skills/lantide-team-workflow-default/SKILL.md`。
- 只在 `references/team/` 寫組織政策，不複製 MCP tool schema 或 Playbook。
- 未定義的企業政策必須由 Agent 詢問，不用 placeholder 或猜測補齊。
- 團隊政策可增加限制，不可放寬 live Lantide 權限與審批。

## 建議順序

### 1. `team-context.md`

填入團隊、常見決策、資料來源、交付形式與敏感資料邊界。不要寫 token、內網 credential、個人資料樣本或機器路徑。

### 2. `usage-policy.md`

調整「必須使用／建議使用／可不使用」條件。規則應以風險和成果用途描述，例如「對外發布的指標必須正式化」，不要依賴某位成員記得口頭慣例。

### 3. `roles-and-review.md`

將 Requester、Analysis owner、Plan reviewer、Report approver、Platform administrator 對應到實際角色。若有職責分離或雙人覆核，在此加入。

### 4. `evidence-policy.md`

加入允許或禁止的外部運算環境、敏感欄位規則、最低驗證項目與保存政策。保留「單一權威分析線」和「不得用聊天補造證據」兩項預設。

### 5. `delivery-policy.md`

定義必要格式、模板、品牌、無障礙要求、核准人與外部目的地。明確區分「分析完成」與「已被核准發布」。

## 何時才修改工作流文件

只有企業真的改變程序時才修改 `references/workflows/`，例如法規要求每個正式分析都經第二人驗證。若只是換角色名稱、提高證據標準或限制發布位置，應修改 `references/team/`。

## 何時才修改 `SKILL.md`

只有以下情況需要修改：

- 新增第四種任務類型，且無法由現有三種工作流表達；
- 改變所有任務都必須遵守的載入順序；
- 改變 live contract 與團隊政策的權威關係；
- 新增跨所有企業版本都適用的完成檢查。

修改後應提高 Skill 版本並重新執行全部驗證。

## Upstream 更新

建議企業 fork 保留預設檔案路徑。更新時：

1. 先保留 `references/team/` 的企業版本。
2. 合併上游 `SKILL.md`、通用 references、workflows、validator 與文件。
3. 檢查上游是否新增團隊政策欄位，再人工整合到企業文件。
4. 執行 validator 與測試。
5. 用至少三個既有企業案例回歸，不以 YAML 驗證通過代替行為驗收。
