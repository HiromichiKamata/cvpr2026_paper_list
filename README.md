# CVPR 2026 Paper List

CVPR 2026 の論文を動画生成・画像生成・アニメ/イラストの3カテゴリに分類し、ポスター画像・日本語タイトル訳・一行まとめを含む閲覧用ビューアーです。

## 🔗 公開ページ

**[→ GitHub Pages で見る](https://hiromichiKamata.github.io/cvpr2026_paper_list/viewer.html)**

## カテゴリ

| カテゴリ | 件数 |
|---------|------|
| 動画生成 | 220件 |
| 画像生成 | 333件 |
| アニメ/イラスト | 54件 |
| **合計** | **607件** |

## ファイル構成

```
viewer.html              # メインビューアー（JSONをfetchして動的レンダリング）
video_gen_enriched.json  # 動画生成論文データ（220件）
image_gen_enriched.json  # 画像生成論文データ（333件）
anime_enriched.json      # アニメ/イラスト論文データ（54件）
generate_md.py           # Markdown生成スクリプト
cvpr2026_video_generation.md  # 動画生成 Markdown
cvpr2026_image_generation.md  # 画像生成 Markdown
cvpr2026_anime.md             # アニメ/イラスト Markdown
```

## viewer.html の機能

- カテゴリタブ切り替え（動画 / 画像 / アニメ）
- キーワード検索
- Cards / Table ビュー切り替え
- ポスター画像表示（CVPRサイトから取得）
- 日本語タイトル訳・一行まとめ表示
- Project Page リンク・iframe展開

## ローカルで使う場合

```bash
python3 -m http.server 8000
# → http://localhost:8000/viewer.html
```

## データソース

- [CVPR 2026 Virtual Site](https://cvpr.thecvf.com/virtual/2026/papers.html)
- [Open Access CVPR 2026](https://openaccess.thecvf.com/CVPR2026?day=all)
