# AXIOMALITY 投资备忘录（双视角：红杉中国 / YC·a16z）

日期：2026-09-25　基础材料：《具身智能的数据闭环》（中文，42 页）、《Engineering the evidence layer》（英文，46 页）　外部研究：四份专题报告（全球竞品、中国生态与政策、美国投资人视角与法规核实、技术尽调），见 `research/` 目录。

> 说明：用户提到的"md 里的外界公司"在仓库与上传件中均未找到（仓库只有一个空 README）。竞品对照全部来自我自己组织的研究，覆盖了原稿竞争页提到的所有公司并补充了 20 余家。

---

## 0. 一页结论

| | 红杉中国（HongShan） | YC / a16z |
|---|---|---|
| **今天会不会投** | **不会**（会见、会跟踪） | **YC：不会，除非改叙事 + 有 demo；a16z：不会**（种子期不投合规叙事的基础设施） |
| **原因** | 零客户绑定；引擎未内测；叙事是"研讨稿 + 标准卡位"，而红杉 2025–26 在具身只投"大脑 + 有量产客户的本体"，数据基础设施零公开出手 | 市场自己框在 $12–60M；why-now 押在 2028 年欧盟法规上；46 页且几乎每页自我否定；没有 design partner、没有 demo |
| **补上什么就能投** | (1) 一家训练场 / 数采龙头 / 拟上市整机厂的付费 PoC，给出"带护照 vs 不带护照"的成交价或验收周期对照；(2) 护照嵌入 CR-3-06 或信通院评价方法成为默认输出格式，并在北数所具身数据跨境流通平台完成首批登记；(3) 补一位中国产业侧联合创始人 | (1) 公开的盲测基准：注入错误 → 对比"规则 + VLM"基线，公布逐类查全率；(2) 两家具名 design partner（数据供应商或 OEM）和 $0.5–1M 的合同 / 计量流量；(3) 一句话定位与 13 页 deck；(4) 一位训练过 VLA 的科学家 |
| **改稿后能到什么水平** | 从"研讨稿"到"可进 IC 的 Pre-A 路演稿"；能否"一定投"取决于 90 天内三件承诺兑现（见第 7 节） | 从"技术白皮书"到"YC 面试可用、a16z 首会可用"的种子稿；能否拿 term sheet 取决于基准结果与 design partner |
| **我的综合判断** | **值得投的是人和方向，不是当前状态。** 创始人是全球少数能写 ISO 顶层本体公理并做机器一致性证明的人，"具身数据的证据层"在中美都是空白品类。但公司现在处于"有资产、无产品、无客户"的状态，估值应按种子 / Pre-A 定价，不应按 deck 里 2030 年 2.2 亿收入定价。 | |

---

## 1. 这家公司到底在做什么（用投资人的语言）

一句话：**机器人训练数据的"质检 + 认证"层。** 任何格式的机器人数据进来，引擎逐条判定"通过 / 修复 / 拒判"并给出依据，最后签发一张可离线验证的"数据护照"。同一套形式化规则库还能编译成机器人运行时的语义护栏。

类比（各有帮助与伤害）：
- **"Applied Intuition 的验证套件独立成一家公司"**：Applied Intuition 估值 $15B（2025-06），2026-07 发布面向机器人的 Dana 平台——说明"物理 AI 验证软件"是高倍数品类，但也说明巨头已在做。
- **"Foretellix for robot learning"**：覆盖驱动验证，NVIDIA / 丰田选择投资而非自建——但 Foretellix 8 年只融了 $135M，2026 年因"验证工具需求慢于预期"裁员 18%。
- **"Vanta for robot data"**：SOC 2 报告是买方要求的徽章，Vanta $4.15B、$300M ARR——但 SOC 2 有买方刚需，机器人数据护照目前没有。

---

## 2. 逐维度评分（1–5 分，中国 / 美国分列）

