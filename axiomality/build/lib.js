// Shared design system for the AXIOMALITY decks (pptxgenjs)
// Palette: "Evidence ink" — ink navy dominant, crimson accent taken from the
// company's own point-cloud renders, teal for "verified / pass" states.
const pptxgen = require("pptxgenjs");
const React = require("react");
const ReactDOMServer = require("react-dom/server");
const sharp = require("sharp");
const Lu = require("react-icons/lu");
const Fa = require("react-icons/fa6");

const C = {
  ink: "151A2D",      // dominant dark
  ink2: "232A44",     // dark panel
  paper: "FFFFFF",
  panel: "F3F4F8",    // light panel tint
  panel2: "E9EBF2",
  text: "1B1F2A",
  muted: "6B7280",
  line: "D5D8E0",
  crimson: "C8123F",  // accent
  crimsonSoft: "FBE7EC",
  teal: "0F8B8D",     // verified / pass
  tealSoft: "E1F3F3",
  amber: "D98E04",
  amberSoft: "FCF1DA",
  white: "FFFFFF",
};

const W = 13.333, H = 7.5;
const M = 0.6; // side margin

function fonts(lang) {
  return lang === "zh"
    ? { head: "Microsoft YaHei", body: "Microsoft YaHei", mono: "Courier New" }
    : { head: "Cambria", body: "Calibri", mono: "Courier New" };
}

function newDeck(lang, meta) {
  const pres = new pptxgen();
  pres.layout = "LAYOUT_WIDE";
  pres.author = "AXIOMALITY";
  pres.company = "AXIOMALITY";
  pres.title = meta.title;
  pres.subject = meta.subject || "";
  pres._lang = lang;
  pres._F = fonts(lang);
  pres._total = meta.total || 0;
  pres._footer = meta.footer || "AXIOMALITY";
  return pres;
}

// ---------- icons ----------
const iconCache = {};
async function iconPng(name, color, bg, size = 256) {
  const key = `${name}-${color}-${bg}-${size}`;
  if (iconCache[key]) return iconCache[key];
  const Comp = Lu["Lu" + name] || Fa["Fa" + name] || Lu[name] || Fa[name];
  if (!Comp) throw new Error("icon not found: " + name);
  const inner = ReactDOMServer.renderToStaticMarkup(
    React.createElement(Comp, { color: "#" + color, size: Math.round(size * 0.5) })
  );
  const off = Math.round(size * 0.25);
  const svg = `<svg xmlns="http://www.w3.org/2000/svg" width="${size}" height="${size}" viewBox="0 0 ${size} ${size}">` +
    (bg ? `<circle cx="${size / 2}" cy="${size / 2}" r="${size / 2}" fill="#${bg}"/>` : "") +
    `<g transform="translate(${off},${off})">${inner}</g></svg>`;
  const buf = await sharp(Buffer.from(svg)).png().toBuffer();
  const data = "image/png;base64," + buf.toString("base64");
  iconCache[key] = data;
  return data;
}

async function icon(slide, name, x, y, d, opts = {}) {
  const data = await iconPng(name, opts.color || C.white, opts.bg === null ? null : (opts.bg || C.crimson));
  slide.addImage({ data, x, y, w: d, h: d });
}

// ---------- chrome ----------
function header(pres, slide, opts) {
  const F = pres._F;
  const { tag, title, sub } = opts;
  if (tag) {
    slide.addText(tag, {
      x: M, y: 0.32, w: 8, h: 0.3, fontFace: F.body, fontSize: 10.5, bold: true,
      color: C.crimson, charSpacing: 2, isTextBox: true, margin: 0,
    });
  }
  // approximate visual length: CJK chars count double
  const vlen = [...title].reduce((a, ch) => a + (/[　-鿿＀-￯]/.test(ch) ? 2 : 1), 0);
  let ts = opts.titleSize || 28;
  if (!opts.titleSize) {
    if (pres._lang === "zh") { if (vlen > 76) ts = 21; else if (vlen > 58) ts = 24; }
    else { if (vlen > 95) ts = 20; else if (vlen > 60) ts = 22; else ts = 26; }
  }
  // two-line-safe title box
  slide.addText(title, {
    x: M, y: 0.58, w: W - 2 * M, h: 0.9, fontFace: F.head, fontSize: ts, bold: true,
    color: C.text, isTextBox: true, margin: 0, valign: "middle", lineSpacingMultiple: 1.0,
  });
  if (sub) {
    slide.addText(sub, {
      x: M, y: 1.5, w: W - 2 * M, h: 0.42, fontFace: F.body, fontSize: 12.5,
      color: C.muted, isTextBox: true, margin: 0, valign: "top",
    });
  }
}

