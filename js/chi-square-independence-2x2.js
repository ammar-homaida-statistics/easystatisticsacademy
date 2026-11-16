/* Easy Statistics Academy Batch #93: shared 2 x 2 Pearson chi-square
 * independence engine for the English and Arabic lessons.
 *
 * Pearson asymptotic test WITHOUT continuity correction. Expected counts
 * E_ij = R_i C_j / N; chi-square = sum (O-E)^2/E with df = 1; the upper-tail
 * p-value is Q(1/2, chi/2) = erfc(sqrt(chi/2)), evaluated with the regularized
 * incomplete gamma function so that small tail probabilities keep their
 * relative accuracy. Cramer's V for a 2 x 2 table is sqrt(chi/N).
 * Only strings are localized; the mathematics is shared.
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
    let a = lanczos[0];
    for (let i = 1; i < lanczos.length; i++) a += lanczos[i] / (z + i);
    const t = z + 7.5;
    return 0.5 * Math.log(2 * Math.PI) + (z + 0.5) * Math.log(t) - t + Math.log(a);
  }
  // Regularized upper incomplete gamma Q(a,x): series for x<a+1,
  // Lentz continued fraction otherwise (Numerical Recipes, section 6.2).
  function gammaQ(a, x) {
    if (!(a > 0) || !Number.isFinite(a) || Number.isNaN(x) || x < 0) return NaN;
    if (x === 0) return 1;
    if (x === Infinity) return 0;
    const factor = Math.exp(-x + a * Math.log(x) - logGamma(a));
    const eps = 2e-15, tiny = 1e-300;
    if (x < a + 1) {
      let ap = a, sum = 1 / a, del = sum;
      for (let n = 1; n <= 1000; n++) {
        ap += 1; del *= x / ap; sum += del;
        if (Math.abs(del) <= Math.abs(sum) * eps) break;
      }
      return Math.min(1, Math.max(0, 1 - sum * factor));
    }
    let b = x + 1 - a, c = 1 / tiny, d = 1 / b, h = d;
    for (let i = 1; i <= 1000; i++) {
      const an = -i * (i - a);
      b += 2;
      d = an * d + b; if (Math.abs(d) < tiny) d = tiny;
      c = b + an / c; if (Math.abs(c) < tiny) c = tiny;
      d = 1 / d;
      const delta = d * c;
      h *= delta;
      if (Math.abs(delta - 1) <= eps) break;
    }
    return Math.min(1, Math.max(0, factor * h));
  }
  function compute(values) {
    if (!Array.isArray(values) || values.length !== 4 ||
        values.some(n => typeof n !== "number" || !Number.isSafeInteger(n) || n < 0 || n > LIMIT)) {
      return { error: "range" };
    }
    const [a, b, c, d] = values, rows = [a + b, c + d], cols = [a + c, b + d];
    const N = a + b + c + d;
    if (N === 0 || rows.some(n=>n===0)||cols.some(n=>n===0)) return { error: "margin" };
    const expected = [rows[0] * cols[0] / N, rows[0] * cols[1] / N,
      rows[1] * cols[0] / N, rows[1] * cols[1] / N];
    const contributions = values.map((o, i) => (o - expected[i]) ** 2 / expected[i]);
    const chi = contributions.reduce((sum, x) => sum + x, 0);
    // With df=1 the chi-square survival function is Q(1/2, chi/2) = erfc(sqrt(chi/2)).
    const p=chi===0?1:gammaQ(0.5, chi / 2);
    return { expected, contributions, chi, df: 1, p, v: Math.sqrt(chi / N), n: N,
      small: expected.filter(n => n < 5).length };
  }
  const api = { compute, gammaQ };
  if (typeof window !== "undefined") window.esaChiIndependence2x2 = api;

  const root = typeof document !== "undefined" && document.getElementById ?
    document.getElementById("esa-chi-independence-lab") : null;
  if (!root) return;
  const ar = root.dataset.locale === "ar";
  const text = ar ? {
    range: "أدخل عددًا صحيحًا من 0 إلى 10,000,000 في كل خلية.",
    margin: "يجب أن يكون مجموعا الصفين ومجموعا العمودين موجبة؛ فالهوامش الصفرية تجعل إحصائية الاستقلال غير معرّفة.",
    correct: "صحّح المدخلات لتقييم شروط العينة الكبيرة.",
    small: n => n + " من 4 تكرارات متوقعة أقل من 5. قد يكون تقريب كاي تربيع غير موثوق؛ فكّر في اختبار فيشر الدقيق وفي تصميم المعاينة.",
    ok: "جميع التكرارات المتوقعة الأربعة لا تقل عن 5. يبقى استقلال المشاهدات شرطًا يجب التحقق منه من تصميم الدراسة."
  } : {
    range: "Enter a whole-number count from 0 to 10,000,000 in every cell.",
    margin: "Both row totals and both column totals must be positive; zero margins make the independence statistic undefined.",
    correct: "Correct the inputs to evaluate the large-sample conditions.",
    small: n => n + " of 4 expected frequencies are below 5. The chi-square approximation may be unreliable; consider Fisher’s exact test and the sampling design.",
    ok: "All four expected frequencies are at least 5. Independence of observations must still be checked from the study design."
  };
  const find = id => root.querySelector("#" + id);
  const ids = ["a", "b", "c", "d"], inputs = ids.map(id => find("esa-chi-" + id));
  if (inputs.some(input => !input) || !find("esa-chi-reset")) return;
  const resultIds = ["esa-chi-stat", "esa-chi-p", "esa-chi-v", ...ids.map(id => "esa-chi-cell-" + id)];
  function clear(message) {
    find("esa-chi-error").hidden = false;
    find("esa-chi-error").textContent = message;
    inputs.forEach(input=>input.setAttribute("aria-invalid","true"));
    resultIds.forEach(id => find(id).textContent = "—");
    find("esa-chi-warning").textContent = text.correct;
  }
  function update() {
    const values = inputs.map(input => input.value.trim() === "" ? NaN : Number(input.value));
    const r = compute(values);
    if (r.error) { clear(text[r.error]); return; }
    inputs.forEach(input => input.setAttribute("aria-invalid", "false"));
    find("esa-chi-error").hidden = true;
    find("esa-chi-error").textContent = "";
    ids.forEach((id, i) => find("esa-chi-cell-" + id).textContent =
      values[i] + " → " + r.expected[i].toFixed(3) + "; " + r.contributions[i].toFixed(4));
    find("esa-chi-stat").textContent = r.chi.toFixed(6);
    find("esa-chi-p").textContent = r.p < 1e-12 ? "< 1e-12" : (r.p < 0.0001 ? r.p.toExponential(3) : r.p.toFixed(6));
    find("esa-chi-v").textContent = r.v.toFixed(6);
    find("esa-chi-warning").textContent = r.small ? text.small(r.small) : text.ok;
  }
  inputs.forEach(input => input.addEventListener("input", update));
  find("esa-chi-reset").addEventListener("click", () => {
    [40, 60, 70, 30].forEach((n, i) => inputs[i].value = String(n));
    update();
  });
  update();
})();
