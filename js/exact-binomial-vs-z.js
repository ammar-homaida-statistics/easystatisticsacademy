/* Batch #90: exact binomial probability-ordering p-values vs null-based normal Z. */
(function(){
"use strict";
function logAdd(a,b){if(a===-Infinity)return b;if(b===-Infinity)return a;const max=Math.max(a,b);return max+Math.log1p(Math.exp(Math.min(a,b)-max));}
function compute(x,n,p0,side="two-sided"){
 if(!Number.isSafeInteger(n)||n<1||n>2000||!Number.isSafeInteger(x)||x<0||x>n||
    !Number.isFinite(p0)||!(p0>0&&p0<1)||!["two-sided","greater","less"].includes(side))return null;
 const logs=new Float64Array(n+1);for(let j=2;j<=n;j++)logs[j]=logs[j-1]+Math.log(j);
 const logp=Math.log(p0),logq=Math.log1p(-p0),lp=[];
 for(let k=0;k<=n;k++)lp.push(logs[n]-logs[k]-logs[n-k]+k*logp+(n-k)*logq);
 const observed=lp[x];let sum=-Infinity;
 for(let k=0;k<=n;k++){
  if((side==="greater"&&k>=x)||(side==="less"&&k<=x)||
     (side==="two-sided"&&lp[k]<=observed+1e-10))sum=logAdd(sum,lp[k]);
 }
 const exact=Math.min(1,Math.exp(sum));
 const z=window.esaOneProportionMath?.compute(x,n,p0,side);
 if(!z)return null;
 return {x,n,p0,side,exact,z:z.z,approx:z.pvalue,adequate:z.adequate,
  absDifference:Math.abs(exact-z.pvalue),
  expectedSuccesses:n*p0,expectedFailures:n*(1-p0)};
}
window.esaExactBinomial={compute,logAdd};
const root=document.getElementById("esa-exact-binomial-lab");if(!root)return;
const $=id=>root.querySelector("#esa-eb-"+id);
const fields=["x","n","p0","side"].map($),error=$("error"),results=$("results"),plot=$("plot");
function fmt(v){return v>=.0000005?v.toFixed(6):v===0?"0 (below display precision)":v.toExponential(3);}
function update(){
 const xraw=$("x").value.trim(),nraw=$("n").value.trim(),praw=$("p0").value.trim();
 const x=/^\d+$/.test(xraw)?Number(xraw):NaN;
 const n=/^\d+$/.test(nraw)?Number(nraw):NaN;
 const p0=praw===""?NaN:Number(praw);
 const r=compute(x,n,p0,$("side").value);
 [fields[0],fields[1],fields[2]].forEach(f=>f.setAttribute("aria-invalid",r?"false":"true"));
 if(!r){
  results.hidden=true;error.hidden=false;
  error.textContent="Enter 0 ≤ integer successes ≤ n, integer n from 1 to 2,000, and null proportion strictly between 0 and 1.";
  return;
 }
 error.hidden=true;error.textContent="";results.hidden=false;
 $("exact").textContent=fmt(r.exact);$("approx").textContent=fmt(r.approx);
 $("difference").textContent=fmt(r.absDifference);
 $("counts").textContent="n·p₀ = "+r.expectedSuccesses.toFixed(3)+"; n·(1−p₀) = "+r.expectedFailures.toFixed(3)+".";
 $("warning").textContent=r.adequate?"Both expected counts meet the conventional ≥10 rule of thumb; the Z test remains an approximation.":"Warning: at least one expected count is below 10; the normal Z approximation may be unreliable.";
 $("interpret").textContent="Exact two-sided tests include all outcomes whose binomial probability under H₀ is no greater than the observed outcome (probability ordering). Exact tests assume the independent binomial model. The difference displayed is in probability units, not percentage points.";
 const ns="http://www.w3.org/2000/svg";plot.replaceChildren();
 function el(tag,attrs,value){const e=document.createElementNS(ns,tag);for(const [key,val]of Object.entries(attrs))e.setAttribute(key,String(val));if(value!==undefined)e.textContent=String(value);plot.append(e);}
 el("title",{},"Exact and approximate binomial p-values");
 el("desc",{},"Two horizontal bars scaled from zero to one for the exact binomial and approximate normal p-values.");
 for(const [i,key,label] of [[0,"exact","Exact binomial"],[1,"approx","Normal Z"]]){
  const y=22+i*54;
  el("text",{x:6,y:y+14,fill:"currentColor","font-size":13},label);
  el("rect",{x:140,y:y-2,width:r[key]*370,height:21,fill:i?"#2563eb":"#0f766e"});
  el("text",{x:520,y:y+14,fill:"currentColor","font-size":12},fmt(r[key]));
 }
 el("line",{x1:140+370*.05,x2:140+370*.05,y1:4,y2:115,stroke:"currentColor","stroke-dasharray":"3 3"});
 plot.setAttribute("aria-label","Exact binomial p-value "+fmt(r.exact)+"; normal Z approximate p-value "+fmt(r.approx)+"; absolute difference "+fmt(r.absDifference));
}
fields.forEach(f=>{f.addEventListener("input",update);f.addEventListener("change",update)});
$("reset").addEventListener("click",()=>{$("x").value="2";$("n").value="10";$("p0").value="0.5";$("side").value="two-sided";update()});
update();
})();
