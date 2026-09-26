# AXIOMALITY 投资备忘录（第二版）

日期：2026-09-26　范围：产品逻辑、稀缺性、可行性、前沿性、市场、科学性；中国（红杉）与硅谷（YC / a16z）两种视角。本版不涉及融资。

---

## 0. 结论

**值得投的是人和方向，现在还差"有人要"的证据。** 这一版做了三件事，把公司从"只有资产和 PPT"推到"有能跑的东西、有真实数据上的发现"：

1. **换方向**：从"证据层 / 数据护照 / 标准卡位"收窄到**具身数据采购的第三方验收：先验货，再付款**（英文：*We inspect robot training data before labs pay for it, and sign the result*）。两位模拟投资人在第一轮各自独立提出了同一个方向。
2. **做出原型**：一个真实可运行的验收引擎和签名验收单（数据护照），已在 DROID 等三个公开真实数据集上跑通，发现了真实问题。
3. **诚实对比**：自己写了一个"一周工作量"的强规则基线，结果检出率持平。BP 据此把壁垒从"更聪明的检查"改为"中立、可复算、签名、跨客户错误库"。

| 视角 | 原稿 | 第一次改稿 | 现在（第三轮评分） | 只改 BP 的上限 | 90 天证据兑现后 |
|---|---|---|---|---|---|
| 红杉中国投委会 | — | 3 / 10 | **5 / 10**（跟踪，不上会） | 6 / 10 | 约 7 / 10 |
| YC（面试即投） | — | 4 / 10 | **5 / 10** | 6 / 10 | 7+（需一个真实供应商说"要"） |
| a16z（上合伙人会） | — | 2 / 10 | **3 / 10** | 4 / 10 | 需两家具名设计伙伴 + 真实数据增量 |

**需要直说的一点**：三轮独立评审的结论一致，只改 BP 到不了"一定投"。缺的是现实里的需求证据：一家付费试点，或一家实验室书面同意"入库验收时接受验收单"。第 5 节是具体的 90 天清单。

---

## 1. 方向为什么这样改

| 原定位 | 问题 | 新定位 |
|---|---|---|
| 具身智能的"证据层"，护照随国标 / 欧盟合规推广 | 中国相关标准全是推荐性，没有采购义务；欧盟只在 2028 年覆盖机器学习安全部件；美国在去监管 | **验收**：数据在买卖之间换手时，由第三方逐条裁决、签名 |
| 四条收入线（护栏按台、证据按项目、引擎年费、评测） | 焦点散，销售动作互相打架 | 一个产品、一种计价：按验收的数据量收费；试点 → 按量 → 站内授权 |
| 卖给整机厂和监管 | 实验室不需要签名，监管不付钱 | 先卖**卖方**：数采中心、挑战者数据供应商要证明自己比同行好；买方用公钥免费复验 |
| "形式化内核让我们检查得更好" | 自测表明强规则基线检出持平 | 壁垒是**中立出具 + 结论可复算 + 离线可验 + 跨客户错误库**；形式化用于保证规则扩到数百条时仍一致（待验证的假设） |

中国的时机：全国 64 座数采中心，2026-09-20 被报道"批量露馅"；信通院《具身智能数据集质量要求及评价方法》2026-11-01 实施，但只有质量指标，没有证据格式；北数所 2026-09 首发具身数据跨境流通平台。

美国的时机：数据供应商在规模化（Mecka 约 5 亿美元估值在谈、XDOF 约 12 亿美元、Build AI 免费开放约 100 万小时），World Labs Atlas 等生成器涌入训练，2026 Q2 物理 AI 单季融资 186 亿美元。合规只作为后续顺风。

---

## 2. 原型：做了什么、结果是什么

代码在 `prototype/`，`python run_all.py`（v1）与 `python run_v2.py`（v2）一条命令复现。生成数据、下载的真实数据和演示私钥都不进仓库，运行时重建。

### 2.1 真实数据（Open X-Embodiment 公开数据）

| 数据集 | 轨迹 / 帧 | 通过* | 修复 | 拒收 | 未检项 | 验收单 |
|---|---|---|---|---|---|---|
| DROID（Franka） | 14 / 2,551 | 5 | 1 | 8 | 时间戳、语义 | 离线验签通过 |
| Jaco Play（Kinova） | 13 / 879 | 13 | 0 | 0 | 时间戳、语义 | 离线验签通过 |
| NYU ROT（xArm） | 14 / 440 | 14 | 0 | 0 | 时间戳、语义 | 离线验签通过 |

\* 只指"可检项"通过。这些数据集没有记录时间戳和物体状态，相关检查未执行。

