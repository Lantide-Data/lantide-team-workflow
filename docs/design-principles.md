# 設計原則

## 預設即可使用

預設政策必須做出有用判斷，而不是要求企業先填完模板。未知的企業特定事實才詢問使用者；通用的 evidence、review 與 delivery 底線直接生效。

## 穩定核心與可變政策分離

`SKILL.md` 負責觸發、載入、權威順序與跨任務不變量。`references/team/` 負責組織背景、使用門檻、角色、證據和交付。這可降低企業客製化時破壞執行流程的風險。

## Skill 不複製 runtime contract

工具名稱、參數、access-mode 能力與 Lantide workflow 會演進。Skill 只保留穩定導航，並以 live MCP context、Playbook、runtime skills、tool schema 與 structured errors為準。

## 方法不等於狀態

Skill 保存團隊希望 Agent 如何工作；實際 Plan、SQL、結果、審閱、Report 與限制保存在 Lantide。不得把特定分析結果寫入本 repo 當成延續機制。

## 一條權威分析線

正式問題應在 Lantide 維持一條可追溯的工作線。外部聊天可以協作，但不能成為唯一 evidence。必要的外部運算要回綁並揭露 lineage 中斷。

## 漸進式載入

Agent先讀分類所需的最少文件，再依連線、角色、證據、交付與工作流需要載入其他 reference。不要每次把所有企業政策與三套工作流全部塞入 context。

## 政策只能更嚴格

團隊 Skill 不是授權機制。企業規則可增加審閱與證據要求，但不能繞過 MCP access mode、Plan lifecycle、approval 或安全限制。