| 维度 | 中国 | 美国 | 依据 |
|---|---|---|---|
| **产品逻辑** | 3 | 3 | 输入 → 引擎 → 护照的产品定义清晰，字段设计成熟（覆盖度 / 物理 / 逻辑 / 不确定度 / 血缘 / 真仿比例 / 监管映射）。问题：证书的价值取决于"谁认"，而目前没人认；四条收入线（护栏、证据、引擎、评测）过散。正确的楔子是先卖"找出坏数据"的工具价值，证书作为副产品累积公信力。 |
| **稀缺性** | 4 | 3.5 | 全球（含中国）**没有任何公司在卖逐条、签名、机器可校验的机器人数据证书**（四份研究一致结论）。人是最稀缺的：TUpper / COLORE 血统的形式化本体专家 + 做过 5,000 万美元收入的经营者。但组件在商品化：NVIDIA Cosmos Evaluator 免费给生成数据打物理合理性分（2026-03），C2PA / 数据溯源标准已存在，韩国 Pebblous 已在卖物理 AI 数据的诊断与认证。最可能加这个功能的是 NVIDIA（Evaluator + Halos 检测实验室），其次 Applied Intuition、Hugging Face。 |
| **可行性（技术）** | 3 | 3 | MVP（模式 / 几何 / 时序 / 语义检查 + 血缘 + 签名）6 个月可做。高风险：VLM 接地"一致但错误"无法被公理发现；物理残差需要力矩与接触力，DROID / LeRobot 主流数据集没有，"物理通过率 99.1%"实际上是运动学数字；SMT 在一阶公理上不可判定，需限制到有界场景图的 EPR 片段并公开 unknown 比例。 |
| **可行性（商业）** | 2.5 | 2 | 中国：标准全部是推荐 / 指导性，无强制合规触发点；国地中心、京东、智元都有内部"评 / 测"，自建质检是主要替代；信通院、CESI、机器人检测认证联盟把"认证"视为自己的地盘，2026 Q4 大概率推评测发证。美国：PI / Figure / DeepMind 自建数据管线，不会外包信任；证书的真实买家是数据供应商（信息不对称方）和出海 OEM。 |
| **前沿性** | 4 | 4 | "本体校验的场景图 + 物理残差 + 签名证书"这一组合在文献里尚无归类（153 篇机器人验证器综述中没有"数据集认证"类）。"同一公理集编译为可微与可判定两种形式"是好的工程叙事但不是定理（模糊松弛对一阶蕴含既不 sound 也不 complete）。LLM 提公理 + 定理证明器把关是已知模式（Specula 是 TLA+ 系统代码，类比松散）。 |
| **市场** | 3 | 3.5 | 中国：可触达收入 2026–28 年 1.5–4 千万元是合理量级（群核 SpatialVerse 2026 上半年订单仅 680 万）；2030 年品类 15–30 亿是自估。中国出货集中（2026 H1 智元 9,700 / 宇树 5,900 台，2026 全年约 6 万台、2030 年 50 万台预测）让"按台授权"有想象空间。美国：deck 自己写的 $12–60M 是功能市场；要成 venture-scale 必须按轨迹计量或走 OEM / 保险 / 公告机构渠道；物理 AI 2026 Q2 单季融资 $18.6B，钱在。 |
| **科学性** | 3.5 | 3.5 | 已核实：ISO/IEC 21838-4 TUpper 确实是多伦多大学 Grüninger 组的成果，COLORE 公开仓库里有 756 个 Prover9 / Mace4 验证文件，"机器证明一致"的方法论真实且长期。**未能核实**："35 项中承担 22 项"（ISO 不公开编辑名单）、FOIS"杰出论文奖"（FOIS 有 Best Paper Award，未见多伦多获奖记录）、NIST IR 8530 提及 TUpper 的具体页码。**IP 风险**：TUpper 的 CLIF 源码是多伦多大学版权 CC BY-SA 4.0，内核若为衍生作品可能有 share-alike 义务，需确认与学校的 IP 协议。 |
| **团队** | 3.5 | 3 | CEO 三重稀缺性成立。缺：训练过 VLA 的机器人学习科学家、销售负责人；中国缺产业侧联合创始人（国地中心 / 信通院 / 智元体系交付经验），美国缺本土 GTM。 |
| **进展** | 1.5 | 1.5 | 已实现的全是资产（数据、专利、资质、关系），没有任何客户行为。引擎 2026 Q4 才内测。 |
| **why now** | 3.5 | 2.5 | 中国：数据集质量标准 2026-11-01 实施、入表已施行、北数所 2026-09 首发具身数据跨境流通平台、数采中心"批量露馅"——证据格式的确定窗口在 2027 年内是真的。美国：欧盟附录 I 2028-08-02 属实但只覆盖机器学习安全部件，美国联邦层面 2026 年在去监管，Colorado AI 法案已被替换为仅披露制——合规是弱 why-now；真正的 why-now 是数据竞赛 + 世界模型合成数据涌入 + 无人拥有的"数据 QA / 评测 / 证据"层。 |

