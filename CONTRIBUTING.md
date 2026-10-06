# 貢獻指南

## 修改範圍

- 通用行為修改放在 `SKILL.md`、通用 references 或 workflows，必須適用於未客製化的團隊。
- 組織示例放在 `examples/`，不要把特定公司政策加入預設 Skill。
- Tool schema、Playbook 或產品文件不要複製進 repo；使用 live contract 或官方連結。
- 使用者可見的 Skill 內容使用英文；repo 維護文件與程式註解使用繁體中文。

## 驗證

```bash
python3 scripts/validate.py
python3 -m unittest discover -s tests -p 'test_*.py'
```

每個行為修改至少增加或調整一個驗收情境。不得提交 credential、真實客戶資料、內網 URL、機器絕對路徑或分析結果。

## Commit

使用 Conventional Commits，subject 與 body 使用繁體中文：

```text
feat(workflow): 新增團隊分析工作流預設

- 補上具體變更
- 記錄驗證結果
```
