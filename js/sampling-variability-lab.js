/* Sampling-variability laboratory shared by the English and Arabic lessons.
   Exact finite population: [160,165,170,175,180], N=5, variance (denominator N)=50.
   For SRSWOR: Var(mean) = (sigma²/n)*(N-n)/(N-1).
   For independent sampling with replacement: Var(mean) = sigma²/n. */
(function () {
  "use strict";
  const root = document.getElementById("esa-sv-lab");
  if (!root) return;
  const ar = document.documentElement.lang === "ar";
  const ui = ar ? {
    ready: "اكتملت المحاكاة وقابلة لإعادة الإنتاج بالبذرة المختارة.",
    count: "عدد العينات المحاكاة",
    error: "أدخل بذرة صحيحة بين 0 و4294967295 واختر القيم المتاحة.",
    axis: "متوسطات العينات",
    yaxis: "عدد التكرارات"
  } : {
    ready: "Simulation complete; identical inputs and seed reproduce the result.",
    count: "Simulated samples",
    error: "Enter an integer seed from 0 to 4294967295 and select available options.",
    axis: "Sample means",
    yaxis: "Frequency"
  };
  const population = [160, 165, 170, 175, 180];
  const N = population.length;
  const mu = population.reduce((s, v) => s + v, 0) / N;
  const sigmaSquared = population.reduce((s, v) => s + (v - mu) ** 2, 0) / N;
  const $ = id => document.getElementById(id);
  const size = $("esa-sv-size"), method = $("esa-sv-method");
  const reps = $("esa-sv-reps"), seed = $("esa-sv-seed");
  const status = $("esa-sv-status"), plot = $("esa-sv-plot"), preview = $("esa-sv-preview");
  const ns = "http://www.w3.org/2000/svg";
  function svgNode(name, attrs, text) {
    const el = document.createElementNS(ns, name);
    Object.entries(attrs).forEach(([k, v]) => el.setAttribute(k, String(v)));
    if (text !== undefined) el.textContent = text;
    plot.appendChild(el);
    return el;
  }
  function random(seedValue) {
    let state = seedValue >>> 0;
    return function () {
      state = (state + 0x6D2B79F5) >>> 0;
      let t = Math.imul(state ^ (state >>> 15), 1 | state);
      t ^= t + Math.imul(t ^ (t >>> 7), 61 | t);
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  }
  function sample(rng, n, replace) {
    const values = [];
    if (replace) {
      for (let k = 0; k < n; k++) values.push(population[Math.floor(rng() * N)]);
    } else {
      const pool = population.slice();
      // Partial Fisher–Yates shuffle: unbiased ordered draw without replacement.
      for (let k = 0; k < n; k++) {
        const j = k + Math.floor(rng() * (N - k));
        [pool[k], pool[j]] = [pool[j], pool[k]];
        values.push(pool[k]);
      }
    }
    return values;
  }
  function histogram(values) {
    while (plot.firstChild) plot.removeChild(plot.firstChild);
    const lo = Math.min(...values), hi = Math.max(...values), span = hi - lo;
    const bins = Array(16).fill(0);
    values.forEach(v => {
      const bin = span === 0 ? 8 : Math.min(15, Math.floor((v - lo) / span * 16));
      bins[bin]++;
    });
    const peak = Math.max(...bins, 1);
    svgNode("line", {x1:48, y1:228, x2:658, y2:228, stroke:"currentColor", "stroke-width":1});
    bins.forEach((count, i) => {
      svgNode("rect", {x:52 + i * 37.5, y:226 - count / peak * 190,
        width:35, height:count / peak * 190, fill:"#2563eb", class:"esa-sv-bin"});
    });
    svgNode("text", {x:52, y:249, fill:"currentColor", "font-size":13}, lo.toFixed(2));
    svgNode("text", {x:609, y:249, fill:"currentColor", "font-size":13}, hi.toFixed(2));
    svgNode("text", {x:280, y:267, fill:"currentColor", "font-size":12}, ui.axis);
    svgNode("text", {x:12, y:28, fill:"currentColor", "font-size":12}, ui.yaxis + ": " + peak);
  }
  function simulate() {
    const n = Number(size.value), B = Number(reps.value), s = Number(seed.value);
    const withReplacement = method.value === "with";
    if (!Number.isInteger(n) || n < 1 || n > N ||
        ![100,500,2000].includes(B) || !["with","without"].includes(method.value) ||
        !Number.isInteger(s) || s < 0 || s > 4294967295 || !seed.value.trim()) {
      status.textContent = ui.error;
      return;
    }
    const rng = random(s), means = [];
    let first = [];
    for (let b = 0; b < B; b++) {
      const observations = sample(rng, n, withReplacement);
      if (b === 0) first = observations;
      means.push(observations.reduce((sum, value) => sum + value, 0) / n);
    }
    const simMean = means.reduce((sum, value) => sum + value, 0) / B;
    const simulatedSE = Math.sqrt(means.reduce((sum, value) => sum + (value - simMean) ** 2, 0) / (B - 1));
    const theoreticalSE = Math.sqrt(sigmaSquared / n *
      (withReplacement ? 1 : (N - n) / (N - 1)));
    const write = (id, value) => { $(id).textContent = value.toFixed(4); };
    write("esa-sv-mu", mu);
    write("esa-sv-sigma2", sigmaSquared);
    write("esa-sv-theory", theoreticalSE);
    write("esa-sv-simulated", simulatedSE);
    write("esa-sv-average", simMean);
    write("esa-sv-bias", simMean - mu);
    preview.textContent = first.join(", ");
    histogram(means);
    status.textContent = ui.ready + " " + ui.count + ": " + B + ".";
  }
  $("esa-sv-run").addEventListener("click", simulate);
  $("esa-sv-reset").addEventListener("click", () => {
    size.value="2"; method.value="without"; reps.value="500"; seed.value="2026";
    simulate();
  });
  simulate();
})();