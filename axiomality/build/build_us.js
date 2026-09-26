// AXIOMALITY — YC / a16z deck v2 (12 slides, no financing ask)
// Positioning: acceptance testing for robot training data — the inspection layer of the robot-data market
const L = require("./lib");
const { C, W, H, M } = L;
const path = require("path");
const fs = require("fs");

const PROTO = "/home/user/ipython/axiomality/prototype";
const DEMO = require("./demo_numbers.json");
const OUT = process.argv[2] || path.join(__dirname, "out", "AXIOMALITY_Seed_Deck_v2.pptx");
const FOOT = "AXIOMALITY  ·  September 2026  ·  Confidential";
function fig(name) { const p = path.join(PROTO, "figures", name); return fs.existsSync(p) ? p : null; }

(async () => {
  const pres = L.newDeck("en", { title: "AXIOMALITY", footer: FOOT });
  const F = pres._F;
  let n = 0;

  // 1 ── Cover
  {
    const s = pres.addSlide(); n++;
    L.darkBg(pres, s);
    L.label(pres, s, "AXIOMALITY", M, 0.55, 4, 0.35, { size: 13, bold: true, color: C.white, extra: { charSpacing: 4 } });
    L.label(pres, s, "We inspect robot training data\nbefore labs pay for it,\nand sign the result.", M, 1.3, 7.6, 2.4, { head: true, size: 28, bold: true, color: C.white, ls: 1.1 });
    L.label(pres, s, "The inspection record a lab accepts at intake: a verdict per episode, a reason for every reject, and a signed passport anyone can verify offline. Prototype runs on public data; no customers yet.", M, 3.85, 7.3, 0.9, { size: 14, color: "C9CDDB" });
    L.pill(pres, s, "Working prototype · see slide 5", M, 4.9, 2.9, 0.36, { fill: C.teal, color: C.white, size: 10.5 });
    const f2 = fig("passport_card.png");
    if (f2) {
      const w = 4.35, h = w * DEMO.fig2_ratio, y = Math.max(1.2, 3.25 - h / 2);
      s.addShape(pres.shapes.RECTANGLE, { x: 8.35, y: y - 0.12, w: w + 0.24, h: h + 0.24, fill: { color: C.ink2 }, line: { color: C.ink2 } });
      s.addImage({ path: f2, x: 8.47, y, w, h });
      L.brackets(pres, s, 8.35, y - 0.12, w + 0.24, h + 0.24, C.crimson, 0.22, 1.5);
      L.label(pres, s, "Real prototype output: a signed passport over synthetic episodes seeded from the company’s measured scan geometry", 8.35, y + h + 0.18, w + 0.24, 0.45, { size: 9, color: "9AA0B4" });
    }
    const stats = [
      [DEMO.us_cover_big, DEMO.us_cover_label],
      ["Signed", "Change any covered value and verification fails (demo key today)"],
      ["Offline", "Buyers verify with a public key, no call to us"],
      ["In your VPC", "The engine runs where the data lives; we never hold it"],
    ];
    stats.forEach((st, i) => {
      const x = M + i * 3.05;
      s.addShape(pres.shapes.LINE, { x, y: 5.6, w: 2.7, h: 0, line: { color: "3A4160", width: 0.75 } });
      L.stat(pres, s, x, 5.7, 2.85, 1.1, st[0], st[1], { dark: true, size: 19, labelSize: 10 });
    });
    s.addNotes("30-second open: robot data is now bought and sold, and almost none of it is inspected by a neutral party. We are the inspection layer. The prototype runs today; slide 5 has the numbers.");
  }

  // 2 ── Problem
  {
    const s = pres.addSlide(); n++;
    L.header(pres, s, { tag: "PROBLEM", title: "Labs buy robot data blind; vendors can’t prove what they sold", sub: "Acceptance today is a sample video and a spot check" });
    const fy = 2.05;
    L.card(pres, s, M, fy, 3.6, 1.6, { fill: C.panel, title: "Vendors", body: "Teleop fleets, data factories and synthetic generators sell hours at $50–200/h. Good vendors can’t prove they are better than bad ones.", bodySize: 10.5 });
    L.card(pres, s, W - M - 3.6, fy, 3.6, 1.6, { fill: C.panel, title: "Labs", body: "Robot foundation-model teams pay by the hour, then discover problems during training, weeks later and after the compute is spent.", bodySize: 10.5 });
    const gx = M + 3.85, gw = W - 2 * M - 7.7;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: gx, y: fy, w: gw, h: 1.6, fill: { color: C.crimsonSoft }, line: { color: C.crimson, width: 1, dashType: "dash" }, rectRadius: 0.08 });
    L.label(pres, s, "Missing: an inspection", gx + 0.2, fy + 0.2, gw - 0.4, 0.35, { head: true, size: 15, bold: true, color: C.crimson, align: "center" });
    L.label(pres, s, "No per-episode verdict · no reason for a reject · no record both sides trust", gx + 0.2, fy + 0.65, gw - 0.4, 0.7, { size: 11, align: "center" });
    L.arrow(pres, s, M + 3.62, fy + 0.8, 0.2, { color: C.crimson });
    L.arrow(pres, s, gx + gw + 0.02, fy + 0.8, 0.2, { color: C.crimson });
    const st = [["89%", "of visual-AI teams blame data for model failures (Voxel51, 2026)"], ["58,000+", "datasets on the LeRobot hub; none validated or signed"], ["$50–200 / h", "teleop data, sold with no record of what is usable"], ["48%", "of visual-AI teams cite data-quality problems (Voxel51, 2026)"]];
    st.forEach((x, i) => L.stat(pres, s, M + i * 3.05, 4.1, 2.9, 1.15, x[0], x[1], { size: 24, labelSize: 10 }));
    L.card(pres, s, M, 5.5, W - 2 * M, 0.95, { fill: C.panel, body: "What goes wrong is not exotic: mislabeled objects, phases out of order, a gripper that “grasps” while open, objects that teleport or float, clocks that run backwards. Rule scripts catch the easy half. The other half needs to know what the scene means.", bodySize: 10.5 });
    L.footer(pres, s, n, "Sources: Voxel51 State of Visual AI (2026); Hugging Face (May 2026); DreamVu, Robot Training Data Companies: The 2026 Landscape; Open X-Embodiment (2023).");
  }

  // 3 ── Why now
  {
    const s = pres.addSlide(); n++;
    L.header(pres, s, { tag: "WHY NOW", title: "In 2026 robot data became a traded commodity, with no inspector", sub: "Vendors are scaling, generators are flooding training, and buyers are writing big checks" });
    const cols = [
      ["Store", "Vendors scaled", ["Scale: physical-AI engine past 150k hours; neutrality questioned after Meta", "Mecka: ~$500M round in talks (Sep 2026)", "XDOF: ~$1.2B valuation (Sep 2026)", "Build AI: ~1M hours of factory video released free (Apr 2026)"]],
      ["Sparkles", "Generators arrived", ["World Labs’ Atlas (Sep 2026) turns phone video into robot-camera data", "NVIDIA’s data-factory blueprint scores generated clips for free", "More synthetic data means more data entering training that no one inspected"]],
      ["Banknote", "Buyers are spending", ["$18.6B physical-AI venture funding in Q2 2026 alone", "Physical Intelligence (~$11B), Skild ($14B), Generalist ($3B), Figure ($39B) spend heavily on data", "Our hypothesis: buyers want a neutral referee at intake"]],
    ];
    for (let i = 0; i < 3; i++) {
      const x = M + i * 4.1;
      L.card(pres, s, x, 1.95, 3.9, 4.0, { fill: C.panel, title: cols[i][1], titleIndent: 0.5 });
      await L.icon(s, cols[i][0], x + 0.2, 2.1, 0.36, { bg: C.crimson });
      L.bullets(pres, s, x + 0.22, 2.62, 3.46, 3.2, cols[i][2], { size: 10.5, paraSpace: 8 });
    }
    L.label(pres, s, "Regulation is a later tailwind, not the reason: EU AI Act obligations for AI embedded in machinery apply from 2 Aug 2028 (Reg. 2026/1744).", M, 6.1, W - 2 * M, 0.4, { size: 10, italic: true, color: C.muted });
    L.footer(pres, s, n, "Sources: Scale AI; press reports on Mecka and XDOF (Sep 2026); Build AI (Apr 2026); World Labs (Sep 2026); NVIDIA (Mar 2026); PitchBook Q2 2026; company announcements.");
  }

  // 4 ── Product
  {
    const s = pres.addSlide(); n++;
    L.header(pres, s, { tag: "PRODUCT", title: "Episodes in; a verdict per episode and a signed passport out", sub: "Three check families. On today's public data only the first runs fully; next, we derive object state from video so the other two run on real data." });
    const layers = [
      ["ListChecks", "Is the record intact?", "Monotonic clocks, dropped frames, NaNs, joint limits, required metadata", "Scripts do this; so do we"],
      ["Move3D", "Is the motion possible?", "Interpenetration, unsupported objects, teleports, gripper-to-object distance", "Needs scene geometry and relations"],
      ["Network", "Does the story contradict itself?", "Task-phase order, gripper state vs contact events, object class vs affordance", "Needs a rulebook proven contradiction-free"],
    ];
    for (let i = 0; i < 3; i++) {
      const y = 2.0 + i * 1.05;
      s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: M, y, w: 7.4, h: 0.92, fill: { color: i === 2 ? C.ink : C.panel }, line: { color: i === 2 ? C.ink : C.panel }, rectRadius: 0.08 });
      await L.icon(s, layers[i][0], M + 0.2, y + 0.24, 0.44, { bg: C.crimson });
      L.label(pres, s, layers[i][1], M + 0.8, y + 0.08, 4.3, 0.38, { head: true, size: 13, bold: true, color: i === 2 ? C.white : C.text });
      L.label(pres, s, layers[i][2], M + 0.8, y + 0.47, 4.3, 0.42, { size: 9.5, color: i === 2 ? "D9DCE8" : C.text });
      L.label(pres, s, layers[i][3], M + 5.2, y + 0.1, 2.05, 0.72, { size: 9.5, italic: true, color: i === 2 ? "F4A3B5" : C.muted, valign: "middle" });
    }
    L.table(pres, s, [
      ["Verdict", "Meaning", "What happens"],
      ["Accept", "All three checks pass", "Billable and trainable"],
      ["Repair", "Correctable recording defect (e.g., timestamps out of order)", "New derived version; original kept"],
      ["Reject", "Violates a rule; frame and rule ID attached", "Back to the vendor as a re-collect list"],
      ["Unknown", "Inputs needed for the check are missing", "Says exactly what is missing; never counted as a pass"],
    ], M, 5.25, 7.4, { colW: [0.95, 3.6, 2.85], size: 9, rowH: 0.25, boldFirst: true });
    const pr = [
      ["Valid failures are kept", "A cup that really slips is valuable failure data, not bad data. We never rewrite a real failure into a success."],
      ["Signed, offline-verifiable", "The passport binds the data hash and rulebook version. Seller, buyer or anyone else verifies with a public key."],
      ["Runs in your environment", "Data never leaves the customer’s VPC. We ship the engine and the rulebook; we never own the data."],
    ];
    pr.forEach((p, i) => L.card(pres, s, 8.35, 2.0 + i * 1.52, 4.4, 1.38, { fill: i === 1 ? C.tealSoft : C.panel, title: p[0], titleSize: 12.5, body: p[1], bodySize: 10 }));
    L.footer(pres, s, n);
  }

  // 5 ── Demo A: real data
  {
    const s = pres.addSlide(); n++;
    L.header(pres, s, { tag: "DEMO \u00b7 REAL DATA", title: "On real DROID data: a stuck arm, a mis-documented field, a possible arm mismatch", sub: "Could a script find these? Yes. We add doing it on every batch, signing the result, and listing what we could not check. 41 episodes from DROID, Jaco Play, NYU ROT." });
    const f = fig("real_finding_example.png");
    if (f) s.addImage({ path: f, x: M, y: 1.98, w: 7.4, h: 3.7 });
    const finds = [
      ["Stuck arm / frozen stream", "DROID ep. 3, frames 19\u201333: the commanded joint position moves (median 0.133 rad) while the measured joints stay bit-identical; frames 43\u201349 are duplicated rows. A policy trained on it learns that commands do nothing."],
      ["Joint past its limit", "DROID ep. 1, frames 141\u2013172: joint 6 reaches 3.959 rad, 207 mrad past the Panda datasheet limit. It may be an FR3 (limit 4.52 rad); the passport records that ambiguity."],
      ["Field doesn\u2019t match its docs", "DROID\u2019s action field is documented as six joint velocities; in all 2,551 frames it equals the commanded Cartesian pose. 8 of 14 episodes carry no language instruction."],
    ];
    finds.forEach((t, i) => L.card(pres, s, 8.2, 1.98 + i * 1.5, 4.55, 1.38, { fill: i === 0 ? C.crimsonSoft : C.panel, title: t[0], titleSize: 11.5, titleColor: i === 0 ? C.crimson : C.text, body: t[1], bodySize: 9 }));
    L.table(pres, s, [
      ["Dataset", "Episodes / frames", "Accept*", "Repair", "Reject", "Not checked", "Passport"],
      ["DROID (Franka)", "14 / 2,551", "5", "1", "8", "Timing, semantic", "Verified offline"],
      ["Jaco Play (Kinova)", "13 / 879", "13", "0", "0", "Timing, semantic", "Verified offline"],
      ["NYU ROT (xArm)", "14 / 440", "14", "0", "0", "Timing, semantic", "Verified offline"],
    ], M, 5.78, 7.4, { colW: [1.6, 1.25, 0.65, 0.6, 0.6, 1.3, 1.4], size: 8.5, rowH: 0.21, boldFirst: true });
    L.footer(pres, s, n, "Real, public data (OXE public bucket). *Accept covers checkable families only: these datasets record no timestamps or object state. On DROID the structural baseline agrees with the engine on 8 of 14 accept/reject calls; the stuck-arm and joint-limit episodes are ones DROID itself labels as failures.");
  }

  // 6 ── Demo B: honest comparison
  {
    const s = pres.addSlide(); n++;
    L.header(pres, s, { tag: "DEMO \u00b7 SYNTHETIC BENCHMARK", title: "Checks are copyable; a neutral, signed record is not", sub: "Noisy synthetic data, 3 task variants, 20 per error class; no checker reads the injection key; precision 1.00 for all three" });
    const f = fig("benchmark_v2_sensitivity.png");
    if (f) s.addImage({ path: f, x: M, y: 1.98, w: 6.9, h: 6.9 * 0.4062 });
    L.table(pres, s, [
      ["", "AXIOMALITY engine", "Our strong baseline", "Structural (afternoon)"],
      ["Recall", "92%", "92%", "41%"],
      ["False rejects (140 clean)", "0", "0", "0"],
      ["Out-of-order clocks restored exactly", "20 / 20", "0 (discarded)", "0 (discarded)"],
      ["Missing inputs", "Returns UNKNOWN", "Rejects", "Rejects"],
      ["Per episode", "14 ms", "1.4 ms", "0.6 ms"],
    ], M, 4.92, 7.9, { colW: [2.6, 1.75, 1.75, 1.8], size: 9, rowH: 0.26, boldFirst: true });
    const pts = [
      ["What we don\u2019t hide", "Our own strong baseline, written after the engine, matches its recall. Knowing what to check is not a moat: any team that knows the error list can write the checks."],
      ["Where the engine still wins", "Finer detection: sinks from 25 mm (baseline 40 mm), post-release jumps from 30 mm (baseline 60 mm). Exact repair of out-of-order clocks. UNKNOWN instead of false rejects. Every verdict cites a versioned, hash-bound rule."],
      ["So where is the moat", "A neutral issuer, re-checkable verdicts, passports that verify offline, and an error library that grows across customers: things no single buyer or seller builds for itself."],
    ];
    pts.forEach((t, i) => L.card(pres, s, 8.75, 1.98 + i * 1.55, 4.0, 1.43, { fill: i === 2 ? C.tealSoft : C.panel, title: t[0], titleSize: 11, body: t[1], bodySize: 8.8 }));
    L.footer(pres, s, n, "Internal prototype, synthetic data; the same team wrote the injector, the engine and the baselines. Full results and code: prototype/results/benchmark_v2.md, reproducible in one command.");
  }

  // 6 ── Why the rulebook
  {
    const s = pres.addSlide(); n++;
    L.header(pres, s, { tag: "HOW IT WORKS", title: "Versioned, hash-bound, consistency-checked rules: anyone can re-derive a verdict", sub: "A VLM judge gives you a plausibility score. We give you a trail anyone can re-check." });
    const layers = [
      ["Top level · TUpper (ISO/IEC 21838-4:2023)", "One of three top-level ontologies with an ISO part, alongside BFO and DOLCE; our founder is a core contributor", C.ink, C.white],
      ["Physical world", "Objects, parts, shape, measurement, materials, process", C.ink2, C.white],
      ["Robot manipulation", "Affordances, contact events, task phases, joint limits, object permanence", "3A4160", C.white],
      ["Your episodes", "Frames, sensors, lineage; LeRobot / RLDS / MCAP", C.panel2, C.text],
    ];
    let ly = 1.95;
    layers.forEach((l) => {
      s.addShape(pres.shapes.RECTANGLE, { x: M, y: ly, w: 6.0, h: 0.72, fill: { color: l[2] }, line: { color: l[2] } });
      L.label(pres, s, l[0], M + 0.2, ly + 0.06, 5.6, 0.3, { head: true, size: 11.5, bold: true, color: l[3] });
      L.label(pres, s, l[1], M + 0.2, ly + 0.37, 5.6, 0.3, { size: 9, color: l[3] === C.white ? "D9DCE8" : C.text });
      ly += 0.8;
    });
    L.card(pres, s, M, 5.2, 6.0, 1.3, { fill: C.tealSoft, title: "Rulebook self-check (in the prototype)", titleSize: 11.5, body: DEMO.us_selfcheck, bodySize: 10 });
    L.table(pres, s, [
      ["", "VLM judge / learned scorer", "AXIOMALITY verdict"],
      ["Output", "A score per clip", "Accept / repair / reject / unknown per episode"],
      ["Reason", "Opaque", "Frame index + rule ID + evidence"],
      ["Re-checkable by a third party", "Re-runnable with the same weights; no rule-level reason", "Yes: same rulebook + data hash reproduce the verdict"],
      ["Missing inputs", "Still returns a score", "Returns “unknown” and lists what is missing"],
      ["Improves by", "Retraining", "Adding a rule, proven consistent before release"],
    ], 7.1, 1.95, 5.65, { colW: [1.65, 1.8, 2.2], size: 9.5, rowH: 0.5, boldFirst: true });
    L.card(pres, s, 7.1, 5.2, 5.65, 1.3, { fill: C.panel, title: "The error library we keep (planned, not in the prototype)", titleSize: 11.5, body: "Rejects cluster into candidate rules; each is proven consistent with the rest before release, and older batches are re-verified. The moat hypothesis: the rulebook stays consistent and citable at hundreds of rules across task families.", bodySize: 9.5 });
    L.footer(pres, s, n, "Sources: ISO/IEC 21838-4:2023; ISO/IEC 24707 (Common Logic); COLORE, University of Toronto; Z3.");
  }

  // 7 ── Competition 2x2
  {
    const s = pres.addSlide(); n++;
    L.header(pres, s, { tag: "COMPETITION", title: "Everyone scores data; we found no one signing neutral per-episode verdicts", sub: "No one signs per-episode physics and logic checks for robot data. The tools where data lives are our rails, not rivals." });
    const gx = M, gy = 2.05, gw = 6.6, gh = 4.3;
    s.addShape(pres.shapes.RECTANGLE, { x: gx, y: gy, w: gw, h: gh, fill: { color: "FAFAFC" }, line: { color: C.line, width: 0.75 } });
    s.addShape(pres.shapes.LINE, { x: gx + gw / 2, y: gy, w: 0, h: gh, line: { color: C.line, width: 0.75 } });
    s.addShape(pres.shapes.LINE, { x: gx, y: gy + gh / 2, w: gw, h: 0, line: { color: C.line, width: 0.75 } });
    s.addShape(pres.shapes.RECTANGLE, { x: gx + gw / 2, y: gy, w: gw / 2, h: gh / 2, fill: { color: C.tealSoft }, line: { color: C.tealSoft } });
    L.label(pres, s, "↑ Signed, re-checkable evidence", gx + 0.12, gy + 0.1, 3.0, 0.3, { size: 9.5, bold: true, color: C.teal });
    L.label(pres, s, "Self or vendor-run  ←→  Neutral third party", gx, gy + gh + 0.06, gw, 0.3, { size: 9.5, color: C.muted, align: "center" });
    L.label(pres, s, "Score only", gx + 0.12, gy + gh - 0.35, 2, 0.3, { size: 9, color: C.muted });
    const dots = [
      ["NVIDIA Cosmos Evaluator (free)", 0.22, 0.72, C.ink],
      ["Applied Intuition Dana", 0.3, 0.6, C.ink],
      ["Instance, Shotwell (YC)", 0.18, 0.86, C.ink],
      ["Vendor self-QA (Scale, Mecka)", 0.1, 0.5, C.ink],
      ["Pebblous (KR) data certification", 0.7, 0.58, C.ink],
      ["Lab in-house pipelines", 0.12, 0.3, C.ink],
      ["AXIOMALITY", 0.82, 0.18, C.crimson],
    ];
    dots.forEach((d) => {
      const x = gx + d[1] * gw, y = gy + d[2] * gh;
      const big = d[3] === C.crimson;
      s.addShape(pres.shapes.OVAL, { x: x - (big ? 0.13 : 0.08), y: y - (big ? 0.13 : 0.08), w: big ? 0.26 : 0.16, h: big ? 0.26 : 0.16, fill: { color: d[3] }, line: { color: d[3] } });
      if (!big && x + 2.65 > gx + gw) L.label(pres, s, d[0], x - 1.25, y + 0.12, 2.5, 0.3, { size: 9, color: C.text, align: "center" });
      else L.label(pres, s, d[0], Math.min(x + 0.15, gx + gw - 2.6), y - 0.14, 2.5, 0.3, { size: big ? 11 : 9, bold: big, color: big ? C.crimson : C.text });
    });
    const notes = [
      ["vs. NVIDIA", "Cosmos Evaluator scores plausibility; it does not sign, does not give rule-level reasons, and lives in one stack. A stack vendor cannot credibly be the neutral referee. We take its score as one input."],
      ["vs. in-house QA", "In-house QA needs no signature today. It does once one intake gate must hold vendor, in-house and synthetic data to one standard. That gate is where we aim; vendors are the first door."],
      ["Rails, not rivals", "Foxglove, Rerun and the LeRobot hub are where data lives. The passport ships as their “verified” badge."],
    ];
    notes.forEach((t, i) => L.card(pres, s, 7.75, 2.05 + i * 1.48, 5.0, 1.36, { fill: C.panel, title: t[0], titleSize: 11.5, body: t[1], bodySize: 9.5 }));
    L.footer(pres, s, n, "Placement is AXIOMALITY’s assessment from public product documentation (2025–26).");
  }

  // 8 ── Business model
  {
    const s = pres.addSlide(); n++;
    L.header(pres, s, { tag: "BUSINESS MODEL", title: "Vendors pay per certified dataset; buyers verify for free", sub: "Revenue scales with robot-data volume that changes hands, not with consulting hours" });
    const cards = [
      ["Paid pilot", "$25k–50k · 8–12 weeks", "One vendor, one task family, their own batch; blind bake-off against their current scripts; credited to year one"],
      ["Per certified hour", "Target 5–8% of data price", "Vendor pays to ship with a passport; buyer verifies free with the public key, which pulls the next vendor in"],
      ["In-VPC license", "Annual", "Large vendors and labs run the engine in their own environment with rulebook updates"],
    ];
    cards.forEach((c, i) => {
      const x = M + i * 4.1;
      L.card(pres, s, x, 1.95, 3.9, 1.95, { fill: i === 1 ? C.crimsonSoft : C.panel, title: c[0], titleSize: 13 });
      L.label(pres, s, c[1], x + 0.22, 2.38, 3.4, 0.35, { head: true, size: 13, bold: true, color: C.crimson });
      L.label(pres, s, c[2], x + 0.22, 2.8, 3.46, 1.05, { size: 10 });
    });
    L.label(pres, s, "Market = robot data changing hands × inspection take rate (model)", M, 4.15, 8, 0.35, { head: true, size: 13, bold: true });
    L.table(pres, s, [
      ["Scenario", "Hours traded / year", "Avg price", "Data spend", "Take rate*", "Inspection revenue pool"],
      ["Today’s pace", "1M", "$100/h", "$100M", "5%", "$5M"],
      ["Industry target", "10M", "$100/h", "$1B", "6%", "$60M"],
      ["Synthetic + real, 2030", "10M real + 100M synthetic", "$100/h real, $5/h synthetic", "$1.5B", "8%", "$120M"],
    ], M, 4.55, 8.0, { colW: [1.6, 1.75, 1.45, 1.05, 0.9, 1.25], size: 9, rowH: 0.4, boldFirst: true });
    L.card(pres, s, 8.85, 4.15, 3.9, 2.35, { fill: C.panel, title: "What makes it venture scale", titleSize: 11.5, body: "Third-party inspection of traded data alone is a $5\u2013120M pool. Venture scale needs the intake gate for all training data, in-house and synthetic included; the lab bake-off tests exactly that. Later: the same passport becomes OEM compliance evidence (EU 2028).", bodySize: 9.5 });
    L.footer(pres, s, n, "Model, not a forecast. Inputs: ~10M-hour industry estimate of data needed; teleop pricing $50–200/h (DreamVu); Scale 150k+ h (2025). *Take rates are hypotheses the pilots test; synthetic volume is an assumption.");
  }

  // 9 ── GTM
  {
    const s = pres.addSlide(); n++;
    L.header(pres, s, { tag: "GO-TO-MARKET", title: "Start with challenger vendors who need to beat Scale on trust", sub: "The buyer is the vendor’s head of data ops; the proof is a blind bake-off on their own batch" });
    L.table(pres, s, [
      ["Target accounts (not customers)", "Type", "Why they need a passport"],
      ["Mecka", "Teleop data vendor", "Scaling fast; needs to prove quality to lab buyers"],
      ["XDOF", "Data pipeline + teleop", "Selling to labs at a $1.2B valuation; trust is the product"],
      ["Build AI", "Egocentric video", "Free data needs a quality story to monetize premium tiers"],
      ["Human Archive", "Egocentric data vendor", "Seed-stage; differentiation against larger suppliers"],
      ["Lightwheel", "Synthetic / sim data", "Synthetic data needs independent acceptance"],
      ["Labs buying data", "Model developer intake", "Accept passports at intake; verification is free"],
    ], M, 1.95, 7.4, { colW: [2.2, 1.9, 3.3], size: 9.5, rowH: 0.42, boldFirst: true });
    L.card(pres, s, 8.3, 1.95, 4.45, 3.05, { fill: C.ink, title: "Blind bake-off", titleColor: C.white, body: "Same batch through four baselines: the vendor’s scripts, simple rules, VLM + rules, our engine.\nExpert ground truth built independently; the customer holds a blind set.\nMetrics: critical false-accepts, good-data false-rejects, unknown rate, review hours per 1,000 episodes.\nIf simple rules match us, we narrow to the error classes they miss.", bodySize: 9.5, bodyColor: "D9DCE8" });
    L.card(pres, s, 8.3, 5.15, 4.45, 1.35, { fill: C.crimsonSoft, title: "Then flip the buyer side", titleColor: C.crimson, titleSize: 11.5, body: "Once one lab accepts passports at intake, every vendor selling to that lab has a reason to ship with one.", bodySize: 9.5 });
    L.footer(pres, s, n, "Accounts are targets chosen from public information; none is a customer or partner today.");
  }

  // 10 ── Built + Dec 31
  {
    const s = pres.addSlide(); n++;
    L.header(pres, s, { tag: "TRACTION", title: "What’s built, and three things you can check by Dec 31", sub: "Everything on this slide can be demonstrated live" });
    const cols = [
      ["Cpu", "Working prototype", C.tealSoft, DEMO.us_proto_bullets],
      ["CircleCheck", "Foundations", C.panel, [
        "Company knowledge kernel: formal axioms built on the ISO/IEC 21838-4 top-level ontology",
        "100,000 measured 3D asset packages from a prior spatial-computing company, proof we can capture and annotate real geometry",
        "13 granted patents; consumer spatial app shipped on Apple Vision Pro",
      ]],
      ["Target", "By Dec 31, 2026", C.crimsonSoft, [
        "One paid pilot or signed LOI with a data vendor",
        "One lab\u2019s written intake requirement to accept passports",
        "Rerun on DROID / LeRobot data against a strong hand-written baseline and Cosmos Evaluator; a third party holds the key. If our margin is under 10 points, we narrow to the error classes rules miss",
      ]],
    ];
    for (let i = 0; i < 3; i++) {
      const x = M + i * 4.1;
      L.card(pres, s, x, 1.95, 3.9, 4.55, { fill: cols[i][2], title: cols[i][1], titleIndent: 0.5 });
      await L.icon(s, cols[i][0], x + 0.2, 2.1, 0.36, { bg: i === 2 ? C.crimson : C.ink });
      L.bullets(pres, s, x + 0.22, 2.6, 3.46, 3.8, cols[i][3], { size: 10, paraSpace: 8 });
    }
    L.footer(pres, s, n, "Prototype code and results are in the data room and can be run in one command.");
  }

  // 11 ── Team
  {
    const s = pres.addSlide(); n++;
    L.header(pres, s, { tag: "TEAM", title: "People who write machine-checked rulebooks, and have shipped at scale", sub: "Formal methods, applied AI, robot perception and 3D capture" });
    L.card(pres, s, M, 1.95, 6.2, 4.55, { fill: C.ink, title: "Founder & CEO", titleColor: C.white, titleSize: 15 });
    L.bullets(pres, s, M + 0.22, 2.5, 5.8, 3.9, [
      { text: "Core contributor to ISO/IEC 21838-4, the TUpper top-level ontology; member of the Industrial Ontologies Foundry; University of Toronto AI doctorate and researcher", options: { color: C.white } },
      { text: "Consistency proofs and model construction for first-order axiom systems; 21 papers, invited AAAI talk, one English-language monograph", options: { color: C.white } },
      { text: "Founding team of a cross-border DTC company backed by Accel and others: >$50M revenue in year one, 100+ people", options: { color: C.white } },
      { text: "Founded a spatial-computing company with one of the first AR apps on Apple Vision Pro; 13 granted patents", options: { color: C.white } },
    ], { size: 10.5, paraSpace: 10 });
    const team = [
      ["CTO & Chief Scientist", "McMaster University AI doctorate; former AI scientist at a top-tier tech company and startup chief scientist"],
      ["Perception & Robotics Lead", "Harbin Institute of Technology doctorate in mechatronics; former director of the perception center at XPeng"],
      ["3D Capture & Simulation Lead", "10+ years as art director in games and stage production; led a city-scale VR reconstruction"],
    ];
    team.forEach((t, i) => L.card(pres, s, 7.1, 1.95 + i * 1.17, 5.6, 1.05, { fill: C.panel, title: t[0], titleSize: 11.5, body: t[1], bodySize: 9.5 }));
    L.card(pres, s, 7.1, 5.5, 5.6, 1.0, { fill: C.crimsonSoft, title: "Hiring now", titleColor: C.crimson, titleSize: 11.5, body: "A robot-learning lead who has trained VLA policies at scale, and a U.S. founding GTM lead for data vendors.", bodySize: 9.5 });
    L.footer(pres, s, n);
  }

  // 12 ── Vision + next steps
  {
    const s = pres.addSlide(); n++;
    L.darkBg(pres, s);
    L.label(pres, s, "AXIOMALITY", M, 0.55, 4, 0.35, { size: 13, bold: true, color: C.white, extra: { charSpacing: 4 } });
    L.label(pres, s, "Every robot dataset that changes hands\nships with a passport.", M, 1.4, 11.5, 1.6, { head: true, size: 32, bold: true, color: C.white, ls: 1.15 });
    const path4 = ["Vendors ship with passports", "Labs accept them at intake", "Synthetic suppliers certify every generated episode", "OEMs reuse them as compliance evidence"];
    path4.forEach((t, i) => {
      const x = M + i * 3.05;
      L.stepChip(pres, s, x, 3.35, i + 1, { d: 0.42 });
      L.label(pres, s, t, x + 0.55, 3.3, 2.4, 0.6, { size: 11.5, color: C.white, valign: "middle" });
    });
    const asks = [
      ["Handshake", "Two intros", "One robot-data vendor and one lab procurement lead, for a blind bake-off on their own batch"],
      ["FileCheck", "12 minutes", "Corrupt any of our episodes yourself; watch the verdict, then the passport, change"],
      ["CalendarCheck", "December 31", "Check the three commitments on slide 11, one by one"],
    ];
    for (let i = 0; i < 3; i++) {
      const x = M + i * 4.1;
      s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y: 4.45, w: 3.9, h: 1.85, fill: { color: C.ink2 }, line: { color: C.ink2 }, rectRadius: 0.08 });
      await L.icon(s, asks[i][0], x + 0.22, 4.65, 0.4, { bg: C.crimson });
      L.label(pres, s, asks[i][1], x + 0.75, 4.68, 3.0, 0.35, { head: true, size: 14, bold: true, color: C.white });
      L.label(pres, s, asks[i][2], x + 0.22, 5.2, 3.5, 1.0, { size: 10.5, color: "D9DCE8" });
    }
    L.label(pres, s, "© 2026 AXIOMALITY · Confidential", W - M - 3.5, H - 0.42, 3.5, 0.3, { size: 9, color: "9AA0B4", align: "right" });
  }

  fs.mkdirSync(path.dirname(OUT), { recursive: true });
  await pres.writeFile({ fileName: OUT });
  console.log("wrote", OUT, "slides:", n);
})().catch((e) => { console.error(e); process.exit(1); });