---

## 3. 核心发现（研究部分的关键事实）

### 3.1 法规与标准核实
- 欧盟：Regulation (EU) 2026/1744（Digital Omnibus）2026-07-24 公报、07-27 生效；附录 III 2027-12-02、附录 I 2028-08-02 **均属实**。但第 10 / 12 条覆盖机器人的路径很窄：只有当学习组件是机械法规下需第三方符合性评估的"安全部件"时才触发；多数操作 / VLA 部署把安全放在确定性安全层，其训练数据不被覆盖；第 10 条的协调标准尚不存在。
- 中国：GB/Z 218.1—2026、YD/T 6770—2026（2026-06-01 实施）、标准体系 2026 版（2026-02-28）、CR-3-06:2025（智元 2025-09 首张）、实景实训专项行动（2026-06-09）、入表规定（财会〔2023〕11 号）、可信数据空间行动计划、一机一码、《具身智能数据集质量要求及评价方法》（2026-07-24 批准、11-01 实施，八维指标）**均属实**。**全部为推荐 / 指导性，且没有任何一项规定"证据格式"。**
- 原稿中的"上研院穹顶 DOME"与"松应 ORCA 仿真数据检测认证"**零检索命中**，松应公开定位是仿真生成平台。改稿已删除 DOME，ORCA 归入仿真厂商。

### 3.2 市场数字核实
| 原稿数字 | 结论 |
|---|---|
| 全球高质量真机数据约 50 万小时 | 有此说法但口径混乱（澎湃说"全球"，贵州省数据局说"国内合规数据"），不宜作全球统计引用 |
| 可用状态需 1,000 万小时 | 行业共识口径，无严格论证 |
| 数采工厂报价约 1,000 元 / 小时；有效成本 >500 元 | 市场价 500–1,000 元 / 小时属实；">500 元有效成本"无直接出处 |
| 2025 年 140+ 家、330+ 款 | 属实（工信部） |
| 2025 年约 1.7 万台出货 | 数字属实但口径是**全球**；2026 全年约 6 万台，2030 年 50 万台（SAG） |
| 2026 年宇树 + 智元占 80% | TrendForce 预测口径；实绩 2026 H1 智元 9,700 / 宇树 5,900 台（Counterpoint） |
| 上海训练场 100 万+ 条、2.5 PB | 属实 |
| 2026 上半年世界模型融资超百亿 | 属实 |
| 全国数采中心 | 64 座、覆盖 27 城；2026-09-20 虎嗅报道"批量露馅" |

