# AXIOMALITY 投资评估与改稿（2026-09-25）

| 文件 | 内容 |
|---|---|
| `01_投资备忘录_AXIOMALITY.md` | 双视角（红杉中国 / YC·a16z）投资备忘录：结论、逐维度评分、事实核实、尖锐问题、改稿说明、待核实清单、英文摘要 |
| `decks/AXIOMALITY_红杉版_PreA路演稿.pptx` | 新中文版，16 页（原稿 42 页） |
| `decks/AXIOMALITY_Seed_Deck_YC_a16z.pptx` | 新英文版，13 页（原稿 46 页） |
| `preview/*.pdf` | 两份新 deck 的 PDF 预览（LibreOffice 渲染，字体以 PowerPoint 实际显示为准） |
| `research/00_deck_critique.md` | 原稿结构诊断 |
| `research/01_global_competitors.md` | 全球竞品与稀缺性（约 85 条来源） |
| `research/02_china_ecosystem.md` | 中国生态、政策标准核实、红杉口味 |
| `research/03_us_investor_lens.md` | 欧盟 / 美国法规核实、YC/a16z 视角、可比公司估值 |
| `research/04_technical_dd.md` | 技术尽调：TUpper / COLORE 核实、先例、十项风险、三个建议 demo |
| `original_text/` | 两份原稿的全文导出（markdown） |
| `build/` | 生成两份 deck 的 pptxgenjs 脚本（`npm i pptxgenjs react-icons react react-dom sharp` 后 `node build_cn.js` / `node build_us.js`；脚本默认从 `../src/media_cn/cover_crop.png` 读封面图，可改为同目录） |

研究方法说明：四份研究报告由并行 agent 通过网页检索完成，容器出口代理封锁了大部分中文站点正文，事实主要来自检索摘要；每条关键事实附 URL，报告内标注了"未核实"条目。
