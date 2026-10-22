/* Easy Statistics Academy Batch #66 — Pearson chi-square goodness-of-fit.
   Prespecified positive null probabilities; no fitted parameters or dependencies. */
(function(){
"use strict";
const root=document.getElementById("esa-gof-explorer");if(!root)return;
const get=id=>root.querySelector("#esa-gof-"+id);
const coeff=[0.99999999999980993,676.5203681218851,-1259.1392167224028,
 771.32342877765313,-176.61502916214059,12.507343278686905,
 -0.13857109526572012,9.984369578019572e-6,1.5056327351493116e-7];
function logGamma(z){
 if(!Number.isFinite(z)||z<=0)return NaN;
 if(z<.5)return Math.log(Math.PI)-Math.log(Math.sin(Math.PI*z))-logGamma(1-z);
 z-=1;let sum=coeff[0];for(let i=1;i<coeff.length;i++)sum+=coeff[i]/(z+i);
 const t=z+7.5;return .5*Math.log(2*Math.PI)+(z+.5)*Math.log(t)-t+Math.log(sum);
}
// Regularized upper incomplete gamma Q(a,x), chi-square right-tail = Q(df/2,chi2/2).
function gammaQ(a,x){
 if(!(a>0)||!Number.isFinite(a)||Number.isNaN(x)||x<0)return NaN;
 if(x===0)return 1;if(x===Infinity)return 0;
 const term=Math.exp(-x+a*Math.log(x)-logGamma(a));
 const eps=2e-14,min=1e-300,max=700;
 let ans;
 if(x<a+1){
   let sum=1/a,del=sum,ap=a;
   for(let n=1;n<=max;n++){
     ap++;del*=x/ap;sum+=del;
     if(Math.abs(del)<=Math.abs(sum)*eps)break;
   }
   ans=1-sum*term;
 }else{
   let b=x+1-a,c=1/min,d=1/b,h=d;
   for(let i=1;i<=max;i++){
     const an=-i*(i-a);b+=2;
     d=an*d+b;if(Math.abs(d)<min)d=min;
     c=b+an/c;if(Math.abs(c)<min)c=min;
     d=1/d;const delta=d*c;h*=delta;
     if(Math.abs(delta-1)<eps)break;
   }
   ans=term*h;
 }
 return Math.max(0,Math.min(1,ans));
}
function compute(observed,probs){
 if(!Array.isArray(observed)||!Array.isArray(probs)||observed.length!==probs.length||
    observed.length<2||observed.length>12)return null;
 if(observed.some(x=>!Number.isSafeInteger(x)||x<0||x>10000000)||
    probs.some(x=>!Number.isFinite(x)||x<=0||x>1))return null;
 const n=observed.reduce((a,b)=>a+b,0),sum=probs.reduce((a,b)=>a+b,0);
 if(n===0||Math.abs(sum-1)>1e-8)return null;
 const expected=probs.map(p=>n*p);
 const terms=observed.map((o,i)=>(o-expected[i])**2/expected[i]);
 const statistic=terms.reduce((a,b)=>a+b,0);
 const df=observed.length-1;
 return {n,df,expected,terms,statistic,p:gammaQ(df/2,statistic/2),
    counts:observed,probs,smallExpected:expected.some(x=>x<5)};
}
window.esaChiSquareGofMath={compute,gammaQ};
const counts=get("counts"),probs=get("probs"),error=get("error"),results=get("results");
const fmt=x=>Number.isFinite(x)?x.toFixed(6):"—";
function parse(text,isCounts){
 const parts=text.split(/[,\n;]+/).map(s=>s.trim());
 if(parts.length<2||parts.length>12||parts.some(s=>!s||
    !/^(?:\d+\.?\d*|\.\d+)(?:e[+-]?\d+)?$/i.test(s)))return null;
 const values=parts.map(Number);
 if(isCounts)return values.every(x=>Number.isSafeInteger(x)&&x>=0&&x<=10000000)?values:null;
 return values.every(x=>Number.isFinite(x)&&x>0&&x<=1)?values:null;
}
const NS="http://www.w3.org/2000/svg";
function node(name,attrs,text){
 const el=document.createElementNS(NS,name);
 for(const [a,v] of Object.entries(attrs||{}))el.setAttribute(a,String(v));
 if(text!==undefined)el.textContent=String(text);
 return el;
}
function plot(stats){
 const plot=get("chart"),max=Math.max(1,...stats.counts,...stats.expected),k=stats.counts.length;
 const width=540,margin=48,usable=width-2*margin,slot=usable/k,scale=148/max;
 plot.replaceChildren(node("title",{},"Observed versus expected categorical counts"),
  node("desc",{},"For each category the first bar shows the observed count and the second shows the expected count under the null."),
  node("line",{x1:margin,y1:175,x2:width-margin,y2:175,stroke:"currentColor"}),
  node("line",{x1:margin,y1:20,x2:margin,y2:175,stroke:"currentColor"}));
 for(let i=0;i<k;i++){
  const cx=margin+slot*(i+.5),bar=Math.max(3,Math.min(16,slot*.27));
  const obs=stats.counts[i],exp=stats.expected[i];
  plot.appendChild(node("rect",{x:cx-bar-2,y:175-obs*scale,width:bar,height:obs*scale,fill:"#0f766e"}));
  plot.appendChild(node("rect",{x:cx+2,y:175-exp*scale,width:bar,height:exp*scale,fill:"#64748b"}));
  plot.appendChild(node("text",{x:cx,y:193,"text-anchor":"middle",fill:"currentColor","font-size":"10"},"C"+(i+1)));
 }
 plot.setAttribute("aria-label","Observed versus expected counts: "+
  stats.counts.map((v,i)=>"category "+(i+1)+" observed "+v+" expected "+stats.expected[i].toFixed(3)).join("; "));
}
function render(){
 const a=parse(counts.value,true),b=parse(probs.value,false);
 if(a===null||b===null){
  error.textContent="Enter matching lists of 2–12 categories: nonnegative whole-number counts and strictly positive probabilities.";error.hidden=false;results.hidden=true;get("chart").replaceChildren();return;
 }
 if(a.length!==b.length){
  error.textContent="Observed counts and null probabilities must contain the same number of categories.";error.hidden=false;results.hidden=true;get("chart").replaceChildren();return;
 }
 const sum=b.reduce((s,v)=>s+v,0);
 if(Math.abs(sum-1)>1e-8){
  error.textContent="Null probabilities must sum to 1 (current sum: "+sum.toFixed(6)+").";error.hidden=false;results.hidden=true;get("chart").replaceChildren();return;
 }
 const result=compute(a,b);
 if(!result){
  error.textContent="The total count must be positive. Use strictly positive pre-specified null probabilities.";error.hidden=false;results.hidden=true;get("chart").replaceChildren();return;
 }
 error.hidden=true;results.hidden=false;
 get("table").replaceChildren(...result.counts.map((o,i)=>{
  const tr=document.createElement("tr");
  for(const text of ["Category "+(i+1),String(o),result.probs[i].toFixed(6),fmt(result.expected[i]),fmt(result.terms[i])]){
   const cell=document.createElement("td");cell.textContent=text;tr.appendChild(cell);
  }
  return tr;
 }));
 get("chi").textContent=fmt(result.statistic);
 get("df").textContent=String(result.df);get("p").textContent=fmt(result.p);
 get("n").textContent=String(result.n);
 get("warning").textContent=result.smallExpected?
  "Warning: at least one expected count is below 5. The asymptotic chi-square approximation may be unreliable; consider an appropriate exact multinomial method or gather more data.":
  "All expected counts are at least 5. The chi-square approximation is still asymptotic and requires independent categorical observations.";
 get("decision").textContent=result.p<.05?
  "At α=0.05 reject the pre-specified null distribution, conditional on test assumptions. This does not establish causality.":
  "At α=0.05 do not reject the pre-specified null distribution. This does not prove the model is true.";
 plot(result);
}
counts.addEventListener("input",render);probs.addEventListener("input",render);
get("reset").addEventListener("click",()=>{counts.value="8, 11, 9, 13, 10, 9";probs.value="1/6, 1/6, 1/6, 1/6, 1/6, 1/6";render()});
// Probabilities are decimal inputs to prevent silently evaluating arbitrary user input.
// Display the fair-die preset as exact decimal fractions summing numerically to 1.
get("die").addEventListener("click",()=>{
 counts.value="8, 11, 9, 13, 10, 9";
 probs.value="0.1666666667, 0.1666666667, 0.1666666667, 0.1666666667, 0.1666666667, 0.1666666665";
 render();
});
get("uneven").addEventListener("click",()=>{
 counts.value="12, 18, 30";probs.value="0.2, 0.3, 0.5";render();
});
render();
})();