### 3.3 竞争格局（浓缩）
- **全球**：Applied Intuition $15B（Dana 面向机器人）；Foretellix $135M（裁员）；NVIDIA 数据工厂蓝图含免费 Cosmos Evaluator（物理正确性 / 时序稳定 / 语义准确评分）+ Halos for Robotics（ANAB 认可检测实验室对接 TÜV / UL）；Scale AI 物理 AI 引擎 150k+ 小时（Meta 交易后中立性受损，是个机会）；Encord $60M C 轮；Foxglove $40M B 轮（数据搜索与整理）；Voxel51 调查 89% 团队把模型失败归咎于数据；Hugging Face LeRobot 58,000+ 数据集无验证；Pebblous（韩国）卖物理 AI 数据诊断 / 认证 + EU AI Act 证据链——**定位最接近，但无形式化内核**。
- **中国**：没有创业公司做数据护照。真正的对手是标准归口与认证机构（CR 认证联盟、信通院、CESI）+ 训练场 / 数采龙头自建质检（国地中心、京东、智元）。信通院 2026 Q4 大概率推"可信具身数据集"评测发证。
- **红杉中国**：2025–26 出手集中在自变量、千寻智能、星动纪元（跟）、中科第五纪（领）、穹彻；在光轮、松应、极佳、群核、帕西尼等数据 / 仿真基础设施上**零公开出手**，这一层的钱来自产业资本与地方国资。红杉在数据层看重的顺序：**客户绑定 > 团队 > 数据资产 > 标准卡位**。

### 3.4 技术尽调要点
- 真正稀缺：TUpper / PSL / COLORE 血统的一阶本体专家与机器一致性证明文化。
- 商品化组件：VLM 场景图（ConceptGraphs 等）、VLM 自动标注（ECoT 已标 250 万条转移）、运动学检查（VISTA、lerobot-doctor）、LTN 软约束、符合性预测、STL / LTL 运行时监控（RoboGuard 是护栏产品的最近先例）、签名清单（sigstore model-transparency、C2PA）。
- 十项风险中高危四项：接地准确性（一致 ≠ 正确）、物理残差缺力矩数据、买方接受度（实验室自建）、简单基线可能等效。
- 最能说服技术型 VC 的三个 demo：注入错误盲测基准；跨本体复用 + 下游策略成功率提升；公开验证器 + 样例护照并邀请篡改。

---

## 4. 红杉中国视角：十个尖锐问题与答案方向

1. **谁付钱？** 买方为什么不自建质检？→ 答案必须是具名客户与对照数字（带护照数据售价 / 验收周期）。
2. **没有强制合规**，审计包 50–300 万元 / 次的付费理由？→ 出海整机厂（欧盟）与拟上市（入表 / 审计）是仅有的两个真实付费理由。
3. **对标 CR 认证**：替代它还是给它做底座？→ 做技术底座与联合发证，毛利来自引擎年费与按数据集的护照。
4. **对标信通院**：客户在乎"形式化证明"吗？→ 目前没有客户明说在乎；要用盲测基准证明形式化层能抓到规则抓不到的错误类。
5. **2026 Q4 内测、零客户，2027 年 800 万？** → 把 800 万拆成具名 pipeline（3 个审计包 + 5 个数据集证据 + 1 个引擎部署），否则不要写。
6. **护栏 100–300 元 / 台 / 年**：2026 年 6 万台装满也只有 600–1,800 万 / 年，且整机厂为何让第三方跑运行时？→ 承认护栏是 2029 年后的期权，本轮不定价。
7. **北数所资质**是撮合不是认证，跨境流通平台上有登记吗？→ 90 天内完成首批登记。
8. **TUpper 如何映射到一条 30 秒的抓取轨迹？国地中心 30 类任务本体要重做吗？** → 展示领域层公理与竞争力问题（competency questions）的证明产物。
9. **物理一致性用谁的物理引擎？** 若用光轮 / 松应的引擎，证书是否在替它们背书？→ 独立校准 + 真机留出集。
10. **谁在国地中心 / 信通院 / 智元体系交付过数据？** → 补人。

## 5. YC / a16z 视角：十个尖锐问题

1. 法规触发是 2028 年且只覆盖机器学习安全部件，2026–27 年实验室买什么、为什么现在？
2. 为什么不是 Foxglove / Rerun / Applied Intuition / Foretellix 的一个功能，或实验室自己的管线？本体之外的护城河是什么？
3. 护照分数与下游策略成功率相关吗？拿数据来。
4. 团队里谁大规模训练 / 部署过 VLA？
5. 物理 / SMT 检查在遥操作数据上的误拒率是多少，拒掉好数据的成本谁承担？
6. 说出两家 design partner；你要 $25k 时他们说了什么？
7. 美国在抢占监管、Colorado 回撤、欧盟协调标准缺席——如果欧盟再延期呢？
8. 自下而上 TAM 是 $12–60M，凭什么是十亿美元公司？
9. 数据供应商会自我认证，为什么接受第三方评分？实验室为什么信你的签名？
10. 合成 / 世界模型数据将占多数，来源是生成器种子时"溯源"意味着什么？

