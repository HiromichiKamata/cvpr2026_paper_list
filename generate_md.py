#!/usr/bin/env python3
"""
CVPR 2026 論文リスト Markdown ジェネレーター
JSON (enriched) を読み込んで Markdown を生成する。
レイアウトを変えたい場合はこのファイルだけ編集すればよい。

使い方:
    python3 generate_md.py                     # 全カテゴリ生成
    python3 generate_md.py video               # 動画生成のみ
    python3 generate_md.py image anime         # 複数指定
"""

import json
import os
import sys
from datetime import datetime

# ── カテゴリ定義 ──────────────────────────────────────────
CATEGORIES = {
    "video": {
        "json":  "video_gen_enriched.json",
        "out":   "cvpr2026_video_generation.md",
        "title": "Video Generation Papers",
    },
    "image": {
        "json":  "image_gen_enriched.json",
        "out":   "cvpr2026_image_generation.md",
        "title": "Image Generation Papers",
    },
    "anime": {
        "json":  "anime_enriched.json",
        "out":   "cvpr2026_anime.md",
        "title": "Anime / Illustration Domain Papers",
    },
}


# ── 1論文のMarkdownブロックを生成 ─────────────────────────
def paper_block(i: int, p: dict) -> str:
    lines = []

    # ---- 見出し ----
    lines.append(f"## {i}. {p['title']}\n")

    # ---- 和訳タイトル（あれば） ----
    if p.get("title_ja"):
        lines.append(f"> 🇯🇵 **{p['title_ja']}**\n")

    # ---- 一行まとめ（あれば） ----
    if p.get("summary_ja"):
        lines.append(f"> 💡 {p['summary_ja']}\n")

    # ---- 著者 ----
    if p.get("authors"):
        lines.append(f"**著者:** {', '.join(p['authors'])}\n")

    # ---- リンク ----
    links = []
    if p.get("paper_url"):
        links.append(f"[📄 Paper]({p['paper_url']})")
    if p.get("arxiv_url"):
        links.append(f"[📋 arXiv]({p['arxiv_url']})")
    if p.get("project_url"):
        links.append(f"[🌐 Project]({p['project_url']})")
    if links:
        lines.append(f"**Links:** {' | '.join(links)}\n")

    # ---- セッション ----
    if p.get("session"):
        lines.append(f"**Session:** {p['session']}\n")

    # ---- ポスター画像 ----
    if p.get("has_poster") and p.get("poster_local"):
        lines.append(f"\n![Poster]({p['poster_local']})\n")
    else:
        lines.append("\n> 🚫 Poster image not yet available\n")

    # ---- Project Page 折りたたみ（GitHubなど標準MDでは非対応だがObsidian/VSCode等で有効） ----
    if p.get("project_url"):
        lines.append(
            f"\n<details>\n<summary>🌐 Project Page プレビュー</summary>\n\n"
            f'<iframe src="{p["project_url"]}" width="100%" height="600" '
            f'loading="lazy" style="border:none;"></iframe>\n\n</details>\n'
        )

    # ---- Abstract ----
    if p.get("abstract"):
        lines.append(f"\n**Abstract:** {p['abstract']}\n")

    lines.append("\n---\n")
    return "\n".join(lines)


# ── カテゴリ全体のMarkdownを生成 ─────────────────────────
def generate(cat_key: str):
    cat = CATEGORIES[cat_key]
    json_path = cat["json"]

    if not os.path.exists(json_path):
        print(f"  [skip] {json_path} not found")
        return

    with open(json_path, encoding="utf-8") as f:
        papers = json.load(f)

    has_poster   = sum(1 for p in papers if p.get("has_poster"))
    has_project  = sum(1 for p in papers if p.get("project_url"))
    has_ja       = sum(1 for p in papers if p.get("title_ja"))

    lines = []
    lines.append(f"# CVPR 2026 — {cat['title']}\n")
    lines.append(
        f"**Total: {len(papers)} papers** | "
        f"Poster: {has_poster} | "
        f"Project page: {has_project} | "
        f"和訳済み: {has_ja}\n"
    )
    lines.append(f"*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}*\n")
    lines.append(
        f"> 📝 **データソース:** `{json_path}` — "
        "レイアウト変更は `generate_md.py` を編集後に再実行してください。\n"
    )
    lines.append("---\n")

    for i, p in enumerate(papers, 1):
        lines.append(paper_block(i, p))

    out_path = cat["out"]
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    size_kb = os.path.getsize(out_path) // 1024
    print(f"  ✅ {out_path} ({size_kb} KB, {len(papers)} papers)")


# ── エントリーポイント ─────────────────────────────────────
if __name__ == "__main__":
    targets = sys.argv[1:] if len(sys.argv) > 1 else list(CATEGORIES.keys())
    invalid = [t for t in targets if t not in CATEGORIES]
    if invalid:
        print(f"Unknown categories: {invalid}. Choose from: {list(CATEGORIES.keys())}")
        sys.exit(1)

    print(f"Generating Markdown for: {targets}")
    for cat_key in targets:
        generate(cat_key)
    print("Done.")
