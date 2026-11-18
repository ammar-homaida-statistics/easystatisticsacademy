/* Easy Statistics Academy Batch #95: Cohen's kappa for two raters.
 *
 * k x k agreement table n_ij (rows = rater A, columns = rater B), N = sum n_ij,
 * p_ij = n_ij / N, row margins r_i, column margins c_j.
 *   p_o = sum_i p_ii,  p_e = sum_i r_i c_i,  kappa = (p_o - p_e) / (1 - p_e).
 *   kappa_max (given the observed margins) = (sum_i min(r_i, c_i) - p_e) / (1 - p_e).
 * Large-sample standard error (Fleiss, Cohen & Everitt, 1969):
 *   Var = [A + B - C] / (N (1 - p_e)^2),
 *   A = sum_i p_ii [1 - (r_i + c_i)(1 - kappa)]^2,
 *   B = (1 - kappa)^2 sum_{i != j} p_ij (c_i + r_j)^2,
 *   C = [kappa - p_e (1 - kappa)]^2.
 * The Wald interval kappa +/- z * SE is truncated to [-1, 1] for display and
 * is unreliable for small N or kappa near +/-1.
 *
 * Batch #96, weighted kappa for ordered categories. Agreement weights
 *   linear:    w_ij = 1 - |i - j| / (k - 1)
 *   quadratic: w_ij = 1 - ((i - j) / (k - 1))^2
 *   p_o(w) = sum_ij w_ij p_ij,  p_e(w) = sum_ij w_ij r_i c_j,
 *   kappa_w = (p_o(w) - p_e(w)) / (1 - p_e(w)).
 * Large-sample variance (Fleiss, Cohen & Everitt, 1969), with
 *   wr_i = sum_j c_j w_ij and wc_j = sum_i r_i w_ij:
 *   Var = [sum_ij p_ij (w_ij - (wr_i + wc_j)(1 - kappa_w))^2
 *          - (kappa_w - p_e(w)(1 - kappa_w))^2] / (N (1 - p_e(w))^2).
 * With identity weights this reduces exactly to A + B - C above. For k = 2,
 * linear and quadratic weights both equal the identity, so kappa_w = kappa.
 */