---

## 6. 改稿说明（我改了什么、为什么）

### 6.1 结构
| | 原中文稿 | 新中文稿（红杉版） | 原英文稿 | 新英文稿（YC / a16z 版） |
|---|---|---|---|---|
| 页数 | 42 | **16** | 46 | **13** |
| 受众 | 标准制定者研讨稿 | Pre-A 路演 | 商业化计划书 | 种子轮 |
| 一句话 | 无 | 让每一条机器人训练数据可核验、可认证、可入表 | "Engineering the evidence layer" | Every robot dataset ships with a machine-checkable passport. |
| 痛点 | 8 页宏观（50 万小时缺口） | 1 页，三类买家今天的痛 + 数采中心"露馅" | 6 页 | 1 页，三种失败模式 + Voxel51 89% |
| 方案 | 15 页六环节 | 产品 1 页 + 实例 1 页 + 壁垒 1 页 | 17 页 | 同左 |
| 竞争 | 1 页，含未核实的 DOME / ORCA 认证 | 重写：加 NVIDIA Cosmos Evaluator、CR 认证联盟、信通院、京东；删 DOME | 1 页 | 重写：加 Applied Dana、Pebblous、Voxel51、RoboGuard |
| 市场 | 三级 + 出货集中 | 保留三级，数字口径修正（全球 1.7 万台 → 中国 2026 约 6 万台 → 2030 年 50 万台） | $12–60M | 三级：楔子 $12–60M → 平台 $100M ARR → 按台版税；对标 Applied / Foretellix / Vanta |
| 进展 | 已实现 / 推进中 / 目标 | 加"90 天内可验证的三件事"（盲测基准、具名伙伴、公开验证器） | 同 | 同 |
| 合作提议（对政府） | 2 页 | 删除，改为融资 ask | — | Ask 页 |
| 融资金额 | 无 | **建议 3,000–5,000 万元 Pre-A**（标注为建议） | 无 | **建议 $4–6M seed**（标注为建议） |
| 语气 | 研讨稿 | 路演 | 每页自我否定 | 自信 + 可证伪的试点设计 |

### 6.2 保留的原稿资产
一句话"一套公理，两种产品"；护照字段设计；示例轨迹 AX-2027-0412；三重核验表；四档基线盲测的试点设计；成本曲线 430 → 85 元（标注为模型值）；三档情景；团队简历（重新排序为"三重稀缺性"）。

### 6.3 删除或弱化
"35 项中承担 22 项"从封面移除（团队页保留为公司自述）；DOME；"合作提议"章节；四个"暂缓方向"；Stone 对偶 / Birkhoff / GraphRAG / t-范数等术语；"来源与说明"整页（改为每页脚注）。

### 6.4 设计
两版共用一套视觉系统：墨蓝主色、取自公司自有点云渲染的绯红强调色、青色表示"通过 / 已验证"；母题为点云标注框的角括号。封面与结语用深色，内容页白底；每页有图表、卡片或图标，没有纯文字页。字号 ≥ 9 pt（原稿大量 7–8 pt）。

---

## 7. 若要"红杉一定投 / YC·a16z 投"，90 天内必须发生的事

