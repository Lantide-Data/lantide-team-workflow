# 團隊導入指南

## 建議試點

選擇一個同時具備以下條件的案例：有真實決策問題、資料可在 Lantide 存取、需要至少一位審閱者、成果未來可能更新。不要先選只有簡單計算的案例，也不要以最高敏感資料作為第一次測試。

## 導入步驟

1. **確認角色**：指定 requester、analysis owner、Plan reviewer、Report approver 與 platform administrator。
2. **安裝預設 Skill**：先不客製化，完成一個案例，觀察預設分類與工作流是否適合。
3. **建立連線**：由使用者在 Lantide Agent Integration 確認 scope 與 access mode；credential 不進聊天或 repo。
4. **執行三種代表情境**：新正式分析、既有分析更新、探索後正式化至少各演練一次。
5. **回看成果**：檢查 Plan、正式執行步驟、evidence、Report、limitations 與 Activity，而不是只評估 Agent 回答是否流暢。
6. **客製化政策**：只修改實際出現差異的 `references/team/` 文件。
7. **建立治理節奏**：指定政策 owner，定期檢查 Skill 是否仍符合團隊工作方式與 Lantide live contract。

## 驗收指標

- 適合一次性回答的問題沒有被強迫建立正式流程。
- 影響決策的真實數字沒有只留在聊天中。
- 探索結果在發布前已正式化或明確標示限制。
- 既有分析更新前會先讀取明確 artifact 和 lineage。
- 使用者知道誰負責 Plan review 與 Report acceptance。
- Agent 遇到未知企業政策時會詢問，而不是自行補齊。

## 失敗訊號

- 團隊把 `SKILL.md` 當成另一份完整產品手冊持續堆內容。
- 每個問題都建立新 Project 或 Plan。
- Agent 在外部工具完成分析，只把結論貼回 Lantide。
- Admin 被視為可略過 Plan、證據或審閱。
- Report 與聊天摘要對同一指標出現不同定義或數字。
