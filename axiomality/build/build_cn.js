// AXIOMALITY — 红杉版路演稿 v2（14 页，不含融资）
// 定位：具身数据采购的第三方验收——先验货，再付款
const L = require("./lib");
const { C, W, H, M } = L;
const path = require("path");
const fs = require("fs");

const MEDIA = __dirname;
const PROTO = "/home/user/ipython/axiomality/prototype";
const DEMO = require("./demo_numbers.json"); // filled from prototype results
const OUT = process.argv[2] || path.join(__dirname, "out", "AXIOMALITY_红杉版_路演稿_v2.pptx");
const FOOT = "AXIOMALITY  ·  路演稿  ·  2026 年 10 月  ·  保密";

function fig(name) { const p = path.join(PROTO, "figures", name); return fs.existsSync(p) ? p : null; }

(async () => {
  const pres = L.newDeck("zh", { title: "AXIOMALITY 路演稿", footer: FOOT });
  const F = pres._F;
  let n = 0;

  // 1 ── 封面
  {
    const s = pres.addSlide(); n++;
    L.darkBg(pres, s);
    L.label(pres, s, "AXIOMALITY", M, 0.55, 4, 0.35, { size: 13, bold: true, color: C.white, extra: { charSpacing: 4 } });
    L.label(pres, s, "具身数据，\n先验货，再付款。", M, 1.4, 7.4, 2.0, { head: true, size: 40, bold: true, color: C.white, ls: 1.12 });
    L.label(pres, s, "具身智能数据采购的第三方验收：一批数据进来，逐条裁决出去，附一张买卖双方都能离线复验的签名验收单。", M, 3.55, 7.2, 0.9, { size: 15, color: "C9CDDB" });
    L.pill(pres, s, "内部原型已跑通 · 见第 5 页", M, 4.55, 2.9, 0.36, { fill: C.teal, color: C.white, size: 10.5 });
    const img = path.join(MEDIA, "cover_crop.png");
    s.addShape(pres.shapes.RECTANGLE, { x: 8.3, y: 1.35, w: 4.45, h: 2.6, fill: { color: C.ink2 }, line: { color: C.ink2 } });
    s.addImage({ path: img, x: 8.45, y: 1.92, w: 4.15, h: 1.46 });
    L.brackets(pres, s, 8.3, 1.35, 4.45, 2.6, C.crimson, 0.22, 1.5);
    L.label(pres, s, "公司实测样本 429：点云与三维标注框（真实数据）", 8.3, 4.02, 4.45, 0.3, { size: 9.5, color: "9AA0B4" });
    const stats = [
      [DEMO.cn_cover_big, DEMO.cn_cover_label],
      ["签名 · 离线可验", "Ed25519 签名验收单；改任一条目字段或计数即验签失败"],
      ["10 万条", "实测三维几何数据包（桌面物体扫描），原型的几何来源"],
      ["ISO/IEC 21838-4", "创始人为顶层本体 TUpper 标准核心贡献者"],
    ];
    stats.forEach((st, i) => {
      const x = M + i * 3.05;
      s.addShape(pres.shapes.LINE, { x, y: 5.35, w: 2.7, h: 0, line: { color: "3A4160", width: 0.75 } });
      L.stat(pres, s, x, 5.45, 2.85, 1.2, st[0], st[1], { dark: true, size: 19, labelSize: 10 });
    });
    s.addNotes("30 秒开场：数采中心卖数据，整机厂和大脑公司买数据，但中间没有验收环节。我们做第三方验收：逐条裁决、拒收附依据、签名验收单双方可复验。原型已经跑通，第 5 页是实测。");
  }

  // 2 ── 问题
  {
    const s = pres.addSlide(); n++;
    L.header(pres, s, { tag: "问题", title: "数采中心在「露馅」：买方花钱，却没有一张验收单", sub: "具身数据已经在大规模买卖，但交易里缺了最基本的一环——验货" });
    // flow: seller -> [gap] -> buyer
    const fy = 2.1;
    L.card(pres, s, M, fy, 3.6, 1.55, { fill: C.panel, title: "卖方：数采中心 · 数采工厂", body: "全国 64 座数采中心 / 训练场，覆盖 27 城；真机数据报价 500–1,000 元 / 小时", bodySize: 10.5 });
    L.card(pres, s, W - M - 3.6, fy, 3.6, 1.55, { fill: C.panel, title: "买方：整机厂 · 具身大脑公司", body: "按小时付费，入库后靠人工抽检；训练失败后才回头查数据", bodySize: 10.5 });
    const gx = M + 3.85, gw = W - 2 * M - 7.7;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: gx, y: fy, w: gw, h: 1.55, fill: { color: C.crimsonSoft }, line: { color: C.crimson, width: 1, dashType: "dash" }, rectRadius: 0.08 });
    L.label(pres, s, "缺失的一环：验收", gx + 0.2, fy + 0.18, gw - 0.4, 0.35, { head: true, size: 14, bold: true, color: C.crimson, align: "center" });
    L.label(pres, s, "没有逐条裁决 · 没有拒收依据 · 没有双方都认的记录\n卖方只能自证，买方不信", gx + 0.2, fy + 0.6, gw - 0.4, 0.8, { size: 10.5, color: C.text, align: "center" });
    L.arrow(pres, s, M + 3.62, fy + 0.78, 0.2, { color: C.crimson });
    L.arrow(pres, s, gx + gw + 0.02, fy + 0.78, 0.2, { color: C.crimson });

    const st = [["64 座", "数采中心 / 训练场，覆盖 27 城"], ["500–1,000 元", "真机数据每小时市场报价"], ["2026-09-20", "虎嗅：数采中心「开始批量露馅」，数据无效、无人买单"], ["0 项", "现行标准中规定了「证据格式」的数量"]];
    st.forEach((x, i) => L.stat(pres, s, M + i * 3.05, 4.05, 2.9, 1.15, x[0], x[1], { size: 22, labelSize: 10 }));
    L.card(pres, s, M, 5.45, W - 2 * M, 1.05, { fill: C.panel, body: "标准只规定了「好数据长什么样」，没有规定「怎么证明」：信通院《具身智能数据集质量要求及评价方法》（2026-11-01 实施）给出八维质量指标，GB/Z 218.1—2026 是指导性技术文件，二者都没有规定逐条可校验的证据格式。公开检索未见中立方出具可离线复验的逐条验收记录。", bodySize: 10.5 });
    L.footer(pres, s, n, "来源：澎湃新闻（2026）；虎嗅《遍地开花的数采中心，开始批量露馅》（2026-09-20）；21 财经（2026-08-05）；全国标准信息公共服务平台。");
  }

  // 3 ── 一个采购负责人的一天
  {
    const s = pres.addSlide(); n++;
    L.header(pres, s, { tag: "场景", title: "一个数据采购负责人的一天：今天 vs 有验收单之后", sub: "情景示意：某具身大脑公司采购一批 5,000 条厨房操作数据" });
    const rows = [
      ["收货", "硬盘 / 网盘到货，格式各异，先花两天转格式", "原型已原生读取 RLDS 并转为 LeRobot 格式（MCAP 规划中），当天出逐条裁决"],
      ["验货", "人工抽检一小部分，看视频、凭经验", "100% 逐条检查：结构、运动学、语义逻辑三层"],
      ["付款", "按合同小时数全额付款", "按「通过」条数付款；拒收条目附依据，退回补采"],
      ["训练", "成功率不稳定，不知道是模型问题还是数据问题", "训练集只含通过条目；有效失败单独保留、单独标注"],
      ["回查", "两周翻日志，和供应商扯皮", "从验收单直接定位到帧、规则与批次"],
    ];
    L.label(pres, s, "今天", M + 1.5, 1.95, 5.1, 0.35, { head: true, size: 14, bold: true, color: C.muted });
    L.label(pres, s, "有验收单之后", M + 6.9, 1.95, 5.2, 0.35, { head: true, size: 14, bold: true, color: C.teal });
    rows.forEach((r, i) => {
      const y = 2.4 + i * 0.8;
      L.stepChip(pres, s, M, y + 0.12, i + 1, { d: 0.42, fill: C.ink });
      L.label(pres, s, r[0], M + 0.55, y + 0.12, 0.9, 0.42, { head: true, size: 13, bold: true, valign: "middle" });
      s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: M + 1.5, y, w: 5.2, h: 0.66, fill: { color: C.panel }, line: { color: C.panel }, rectRadius: 0.06 });
      L.label(pres, s, r[1], M + 1.65, y + 0.05, 4.9, 0.56, { size: 10.5, valign: "middle", color: C.muted });
      L.arrow(pres, s, M + 6.72, y + 0.33, 0.16, { color: C.crimson });
      s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: M + 6.9, y, w: 5.23, h: 0.66, fill: { color: C.tealSoft }, line: { color: C.tealSoft }, rectRadius: 0.06 });
      L.label(pres, s, r[2], M + 7.05, y + 0.05, 4.95, 0.56, { size: 10.5, valign: "middle" });
    });
    L.footer(pres, s, n, "情景示意，非客户引语；流程依据对数采与训练流程的公开报道整理。");
  }

  // 4 ── 产品
  {
    const s = pres.addSlide(); n++;
    L.header(pres, s, { tag: "产品", title: "一批数据进，一张验收单出", sub: "三层检查逐条执行，每条得到通过 / 修复 / 拒收 / 未知，附定位到帧与规则的依据" });
    const layers = [
      ["ListChecks", "结构层", "时间戳单调、丢帧、NaN、关节限位、元数据完整", "规则脚本能做，我们也做"],
      ["Move3D", "运动学与几何层", "物体穿模、悬空无支撑、瞬移（超速）、夹爪与物体距离", "需要场景几何与物体关系"],
      ["Network", "语义逻辑层", "任务阶段顺序、夹爪状态与接触事件一致、类别与可供性相符", "需要经证明无矛盾的规则库"],
    ];
    for (let i = 0; i < 3; i++) {
      const y = 2.0 + i * 1.05;
      s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: M, y, w: 7.4, h: 0.92, fill: { color: i === 2 ? C.ink : C.panel }, line: { color: i === 2 ? C.ink : C.panel }, rectRadius: 0.08 });
      await L.icon(s, layers[i][0], M + 0.2, y + 0.24, 0.44, { bg: C.crimson });
      L.label(pres, s, layers[i][1], M + 0.8, y + 0.1, 2.2, 0.35, { head: true, size: 13, bold: true, color: i === 2 ? C.white : C.text });
      L.label(pres, s, layers[i][2], M + 0.8, y + 0.47, 4.3, 0.4, { size: 10, color: i === 2 ? "D9DCE8" : C.text });
      L.label(pres, s, layers[i][3], M + 5.2, y + 0.1, 2.05, 0.72, { size: 9.5, italic: true, color: i === 2 ? "F4A3B5" : C.muted, valign: "middle" });
    }
    L.table(pres, s, [
      ["裁决", "含义", "处理"],
      ["通过", "三层检查均无矛盾", "进入可付款、可训练的集合"],
      ["修复", "可纠正的记录错误（如时间戳乱序）", "生成派生版本，原始记录保留"],
      ["拒收", "违反规则，附帧号与规则编号", "退回卖方，作为补采依据"],
      ["未知", "缺少判定所需的输入", "明确列出缺什么，不当作通过"],
    ], M, 5.25, 7.4, { colW: [0.9, 3.4, 3.1], size: 9.5, rowH: 0.25, boldFirst: true });

    // right: principle cards
    const pr = [
      ["有效失败必须保留", "杯子真的滑落是有价值的失败样本，不是坏数据；引擎不会把真实失败改写成成功。"],
      ["签名验收单", "绑定数据哈希与规则库版本；卖方、买方、第三方用公钥即可离线复验，不依赖我们的服务。"],
      ["客户环境内运行", "数据不出客户机房；我们交付引擎与规则库，不持有数据。"],
    ];
    pr.forEach((p, i) => L.card(pres, s, 8.35, 2.0 + i * 1.52, 4.4, 1.38, { fill: i === 1 ? C.tealSoft : C.panel, title: p[0], titleSize: 12.5, body: p[1], bodySize: 10 }));
    L.footer(pres, s, n);
  }

  // 5 ── Demo A：真实数据
  {
    const s = pres.addSlide(); n++;
    L.header(pres, s, { tag: "DEMO · 真实数据", title: "真实数据上，结构基线漏掉的：卡死 / 冻结、缺指令、字段说明错误", sub: "Open X-Embodiment 公开数据：DROID（Franka）、Jaco Play（Kinova）、NYU ROT（xArm）共 41 条轨迹、3,870 帧" });
    const f = fig("real_finding_example.png");
    if (f) s.addImage({ path: f, x: M, y: 1.98, w: 7.4, h: 3.7 });
    const finds = [
      ["机械臂卡死 / 数据流冻结", "DROID 第 3 条，第 19–33 帧：指令关节位置在动（中位差 0.133 rad），实测关节逐位不变；第 43–49 帧整行重复。用它训练，策略会学到「指令无效」。"],
      ["关节越限", "DROID 第 1 条，第 141–172 帧：关节 6 达 3.959 rad，超出 Panda 手册上限 207 mrad（也可能是 FR3 机型，其上限 4.52 rad——验收单会把这个歧义写明）。"],
      ["字段说明与数值不符", "DROID 的 action 字段文档写「6 个关节速度」，实际 2,551 帧全部等于指令笛卡尔位姿。另有 8/14 条缺少任何语言指令。"],
    ];
    finds.forEach((t, i) => L.card(pres, s, 8.2, 1.98 + i * 1.5, 4.55, 1.38, { fill: i === 0 ? C.crimsonSoft : C.panel, title: t[0], titleSize: 11.5, titleColor: i === 0 ? C.crimson : C.text, body: t[1], bodySize: 9 }));
    L.table(pres, s, [
      ["数据集", "轨迹 / 帧", "通过*", "修复", "拒收", "未检项", "验收单"],
      ["DROID（Franka）", "14 / 2,551", "5", "1", "8", "时间戳、语义", "离线验签通过"],
      ["Jaco Play（Kinova）", "13 / 879", "13", "0", "0", "时间戳、语义", "离线验签通过"],
      ["NYU ROT（xArm）", "14 / 440", "14", "0", "0", "时间戳、语义", "离线验签通过"],
    ], M, 5.78, 7.4, { colW: [1.7, 1.15, 0.65, 0.6, 0.6, 1.3, 1.4], size: 8.5, rowH: 0.21, boldFirst: true });
    L.footer(pres, s, n, "真实公开数据（OXE 公共存储桶）。*仅指可检项通过：这些数据集没有时间戳和物体状态，相关检查未执行。DROID 上结构基线与引擎的通过 / 拒收一致 8/14；卡死、越限两条均在 DROID 自标为 failure 的轨迹中。");
  }

  // 6 ── Demo B：诚实对比
  {
    const s = pres.addSlide(); n++;
    L.header(pres, s, { tag: "DEMO · 合成基准", title: "检出与强基线持平：我们卖的不是更聪明的检查，而是双方都认的验收单", sub: "含噪声的合成数据：3 种任务变体、每类错误 20 条、容差在独立数据上校准；三方都不读注入密钥；精确率三方均为 1.00" });
    const f = fig("benchmark_v2_sensitivity.png");
    if (f) s.addImage({ path: f, x: M, y: 1.98, w: 6.9, h: 6.9 * 0.4062 });
    L.table(pres, s, [
      ["", "AXIOMALITY 引擎", "我们的强基线（写于引擎之后）", "结构基线（半天）"],
      ["检出率", "92%", "92%", "41%"],
      ["干净样本误拒（140 条）", "0", "0", "0"],
      ["时间戳乱序：字节级还原", "20 / 20", "0（直接丢弃）", "0（直接丢弃）"],
      ["缺输入时", "返回「未知」", "拒收", "拒收"],
      ["每条耗时", "14 ms", "1.4 ms", "0.6 ms"],
    ], M, 4.92, 7.9, { colW: [2.5, 1.8, 1.8, 1.8], size: 9, rowH: 0.26, boldFirst: true });
    const pts = [
      ["我们不回避的结论", "强规则基线在检出率上和我们持平。只靠「会写检查」建不起壁垒——任何团队知道要抓什么，就能写出来。"],
      ["细节优势（基线约一天可追平，不作壁垒）", "更小的误差：物体下陷 25 mm 起即可检出（基线 40 mm），松手后跳动 30 mm 起（基线 60 mm）；时间戳乱序可字节级还原；缺输入返回「未知」而非误杀；每条裁决引用规则编号。"],
      ["所以壁垒在哪里", "中立出具、结论可复算、验收单离线可验，加上跨客户累积的错误库——这是单个买方或卖方自己写不出来的。"],
    ];
    pts.forEach((t, i) => L.card(pres, s, 8.75, 1.98 + i * 1.55, 4.0, 1.43, { fill: i === 2 ? C.tealSoft : C.panel, title: t[0], titleSize: 11, body: t[1], bodySize: 8.8 }));
    L.footer(pres, s, n, "内部原型，合成数据；注入器、引擎与基线出自同一团队。完整结果与代码：prototype/results/benchmark_v2.md，一条命令复现。");
  }

  // 6 ── 单位经济
  {
    const s = pres.addSlide(); n++;
    L.header(pres, s, { tag: "单位经济", title: "验收费远小于坏数据的损失", sub: "测算示意：一次 1 万小时的数据采购；参数可替换，真实值在首个付费试点中逐批测量" });
    const inputs = [
      ["采购量", "10,000 小时"],
      ["采购单价", "750 元 / 小时（市场报价 500–1,000 元区间中值）"],
      ["采购额", "750 万元"],
      ["无效数据比例（假设）", "15%（媒体报道「批量露馅」，真实比例待 PoC 实测）"],
    ];
    L.label(pres, s, "输入", M, 1.95, 5, 0.35, { head: true, size: 13, bold: true });
    inputs.forEach((r, i) => {
      const y = 2.35 + i * 0.5;
      s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: M, y, w: 6.2, h: 0.42, fill: { color: C.panel }, line: { color: C.panel }, rectRadius: 0.05 });
      L.label(pres, s, r[0], M + 0.15, y + 0.04, 1.9, 0.34, { size: 10.5, bold: true, valign: "middle" });
      L.label(pres, s, r[1], M + 2.1, y + 0.04, 4.0, 0.34, { size: 10.5, valign: "middle" });
    });
    s.addChart(pres.charts.BAR, [{ name: "万元", labels: ["直接损失：无效数据采购款", "间接损失：训练算力与工程回查（下限，按直接损失 50% 估）", "验收费（目标：采购额 6%）"], values: [112.5, 56.25, 45] }], {
      x: M, y: 4.45, w: 6.2, h: 2.05, barDir: "bar", chartColors: [C.crimson, "E07A93", C.teal], showValue: true, dataLabelPosition: "outEnd", dataLabelFontSize: 9, dataLabelColor: C.text,
      catAxisLabelFontSize: 8.5, valAxisHidden: true, valGridLine: { style: "none" }, catGridLine: { style: "none" }, showLegend: false, catAxisLabelColor: C.text, catAxisLabelFontFace: F.body, dataLabelFontFace: F.body, varyColors: true,
    });
    // right side: explanation
    L.stat(pres, s, 7.2, 1.95, 5.5, 1.2, "168 万 vs 45 万", "一次采购的坏数据损失 vs 验收费（示意）；按本页假设，无效比例 ≥ 4% 买方即回本，不计间接损失时 ≥ 6%", { size: 30, labelSize: 10.5 });
    L.card(pres, s, 7.2, 3.3, 5.5, 1.45, { fill: C.panel, title: "谁付钱", titleSize: 12, body: "买方付：少付无效数据的钱，并省掉回查成本。\n卖方也愿意付：带验收单的数据更容易成交、更快回款，优质卖方借此与「露馅」的同行拉开差距。", bodySize: 10 });
    L.card(pres, s, 7.2, 4.9, 5.5, 1.6, { fill: C.crimsonSoft, title: "我们在试点中逐批记录的真实数字", titleColor: C.crimson, titleSize: 12, body: "无效比例 · 每千条人工复核工时 · 验收单对成交价与回款周期的影响 · 每小时验收的实际成本（VLM 推理、求解器、人工复核分项）", bodySize: 10 });
    L.footer(pres, s, n, "测算示意：采购单价取公开报价区间中值；无效比例与间接损失为假设；验收费率为目标值，均未经客户验证。");
  }

  // 7 ── 为什么是现在
  {
    const s = pres.addSlide(); n++;
    L.header(pres, s, { tag: "为什么是现在", title: "2026 下半年：数据开始买卖，质量开始出事，规则刚刚落地", sub: "供给过剩、质量失真、标准只给指标不给证据——验收环节的窗口就在这 12 个月" });
    const events = [
      ["2025-09", "智元获首张人形机器人数据集 CR 认证（CR-3-06）"],
      ["2026-06", "YD/T 6770—2026 基准测试方法实施；实景实训专项行动"],
      ["2026-09", "北数所首发具身智能数据要素跨境流通平台"],
      ["2026-09-20", "虎嗅：数采中心开始批量露馅"],
      ["2026-11-01", "信通院《具身智能数据集质量要求及评价方法》实施"],
    ];
    const tx = M, tw = W - 2 * M, ty = 2.6;
    s.addShape(pres.shapes.LINE, { x: tx, y: ty, w: tw, h: 0, line: { color: C.line, width: 1.5 } });
    events.forEach((e, i) => {
      const x = tx + (i + 0.5) * (tw / events.length);
      const hot = i >= 3;
      s.addShape(pres.shapes.OVAL, { x: x - 0.09, y: ty - 0.09, w: 0.18, h: 0.18, fill: { color: hot ? C.crimson : C.ink }, line: { color: hot ? C.crimson : C.ink } });
      L.label(pres, s, e[0], x - 1.1, ty - 0.5, 2.2, 0.3, { head: true, size: 12, bold: true, color: hot ? C.crimson : C.text, align: "center" });
      L.label(pres, s, e[1], x - 1.15, ty + 0.2, 2.3, 0.8, { size: 9.5, align: "center" });
    });
    const drivers = [
      ["Factory", "供给过剩", "64 座数采中心、京东计划 60 万人两年采 1,000 万小时第一视角视频；Build AI 免费开放约 100 万小时工厂视频。原始小时数不再稀缺，稀缺的是能证明可用的小时数。"],
      ["TriangleAlert", "质量出事", "数采中心「露馅」、有效性被公开质疑。买方开始要求验收，卖方开始需要证明自己。"],
      ["Scale", "规则落地", "信通院八维指标 11-01 实施，买卖双方第一次有了共同的质量语言，但仍缺一张可逐条复验的验收单——我们把八维指标变成机器可校验的字段。"],
    ];
    for (let i = 0; i < 3; i++) {
      const x = M + i * 4.1;
      L.card(pres, s, x, 3.9, 3.9, 2.6, { fill: C.panel, title: drivers[i][1], titleIndent: 0.5, body: drivers[i][2], bodySize: 10 });
      await L.icon(s, drivers[i][0], x + 0.2, 4.05, 0.36, { bg: C.ink });
    }
    L.footer(pres, s, n, "来源：央广网（2025-09）；新华网（2026-06-01）；北数所（2026-09）；虎嗅（2026-09-20）；21 财经（2026-08-05）；量子位（2026-04，京东）；Build AI（2026-04）。");
  }

  // 8 ── 竞争
  {
    const s = pres.addSlide(); n++;
    L.header(pres, s, { tag: "竞争", title: "真正的对手是「自检」和认证机构，不是另一家创业公司", sub: "公开检索未见中立方出具可离线复验的逐条验收记录；我们靠「可复算」保证中立" });
    const Y = "●", P = "◐", N = "○";
    L.table(pres, s, [
      ["", "买方自建质检\n（国地中心、京东、智元）", "卖方自检\n（数采中心）", "认证机构\n（CR-3-06、信通院评测）", "NVIDIA Cosmos Evaluator\n（免费打分）", "AXIOMALITY"],
      ["中立：买卖双方都认", N, N, Y, P, P + " 需隔离"],
      ["逐条裁决，不是抽样", P, P, N, Y, Y],
      ["语义与物理关系检查（阶段、接触、穿模、瞬移）", P, N, N, P, P + " 原型"],
      ["结论可复算、签名离线可验", N, N, N, N, Y],
      ["按批交付，天级周期", Y, Y, N, Y, P + " 原型"],
      ["公信力与渠道", P, N, Y, P, N + " 待建"],
    ], M, 1.95, W - 2 * M, { colW: [3.2, 1.95, 1.55, 2.0, 2.0, 1.43], size: 9.5, rowH: 0.36, boldFirst: true });
    L.label(pres, s, "●  具备     ◐  部分     ○  不具备", M, 4.75, 5, 0.25, { size: 9, color: C.muted });
    const notes = [
      ["与认证机构：做底座，不抢证", "CR 认证是一次性审核加证书，信通院是抽样评测。我们把八维指标变成逐条可校验的字段，做它们评价结果的机器可验载体。"],
      ["与买方自建：中立才有意义", "卖方的自检买方不认，买方的自检卖方不认。验收单要双方都认，只能由第三方出具，并且任何人都能复算。"],
      ["与 NVIDIA：打分 ≠ 验收", "Cosmos Evaluator 给生成数据打合理性分，但不签名、不做逐条规则裁决、绑定 NVIDIA 栈。我们把它当作输入之一，而不是对手。"],
    ];
    notes.forEach((t, i) => L.card(pres, s, M + i * 4.1, 5.1, 3.9, 1.45, { fill: C.panel, title: t[0], titleSize: 11, body: t[1], bodySize: 9.5 }));
    L.footer(pres, s, n, "来源：央广网（CR-3-06）；21 财经（信通院标准）；NVIDIA（2026-03）；各公司公开资料。「中立」一行：靠可复算保证中立——规则与判定代码对买卖双方开放审计，验收业务设独立主体并披露利益冲突；「公信力与渠道」如实标注为待建。");
  }

  // 9 ── 壁垒
  {
    const s = pres.addSlide(); n++;
    L.header(pres, s, { tag: "壁垒", title: "壁垒假设：中立 + 可复算 + 跨客户累积的错误库", sub: "规则扩到数百条、覆盖多个任务族时的一致性待验证；当前原型 30 条规则、1 个任务族，真实数据上暂只跑数值检查" });
    const layers = [
      ["顶层 · TUpper（ISO/IEC 21838-4:2023）", "国际标准顶层本体之一（与 BFO、DOLCE 并列）；创始人为核心贡献者", C.ink, C.white],
      ["中层 · 物理世界", "物体、部件、形状、度量、材料、过程", C.ink2, C.white],
      ["领域层 · 机器人操作", "可供性、接触事件、任务阶段、关节限位、物体恒存", "3A4160", C.white],
      ["数据层 · 轨迹", "帧、传感器、血缘；LeRobot / RLDS / MCAP", C.panel2, C.text],
    ];
    let ly = 1.95;
    layers.forEach((l) => {
      s.addShape(pres.shapes.RECTANGLE, { x: M, y: ly, w: 6.0, h: 0.72, fill: { color: l[2] }, line: { color: l[2] } });
      L.label(pres, s, l[0], M + 0.2, ly + 0.06, 5.6, 0.3, { head: true, size: 11.5, bold: true, color: l[3] });
      L.label(pres, s, l[1], M + 0.2, ly + 0.37, 5.6, 0.3, { size: 9.5, color: l[3] === C.white ? "D9DCE8" : C.text });
      ly += 0.8;
    });
    L.card(pres, s, M, 5.2, 6.0, 1.3, { fill: C.tealSoft, title: "规则库自检（原型已实现）", titleSize: 11.5, body: DEMO.cn_selfcheck, bodySize: 10 });
    // flywheel
    L.label(pres, s, "错误库飞轮（规划中，原型未实现）", 7.2, 1.95, 5.5, 0.35, { head: true, size: 14, bold: true });
    const steps = ["客户一批数据验收", "拒收与未知条目归类，发现新的错误类型", "新规则由候选生成、经求解器证明不与现有规则矛盾后发布", "旧批次按新规则重验，验收单升级版本", "下一个客户的同类错误直接被拦住"];
    steps.forEach((t, i) => {
      const y = 2.4 + i * 0.66;
      L.stepChip(pres, s, 7.2, y, i + 1, { d: 0.4, fill: i === 4 ? C.crimson : C.ink });
      L.label(pres, s, t, 7.75, y - 0.02, 5.0, 0.5, { size: 10.5, valign: "middle" });
    });
    L.card(pres, s, 7.2, 5.75, 5.5, 0.75, { fill: C.panel, body: "稀缺的是人：全球能写一阶逻辑公理并做机器一致性证明的团队极少；检查脚本、VLM 标注、签名清单都是通用件，我们也把它们当通用件。", bodySize: 9.5 });
    L.footer(pres, s, n, "来源：ISO/IEC 21838-4:2023；ISO/IEC 24707；COLORE（多伦多大学）。");
  }

  // 10 ── 商业模式与市场
  {
    const s = pres.addSlide(); n++;
    L.header(pres, s, { tag: "商业模式", title: "一个产品、一种计价：按验收的数据量收费", sub: "收入跟着数据交易量走，不跟着项目走" });
    const cards = [
      ["付费试点", "8–12 周 · 30–80 万元", "一个任务族、一台本体、客户自带数据；四档基线盲测；试点费抵扣首年费用"],
      ["按量验收", "按验收小时或批次计费", "目标费率为采购额的 5–8%；卖方为「带验收单出货」付费，或买方为「入库验收」付费"],
      ["站内部署", "年费", "大型训练场与数采中心在自有机房运行引擎，按年授权规则库与更新"],
    ];
    cards.forEach((c, i) => {
      const x = M + i * 4.1;
      L.card(pres, s, x, 1.95, 3.9, 1.9, { fill: i === 1 ? C.crimsonSoft : C.panel, title: c[0], titleSize: 13 });
      L.label(pres, s, c[1], x + 0.22, 2.38, 3.4, 0.35, { head: true, size: 13, bold: true, color: C.crimson });
      L.label(pres, s, c[2], x + 0.22, 2.8, 3.46, 1.0, { size: 10 });
    });
    L.label(pres, s, "市场 = 数据采购额 × 验收费率（测算示意）", M, 4.1, 7, 0.35, { head: true, size: 13, bold: true });
    L.table(pres, s, [
      ["情景", "年度真机数据采购量", "单价", "采购额", "验收费率", "验收市场"],
      ["保守", "100 万小时", "600 元", "6 亿元", "5%", "3,000 万元"],
      ["基准", "300 万小时", "750 元", "22.5 亿元", "6%", "1.35 亿元"],
      ["进取", "1,000 万小时", "750 元", "75 亿元", "8%", "6 亿元"],
    ], M, 4.5, 7.6, { colW: [0.9, 1.9, 1.0, 1.3, 1.1, 1.4], size: 9.5, rowH: 0.36, boldFirst: true });
    L.card(pres, s, 8.5, 4.1, 4.25, 2.4, { fill: C.panel, title: "情景依据与远期期权", titleSize: 11.5, body: "行业共识：可用状态需千万小时级真机数据；京东计划两年采 1,000 万小时。\n远期期权（本阶段不计入，触发后计入）：合成 / 世界模型数据的出厂检验（首个合成数据供应商付费后）；出海整机厂的欧盟数据治理证据包（首个出海客户后）；运行时语义护栏。", bodySize: 9.5 });
    L.footer(pres, s, n, "测算示意：采购量与费率为情景假设，单价取公开报价区间；来源：澎湃新闻（2026）；量子位（2026-04）；贵州省大数据局（2026-07）。");
  }

  // 11 ── 首批客户与试点
  {
    const s = pres.addSlide(); n++;
    L.header(pres, s, { tag: "市场路径", title: "标准起草单位就是第一批客户名单", sub: "GB/Z 218.1—2026 的起草单位同时是最大的数据买方与卖方——他们最需要一张双方都认的验收单" });
    L.table(pres, s, [
      ["目标客户（未签约）", "类型", "切入点", "决策人"],
      ["人形机器人（上海）/ 国地中心", "训练场 · 卖方与买方", "存量 100 万+ 条的验收与上架", "数据平台负责人"],
      ["帕西尼感知", "数采工厂 · 卖方", "「带验收单出货」", "数据业务负责人"],
      ["银河通用", "具身大脑 · 买方", "外采数据入库验收", "训练数据负责人"],
      ["小米机器人", "整机 · 买方", "外采数据入库验收", "训练数据负责人"],
      ["自变量机器人", "具身大脑 · 买方", "外采数据入库验收", "数据负责人"],
      ["穹彻智能", "具身大脑 · 买方", "外采数据入库验收", "数据负责人"],
      ["浦江实验室 · 智源", "研究机构 · 发布方", "开源数据集附验收单", "数据集负责人"],
      ["北数所具身跨境流通平台", "交易平台 · 渠道", "挂牌数据的验收单", "平台运营负责人"],
    ], M, 1.95, 7.3, { colW: [2.15, 1.65, 2.0, 1.5], size: 9, rowH: 0.4, boldFirst: true });
    L.card(pres, s, 8.2, 1.95, 4.55, 3.0, { fill: C.ink, title: "付费试点设计", titleColor: C.white, body: "客户自带一批数据，同一批依次通过四档基线：客户现有脚本、几何规则、VLM + 规则、完整引擎。\n专家真值独立建立，客户持有留出集。\n验收指标：严重错误误放率、好数据误拒率、未知比例、每千条复核工时、端到端时长。\n结果预先约定：若简单规则同样有效，就收窄到规则抓不到的错误类。", bodySize: 9.5, bodyColor: "D9DCE8" });
    L.card(pres, s, 8.2, 5.1, 4.55, 1.4, { fill: C.crimsonSoft, title: "核心指标", titleColor: C.crimson, titleSize: 11.5, body: "每季度完成验收的数据小时数：同时反映供给（吞吐）、需求（付费验收的客户）与质量（通过率）。", bodySize: 9.5 });
    L.footer(pres, s, n, "起草单位来源：全国标准信息公共服务平台（GB/Z 218.1—2026）。名单为目标客户，均未签约。");
  }

  // 12 ── 进展与 90 天
  {
    const s = pres.addSlide(); n++;
    L.header(pres, s, { tag: "进展", title: "已经做成的、原型跑出来的、90 天内可以验证的", sub: "每一项都可以当场核查；目标均标注日期" });
    const cols = [
      ["CircleCheck", "已实现", C.tealSoft, [
        "形式化本体积累：TUpper（ISO/IEC 21838-4）团队背景；与产品规则库的对齐是下一步目标",
        "10 万条实测三维几何数据包；房间级重建与物体级标注技术栈（9 项发明专利申请）",
        "消费级空间应用已上线（Apple Vision Pro）；13 项授权专利",
        "北京国际大数据交易所数据经纪商资质",
      ]],
      ["Cpu", "原型（本月跑通）", C.panel, DEMO.cn_proto_bullets],
      ["Target", "12 月 31 日前可验证", C.crimsonSoft, [
        "在 DROID / AgiBot World 真实数据上对比加强规则基线与 Cosmos Evaluator，第三方持有注入密钥；若增量 < 10 个百分点，收窄到规则抓不到的错误类",
        "1 家具名客户以自带数据跑付费试点，给出验收前后的对照数字",
        "验收单字段对齐信通院八维指标，向信通院或 CR 认证联盟之一提交",
        "在带物体标注的真实数据上跑出语义层，不再全部「未知」",
      ]],
    ];
    for (let i = 0; i < 3; i++) {
      const x = M + i * 4.1;
      L.card(pres, s, x, 1.95, 3.9, 4.55, { fill: cols[i][2], title: cols[i][1], titleIndent: 0.5 });
      await L.icon(s, cols[i][0], x + 0.2, 2.1, 0.36, { bg: i === 2 ? C.crimson : C.ink });
      L.bullets(pres, s, x + 0.22, 2.6, 3.46, 3.8, cols[i][3], { size: 10, paraSpace: 7 });
    }
    L.footer(pres, s, n, "来源：AXIOMALITY 内部记录与原型代码（可当场演示）；目标为计划值。");
  }

  // 13 ── 团队
  {
    const s = pres.addSlide(); n++;
    L.header(pres, s, { tag: "团队", title: "能写经证明的规则库，也经历过一年 5,000 万美元营收的创业", sub: "本体与形式化验证、AI 算法、感知与机器人、三维资产四条能力线" });
    L.card(pres, s, M, 1.95, 6.2, 4.55, { fill: C.ink, title: "创始人 & CEO", titleColor: C.white, titleSize: 15 });
    L.bullets(pres, s, M + 0.22, 2.5, 5.8, 3.9, [
      { text: "标准：ISO/IEC 21838-4（TUpper 顶层本体）核心贡献者；国际工业本体联盟成员；多伦多大学人工智能博士与研究员", options: { color: C.white } },
      { text: "科学：形式化本体、一阶逻辑公理体系的一致性证明与模型构造、可信神经符号 AI；21 篇论文，AAAI 特邀报告，1 部英文专著", options: { color: C.white } },
      { text: "经营：跨境 DTC 平台创始团队成员，获 Accel 等美国头部风投 500 万美元天使投资，一年内年收入超 5,000 万美元，带领 100+ 人团队", options: { color: C.white } },
      { text: "空间计算：创办空间计算公司，Apple Vision Pro 首批 AR 应用之一；13 项授权专利，2,400 万元专利转让、1,000 万元技术许可", options: { color: C.white } },
    ], { size: 10.5, paraSpace: 9 });
    const team = [
      ["CTO & 首席科学家", "麦克马斯特大学 AI 博士；曾任一线大厂 AI 算法科学家、创业公司首席科学家；加拿大 AI 学术与工业应用大赛第一名"],
      ["感知与机器人负责人", "哈尔滨工业大学机械电子工程博士；曾任小鹏汽车 AI 算法工程师、智能感知中心总监"],
      ["仿真与三维资产负责人", "10 年+ 游戏与舞台美术总监；主导 1750 年北京古城数字（VR）重建"],
    ];
    team.forEach((t, i) => L.card(pres, s, 7.1, 1.95 + i * 1.17, 5.6, 1.05, { fill: C.panel, title: t[0], titleSize: 11.5, body: t[1], bodySize: 9.5 }));
    L.card(pres, s, 7.1, 5.5, 5.6, 1.0, { fill: C.crimsonSoft, title: "正在招募", titleColor: C.crimson, titleSize: 11.5, body: "在训练场 / 数采体系交付过数据的产业侧合伙人；训练过 VLA 策略的机器人学习科学家。", bodySize: 9.5 });
    L.footer(pres, s, n);
  }

  // 14 ── 结语
  {
    const s = pres.addSlide(); n++;
    L.darkBg(pres, s);
    L.label(pres, s, "AXIOMALITY", M, 0.55, 4, 0.35, { size: 13, bold: true, color: C.white, extra: { charSpacing: 4 } });
    L.label(pres, s, "每一批换手的具身数据，\n都应该先验货，再付款。", M, 1.4, 11, 1.7, { head: true, size: 32, bold: true, color: C.white, ls: 1.15 });
    L.label(pres, s, "从数采中心的出货验收开始；再到买方的入库验收、合成数据的出厂检验；最终成为具身数据交易里默认附带的那张验收单。", M, 3.25, 11, 0.8, { size: 13, color: "C9CDDB" });
    const asks = [
      ["Handshake", "两个介绍", "请介绍自变量、穹彻等被投公司的数据负责人，用他们自己的一批数据做盲测"],
      ["FileCheck", "12 分钟", "现场生成一张验收单，请您亲手改一条数据，看验签当场失败"],
      ["CalendarCheck", "12 月 31 日", "三项 90 天承诺届时逐项核对：真实数据盲测、具名付费试点、标准机构提交"],
    ];
    for (let i = 0; i < 3; i++) {
      const x = M + i * 4.1;
      s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y: 4.45, w: 3.9, h: 1.85, fill: { color: C.ink2 }, line: { color: C.ink2 }, rectRadius: 0.08 });
      await L.icon(s, asks[i][0], x + 0.22, 4.65, 0.4, { bg: C.crimson });
      L.label(pres, s, asks[i][1], x + 0.75, 4.68, 3.0, 0.35, { head: true, size: 14, bold: true, color: C.white });
      L.label(pres, s, asks[i][2], x + 0.22, 5.2, 3.5, 1.0, { size: 10.5, color: "D9DCE8" });
    }
    L.label(pres, s, "© 2026 AXIOMALITY  ·  保密  ·  未经许可不得传播", M, H - 0.5, 8, 0.3, { size: 9, color: "9AA0B4" });
  }

  fs.mkdirSync(path.dirname(OUT), { recursive: true });
  await pres.writeFile({ fileName: OUT });
  console.log("wrote", OUT, "slides:", n);
})().catch((e) => { console.error(e); process.exit(1); });
