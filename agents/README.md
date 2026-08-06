# agents／選配加值（Claude Code 專用）

**這個資料夾是加分項，不是必需品。** 沒有這裡的東西，`civic-tech-writing-pipeline`
一樣完整可用——所有流程與檢查都能用對話工具或人工完成。

會用到這裡的人：使用 Claude Code（或其他支援「子代理」的環境），想把交付前的獨立驗收自動化。

---

## 為什麼是「選配」而不是核心

本 skill 的核心資產是**驗收條件清單**（[`../civic-tech-writing-pipeline/checklists/`](../civic-tech-writing-pipeline/checklists/)），
不是代理本身。

驗收之所以有效，是因為條件寫得夠具體，而不是因為代理多聰明——
同一個代理，如果只跟它說「幫我看看這篇好不好」，回來的東西會軟綿綿的。

所以：**清單是共通底盤，代理只是執行它的其中一種方式。**
這樣設計，用 ChatGPT 的人開個新對話貼清單就能拿到大部分效果，不會因為沒有 Claude Code 而拿到殘缺版。

---

## 內容

| 檔案 | 用途 |
|---|---|
| [article-reviewer.md](article-reviewer.md) | 文章獨立驗收員的代理定義 |

## 安裝

複製到你的 Claude Code 代理目錄：

```bash
cp agents/article-reviewer.md ~/.claude/agents/
```

或放在專案的 `.claude/agents/` 底下，只在該專案生效。

## 使用

派工時**只給兩樣東西**：

1. 對應文體的驗收條件（`checklists/` 底下那兩份的內容）
2. 文章的檔案路徑

⚠️ **絕對不要給它產出過程、討論脈絡或你的思路。** 一旦它知道你為什麼那樣寫，
它就會開始替你辯護，而不是挑錯。這是整個機制唯一的關鍵。