function footer(pres, slide, n, note) {
  const F = pres._F;
  slide.addText(pres._footer, {
    x: M, y: H - 0.45, w: 6, h: 0.3, fontFace: F.body, fontSize: 8.5, color: C.muted,
    isTextBox: true, margin: 0,
  });
  if (note) {
    slide.addText(note, {
      x: M, y: H - 0.72, w: W - 2 * M - 1, h: 0.28, fontFace: F.body, fontSize: 8, color: C.muted,
      isTextBox: true, margin: 0, valign: "bottom",
    });
  }
  slide.addText(String(n), {
    x: W - M - 0.6, y: H - 0.45, w: 0.6, h: 0.3, fontFace: F.body, fontSize: 8.5, color: C.muted,
    align: "right", isTextBox: true, margin: 0,
  });
}

// ---------- building blocks ----------
function stat(pres, slide, x, y, w, h, big, label, opts = {}) {
  const F = pres._F;
  const dark = opts.dark;
  slide.addText(big, {
    x, y, w, h: h * 0.6, fontFace: F.head, fontSize: opts.size || 40, bold: true,
    color: opts.color || (dark ? C.white : C.crimson), isTextBox: true, margin: 0, valign: "bottom",
  });
  slide.addText(label, {
    x, y: y + h * 0.6, w, h: h * 0.4, fontFace: F.body, fontSize: opts.labelSize || 11.5,
    color: dark ? "C9CDDB" : C.muted, isTextBox: true, margin: 0, valign: "top",
  });
}

function card(pres, slide, x, y, w, h, opts = {}) {
  const F = pres._F;
  slide.addShape(pres.shapes.ROUNDED_RECTANGLE, {
    x, y, w, h, fill: { color: opts.fill || C.panel }, line: { color: opts.lineColor || (opts.fill || C.panel), width: 0.5 },
    rectRadius: 0.08,
    shadow: opts.shadow ? { type: "outer", blur: 6, offset: 2, angle: 90, color: "000000", opacity: 0.12 } : undefined,
  });
  let ty = y + 0.18;
  if (opts.title) {
    slide.addText(opts.title, {
      x: x + 0.22 + (opts.titleIndent || 0), y: ty, w: w - 0.44 - (opts.titleIndent || 0), h: opts.titleH || 0.36,
      fontFace: F.head, fontSize: opts.titleSize || 14, bold: true,
      color: opts.titleColor || C.text, isTextBox: true, margin: 0, valign: "top",
    });
    ty += (opts.titleH || 0.36) + 0.04;
  }
  if (opts.body) {
    slide.addText(opts.body, {
      x: x + 0.22, y: ty, w: w - 0.44, h: y + h - ty - 0.14, fontFace: F.body,
      fontSize: opts.bodySize || 11.5, color: opts.bodyColor || C.text, isTextBox: true, margin: 0,
      valign: "top", paraSpaceAfter: opts.paraSpace == null ? 4 : opts.paraSpace, lineSpacingMultiple: 1.08,
    });
  }
}

// bracket corners (point-cloud bounding-box motif)
function brackets(pres, slide, x, y, w, h, color = C.crimson, len = 0.18, width = 1.5) {
  const L = (x1, y1, x2, y2) => slide.addShape(pres.shapes.LINE, { x: Math.min(x1, x2), y: Math.min(y1, y2), w: Math.abs(x2 - x1), h: Math.abs(y2 - y1), line: { color, width } });
  L(x, y, x + len, y); L(x, y, x, y + len);
  L(x + w - len, y, x + w, y); L(x + w, y, x + w, y + len);
  L(x, y + h - len, x, y + h); L(x, y + h, x + len, y + h);
  L(x + w - len, y + h, x + w, y + h); L(x + w, y + h - len, x + w, y + h);
}

