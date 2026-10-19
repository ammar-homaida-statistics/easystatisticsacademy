/* Shared English/Arabic SD laboratory. No storage, network, or external libraries. */
(function () {
  "use strict";
  if (!document.getElementById("esa-sd-lab")) return;
  const $ = id => document.getElementById(id);
  const ar = document.documentElement.lang === "ar";
  const labels = ar ? {
    ready:"أُعيد الحساب وفق القيم المدخلة.",
    invalid:"أدخل من قيمة واحدة إلى 20 قيمة عددية منتهية، تفصلها فواصل أو مسافات، وألا تتجاوز القيمة المطلقة مليونًا.",
    undefined:"غير معرّف (يلزم وجود مشاهدتين على الأقل)",
    single:"لا يمكن حساب تباين العينة أو انحرافها المعياري عند وجود قيمة واحدة فقط.",
    note:"الانحراف المعياري يقيس التشتت في وحدة القياس الأصلية؛ أما التباين ففي الوحدة المربعة.",
    data:"القيم"
  } : {
    ready:"Calculation updated for the observations shown.",
    invalid:"Enter 1–20 finite numbers separated by commas or spaces; absolute values must not exceed one million.",
    undefined:"Undefined (requires at least two observations)",
    single:"Sample variance and sample SD are undefined when n = 1.",
    note:"Standard deviation is in the original measurement units; variance uses squared units.",
    data:"Values"
  };
  const values=$("esa-sd-values"), status=$("esa-sd-status"), table=$("esa-sd-table");
  const initial="2, 4, 4, 4, 5, 5, 7, 9";
  function format(n) { return n.toFixed(4); }
  function parse(raw) {
    const entries=raw.trim().split(/[\s,;]+/).filter(Boolean);
    if (!entries.length || entries.length>20) return null;
    const pattern=/^[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:e[+-]?\d+)?$/i;
    if (!entries.every(s=>pattern.test(s))) return null;
    const nums=entries.map(Number);
    return nums.every(n=>Number.isFinite(n)&&Math.abs(n)<=1000000)?nums:null;
  }
  function render() {
    const xs=parse(values.value);
    if (!xs) { status.textContent=labels.invalid;return; }
    const n=xs.length;
    const mean=xs.reduce((sum,x)=>sum+x,0)/n;
    const deltas=xs.map(x=>x-mean);
    const squares=deltas.map(d=>d*d);
    const ss=squares.reduce((sum,x)=>sum+x,0);
    const populationVariance=ss/n;
    const populationSD=Math.sqrt(populationVariance);
    const sampleVariance=n>=2?ss/(n-1):null;
    const sampleSD=sampleVariance===null?null:Math.sqrt(sampleVariance);
    [["esa-sd-count",String(n)],["esa-sd-mean",format(mean)],["esa-sd-ss",format(ss)],
     ["esa-sd-pop-var",format(populationVariance)],["esa-sd-pop-sd",format(populationSD)],
     ["esa-sd-samp-var",sampleVariance===null?labels.undefined:format(sampleVariance)],
     ["esa-sd-samp-sd",sampleSD===null?labels.undefined:format(sampleSD)]]
      .forEach(([id,value])=>{$(id).textContent=value;});
    table.replaceChildren();
    xs.forEach((x,i)=>{
      const row=document.createElement("tr");
      [i+1,format(x),format(deltas[i]),format(squares[i])].forEach(val=>{
        const cell=document.createElement("td");
        cell.dir="ltr";cell.textContent=String(val);row.appendChild(cell);
      });
      table.appendChild(row);
    });
    status.textContent=labels.ready;
    $("esa-sd-note").textContent=n===1?labels.single:labels.note;
  }
  $("esa-sd-run").addEventListener("click",render);
  $("esa-sd-outlier").addEventListener("click",()=>{values.value="2, 4, 4, 4, 5, 5, 7, 30";render();});
  $("esa-sd-identical").addEventListener("click",()=>{values.value="10, 10, 10, 10, 10";render();});
  $("esa-sd-single").addEventListener("click",()=>{values.value="10";render();});
  $("esa-sd-reset").addEventListener("click",()=>{values.value=initial;render();});
  render();
})();