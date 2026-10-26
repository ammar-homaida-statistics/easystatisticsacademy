/* Batch #72: Student t inference via regularized incomplete beta, not a normal approximation. */
(function(){
"use strict";
const root=document.getElementById("esa-student-t-lab");if(!root)return;
const el=id=>root.querySelector("#esa-st-"+id);
const coefficients=[0.99999999999980993,676.5203681218851,-1259.1392167224028,
771.32342877765313,-176.61502916214059,12.507343278686905,
-0.13857109526572012,9.9843695780195716e-6,1.5056327351493116e-7];
function logGamma(z){
 if(z<0.5)return Math.log(Math.PI)-Math.log(Math.sin(Math.PI*z))-logGamma(1-z);
 z-=1;let x=coefficients[0];
 for(let i=1;i<coefficients.length;i++)x+=coefficients[i]/(z+i);
 const t=z+7.5;
 return 0.5*Math.log(2*Math.PI)+(z+0.5)*Math.log(t)-t+Math.log(x);
}
function betaFraction(a,b,x){
 const tiny=1e-300,eps=3e-14;
 let qab=a+b,qap=a+1,qam=a-1,c=1,d=1-qab*x/qap;
 if(Math.abs(d)<tiny)d=tiny;
 d=1/d;let h=d;
 for(let m=1;m<=320;m++){
  const m2=2*m;
  let aa=m*(b-m)*x/((qam+m2)*(a+m2));
  d=1+aa*d;if(Math.abs(d)<tiny)d=tiny;
  c=1+aa/c;if(Math.abs(c)<tiny)c=tiny;
  d=1/d;h*=d*c;
  aa=-(a+m)*(qab+m)*x/((a+m2)*(qap+m2));
  d=1+aa*d;if(Math.abs(d)<tiny)d=tiny;
  c=1+aa/c;if(Math.abs(c)<tiny)c=tiny;
  d=1/d;const delta=d*c;h*=delta;
  if(Math.abs(delta-1)<eps)return h;
 }
 return h;
}
function regBeta(x,a,b){
 if(x<=0)return 0;if(x>=1)return 1;
 const front=Math.exp(logGamma(a+b)-logGamma(a)-logGamma(b)+a*Math.log(x)+b*Math.log1p(-x));
 if(x<(a+1)/(a+b+2))return Math.min(1,Math.max(0,front*betaFraction(a,b,x)/a));
 return Math.min(1,Math.max(0,1-front*betaFraction(b,a,1-x)/b));
}
function tSurvivalAbs(t,df){
 if(t===Infinity)return 0;
 if(t===0)return 0.5;
 return Math.max(0,Math.min(0.5,0.5*regBeta(df/(df+t*t),df/2,0.5)));
}
function tQuantile975(df){
 let low=0,high=1;
 while(tSurvivalAbs(high,df)>.025&&high<1e10)high*=2;
 for(let i=0;i<72;i++){
  const mid=(low+high)/2;
  if(tSurvivalAbs(mid,df)>.025)low=mid;else high=mid;
 }
 return (low+high)/2;
}
function compute(n,mean,sd,mu0,alternative="two-sided"){
 if(!Number.isSafeInteger(n)||n<2||n>1000000||!Number.isFinite(mean)||
    !Number.isFinite(mu0)||!Number.isFinite(sd)||sd<=0||sd>1e9||
    Math.abs(mean)>1e9||Math.abs(mu0)>1e9||
    !["two-sided","greater","less"].includes(alternative))return null;
 const df=n-1,se=sd/Math.sqrt(n),t=(mean-mu0)/se;
 if(!Number.isFinite(t))return null;
 const sf=tSurvivalAbs(Math.abs(t),df);
 const upper=t>=0?sf:1-sf,lower=t>=0?1-sf:sf;
 const pvalue=alternative==="two-sided"?Math.min(1,2*sf):
  alternative==="greater"?upper:lower;
 const critical=tQuantile975(df),margin=critical*se;
 return {n,mean,sd,mu0,alternative,df,se,t,pvalue,critical,
  lower:mean-margin,upper:mean+margin};
}
window.esaStudentTMath={compute,regBeta,tSurvivalAbs,tQuantile975};
const fmt=x=>x.toFixed(6);
const svgNS="http://www.w3.org/2000/svg";
function elem(tag,attrs={},text){
 const e=document.createElementNS(svgNS,tag);
 for(const [k,v] of Object.entries(attrs))e.setAttribute(k,String(v));
 if(text!==undefined)e.textContent=String(text);
 return e;
}
function density(t,df){
 return Math.exp(logGamma((df+1)/2)-logGamma(df/2)-
  0.5*Math.log(df*Math.PI)-((df+1)/2)*Math.log1p(t*t/df));
}
function plot(v){
 const axis=el("plot"),limit=Math.min(18,Math.max(4.5,Math.abs(v.t)+1.1));
 const xscale=t=>38+540*(t+limit)/(2*limit),base=195;
 const peak=density(0,v.df),yscale=t=>base-155*density(t,v.df)/peak;
 const segments=[];
 const count=180,step=2*limit/count;
 for(let i=0;i<count;i++){
  const left=-limit+i*step,right=left+step,middle=(left+right)/2;
  const selected=v.alternative==="two-sided"?Math.abs(middle)>=Math.abs(v.t):
    v.alternative==="greater"?middle>=v.t:middle<=v.t;
  if(selected){
   const h=base-yscale(middle);
   segments.push(elem("rect",{x:xscale(left),y:base-h,width:Math.max(.2,xscale(right)-xscale(left)+.2),
     height:h,fill:"#0f766e",opacity:.42}));
  }
 }
 let path="";
 for(let i=0;i<=count;i++){
  const t=-limit+i*step;
  path+=(i?"L":"M")+xscale(t).toFixed(2)+","+yscale(t).toFixed(2);
 }
 axis.replaceChildren(
  elem("title",{},"Student t distribution with tail region for selected alternative"),
  elem("desc",{},"Shaded tails correspond to the displayed Student t-based p-value; dashed line marks the observed test statistic."),
  ...segments,
  elem("line",{x1:38,x2:578,y1:base,y2:base,stroke:"currentColor"}),
  elem("path",{d:path,fill:"none",stroke:"#2563eb","stroke-width":2.5}),
  elem("line",{x1:xscale(v.t),x2:xscale(v.t),y1:18,y2:base,stroke:"#b45309","stroke-width":2,"stroke-dasharray":"5 4"}),
  elem("text",{x:38,y:216,"font-size":13,fill:"currentColor"},(-limit).toFixed(1)),
  elem("text",{x:308,y:216,"font-size":13,fill:"currentColor","text-anchor":"middle"},"0"),
  elem("text",{x:578,y:216,"font-size":13,fill:"currentColor","text-anchor":"end"},limit.toFixed(1))
 );
 axis.setAttribute("aria-label","Student t distribution with "+v.df+" degrees of freedom. Observed t="+fmt(v.t)+
  ". "+v.alternative+" tail p-value "+fmt(v.pvalue)+".");
}
function render(){
 const raw=[el("n").value.trim(),el("mean").value.trim(),
  el("sd").value.trim(),el("mu0").value.trim()];
 const n=/^\d+$/.test(raw[0])?Number(raw[0]):NaN;
 const numeric=raw.slice(1).map(s=>s===""?NaN:Number(s));
 const v=compute(n,...numeric,el("alternative").value);
 const results=el("results"),error=el("error");
 if(!v){
  error.hidden=false;error.textContent="Enter n=2–1,000,000 (integer), finite sample and null means, and sample standard deviation s>0. Values of |means| and s must not exceed 1,000,000,000.";
  results.hidden=true;return;
 }
 results.hidden=false;error.hidden=true;error.textContent="";
 for(const k of ["df","se","t","pvalue","critical","lower","upper"])
  el(k).textContent=k==="df"?String(v.df):fmt(v[k]);
 el("decision").textContent=(v.pvalue<.05?"Reject":"Do not reject")+
  " H₀: μ=μ₀ at α=0.05, provided sampling and distribution assumptions are appropriate.";
 el("assumptions").textContent=(v.n<30?
  "Small sample: validity requires approximately normal population data and no serious outliers. ":
  "Larger samples can improve robustness, but independence and strongly influential outliers still matter. ")+
  "The sample standard deviation uses n−1 degrees of freedom; the normal Z distribution is NOT substituted.";
 el("limits").textContent="The displayed interval is a two-sided 95% Student t confidence interval, regardless of selected one-sided test. "+
  "Summary inputs cannot diagnose skewness or outliers; a non-significant result does not prove equality.";
 plot(v);
}
for(const id of ["n","mean","sd","mu0","alternative"]){
 el(id).addEventListener("input",render);el(id).addEventListener("change",render);
}
el("reset").addEventListener("click",()=>{
 for(const [k,v] of Object.entries({n:"10",mean:"12",sd:"3",mu0:"10",alternative:"two-sided"}))
  el(k).value=v;
 render();
});
render();
})();