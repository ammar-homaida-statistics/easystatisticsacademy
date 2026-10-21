/* Batch #59 — accessible Mean vs Median sensitivity explorer. No dependencies or storage. */
(function () {
  "use strict";
  const root = document.getElementById("esa-mean-median-explorer");
  if (!root) return;
  const byId = (id) => document.getElementById(id);
  const arabic = document.documentElement.lang === "ar";
  const t = (english, translation) => arabic ? translation : english;
  const sample = byId("esa-mm-sample");
  const extreme = byId("esa-mm-extreme");
  const error = byId("esa-mm-error");
  const summary = byId("esa-mm-results");
  const chart = byId("esa-mm-chart");
  const svgGroup = byId("esa-mm-points");
  const NS = "http://www.w3.org/2000/svg";
  const token = /^[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:e[+-]?\d+)?$/i;
  const output = (id, value) => { byId(id).textContent = value; };
  const display = (value) => Number(value.toPrecision(9)).toLocaleString("en-US", {maximumFractionDigits:9});
  function statistics(values) {
    const sorted = values.slice().sort((a, b) => a - b);
    const n = sorted.length;
    const mean = values.reduce((sum, x) => sum + x, 0) / n;
    const median = n % 2 ? sorted[(n - 1) / 2] :
      (sorted[n / 2 - 1] + sorted[n / 2]) / 2;
    return {mean, median};
  }
  function parse(text) {
    const items = text.split(/[\s,;]+/).filter(Boolean);
    if (items.length < 3 || items.length > 40 ||
        items.some((value) => !token.test(value))) {
      throw Error(t("Enter 3–40 finite numbers, separated by commas or spaces. Use a dot for decimals.", "أدخل من 3 إلى 40 عدداً منتهياً مفصولاً بفاصلة أو مسافة، واستخدم النقطة للفاصلة العشرية."));
    }
    const values = items.map(Number);
    if (values.some((x) => !Number.isFinite(x) || Math.abs(x) > 1e9)) {
      throw Error(t("Each observation must be finite and have an absolute value no greater than 1,000,000,000.", "يجب أن تكون القيمة العددية لكل مشاهدة منتهية وألا تتجاوز قيمتها المطلقة ملياراً."));
    }
    return values;
  }
  function node(tag, attrs, value) {
    const el = document.createElementNS(NS, tag);
    for (const [key, attr] of Object.entries(attrs)) el.setAttribute(key, String(attr));
    if (value !== undefined) el.textContent = value;
    return el;
  }
  function visualize(original, changed) {
    const all = original.concat(changed), min = Math.min(...all), max = Math.max(...all);
    const span = max - min || 1;
    const pos = (x) => 76 + (x - min) * 526 / span;
    const nodes = [
      node("line", {x1:76,y1:176,x2:602,y2:176,stroke:"currentColor","stroke-width":1}),
      node("text", {x:76,y:194,"text-anchor":"start","font-size":13,fill:"currentColor"},display(min)),
      node("text", {x:602,y:194,"text-anchor":"end","font-size":13,fill:"currentColor"},display(max)),
      node("text", {x:5,y:57,"font-size":14,fill:"currentColor"},t("Before", "قبل")),
      node("text", {x:5,y:131,"font-size":14,fill:"currentColor"},t("After", "بعد"))
    ];
    for (const [row,values,color] of [[0,original,"#0f766e"],[1,changed,"#b45309"]]) {
      for (let i = 0; i < values.length; i++) {
        const circle = node("circle", {
          cx:pos(values[i]).toFixed(2),cy:40+row*76+(i%5-2)*3.5,
          r:4.4,fill:color,"fill-opacity":0.78
        });
        circle.appendChild(node("title",{},(row ? t("After: ", "بعد: ") : t("Before: ", "قبل: "))+display(values[i])));
        nodes.push(circle);
      }
    }
    svgGroup.replaceChildren(...nodes);
    chart.setAttribute("aria-label",
      t("Dot plot comparing ", "مخطط نقطي يقارن ") + original.length + t(" baseline observations to modified observations. ", " مشاهدة أصلية بالقيم المعدلة. ") +
      t("Baseline range ", "مدى البيانات الأصلية ") + display(Math.min(...original)) + t(" to ", " إلى ") + display(Math.max(...original)) +
      t("; modified range ", "؛ ومدى البيانات المعدلة ") + display(Math.min(...changed)) + t(" to ", " إلى ") + display(Math.max(...changed)) + ".");
  }
  function render() {
    try {
      const before = parse(sample.value);
      const raw = extreme.value.trim();
      if (!raw || !token.test(raw)) throw Error(t("Enter a valid replacement observation.", "أدخل قيمة عددية صحيحة للمشاهدة البديلة."));
      const replacement = Number(raw);
      if (!Number.isFinite(replacement) || Math.abs(replacement) > 1e9) {
        throw Error(t("Replacement must be finite and within ±1,000,000,000.", "يجب أن تكون القيمة البديلة منتهية وفي حدود ±1,000,000,000."));
      }
      const after = before.slice();
      after[before.indexOf(Math.max(...before))] = replacement;
      const a = statistics(before), b = statistics(after);
      error.hidden = true;error.textContent = "";
      summary.hidden = false;chart.hidden = false;
      output("esa-mm-mean-before",display(a.mean));
      output("esa-mm-median-before",display(a.median));
      output("esa-mm-mean-after",display(b.mean));
      output("esa-mm-median-after",display(b.median));
      output("esa-mm-mean-change",display(b.mean-a.mean));
      output("esa-mm-median-change",display(b.median-a.median));
      output("esa-mm-explainer",t("Replaced one largest baseline observation (", "استُبدلت إحدى القيم الكبرى الأصلية (")+
        display(Math.max(...before))+t(") with ", ") بالقيمة ")+display(replacement)+
        t(". The mean uses every magnitude; the median depends on ranked middle observations. ", ". يتأثر المتوسط بمقادير جميع القيم، بينما يتحدد الوسيط وفق ترتيب القيم الوسطى. ")+
        t("The median is not necessarily unchanged for every sample or replacement.", "قد يتغير الوسيط أيضاً في بعض العينات أو عند بعض الاستبدالات."));
      visualize(before, after);
    } catch (err) {
      summary.hidden = true;chart.hidden = true;
      svgGroup.replaceChildren();
      error.textContent = err.message;
      error.hidden = false;
    }
  }
  sample.addEventListener("input",render);
  extreme.addEventListener("input",render);
  byId("esa-mm-reset").addEventListener("click",() => {
    sample.value = "2, 4, 6, 8, 10";
    extreme.value = "100";
    render();
  });
  render();
})();
