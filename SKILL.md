# 你找的 SKILL.md 不在這裡

**流程本體在 [`civic-tech-writing-pipeline/SKILL.md`](civic-tech-writing-pipeline/SKILL.md)。**

這個檔案只是路標。整個 `civic-tech-writing-pipeline/` 資料夾才是交付主體——
要用這套 skill，複製那個資料夾，不是複製這個檔案。

## 給接手的 AI

如果你是被交接來執行這套寫作流程的 AI，請照這個順序讀：

1. [`civic-tech-writing-pipeline/SKILL.md`](civic-tech-writing-pipeline/SKILL.md)　流程本體，先讀「文章類型」與「開始前必問」
2. [`civic-tech-writing-pipeline/templates/`](civic-tech-writing-pipeline/templates/)　選定類型後複製對應模板
3. [`civic-tech-writing-pipeline/checklists/`](civic-tech-writing-pipeline/checklists/)　交付前的驗收條件，寫之前先看一遍
4. [`civic-tech-writing-pipeline/發布指引.md`](civic-tech-writing-pipeline/發布指引.md)　發布前才需要

其餘說明見 [`README.md`](README.md)。

> 為什麼有這個檔案：一次跨平台可攜性測試中，交接指令口述的入口是
> `AI-Writing-Skill/SKILL.md`（少了中間一層資料夾），接手的 AI 在根目錄找不到
> `SKILL.md` 而卡住。執行該次測試的平台自評這是「可攜性風險最高的一點」。
> 說明文件其實寫對了路徑，但**沒有人保證接手的 AI 會先讀說明文件**——
> 所以在它一定會找的位置放一個路標，比把路徑寫得更清楚有效。
> 緣由見 [`docs/可攜性測試診斷_2026-08-18.md`](docs/可攜性測試診斷_2026-08-18.md)。
