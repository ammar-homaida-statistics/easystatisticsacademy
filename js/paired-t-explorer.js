/* Batch #68 — Paired t inference. Student t tails use regularized incomplete
   beta; no external libraries, no data persistence, and no untrusted HTML. */
(function(){
"use strict";
const root=document.getElementById("esa-paired-t-lab");
if(!root)return;
const get=id=>root.querySelector("#esa-pt-"+id);
const coefficients=[.99999999999980993,676.5203681218851,-1259.1392167224028,
  771.32342877765313,-176.61502916214059,12.507343278686905,
 -.13857109526572012,9.984369578019572e-6,1.5056327351493116e-7];
function logGamma(z){
 if(!(z>0)||!Number.isFinite(z))return NaN;
 if(z<.5)return Math.log(Math.PI)-Math.log(Math.sin(Math.PI*z))-logGamma(1-z);
 z-=1;let a=coefficients[0];for(let i=1;i<coefficients.length;i++)a+=coefficients[i]/(z+i);
 let t=z+7.5;return Math.log(2*Math.PI)/2+(z+.5)*Math.log(t)-t+Math.log(a);
}
function continuedFraction(a,b,x){
 // Modified Lentz algorithm for the incomplete-beta continued fraction.
 const tiny=1e-300,eps=2e-14;
 let qab=a+b,qap=a+1,qam=a-1,c=1,d=1-qab*x/qap;
 if(Math.abs(d)<tiny)d=tiny;
 d=1/d;let h=d;
 for(let m=1;m<=400;m++){
  const m2=2*m;
  let aa=m*(b-m)*x/((qam+m2)*(a+m2));
  d=1+aa*d;if(Math.abs(d)<tiny)d=tiny;
  c=1+aa/c;if(Math.abs(c)<tiny)c=tiny;
  d=1/d;h*=d*c;
  aa=-(a+m)*(qab+m)*x/((a+m2)*(qap+m2));
  d=1+aa*d;if(Math.abs(d)<tiny)d=tiny;
  c=1+aa/c;if(Math.abs(c)<tiny)c=tiny;
  d=1/d;const delta=d*c;h*=delta;
  if(Math.abs(delta-1)<eps)break;
 }
 return h;
}
function regularizedBeta(x,a,b){
 if(!(a>0&&b>0)||!Number.isFinite(x)||x<0||x>1)return NaN;
 if(x===0)return 0;if(x===1)return 1;
 const front=Math.exp(logGamma(a+b)-logGamma(a)-logGamma(b)+
   a*Math.log(x)+b*Math.log1p(-x));
 const value=x<(a+1)/(a+b+2)?
    front*continuedFraction(a,b,x)/a:
    1-front*continuedFraction(b,a,1-x)/b;
 return Math.max(0,Math.min(1,value));
}
function studentUpperTail(t,df){
 if(!Number.isFinite(t)||!(df>0))return NaN;
 if(t===0)return .5;
 const x=df/(df+t*t);
 const half=regularizedBeta(x,df/2,.5)/2;
 return t>0?half:1-half;
}
function critical95(df){
 let lo=0,hi=16;
 while(studentUpperTail(hi,df)>.025&&hi<1e8)hi*=2;
 for(let i=0;i<90;i++){
  const mid=(lo+hi)/2;
  if(studentUpperTail(mid,df)>.025)lo=mid;else hi=mid;
 }
 return (lo+hi)/2;
}
function compute(pairs,alternative="two-sided",nullMean=0){
 if(!Array.isArray(pairs)||pairs.length<2||pairs.length>40||
    !["two-sided","greater","less"].includes(alternative)||
    !Number.isFinite(nullMean)||Math.abs(nullMean)>1e6)return null;
 if(pairs.some(row=>!Array.isArray(row)||row.length!==2||
    row.some(v=>!Number.isFinite(v)||Math.abs(v)>1e6)))return null;
 const n=pairs.length,diffs=pairs.map(([before,after])=>after-before);
 const mean=diffs.reduce((a,b)=>a+b,0)/n;
 const ss=diffs.reduce((s,d)=>s+(d-mean)**2,0);
 const sd=Math.sqrt(ss/(n-1)),se=sd/Math.sqrt(n),df=n-1;
 if(!(sd>0)&&Number.isFinite(sd))return {degenerate:true,n,diffs,mean,df};
 if(!Number.isFinite(sd)||!Number.isFinite(se)||!(se>0))return null;
 const t=(mean-nullMean)/se,tail=studentUpperTail(t,df);
 const p=alternative==="two-sided"?Math.min(1,2*Math.min(tail,1-tail)):
         alternative==="greater"?tail:1-tail;
 const c=critical95(df),half=c*se;
 return {n,pairs,diffs,mean,sd,se,t,df,p,critical:c,lower:mean-half,upper:mean+half,
   alternative,nullMean,degenerate:false};
}
window.esaPairedTMath={compute,studentUpperTail,critical95,regularizedBeta};
const input=get("input"),alternative=get("alternative"),hypothesis=get("null"),
      results=get("results"),error=get("error");
const numberPattern=/^[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:e[+-]?\d+)?$/i;
function parse(text){
 const lines=text.trim().split(/\r?\n|;/).map(x=>x.trim()).filter(Boolean);
 if(lines.length<2||lines.length>40)return null;
 const matrix=lines.map(s=>s.split(",").map(x=>x.trim()));
 if(matrix.some(row=>row.length!==2||row.some(x=>!numberPattern.test(x))))return null;
 const values=matrix.map(row=>row.map(Number));
 return values.every(row=>row.every(v=>Number.isFinite(v)&&Math.abs(v)<=1e6))?values:null;
}
const svgNS="http://www.w3.org/2000/svg";
function element(name,attributes,txt){
 const e=document.createElementNS(svgNS,name);
 for(const [a,v] of Object.entries(attributes||{}))e.setAttribute(a,String(v));
 if(txt!==undefined)e.textContent=String(txt);
 return e;
}
function plot(stats){
 const svg=get("plot");
 svg.replaceChildren(element("title",{},"Before and after observations in matched pairs"),
  element("desc",{},"Each horizontal segment joins a before observation in grey with the matched after observation in teal."));
 const show=stats.pairs.slice(0,16),flat=show.flat();
 let min=Math.min(...flat),max=Math.max(...flat);
 const padding=Math.max(1,(max-min)*.08);
 min-=padding;max+=padding;
 const xpos=x=>40+535*(x-min)/(max-min);
 svg.setAttribute("viewBox","0 0 620 "+(show.length*25+50));
 svg.appendChild(element("line",{x1:40,y1:show.length*25+24,x2:575,y2:show.length*25+24,stroke:"currentColor"}));
 show.forEach(([before,after],i)=>{
  const y=24+i*25;
  svg.appendChild(element("text",{x:27,y:y+4,"text-anchor":"end",fill:"currentColor","font-size":11},String(i+1)));
  svg.appendChild(element("line",{x1:xpos(before),x2:xpos(after),y1:y,y2:y,stroke:"#94a3b8","stroke-width":3}));
  svg.appendChild(element("circle",{cx:xpos(before),cy:y,r:4,fill:"#64748b"}));
  svg.appendChild(element("circle",{cx:xpos(after),cy:y,r:4,fill:"#0d9488"}));
 });
 svg.appendChild(element("text",{x:40,y:show.length*25+42,fill:"currentColor","font-size":11},min.toFixed(1)));
 svg.appendChild(element("text",{x:570,y:show.length*25+42,fill:"currentColor","text-anchor":"end","font-size":11},max.toFixed(1)));
 svg.setAttribute("aria-label","Matched before/after changes: "+
    stats.diffs.slice(0,16).map((d,i)=>"pair "+(i+1)+" change "+d.toFixed(2)).join("; ")+
    (stats.n>16?"; chart displays first 16 of "+stats.n+" pairs":""));
 get("plot-limit").textContent=stats.n>16?
    "Chart displays the first 16 of "+stats.n+" pairs; calculations use all pairs.":"";
}
const fmt=n=>Number.isFinite(n)?n.toFixed(6):"—";
function render(){
 const pairs=parse(input.value),nullMean=Number(hypothesis.value);
 const validNull=hypothesis.value.trim()!==""&&numberPattern.test(hypothesis.value.trim())&&
  Number.isFinite(nullMean)&&Math.abs(nullMean)<=1e6;
 const x=pairs&&validNull?compute(pairs,alternative.value,nullMean):null;
 if(!x||x.degenerate){
   results.hidden=true;error.hidden=false;get("plot").replaceChildren();
   error.textContent=x&&x.degenerate?
     "Every observed within-pair difference is identical, so the sample difference variance is zero. The conventional t-statistic, p-value and t-interval are not defined; do not interpret a divided-by-zero result.":
     "Provide 2–40 complete matched pairs, each as two finite numbers 'before, after' separated by a comma, and a finite hypothesized mean difference. Missing, mismatched, invalid or extremely large observations are not accepted.";
   return;
 }
 error.hidden=true;results.hidden=false;
 const tbody=get("table");tbody.replaceChildren();
 x.pairs.forEach(([before,after],i)=>{
   const tr=document.createElement("tr");
   for(const val of [String(i+1),fmt(before),fmt(after),fmt(x.diffs[i])]){
     const td=document.createElement("td");td.textContent=val;tr.appendChild(td);
   }
   tbody.appendChild(tr);
 });
 for(const [key,value] of Object.entries({n:String(x.n),mean:fmt(x.mean),
  sd:fmt(x.sd),se:fmt(x.se),t:fmt(x.t),df:String(x.df),p:fmt(x.p),
  critical:fmt(x.critical),lower:fmt(x.lower),upper:fmt(x.upper)})){
  get(key).textContent=value;
 }
 get("conclusion").textContent=x.p<.05?
  "At the 5% significance level, reject the specified null if assumptions hold. The sign of the difference follows after minus before.":
  "At the 5% significance level, do not reject the specified null. This does not establish that the mean difference equals the null value.";
 get("interpret").textContent=
   "Two-sided 95% t confidence interval for the population mean paired difference: ["+
   fmt(x.lower)+", "+fmt(x.upper)+"]. The interval uses df = n − 1 and is distinct from a one-sided test. "+
   "The result assumes independent pairs and approximately normally distributed population differences, particularly with small n.";
 plot(x);
}
input.addEventListener("input",render);
alternative.addEventListener("change",render);
hypothesis.addEventListener("input",render);
get("reset").addEventListener("click",()=>{
 input.value="70,75\n68,72\n75,79\n71,74\n69,74";
 hypothesis.value="0";alternative.value="two-sided";render();
});
get("negative").addEventListener("click",()=>{
 input.value="75,70\n72,68\n79,75\n74,71\n74,69";
 hypothesis.value="0";alternative.value="two-sided";render();
});
render();
})();