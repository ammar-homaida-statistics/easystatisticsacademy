/* Batch #69: Welch independent two-sample inference. No third-party dependencies. */
(function(){
"use strict";
const root=document.getElementById("esa-welch-lab");if(!root)return;
const get=id=>root.querySelector("#esa-w-"+id);
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

const pattern=/^[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:e[+-]?\d+)?$/i;
function parseNumbers(text){
 // A missing comma-delimited observation must not silently disappear.
 if(/,\s*,|^\s*,|,\s*$/.test(text))return null;
 const parts=text.trim().split(/[\s,;]+/).filter(Boolean);
 if(parts.length<2||parts.length>40||parts.some(x=>!pattern.test(x)))return null;
 const nums=parts.map(Number);
 return nums.every(n=>Number.isFinite(n)&&Math.abs(n)<=1e6)?nums:null;
}
function summarize(values){
 if(!Array.isArray(values)||values.length<2||values.length>40||
    values.some(v=>!Number.isFinite(v)||Math.abs(v)>1e6))return null;
 const n=values.length, mean=values.reduce((a,b)=>a+b,0)/n;
 const variance=values.reduce((a,v)=>a+(v-mean)**2,0)/(n-1);
 return {n,mean,sd:Math.sqrt(variance),variance};
}
function compute(a,b,alternative="two-sided",nullDifference=0){
 if(!["two-sided","greater","less"].includes(alternative)||
    !Number.isFinite(nullDifference)||Math.abs(nullDifference)>1e6)return null;
 const g1=summarize(a),g2=summarize(b);
 if(!g1||!g2)return null;
 const v1=g1.variance/g1.n,v2=g2.variance/g2.n,total=v1+v2;
 if(!(total>0)||!Number.isFinite(total))return {degenerate:true,g1,g2};
 const se=Math.sqrt(total);
 const divisor=v1*v1/(g1.n-1)+v2*v2/(g2.n-1);
 const df=total*total/divisor;
 if(!(df>0)||!Number.isFinite(df))return null;
 const difference=g1.mean-g2.mean;
 const t=(difference-nullDifference)/se;
 const tail=studentUpperTail(t,df);
 const p=alternative==="two-sided"?Math.min(1,2*Math.min(tail,1-tail)):
   alternative==="greater"?tail:1-tail;
 const critical=critical95(df),half=critical*se;
 const lower=difference-half,upper=difference+half;
 if([t,p,critical,lower,upper].some(v=>!Number.isFinite(v)))return null;
 return {g1,g2,difference,se,df,t,p,critical,lower,upper,degenerate:false,alternative,nullDifference};
}
window.esaWelchMath={compute,studentUpperTail,critical95,regularizedBeta};
const aInput=get("a"),bInput=get("b"),alt=get("alternative"),nullInput=get("null"),
  error=get("error"),results=get("results");
const format=x=>Number.isFinite(x)?x.toFixed(6):"—";
function draw(stats){
 const plot=get("plot");
 const ns="http://www.w3.org/2000/svg";
 const svg=(tag,attrs,content)=>{
  const node=document.createElementNS(ns,tag);
  Object.entries(attrs).forEach(([k,v])=>node.setAttribute(k,String(v)));
  if(content!==undefined)node.textContent=String(content);
  return node;
 };
 const bound=Math.max(1,Math.abs(stats.difference),Math.abs(stats.lower),Math.abs(stats.upper));
 const range=bound*1.15;
 const xpos=x=>310+270*x/range;
 plot.replaceChildren(svg("title",{},"Welch two-sided 95 percent confidence interval for group mean difference"),
   svg("desc",{},"Zero reference, confidence interval endpoints, and sample mean difference, all in units of group A minus group B."),
   svg("line",{x1:32,x2:588,y1:102,y2:102,stroke:"currentColor"}),
   svg("line",{x1:xpos(0),x2:xpos(0),y1:20,y2:131,stroke:"#64748b","stroke-dasharray":"4 4"}),
   svg("line",{x1:xpos(stats.lower),x2:xpos(stats.upper),y1:72,y2:72,stroke:"#0d9488","stroke-width":6}),
   svg("circle",{cx:xpos(stats.lower),cy:72,r:5,fill:"#0d9488"}),
   svg("circle",{cx:xpos(stats.upper),cy:72,r:5,fill:"#0d9488"}),
   svg("circle",{cx:xpos(stats.difference),cy:72,r:7,fill:"#64748b"}),
   svg("text",{x:xpos(0),y:146,"text-anchor":"middle",fill:"currentColor","font-size":13},"0"),
   svg("text",{x:310,y:18,"text-anchor":"middle",fill:"currentColor","font-size":14},"Difference = "+format(stats.difference)),
   svg("text",{x:32,y:166,fill:"currentColor","font-size":12},format(-range)),
   svg("text",{x:588,y:166,"text-anchor":"end",fill:"currentColor","font-size":12},format(range)));
 plot.setAttribute("aria-label","95% confidence interval from "+format(stats.lower)+" to "+format(stats.upper)+
  " for group A minus group B; observed difference "+format(stats.difference)+". Zero is marked.");
}
function update(){
 const a=parseNumbers(aInput.value),b=parseNumbers(bInput.value),
       nullDiff=nullInput.value.trim()===""?NaN:Number(nullInput.value);
 const stats=a&&b?compute(a,b,alt.value,nullDiff):null;
 if(!stats||stats.degenerate){
  error.textContent=stats&&stats.degenerate?
   "The standard error is zero because neither group varies; the usual Welch t inference is undefined.":
   "Enter 2–40 finite numbers (absolute value ≤ 1,000,000) per independent group, separated by commas, spaces or new lines, and a valid null difference.";
  error.hidden=false;results.hidden=true;return;
 }
 error.hidden=true;error.textContent="";results.hidden=false;
 const values={n1:stats.g1.n,n2:stats.g2.n,mean1:stats.g1.mean,mean2:stats.g2.mean,
  sd1:stats.g1.sd,sd2:stats.g2.sd,difference:stats.difference,se:stats.se,
  t:stats.t,df:stats.df,p:stats.p,critical:stats.critical,lower:stats.lower,upper:stats.upper};
 Object.entries(values).forEach(([k,v])=>get(k).textContent=["n1","n2"].includes(k)?String(v):format(v));
 get("conclusion").textContent=(stats.p<.05?"Reject":"Do not reject")+
  " H₀ at α = 0.05 (subject to assumptions). A p-value does not measure effect magnitude or prove causation.";
 get("interpret").textContent="The two-sided 95% interval estimates μ₁−μ₂, not a prediction interval for individual observations. "+
   (stats.lower>0||stats.upper<0?"This interval excludes zero.":"This interval includes zero.")+
   " One-sided alternatives change the p-value, not the reported two-sided interval.";
 draw(stats);
}
[aInput,bInput,alt,nullInput].forEach(x=>{
 x.addEventListener("input",update);x.addEventListener("change",update);
});
get("reset").addEventListener("click",()=>{
 aInput.value="73, 77, 80, 78, 82, 79, 84";
 bInput.value="70, 68, 74, 71, 75, 69";
 alt.value="two-sided";nullInput.value="0";update();
});
get("reverse").addEventListener("click",()=>{const tmp=aInput.value;aInput.value=bInput.value;bInput.value=tmp;update();});
update();
})();
