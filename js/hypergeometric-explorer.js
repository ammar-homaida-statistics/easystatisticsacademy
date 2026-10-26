/* Batch #60 — exact sampling-without-replacement probabilities.
   The hypergeometric law is evaluated through log combinations to avoid overflow.
   The binomial curve is an explicit with-replacement approximation, not an identity. */
(function () {
  "use strict";
  const root = document.getElementById("esa-hypergeom-explorer");
  const arabic = document.documentElement.lang === "ar";
  if (!root) return;
  const el = (id) => document.getElementById("esa-hg-" + id);
  const ids = ["N", "K", "n", "x"];
  const bars = el("bars");
  const chart = el("chart");
  const status = el("status");
  const outputIds = ["support", "exact", "approx", "difference", "mean", "variance", "total", "sampling-fraction"];
  const NS = "http://www.w3.org/2000/svg";
  const logFactorials = [0];
  function ensureFactorials(n) {
    while (logFactorials.length <= n) {
      const k = logFactorials.length;
      logFactorials.push(logFactorials[k - 1] + Math.log(k));
    }
  }
  function logChoose(n, k) {
    if (k < 0 || k > n) return -Infinity;
    ensureFactorials(n);
    return logFactorials[n] - logFactorials[k] - logFactorials[n - k];
  }
  function hypergeom(N, K, n, x) {
    if (x < Math.max(0, n - (N - K)) || x > Math.min(n, K)) return 0;
    return Math.exp(logChoose(K, x) + logChoose(N - K, n - x) - logChoose(N, n));
  }
  function binomial(n, p, x) {
    if (x < 0 || x > n) return 0;
    if (p === 0) return x === 0 ? 1 : 0;
    if (p === 1) return x === n ? 1 : 0;
    return Math.exp(logChoose(n, x) + x * Math.log(p) + (n - x) * Math.log1p(-p));
  }
  const format = (n) => n.toFixed(6);
  function draw(N, K, n, selected) {
    const p = K / N;
    const left = Math.max(0, n - (N - K)), right = Math.min(n, K);
    const xs = Array.from({length:n + 1}, (_, x) => x);
    const exact = xs.map(x => hypergeom(N, K, n, x));
    const approx = xs.map(x => binomial(n, p, x));
    const peak = Math.max(1e-12, ...exact, ...approx);
    const chartWidth = 650, base = 216;
    const step = chartWidth / (n + 1);
    const items = [];
    const node = (tag, attrs, label) => {
      const e = document.createElementNS(NS, tag);
      for (const [key, val] of Object.entries(attrs)) e.setAttribute(key, String(val));
      if (label !== undefined) e.textContent = label;
      return e;
    };
    items.push(node("line",{x1:48,y1:base,x2:698,y2:base,stroke:"currentColor","stroke-width":1}));
    for (const x of xs) {
      const center = 48 + (x + 0.5) * step;
      const h = exact[x] * 170 / peak;
      const b = approx[x] * 170 / peak;
      const w = Math.max(0.5, Math.min(9,step * .31));
      const a = node("rect",{x:(center-w-1).toFixed(2),y:(base-h).toFixed(2),
        width:w.toFixed(2),height:Math.max(0,h).toFixed(2),
        fill:"#0f766e",opacity:x===selected?1:.77});
      a.appendChild(node("title",{},(arabic?"دون إرجاع؛ س = ":"Without replacement; x = ")+x+"; P = "+format(exact[x])));
      items.push(a);
      const second = node("rect",{x:(center+1).toFixed(2),y:(base-b).toFixed(2),
        width:w.toFixed(2),height:Math.max(0,b).toFixed(2),
        fill:"#b45309",opacity:x===selected?1:.65});
      second.appendChild(node("title",{},(arabic?"تقريب ثنائي الحدين؛ س = ":"Binomial approximation; x = ")+x+"; P = "+format(approx[x])));
      items.push(second);
    }
    for (const x of [...new Set([0,Math.round(n/2),n])]) {
      items.push(node("text",{x:(48+(x+.5)*step).toFixed(2),y:235,
        "font-size":12,fill:"currentColor","text-anchor":"middle"},String(x)));
    }
    bars.replaceChildren(...items);
    chart.setAttribute("aria-label",arabic ? "احتمالات فوق هندسية دقيقة باللون الأخضر وتقريب ثنائي الحدين بالبرتقالي للنتائج من صفر إلى "+n+". القيمة المختارة "+selected+"؛ احتمالها الدقيق "+format(exact[selected])+"." : "Exact hypergeometric probabilities in teal and with-replacement binomial approximation in amber, across counts 0 to "+n+". Selected count "+selected+". Exact probability "+format(exact[selected])+".");
    return {left,right,exact:exact[selected],approx:approx[selected],
      total:exact.reduce((a,b)=>a+b,0)};
  }
  function clear() {
    for (const id of outputIds) el(id).textContent = "—";
    bars.replaceChildren();chart.hidden=true;chart.style.display="none";
  }
  function render() {
    try {
      const numbers = {};
      for (const id of ids) {
        const raw = el(id).value.trim();
        if (!/^\d+$/.test(raw)) throw Error(arabic?"يرجى إدخال أعداد صحيحة لـ N وK وn وx.":"Enter whole numbers for N, K, n and x.");
        numbers[id] = Number(raw);
        if (!Number.isSafeInteger(numbers[id])) throw Error(arabic?"يجب أن تكون جميع المدخلات أعدادًا صحيحة ضمن المجال الآمن.":"Inputs must be safe whole numbers.");
      }
      const {N,K,n,x} = numbers;
      if (N < 1 || N > 1000 || K > N || n > N || n > 100 || x > n) {
        throw Error(arabic?"يُشترط 1 ≤ N ≤ 1000 و0 ≤ K ≤ N و0 ≤ n ≤ min(N,100) و0 ≤ x ≤ n.":"Use 1 ≤ N ≤ 1000, 0 ≤ K ≤ N, 0 ≤ n ≤ min(N, 100), and 0 ≤ x ≤ n.");
      }
      const result = draw(N,K,n,x);
      const p=K/N, variance=N===1?0:n*p*(1-p)*(N-n)/(N-1);
      el("support").textContent = result.left + (arabic?" إلى ":" to ") + result.right;
      el("exact").textContent = format(result.exact);
      el("approx").textContent = format(result.approx);
      el("difference").textContent = format(Math.abs(result.exact-result.approx));
      el("mean").textContent = format(n*p);
      el("variance").textContent = format(variance);
      el("total").textContent = format(result.total);
      el("sampling-fraction").textContent = (100*n/N).toFixed(2)+"%";
      status.textContent = (x<result.left||x>result.right?
        (arabic?"القيمة المختارة غير ممكنة دون إرجاع؛ واحتمالها الدقيق صفر. ":"The selected x is impossible without replacement, so its exact probability is zero. ") : "") +
        (n/N > .05?
          (arabic?"تنبيه: تتجاوز نسبة المعاينة 5% وقد يكون تقريب ثنائي الحدين غير دقيق. ":"Caution: the sample exceeds 5% of the population; the binomial approximation may be inaccurate. ") :
          (arabic?"نسبة المعاينة لا تتجاوز 5% لكن دقة التقريب تعتمد أيضًا على المعلمات. ":"The sampling fraction is at most 5%; binomial approximation accuracy still depends on the parameters. ")) +
        (arabic?"السحب عشوائي منتظم دون إرجاع؛ ويستخدم نموذج المقارنة محاولات مستقلة مع p = K/N.":"Sampling is uniformly random without replacement; the comparison model uses independent trials with p = K/N.");
      status.hidden=false;chart.hidden=false;chart.style.display="block";
    } catch (error) {
      clear();status.textContent=error.message;status.hidden=false;
    }
  }
  for (const id of ids) el(id).addEventListener("input",render);
  el("reset").addEventListener("click",()=>{
    for (const [id,val] of Object.entries({N:"100",K:"10",n:"5",x:"1"})) el(id).value=val;
    render();
  });
  render();
})();
