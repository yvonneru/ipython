// AXIOMALITY — 红杉版 Pre-A 路演稿（16 页）
const L = require("./lib");
const { C, W, H, M } = L;
const path = require("path");
const fs = require("fs");

const MEDIA = path.join(__dirname, "..", "src", "media_cn");
const OUT = process.argv[2] || path.join(__dirname, "out", "AXIOMALITY_红杉版_PreA路演稿.pptx");

const TOTAL = 16;
const FOOT = "AXIOMALITY  ·  Pre-A 路演稿  ·  2026 年 10 月  ·  保密";

(async () => {
  const pres = L.newDeck("zh", { title: "AXIOMALITY 红杉版路演稿", total: TOTAL, footer: FOOT });
  const F = pres._F;
  let n = 0;

  // ───────────────────────── 1. 封面 ─────────────────────────
  {
    const s = pres.addSlide(); n++;
    L.darkBg(pres, s);
    L.label(pres, s, "AXIOMALITY", M, 0.55, 4, 0.35, { size: 13, bold: true, color: C.white, extra: { charSpacing: 4 } });
    L.label(pres, s, "让每一条机器人训练数据\n可核验、可认证、可入表", M, 1.55, 7.2, 2.0, { head: true, size: 36, bold: true, color: C.white, ls: 1.12 });
    L.label(pres, s, "具身智能数据的核验引擎（Engine）与数据护照（Passport）", M, 3.7, 7.2, 0.5, { size: 16, color: "C9CDDB" });
    L.label(pres, s, "Pre-A 融资路演稿  ·  2026 年 10 月  ·  保密", M, 4.25, 7.2, 0.4, { size: 12, color: "9AA0B4" });

    // sample image with bracket motif
    const img = path.join(MEDIA, "cover_crop.png");
    s.addShape(pres.shapes.RECTANGLE, { x: 8.3, y: 1.35, w: 4.45, h: 2.6, fill: { color: C.ink2 }, line: { color: C.ink2 } });
    s.addImage({ path: img, x: 8.45, y: 1.92, w: 4.15, h: 1.46 });
    L.brackets(pres, s, 8.3, 1.35, 4.45, 2.6, C.crimson, 0.22, 1.5);
    L.label(pres, s, "AXIOMALITY 实测样本 429：PLY 点云与三维标注框（真实数据）", 8.3, 4.02, 4.45, 0.3, { size: 9.5, color: "9AA0B4" });

    // bottom stats
    const stats = [
      ["ISO/IEC 21838-4", "顶层本体 TUpper 核心贡献者创办"],
      ["10 万条", "实测三维数据包（照片 · USDZ · PLY · JSON）"],
      ["13 + 9", "授权专利 + 发明专利申请"],
      ["2026 Q4", "核验引擎内测；2027 年首批付费客户"],
    ];
    stats.forEach((st, i) => {
      const x = M + i * 3.05;
      s.addShape(pres.shapes.LINE, { x, y: 5.35, w: 2.7, h: 0, line: { color: "3A4160", width: 0.75 } });
      L.stat(pres, s, x, 5.45, 2.8, 1.2, st[0], st[1], { dark: true, size: 22, labelSize: 10.5 });
    });
    s.addNotes("开场 30 秒：我们做的是具身智能数据的质检与认证层。输入任何格式的机器人数据，输出逐条裁决和一张可离线验证的数据护照。创始人是 ISO 顶层本体标准的核心作者。");
  }

  // ───────────────────────── 2. 一页看懂 ─────────────────────────
  {
    const s = pres.addSlide(); n++;
    L.header(pres, s, { tag: "一页看懂", title: "机器人数据的「质检 + 护照」：一个引擎，两个产品", sub: "输入任何格式的机器人轨迹与场景数据，输出逐条裁决、可离线验签的数据护照，以及可按台预装的语义护栏" });

    // flow strip
    const fy = 1.95;
    const boxes = [
      ["输入", "LeRobot · RLDS · ROS 2 / MCAP\nOpenUSD · 视频 · 3D 扫描\n真机、遥操作、仿真、部署日志", C.panel, C.text],
      ["AXIOMALITY Engine", "接地 → 物理 / 逻辑 / 不确定度三重核验\n→ 通过 / 修复 / 拒判，附依据子图", C.ink, C.white],
      ["输出", "数据护照（签名证书 · 离线可验）\n训练就绪数据集 + 评测套件 + 审计包\n语义护栏（运行时，按台预装）", C.tealSoft, C.text],
    ];
    const bw = 3.75, gap = 0.45;
    boxes.forEach((b, i) => {
      const x = M + i * (bw + gap);
      L.card(pres, s, x, fy, bw, 1.35, { fill: b[2], title: b[0], titleColor: b[3], body: b[1], bodyColor: b[3] === C.white ? "D9DCE8" : C.text, bodySize: 11, titleSize: 14 });
      if (i < 2) L.arrow(pres, s, x + bw + 0.08, fy + 0.68, gap - 0.16, { color: C.crimson });
    });

    // four quadrants
    const qy = 3.6, qh = 1.4, qw = (W - 2 * M - 0.3) / 2;
    const quads = [
      ["LayoutGrid", "我们卖什么", "楔子产品：认证证据项目（护照 + 审计包，按数据集 30–80 万元）→ 引擎站内年费（50–200 万元）→ 语义护栏按台授权（100–300 元 / 台 / 年）。同一内核，三级扩展。"],
      ["Users", "卖给谁", "拟上市与出海的整机厂（训练与合规团队）、国家级训练场与数据商（要把数据卖出价、挂牌上架）、具身大脑与世界模型公司（合成数据需要核验与来源记录）。"],
      ["Clock", "为什么是现在", "原始小时数价格归零（免费视频已出现）；世界模型把未经核验的合成数据推入训练；GB/Z 218.1、YD/T 6770 落地，数据入表与欧盟附录 I（2028-08）要求逐条证据。"],
      ["ShieldCheck", "为什么是我们", "全球少数写过 ISO 顶层本体公理并做过机器一致性证明的团队；已有 10 万条实测三维数据、13 项专利、北数所数据经纪商资质；创始人曾把一家公司做到年收入 5,000 万美元。"],
    ];
    for (let i = 0; i < 4; i++) {
      const x = M + (i % 2) * (qw + 0.3), y = qy + Math.floor(i / 2) * (qh + 0.2);
      L.card(pres, s, x, y, qw, qh, { fill: C.white, lineColor: C.line, title: quads[i][1], titleIndent: 0.5, body: quads[i][2], bodySize: 10.5 });
      await L.icon(s, quads[i][0], x + 0.2, y + 0.16, 0.36, { bg: C.crimson });
    }
    L.footer(pres, s, n);
  }

  // ───────────────────────── 3. 买家今天的痛 ─────────────────────────
  {
    const s = pres.addSlide(); n++;
    L.header(pres, s, { tag: "痛点", title: "痛点不是「数据不够」，而是「没有一条数据能证明可用」", sub: "三类买家，三种今天就在花钱却解决不了的问题" });
    const cards = [
      ["Bot", "整机厂 · 训练团队", "真机数据市场价 500–1,000 元 / 小时，废数据多、有效率低；换一台机器人，动作层复用率 ≈ 0，需要重采、重标、重验。训练失败后，没有逐条证据说明错在哪一帧、违反了哪条规则。", "「同一批数据，训练成功率忽高忽低，我们只能靠人肉抽查。」"],
      ["Database", "训练场 · 数据商 · 交易所", "全国 64 座数采中心 / 训练场（27 城）；上海训练场累计 100 万+ 条真机数据。但 2026-09 媒体已报道数采中心「批量露馅」：数据无效、无人买单；交易所无法定价、无法上架，卖方只能自证。", "「不是没有数据，是没有人能给数据出一份别人认的质检报告。」"],
      ["Landmark", "CFO · 合规 · 出海", "数据资产入表（2024-01 施行）要求质量与来源证据；欧盟附录 I 自 2028-08-02 起要求机器人训练数据可追溯、可审计；现有形式是文档自述与日志抽样，机器无法逐条校验。", "「拟上市和出海都要证据，我们现在拿不出机器可校验的东西。」"],
    ];
    const cw = (W - 2 * M - 0.6) / 3, ch = 3.05, cy = 1.95;
    for (let i = 0; i < 3; i++) {
      const x = M + i * (cw + 0.3);
      L.card(pres, s, x, cy, cw, ch, { fill: C.panel, title: cards[i][1], titleIndent: 0.5, body: cards[i][2], bodySize: 10.5 });
      await L.icon(s, cards[i][0], x + 0.2, cy + 0.16, 0.36, { bg: C.ink });
      L.label(pres, s, cards[i][3], x + 0.22, cy + ch - 0.78, cw - 0.44, 0.62, { size: 10.5, italic: true, color: C.crimson });
    }
    // stat row
    const st = [["500–1,000 元 / 小时", "真机数据市场报价；有效率无人担保"], ["≈ 0", "动作层跨本体的直接复用率"], ["64 座 · 100 万+ 条", "数采中心数量 · 上海训练场存量，尚无核验与上架规范"], ["23 个月", "距欧盟附录 I 对机器人生效（2028-08-02）"]];
    st.forEach((x, i) => L.stat(pres, s, M + i * 3.05, 5.25, 2.95, 1.1, x[0], x[1], { size: 17, labelSize: 9.5 }));
    L.footer(pres, s, n, "来源：澎湃新闻《具身智能带火了数据采集生意》（2026）；虎嗅《遍地开花的数采中心，开始批量露馅》（2026-09-20）；国地中心；财政部；欧盟委员会（Regulation (EU) 2026/1744）。");
  }

  // ───────────────────────── 4. 价值迁移 ─────────────────────────
  {
    const s = pres.addSlide(); n++;
    L.header(pres, s, { tag: "行业转折", title: "原始小时数正在归零，价值迁移到「证据」这一层", sub: "当视频和原始轨迹按小时免费供给，仍有毛利的只剩语义、核验与认证；证据格式将成为具身数据的计量与交易单位" });
    // value tiers (left)
    const tiers = [
      ["认证", "审计包、上架与入表证据；监管方与交易所采信", C.crimson, C.white, 4.4],
      ["核验", "物理、逻辑、不确定度是否自洽；逐条裁决", "A61A3F", C.white, 5.0],
      ["语义", "发生了什么：对象、可供性、接触、任务阶段", C.ink2, C.white, 5.6],
      ["原始小时数", "未接地的轨迹与视频：2024 年 50–200 美元 / 小时 → 2026 年趋近于零", C.panel2, C.text, 6.2],
    ];
    let ty = 1.95;
    tiers.forEach((t) => {
      const w = t[4];
      const x = M + (6.2 - w) / 2;
      s.addShape(pres.shapes.RECTANGLE, { x, y: ty, w, h: 0.78, fill: { color: t[2] }, line: { color: t[2] } });
      L.label(pres, s, t[0], x + 0.2, ty + 0.08, 1.4, 0.6, { head: true, size: 14, bold: true, color: t[3], valign: "middle" });
      L.label(pres, s, t[1], x + 1.5, ty + 0.08, w - 1.7, 0.6, { size: 10, color: t[3], valign: "middle" });
      ty += 0.9;
    });
    L.label(pres, s, "越往上越稀缺、越难替代；带护照数据在数据商侧定价 1,000–3,000 元 / 小时", M, ty + 0.05, 6.2, 0.35, { size: 10, italic: true, color: C.muted });

    // observations (right)
    L.table(pres, s, [
      ["观察", "数据", "来源"],
      ["原始数据价格下行", "遥操作 50–200 美元 / 小时（2024）→ 数采工厂约 140 美元（2025）→ 原始工厂视频免费开放（2026）", "DreamVu；投资界"],
      ["质量压倒规模", "精选 500 条示范微调 7B 模型，优于以粗糙数据训练的 70B 模型", "State of Robotics 2026"],
      ["泛化来自覆盖度", "32 对环境–物体 × 50 条示范即可在新环境达到约 90% 成功率；同一场景重复一千次不提升", "Lin 等（2024）"],
      ["合规成为准入条件", "欧盟附录 I 自 2028-08-02 适用于机器人；GB/Z 218.1—2026 与 YD/T 6770—2026 落地", "欧盟委员会；信标委；工信部"],
    ], 7.15, 1.95, 5.55, { colW: [1.45, 3.0, 1.1], size: 9.5, rowH: 0.62, boldFirst: true });
    L.card(pres, s, 7.15, 5.35, 5.55, 0.95, { fill: C.crimsonSoft, body: "结论：数据商与实验室为语义和覆盖度付费，交易所与监管方为核验和认证付费。谁定义证据格式，谁就定义交易单位。", bodySize: 11, bodyColor: C.crimson });
    L.footer(pres, s, n, "来源：State of Robotics 2026；DreamVu《Robot Training Data Companies: The 2026 Landscape》（2026-08）；Lin 等《Data Scaling Laws in Imitation Learning》（2024）。");
  }

  // ───────────────────────── 5. 产品 ─────────────────────────
  {
    const s = pres.addSlide(); n++;
    L.header(pres, s, { tag: "产品", title: "Engine + Passport：任意格式进，逐条裁决与护照出", sub: "五步流水线；每条轨迹得到通过 / 修复 / 拒判三种裁决之一，并附可回溯到具体公理与帧的依据子图" });
    const steps = [
      ["接入", "LeRobot、RLDS、ROS 2 / MCAP、OpenUSD、视频、3D 扫描；不要求客户改变采集方式"],
      ["接地", "视觉语言模型 + 图网络把每一帧映射到内核概念：对象、可供性、接触、任务阶段"],
      ["核验", "物理残差（PINN / 神经算子）· SMT 对照内核公理 · 符合性预测校准不确定度"],
      ["裁决", "通过 / 修复 / 拒判，附依据子图；有效失败保留，原始记录不可覆盖"],
      ["护照", "私钥签名、绑定内核版本与数据哈希；公开规范 + 公钥即可离线验证"],
    ];
    const sw = 1.45, sg = 0.14, sy = 1.95;
    steps.forEach((st, i) => {
      const x = M + i * (sw + sg);
      L.stepChip(pres, s, x, sy, i + 1, { d: 0.4 });
      L.label(pres, s, st[0], x + 0.5, sy + 0.02, sw - 0.5, 0.38, { head: true, size: 13, bold: true, valign: "middle" });
      L.label(pres, s, st[1], x, sy + 0.5, sw, 1.6, { size: 9, color: C.text });
      if (i < 4) L.arrow(pres, s, x + sw - 0.05, sy + 0.2, sg + 0.05, { color: C.crimson });
    });
    // three checks table under
    L.table(pres, s, [
      ["校验层", "方法", "判据", "失败处理"],
      ["物理一致性", "PINN / 神经算子残差代理", "残差在阈值内", "修复：投影到最近的可满足解"],
      ["逻辑一致性", "SMT（Z3）对照内核公理 Φ", "SAT 通过 / UNSAT 拒判", "拒判：转人工复核，出具诊断报告"],
      ["不确定度", "符合性预测，覆盖率 ≥ 1 − α", "落在预测集内", "越界即低置信，触发硬核验"],
    ], M, 4.25, 7.65, { colW: [1.3, 2.2, 1.65, 2.5], size: 9.5, rowH: 0.36, boldFirst: true });
    L.label(pres, s, "同一公理集一次编译为两种形式：训练时作为可微的软约束，推理时作为可判定的一致性校验。", M, 5.85, 7.65, 0.5, { size: 10, italic: true, color: C.muted });

    // passport card (right)
    const px = 8.65, py = 1.95, pw = 4.1, ph = 4.55;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: px, y: py, w: pw, h: ph, fill: { color: C.ink }, line: { color: C.ink }, rectRadius: 0.08 });
    L.brackets(pres, s, px + 0.12, py + 0.12, pw - 0.24, ph - 0.24, C.crimson, 0.18, 1.25);
    L.label(pres, s, "AXIOMALITY PASSPORT · 数据护照（样例）", px + 0.3, py + 0.28, pw - 0.6, 0.3, { size: 9.5, bold: true, color: C.crimson, extra: { charSpacing: 1 } });
    const rows = [
      ["数据集", "AX-2027-0412 · 厨房操作任务"],
      ["轨迹数", "12,480 条 · 真机 8,140 / 仿真 4,340"],
      ["内核版本", "kernel v1.2 · 对齐 ISO/IEC 21838-4"],
      ["语义覆盖度", "96.4% 的帧已接地（经抽检）"],
      ["物理一致性", "99.1% 通过 · 0.7% 修复 · 0.2% 拒判"],
      ["不确定度校准", "符合性预测覆盖率 0.94（分组报告）"],
      ["安全规则", "ISO 13482 约束集 · 放行 0 违规"],
      ["来源溯源", "同意书与采集链逐条哈希存证"],
      ["监管映射", "欧盟第 10 / 12 条 · GB/Z 218.1"],
      ["签名", "2027-04-12 · sha256 9f2c…a41e"],
    ];
    rows.forEach((r, i) => {
      const y = py + 0.68 + i * 0.34;
      L.label(pres, s, r[0], px + 0.3, y, 1.1, 0.3, { size: 8.5, color: "9AA0B4" });
      L.label(pres, s, r[1], px + 1.35, y, pw - 1.6, 0.3, { size: 8.5, color: C.white });
    });
    L.pill(pres, s, "VERIFIED · 离线可验", px + pw - 1.85, py + ph - 0.5, 1.6, 0.3, { fill: C.teal, color: C.white, size: 9 });
    L.label(pres, s, "字段取值为样例；2026 年 12 月起可在保密协议下以评审方自带数据生成实际护照。", px, py + ph + 0.06, pw, 0.3, { size: 8.5, color: C.muted });
    L.footer(pres, s, n);
  }

  // ───────────────────────── 6. 一条轨迹的旅程 ─────────────────────────
  {
    const s = pres.addSlide(); n++;
    L.header(pres, s, { tag: "实例", title: "一条轨迹的旅程：失效样本变成新公理，存量数据随之升值", sub: "示例轨迹 AX-2027-0412：厨房，将杯子放入洗碗机（字段为产品设计样例）" });
    const cols = [
      ["采集", "手机三层扫描 + 遥操作示范；房间几何 12 m²、物体 37 件；同意书随采集记录并哈希存证", C.panel],
      ["接地", "对象：杯子（可抓取、易碎）、洗碗机（容器、可开合）；接触事件 3 次；任务阶段 4 段；帧覆盖度 97%", C.panel],
      ["核验", "物理残差通过；SMT 对照内核公理为 SAT；不确定度 0.03；裁决：通过，附依据子图", C.tealSoft],
      ["增强", "数字孪生生成 5 条变体（光照 2、位姿 2、失效 1：杯子滑落）；逐条再核验：4 条通过、1 条拒判", C.panel],
      ["护照", "真机 1 条 + 仿真 4 条写入护照；导出 LeRobot / RLDS / OpenUSD；签名离线可验", C.tealSoft],
      ["回流", "拒判原因：湿滑台面缺少摩擦约束 → 新增公理 → 采集清单补采湿滑场景 → 旧数据集重新核验，护照升级 v1.3", C.crimsonSoft],
    ];
    const cw = (W - 2 * M - 5 * 0.14) / 6, cy = 2.0, ch = 2.75;
    cols.forEach((c, i) => {
      const x = M + i * (cw + 0.14);
      L.stepChip(pres, s, x, cy, i + 1, { d: 0.38, fill: i === 5 ? C.crimson : C.ink });
      L.label(pres, s, c[0], x + 0.48, cy + 0.02, cw - 0.5, 0.36, { head: true, size: 13, bold: true, valign: "middle" });
      L.card(pres, s, x, cy + 0.5, cw, ch - 0.5, { fill: c[2], body: c[1], bodySize: 9.5 });
    });
    // feedback arrow text
    s.addShape(pres.shapes.LINE, { x: M + 0.3, y: 5.05, w: W - 2 * M - 0.6, h: 0, line: { color: C.crimson, width: 1.25, dashType: "dash", beginArrowType: "triangle" } });
    L.label(pres, s, "回流：失效案例 → 新公理 → 核验覆盖度上升 → 每小时核验成本下降 → 采集只花在回流指定的新场景", M + 0.3, 5.12, W - 2 * M - 0.6, 0.3, { size: 10, color: C.crimson, align: "center" });
    const st = [["每个概念只公理化一次", "此后所有轨迹复用"], ["430 → 85 元", "每小时核验数据全负担成本（2026 Q4 → 2030，模型值）"], ["< 35 元 / 小时", "仿真扩展轨迹的边际成本目标"], ["v1.2 → v1.3", "已交付数据集随内核升级重新签发护照"]];
    st.forEach((x, i) => L.stat(pres, s, M + i * 3.05, 5.55, 2.9, 1.05, x[0], x[1], { size: 20, labelSize: 9.5 }));
    L.footer(pres, s, n, "来源：AXIOMALITY 产品记录；成本为单位经济模型的目标值，未签约。");
  }

  // ───────────────────────── 7. 为什么难以复制 ─────────────────────────
  {
    const s = pres.addSlide(); n++;
    L.header(pres, s, { tag: "壁垒", title: "壁垒：经机器证明一致的知识内核，加一个越用越便宜的飞轮", sub: "左：内核是护栏与护照的共同源头；右：失效回流让核验成本随覆盖度单调下降" });
    // left: kernel layers
    const layers = [
      ["顶层 · TUpper（ISO/IEC 21838-4:2023）", "国际正式承认的三大顶层本体之一（与 BFO、DOLCE 并列）；团队参与制定", C.ink, C.white],
      ["中层 · 物理世界", "物体、部件、形状、度量、材料、变化、过程（PSL）", C.ink2, C.white],
      ["领域层 · 机器人", "本体、可供性、接触与力事件、运动链、任务阶段、ISO 10218 / 13482 安全约束", "3A4160", C.white],
      ["数据层 · 轨迹", "轨迹、帧、传感器、血缘；导出 OpenUSD / LeRobot / RLDS", C.panel2, C.text],
    ];
    let ly = 1.95;
    layers.forEach((l) => {
      s.addShape(pres.shapes.RECTANGLE, { x: M, y: ly, w: 6.0, h: 0.72, fill: { color: l[2] }, line: { color: l[2] } });
      L.label(pres, s, l[0], M + 0.2, ly + 0.06, 5.6, 0.3, { head: true, size: 11.5, bold: true, color: l[3] });
      L.label(pres, s, l[1], M + 0.2, ly + 0.36, 5.6, 0.3, { size: 9.5, color: l[3] === C.white ? "D9DCE8" : C.text });
      ly += 0.8;
    });
    L.table(pres, s, [
      ["性质", "含义", "实现"],
      ["一致性", "全部公理经机器证明无矛盾", "Prover9 定理证明 + Mace4 模型构造"],
      ["可扩展", "新机器人、传感器、任务与法规作为模块加载", "表示定理保证模块保结构合并"],
      ["可判定", "每条轨迹的接地结果可在运行时校验", "SMT（Z3）对照公理求解"],
    ], M, 5.2, 6.0, { colW: [0.9, 2.6, 2.5], size: 9, rowH: 0.3, boldFirst: true });

    // right: cost curve chart
    L.label(pres, s, "每小时核验数据全负担成本（元，目标路径）", 7.1, 1.95, 5.6, 0.3, { head: true, size: 12, bold: true });
    s.addChart(pres.charts.LINE, [{ name: "元 / 小时", labels: ["2026 Q4", "2027", "2028", "2029", "2030"], values: [430, 245, 145, 105, 85] }], {
      x: 7.1, y: 2.25, w: 5.6, h: 2.5, chartColors: [C.crimson], lineSize: 2.5, lineDataSymbolSize: 8,
      showValue: true, dataLabelPosition: "t", dataLabelFontSize: 9, dataLabelColor: C.text, dataLabelFontFace: F.body,
      catAxisLabelFontSize: 9, valAxisLabelFontSize: 9, catAxisLabelColor: C.muted, valAxisLabelColor: C.muted,
      valGridLine: { color: "E5E7EB", size: 0.5 }, catGridLine: { style: "none" }, showLegend: false, valAxisMinVal: 0, valAxisMaxVal: 500,
      catAxisLabelFontFace: F.body, valAxisLabelFontFace: F.body,
    });
    L.card(pres, s, 7.1, 4.9, 5.6, 1.6, { fill: C.panel, title: "飞轮如何转", body: "成本集中于概念的首次核验而非重复核验：每个新物体、新可供性、新失效模式只公理化一次。客户回传的部署失效 → LLM 智能体提出候选公理 → Prover9 / Mace4 把关 → 内核 v(n+1) → 旧数据集重新核验、护照升级。数据资产随内核成长增值，原始小时数则持续折旧。", bodySize: 10 });
    L.footer(pres, s, n, "来源：ISO/IEC 21838-4:2023；ISO/IEC 24707；NIST IR 8530（2024）；AXIOMALITY 技术论文；成本曲线为单位经济模型的目标值。");
  }

  // ───────────────────────── 8. 竞争与稀缺性 ─────────────────────────
  {
    const s = pres.addSlide(); n++;
    L.header(pres, s, { tag: "竞争", title: "竞争：还没有人在卖「逐条机器可校验、可离线验签」的数据证据", sub: "采集、仿真、工具、安全层是互补方；真正的潜在对手是标准归口与认证机构、训练场自建质检，以及 NVIDIA 的免费评分器" });
    L.table(pres, s, [
      ["能力", "采集 / 数采工厂", "仿真 · 世界模型", "工具 · 评测", "运行时安全层", "标准与认证机构（中国）", "AXIOMALITY"],
      ["形式化本体（ISO 血统）、机器证明一致", "○", "○", "○", "○", "○", "●"],
      ["物理 + 逻辑 + 不确定度逐条核验", "○", "◐", "◐", "◐", "○", "●"],
      ["签名证书，公开规范 + 公钥离线可验", "○", "○", "○", "○", "◐", "●"],
      ["跨本体统一模式（语义层复用）", "○", "◐", "◐", "○", "◐", "●"],
      ["认证 / 审计包（对齐国标与欧盟条款）", "○", "○", "○", "◐", "●", "●"],
      ["同一内核供运行时护栏", "○", "○", "○", "●", "○", "●"],
      ["代表", "智元数采、帕西尼、京东、Build AI、Mecka、Scale AI", "光轮智能、松应 ORCA、群核 SpatialVerse、NVIDIA Cosmos、World Labs Atlas", "NVIDIA Cosmos Evaluator（免费物理合理性评分）、Applied Intuition Dana、Foxglove、Encord、Voxel51", "NVIDIA Halos for Robotics、3Laws Supervisor", "机器人检测认证联盟 CR-3-06（智元 2025-09 首张）、信通院（数据集质量标准 2026-11-01 实施）、CESI EIBench", "内核 + 引擎 + 护照"],
    ], M, 1.95, W - 2 * M, { colW: [2.2, 1.6, 1.9, 2.05, 1.45, 1.75, 1.18], size: 8.5, rowH: 0.34, boldFirst: true });
    L.label(pres, s, "●  具备     ◐  部分     ○  不具备", M, 5.2, 5, 0.25, { size: 9, color: C.muted });
    const notes = [
      ["与 NVIDIA 的关系", "Cosmos Evaluator 免费给生成数据打物理合理性分，但不签名、不形式化、绑定 NVIDIA 栈；Halos 做功能安全层（ANAB 认可实验室对接 TÜV、UL）。我们位于其上的任务语义层，国内整机厂需要不依赖 NVIDIA 的国产证据层。"],
      ["与 CR 认证 / 信通院的关系", "CR-3-06 是一次性审核加纸质证书，信通院评测是抽样 + 脚本；二者有公信力与渠道但无逐条机器可验的证据。策略：做其评价方法的技术底座与联合发证，护照成为「评价结果的可验证载体」。"],
      ["与训练场 / 数采龙头的关系", "国地中心、京东、智元都有内部「评 / 测」环节，自建质检是最主要的替代方案。我们的差异：中立签发、离线可复算、跨司法辖区映射（欧盟第 10 / 12 条 + GB/Z 218.1 + 数据集质量八维）。"],
    ];
    notes.forEach((t, i) => L.card(pres, s, M + i * 4.1, 5.45, 3.9, 1.2, { fill: C.panel, title: t[0], titleSize: 11, body: t[1], bodySize: 9 }));
    L.footer(pres, s, n, "来源：各公司公告与媒体报道（2025–26）；NVIDIA（2026-03、2026-06）；央广网（2025-09 CR 认证）；21 财经（2026-08-05）；定位为 AXIOMALITY 判断。");
  }

  // ───────────────────────── 9. 商业模式 ─────────────────────────
  {
    const s = pres.addSlide(); n++;
    L.header(pres, s, { tag: "商业模式", title: "一个楔子，三级扩展：从项目费到年费，再到按台授权", sub: "以认证证据项目切入（客户今天就有预算），扩展到站内引擎年费，最终随整机出货按台收取护栏授权费" });
    const stages = [
      ["1 · 认证证据项目", "护照按数据集 30–80 万元\n审计包按发布 50–300 万元", "买家：拟上市 / 出海整机厂、具身大脑公司\n毛利 ≈ 85%", C.panel],
      ["2 · 引擎站内部署", "年费 50–200 万元\n算力由客户承担", "买家：国家级训练场、数据商、实训空间\n毛利 ≈ 70%；试点费在首年年费中抵扣", C.panel],
      ["3 · 语义护栏按台授权", "100–300 元 / 台 / 年\n随底座与操作系统预装", "买家：整机厂（按出货量）\n毛利 ≈ 90%；2029 年起增长最快的一条", C.crimsonSoft],
    ];
    stages.forEach((st, i) => {
      const x = M + i * 4.1;
      L.card(pres, s, x, 1.95, 3.9, 1.95, { fill: st[3], title: st[0], titleSize: 13, body: st[1] + "\n" + st[2], bodySize: 10 });
      if (i < 2) L.arrow(pres, s, x + 3.92, 2.9, 0.16, { color: C.crimson });
    });
    L.table(pres, s, [
      ["指标（模型值）", "2027", "2028", "2030"],
      ["核验小时数（含站内部署）", "3 万", "25 万", "400 万"],
      ["其中自营核验", "3 万", "10 万", "30 万"],
      ["每小时全负担成本（自营）", "245 元", "145 元", "85 元"],
      ["付费客户数", "5", "15", "80"],
      ["护栏装机台数", "—", "2 万", "30 万"],
      ["公司混合毛利率", "65%", "72%", "82%"],
    ], M, 4.15, 6.4, { colW: [2.9, 1.1, 1.1, 1.3], size: 9.5, rowH: 0.31, boldFirst: true });
    L.card(pres, s, 7.3, 4.15, 5.4, 2.35, { fill: C.panel, title: "客户扩展路径（净收入留存目标 > 130%）", body: "一家整机厂：先为一个数据集买护照（30–80 万）→ 训练团队把引擎装进站内（年费）→ 出货时护栏随底座预装（按台）。\n\n2027 年 800 万元基准的构成：认证证据 3 家（150–240 万）+ 引擎 2 家（200–400 万）+ 审计包 1 次发布（100–300 万）。\n\n2030 年 400 万小时中约 30 万小时自营（85 元 / 小时），其余在客户站内完成；护栏授权边际成本接近零。", bodySize: 10 });
    L.footer(pres, s, n, "来源：AXIOMALITY 单位经济模型；所有目标类指标均未签约。");
  }

  // ───────────────────────── 10. 市场 ─────────────────────────
  {
    const s = pres.addSlide(); n++;
    L.header(pres, s, { tag: "市场", title: "市场三级：近期可核查、中期是品类、长期是物理 AI 的许可层", sub: "中国整机出货约 80% 集中于两家厂商，数据标准可以集中制定；所缺的是使数据可验证、可流通的一层" });
    const tiers = [
      ["近期 2026–28", "可核查的收入", "整机厂认证证据与入表、训练场基础设施、护栏首批授权：1.5–4 千万元", C.panel2, C.text],
      ["中期 2029–30", "品类：具身智能的核验与证据层", "汽车与航空中验证与确认占软件投入三到五成；芯片行业的形式化验证工具是独立品类。国内 2030 年数十万台出货，品类 15–30 亿元，两三家分", C.ink2, C.white],
      ["长期 2031 起", "许可层：按台计费", "凡是 AI 驱动的物理设备都需要语义安全与证据；NVIDIA Halos 在西方的定位是「拥有安全标准即拥有监管护城河」，国内需要对等的一层", C.ink, C.white],
    ];
    tiers.forEach((t, i) => {
      const y = 1.95 + i * 1.12;
      const w = 4.6 + i * 0.9;
      s.addShape(pres.shapes.RECTANGLE, { x: M, y, w, h: 1.0, fill: { color: t[3] }, line: { color: t[3] } });
      L.label(pres, s, t[0], M + 0.2, y + 0.1, 1.5, 0.8, { head: true, size: 12, bold: true, color: t[4], valign: "middle" });
      L.label(pres, s, t[1], M + 1.75, y + 0.1, w - 1.95, 0.3, { head: true, size: 11, bold: true, color: t[4] });
      L.label(pres, s, t[2], M + 1.75, y + 0.4, w - 1.95, 0.55, { size: 9.5, color: t[4] === C.white ? "D9DCE8" : C.text });
    });
    // right facts
    const rx = 7.6;
    s.addChart(pres.charts.DOUGHNUT, [{ name: "出货集中度", labels: ["宇树 + 智元", "其他厂商"], values: [80, 20] }], {
      x: rx, y: 1.85, w: 2.3, h: 2.1, chartColors: [C.crimson, C.panel2], holeSize: 60, showLegend: false, showValue: false, showPercent: false, showTitle: false, dataLabelFontSize: 9,
    });
    L.label(pres, s, "80%", rx + 0.72, 2.55, 0.9, 0.5, { head: true, size: 20, bold: true, color: C.crimson, align: "center", valign: "middle" });
    L.label(pres, s, "2026 年中国人形出货集中度：宇树 + 智元近 80%（TrendForce 预测）", rx, 3.95, 2.4, 0.5, { size: 9, color: C.muted });
    const facts = [["140+ 家 · 330+ 款", "中国整机企业与型号（2025，工信部）"], ["1.7 万 → 6 万台", "全球人形出货 2025 → 中国 2026 预测；2030 年 50 万台"], ["9,700 / 5,900 台", "2026 上半年智元 / 宇树出货（Counterpoint）"], ["44 → 231 亿美元", "具身智能市场 2025 → 2030（CAGR 39%）"]];
    facts.forEach((f, i) => L.stat(pres, s, rx + 2.7 + (i % 2) * 1.35 * 0 , 1.9 + i * 0.85, 2.5, 0.8, f[0], f[1], { size: 16, labelSize: 9 }));
    L.card(pres, s, rx, 4.55, 5.1, 1.95, { fill: C.crimsonSoft, title: "对我们的含义", body: "本体集中于头部两家，数据格式与语义可集中统一，与头部整机厂对接即可覆盖多数真机数据；国家级训练场已积累 100 万+ 条真机数据，所缺为统一的核验与上架规范；数据资产化需要可校验的质量证据，否则无法入表、无法交易。", bodySize: 10, titleColor: C.crimson });
    L.footer(pres, s, n, "来源：MarketsandMarkets；工信部国新办发布会（2025）；TrendForce；Counterpoint（2026 H1）；SAG；国地中心；AXIOMALITY 测算。");
  }

  // ───────────────────────── 11. 为什么是现在 ─────────────────────────
  {
    const s = pres.addSlide(); n++;
    L.header(pres, s, { tag: "为什么是现在", title: "为什么是现在：标准已发布、入表已施行、欧盟时钟已设定，窗口在 2027 年内", sub: "三股力量同时到位：供给侧原始数据归零、需求侧合成数据涌入训练、制度侧要求逐条可追溯" });
    // timeline
    const events = [
      ["2024-01", "数据资产入表施行（财政部）"],
      ["2024-11", "可信数据空间行动计划（国家数据局）"],
      ["2026-02", "人形机器人与具身智能标准体系（2026 版）"],
      ["2026-06", "YD/T 6770—2026 基准测试方法实施；实景实训专项行动"],
      ["2026-11", "数据集质量要求及评价方法实施（GB/Z 218.1—2026）"],
      ["2027-12", "欧盟附录 III：独立高风险系统义务适用"],
      ["2028-08", "欧盟附录 I：嵌入机器人等产品的 AI 适用"],
    ];
    const tx = M, tw = W - 2 * M, ty = 2.55;
    s.addShape(pres.shapes.LINE, { x: tx, y: ty, w: tw, h: 0, line: { color: C.line, width: 1.5 } });
    events.forEach((e, i) => {
      const x = tx + (i + 0.5) * (tw / events.length);
      const hot = i >= 4;
      s.addShape(pres.shapes.OVAL, { x: x - 0.09, y: ty - 0.09, w: 0.18, h: 0.18, fill: { color: hot ? C.crimson : C.ink }, line: { color: hot ? C.crimson : C.ink } });
      L.label(pres, s, e[0], x - 0.8, ty - 0.5, 1.6, 0.3, { head: true, size: 11, bold: true, color: hot ? C.crimson : C.text, align: "center" });
      L.label(pres, s, e[1], x - 0.78, ty + 0.2, 1.56, 0.9, { size: 8.5, color: C.text, align: "center" });
    });
    L.pill(pres, s, "今天 2026-09 · 距附录 I 生效不足 23 个月", tx + tw / 2 - 1.9, 3.75, 3.8, 0.32, { size: 9.5 });
    const drivers = [
      ["TrendingDown", "供给侧：原始数据归零", "Build AI 免费开放约 100 万小时工厂视频；遥操作 50–200 美元 / 小时的价格没有护城河。仍有毛利的是语义、核验与认证。"],
      ["Sparkles", "需求侧：合成数据涌入", "World Labs Atlas（2026-09）以手机视频批量生成机器人相机数据；国内 2026 上半年世界模型融资超百亿元。生成器越多，进入训练前的核验与来源比例记录越是必需。"],
      ["Scale", "制度侧：逐条可追溯", "GB/Z 218.1 规定了质量要求但未规定证据格式；YD/T 6770 的评测集隔离仍靠自证；入表与附录 I 都要求机器可校验的记录。证据格式尚无人定义。"],
    ];
    for (let i = 0; i < 3; i++) {
      const x = M + i * 4.1;
      L.card(pres, s, x, 4.35, 3.9, 2.15, { fill: C.panel, title: drivers[i][1], titleIndent: 0.5, body: drivers[i][2], bodySize: 10 });
      await L.icon(s, drivers[i][0], x + 0.2, 4.5, 0.36, { bg: C.ink });
    }
    L.footer(pres, s, n, "来源：财政部（2023）；国家数据局（2024）；新华社（2026-02-28）；全国信标委；工信部；欧盟委员会 / Gibson Dunn（Regulation (EU) 2026/1744）；36 氪、虎嗅（2026）。");
  }

  // ───────────────────────── 12. 市场路径 ─────────────────────────
  {
    const s = pres.addSlide(); n++;
    L.header(pres, s, { tag: "市场路径", title: "三条渠道、一份首批客户清单、一个 8–12 周的付费试点", sub: "以实际护照促成合同：2026 年 12 月起，在保密协议下用合作伙伴自带数据生成真实护照，12 分钟演示" });
    const ch = [
      ["Layers", "底座与操作系统公司", "内核 API 嵌入底座与世界模型；护栏随操作系统预装，按台授权由渠道分发"],
      ["Briefcase", "四大与律所", "入表与审计项目由会计师事务所与律所带入；审计包经四大复核出具"],
      ["Building2", "训练场、认证机构与交易所", "北数所 2026-09 首发具身数据跨境流通平台：首批带护照数据集登记；与 CR 认证联盟 / 信通院联合发证；训练场存量数据以护照格式核验"],
    ];
    for (let i = 0; i < 3; i++) {
      const y = 1.95 + i * 1.05;
      await L.icon(s, ch[i][0], M, y + 0.05, 0.4, { bg: C.crimson });
      L.label(pres, s, ch[i][1], M + 0.55, y, 3.6, 0.3, { head: true, size: 12, bold: true });
      L.label(pres, s, ch[i][2], M + 0.55, y + 0.3, 3.6, 0.7, { size: 9.5, color: C.text });
    }
    L.table(pres, s, [
      ["首批目标客户（2026 Q4 – 2027）", "数量", "切入产品"],
      ["拟上市 / 出海人形与服务机器人整机厂", "5 家", "认证证据项目 → 护栏共同开发"],
      ["国家级训练场与实训空间", "2 家", "引擎站内部署（存量数据核验）"],
      ["数据商与数采工厂", "3 家", "护照按数据集；上架证据"],
      ["具身大脑 / 世界模型公司", "2 家", "合成数据核验与来源比例记录"],
      ["标准与认证机构（信通院 / CR 认证联盟）", "1–2 家", "技术底座与联合发证"],
    ], 4.95, 1.95, 3.75, { colW: [2.15, 0.6, 1.0], size: 8.5, rowH: 0.44, boldFirst: true });
    L.card(pres, s, 9.0, 1.95, 3.7, 3.2, { fill: C.ink, title: "付费试点：8–12 周", titleColor: C.white, body: "范围：一个任务族、一台本体、固定数据量与验收标准\n费用：30–80 万元，在首年引擎年费中抵扣\n盲测：同一批数据依次通过四档基线——客户现有脚本、几何规则、VLM + 规则、完整 Engine；专家真值独立建立\n验收指标：严重错误误放率、好数据误拒率、未知比例、每千条复核工时\n试点结果决定范围：否定结果预注册并保留，同样进入回流", bodySize: 9.5, bodyColor: "D9DCE8" });
    L.card(pres, s, M, 5.35, W - 2 * M, 1.15, { fill: C.crimsonSoft, title: "核心指标：每季度完成认证的核验数据小时数", body: "每一条收入线都在这个数字的下游；它同时刻画供给（采集与核验吞吐）、需求（愿为护照付费的客户）与质量（能通过核验的轨迹）。2027 年目标：核验通过率 ≥ 85%、内核覆盖度 ≥ 95%、认证时长 < 48 小时 / 千条。", bodySize: 10, titleColor: C.crimson });
    L.footer(pres, s, n, "来源：AXIOMALITY 试点方案（2026-09）；客户数量为目标，未签约。");
  }

  // ───────────────────────── 13. 进展与 90 天 ─────────────────────────
  {
    const s = pres.addSlide(); n++;
    L.header(pres, s, { tag: "进展", title: "已实现的是资产与关系，90 天内可验证的是三件事", sub: "三列分列，目标类指标均标注日期；正式路演前至少一家具名共同开发伙伴由「推进中」转为「已实现」" });
    const cols = [
      ["CircleCheck", "已实现", C.tealSoft, [
        "知识内核：公理经机器证明一致，对齐 ISO/IEC 21838-4",
        "10 万条实测三维数据包；房间级重建与物体级三维标注技术栈（9 项发明专利申请）",
        "消费级空间应用已上线（Apple Vision Pro）；13 项授权专利",
        "北京国际大数据交易所数据经纪商资质",
        "合规与审计合作：国际律师事务所（条款映射）、四大会计师事务所（审计包复核）",
      ]],
      ["Loader", "推进中", C.panel, [
        "核验引擎最小版本（2026 Q4 内测）：接入 → 场景图 → SMT 校验 → 护照",
        "家庭场景 Kernel v1；Engine 接入 LeRobot / RLDS / OpenUSD",
        "与人形整机厂、底座与操作系统公司洽谈共同开发与渠道合作",
        "强监管行业关系：跨国医疗器械与制药企业、国家标准机构、大型医院网络",
      ]],
      ["Target", "90 天内可验证（承诺）", C.crimsonSoft, [
        "公开盲测基准：在 DROID / AgiBot World 各 200 条轨迹上注入 7 类错误（错标、不可能关系、事件倒序、物体瞬移、时间扭曲、关节越限、夹爪–接触不一致），对比「规则 + VLM」基线，公布逐类查全率与每小时成本；第三方持有注入密钥",
        "签下 1 家具名共同开发伙伴（整机厂或训练场），以其自带数据生成真实护照，并公开验证器、公钥与样例护照供任何人离线复验",
        "Passport v1 字段对齐《具身智能数据集质量要求及评价方法》八维指标（2026-11-01 实施）与 CR-3-06，提交信通院或 CR 认证联盟之一",
      ]],
    ];
    for (let i = 0; i < 3; i++) {
      const x = M + i * 4.1;
      L.card(pres, s, x, 1.95, 3.9, 3.6, { fill: cols[i][2], title: cols[i][1], titleIndent: 0.5 });
      await L.icon(s, cols[i][0], x + 0.2, 2.1, 0.36, { bg: i === 2 ? C.crimson : C.ink });
      L.bullets(pres, s, x + 0.22, 2.6, 3.46, 2.85, cols[i][3], { size: 9.5, paraSpace: 5 });
    }
    L.table(pres, s, [
      ["有日期的目标", "2027 Q1", "2027 Q2", "2027 年底", "2028"],
      ["里程碑", "3 家共同开发伙伴；1 万条核验轨迹", "Passport v1 获 1 家监管机构或标准组织认可", "5 家付费客户、800 万元收入", "附录 I 生效前交付审计包；3,000 万元收入"],
    ], M, 5.75, W - 2 * M, { colW: [1.6, 2.6, 2.7, 2.4, 2.83], size: 9, rowH: 0.34, boldFirst: true });
    L.footer(pres, s, n, "来源：AXIOMALITY 内部记录（可应要求提供）；目标为计划值，未签约。");
  }

  // ───────────────────────── 14. 团队 ─────────────────────────
  {
    const s = pres.addSlide(); n++;
    L.header(pres, s, { tag: "团队", title: "团队：写过国际标准公理，证明过一致性，也做过 5,000 万美元收入的公司", sub: "本体与标准、AI 算法、感知与机器人、仿真与三维资产四条能力线" });
    L.card(pres, s, M, 1.95, 6.2, 4.55, { fill: C.ink, title: "创始人 & CEO", titleColor: C.white, titleSize: 15 });
    L.bullets(pres, s, M + 0.22, 2.5, 5.8, 3.9, [
      { text: "稀缺性一 · 标准：ISO/IEC 21838-4（TUpper 顶层本体）核心构建者，承担 35 项中 22 项；国际工业本体联盟成员；多伦多大学人工智能博士与研究员", options: { color: C.white } },
      { text: "稀缺性二 · 科学：形式化本体与知识表示、一阶逻辑公理体系的一致性证明与模型构造、可信神经符号 AI；21 篇 SCI / 顶会论文，FOIS 杰出论文奖，AAAI 特邀报告，1 部英文专著", options: { color: C.white } },
      { text: "稀缺性三 · 经营：跨境 DTC 平台创始团队成员，获 Accel 等美国头部风投 500 万美元天使投资，一年内年收入超 5,000 万美元，带领 100+ 人团队；联合创办推荐系统公司（多伦多大学与帝国理工孵化）", options: { color: C.white } },
      { text: "空间计算：创办空间计算公司，Apple Vision Pro 首批 AR 应用之一；13 项授权专利，2,400 万元专利转让、1,000 万元技术许可；主持 3 项国际科研项目", options: { color: C.white } },
      { text: "投资视角：曾在头部风险投资机构从事商业尽调与投资研究", options: { color: C.white } },
    ], { size: 10.5, paraSpace: 7 });
    const team = [
      ["CTO & 首席科学家", "麦克马斯特大学 AI 博士；曾任一线大厂 AI 算法科学家、创业公司首席科学家；深圳海外高层次人才；加拿大 AI 学术与工业应用大赛第一名"],
      ["感知与机器人负责人", "哈尔滨工业大学机械电子工程博士；曾任小鹏汽车 AI 算法工程师、智能感知中心总监；论文 10 余篇"],
      ["仿真与三维资产负责人", "10 年+ 游戏与舞台美术总监经验；主导 1750 年北京古城数字（VR）重建；中国国家画院特聘讲师"],
    ];
    team.forEach((t, i) => L.card(pres, s, 7.1, 1.95 + i * 1.17, 5.6, 1.05, { fill: C.panel, title: t[0], titleSize: 11.5, body: t[1], bodySize: 9.5 }));
    L.card(pres, s, 7.1, 5.5, 5.6, 1.0, { fill: C.crimsonSoft, title: "本轮要补的三个人", titleColor: C.crimson, titleSize: 11.5, body: "训练过 VLA 策略的机器人学习科学家（负责核验与训练收益的实验）；在国地中心 / 信通院 / 智元体系交付过数据的中国产业侧联合创始人；面向整机厂与训练场的销售负责人。", bodySize: 9.5 });
    L.footer(pres, s, n);
  }

  // ───────────────────────── 15. 财务与融资 ─────────────────────────
  {
    const s = pres.addSlide(); n++;
    L.header(pres, s, { tag: "财务与融资", title: "财务：2030 年收入 2.2 亿元、毛利率 82%；本轮融资支撑 18 个月三项门槛", sub: "认证证据先行，经常性收入（护栏 + 引擎）于 2029 年超过按次的证据收入" });
    s.addChart(pres.charts.BAR, [
      { name: "认证证据", labels: ["2027", "2028", "2029", "2030"], values: [5, 15, 35, 70] },
      { name: "引擎站内部署", labels: ["2027", "2028", "2029", "2030"], values: [3, 9, 25, 50] },
      { name: "语义护栏授权", labels: ["2027", "2028", "2029", "2030"], values: [0, 3, 20, 70] },
      { name: "评测套件", labels: ["2027", "2028", "2029", "2030"], values: [0, 3, 10, 30] },
    ], {
      x: M, y: 1.95, w: 6.3, h: 3.0, barDir: "col", barGrouping: "stacked", chartColors: [C.crimson, C.ink, C.teal, C.amber],
      showValue: false, showLegend: true, legendPos: "b", legendFontSize: 9, legendFontFace: F.body,
      catAxisLabelFontSize: 9, valAxisLabelFontSize: 9, catAxisLabelColor: C.muted, valAxisLabelColor: C.muted,
      valGridLine: { color: "E5E7EB", size: 0.5 }, catGridLine: { style: "none" }, showTitle: true, title: "分产品收入（百万元，示意）", titleFontSize: 11, titleFontFace: F.body, titleColor: C.text,
      catAxisLabelFontFace: F.body, valAxisLabelFontFace: F.body,
    });
    L.table(pres, s, [
      ["2030 年情景", "保守", "基准", "乐观"],
      ["收入", "4,000 万元", "2.2 亿元", "5 亿元"],
      ["客户数", "20", "80", "150"],
      ["触发条件", "护照未进入评价方法；仅证据与项目收入", "附录 I 如期；护栏 30 万台；一家机构纳入护照", "护照进入 CR 实施规则；护栏预装 80 万台"],
    ], M, 5.1, 6.3, { colW: [1.1, 1.6, 1.8, 1.8], size: 8.5, rowH: 0.34, boldFirst: true });
    // ask
    L.card(pres, s, 7.2, 1.95, 5.5, 4.55, { fill: C.ink, title: "本轮融资（Pre-A）", titleColor: C.white, titleSize: 15 });
    L.label(pres, s, "建议 3,000–5,000 万元", 7.42, 2.5, 5.0, 0.5, { head: true, size: 22, bold: true, color: C.crimson });
    L.label(pres, s, "（金额为本次修订建议，按 25 人团队 18 个月运行与三项门槛测算；请创始团队确认）", 7.42, 3.0, 5.0, 0.4, { size: 9, color: "9AA0B4" });
    L.table(pres, s, [
      ["资金用途", "占比", "对应门槛"],
      ["内核与引擎研发", "45%", "门槛 1：内核 v1 一致性证明发布；Engine 内测接入三种格式；3 家共同开发伙伴"],
      ["首批客户交付与试点", "25%", "门槛 2：5 家付费客户、800 万元；1 家机构纳入护照"],
      ["团队（机器人学习科学家、销售）", "20%", "门槛 3：审计包在附录 I 生效前交付；3,000 万元收入"],
      ["标准、合规与审计合作", "10%", "训练场试点、标准工作组席位、监管沙盒"],
    ], 7.42, 3.5, 5.05, { colW: [1.7, 0.55, 2.8], size: 8.5, rowH: 0.5, headFill: C.crimson });
    L.label(pres, s, "投入方向是内核覆盖度而非采集规模：每 500 万元研发投入 → 覆盖度 +5 个百分点、核验成本 −40%。", 7.42, 6.05, 5.05, 0.4, { size: 9, italic: true, color: "D9DCE8" });
    L.footer(pres, s, n, "说明：财务预测为示意；目标类指标未签约；融资金额与用途为修订建议。");
  }

  // ───────────────────────── 16. 结语 ─────────────────────────
  {
    const s = pres.addSlide(); n++;
    L.darkBg(pres, s);
    L.label(pres, s, "AXIOMALITY", M, 0.55, 4, 0.35, { size: 13, bold: true, color: C.white, extra: { charSpacing: 4 } });
    L.label(pres, s, "核验数据的证据格式，\n将决定具身智能数据的计量与交易单位。", M, 1.5, 11, 1.7, { head: true, size: 30, bold: true, color: C.white, ls: 1.15 });
    L.label(pres, s, "我们要做的，是让这个格式成为参考实现——内核规范公开、护照离线可验、审计包经会计师事务所复核、不持有客户数据、不训练自有基础模型。", M, 3.35, 11, 0.8, { size: 13, color: "C9CDDB" });
    const asks = [
      ["Handshake", "领投本轮", "Pre-A，18 个月三项门槛，投入方向是内核覆盖度"],
      ["Network", "三个介绍", "一家拟上市 / 出海整机厂、一家国家级训练场、一家底座或操作系统公司"],
      ["FileCheck", "一次验证", "2026 年 12 月起，以您被投企业的自带数据在保密协议下生成真实护照，12 分钟"],
    ];
    for (let i = 0; i < 3; i++) {
      const x = M + i * 4.1;
      s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y: 4.55, w: 3.9, h: 1.75, fill: { color: C.ink2 }, line: { color: C.ink2 }, rectRadius: 0.08 });
      await L.icon(s, asks[i][0], x + 0.22, 4.75, 0.4, { bg: C.crimson });
      L.label(pres, s, asks[i][1], x + 0.75, 4.78, 3.0, 0.35, { head: true, size: 14, bold: true, color: C.white });
      L.label(pres, s, asks[i][2], x + 0.22, 5.3, 3.5, 0.9, { size: 10.5, color: "D9DCE8" });
    }
    L.label(pres, s, "© 2026 AXIOMALITY  ·  保密  ·  未经许可不得传播", M, H - 0.5, 8, 0.3, { size: 9, color: "9AA0B4" });
  }

  fs.mkdirSync(path.dirname(OUT), { recursive: true });
  await pres.writeFile({ fileName: OUT });
  console.log("wrote", OUT, "slides:", n);
})().catch((e) => { console.error(e); process.exit(1); });
