# AXIOMALITY：投资评估、原型与路演稿（2026-09-26）

| 路径 | 内容 |
|---|---|
| `01_投资备忘录_AXIOMALITY.md` | 投资备忘录第二版：结论、方向调整、原型结果、评分变化、90 天清单、英文摘要（不含融资） |
| `decks/AXIOMALITY_红杉版路演稿.pptx` | 中文红杉版，15 页，定位"具身数据，先验货，再付款" |
| `decks/AXIOMALITY_Seed_Deck_YC_a16z.pptx` | 英文 YC / a16z 版，13 页，"We inspect robot training data before labs pay for it" |
| `preview/*.pdf` | 两份 deck 的 PDF 预览（LibreOffice 渲染，以 PowerPoint 实际显示为准） |
| `prototype/` | 可运行的验收引擎与签名验收单：`python run_all.py`（v1 合成基准）、`python run_v2.py`（真实数据 + 含噪声基准 + 强基线） |
| `research/` | 原稿诊断、全球竞品、中国生态与政策、美国投资人视角、技术尽调 |
| `research/investor_reviews/` | 三轮模拟投资人评审（红杉、YC / a16z） |
| `original_text/` | 两份原稿全文导出 |
| `build/` | 生成两份 deck 的脚本：`npm i pptxgenjs react-icons react react-dom sharp` 后运行 `node build_cn.js` 与 `node build_us.js`，需要先运行原型以生成 `prototype/figures/` |
