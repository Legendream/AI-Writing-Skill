#!/usr/bin/env python3
"""從正本驗收條件清單產生「驗收員版」：濾掉給規則維護者看的立規緣由／修訂紀錄，
只留驗收員需要的操作型內容（PR #42 之後的延伸：實測顯示這些緣由對驗收覆蓋率
沒有幫助，見 docs/實驗_重複規則與驗收覆蓋率.md）。

用法：
    python3 checklists/generate_reviewer_version.py

正本裡用兩種機制標記「哪些留、哪些濾」：
1. 從 `## 給驗收者` 那一行開始才收錄（沿用既有的「貼給驗收者時，從分隔線開始貼」慣例，
   自動排除開頭的修訂紀錄與「給規則維護者」節）。
2. 這之後的每一行 `>` 開頭的引言區塊，預設濾掉；只有被
   `<!-- 驗收員可讀:開始 -->` ... `<!-- 驗收員可讀:結束 -->` 包住的引言區塊才保留
   （目前只有第 0 條的層級警示、K／L 節的發布前豁免說明這兩處是操作型內容，其餘都是
   給維護者看的立規緣由，被排除在標記之外）。

正本異動後，重新執行本腳本即可更新驗收員版，不要手動編輯輸出檔。
"""
import re
import sys
from pathlib import Path

CHECKLISTS_DIR = Path(__file__).parent

SOURCES = [
    ("驗收條件_領域資源指南.md", "驗收條件_領域資源指南_驗收員版.md"),
    ("驗收條件_方法論長文.md", "驗收條件_方法論長文_驗收員版.md"),
]

START_MARKER = "<!-- 驗收員可讀:開始 -->"
END_MARKER = "<!-- 驗收員可讀:結束 -->"


def generate(src_path: Path) -> str:
    lines = src_path.read_text(encoding="utf-8").splitlines()

    start_idx = None
    for i, line in enumerate(lines):
        if line.strip() == "## 給驗收者":
            start_idx = i
            break
    if start_idx is None:
        raise SystemExit(f"{src_path.name}：找不到「## 給驗收者」，無法判斷從哪裡開始收錄")

    kept = []
    keep_blockquote = False
    for line in lines[start_idx:]:
        stripped = line.strip()
        if stripped == START_MARKER:
            keep_blockquote = True
            continue
        if stripped == END_MARKER:
            keep_blockquote = False
            continue
        if stripped.startswith(">") and not keep_blockquote:
            continue
        kept.append(line)

    body = "\n".join(kept)
    body = re.sub(r"\n{3,}", "\n\n", body)

    title_line = next((l for l in lines if l.startswith("# ")), "# 驗收條件")
    header = (
        f"{title_line} — 驗收員版\n\n"
        f"> ⚙️ **本檔自動產生，不要手動編輯。** 由 `checklists/{src_path.name}` 透過 "
        f"`checklists/generate_reviewer_version.py` 產生，濾掉了給規則維護者看的立規緣由\n"
        f"> 與修訂紀錄（實測顯示這些對驗收覆蓋率沒有幫助，見 "
        f"`docs/實驗_重複規則與驗收覆蓋率.md`），只留驗收員需要的操作型內容。\n"
        f"> 正本異動後，重新執行產生腳本即可更新本檔。\n\n---\n\n"
    )
    return header + body.strip() + "\n"


def main():
    for src_name, out_name in SOURCES:
        src_path = CHECKLISTS_DIR / src_name
        out_path = CHECKLISTS_DIR / out_name
        content = generate(src_path)
        out_path.write_text(content, encoding="utf-8")
        print(f"已產生 {out_path.relative_to(CHECKLISTS_DIR.parent.parent)}"
              f"（{len(content.splitlines())} 行，正本 {len(src_path.read_text(encoding='utf-8').splitlines())} 行）")


if __name__ == "__main__":
    sys.exit(main())