在 DROID 中的真实发现：

- **机械臂卡死 / 数据流冻结**：第 3 条第 19–33 帧，指令关节位置在动（中位差 0.133 rad），实测关节逐位不变；第 43–49 帧整行重复。
- **关节越限**：第 1 条第 141–172 帧，关节 6 达 3.959 rad，超出 Panda 手册上限 207 mrad。也可能是 FR3 机型，其上限 4.52 rad。
- **字段说明与数值不符**：action 字段文档写"6 个关节速度"，2,551 帧全部等于指令笛卡尔位姿；另有 8/14 条没有任何语言指令。

诚实说明：卡死和越限两条都在 DROID 自标为 failure 的轨迹里；结构基线在 DROID 上与引擎的通过 / 拒收判断一致 8/14；形式化求解器（Z3）在真实数据模式下没有参与裁决。

### 2.2 合成基准（含噪声，3 种任务变体，每类错误 20 条）

| | 引擎 | 强规则基线（写于引擎之后） | 结构基线 |
|---|---|---|---|
| 检出率 | 92% | 92% | 41% |
| 精确率 | 1.00 | 1.00 | 1.00 |
| 干净样本误拒（140 条） | 0 | 0 | 0 |
| 时间戳乱序字节级还原 | 20 / 20 | 0 | 0 |
| 每条耗时 | 14 ms | 1.4 ms | 0.6 ms |

引擎的剩余优势包括：更小的可检误差（下陷 25 mm vs 40 mm，松手后跳动 30 mm vs 60 mm）、字节级修复，以及缺输入时返回"未知"。评审判断这些优势"基线约一天可追平，不作壁垒"，BP 已照此表述。

规则库：30 条规则，其中 24 条用 Z3 在 14 帧有界模型上证明可同时满足，9 条在合成数据上逐条由 Z3 判定，6 条为数值检查。原型里没有 TUpper 代码；与 ISO/IEC 21838-4 的对齐是产品目标，不是已完成的事实。

---

## 3. 逐维度评估（当前状态）

| 维度 | 评价 |
|---|---|
| 产品逻辑 | **清楚了**：一批数据进，一张验收单出；卖方付费出货，买方免费复验。剩下的主要矛盾是：实验室自己的质检不需要签名。解法是先做卖方，再争取一家实验室把验收单写进入库标准。 |
| 稀缺性 | 人稀缺：TUpper / COLORE 血统的一阶本体专家，加上经历过一年 5,000 万美元营收的创业者。品类空：公开检索未见中立方出具可离线复验的逐条验收记录。但组件在商品化，NVIDIA Cosmos Evaluator 免费、韩国 Pebblous 在做数据认证。 |
| 可行性 | 引擎已能跑，签名与篡改检测成立。最大缺口是真实数据上的语义层：现有公开数据集不记录物体状态，需要"从视频抽取物体状态"的前端，这需要机器人学习方向的负责人。 |
| 前沿性 | 组合新，单个部件多为已有技术。形式化方法的价值要在"规则扩到数百条时仍一致、可引用"上证明，目前是假设。 |
| 市场 | 中国：按"采购额 × 验收费率"估算，情景 3,000 万至 6 亿元，基准 1.35 亿元。美国：仅第三方验收是 500 万至 1.2 亿美元的池子；要成 venture scale，必须成为所有训练数据（含自采与合成）的入库关口。 |
| 科学性 | BP 已去掉无法支撑的数字，包括护照样例中的 96.4% / 99.1% / 0.94、430→85 元成本曲线、"一个字节"之类说法。现在每个数字都能在代码和结果文件里核到。 |
| 团队 | 创始人三重稀缺性成立。缺中国产业侧合伙人（有训练场 / 数采体系交付经验），以及训练过 VLA 的机器人学习负责人。 |
| 进展 | 从"零"变为：可运行原型、真实数据发现、签名验收单。仍然零客户。 |

---

## 4. 两份 deck 的结构

**中文红杉版（15 页，无融资）**

1. 封面：具身数据，先验货，再付款
2. 数采中心露馅，买方没有验收单
3. 一个采购负责人的一天
4. 产品：一批数据进，一张验收单出
5. Demo：真实数据
6. Demo：与强基线的诚实对比
7. 单位经济：验收费远小于坏数据损失，无效比例 ≥ 4% 即回本
8. 为什么是现在
9. 竞争：对手是自检和认证机构
10. 壁垒假设
11. 商业模式与市场
12. 首批客户名单：标准起草单位，加上自变量、穹彻
13. 进展与 12 月 31 日前可验证的事项
14. 团队
15. 结语与请求：两个介绍、12 分钟现场、12 月 31 日核对