(function () {
  "use strict";
  const LIMIT = 10000000;
  const WEIGHTS = { none: true, linear: true, quadratic: true };
  function weightMatrix(k, scheme) {
    return Array.from({ length: k }, (_, i) => Array.from({ length: k }, (_, j) => {
      if (scheme === "linear") return 1 - Math.abs(i - j) / (k - 1);
      if (scheme === "quadratic") return 1 - ((i - j) / (k - 1)) ** 2;
      return i === j ? 1 : 0;
    }));
  }
  function compute(table, scheme) {
    if (scheme === undefined) scheme = "none";
    if (typeof scheme !== "string" || !Object.prototype.hasOwnProperty.call(WEIGHTS, scheme)) return { error: "weights" };
    if (!Array.isArray(table) || table.length < 2 || table.length > 5) return { error: "shape" };
    const k = table.length;
    if (table.some(row => !Array.isArray(row) || row.length !== k)) return { error: "shape" };
    if (table.some(row => row.some(v => typeof v !== "number" || !Number.isSafeInteger(v) || v < 0 || v > LIMIT))) {
      return { error: "range" };
    }
    const N = table.flat().reduce((s, v) => s + v, 0);
    if (N === 0) return { error: "empty" };
    const p = table.map(row => row.map(v => v / N));
    const r = p.map(row => row.reduce((s, v) => s + v, 0));
    const c = p[0].map((_, j) => p.reduce((s, row) => s + row[j], 0));
    let po = 0, pe = 0, poMax = 0;
    for (let i = 0; i < k; i++) { po += p[i][i]; pe += r[i] * c[i]; poMax += Math.min(r[i], c[i]); }
    if (scheme !== "none") return weighted(k, N, p, r, c, scheme);
    const out = { k, N, po, pe, rowMargins: r, colMargins: c, weights: "none" };
    if (1 - pe < 1e-12) return Object.assign(out, { degenerate: true, kappa: NaN, kappaMax: NaN, se: NaN, lower: NaN, upper: NaN });
    const kappa = (po - pe) / (1 - pe);
    const kappaMax = (poMax - pe) / (1 - pe);
    let A = 0, B = 0;
    for (let i = 0; i < k; i++) {
      A += p[i][i] * (1 - (r[i] + c[i]) * (1 - kappa)) ** 2;
      for (let j = 0; j < k; j++) if (i !== j) B += p[i][j] * (c[i] + r[j]) ** 2;
    }
    B *= (1 - kappa) ** 2;
    const C = (kappa - pe * (1 - kappa)) ** 2;
    const variance = Math.max(0, (A + B - C) / (N * (1 - pe) ** 2));
    const se = Math.sqrt(variance);
    return Object.assign(out, { degenerate: false, kappa, kappaMax, se,
      lower: Math.max(-1, kappa - 1.959963984540054 * se),
      upper: Math.min(1, kappa + 1.959963984540054 * se) });
  }
  function weighted(k, N, p, r, c, scheme) {
    const w = weightMatrix(k, scheme);
    let po = 0, pe = 0;
    for (let i = 0; i < k; i++) for (let j = 0; j < k; j++) { po += w[i][j] * p[i][j]; pe += w[i][j] * r[i] * c[j]; }
    // kappa_max is defined here only for unweighted kappa; it is not reported.
    const out = { k, N, po, pe, rowMargins: r, colMargins: c, weights: scheme, kappaMax: NaN };
    if (1 - pe < 1e-12) return Object.assign(out, { degenerate: true, kappa: NaN, se: NaN, lower: NaN, upper: NaN });
    const kappa = (po - pe) / (1 - pe);
    const wr = w.map(row => row.reduce((s, v, j) => s + v * c[j], 0));
    const wc = w[0].map((_, j) => w.reduce((s, row, i) => s + row[j] * r[i], 0));
    let A = 0;
    for (let i = 0; i < k; i++) for (let j = 0; j < k; j++) A += p[i][j] * (w[i][j] - (wr[i] + wc[j]) * (1 - kappa)) ** 2;
    const C = (kappa - pe * (1 - kappa)) ** 2;
    const se = Math.sqrt(Math.max(0, (A - C) / (N * (1 - pe) ** 2)));
    return Object.assign(out, { degenerate: false, kappa, se,
      lower: Math.max(-1, kappa - 1.959963984540054 * se),
      upper: Math.min(1, kappa + 1.959963984540054 * se) });
  }
  const api = { compute, weightMatrix };
  if (typeof window !== "undefined") window.esaCohensKappa = api;

  const root = typeof document !== "undefined" && document.getElementById ?
    document.getElementById("esa-kappa-lab") : null;
  if (!root) return;
  const ar = root.dataset.locale === "ar";
  const T = ar ? {
    error: "أدخل جدولًا مربعًا من 2–5 فئات: كل سطر فئة المُقيّم A، والأعداد صحيحة غير سالبة (حتى 10,000,000) مفصولة بفواصل إنجليزية.",
    empty: "الجدول فارغ: يجب أن تكون هناك حالة واحدة على الأقل.",
    degenerate: "الاتفاق المتوقع بالصدفة يساوي 1 (المقيّمان يستخدمان الفئة نفسها دائمًا)، لذا فإن كابا غير معرّفة.",
    undef: "غير معرّف",
    na: "لا ينطبق على كابا الموزونة",
    twoCat: "مع فئتين فقط تتطابق الأوزان الخطية والتربيعية مع كابا غير الموزونة.",
    weightedNote: "كابا الموزونة تمنح اتفاقًا جزئيًا للاختلافات القريبة؛ فلا تستخدمها إلا إذا كانت الفئات مرتّبة بالترتيب المُدخل.",
    paradox: "الاتفاق المشاهد مرتفع لكن كابا منخفضة: عندما تهيمن فئة واحدة يرتفع الاتفاق المتوقع بالصدفة. قارن مع أقصى كابا ممكنة."
  } : {
    error: "Enter a square table with 2–5 categories: each line is rater A's category, with nonnegative whole-number counts (up to 10,000,000) separated by commas.",
    empty: "The table is empty: at least one rated case is needed.",
    degenerate: "Chance agreement equals 1 (both raters always use the same single category), so kappa is undefined.",
    undef: "Undefined",
    na: "Not defined for weighted kappa",
    twoCat: "With only two categories, linear and quadratic weights coincide with unweighted kappa.",
    weightedNote: "Weighted kappa gives partial credit to near misses; use it only when the categories are ordered as entered.",
    paradox: "Observed agreement is high but kappa is low: when one category dominates, chance agreement is also high. Compare with the maximum attainable kappa."
  };
  const find = id => root.querySelector("#esa-kappa-" + id);
  const input = find("input");
  const scheme = find("weights");
  const outs = ["n", "po", "pe", "kappa", "kmax", "se", "ci"];
  const fmt = x => Number.isFinite(x) ? x.toFixed(4) : T.undef;
  function parse(text) {
    const rows = text.trim().split(/\n+/).map(line => line.trim()).filter(Boolean);
    return rows.map(line => line.split(",").map(s => s.trim() === "" ? NaN : Number(s.trim())));
  }
  function fail(message) {
    find("error").hidden = false;
    find("error").textContent = message;
    input.setAttribute("aria-invalid", "true");
    outs.forEach(id => find(id).textContent = "—");
    find("note").textContent = "";
  }
  function update() {
    const r = compute(parse(input.value), scheme ? scheme.value : "none");
    if (r.error) { fail(r.error === "empty" ? T.empty : T.error); return; }
    find("error").hidden = true; find("error").textContent = "";
    input.setAttribute("aria-invalid", "false");
    find("n").textContent = String(r.N);
    find("po").textContent = fmt(r.po);
    find("pe").textContent = fmt(r.pe);
    find("kappa").textContent = fmt(r.kappa);
    find("kmax").textContent = r.weights === "none" ? fmt(r.kappaMax) : T.na;
    find("se").textContent = fmt(r.se);
    find("ci").textContent = Number.isFinite(r.lower) ? "[" + r.lower.toFixed(4) + ", " + r.upper.toFixed(4) + "]" : T.undef;
    find("note").textContent = r.degenerate ? T.degenerate :
      r.weights !== "none" ? (r.k === 2 ? T.twoCat : T.weightedNote) :
      (r.po >= 0.85 && r.kappa < 0.5 ? T.paradox : "");
  }
  input.addEventListener("input", update);
  if (scheme) scheme.addEventListener("change", update);
  const presets = { example: "20, 5\n10, 15", paradox: "85, 5\n5, 5", three: "22, 3, 1\n4, 18, 2\n0, 3, 17" };
  for (const [name, value] of Object.entries(presets)) {
    const button = find(name);
    if (button) button.addEventListener("click", () => { input.value = value; update(); });
  }
  update();
})();
