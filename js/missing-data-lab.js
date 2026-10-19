/* Fixed-population missing data teaching laboratory. Shared English/Arabic calculations. */
(function () {
  "use strict";
  const root = document.getElementById("esa-md-lab");
  if (!root) return;
  const $ = id => document.getElementById(id);
  const ar = document.documentElement.lang === "ar";
  const words = ar ? {
    ready:"اكتملت المحاكاة باستخدام البذرة المحددة.",
    invalid:"أدخل بذرة صحيحة بين 0 و4294967295 واختر الخيارات المتاحة.",
    missing:"مفقود", none:"لا توجد قيم مشاهدة", unavailable:"غير متاح",
    missingness:"تظهر قيمة الفقد المحققة؛ وقد تختلف عن الاحتمال الأساسي.",
    equality:"الإكمال بالمتوسط لا يغير متوسط القيم المشاهدة، لكنه لا يعالج الانحياز وقد يقلل التباين."
  } : {
    ready:"Simulation complete; the same inputs and seed reproduce the result.",
    invalid:"Enter an integer seed from 0 to 4294967295 and select valid controls.",
    missing:"Missing", none:"No observed values", unavailable:"Unavailable",
    missingness:"Realized missingness varies by chance and need not equal the baseline probability.",
    equality:"Mean imputation preserves the complete-case mean; it does not fix bias and may shrink variance."
  };
  const population = [40,45,50,55,60,65,70,75,80,100];
  const group = ["A","A","A","A","A","B","B","B","B","B"];
  const N = population.length;
  const truth = population.reduce((a,b)=>a+b,0)/N;
  function random(seed) {
    let state = seed >>> 0;
    return function () {
      state = (state + 0x6D2B79F5) >>> 0;
      let t = Math.imul(state ^ (state >>> 15), 1 | state);
      t ^= t + Math.imul(t ^ (t >>> 7), 61 | t);
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  }
  const mode=$("esa-md-mode"), level=$("esa-md-level"), seed=$("esa-md-seed");
  const status=$("esa-md-status"), table=$("esa-md-table");
  function put(id,value) { $(id).textContent=value; }
  function format(value) { return Number.isFinite(value) ? value.toFixed(4) : words.unavailable; }
  function probability(kind,p,i) {
    if (kind==="mcar") return p;
    if (kind==="mar") return group[i]==="B" ? Math.min(.95,1.6*p) : .55*p;
    return population[i]>=70 ? Math.min(.95,1.8*p) : .3*p;
  }
  function simulate() {
    const nSeed=Number(seed.value), p=Number(level.value), kind=mode.value;
    if (!seed.value.trim() || !Number.isInteger(nSeed) || nSeed<0 || nSeed>4294967295 ||
        ![.1,.3,.5].includes(p) || !["mcar","mar","mnar"].includes(kind)) {
      status.textContent=words.invalid;
      return;
    }
    const rng=random(nSeed);
    const missing=population.map((value,i)=>rng()<probability(kind,p,i));
    const observed=population.filter((value,i)=>!missing[i]);
    const count=missing.filter(Boolean).length;
    const obsMean=observed.length ? observed.reduce((a,b)=>a+b,0)/observed.length : NaN;
    const filled=population.map((value,i)=>missing[i]?obsMean:value);
    const filledMean=observed.length?filled.reduce((a,b)=>a+b,0)/N:NaN;
    const filledVar=observed.length?filled.reduce((a,b)=>a+(b-filledMean)**2,0)/(N-1):NaN;
    put("esa-md-true",format(truth));
    put("esa-md-fraction",count+" / "+N+" ("+(100*count/N).toFixed(0)+"%)");
    put("esa-md-observed",format(obsMean));
    put("esa-md-imputed",format(filledMean));
    put("esa-md-error",format(obsMean-truth));
    put("esa-md-variance",format(filledVar));
    table.replaceChildren();
    population.forEach((value,i)=>{
      const tr=document.createElement("tr");
      [i+1,group[i],value,missing[i]?words.missing:value,
        !observed.length?words.unavailable:filled[i].toFixed(2)].forEach(cell=>{
        const td=document.createElement("td");
        td.textContent=String(cell);
        tr.appendChild(td);
      });
      table.appendChild(tr);
    });
    status.textContent=words.ready;
    $("esa-md-notes").textContent=observed.length?words.missingness+" "+words.equality:
      words.none+". "+words.missingness;
  }
  $("esa-md-run").addEventListener("click",simulate);
  $("esa-md-reset").addEventListener("click",()=>{
    mode.value="mcar";level.value="0.3";seed.value="2026";simulate();
  });
  simulate();
})();