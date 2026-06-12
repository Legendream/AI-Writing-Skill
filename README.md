# 公民科技知識庫：人機協同寫作 pipeline

這是「臺灣公民科技專案與工具行動指引」專案的人機協同寫作 pipeline，包含一套可複製的寫作流程（skill）、兩種文體的模板與範例。目標是降低「把知識整理成系統化文章」的門檻，讓社群貢獻者能照著流程，與 AI 協作產出格式一致、事實可查證、對 AI 檢索友善的公民科技文章。

## 內容物

```
civic-tech-writing-pipeline/
├── SKILL.md          寫作流程本體：文章類型、階段門檻、事實查核關卡、格式規範
├── templates/        兩種文體的模板（方法論長文、領域資源短文）
├── examples/         實際範例文章（陸續加入）
└── styles/           個人風格檔的說明與模板（風格可替換，流程共用）
```

## 怎麼使用

**在 Claude Code**：把 `civic-tech-writing-pipeline/` 資料夾複製到 `~/.claude/skills/`，之後提到「寫方法論文章」、「整理資源清單」等需求時會自動觸發。

**在 claude.ai 網頁版**：把 `SKILL.md` 的內容（或本 repo 的 raw 連結）貼進對話，再開始寫作。

**人與 AI 的分工**：人負責選題、提供素材、事實查核的最終把關與風格品味；AI 負責素材整理、大綱、初稿與格式查核。詳見 `SKILL.md`。

本 pipeline 以在 Claude 環境順暢運作為標準，不保證在其他 AI 工具上的使用體驗，但 `SKILL.md` 的流程與查核清單為工具中立的步驟，可供任何 AI 協作情境參照。

## 維護政策

（待補：交付驗收後確定）

## 授權

本 repo 內容以 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh-hant) 授權使用、修改與散布，使用時須標示：

> CC BY 4.0, by g0v jothon & Claire Cheng

授權範圍為本案交付驗收之版本（以 git tag 標記為準）。後續獨立開發之版本不在本次授權範圍內。
