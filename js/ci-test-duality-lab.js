/* Batch #101: confidence interval ↔ hypothesis test duality for one mean (z or t).
   Exact Student t tail via the regularized incomplete beta; normal tails via an
   accurate erfc (series for x<2.5, continued fraction otherwise). */
(function(){
"use strict";
const G=[0.99999999999980993,676.5203681218851,-1259.1392167224028,771.32342877765313,
 -176.61502916214059,12.507343278686905,-0.13857109526572012,9.9843695780195716e-6,1.5056327351493116e-7];
function logGamma(z){
 if(z<0.5)return Math.log(Math.PI)-Math.log(Math.sin(Math.PI*z))-logGamma(1-z);
 z-=1;let x=G[0];for(let i=1;i<G.length;i++)x+=G[i]/(z+i);
 const t=z+7.5;return 0.5*Math.log(2*Math.PI)+(z+0.5)*Math.log(t)-t+Math.log(x);
}
function betacf(a,b,x){
 const TINY=1e-300;let qab=a+b,qap=a+1,qam=a-1,c=1,d=1-qab*x/qap;
 if(Math.abs(d)<TINY)d=TINY;d=1/d;let h=d;
 for(let m=1;m<=400;m++){
  const m2=2*m;let aa=m*(b-m)*x/((qam+m2)*(a+m2));
  d=1+aa*d;if(Math.abs(d)<TINY)d=TINY;c=1+aa/c;if(Math.abs(c)<TINY)c=TINY;d=1/d;h*=d*c;
  aa=-(a+m)*(qab+m)*x/((a+m2)*(qap+m2));
  d=1+aa*d;if(Math.abs(d)<TINY)d=TINY;c=1+aa/c;if(Math.abs(c)<TINY)c=TINY;d=1/d;
  const del=d*c;h*=del;if(Math.abs(del-1)<1e-15)break;
 }
 return h;
}
function ibeta(x,a,b){
 if(x<=0)return 0;if(x>=1)return 1;
 const front=Math.exp(logGamma(a+b)-logGamma(a)-logGamma(b)+a*Math.log(x)+b*Math.log1p(-x));
 if(x<(a+1)/(a+b+2))return front*betacf(a,b,x)/a;
 return 1-front*betacf(b,a,1-x)/b;
}
function erfc(x){
 if(x<0)return 2-erfc(-x);
 if(x<2.5){let sum=x,term=x;const x2=x*x;
  for(let n=1;n<200;n++){term*=-x2/n;const add=term/(2*n+1);sum+=add;if(Math.abs(add)<1e-17*Math.abs(sum))break;}
  return 1-2/Math.sqrt(Math.PI)*sum;}
 const TINY=1e-300;let f=x,C=x,D=0;
 for(let n=1;n<500;n++){const a=n/2;D=x+a*D;if(Math.abs(D)<TINY)D=TINY;C=x+a/C;if(Math.abs(C)<TINY)C=TINY;
  D=1/D;const del=C*D;f*=del;if(Math.abs(del-1)<1e-16)break;}
 return Math.exp(-x*x)/Math.sqrt(Math.PI)/f;
}
/* Upper-tail probability P(T >= s) for the chosen reference distribution. */
function upper(s,method,df){
 if(method==="z")return 0.5*erfc(s/Math.SQRT2);
 if(s===0)return 0.5;
 const half=0.5*ibeta(df/(df+s*s),df/2,0.5);
 return s>0?half:1-half;
}
/* Quantile q with P(T >= q) = tail, 0 < tail <= 0.5, by bisection on the exact tail. */
function quantile(tail,method,df){
 if(tail===0.5)return 0;
 let lo=0,hi=1;while(upper(hi,method,df)>tail&&hi<1e12)hi*=2;
 for(let i=0;i<200;i++){const mid=(lo+hi)/2;if(upper(mid,method,df)>tail)lo=mid;else hi=mid;if(hi-lo<=1e-15*hi)break;}
 return (lo+hi)/2;
}
function compute(o){
 const {method,side,mean,sd,n,mu0,alpha}=o;
 if(!["z","t"].includes(method)||!["two-sided","greater","less"].includes(side))return null;
 if(!Number.isSafeInteger(n)||n<2||n>1e6)return null;
 if(![mean,sd,mu0,alpha].every(Number.isFinite)||sd<=0||sd>1e9||Math.abs(mean)>1e9||Math.abs(mu0)>1e9)return null;
 if(!(alpha>=0.001&&alpha<=0.5))return null;
 const df=n-1,se=sd/Math.sqrt(n),stat=(mean-mu0)/se;
 const crit=quantile(side==="two-sided"?alpha/2:alpha,method,df);
 const lower=side==="less"?-Infinity:mean-crit*se;
 const upperBound=side==="greater"?Infinity:mean+crit*se;
 let p;
 if(side==="two-sided")p=Math.min(1,2*upper(Math.abs(stat),method,df));
 else if(side==="greater")p=upper(stat,method,df);
 else p=upper(-stat,method,df);
 // Closed interval; the test rejects exactly when the null value lies outside it.
 // Both are decided from the same standardized distance, with a relative tolerance
 // of 1e-12 so that a null value placed on an endpoint counts as inside (p = α).
 const tol=1e-12*Math.max(1,crit);
 const dist=side==="two-sided"?Math.abs(stat):side==="greater"?stat:-stat;
 const inside=dist<=crit+tol;
 return {method,side,df:method==="t"?df:null,se,stat,crit,lower,upper:upperBound,p,inside,reject:!inside};
}
window.esaCiTestDuality={compute,upper,quantile,erfc,ibeta};

const root=document.getElementById("esa-cid-lab");
if(!root)return;
const $=id=>document.getElementById(id);
const ids=["method","side","mean","sd","n","mu0","alpha"];
const fmt=(x,d=4)=>x===Infinity?"∞":x===-Infinity?"−∞":(Math.abs(x)<5e-5&&x!==0?x.toExponential(3):x.toFixed(d)).replace("-","−");
const fmtP=p=>p<1e-6?p.toExponential(3):p.toFixed(6);
const AR=root.dataset.locale==="ar";
const T=AR?{err:"أدخل متوسطًا وقيمة عدم منتهيين، وانحرافًا معياريًا أكبر من 0، وحجم عيّنة صحيحًا من 2 إلى 1,000,000، وقيمة α بين 0.001 و0.5.",
 inside:"نعم — μ₀ داخل الفترة",outside:"لا — μ₀ خارج الفترة",
 reject:a=>"نرفض H₀ عند α = "+a+" (p < α)",keep:a=>"لا نرفض H₀ عند α = "+a+" (p ≥ α)",
 agree:"الفترة والاختبار متفقان.",disagree:"الفترة والاختبار غير متفقين — راجع المدخلات."}
:{err:"Enter a finite mean and null value, an SD greater than 0, a whole-number n from 2 to 1,000,000, and α between 0.001 and 0.5.",
 inside:"Yes — μ₀ is inside the interval",outside:"No — μ₀ is outside the interval",
 reject:a=>"Reject H₀ at α = "+a+" (p < α)",keep:a=>"Do not reject H₀ at α = "+a+" (p ≥ α)",
 agree:"Interval and test agree.",disagree:"Interval and test disagree — check the inputs."};
function read(){
 return {method:$("esa-cid-method").value,side:$("esa-cid-side").value,mean:Number($("esa-cid-mean").value),
  sd:Number($("esa-cid-sd").value),n:Number($("esa-cid-n").value),mu0:Number($("esa-cid-mu0").value),alpha:Number($("esa-cid-alpha").value)};
}
function update(){
 const raw=ids.slice(2).map(i=>$("esa-cid-"+i).value.trim());
 const r=raw.some(v=>v==="")?null:compute(read());
 const err=$("esa-cid-error"),res=$("esa-cid-results");
 ids.slice(2).forEach(i=>$("esa-cid-"+i).setAttribute("aria-invalid",r?"false":"true"));
 if(!r){err.hidden=false;res.hidden=true;
  err.textContent=T.err;return;}
 err.hidden=true;err.textContent="";res.hidden=false;
 const a=read().alpha,lvl=(100*(1-a)).toFixed(a*100%1===0?0:1);
 const symbol=r.method==="z"?"z":"t";
 $("esa-cid-crit").textContent=(r.method==="z"?"z":"t("+r.df+")")+" = "+fmt(r.crit);
 $("esa-cid-ci").textContent=lvl+"%: ["+fmt(r.lower)+", "+fmt(r.upper)+"]";
 $("esa-cid-stat").textContent=symbol+" = "+fmt(r.stat);
 $("esa-cid-p").textContent=fmtP(r.p);
 $("esa-cid-inside").textContent=r.inside?T.inside:T.outside;
 $("esa-cid-decision").textContent=r.reject?T.reject(a):T.keep(a);
 const pAgrees=r.reject?r.p<a:r.p>=a-1e-9*a;
 $("esa-cid-agree").textContent=pAgrees?T.agree:T.disagree;
}
function set(v){for(const k in v)$("esa-cid-"+k).value=v[k];update();}
ids.forEach(i=>$("esa-cid-"+i).addEventListener(i==="method"||i==="side"?"change":"input",update));
$("esa-cid-example").addEventListener("click",()=>set({method:"t",side:"two-sided",mean:104.2,sd:8.5,n:25,mu0:100,alpha:0.05}));
$("esa-cid-inside-ex").addEventListener("click",()=>set({method:"t",side:"two-sided",mean:102.1,sd:8.5,n:25,mu0:100,alpha:0.05}));
$("esa-cid-boundary").addEventListener("click",()=>{
 const r=compute(read());if(!r)return;
 const target=r.side==="less"?r.upper:r.lower;
 $("esa-cid-mu0").value=String(target);update();
});
update();
})();
