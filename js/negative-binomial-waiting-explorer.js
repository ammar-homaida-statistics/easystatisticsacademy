/* Shared negative-binomial waiting-time explorer for Arabic and English lessons. */
(function(){
  "use strict";
  const root=document.getElementById("esa-negbin-wait-explorer");
  if(!root)return;
  const ar=document.documentElement.lang==="ar";
  const byId=id=>root.querySelector("#"+id);
  const rInput=byId("esa-negbin-r"),pInput=byId("esa-negbin-p"),kInput=byId("esa-negbin-k");
  const CHART_BASE=135;
  function choose(n,k){
    if(k<0||k>n)return 0;
    let result=1;
    const count=Math.min(k,n-k);
    for(let i=1;i<=count;i++)result*=(n-count+i)/i;
    return result;
  }
  function mass(k,r,p){
    if(k<r)return 0;
    return choose(k-1,r-1)*Math.pow(p,r)*Math.pow(1-p,k-r);
  }
  function compute(r,p,k){
    if(!Number.isSafeInteger(r)||r<1||r>100||
       !Number.isFinite(p)||p<=0||p>1||
       !Number.isSafeInteger(k)||k<r||k>300)return null;
    const exact=mass(k,r,p);
    let cumulative=0;
    for(let j=r;j<=k;j++)cumulative+=mass(j,r,p);
    cumulative=Math.max(0,Math.min(1,cumulative));
    return {pmf:exact,cdf:cumulative,tail:1-cumulative,
      mean:r/p,variance:r*(1-p)/(p*p)};
  }
  window.esaNegBinMath=compute;
  function update(){
    const r=Number(rInput.value),p=Number(pInput.value);
    // Update min before setting k so the native slider does not clamp incorrectly.
    kInput.min=String(r);
    const k=Math.max(r,Math.min(30,Number(kInput.value)));
    kInput.value=String(k);
    const m=compute(r,p,k);
    if(!m)return;
    byId("esa-negbin-r-value").textContent=String(r);
    byId("esa-negbin-p-value").textContent=p.toFixed(2);
    byId("esa-negbin-k-value").textContent=String(k);
    byId("esa-negbin-pmf").textContent=m.pmf.toFixed(6);
    byId("esa-negbin-cdf").textContent=m.cdf.toFixed(6);
    byId("esa-negbin-tail").textContent=m.tail.toFixed(6);
    byId("esa-negbin-mean").textContent=m.mean.toFixed(4);
    byId("esa-negbin-variance").textContent=m.variance.toFixed(4);
    byId("esa-negbin-special").textContent=r===1
      ? (ar?"عندما r = 1 يصبح التوزيع السالب ذو الحدين هو التوزيع الهندسي لعدد المحاولات حتى أول نجاح.":
        "With r = 1, this is exactly the geometric trials-to-first-success distribution.")
      : (ar?"عندما r > 1 يشمل عدد المحاولات جميع النجاحات المطلوبة؛ اجعل r = 1 للعودة إلى التوزيع الهندسي.":
        "For r > 1, the completion trial includes all r successful trials; set r = 1 to recover the geometric distribution.");
    const chart=byId("esa-negbin-bars");
    const ns="http://www.w3.org/2000/svg",nodes=[];
    for(let j=r;j<r+12;j++){
      const x=40+(j-r)*24;
      const height=110*mass(j,r,p);
      const rect=document.createElementNS(ns,"rect");
      rect.setAttribute("x",String(x));
      rect.setAttribute("width","17");
      rect.setAttribute("y",String(CHART_BASE-height));
      rect.setAttribute("height",String(height));
      rect.setAttribute("fill",j===k?"#0d9488":"#64748b");
      rect.setAttribute("data-trial",String(j));
      nodes.push(rect);
      if(j===r||j===r+5||j===r+11){
        const text=document.createElementNS(ns,"text");
        text.setAttribute("x",String(x+8.5));
        text.setAttribute("y","152");
        text.setAttribute("fill","currentColor");
        text.setAttribute("font-size","10");
        text.setAttribute("text-anchor","middle");
        text.textContent=String(j);
        nodes.push(text);
      }
    }
    chart.replaceChildren(...nodes);
    byId("esa-negbin-chart").setAttribute("aria-label",
      (ar?"دالة الكتلة الاحتمالية السالبة ذات الحدين، عدد النجاحات المطلوبة r = ":
           "Negative binomial completion-trial PMF for r = ")+r+
      (ar?"، احتمال النجاح p = ":" successes with p = ")+p.toFixed(2)+
      (ar?"، المحاولة المحددة k = ":"; selected trial k = ")+k+
      ", P(X=k) = "+m.pmf.toFixed(6)+
      (ar?"، الحسابات التراكمية تشمل جميع المحاولات الممكنة.":
           "; cumulative probabilities include all possible trials."));
  }
  [rInput,pInput,kInput].forEach(input=>input.addEventListener("input",update));
  function preset(r,p,k){
    rInput.value=String(r);pInput.value=String(p);
    kInput.min=String(r);kInput.value=String(k);update();
  }
  byId("esa-negbin-reset").addEventListener("click",()=>preset(3,0.5,5));
  byId("esa-negbin-geometric").addEventListener("click",()=>preset(1,0.5,3));
  update();
})();