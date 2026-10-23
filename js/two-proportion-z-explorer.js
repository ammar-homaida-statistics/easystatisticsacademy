/* Batch #70: Two independent proportions, pooled equality-null Z and unpooled Wald CI. */
(function(){
"use strict";
const root=document.getElementById("esa-two-proportion-lab");if(!root)return;
const get=x=>root.querySelector("#esa-2p-"+x);
const fields=["x1","n1","x2","n2"].map(get),alternative=get("alternative"),
 error=get("error"),output=get("results");
function erfcPositive(x){
 const t=1/(1+0.3275911*x);
 return t*(0.254829592+t*(-0.284496736+
 t*(1.421413741+t*(-1.453152027+t*1.061405429))))*Math.exp(-x*x);
}
function tail(z){return z>=0?0.5*erfcPositive(z/Math.SQRT2):1-0.5*erfcPositive(-z/Math.SQRT2)}
function compute(x1,n1,x2,n2,side="two-sided"){
 if([x1,n1,x2,n2].some(v=>!Number.isSafeInteger(v))||
    n1<1||n2<1||n1>1000000||n2>1000000||
    x1<0||x1>n1||x2<0||x2>n2||!["two-sided","greater","less"].includes(side))return null;
 const p1=x1/n1,p2=x2/n2,diff=p1-p2,pooled=(x1+x2)/(n1+n2);
 const pooledSE=Math.sqrt(pooled*(1-pooled)*(1/n1+1/n2));
 const seCI=Math.sqrt(p1*(1-p1)/n1+p2*(1-p2)/n2);
 const adequate=[n1*pooled,n1*(1-pooled),n2*pooled,n2*(1-pooled)].every(v=>v>=10);
 if(pooledSE===0)return {degenerate:true,p1,p2,pooled,adequate,diff};
 const z=diff/pooledSE,upper=tail(z);
 const p=side==="two-sided"?Math.min(1,2*Math.min(upper,1-upper)):
   side==="greater"?upper:1-upper;
 const z975=1.959963984540054,lower=diff-z975*seCI,upperCI=diff+z975*seCI;
 return {p1,p2,diff,pooled,pooledSE,seCI,z,p,
   lower,upperCI,adequate,side,degenerate:false};
}
window.esaTwoProportionMath={compute,tail};
const fmt=x=>Number.isFinite(x)?x.toFixed(6):"—";
const ns="http://www.w3.org/2000/svg";
function element(t,a={},v){const e=document.createElementNS(ns,t);for(const [k,x] of Object.entries(a))e.setAttribute(k,String(x));if(v!==undefined)e.textContent=String(v);return e}
function plot(s){
 const svg=get("plot"),range=Math.max(.2,Math.abs(s.lower),Math.abs(s.upperCI),Math.abs(s.diff))*1.17;
 const xpos=x=>310+268*x/range;
 svg.replaceChildren(element("title",{},"Observed difference and unpooled Wald 95% confidence interval"),
 element("desc",{},"The point is p hat one minus p hat two, the interval is unpooled, and zero is a reference."),
 element("line",{x1:34,x2:586,y1:102,y2:102,stroke:"currentColor"}),
 element("line",{x1:xpos(0),x2:xpos(0),y1:24,y2:135,stroke:"#64748b","stroke-dasharray":"4 4"}),
 element("line",{x1:xpos(s.lower),x2:xpos(s.upperCI),y1:70,y2:70,stroke:"#0d9488","stroke-width":6}),
 element("circle",{cx:xpos(s.lower),cy:70,r:5,fill:"#0d9488"}),
 element("circle",{cx:xpos(s.upperCI),cy:70,r:5,fill:"#0d9488"}),
 element("circle",{cx:xpos(s.diff),cy:70,r:7,fill:"#64748b"}),
 element("text",{x:310,y:20,"text-anchor":"middle",fill:"currentColor","font-size":13},"p₁ − p₂ = "+fmt(s.diff)),
 element("text",{x:34,y:170,fill:"currentColor","font-size":11},fmt(-range)),
 element("text",{x:586,y:170,"text-anchor":"end",fill:"currentColor","font-size":11},fmt(range)),
 element("text",{x:xpos(0),y:151,"text-anchor":"middle",fill:"currentColor","font-size":11},"0"));
 svg.setAttribute("aria-label","Observed difference "+fmt(s.diff)+
   "; unpooled 95% confidence interval "+fmt(s.lower)+" to "+fmt(s.upperCI)+".");
}
function update(){
 const numbers=fields.map(e=>e.value.trim()!==""&&/^\d+$/.test(e.value.trim())?Number(e.value):NaN);
 const s=compute(...numbers,alternative.value);
 if(!s||s.degenerate){
  error.hidden=false;error.textContent=s&&s.degenerate?
    "Pooled-null variance is zero (all observations are successes or all failures); the Z test is undefined. Use an appropriate exact or alternative method.":
    "Enter whole-number successes and sample sizes (1–1,000,000), with 0 ≤ successes ≤ sample size for each independent group.";
  output.hidden=true;return;
 }
 error.hidden=true;error.textContent="";output.hidden=false;
 for(const k of ["p1","p2","diff","pooled","pooledSE","seCI","z","p","lower","upperCI"])get(k).textContent=fmt(s[k]);
 get("conditions").textContent=s.adequate?
   "Pooled expected success and failure counts are at least 10 in both groups (normal approximation count check passed).":
   "WARNING: At least one pooled expected success/failure count is below 10. The normal-approximation p-value and Wald CI may be unreliable; consider Fisher's exact test or a more reliable interval.";
 get("conclusion").textContent=(s.p<.05?"Reject":"Do not reject")+
   " equality H₀ at α=0.05, if independent sampling and approximation conditions are credible. Statistical significance alone does not establish causality.";
 get("interpretation").textContent="The unpooled 95% Wald interval describes p₁−p₂ and can extend outside the feasible difference range [−1,1]. "+
   "For small samples or proportions near 0 or 1, use a better-supported score or exact interval. "+
   "A one-sided test changes the p-value, not this two-sided interval.";
 plot(s);
}
fields.concat(alternative).forEach(e=>{e.addEventListener("input",update);e.addEventListener("change",update)});
get("reset").addEventListener("click",()=>{
 [120,200,90,200].forEach((v,i)=>fields[i].value=String(v));alternative.value="two-sided";update();
});
get("swap").addEventListener("click",()=>{
 const x1=fields[0].value,n1=fields[1].value;
 fields[0].value=fields[2].value;fields[1].value=fields[3].value;
 fields[2].value=x1;fields[3].value=n1;update();
});
update();
})();