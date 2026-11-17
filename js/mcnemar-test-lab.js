/* Easy Statistics Academy Batch #94: McNemar test for paired binary data.
 *
 * Paired 2x2 table (rows = first measurement, columns = second):
 *   a = (+,+)  b = (+,-)
 *   c = (-,+)  d = (-,-)
 * Only the discordant pairs b and c carry information about a change in the
 * marginal proportion. Under H0 (P(+ first) = P(+ second)), conditional on
 * n_d = b + c, b ~ Binomial(n_d, 1/2).
 *  - asymptotic: chi2 = (b - c)^2 / (b + c), df = 1, p = Q(1/2, chi2/2);
 *  - continuity-corrected (Edwards): chi2 = max(|b - c| - 1, 0)^2 / (b + c);
 *  - exact two-sided: p = min(1, 2 P(X <= min(b, c))), X ~ Bin(b + c, 1/2).
 */
(function () {
  "use strict";
  const LIMIT = 10000000;
  const lanczos = [0.99999999999980993, 676.5203681218851, -1259.1392167224028,
    771.32342877765313, -176.61502916214059, 12.507343278686905,
    -0.13857109526572012, 9.984369578019572e-6, 1.5056327351493116e-7];
  function logGamma(z) {
    if (!(z > 0) || !Number.isFinite(z)) return NaN;
    if (z < 0.5) return Math.log(Math.PI) - Math.log(Math.sin(Math.PI * z)) - logGamma(1 - z);
    z -= 1;
    let s = lanczos[0];
    for (let i = 1; i < lanczos.length; i++) s += lanczos[i] / (z + i);
    const t = z + 7.5;
    return 0.5 * Math.log(2 * Math.PI) + (z + 0.5) * Math.log(t) - t + Math.log(s);
  }
  function gammaQ(a, x) {
    if (!(a > 0) || Number.isNaN(x) || x < 0) return NaN;
    if (x === 0) return 1;
    if (x === Infinity) return 0;
    const factor = Math.exp(-x + a * Math.log(x) - logGamma(a)), eps = 2e-15, tiny = 1e-300;
    if (x < a + 1) {
      let ap = a, sum = 1 / a, del = sum;
      for (let n = 1; n <= 1000; n++) { ap += 1; del *= x / ap; sum += del; if (Math.abs(del) <= Math.abs(sum) * eps) break; }
      return Math.min(1, Math.max(0, 1 - sum * factor));
    }
    let b = x + 1 - a, c = 1 / tiny, d = 1 / b, h = d;
    for (let i = 1; i <= 1000; i++) {
      const an = -i * (i - a); b += 2;
      d = an * d + b; if (Math.abs(d) < tiny) d = tiny;
      c = b + an / c; if (Math.abs(c) < tiny) c = tiny;
      d = 1 / d; const delta = d * c; h *= delta;
      if (Math.abs(delta - 1) <= eps) break;
    }
    return Math.min(1, Math.max(0, factor * h));
  }
  // P(X <= m) for X ~ Bin(n, 1/2), summed downward from k = m in log space.
  function binomHalfCdf(m, n) {
    if (m >= n) return 1;
    if (m < 0) return 0;
    const logTerm = logGamma(n + 1) - logGamma(m + 1) - logGamma(n - m + 1) - n * Math.LN2;
    let term = 1, sum = 1;
    for (let k = m; k > 0; k--) {
      term *= k / (n - k + 1);
      sum += term;
      if (term < sum * 1e-17) break;
    }
    return Math.min(1, Math.exp(logTerm + Math.log(sum)));
  }
  function compute(values) {
    if (!Array.isArray(values) || values.length !== 4 ||
        values.some(v => typeof v !== "number" || !Number.isSafeInteger(v) || v < 0 || v > LIMIT)) {
      return { error: "range" };
    }
    const [a, b, c, d] = values, n = a + b + c + d, nd = b + c;
    if (n === 0) return { error: "empty" };
    const out = { a, b, c, d, n, nd,
      pFirst: (a + b) / n, pSecond: (a + c) / n, diff: (a + b - (a + c)) / n };
    if (nd === 0) {
      return Object.assign(out, { chi: NaN, p: NaN, chiCC: NaN, pCC: NaN, pExact: 1, noDiscordant: true });
    }
    const chi = (b - c) ** 2 / nd;
    const chiCC = Math.max(Math.abs(b - c) - 1, 0) ** 2 / nd;
    return Object.assign(out, {
      chi, p: chi === 0 ? 1 : gammaQ(0.5, chi / 2),
      chiCC, pCC: chiCC === 0 ? 1 : gammaQ(0.5, chiCC / 2),
      pExact: Math.min(1, 2 * binomHalfCdf(Math.min(b, c), nd)),
      small: nd < 25, noDiscordant: false
    });
  }
  const api = { compute, binomHalfCdf, gammaQ };
  if (typeof window !== "undefined") window.esaMcNemar = api;

  const root = typeof document !== "undefined" && document.getElementById ?
    document.getElementById("esa-mcnemar-lab") : null;
  if (!root) return;
  const find = id => root.querySelector("#esa-mcn-" + id);
  const ids = ["a", "b", "c", "d"], inputs = ids.map(find);
  const outputs = ["n", "nd", "p1", "p2", "diff", "chi", "p", "chicc", "pcc", "exact"];
  const fmtP = p => !Number.isFinite(p) ? "Undefined" : p < 1e-12 ? "< 1e-12" : p < 0.0001 ? p.toExponential(3) : p.toFixed(6);
  const fmt = x => Number.isFinite(x) ? x.toFixed(6) : "Undefined";
  function fail(message) {
    find("error").hidden = false;
    find("error").textContent = message;
    inputs.forEach(input => input.setAttribute("aria-invalid", "true"));
    outputs.forEach(id => find(id).textContent = "—");
    find("advice").textContent = "Correct the inputs to see which p-value is appropriate.";
  }
  function update() {
    const values = inputs.map(input => input.value.trim() === "" ? NaN : Number(input.value));
    const r = compute(values);
    if (r.error === "range") { fail("Enter a whole-number count from 0 to 10,000,000 in every cell."); return; }
    if (r.error === "empty") { fail("At least one pair is needed: all four counts are zero."); return; }
    find("error").hidden = true; find("error").textContent = "";
    inputs.forEach(input => input.setAttribute("aria-invalid", "false"));
    find("n").textContent = String(r.n);
    find("nd").textContent = String(r.nd);
    find("p1").textContent = r.pFirst.toFixed(4);
    find("p2").textContent = r.pSecond.toFixed(4);
    find("diff").textContent = (r.diff > 0 ? "+" : "") + r.diff.toFixed(4);
    find("chi").textContent = fmt(r.chi);
    find("p").textContent = fmtP(r.p);
    find("chicc").textContent = fmt(r.chiCC);
    find("pcc").textContent = fmtP(r.pCC);
    find("exact").textContent = fmtP(r.pExact);
    find("advice").textContent = r.noDiscordant ?
      "There are no discordant pairs (b + c = 0): the chi-square statistic is undefined, the exact p-value is 1, and the data contain no evidence of change." :
      r.small ? "Only " + r.nd + " discordant pairs (b + c < 25, a common rule of thumb): report the exact binomial p-value." :
      "With " + r.nd + " discordant pairs the chi-square approximation is usually adequate; the exact p-value remains valid and can always be reported.";
  }
  inputs.forEach(input => input.addEventListener("input", update));
  const presets = { example: [45, 5, 20, 30], small: [12, 1, 6, 9], none: [40, 0, 0, 60] };
  for (const [name, vals] of Object.entries(presets)) {
    const button = find(name);
    if (button) button.addEventListener("click", () => { vals.forEach((v, i) => inputs[i].value = String(v)); update(); });
  }
  update();
})();
