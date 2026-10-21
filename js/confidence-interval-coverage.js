/* Shared exact-normal confidence-interval coverage engine; only presentation varies by language. */
(function () {
      "use strict";
      const root = document.getElementById("esa-ci-coverage-lab");
      if (!root) return;
      const arabic = document.documentElement.lang === "ar";
      const byId = (id) => document.getElementById(id);
      const confidence = byId("esa-ci-confidence");
      const sampleSize = byId("esa-ci-n");
      const chart = byId("esa-ci-chart");
      const plot = byId("esa-ci-intervals");
      const recent = byId("esa-ci-recent");
      const critical = {90:1.6448536269514722,95:1.959963984540054,99:2.5758293035489004};
      const NS = "http://www.w3.org/2000/svg";
      let total = 0, captured = 0, last = [];

      function standardNormal() {
        // Box-Muller: exact normal transformation of independent uniform draws.
        const u = 1 - Math.random();
        const v = Math.random();
        return Math.sqrt(-2 * Math.log(u)) * Math.cos(2 * Math.PI * v);
      }
      function model() {
        const n = Number(sampleSize.value), level = Number(confidence.value);
        return {n:n,level:level,half:critical[level] / Math.sqrt(n)};
      }
      function draw() {
        const cfg = model();
        byId("esa-ci-total").textContent = total.toLocaleString("en-US");
        byId("esa-ci-hit").textContent = captured.toLocaleString("en-US");
        byId("esa-ci-miss").textContent = (total - captured).toLocaleString("en-US");
        byId("esa-ci-observed").textContent = total ?
          (100 * captured / total).toFixed(1) + "%" : "—";
        byId("esa-ci-nominal").textContent = cfg.level + "%";
        byId("esa-ci-halfwidth").textContent = cfg.half.toFixed(4);

        // +/- 7 standard errors spans every ordinary sample interval.
        const plotScale = 7 / Math.sqrt(cfg.n);
        const position = (x) => Math.max(52, Math.min(588, 320 + 268 * x / plotScale));
        const nodes = [];
        for (let i = 0; i < last.length; i++) {
          const row = last[i], y = 32 + 14 * i;
          const line = document.createElementNS(NS, "line");
          line.setAttribute("x1", position(row.low).toFixed(2));
          line.setAttribute("x2", position(row.high).toFixed(2));
          line.setAttribute("y1", y);
          line.setAttribute("y2", y);
          line.setAttribute("stroke", row.hit ? "#0f766e" : "#b45309");
          line.setAttribute("stroke-width", "3.2");
          if (!row.hit) line.setAttribute("stroke-dasharray", "5 3");
          line.setAttribute("class", "esa-ci-interval");
          line.setAttribute("data-lower", row.low.toFixed(9));
          line.setAttribute("data-upper", row.high.toFixed(9));
          line.setAttribute("data-capture", row.hit ? "yes" : "no");
          nodes.push(line);
        }
        plot.replaceChildren(...nodes);
        const items = last.slice(-5).reverse().map((row) => {
          const li = document.createElement("li");
          li.textContent = "[" + row.low.toFixed(3) + ", " + row.high.toFixed(3) +
            "] — " + (row.hit ? (arabic ? "يشمل µ" : "captures µ") :
            (arabic ? "لا يشمل µ" : "misses µ"));
          return li;
        });
        recent.replaceChildren(...items);
        chart.setAttribute("aria-label", arabic ?
          ("أحدث " + last.length + " من أصل " + total + " فترة ثقة؛ متوسط المجتمع ثابت عند الصفر؛ " +
          captured + " فترة تشمل المتوسط الحقيقي.") :
          ("Latest " + last.length + " of " + total +
          " intervals; population mean fixed at zero; " + captured +
          " of " + total + " intervals capture the true mean."));
      }
      function run(count) {
        const cfg = model(), se = 1 / Math.sqrt(cfg.n);
        for (let i = 0; i < count; i++) {
          // Exact distribution of the mean of n independent N(0,1) observations.
          const mean = standardNormal() * se;
          const low = mean - cfg.half, high = mean + cfg.half;
          const hit = low <= 0 && 0 <= high;
          total++;
          if (hit) captured++;
          last.push({low:low,high:high,hit:hit});
          if (last.length > 20) last.shift();
        }
        draw();
      }
      function restart() {
        total = 0;captured = 0;last = [];
        run(100);
      }
      byId("esa-ci-run-100").addEventListener("click", () => run(100));
      byId("esa-ci-run-500").addEventListener("click", () => run(500));
      byId("esa-ci-reset").addEventListener("click", restart);
      confidence.addEventListener("change", restart);
      sampleSize.addEventListener("change", restart);
      restart();
    })();
