/* Batch #91: conditional Fisher exact 2x2 versus Pearson chi-square; Batch #97 adds Yates and an accurate erfc.
   Two-sided Fisher follows probability ordering, as SciPy fisher_exact. */
(function(){
"use strict";
// Batch #97: accurate erfc (Taylor series below 2.5, Lentz continued fraction
// above). The previous 5-term approximation had absolute error up to 1.4e-7
// and relative error up to 0.44% in the far tail.
function erfc(x){
 if(x<0)return 2-erfc(-x);
 if(x<2.5){let sum=x,term=x;const x2=x*x;
  for(let n=1;n<200;n++){term*=-x2/n;const add=term/(2*n+1);sum+=add;if(Math.abs(add)<1e-17*Math.abs(sum))break;}
  return 1-2/Math.sqrt(Math.PI)*sum;}
 const TINY=1e-300;let f=x,C=x,D=0;
 for(let n=1;n<500;n++){const a=n/2;D=x+a*D;if(Math.abs(D)<TINY)D=TINY;C=x+a/C;if(Math.abs(C)<TINY)C=TINY;
  D=1/D;const delta=C*D;f*=delta;if(Math.abs(delta-1)<1e-16)break;}
 return Math.exp(-x*x)/Math.sqrt(Math.PI)/f;
}
function compute(a,b,c,d,side="two-sided"){
 const cells=[a,b,c,d];
 if(cells.some(x=>!Number.isSafeInteger(x)||x<0)||!["two-sided","greater","less"].includes(side))return null;
 const N=a+b+c+d,r1=a+b,r2=c+d,c1=a+c,c2=b+d;
 if(!(N>0&&N<=2000)||!r1||!r2||!c1||!c2)return null;
 const expected=[r1*c1/N,r1*c2/N,r2*c1/N,r2*c2/N];
 const chi=cells.reduce((s,o,i)=>s+(o-expected[i])**2/expected[i],0);
 const chiP=chi===0?1:Math.max(0,Math.min(1,erfc(Math.sqrt(chi/2))));
 // Yates continuity correction, as SciPy chi2_contingency(correction=True):
 // each |O - E| is reduced by min(0.5, |O - E|).
 const yates=cells.reduce((s,o,i)=>s+Math.max(0,Math.abs(o-expected[i])-.5)**2/expected[i],0);
 const yatesP=yates===0?1:Math.max(0,Math.min(1,erfc(Math.sqrt(yates/2))));
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
 return {a,b,c,d,N,r1,r2,c1,c2,expected,chi,chiP,yates,yatesP,fisher,side,small:expected.filter(x=>x<5).length,lo,hi};
}
window.esaFisherChiMath={compute};
const root=document.getElementById("esa-fisher-chi-lab");if(!root)return;
const AR=root.dataset.locale==="ar";
const T=AR?{
 error:"أدخل أربعة أعداد صحيحة غير سالبة، بحيث يكون مجموع كل صف وكل عمود موجبًا، والحجم الكلي N بين 1 و2000.",
 small:n=>n+" من أصل أربعة تكرارات متوقعة أقل من 5؛ وقد يكون تقريب بيرسون للعينات الكبيرة غير موثوق.",
 ok:"جميع التكرارات المتوقعة 5 أو أكثر؛ ومع ذلك تبقى افتراضات الاستقلال والمعاينة مهمة.",
 meaning:"يشترط فيشر على المجموعين الهامشيين معًا؛ وتجمع القيمة الاحتمالية الثنائية احتمالات الجداول التي لا يزيد احتمالها على احتمال الجدول المشاهد. يستخدم بيرسون توزيع χ² بدرجة حرية واحدة، مع تصحيح ييتس ودونه. يتطلب الاستدلال الشرطي الدقيق نموذج معاينة مستقلة مناسبًا، ولا يثبت أيّ الاختبارين السببية.",
 title:"القيم الاحتمالية لاختبار فيشر الدقيق واختبار كاي تربيع لبيرسون",
 fisher:"فيشر",pearson:"بيرسون",
 aria:(f,p)=>"القيمة الاحتمالية لفيشر "+f+"؛ القيمة الاحتمالية لبيرسون "+p
}:{
 error:"Enter four non-negative whole-number counts, each row and column total positive, and overall N between 1 and 2000.",
 small:n=>n+" of four expected cell counts are below 5; Pearson's large-sample approximation can be unreliable.",
 ok:"All expected cell counts are at least 5; independence and sampling assumptions still matter.",
 meaning:"Fisher conditions on both margins; the two-sided p-value sums tables no more probable than the observed table. Pearson uses χ² with 1 df, shown without and with Yates' continuity correction. Exact conditional inference requires an appropriate independent sampling model; neither test establishes causation.",
 title:"Conditional Fisher exact and Pearson chi-square p-values",
 fisher:"Fisher",pearson:"Pearson",
 aria:(f,p)=>"Fisher exact p-value "+f+"; Pearson chi-square p-value "+p
};
const $=x=>root.querySelector("#esa-fc-"+x),fields=["a","b","c","d"].map($),side=$("side"),
 error=$("error"),results=$("results");
const fmt=x=>x<.0000005&&x>0?x.toExponential(4):x.toFixed(6);
function update(){
 const nums=fields.map(e=>/^\d+$/.test(e.value.trim())?Number(e.value.trim()):NaN);
 const r=compute(...nums,side.value);
 fields.forEach(e=>e.setAttribute("aria-invalid",r?"false":"true"));
 if(!r){error.hidden=false;results.hidden=true;error.textContent=T.error;return;}
 error.hidden=true;error.textContent="";results.hidden=false;
 $("fisher").textContent=fmt(r.fisher);$("pearson").textContent=fmt(r.chiP);
 if($("yates"))$("yates").textContent=fmt(r.yatesP);
 $("chi").textContent=r.chi.toFixed(6);$("N").textContent=String(r.N);
 ["a","b","c","d"].forEach((name,i)=>$(name+"expected").textContent=r.expected[i].toFixed(3));
 $("warning").textContent=r.small?
  T.small(r.small):T.ok;
 $("meaning").textContent=T.meaning;
 const plot=$("plot"),ns="http://www.w3.org/2000/svg";plot.replaceChildren();
 function el(tag,attrs,label){const e=document.createElementNS(ns,tag);for(const [k,v]of Object.entries(attrs))e.setAttribute(k,String(v));if(label!==undefined)e.textContent=label;plot.append(e);}
 el("title",{},T.title);
 for(const [i,label,value,color]of [[0,T.fisher,r.fisher,"#0f766e"],[1,T.pearson,r.chiP,"#2563eb"]]){
  const y=18+i*52;el("text",{x:5,y:y+16,fill:"currentColor","font-size":13},label);
  el("rect",{x:110,y:y,width:Math.max(0,375*value),height:20,fill:color});
  el("text",{x:495,y:y+15,fill:"currentColor","font-size":12},fmt(value));
 }
 el("line",{x1:110+375*.05,x2:110+375*.05,y1:3,y2:118,stroke:"currentColor","stroke-dasharray":"3 3"});
 plot.setAttribute("aria-label",T.aria(fmt(r.fisher),fmt(r.chiP)));
}
[...fields,side].forEach(e=>{e.addEventListener("input",update);e.addEventListener("change",update)});
$("reset").addEventListener("click",()=>{[1,9,11,3].forEach((x,i)=>fields[i].value=x);side.value="two-sided";update();});
update();
})();