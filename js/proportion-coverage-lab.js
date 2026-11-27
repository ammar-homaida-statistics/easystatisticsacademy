/* Batch #104: exact coverage of Wald, Wilson and Clopper–Pearson intervals for a binomial
   proportion. Coverage(p) = Σ_x P(X = x | n, p) · 1{L(x) ≤ p ≤ U(x)}, an exact finite sum
   (no simulation). Clopper–Pearson limits invert the regularized incomplete beta function.
   Bilingual (data-locale="ar"). */
(function(){
"use strict";
const Z=Object.freeze({90:1.6448536269514722,95:1.959963984540054,99:2.5758293035489004});
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
 for(let m=1;m<=1000;m++){
  const m2=2*m;let aa=m*(b-m)*x/((qam+m2)*(a+m2));
  d=1+aa*d;if(Math.abs(d)<TINY)d=TINY;c=1+aa/c;if(Math.abs(c)<TINY)c=TINY;d=1/d;h*=d*c;
  aa=-(a+m)*(qab+m)*x/((a+m2)*(qap+m2));
  d=1+aa*d;if(Math.abs(d)<TINY)d=TINY;c=1+aa/c;if(Math.abs(c)<TINY)c=TINY;d=1/d;
  const del=d*c;h*=del;if(Math.abs(del-1)<1e-15)break;
 }
 return h;
}
/* Regularized incomplete beta I_x(a, b). */
function ibeta(x,a,b){
 if(x<=0)return 0;if(x>=1)return 1;
 const front=Math.exp(logGamma(a+b)-logGamma(a)-logGamma(b)+a*Math.log(x)+b*Math.log1p(-x));
 if(x<(a+1)/(a+b+2))return front*betacf(a,b,x)/a;
 return 1-front*betacf(b,a,1-x)/b;
}
/* Beta quantile by bisection on I_x(a,b) (monotone in x). */
function betaQuantile(q,a,b){
 let lo=0,hi=1;
 for(let i=0;i<200;i++){const m=(lo+hi)/2;if(ibeta(m,a,b)<q)lo=m;else hi=m;if(hi-lo<1e-15)break;}
 return (lo+hi)/2;
}
const CACHE=new Map();
function intervals(n,level){
 const key=n+"|"+level;if(CACHE.has(key))return CACHE.get(key);
 const z=Z[level],a=1-level/100,out=[];
 for(let x=0;x<=n;x++){
  const p=x/n,m=z*Math.sqrt(p*(1-p)/n);
  const den=1+z*z/n,c=(p+z*z/(2*n))/den,r=z*Math.sqrt(p*(1-p)/n+z*z/(4*n*n))/den;
  out.push({wald:[p-m,p+m],wilson:[Math.max(0,c-r),Math.min(1,c+r)],
   cp:[x===0?0:betaQuantile(a/2,x,n-x+1),x===n?1:betaQuantile(1-a/2,x+1,n-x)]});
 }
 if(CACHE.size>20)CACHE.clear();
 CACHE.set(key,out);
 return out;
}
function logPmf(x,n,p){
 if(p<=0)return x===0?0:-Infinity;if(p>=1)return x===n?0:-Infinity;
 return logGamma(n+1)-logGamma(x+1)-logGamma(n-x+1)+x*Math.log(p)+(n-x)*Math.log1p(-p);
}
/* Closed intervals; a 1e-12 tolerance keeps endpoints that equal p (e.g. Clopper–Pearson
   limits at n = 1) inside despite rounding in the beta quantile. */
const EPS=1e-12;
function coverageAt(n,p,ints){
 const cov={wald:0,wilson:0,cp:0};
 for(let x=0;x<=n;x++){
  const w=Math.exp(logPmf(x,n,p));if(w===0)continue;
  for(const k of ["wald","wilson","cp"]){const [L,U]=ints[x][k];if(L<=p+EPS&&p<=U+EPS)cov[k]+=w;}
 }
 return cov;
}
function compute(n,p,level){
 if(!Number.isSafeInteger(n)||n<1||n>1000||!Number.isFinite(p)||p<0.001||p>0.999||Z[level]===undefined)return null;
 const ints=intervals(n,level);
 return Object.assign({n,p,level},coverageAt(n,p,ints));
}
function curve(n,level,points=199){
 const ints=intervals(n,level),out=[];
 for(let i=1;i<=points;i++){const p=i/(points+1);out.push(Object.assign({p},coverageAt(n,p,ints)));}
 return out;
}
window.esaPropCoverage={compute,curve,intervals,ibeta,betaQuantile};

const root=document.getElementById("esa-pcov-lab");if(!root)return;
const $=id=>document.getElementById("esa-pcov-"+id),NS="http://www.w3.org/2000/svg";
const AR=root.dataset.locale==="ar";
const T=AR?{err:"أدخل حجم عيّنة صحيحًا من 1 إلى 1,000، ونسبة حقيقية p بين 0.001 و0.999.",
 below:"أقل من المستوى الاسمي",ok:"عند المستوى الاسمي أو أعلى",
 chartTitle:"التغطية الفعلية مقابل p الحقيقية",nominal:"المستوى الاسمي",
 aria:(l)=>"منحنيات التغطية الفعلية لفترات والد وويلسون وكلوبر–بيرسون عند مستوى "+l+"%."}
:{err:"Enter a whole-number n from 1 to 1,000 and a true proportion p between 0.001 and 0.999.",
 below:"below the nominal level",ok:"at or above the nominal level",
 chartTitle:"Actual coverage against the true p",nominal:"nominal",
 aria:(l)=>"Exact coverage curves of the Wald, Wilson and Clopper–Pearson intervals at the "+l+"% level."};
const NAMES=AR?{wald:"والد",wilson:"ويلسون",cp:"كلوبر–بيرسون"}:{wald:"Wald",wilson:"Wilson",cp:"Clopper–Pearson"};
const COLORS={wald:"#b42318",wilson:"#0f766e",cp:"#2563eb"};
function mk(tag,attrs,text){const e=document.createElementNS(NS,tag);for(const [k,v] of Object.entries(attrs))e.setAttribute(k,String(v));if(text!==undefined)e.textContent=String(text);return e;}
function draw(n,level,p){
 const svg=$("chart"),c=curve(n,level,99),W=460,H=200,L=44,R=10,Tp=12,B=28;
 const lo=Math.min(0.6,...c.map(o=>Math.min(o.wald,o.wilson,o.cp)));
 const sx=v=>L+(W-L-R)*v,sy=v=>Tp+(H-Tp-B)*(1-(v-lo)/(1-lo));
 const kids=[mk("title",{},T.chartTitle)];
 for(const t of [lo,(lo+1)/2,1])kids.push(mk("text",{x:2,y:sy(t)+4,"font-size":10,fill:"currentColor"},t.toFixed(2)));
 for(const t of [0,0.5,1])kids.push(mk("text",{x:sx(t)-6,y:H-8,"font-size":10,fill:"currentColor"},String(t)));
 kids.push(mk("line",{x1:sx(0),x2:sx(1),y1:sy(level/100),y2:sy(level/100),stroke:"currentColor","stroke-dasharray":"4 3"}));
 kids.push(mk("line",{x1:sx(p),x2:sx(p),y1:Tp,y2:H-B,stroke:"currentColor","stroke-opacity":0.5}));
 for(const k of ["wald","wilson","cp"]){
  const d=c.map((o,i)=>(i?"L":"M")+sx(o.p).toFixed(1)+" "+sy(Math.max(lo,o[k])).toFixed(1)).join(" ");
  kids.push(mk("path",{d,fill:"none",stroke:COLORS[k],"stroke-width":1.4}));
 }
 svg.replaceChildren(...kids);svg.setAttribute("aria-label",T.aria(level));
}
function update(){
 const nRaw=$("n").value.trim(),pRaw=$("p").value.trim(),level=Number($("level").value);
 const r=nRaw===""||pRaw===""?null:compute(Number(nRaw),Number(pRaw),level);
 ["n","p"].forEach(k=>$(k).setAttribute("aria-invalid",r?"false":"true"));
 if(!r){$("error").hidden=false;$("error").textContent=T.err;$("results").hidden=true;return;}
 $("error").hidden=true;$("error").textContent="";$("results").hidden=false;
 for(const k of ["wald","wilson","cp"]){
  $(k).textContent=r[k].toFixed(4);
  $(k+"-flag").textContent=r[k]<level/100-1e-12?T.below:T.ok;
 }
 draw(r.n,level,r.p);
}
["n","p","level"].forEach(k=>{$(k).addEventListener("input",update);$(k).addEventListener("change",update);});
const set=v=>{for(const k in v)$(k).value=v[k];update();};
$("small").addEventListener("click",()=>set({n:"30",p:"0.1",level:"95"}));
$("half").addEventListener("click",()=>set({n:"100",p:"0.5",level:"95"}));
$("rare").addEventListener("click",()=>set({n:"20",p:"0.05",level:"95"}));
update();
})();