function bullets(pres, slide, x, y, w, h, items, opts = {}) {
  const F = pres._F;
  const arr = items.map((t, i) => {
    if (typeof t === "string") return { text: t, options: { bullet: { indent: 14 }, breakLine: i < items.length - 1, paraSpaceAfter: opts.paraSpace == null ? 6 : opts.paraSpace } };
    return { text: t.text, options: Object.assign({ bullet: { indent: 14 }, breakLine: i < items.length - 1, paraSpaceAfter: opts.paraSpace == null ? 6 : opts.paraSpace }, t.options || {}) };
  });
  slide.addText(arr, {
    x, y, w, h, fontFace: F.body, fontSize: opts.size || 12, color: opts.color || C.text,
    isTextBox: true, margin: 0, valign: opts.valign || "top", lineSpacingMultiple: 1.1,
  });
}

function table(pres, slide, rows, x, y, w, opts = {}) {
  const F = pres._F;
  const head = rows[0];
  const body = rows.slice(1);
  const trs = [];
  trs.push(head.map((c) => ({ text: c, options: { bold: true, color: C.white, fill: { color: opts.headFill || C.ink }, fontSize: opts.headSize || (opts.size || 10.5), fontFace: F.body, valign: "middle" } })));
  body.forEach((r, ri) => {
    trs.push(r.map((c, ci) => {
      const isObj = typeof c === "object" && c !== null;
      const text = isObj ? c.text : c;
      const o = {
        fontSize: opts.size || 10.5, fontFace: F.body, color: C.text, valign: "middle",
        fill: { color: ri % 2 === 0 ? C.white : C.panel },
        bold: ci === 0 && opts.boldFirst,
      };
      if (isObj && c.options) Object.assign(o, c.options);
      return { text, options: o };
    }));
  });
  slide.addTable(trs, {
    x, y, w, colW: opts.colW, rowH: opts.rowH || 0.32, border: { type: "solid", color: C.line, pt: 0.5 },
    margin: opts.margin || [0.04, 0.08, 0.04, 0.08], autoPage: false,
  });
}

// numbered step chip
function stepChip(pres, slide, x, y, n, opts = {}) {
  const F = pres._F;
  const d = opts.d || 0.42;
  slide.addShape(pres.shapes.OVAL, { x, y, w: d, h: d, fill: { color: opts.fill || C.crimson }, line: { color: opts.fill || C.crimson } });
  slide.addText(String(n), { x, y, w: d, h: d, fontFace: F.head, fontSize: opts.size || 13, bold: true, color: C.white, align: "center", valign: "middle", isTextBox: true, margin: 0 });
}

function arrow(pres, slide, x, y, w, opts = {}) {
  slide.addShape(pres.shapes.LINE, { x, y, w, h: 0, line: { color: opts.color || C.muted, width: 1.25, endArrowType: "triangle" } });
}

function label(pres, slide, text, x, y, w, h, opts = {}) {
  const F = pres._F;
  slide.addText(text, Object.assign({
    x, y, w, h, fontFace: opts.head ? F.head : F.body, fontSize: opts.size || 12, color: opts.color || C.text,
    bold: !!opts.bold, italic: !!opts.italic, align: opts.align || "left", valign: opts.valign || "top",
    isTextBox: true, margin: 0, paraSpaceAfter: opts.paraSpace == null ? 3 : opts.paraSpace, lineSpacingMultiple: opts.ls || 1.08,
  }, opts.extra || {}));
}

function pill(pres, slide, text, x, y, w, h, opts = {}) {
  const F = pres._F;
  slide.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y, w, h, fill: { color: opts.fill || C.crimsonSoft }, line: { color: opts.fill || C.crimsonSoft }, rectRadius: 0.5 });
  slide.addText(text, { x, y, w, h, fontFace: F.body, fontSize: opts.size || 10, bold: true, color: opts.color || C.crimson, align: "center", valign: "middle", isTextBox: true, margin: 0 });
}

function darkBg(pres, slide) {
  slide.background = { color: C.ink };
}

module.exports = { pptxgen, C, W, H, M, newDeck, icon, iconPng, header, footer, stat, card, brackets, bullets, table, stepChip, arrow, label, pill, darkBg };
