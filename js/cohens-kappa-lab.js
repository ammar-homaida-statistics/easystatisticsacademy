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
 */
(function () {
  "use strict";
  const LIMIT = 10000000;
  function compute(table) {
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
    const out = { k, N, po, pe, rowMargins: r, colMargins: c };
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
  const api = { compute };
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
    paradox: "الاتفاق المشاهد مرتفع لكن كابا منخفضة: عندما تهيمن فئة واحدة يرتفع الاتفاق المتوقع بالصدفة. قارن مع أقصى كابا ممكنة."
  } : {
    error: "Enter a square table with 2–5 categories: each line is rater A's category, with nonnegative whole-number counts (up to 10,000,000) separated by commas.",
    empty: "The table is empty: at least one rated case is needed.",
    degenerate: "Chance agreement equals 1 (both raters always use the same single category), so kappa is undefined.",
    undef: "Undefined",
    paradox: "Observed agreement is high but kappa is low: when one category dominates, chance agreement is also high. Compare with the maximum attainable kappa."
  };
  const find = id => root.querySelector("#esa-kappa-" + id);
  const input = find("input");
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
    const r = compute(parse(input.value));
    if (r.error) { fail(r.error === "empty" ? T.empty : T.error); return; }
    find("error").hidden = true; find("error").textContent = "";
    input.setAttribute("aria-invalid", "false");
    find("n").textContent = String(r.N);
    find("po").textContent = fmt(r.po);
    find("pe").textContent = fmt(r.pe);
    find("kappa").textContent = fmt(r.kappa);
    find("kmax").textContent = fmt(r.kappaMax);
    find("se").textContent = fmt(r.se);
    find("ci").textContent = Number.isFinite(r.lower) ? "[" + r.lower.toFixed(4) + ", " + r.upper.toFixed(4) + "]" : T.undef;
    find("note").textContent = r.degenerate ? T.degenerate :
      (r.po >= 0.85 && r.kappa < 0.5 ? T.paradox : "");
  }
  input.addEventListener("input", update);
  const presets = { example: "20, 5\n10, 15", paradox: "85, 5\n5, 5", three: "22, 3, 1\n4, 18, 2\n0, 3, 17" };
  for (const [name, value] of Object.entries(presets)) {
    const button = find(name);
    if (button) button.addEventListener("click", () => { input.value = value; update(); });
  }
  update();
})();