**英文 YC / a16z 版（13 页，无融资）**

1. 封面：We inspect robot training data before labs pay for it
2. 问题
3. 为什么是现在
4. 产品
5. Demo：真实数据
6. Demo：Checks are copyable; a neutral, signed record is not
7. 可复算规则
8. 竞争 2×2
9. 商业模式与 venture-scale 条件
10. 挑战者供应商 GTM
11. 进展与 Dec 31 承诺
12. 团队
13. 愿景与请求

---

## 5. 让他们投：90 天内必须在现实中完成的事

创始人需要做以下几件事：

| # | 事项 | 红杉 | YC | a16z |
|---|---|---|---|---|
| 1 | **一家具名付费试点**（≥ 30 万元 / $25k，客户自带数据，指标预先注册），或两份 LOI | 必须 | 必须 | 必须 |
| 2 | **一家实验室或具身大脑公司书面同意入库时接受验收单**（中国优先找自变量、穹彻等红杉被投） | 强加分 | 加分 | 必须 |
| 3 | **在带物体标注的真实数据上跑出语义层**：先做从视频抽取物体状态的前端，在 ≥ 500 条真实轨迹上对比强基线和 Cosmos Evaluator，注入密钥和专家真值交第三方持有；增量 < 10 个百分点就收窄 | 必须 | 加分 | 必须 |
| 4 | **补人**：中国产业侧合伙人全职；机器人学习负责人到位；美国 GTM | 必须 | 必须 | 加分 |
| 5 | **渠道**：北数所跨境流通平台首批带验收单挂牌，拿到买方价差反馈；验收单字段对齐信通院八维指标并提交 | 加分 | — | — |
| 6 | **30+ 次客户访谈**，在 BP 上写真实计数，哪怕是 0 | 加分 | 必须 | 加分 |

---

## 6. 需要创始团队核实或补充
1. "ISO/IEC 21838-4 承担 35 项中 22 项"的出处（ISO 不公开编辑名单）；BP 已改为"核心贡献者"。
2. FOIS 奖项的年份与论文题目；BP 已删去。
3. TUpper CLIF 源码（多伦多大学版权、CC BY-SA 4.0）与公司内核的许可关系，以及学校 IP 协议。
4. 客户访谈与试点的真实计数，填进两份 BP 的"市场路径 / GTM"页。
5. 公司自有数据和经纪商资质与"中立验收"之间的利益冲突隔离安排。
6. 若要在 Hugging Face 上跑 LeRobot 数据集，需在环境网络设置中放行 `huggingface.co`；本次改用 OXE 公共存储桶。

---

## 7. 研究与评审材料
- `research/00_deck_critique.md`：原稿诊断
- `research/01_global_competitors.md`：全球竞品（约 85 条来源）
- `research/02_china_ecosystem.md`：中国生态、政策核实、红杉口味
- `research/03_us_investor_lens.md`：欧盟 / 美国法规核实、YC / a16z 视角、可比公司
- `research/04_technical_dd.md`：技术尽调
- `research/investor_reviews/`：三轮模拟投资人评审原文（红杉与 YC / a16z 各三轮）

研究由并行 agent 通过网页检索完成。容器出口代理封锁了大部分中文站点正文，事实主要来自检索摘要，每条附 URL，未核实项已标注。

---

## English summary

**Verdict.** Back the founder and the direction. The company moved from "assets and slides" to a working prototype with real findings on real data, but it still has zero customers. Three rounds of independent simulated reviews agree: wording alone caps the deck at about HongShan 6/10, YC 6/10, a16z 4/10. A yes needs real demand evidence within 90 days.

**What changed.** The company was repositioned from a compliance-led "evidence layer" to third-party acceptance testing for robot training data changing hands: "We inspect robot training data before labs pay for it, and sign the result." Vendors pay, and buyers verify free with a public key.

**Built.** A runnable engine and Ed25519-signed passport. On 41 real episodes from DROID, Jaco Play and NYU ROT it found a stuck-arm or frozen-stream episode, a joint 207 mrad past the Panda datasheet limit (possibly an FR3), and a DROID action field whose values contradict its documentation. On a noisy synthetic benchmark, the engine ties our own strong hand-written baseline at 92% recall with zero false rejects. The deck says so plainly and places the moat in neutrality, re-checkable signed verdicts, and a cross-customer error library.

**Next 90 days.**
- One paid pilot or two LOIs.
- One lab's written intake requirement.
- Semantic checks on ≥ 500 real episodes against the strong baseline and Cosmos Evaluator, with a third-party key.
- A robot-learning lead and a China industry co-founder.
