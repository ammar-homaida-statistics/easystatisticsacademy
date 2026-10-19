/* Shared deterministic bootstrap learning lab. No dependencies or network calls. */
(function () {
  "use strict";
  const root = document.getElementById("esa-bootstrap-lab");
  if (!root) return;
  const ar = root.dataset.lang === "ar";
  const el = name => root.querySelector("#esa-boot-" + name);
  const words = ar ? {
    empty: "أدخل ملاحظتين على الأقل (وبحد أقصى 100). استعمل الفاصلة أو المسافة بين القيم.",
    invalid: "يجب أن تكون البيانات أعدادًا منتهية، وألا يتجاوز مقدار أي قيمة مليونًا.",
    seed: "يجب أن تكون البذرة عددًا صحيحًا بين 1 و4294967295.",
    ready: "تجربة تعليمية حتمية: تكرار التشغيل بنفس البيانات والبذرة يعطي النتيجة نفسها.",
    x: "متوسطات العينات المعاد سحبها", y: "عدد التكرارات",
    chart: "مدرج تكراري لتوزيع متوسطات العينات المعاد سحبها",
    constant: "القيم متساوية، لذلك يكون الخطأ المعياري التمهيدي صفرًا."
  } : {
    empty: "Enter between 2 and 100 observations separated by commas or whitespace.",
    invalid: "All data must be finite numbers with magnitude at most one million.",
    seed: "Seed must be an integer between 1 and 4294967295.",
    ready: "Deterministic illustration: the same data and seed produce identical results.",
    x: "Bootstrap sample means", y: "Resamples",
    chart: "Histogram of bootstrap sample means",
    constant: "All observations are identical, so the illustrative bootstrap SE is zero."
  };
  const svgNS = "http://www.w3.org/2000/svg";
  const fmt = x => Number(x).toFixed(4);
  function readData() {
    const raw = el("data").value.trim();
    const tokens = raw.split(/[\s,;]+/).filter(Boolean);
    if (tokens.length < 2 || tokens.length > 100) throw Error(words.empty);
    const nums = tokens.map(Number);
    if (nums.some(x => !Number.isFinite(x) || Math.abs(x) > 1e6)) throw Error(words.invalid);
    return nums;
  }
  function percentile(sorted, p) {
    const pos = (sorted.length - 1) * p, a = Math.floor(pos), b = Math.ceil(pos);
    return sorted[a] + (sorted[b] - sorted[a]) * (pos - a);
  }
  function histogram(values) {
    const graph = el("plot");
    graph.replaceChildren();
    const lo = Math.min(...values), hi = Math.max(...values);
    const bins = Array(10).fill(0);
    for (const value of values) {
      const index = lo === hi ? 4 : Math.min(9, Math.floor(10 * (value - lo) / (hi - lo)));
      bins[index] += 1;
    }
    const maxCount = Math.max(1, ...bins), base = 194, height = 160;
    bins.forEach((v, i) => {
      const rect = document.createElementNS(svgNS, "rect");
      rect.setAttribute("x", String(40 + 52 * i));
      rect.setAttribute("y", String(base - height * v / maxCount));
      rect.setAttribute("width", "49");
      rect.setAttribute("height", String(height * v / maxCount));
      rect.setAttribute("fill", "#0d9488");
      const title = document.createElementNS(svgNS, "title");
      title.textContent = (ar ? "الفئة " : "Bin ") + (i + 1) + ": " + v;
      rect.appendChild(title);
      graph.appendChild(rect);
    });
    const axis = document.createElementNS(svgNS, "path");
    axis.setAttribute("d", "M36 25 V194 H570");
    axis.setAttribute("stroke", "currentColor");
    axis.setAttribute("fill", "none");
    graph.appendChild(axis);
    const line = (txt,x,y,anchor) => {
      const t = document.createElementNS(svgNS, "text");
      t.setAttribute("x", x); t.setAttribute("y", y);
      t.setAttribute("text-anchor", anchor);
      t.setAttribute("fill", "currentColor"); t.setAttribute("font-size", "13");
      t.textContent = txt; graph.appendChild(t);
    };
    line(fmt(lo), "40", "216", "start");
    line(fmt(hi), "568", "216", "end");
    line(String(maxCount), "33", "30", "end");
    el("graph").setAttribute("aria-label", words.chart + ". " + values.length +
      (ar ? " تكرارًا، من " : " resamples, from ") + fmt(lo) + (ar ? " إلى " : " to ") + fmt(hi));
    el("counts").textContent = bins.join(", ");
  }
  function simulate() {
    try {
      const data = readData();
      const seedString = el("seed").value.trim();
      const seed = Number(seedString);
      if (!/^\d+$/.test(seedString) || !Number.isSafeInteger(seed) ||
          seed < 1 || seed > 4294967295) throw Error(words.seed);
      const B = Number(el("replications").value);
      if (![100, 500, 1000].includes(B)) throw Error(words.seed);
      let state = seed >>> 0;
      function draw() {
        state ^= (state << 13);
        state ^= (state >>> 17);
        state ^= (state << 5);
        return (state >>> 0) / 4294967296;
      }
      const n = data.length;
      const original = data.reduce((a,b) => a + b, 0) / n;
      const means = [];
      for (let b = 0; b < B; b++) {
        let sum = 0;
        for (let i = 0; i < n; i++) sum += data[Math.floor(draw() * n)];
        means.push(sum / n);
      }
      const bootMean = means.reduce((a,b) => a+b, 0) / B;
      const se = Math.sqrt(means.reduce((s,v) => s+(v-bootMean)*(v-bootMean),0)/(B-1));
      const sorted = means.slice().sort((a,b) => a-b);
      const low = percentile(sorted,0.025),high = percentile(sorted,0.975);
      el("n").textContent = String(n);
      el("mean").textContent = fmt(original);
      el("bootstrap-mean").textContent = fmt(bootMean);
      el("se").textContent = fmt(se);
      el("lower").textContent = fmt(low);
      el("upper").textContent = fmt(high);
      el("repetitions").textContent = String(B);
      el("status").textContent = se === 0 ? words.constant : words.ready;
      histogram(means);
      root.dataset.valid = "true";
    } catch (error) {
      root.dataset.valid = "false";
      el("status").textContent = error.message;
      el("n").textContent = "—";
      ["mean","bootstrap-mean","se","lower","upper"].forEach(id => {el(id).textContent = "—";});
      el("plot").replaceChildren();
      el("counts").textContent = "—";
    }
  }
  el("run").addEventListener("click",simulate);
  el("reset").addEventListener("click",() => {
    el("data").value = "5, 7, 8, 10";
    el("seed").value = "12345";
    el("replications").value = "500";
    simulate();
  });
  simulate();
})();