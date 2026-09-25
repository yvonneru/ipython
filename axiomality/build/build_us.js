// AXIOMALITY — YC / a16z seed deck (13 slides)
const L = require("./lib");
const { C, W, H, M } = L;
const path = require("path");
const fs = require("fs");

const MEDIA = path.join(__dirname, "..", "src", "media_cn");
const OUT = process.argv[2] || path.join(__dirname, "out", "AXIOMALITY_Seed_Deck_YC_a16z.pptx");
const FOOT = "AXIOMALITY  ·  Seed deck  ·  September 2026  ·  Confidential";

(async () => {
  const pres = L.newDeck("en", { title: "AXIOMALITY seed deck", footer: FOOT });
  const F = pres._F;
  let n = 0;

  // ───────────── 1. Cover ─────────────
  {
    const s = pres.addSlide(); n++;
    L.darkBg(pres, s);
    L.label(pres, s, "AXIOMALITY", M, 0.55, 4, 0.35, { size: 13, bold: true, color: C.white, extra: { charSpacing: 4 } });
    L.label(pres, s, "Every robot dataset ships with\na machine-checkable passport.", M, 1.45, 7.9, 1.9, { head: true, size: 32, bold: true, color: C.white, ls: 1.1 });
    L.label(pres, s, "The verification layer for physical-AI data: a formally checked engine that scores, signs and audits every robot trajectory, so labs train on evidence instead of assumptions.", M, 3.5, 7.6, 0.9, { size: 14, color: "C9CDDB" });
    L.label(pres, s, "Seed round  ·  September 2026  ·  Confidential", M, 4.55, 7.2, 0.4, { size: 12, color: "9AA0B4" });
    const img = path.join(MEDIA, "cover_crop.png");
    s.addShape(pres.shapes.RECTANGLE, { x: 8.55, y: 1.35, w: 4.2, h: 2.5, fill: { color: C.ink2 }, line: { color: C.ink2 } });
    s.addImage({ path: img, x: 8.7, y: 1.915, w: 3.9, h: 1.37 });
    L.brackets(pres, s, 8.55, 1.35, 4.2, 2.5, C.crimson, 0.22, 1.5);
    L.label(pres, s, "AXIOMALITY sample 429: measured point cloud with oriented 3D boxes (real data)", 8.55, 3.92, 4.2, 0.4, { size: 9.5, color: "9AA0B4" });
    const stats = [
      ["ISO/IEC 21838-4", "Founded by a core contributor to the TUpper top-level ontology standard"],
      ["100,000", "Measured 3D asset packages (photo · USDZ · PLY · JSON)"],
      ["13 + 9", "Granted patents + invention applications"],
      ["Q4 2026", "Engine internal test; first paid design partners 2027"],
    ];
    stats.forEach((st, i) => {
      const x = M + i * 3.05;
      s.addShape(pres.shapes.LINE, { x, y: 5.35, w: 2.7, h: 0, line: { color: "3A4160", width: 0.75 } });
      L.stat(pres, s, x, 5.45, 2.85, 1.2, st[0], st[1], { dark: true, size: 19, labelSize: 10 });
    });
    s.addNotes("30-second open: we are the QA and certification layer for robot training data. Any format in; a per-record verdict and a signed, offline-verifiable passport out. The founder co-wrote an ISO top-level ontology standard and previously built a $50M-revenue company.");
  }

  // ───────────── 2. Problem ─────────────
  {
    const s = pres.addSlide(); n++;
    L.header(pres, s, { tag: "PROBLEM", title: "Robot teams cannot trust their data, and the flood is getting worse", sub: "Three failure modes that cost real engineering hours today, none of which produce a record anyone else can check" });
    const cards = [
      ["Upload", "Before training", "Demonstrations, field logs, scans and generated clips arrive with different frames, units and task labels. Coordinate errors, duplicates and mislabeled phases train silently. In a 2026 Voxel51 survey, 89% of teams blamed data for model failures and 48% cited quality problems.", "“We spend 600 review hours a month and still don’t know what got through.”"],
      ["Bug", "After a failure", "Perception, coverage, task order and physical contact all produce the same failed rollout. Engineers need the source record, a localized cause and a regression test. Today they get a video and a guess.", "“Which frame, which rule, which batch? Nobody can tell us.”"],
      ["FileWarning", "Before release", "New sensors, sites and synthetic mixtures invalidate earlier conclusions. There is no versioned, per-record evidence of what a model was trained on, no real-to-synthetic ratio, no consent lineage, and nothing a buyer, insurer or notified body can re-check.", "“We can’t prove what we trained on, so we can’t sell it or ship it into the EU.”"],
    ];
    const cw = (W - 2 * M - 0.6) / 3, ch = 3.1, cy = 1.95;
    for (let i = 0; i < 3; i++) {
      const x = M + i * (cw + 0.3);
      L.card(pres, s, x, cy, cw, ch, { fill: C.panel, title: cards[i][1], titleIndent: 0.5, body: cards[i][2], bodySize: 10.5 });
      await L.icon(s, cards[i][0], x + 0.2, cy + 0.16, 0.36, { bg: C.ink });
      L.label(pres, s, cards[i][3], x + 0.22, cy + ch - 0.72, cw - 0.44, 0.6, { size: 10.5, italic: true, color: C.crimson });
    }
    const st = [["$50–200 / h", "Teleoperation data, with no record of what is usable"], ["58,000+", "Datasets on the LeRobot hub (May 2026); none validated or signed"], ["≈ 0", "Direct reuse of the action layer across embodiments"], ["0", "Vendors selling a per-record, machine-checkable certificate"]];
    st.forEach((x, i) => L.stat(pres, s, M + i * 3.05, 5.3, 2.9, 1.1, x[0], x[1], { size: 24, labelSize: 10 }));
    L.footer(pres, s, n, "Sources: Voxel51 State of Visual AI survey (2026); Hugging Face (May 2026); DreamVu, Robot Training Data Companies: The 2026 Landscape; Open X-Embodiment (2023).");
  }

  // ───────────── 3. Why now ─────────────
  {
    const s = pres.addSlide(); n++;
    L.header(pres, s, { tag: "WHY NOW", title: "Raw hours are going to zero, generators are flooding training, and the money has arrived", sub: "Value is moving from hours to evidence; the evidence format becomes the unit of trade" });
    const drivers = [
      ["TrendingDown", "Supply: raw data is free", "Build AI released Egocentric-1M, about one million hours of factory video under Apache-2.0 (Apr 2026). Teleoperation at $50–200/hour has no moat. Margin survives only in semantics, verification and certification."],
      ["Sparkles", "Demand: synthetic data", "World Labs’ Atlas (Sep 2026) generates robot-camera RGB and depth from phone video; NVIDIA’s Cosmos data-factory blueprint ships a free Evaluator that scores generated clips. More generators mean more unverified data entering training, with no signed record of real-to-synthetic ratio."],
      ["Banknote", "Money: budgets arrived", "Physical-AI startups raised a record $18.6B in Q2 2026 alone. Physical Intelligence (~$11B), Skild ($14B), Generalist ($3B) and Figure ($39B) are buying data; Scale’s physical-AI engine passed 150k hours. Buyers now gate their own data and need a neutral referee."],
    ];
    for (let i = 0; i < 3; i++) {
      const x = M + i * 4.1;
      L.card(pres, s, x, 1.95, 3.9, 2.55, { fill: C.panel, title: drivers[i][1], titleIndent: 0.5, body: drivers[i][2], bodySize: 10.5 });
      await L.icon(s, drivers[i][0], x + 0.2, 2.1, 0.36, { bg: C.crimson });
    }
    // value ladder
    const tiers = [["Certification", "audit packs, listing evidence; what regulators and buyers accept", C.crimson, C.white], ["Verification", "physics, logic, uncertainty: is the record consistent?", "A61A3F", C.white], ["Semantics", "what happened: objects, affordances, contacts, task phases", C.ink2, C.white], ["Raw hours", "$50–200/h (2024) → near zero (2026)", C.panel2, C.text]];
    tiers.forEach((t, i) => {
      const y = 4.75 + i * 0.42, w = 5.2 + i * 0.8, x = M;
      s.addShape(pres.shapes.RECTANGLE, { x, y, w, h: 0.36, fill: { color: t[2] }, line: { color: t[2] } });
      L.label(pres, s, t[0], x + 0.15, y + 0.03, 1.5, 0.3, { head: true, size: 11, bold: true, color: t[3], valign: "middle" });
      L.label(pres, s, t[1], x + 1.6, y + 0.03, w - 1.7, 0.3, { size: 9.5, color: t[3], valign: "middle" });
    });
    L.card(pres, s, 8.6, 4.75, 4.15, 1.7, { fill: C.crimsonSoft, title: "Compliance: tailwind, not thesis", titleColor: C.crimson, titleSize: 11.5, body: "EU AI Act Annex I applies to AI embedded in machinery, including ML safety components of robots, from 2 Aug 2028 (Reg. 2026/1744). We sell to the data race today; the audit pack is what the same evidence becomes in 2028.", bodySize: 9.5 });
    L.footer(pres, s, n, "Sources: Build AI (Apr 2026); World Labs (Sep 2026); NVIDIA (Mar 2026); PitchBook Q2 2026; company announcements; European Commission (Regulation (EU) 2026/1744).");
  }

  // ───────────── 4. Product ─────────────
  {
    const s = pres.addSlide(); n++;
    L.header(pres, s, { tag: "PRODUCT", title: "Engine + Passport: any format in, a per-record verdict and a signed certificate out", sub: "Five stages; every episode gets pass / repair / reject with an evidence trail back to the exact frame and rule" });
    const steps = [
      ["Ingest", "LeRobot, RLDS, ROS 2 / MCAP, OpenUSD, video, 3D scans. No change to how customers collect."],
      ["Ground", "VLM + graph models map each frame to kernel concepts: objects, affordances, contacts, task phases."],
      ["Verify", "Physics residuals (kinematic, and dynamic where torque exists) · SMT check against the rulebook · calibrated uncertainty."],
      ["Decide", "Pass / repair / reject with an evidence subgraph. Valid failures are kept; originals are never overwritten."],
      ["Passport", "Signed against kernel version and data hash. Verifiable offline with the public spec and key."],
    ];
    const sw = 1.45, sg = 0.14, sy = 1.95;
    steps.forEach((st, i) => {
      const x = M + i * (sw + sg);
      L.stepChip(pres, s, x, sy, i + 1, { d: 0.4 });
      L.label(pres, s, st[0], x + 0.5, sy + 0.02, sw - 0.5, 0.38, { head: true, size: 13, bold: true, valign: "middle" });
      L.label(pres, s, st[1], x, sy + 0.5, sw, 1.7, { size: 9.5 });
      if (i < 4) L.arrow(pres, s, x + sw - 0.05, sy + 0.2, sg + 0.05, { color: C.crimson });
    });
    L.table(pres, s, [
      ["Check", "Method", "Criterion", "On failure"],
      ["Physical consistency", "Geometry, kinematics, and dynamics residual where τ / contact exist", "Residual within calibrated tolerance", "Repair: project to nearest feasible record, logged"],
      ["Logical consistency", "SMT (Z3) against kernel axioms Φ over a bounded scene graph", "SAT pass / UNSAT reject / UNKNOWN surfaced", "Reject: human review with diagnostic; never silently passed"],
      ["Uncertainty", "Conformal prediction, coverage ≥ 1 − α, reported per group", "Inside prediction set", "Low confidence: escalate to a more expensive check"],
    ], M, 4.2, 7.65, { colW: [1.3, 2.5, 1.75, 2.1], size: 8.5, rowH: 0.4, boldFirst: true });
    L.label(pres, s, "One rulebook, compiled twice: a differentiable soft constraint for training and a decidable hard check for verification.", M, 6.2, 7.65, 0.4, { size: 10, italic: true, color: C.muted });

    const px = 8.65, py = 1.95, pw = 4.1, ph = 4.55;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: px, y: py, w: pw, h: ph, fill: { color: C.ink }, line: { color: C.ink }, rectRadius: 0.08 });
    L.brackets(pres, s, px + 0.12, py + 0.12, pw - 0.24, ph - 0.24, C.crimson, 0.18, 1.25);
    L.label(pres, s, "AXIOMALITY PASSPORT · sample", px + 0.3, py + 0.28, pw - 0.6, 0.3, { size: 9.5, bold: true, color: C.crimson, extra: { charSpacing: 1 } });
    const rows = [
      ["Dataset", "AX-2027-0412 · kitchen tasks"],
      ["Episodes", "12,480 (8,140 real / 4,340 syn.)"],
      ["Kernel", "v1.2 · ISO/IEC 21838-4 aligned"],
      ["Grounding", "96.4% frames mapped (audited)"],
      ["Physics", "99.1% pass · 0.7% fix · 0.2% reject"],
      ["Uncertainty", "0.94 coverage, per group"],
      ["Safety rules", "ISO 13482-derived · 0 violations"],
      ["Provenance", "Per-episode hashes · consent"],
      ["Regulatory map", "EU Art. 10 / 12 · GB/Z 218.1"],
      ["Signature", "2027-04-12 · sha256 9f2c…a41e"],
    ];
    rows.forEach((r, i) => {
      const y = py + 0.68 + i * 0.34;
      L.label(pres, s, r[0], px + 0.3, y, 1.2, 0.3, { size: 8.5, color: "9AA0B4" });
      L.label(pres, s, r[1], px + 1.45, y, pw - 1.7, 0.3, { size: 8.5, color: C.white });
    });
    L.pill(pres, s, "VERIFIED · offline", px + pw - 1.6, py + ph - 0.5, 1.35, 0.3, { fill: C.teal, color: C.white, size: 9 });
    L.label(pres, s, "Product design example; values illustrate the evidence interface. Real passports on partner data under NDA from Dec 2026.", px, py + ph + 0.06, pw, 0.4, { size: 8.5, color: C.muted });
    L.footer(pres, s, n);
  }

  // ───────────── 5. Example ─────────────
  {
    const s = pres.addSlide(); n++;
    L.header(pres, s, { tag: "HOW IT WORKS", title: "One episode’s journey: a rejected variant becomes a new rule, and old data gets more valuable", sub: "Illustrative episode AX-2027-0412: kitchen, place a cup into a dishwasher" });
    const cols = [
      ["Collect", "Phone scan + teleoperated demo. 12 m² kitchen, 37 objects; consent recorded and hashed with the capture.", C.panel],
      ["Ground", "Cup (graspable, fragile), dishwasher (container, openable); 3 contact events; 4 task phases; 97% of frames mapped.", C.panel],
      ["Verify", "Physics residual within tolerance; SMT against the kernel: SAT; uncertainty 0.03. Verdict: pass, with evidence subgraph.", C.tealSoft],
      ["Augment", "Digital twin generates 5 variants (2 lighting, 2 pose, 1 failure: cup slips). Re-verified one by one: 4 pass, 1 rejected.", C.panel],
      ["Passport", "1 real + 4 synthetic episodes written to the passport; exported to LeRobot / RLDS / OpenUSD; signed, offline-verifiable.", C.tealSoft],
      ["Learn", "Rejection cause: no friction constraint for wet counters → new axiom, proven before use → targeted re-collection → old datasets re-verified, passport v1.3.", C.crimsonSoft],
    ];
    const cw = (W - 2 * M - 5 * 0.14) / 6, cy = 2.0, ch = 2.85;
    cols.forEach((c, i) => {
      const x = M + i * (cw + 0.14);
      L.stepChip(pres, s, x, cy, i + 1, { d: 0.38, fill: i === 5 ? C.crimson : C.ink });
      L.label(pres, s, c[0], x + 0.48, cy + 0.02, cw - 0.5, 0.36, { head: true, size: 13, bold: true, valign: "middle" });
      L.card(pres, s, x, cy + 0.5, cw, ch - 0.5, { fill: c[2], body: c[1], bodySize: 9.5 });
    });
    s.addShape(pres.shapes.LINE, { x: M + 0.3, y: 5.12, w: W - 2 * M - 0.6, h: 0, line: { color: C.crimson, width: 1.25, dashType: "dash", beginArrowType: "triangle" } });
    L.label(pres, s, "Feedback: confirmed failures → new axioms → higher kernel coverage → lower verification cost per hour → collection spent only where the loop points", M + 0.3, 5.2, W - 2 * M - 0.6, 0.3, { size: 10, color: C.crimson, align: "center" });
    const st = [["Once", "Each new concept is axiomatized once, then reused by every episode"], ["$60 → $12 / h", "Fully loaded verification cost, Q4 2026 → 2030 (model target)"], ["< $5 / h", "Marginal cost target for a re-verified synthetic episode"], ["v1.2 → v1.3", "Delivered datasets re-signed as the kernel grows"]];
    st.forEach((x, i) => L.stat(pres, s, M + i * 3.05, 5.6, 2.9, 1.0, x[0], x[1], { size: 20, labelSize: 9.5 }));
    L.footer(pres, s, n, "Source: AXIOMALITY product records. Cost figures are unit-economics model targets (converted at ¥7.2 per USD), not contracted.");
  }

  // ───────────── 6. Why hard to copy ─────────────
  {
    const s = pres.addSlide(); n++;
    L.header(pres, s, { tag: "MOAT", title: "A mathematically checked rulebook, and a flywheel that makes each hour cheaper than the last", sub: "One rulebook feeds both the passport and the runtime guardrail; the loop compounds domain knowledge competitors cannot download" });
    const layers = [
      ["Top level · TUpper (ISO/IEC 21838-4:2023)", "One of the three top-level ontologies with an ISO part (with BFO and DOLCE); our founder is a core contributor. Consistency machine-checked with Prover9 / Mace4.", C.ink, C.white],
      ["Physical world", "Objects, parts, shape, measurement, materials, change and process (PSL lineage).", C.ink2, C.white],
      ["Robotics domain", "Embodiment, affordances, contact and force events, kinematic chains, task phases, safety rules derived from ISO 10218 / 13482.", "3A4160", C.white],
      ["Dataset instances", "Episodes, frames, sensors, lineage; exports to OpenUSD / LeRobot / RLDS.", C.panel2, C.text],
    ];
    let ly = 1.95;
    layers.forEach((l) => {
      s.addShape(pres.shapes.RECTANGLE, { x: M, y: ly, w: 6.0, h: 0.76, fill: { color: l[2] }, line: { color: l[2] } });
      L.label(pres, s, l[0], M + 0.2, ly + 0.06, 5.6, 0.3, { head: true, size: 11.5, bold: true, color: l[3] });
      L.label(pres, s, l[1], M + 0.2, ly + 0.36, 5.6, 0.38, { size: 9, color: l[3] === C.white ? "D9DCE8" : C.text });
      ly += 0.84;
    });
    L.card(pres, s, M, 5.38, 6.0, 1.25, { fill: C.panel, title: "What is rare here", titleSize: 11.5, body: "Very few teams can write and machine-verify first-order axiomatizations of process, parts and physical quantities. Applying that to robot data is unusual; VLM labelling, kinematic checks and signed manifests are commodity, and we treat them that way.", bodySize: 9 });

    L.label(pres, s, "Fully loaded verification cost per hour (USD, model target)", 7.1, 1.95, 5.6, 0.3, { head: true, size: 12, bold: true });
    s.addChart(pres.charts.LINE, [{ name: "USD / h", labels: ["Q4 2026", "2027", "2028", "2029", "2030"], values: [60, 34, 20, 15, 12] }], {
      x: 7.1, y: 2.25, w: 5.6, h: 2.5, chartColors: [C.crimson], lineSize: 2.5, lineDataSymbolSize: 8,
      showValue: true, dataLabelPosition: "t", dataLabelFontSize: 9, dataLabelColor: C.text, dataLabelFontFace: F.body,
      catAxisLabelFontSize: 9, valAxisLabelFontSize: 9, catAxisLabelColor: C.muted, valAxisLabelColor: C.muted,
      valGridLine: { color: "E5E7EB", size: 0.5 }, catGridLine: { style: "none" }, showLegend: false, valAxisMinVal: 0, valAxisMaxVal: 70,
      catAxisLabelFontFace: F.body, valAxisLabelFontFace: F.body,
    });
    L.card(pres, s, 7.1, 4.9, 5.6, 1.6, { fill: C.panel, title: "How the flywheel turns", body: "Cost sits in the first verification of a concept, not in repeats. Customer field failures → LLM agents propose candidate rules → provers check them before release → kernel v(n+1) → delivered datasets re-verified and re-signed. Human review shrinks to the reject path; what does not fall (VLM inference, prover time) is priced into the model.", bodySize: 9.5 });
    L.footer(pres, s, n, "Sources: ISO/IEC 21838-4:2023; ISO/IEC 24707; COLORE (University of Toronto); AXIOMALITY technical papers. Cost curve is a unit-economics target.");
  }

  // ───────────── 7. Market ─────────────
  {
    const s = pres.addSlide(); n++;
    L.header(pres, s, { tag: "MARKET", title: "Validation software for physical AI already earns premium multiples; robot learning has no such layer yet", sub: "Wedge into a countable buyer pool, meter by trajectory, then collect a per-robot royalty at fleet scale" });
    const comps = [
      ["Applied Intuition", "$15B", "Simulation and validation for AVs; $600M Series F (Jun 2025). Launched Dana for robots (Jul 2026). Proves validation tooling for physical AI is a large, high-margin category."],
      ["Foretellix", "$135M raised", "Coverage-driven verification for AV; NVIDIA and Toyota Woven invested rather than built. Shows the concept, and its limit: AV-only, no per-record certificate."],
      ["Vanta", "$4.15B", "SOC 2 automation; $300M ARR (Apr 2026). The badge buyers demand becomes the product. A passport is the SOC 2 report for a robot dataset."],
    ];
    comps.forEach((c, i) => {
      const x = M + i * 4.1;
      L.card(pres, s, x, 1.95, 3.9, 1.85, { fill: C.panel, title: c[0], titleSize: 13 });
      L.label(pres, s, c[1], x + 0.22, 2.35, 3.4, 0.4, { head: true, size: 18, bold: true, color: C.crimson });
      L.label(pres, s, c[2], x + 0.22, 2.8, 3.46, 0.95, { size: 9.5 });
    });
    L.table(pres, s, [
      ["Stage", "Construction", "Annual value"],
      ["Wedge (2027–28)", "80–200 U.S./Canadian organizations with recurring robot data × $150k–300k", "$12M–60M"],
      ["Platform (2029–30)", "500 customers × $200k recurring, metered by verified trajectory volume", "$100M ARR"],
      ["Royalty (2030+)", "Runtime guardrail per robot per year; China alone forecasts 500k humanoids shipped in 2030, global fleets in the millions", "$100M+ incremental"],
    ], M, 4.05, 7.9, { colW: [1.6, 4.7, 1.6], size: 9.5, rowH: 0.5, boldFirst: true });
    const facts = [["$18.6B", "Physical-AI venture funding in Q2 2026 alone (PitchBook)"], ["$47B", "Physical-AI funding in H1 2026 (Crunchbase)"], ["150k+ h", "Scale AI physical-AI data engine volume, 10 new robotics customers in 2025"], ["$4.9B → $17.1B", "Data annotation and training-data market 2025 → 2030 (SCSP)"]];
    facts.forEach((f, i) => L.stat(pres, s, 8.75 + (i % 2) * 2.05, 4.05 + Math.floor(i / 2) * 1.25, 2.0, 1.15, f[0], f[1], { size: 15, labelSize: 8.5 }));
    L.footer(pres, s, n, "Sources: company announcements; PitchBook; Crunchbase; Scale AI; SCSP / ISF Voices 2026; SAG (China humanoid forecast). Market construction is AXIOMALITY’s estimate.");
  }

  // ───────────── 8. Competition ─────────────
  {
    const s = pres.addSlide(); n++;
    L.header(pres, s, { tag: "COMPETITION", title: "Nobody sells a signed, per-record certificate for robot data; the ingredients are commoditizing, the referee is not", sub: "Complements: collection, curation, simulation, runtime safety. Credible threats: NVIDIA adding a manifest; labs staying in-house." });
    L.table(pres, s, [
      ["Capability", "Collection", "Curation / tools", "Simulation / world models", "Runtime safety", "Certification bodies", "AXIOMALITY"],
      ["Formal rulebook, machine-checked consistent", "○", "○", "○", "○", "○", "●"],
      ["Per-record physics + logic + uncertainty checks", "○", "◐", "◐", "◐", "○", "●"],
      ["Signed certificate, verifiable offline by anyone", "○", "○", "○", "○", "◐", "●"],
      ["Cross-embodiment schema (semantic reuse)", "○", "◐", "◐", "○", "○", "●"],
      ["Audit pack mapped to EU Art. 10/12 and China GB/Z 218.1", "○", "○", "○", "◐", "●", "●"],
      ["Same rulebook compiled to a runtime guardrail", "○", "○", "○", "●", "○", "●"],
      ["Who", "Scale AI, Mecka, Build AI, XDOF, Human Archive", "Foxglove, Encord, Voxel51, Rerun, NVIDIA Cosmos Evaluator (free scoring), Applied Intuition Dana", "NVIDIA Cosmos, World Labs Atlas, Lightwheel, Genesis", "3Laws, RoboGuard, NVIDIA Halos OS", "NVIDIA Halos Inspection Lab (ANAB, TÜV/UL), Pebblous (KR), CR data-set certification (CN)", "Kernel + Engine + Passport"],
    ], M, 1.95, W - 2 * M, { colW: [2.35, 1.55, 2.05, 1.65, 1.45, 1.9, 1.18], size: 8.5, rowH: 0.34, boldFirst: true });
    L.label(pres, s, "● present   ◐ partial   ○ absent", M, 5.2, 5, 0.25, { size: 9, color: C.muted });
    const notes = [
      ["vs. NVIDIA", "Cosmos Evaluator scores plausibility for free but is unsigned, non-formal and tied to the NVIDIA stack; Halos certifies compute and safety. We are the neutral signer at the task-semantics level, on any stack."],
      ["vs. in-house pipelines", "PI, Figure and DeepMind curate internally. The passport wins where there is information asymmetry: vendors selling to labs, OEMs selling into regulated markets, buyers wanting an independent re-check. Labs are the channel."],
      ["vs. tooling", "Foxglove, Rerun and LeRobot are where the data lives; we ship as their “verified” badge, not a replacement. The spec is public; the proven domain rulebook and the signer’s track record do not travel."],
    ];
    notes.forEach((t, i) => L.card(pres, s, M + i * 4.1, 5.45, 3.9, 1.25, { fill: C.panel, title: t[0], titleSize: 11, body: t[1], bodySize: 8.5 }));
    L.footer(pres, s, n, "Sources: company announcements and press (2025–26); NVIDIA (Mar and Jun 2026); DreamVu 2026 landscape. Positioning is AXIOMALITY’s assessment.");
  }

  // ───────────── 9. Business model ─────────────
  {
    const s = pres.addSlide(); n++;
    L.header(pres, s, { tag: "BUSINESS MODEL", title: "Pilot, then annual deployment, then a per-robot royalty from the same rulebook", sub: "Separate bookings, commitments, credits and cash; cohort math below is the sizing example, not a forecast" });
    const stages = [
      ["1 · Paid pilot", "$25k–50k, 8–12 weeks", "One task family, one embodiment, fixed data and acceptance criteria. Blinded baselines; the pilot fee credits against year one.", C.panel],
      ["2 · Annual deployment", "$120k–240k per year", "Supported connectors, recurring checks, evidence packs per release; implementation scoped separately. Metered by verified trajectories as volume grows.", C.panel],
      ["3 · Runtime guardrail royalty", "per robot per year", "Same rulebook, precompiled for millisecond checks; gated behind latency and false-block tests on target hardware. Outside the initial cohort model.", C.crimsonSoft],
    ];
    stages.forEach((st, i) => {
      const x = M + i * 4.1;
      L.card(pres, s, x, 1.95, 3.9, 1.95, { fill: st[3], title: st[0], titleSize: 13 });
      L.label(pres, s, st[1], x + 0.22, 2.35, 3.4, 0.35, { head: true, size: 14, bold: true, color: C.crimson });
      L.label(pres, s, st[2], x + 0.22, 2.75, 3.46, 1.1, { size: 9.5 });
      if (i < 2) L.arrow(pres, s, x + 3.92, 2.9, 0.16, { color: C.crimson });
    });
    L.table(pres, s, [
      ["Sizing cohort (midpoint)", "USD", "Interpretation"],
      ["10 pilots × $40,000", "$400,000", "Project bookings"],
      ["4 annual × $180,000", "$720,000", "Before first-year credits"],
      ["4 credits × $20,000", "−$80,000", "Avoid double counting"],
      ["Net software commitment", "$640,000", "First contracted year"],
      ["Combined bookings", "$1,040,000", "Pilots + net software"],
    ], M, 4.15, 6.3, { colW: [2.5, 1.3, 2.5], size: 9.5, rowH: 0.34, boldFirst: true });
    L.card(pres, s, 7.2, 4.15, 5.5, 2.35, { fill: C.panel, title: "Customer ROI and expansion", body: "Illustrative baseline: 600 review hours a month × $150 = $1.08M of annual review capacity; a 40% reduction releases $432k against a $180k first-year purchase, before the customer’s own integration and compute. Renewal is the proof, not the model.\n\nExpansion path inside one account: one dataset → every release → a second embodiment → runtime. Gross margin target 80%+ once verification runs in the customer’s environment and compute is theirs.", bodySize: 9.5 });
    L.footer(pres, s, n, "Source: AXIOMALITY pricing and cohort model; all figures are sizing examples, not contracted.");
  }

  // ───────────── 10. Go-to-market ─────────────
  {
    const s = pres.addSlide(); n++;
    L.header(pres, s, { tag: "GO-TO-MARKET", title: "First buyers own a recurring data decision; the pilot is designed to be falsifiable", sub: "Founder-led U.S. and Canadian sales; we pre-register the comparison and keep negative results" });
    L.table(pres, s, [
      ["Buyer", "Budget owner", "Initial deliverable", "Public workflow examples"],
      ["Data supplier", "Data operations", "Repeatable customer acceptance; a passport that raises sale price or shortens buyer review", "Scale, Mecka, Human Archive, Build AI"],
      ["Robot OEM", "Autonomy / quality lead", "Failure-linked regression evidence; audit pack for EU shipments", "Agility / GXO, Sanctuary / Magna, Vention"],
      ["Model developer", "Robot-learning lead", "Batch acceptance and diagnostics on mixed real / synthetic data", "Physical Intelligence, Figure, Generalist, Dyna"],
      ["Industrial integrator", "Engineering / quality", "Application-specific test evidence for a named cell", "Universal Robots ecosystem"],
    ], M, 1.95, 7.6, { colW: [1.35, 1.45, 3.0, 1.8], size: 9, rowH: 0.5, boldFirst: true });
    L.card(pres, s, 8.5, 1.95, 4.25, 2.55, { fill: C.ink, title: "Pilot design", titleColor: C.white, body: "Same batch through four baselines: the customer’s scripts, simple rules, VLM + rules, full Engine. Expert ground truth built independently; natural and injected errors reported separately.\nAcceptance: critical false-accepts, good-data false-rejects, unknown rate, review hours per 1,000 episodes, end-to-end time.\nCustomer keeps a blind held-out set; model, compute and data budget are fixed.", bodySize: 9.5, bodyColor: "D9DCE8" });
    L.table(pres, s, [
      ["If the pilot shows…", "We…"],
      ["Simple rules match the full Engine at equal cost", "Narrow to the error classes rules miss"],
      ["Every account needs heavy redesign", "Shrink the task domain, price as a service"],
      ["Augmentation adds no real-world lift", "Recalibrate the generator and the mixture"],
      ["Runtime tail latency fails acceptance", "Keep the module offline"],
      ["Engine beats every baseline and the customer renews", "Scale team, scenes and channels"],
    ], M, 4.75, 7.6, { colW: [4.3, 3.3], size: 9, rowH: 0.29, boldFirst: false });
    L.card(pres, s, 8.5, 4.75, 4.25, 1.75, { fill: C.crimsonSoft, title: "The one number we run on", titleColor: C.crimson, titleSize: 11.5, body: "Verified trajectory hours certified per quarter. Every revenue line sits downstream of it; it measures supply (throughput), demand (who pays for a passport) and quality (what passes) at once.", bodySize: 9.5 });
    L.footer(pres, s, n, "Sources: AXIOMALITY pilot plan (Sep 2026); public workflow examples from company announcements.");
  }

  // ───────────── 11. Traction & next 90 days ─────────────
  {
    const s = pres.addSlide(); n++;
    L.header(pres, s, { tag: "TRACTION", title: "What exists today is assets and relationships; what we will prove in 90 days is three things", sub: "Every target carries a date; at least one named design partner moves to “achieved” before the round closes" });
    const cols = [
      ["CircleCheck", "Achieved", C.tealSoft, [
        "Knowledge kernel: axioms machine-checked consistent, aligned with ISO/IEC 21838-4 (TUpper / COLORE lineage)",
        "100,000 measured 3D packages; room-level reconstruction and object-level 3D annotation stack (9 invention applications)",
        "Consumer spatial app live on Apple Vision Pro; 13 granted patents",
        "Beijing International Big Data Exchange data-broker license (China channel)",
        "Working relationships: an international law firm (clause mapping), a Big Four firm (audit-pack review), multinational medical-device and pharma companies",
      ]],
      ["Loader", "In progress", C.panel, [
        "Minimum Engine, internal test Q4 2026: ingest → scene graph → SMT check → Passport",
        "Kernel v1 for home scenes; connectors for LeRobot v3, RLDS, OpenUSD",
        "Co-development and channel talks with humanoid OEMs and platform / OS companies",
      ]],
      ["Target", "Next 90 days (committed)", C.crimsonSoft, [
        "Public blind benchmark: 200 DROID + 200 LeRobot episodes with 7 injected error classes; Engine vs. rules + VLM baseline; per-class recall and cost per hour; a third party holds the injection key",
        "One named design partner (data supplier or OEM) running real passports on their own data under NDA",
        "Public Passport spec, public key and CLI verifier with a passport for one open dataset: tamper it, and the verifier fails",
      ]],
    ];
    for (let i = 0; i < 3; i++) {
      const x = M + i * 4.1;
      L.card(pres, s, x, 1.95, 3.9, 3.7, { fill: cols[i][2], title: cols[i][1], titleIndent: 0.5 });
      await L.icon(s, cols[i][0], x + 0.2, 2.1, 0.36, { bg: i === 2 ? C.crimson : C.ink });
      L.bullets(pres, s, x + 0.22, 2.6, 3.46, 2.95, cols[i][3], { size: 9.5, paraSpace: 5 });
    }
    L.table(pres, s, [
      ["Dated targets", "Q1 2027", "Q2 2027", "Month 18", "2028"],
      ["Milestone", "3 co-development partners; 10,000 verified episodes", "Passport v1 recognized by one assessment body or standards organization", "5 cumulative paying customers; 2 renewals or expansions", "Audit packs delivered before EU Annex I applies"],
    ], M, 5.85, W - 2 * M, { colW: [1.4, 2.6, 2.9, 2.5, 2.73], size: 9, rowH: 0.34, boldFirst: true });
    L.footer(pres, s, n, "Source: AXIOMALITY records (available on request). Targets are plans, not contracts.");
  }

  // ───────────── 12. Team ─────────────
  {
    const s = pres.addSlide(); n++;
    L.header(pres, s, { tag: "TEAM", title: "Why us: we co-wrote the standard, we proved it consistent, and we have run a $50M-revenue company", sub: "Ontology and standards, AI algorithms, perception and robotics, simulation and 3D assets" });
    L.card(pres, s, M, 1.95, 6.2, 4.55, { fill: C.ink, title: "Founder & CEO", titleColor: C.white, titleSize: 15 });
    L.bullets(pres, s, M + 0.22, 2.5, 5.8, 3.9, [
      { text: "Standards: core contributor to ISO/IEC 21838-4 (TUpper top-level ontology); member of the Industrial Ontologies Foundry; University of Toronto AI doctorate and researcher", options: { color: C.white } },
      { text: "Science: formal ontology and knowledge representation, consistency proofs and model construction for first-order axiom systems, trustworthy neuro-symbolic AI; 21 papers, FOIS best-paper award, invited AAAI talk, one English-language monograph", options: { color: C.white } },
      { text: "Operating: founding team of a cross-border DTC platform backed by Accel and others ($5M angel), >$50M revenue in year one, 100+ person team; co-founded a recommendation-systems company incubated at Toronto and Imperial", options: { color: C.white } },
      { text: "Spatial computing: founded a spatial-computing company, one of the first AR apps on Apple Vision Pro; 13 granted patents, ¥24M patent transfer, ¥10M technology license; prior VC diligence experience", options: { color: C.white } },
    ], { size: 10.5, paraSpace: 8 });
    const team = [
      ["CTO & Chief Scientist", "McMaster University AI doctorate; former AI algorithm scientist at a top-tier tech company and startup chief scientist; first place, Canadian AI academic and industrial applications competition"],
      ["Perception & Robotics Lead", "Harbin Institute of Technology doctorate in mechatronics; former AI algorithm engineer and director of the perception center at XPeng; 10+ papers"],
      ["Simulation & 3D Assets Lead", "10+ years as art director in games and stage production; led the digital (VR) reconstruction of 1750 Beijing"],
    ];
    team.forEach((t, i) => L.card(pres, s, 7.1, 1.95 + i * 1.17, 5.6, 1.05, { fill: C.panel, title: t[0], titleSize: 11.5, body: t[1], bodySize: 9.5 }));
    L.card(pres, s, 7.1, 5.5, 5.6, 1.0, { fill: C.crimsonSoft, title: "Hiring with this round", titleColor: C.crimson, titleSize: 11.5, body: "A robot-learning scientist who has trained VLA policies at scale (owns the benchmark and training-lift experiments); a U.S.-based founding GTM lead for data suppliers and OEMs.", bodySize: 9.5 });
    L.footer(pres, s, n);
  }

  // ───────────── 13. Ask ─────────────
  {
    const s = pres.addSlide(); n++;
    L.darkBg(pres, s);
    L.label(pres, s, "AXIOMALITY", M, 0.55, 4, 0.35, { size: 13, bold: true, color: C.white, extra: { charSpacing: 4 } });
    L.label(pres, s, "The evidence format for robot data will decide\nhow it is measured, priced and traded.", M, 1.3, 11.5, 1.5, { head: true, size: 28, bold: true, color: C.white, ls: 1.15 });
    L.label(pres, s, "We are raising a seed round to turn a verified rulebook into the reference implementation: public spec, offline-verifiable passports, no customer data ownership, no foundation model of our own.", M, 2.9, 11, 0.8, { size: 13, color: "C9CDDB" });
    // ask box
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: M, y: 3.95, w: 5.6, h: 2.6, fill: { color: C.ink2 }, line: { color: C.ink2 }, rectRadius: 0.08 });
    L.label(pres, s, "Raising", M + 0.25, 4.12, 3, 0.3, { size: 11, bold: true, color: "9AA0B4", extra: { charSpacing: 2 } });
    L.label(pres, s, "$4–6M seed", M + 0.25, 4.4, 5, 0.6, { head: true, size: 28, bold: true, color: C.crimson });
    L.label(pres, s, "Sized to the 18-month plan with a collection buffer (amount is this revision’s suggestion; founders to confirm). Use: core product 45%, independent validation and benchmarks 25%, U.S. GTM and design partners 20%, operations 10%.", M + 0.25, 5.05, 5.1, 1.4, { size: 10.5, color: "D9DCE8" });
    const gates = [
      ["Months 0–3", "Vertical slice: one task, one connector, public benchmark, reproducible evidence package"],
      ["Months 4–9", "Two paid validation engagements; all implementation and review effort recorded"],
      ["Months 10–18", "Five cumulative customers, two renewals or expansions; second embodiment reused without kernel edits"],
    ];
    gates.forEach((g, i) => {
      const y = 3.95 + i * 0.88;
      L.stepChip(pres, s, 6.6, y + 0.05, i + 1, { d: 0.38 });
      L.label(pres, s, g[0], 7.1, y, 5.6, 0.3, { head: true, size: 12.5, bold: true, color: C.white });
      L.label(pres, s, g[1], 7.1, y + 0.3, 5.6, 0.55, { size: 10, color: "D9DCE8" });
    });
    L.label(pres, s, "Three ways to help now: lead the round; introduce one data supplier and one OEM; bring your own data and get a real passport under NDA in a 12-minute session.", M, 6.7, 12, 0.35, { size: 10.5, italic: true, color: "C9CDDB" });
    L.label(pres, s, "© 2026 AXIOMALITY · Confidential", W - M - 3.5, H - 0.42, 3.5, 0.3, { size: 9, color: "9AA0B4", align: "right" });
  }

  fs.mkdirSync(path.dirname(OUT), { recursive: true });
  await pres.writeFile({ fileName: OUT });
  console.log("wrote", OUT, "slides:", n);
})().catch((e) => { console.error(e); process.exit(1); });
