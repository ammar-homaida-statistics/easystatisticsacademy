/* Batch #91: conditional Fisher exact 2x2 versus Pearson chi-square (no Yates correction).
   Two-sided Fisher follows probability ordering, as SciPy fisher_exact. */
(function(){
"use strict";
function erfc(x){const t=1/(1+.3275911*x);return t*(.254829592+t*(-.284496736+t*(1.421413741+t*(-1.453152027+t*1.061405429))))*Math.exp(-x*x);}
function compute(a,b,c,d,side="two-sided"){
 const cells=[a,b,c,d];
 if(cells.some(x=>!Number.isSafeInteger(x)||x<0)||!["two-sided","greater","less"].includes(side))return null;
 const N=a+b+c+d,r1=a+b,r2=c+d,c1=a+c,c2=b+d;
 if(!(N>0&&N<=2000)||!r1||!r2||!c1||!c2)return null;
 const expected=[r1*c1/N,r1*c2/N,r2*c1/N,r2*c2/N];
 const chi=cells.reduce((s,o,i)=>s+(o-expected[i])**2/expected[i],0);
 const chiP=chi===0?1:Math.max(0,Math.min(1,erfc(Math.sqrt(chi/2))));
 const lo=Math.max(0,r1-c2),hi=Math.min(r1,c1);
 // Exact conditional hypergeometric distribution for top-left cell, fixed margins.
 const logfacts=new Float64Array(N+1);
 for(let i=2;i<=N;i++)logfacts[i]=logfacts[i-1]+Math.log(i);
 const comb=(n,k)=>logfacts[n]-logfacts[k]-logfacts[n-k];
 const logs=[];
 for(let x=lo;x<=hi;x++)logs.push(comb(c1,x)+comb(c2,r1-x)-comb(N,r1));
 const observed=logs[a-lo];
 let sum=0;
 for(let x=lo;x<=hi;x++){
  const log=logs[x-lo];
  // Relative probability-ordering tie tolerance, avoid subtracting tiny probabilities.
  if(side==="greater"?x>=a:side==="less"?x<=a:log<=observed+1e-9)sum+=Math.exp(log);
 }
 const fisher=Math.min(1,sum);
 return {a,b,c,d,N,r1,r2,c1,c2,expected,chi,chiP,fisher,side,small:expected.filter(x=>x<5).length,lo,hi};
}
window.esaFisherChiMath={compute};
const root=document.getElementById("esa-fisher-chi-lab");if(!root)return;
const $=x=>root.querySelector("#esa-fc-"+x),fields=["a","b","c","d"].map($),side=$("side"),
 error=$("error"),results=$("results");
const fmt=x=>x<.0000005&&x>0?x.toExponential(4):x.toFixed(6);
function update(){
 const nums=fields.map(e=>/^\d+$/.test(e.value.trim())?Number(e.value.trim()):NaN);
 const r=compute(...nums,side.value);
 fields.forEach(e=>e.setAttribute("aria-invalid",r?"false":"true"));
 if(!r){error.hidden=false;results.hidden=true;error.textContent="Enter four non-negative whole-number counts, each row and column total positive, and overall N between 1 and 2000.";return;}
 error.hidden=true;error.textContent="";results.hidden=false;
 $("fisher").textContent=fmt(r.fisher);$("pearson").textContent=fmt(r.chiP);
 $("chi").textContent=r.chi.toFixed(6);$("N").textContent=String(r.N);
 ["a","b","c","d"].forEach((name,i)=>$(name+"expected").textContent=r.expected[i].toFixed(3));
 $("warning").textContent=r.small?
  r.small+" of four expected cell counts are below 5; Pearson's large-sample approximation can be unreliable.":
  "All expected cell counts are at least 5; independence and sampling assumptions still matter.";
 $("meaning").textContent="Fisher conditions on both margins; the two-sided p-value sums tables no more probable than the observed table. Pearson uses χ² with 1 df and no Yates correction. Exact conditional inference requires an appropriate independent sampling model; neither test establishes causation.";
 const plot=$("plot"),ns="http://www.w3.org/2000/svg";plot.replaceChildren();
 function el(tag,attrs,label){const e=document.createElementNS(ns,tag);for(const [k,v]of Object.entries(attrs))e.setAttribute(k,String(v));if(label!==undefined)e.textContent=label;plot.append(e);}
 el("title",{},"Conditional Fisher exact and Pearson chi-square p-values");
 for(const [i,label,value,color]of [[0,"Fisher",r.fisher,"#0f766e"],[1,"Pearson",r.chiP,"#2563eb"]]){
  const y=18+i*52;el("text",{x:5,y:y+16,fill:"currentColor","font-size":13},label);
  el("rect",{x:110,y:y,width:Math.max(0,375*value),height:20,fill:color});
  el("text",{x:495,y:y+15,fill:"currentColor","font-size":12},fmt(value));
 }
 el("line",{x1:110+375*.05,x2:110+375*.05,y1:3,y2:118,stroke:"currentColor","stroke-dasharray":"3 3"});
 plot.setAttribute("aria-label","Fisher exact p-value "+fmt(r.fisher)+"; Pearson chi-square p-value "+fmt(r.chiP));
}
[...fields,side].forEach(e=>{e.addEventListener("input",update);e.addEventListener("change",update)});
$("reset").addEventListener("click",()=>{[1,9,11,3].forEach((x,i)=>fields[i].value=x);side.value="two-sided";update();});
update();
})();