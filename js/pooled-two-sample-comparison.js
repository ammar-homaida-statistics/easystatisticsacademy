/* Batch #88 — pooled equal-variance t comparison against the existing Welch engine. */
(function(){
"use strict";
function compute(a,b,alternative="two-sided",nullDifference=0){
 const welch=window.esaWelchMath;
 if(!welch||typeof welch.compute!=="function")return null;
 const reference=welch.compute(a,b,alternative,nullDifference);
 if(!reference)return null;
 const g1=reference.g1,g2=reference.g2;
 if(!g1||!g2)return null;
 const df=g1.n+g2.n-2;
 const pooledVariance=((g1.n-1)*g1.variance+(g2.n-1)*g2.variance)/df;
 const se=Math.sqrt(pooledVariance*(1/g1.n+1/g2.n));
 if(!(pooledVariance>0)||!(se>0)||!Number.isFinite(se))return {degenerate:true,df};
 const difference=g1.mean-g2.mean;
 const t=(difference-nullDifference)/se;
 if(!Number.isFinite(t))return null;
 const upper=welch.studentUpperTail(t,df);
 const p=alternative==="two-sided"?Math.min(1,2*Math.min(upper,1-upper)):
    alternative==="greater"?upper:1-upper;
 const critical=welch.critical95(df),margin=critical*se;
 if([p,critical,margin].some(x=>!Number.isFinite(x)))return null;
 return {difference,t,p,df,se,critical,lower:difference-margin,upper:difference+margin,
         pooledVariance,welch:reference,degenerate:false};
}
window.esaPooledTMath={compute};
const root=document.getElementById("esa-welch-lab");
if(!root)return;
const ar=root.dataset.locale==="ar";
const $=id=>root.querySelector("#esa-w-"+id);
const a=$("a"),b=$("b"),alt=$("alternative"),nullInput=$("null");
const outputs=$("pool-results"),note=$("pool-warning"),plot=$("pool-plot");
const numPattern=/^[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:e[+-]?\d+)?$/i;
function parse(str){
 if(/,\s*,|^\s*,|,\s*$/.test(str))return null;
 const pieces=str.trim().split(/[\s,;]+/).filter(Boolean);
 if(pieces.length<2||pieces.length>40||pieces.some(x=>!numPattern.test(x)))return null;
 const nums=pieces.map(Number);
 return nums.every(x=>Number.isFinite(x)&&Math.abs(x)<=1e6)?nums:null;
}
const fmt=n=>Number.isFinite(n)?n.toFixed(6):"—";
function render(){
 const aVals=parse(a.value),bVals=parse(b.value);
 const raw=nullInput.value.trim(),delta=raw!==""&&numPattern.test(raw)?Number(raw):NaN;
 const data=aVals&&bVals?compute(aVals,bVals,alt.value,delta):null;
 if(!data||data.degenerate){outputs.hidden=true;plot.replaceChildren();return;}
 outputs.hidden=false;
 for(const [id,val] of Object.entries({se:data.se,df:data.df,t:data.t,p:data.p,
       critical:data.critical,lower:data.lower,upper:data.upper}))
   $("pool-"+id).textContent=fmt(val);
 const welch=data.welch;
 const unequal= Math.max(welch.g1.variance,welch.g2.variance)/
     Math.max(1e-15,Math.min(welch.g1.variance,welch.g2.variance));
 note.textContent=ar?"يفترض اختبار التباين المشترك تساوي تباينَي المجتمعين. "+(unequal>4?"نسبة تباينَي العينتين أكبر من 4. ":"تقارب تباينَي العينتين لا يثبت تساوي تباينَي المجتمعين. ")+"لا يتطلب اختبار ويلش افتراض التساوي، ويُفضَّل كخيار عام. يلزم الاستقلال وتقييم الافتراضات التوزيعية.":"Pooled inference assumes equal population variances. "+
  (unequal>4?"Observed sample variances differ substantially (ratio >4). ":
   "Sample variances alone cannot establish or rule out equal population variances. ")+
  "Welch avoids the equal-variance assumption; prefer it as a general default. "+
  "Both approaches assume independent groups and suitable distributional conditions.";
 plot.replaceChildren();
 const ns="http://www.w3.org/2000/svg";
 const max=Math.max(1,...[welch.lower,welch.upper,data.lower,data.upper].map(Math.abs));
 const x=v=>85+430*(v+max*1.15)/(2*max*1.15);
 function el(tag,attrs,text){const z=document.createElementNS(ns,tag);
  Object.entries(attrs).forEach(([k,v])=>z.setAttribute(k,String(v)));
  if(text!==undefined)z.textContent=String(text);plot.append(z);}
 el("line",{x1:x(0),x2:x(0),y1:9,y2:122,stroke:"currentColor","stroke-dasharray":"4 4"});
 [[welch.lower,welch.upper],[data.lower,data.upper]].forEach((bounds,i)=>{
   const y=39+57*i,color=i?"#2563eb":"#0f766e";
   el("text",{x:8,y:y+4,fill:"currentColor","font-size":13},i?(ar?"مشترك":"Pooled"):(ar?"ويلش":"Welch"));
   el("line",{x1:x(bounds[0]),x2:x(bounds[1]),y1:y,y2:y,stroke:color,"stroke-width":5});
   for(const bound of bounds)el("circle",{cx:x(bound),cy:y,r:4,fill:color});
 });
 plot.setAttribute("aria-label",ar?"فترتا الثقة الثنائيتان 95% لفرق المتوسطين أ ناقص ب. ويلش من "+fmt(welch.lower)+" إلى "+fmt(welch.upper)+"؛ التباين المشترك من "+fmt(data.lower)+" إلى "+fmt(data.upper)+".":"Two-sided 95% confidence intervals for independent mean difference A minus B. Welch "+fmt(welch.lower)+" to "+fmt(welch.upper)+"; pooled "+fmt(data.lower)+" to "+fmt(data.upper)+".");
}
[a,b,alt,nullInput].forEach(field=>{field.addEventListener("input",render);field.addEventListener("change",render);});
for(const id of ["reset","reverse"])$(""+id).addEventListener("click",()=>queueMicrotask(render));
render();
})();