| # | 事项 | 中国 | 美国 |
|---|---|---|---|
| 1 | **公开盲测基准**：DROID / AgiBot World 各 200 条，注入 7 类错误，对比"规则 + VLM"基线，公布逐类查全率与每小时成本，第三方持注入密钥 | 必须 | 必须 |
| 2 | **具名 design partner** 以自带数据生成真实护照 | 训练场 / 数采龙头 / 拟上市整机厂 1 家 | 数据供应商或 OEM 2 家，$25–50k 试点已付款 |
| 3 | **公开验证器 + 公钥 + 样例护照**，邀请篡改 | 必须 | 必须 |
| 4 | **渠道绑定** | 护照嵌入 CR-3-06 / 信通院评价方法；北数所跨境流通平台首批登记 | 成为 LeRobot / Foxglove 的"verified"徽章 |
| 5 | **补人** | 中国产业侧联合创始人 | 训练过 VLA 的科学家 + 美国 GTM |
| 6 | **叙事** | 16 页红杉版（已完成） | 13 页种子版（已完成） |

---

## 8. 需要创始团队核实或补充的事实清单
1. "ISO/IEC 21838-4 承担 35 项中 22 项"的出处（ISO 不公开编辑名单）。
2. FOIS 奖项的年份与论文题目（FOIS 设 Best Paper Award）。
3. NIST IR 8530 提及 TUpper 的页码。
4. TUpper CLIF 源码（多伦多大学版权、CC BY-SA 4.0）与公司内核的许可关系及学校 IP 协议。
5. "上研院穹顶 DOME"与"松应 ORCA 检测认证"的出处（未检索到）。
6. "头部厂商有效成本 >500 元 / 小时"的出处。
7. 融资金额：本次修订建议中国 Pre-A 3,000–5,000 万元、美国种子 $4–6M，请按实际预算确认。
8. 2027 年 800 万元收入的具名 pipeline。

---

## English summary

**Verdict.** Worth backing the founder and the direction, not the current state. AXIOMALITY is an empty category (no one, in China or globally, sells a per-record, signed, offline-verifiable certificate for robot training data), led by one of very few people who can write and machine-verify first-order top-level-ontology axioms and who has also run a $50M-revenue company. But the company today has assets, no product (engine internal test Q4 2026) and no customers. HongShan would not invest now: their 2025–26 embodied deals are brains and customer-bound hardware, with zero public deals in data infrastructure; they buy customer binding, not standards positioning. YC would fund a re-cut version with a demo and one quantified result; a16z would look at a Series A with two named design partners, ~$0.5–1M ARR or metered trajectory volume, and a 10x claim (passport score predicts policy success).

**What we verified.** EU Regulation 2026/1744 dates are correct, but Art. 10/12 reach robots only when the learned component is a machinery safety component; the U.S. is deregulating. All nine Chinese standards cited are real and dated correctly, all are recommended/guidance-level, and none defines an evidence format. "DOME" and "ORCA certification" could not be found. Shipment figures: 17k humanoids in 2025 is a global number; China 2026 ≈ 60k, 2030 forecast 500k; AgiBot 9,700 / Unitree 5,900 units in H1 2026. TUpper (ISO/IEC 21838-4) is a University of Toronto (Grüninger) product with 756 Prover9/Mace4 verification files in the public COLORE repo; the "22 of 35" and FOIS-award claims are unverifiable from public sources; TUpper's source is CC BY-SA 4.0, an IP point to clear.

**Closest threats.** NVIDIA (free Cosmos Evaluator + Halos inspection lab), Applied Intuition (Dana), Pebblous (Korea, data certification for physical AI), and in China the certification bodies (CR-3-06, CAICT) plus in-house QA at training grounds. Labs (PI, Figure, DeepMind) curate in-house; the passport's real buyers are data suppliers, exporting OEMs and buyers who want an independent re-check.

**What changed in the decks.** China deck cut from 42 to 16 slides and rewritten as a Pre-A pitch (one-liner, buyer pain, product, example, moat, competition, model, market, why-now, GTM, 90-day proof, team, financials + suggested ¥30–50M ask, close). U.S. deck cut from 46 to 13 slides in YC/a16z form (one-liner, problem, why-now, product, example, moat, market with Applied/Foretellix/Vanta comps, competition, model, GTM with falsifiers, traction + 90-day proof, team, $4–6M seed ask with gates). Unverified claims were removed or labeled; numbers were re-based on verified sources.
