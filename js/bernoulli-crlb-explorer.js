/* Exact Bernoulli Cramér–Rao comparison: interior parameter, IID sampling. */
(function(){
  "use strict";
  if(!document.getElementById("esa-crlb-lab"))return;
  const $=id=>document.getElementById(id);
  const fields=["information","crlb","variance-mean","variance-first","efficiency-mean","efficiency-first","ratio"];
  const reset=()=>{fields.forEach(x=>{$("esa-crlb-"+x).textContent="—";});};
  function show(){
    const rawP=$("esa-crlb-p").value.trim(),rawN=$("esa-crlb-n").value.trim();
    const p=Number(rawP),n=Number(rawN);
    if(rawP===""||rawN===""||!Number.isFinite(p)||!(p>0&&p<1)||
       !Number.isSafeInteger(n)||n<1||n>500){
      reset();
      $("esa-crlb-status").textContent=
        "Enter 0 < p < 1 and an integer sample size from 1 to 500. Boundary values p=0 and p=1 are excluded from the regular CRLB formula.";
      return;
    }
    const varianceFirst=p*(1-p);
    const varianceMean=varianceFirst/n;
    const information=n/varianceFirst;
    const values={
      information:information.toFixed(4),
      crlb:varianceMean.toFixed(6),
      "variance-mean":varianceMean.toFixed(6),
      "variance-first":varianceFirst.toFixed(6),
      "efficiency-mean":"100.00%",
      "efficiency-first":(100/n).toFixed(2)+"%",
      ratio:n.toFixed(0)+"×"
    };
    for(const [key,value] of Object.entries(values))$("esa-crlb-"+key).textContent=value;
    $("esa-crlb-status").textContent=n===1?
      "With only one observation, the two estimators coincide and both attain the bound.":
      "The sample proportion uses all n IID observations and attains the bound; the first-observation estimator is unbiased but less efficient.";
  }
  $("esa-crlb-run").addEventListener("click",show);
  $("esa-crlb-reset").addEventListener("click",()=>{
    $("esa-crlb-p").value="0.30";$("esa-crlb-n").value="20";show();
  });
  ["esa-crlb-p","esa-crlb-n"].forEach(id=>$(id).addEventListener("change",show));
  show();
})();