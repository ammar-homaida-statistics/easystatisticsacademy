/* Batch #71: one-proportion equality-null Z test, Wald and Wilson intervals. */
(function(){
"use strict";
const root=document.getElementById("esa-one-proportion-lab");if(!root)return;
const $=id=>root.querySelector("#esa-op-"+id);
const xs=$("x"),ns=$("n"),p0s=$("p0"),alternative=$("alternative");
const erfcPositive=t=>{
 const q=1/(1+0.3275911*t);
 return q*(0.254829592+q*(-0.284496736+
 q*(1.421413741+q*(-1.453152027+q*1.061405429))))*Math.exp(-t*t);
};
const upperTail=z=>z>=0 ? 0.5*erfcPositive(z/Math.SQRT2) : 1-0.5*erfcPositive(-z/Math.SQRT2);
const critical=1.959963984540054;
function compute(x,n,p0,side="two-sided"){
 if(!Number.isSafeInteger(x)||!Number.isSafeInteger(n)||n<1||n>1000000||x<0||x>n||
    !Number.isFinite(p0)||!(p0>0&&p0<1)||
    !["two-sided","greater","less"].includes(side))return null;
 const phat=x/n,se0=Math.sqrt(p0*(1-p0)/n),z=(phat-p0)/se0;
 const upper=upperTail(z),pvalue=side==="two-sided"?Math.min(1,2*Math.min(upper,1-upper)):
  side==="greater"?upper:1-upper;
 const seWald=Math.sqrt(phat*(1-phat)/n);
 const waldLower=phat-critical*seWald,waldUpper=phat+critical*seWald;
 const denom=1+critical*critical/n;
 const center=(phat+critical*critical/(2*n))/denom;
 const margin=critical*Math.sqrt(phat*(1-phat)/n+critical*critical/(4*n*n))/denom;
 return {phat,se0,z,pvalue,seWald,waldLower,waldUpper,
  wilsonLower:center-margin,wilsonUpper:center+margin,
  adequate:n*p0>=10&&n*(1-p0)>=10,
  x,n,p0,side};
}
window.esaOneProportionMath={compute,upperTail};
const fmt=v=>v.toFixed(6);
const nsSVG="http://www.w3.org/2000/svg";
function svg(name,attributes={},text){
 const el=document.createElementNS(nsSVG,name);
 for(const [k,v] of Object.entries(attributes))el.setAttribute(k,String(v));
 if(text!==undefined)el.textContent=String(text);
 return el;
}
function plot(v){
 const svgEl=$("plot"),pos=t=>45+525*t;
 const makeLine=(lo,hi,y,fill)=>[
  svg("line",{x1:pos(lo),x2:pos(hi),y1:y,y2:y,stroke:fill,"stroke-width":5}),
  svg("circle",{cx:pos(lo),cy:y,r:4,fill}),
  svg("circle",{cx:pos(hi),cy:y,r:4,fill})];
 svgEl.replaceChildren(
  svg("title",{},"Observed proportion, Wald interval and Wilson score interval"),
  svg("desc",{},"Horizontal scale from zero to one. Grey vertical line marks null proportion. Teal and orange lines show two different two-sided 95% confidence intervals."),
  svg("line",{x1:45,x2:570,y1:145,y2:145,stroke:"currentColor"}),
  svg("line",{x1:pos(v.p0),x2:pos(v.p0),y1:22,y2:149,stroke:"#64748b","stroke-dasharray":"4 4"}),
  ...makeLine(v.waldLower,v.waldUpper,55,"#0d9488"),
  ...makeLine(v.wilsonLower,v.wilsonUpper,100,"#b45309"),
  svg("circle",{cx:pos(v.phat),cy:78,r:6,fill:"#64748b"}),
  svg("text",{x:45,y:167,fill:"currentColor","font-size":13},"0"),
  svg("text",{x:570,y:167,fill:"currentColor","font-size":13,"text-anchor":"end"},"1"),
  svg("text",{x:45,y:45,fill:"currentColor","font-size":11},"Wald"),
  svg("text",{x:45,y:92,fill:"currentColor","font-size":11},"Wilson")
 );
 svgEl.setAttribute("aria-label","Observed proportion "+fmt(v.phat)+
 "; Wald 95% interval "+fmt(v.waldLower)+" to "+fmt(v.waldUpper)+
 "; Wilson 95% interval "+fmt(v.wilsonLower)+" to "+fmt(v.wilsonUpper)+
 "; null proportion "+fmt(v.p0)+".");
}
function render(){
 const xraw=xs.value.trim(),nraw=ns.value.trim(),praw=p0s.value.trim();
 const x=/^\d+$/.test(xraw)?Number(xraw):NaN;
 const n=/^\d+$/.test(nraw)?Number(nraw):NaN;
 const p0=praw!==""?Number(praw):NaN;
 const v=compute(x,n,p0,alternative.value);
 const error=$("error"),results=$("results");
 if(!v){
  results.hidden=true;error.hidden=false;
  error.textContent="Enter integer success count 0 ≤ x ≤ n, sample size 1–1,000,000, and 0 < null proportion p₀ < 1.";
  return;
 }
 error.hidden=true;error.textContent="";results.hidden=false;
 for(const key of ["phat","se0","z","pvalue","seWald","waldLower","waldUpper",
  "wilsonLower","wilsonUpper"]) $(key).textContent=fmt(v[key]);
 $("conditions").textContent=v.adequate?
  "Normal-approximation counts check passed: n p₀ and n(1−p₀) are at least 10.":
  "WARNING: n p₀ or n(1−p₀) is below 10. The Z approximation can be unreliable; consider an exact binomial test.";
 $("decision").textContent=(v.pvalue<.05?"Reject":"Do not reject")+" H₀: p=p₀ at α=0.05 if assumptions are satisfied.";
 $("interpretation").textContent="The two-sided 95% Wald interval can extend outside [0,1] and behave poorly near endpoints. "+
 "Wilson score intervals usually have better coverage; the score interval is closely related to inversion of the Z score test. "+
 "The two-sided confidence intervals are unchanged by the selected one-sided alternative.";
 plot(v);
}
[xs,ns,p0s,alternative].forEach(el=>{el.addEventListener("input",render);el.addEventListener("change",render);});
$("reset").addEventListener("click",()=>{
 xs.value="120";ns.value="200";p0s.value="0.50";alternative.value="two-sided";render();
});
render();
})();