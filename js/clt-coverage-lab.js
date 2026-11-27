/* Batch #105: does the Central Limit Theorem rescue the one-sample t interval?
   Seeded Monte Carlo (mulberry32 + Box–Muller) of the actual coverage of the nominal
   t interval for samples from normal, uniform, exponential and lognormal populations,
   with the split of misses into the two tails and a histogram of the sample means.
   Bilingual (data-locale="ar"). */
(function(){
"use strict";
function mulberry32(seed){
 let a=seed>>>0;
 return function(){a=(a+0x6D2B79F5)>>>0;let t=a;t=Math.imul(t^(t>>>15),t|1);t^=t+Math.imul(t^(t>>>7),t|61);return ((t^(t>>>14))>>>0)/4294967296;};
}
const POP={
 normal:{mean:0,draw:(u,g)=>g()},
 uniform:{mean:0.5,draw:(u)=>u()},
 exponential:{mean:1,draw:(u)=>-Math.log(1-u())},
 lognormal:{mean:Math.exp(0.5),draw:(u,g)=>Math.exp(g())}
};
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
const tUpper=(s,df)=>0.5*ibeta(df/(df+s*s),df/2,0.5); // P(T ≥ s), s ≥ 0
function tQuantile(tail,df){
 let lo=0,hi=1;while(tUpper(hi,df)>tail)hi*=2;
 for(let i=0;i<200;i++){const m=(lo+hi)/2;if(tUpper(m,df)>tail)lo=m;else hi=m;if(hi-lo<=1e-14*hi)break;}
 return (lo+hi)/2;
}
function simulate(pop,n,level,reps,seed){
 const P=POP[pop];
 if(!P||!Number.isSafeInteger(n)||n<2||n>200||![90,95,99].includes(level)||!Number.isSafeInteger(reps)||reps<100||reps>50000)return null;
 const u=mulberry32(seed===undefined?20261127:seed);
 let spare=null;
 const g=()=>{if(spare!==null){const s=spare;spare=null;return s;}
  let a=u();while(a<=0)a=u();const b=u(),r=Math.sqrt(-2*Math.log(a));spare=r*Math.sin(2*Math.PI*b);return r*Math.cos(2*Math.PI*b);};
 const q=tQuantile((1-level/100)/2,n-1),mu=P.mean,means=new Float64Array(reps);
 let cover=0,below=0,above=0;
 for(let r=0;r<reps;r++){
  let s=0,ss=0;const x=new Float64Array(n);
  for(let i=0;i<n;i++){x[i]=P.draw(u,g);s+=x[i];}
  const m=s/n;for(let i=0;i<n;i++){const d=x[i]-m;ss+=d*d;}
  const half=q*Math.sqrt(ss/(n-1)/n);means[r]=m;
  if(m+half<mu)below++;else if(m-half>mu)above++;else cover++;
 }
 const c=cover/reps;
 return {pop,n,level,reps,q,mu,coverage:c,se:Math.sqrt(c*(1-c)/reps),missBelow:below/reps,missAbove:above/reps,means};
}
window.esaCLTCoverage={simulate,mulberry32,tQuantile,POP};

const root=document.getElementById("esa-clt-lab");if(!root)return;
const $=id=>document.getElementById("esa-clt-"+id),NS="http://www.w3.org/2000/svg";
const AR=root.dataset.locale==="ar";
const T=AR?{err:"اختر مجتمعًا، وحجم عيّنة صحيحًا من 2 إلى 200.",
 note:(c,l,b,a)=>"التغطية الفعلية "+c+" مقابل "+l+"% اسميًا. الفترة وقعت كلها تحت μ في "+b+" من العيّنات، وكلها فوقها في "+a+".",
 lop:"الأخطاء غير متوازنة بين الطرفين: الفترة تخطئ في جهة واحدة أكثر بكثير من الأخرى، وهذا أثر الالتواء.",
 ok:"الأخطاء متوازنة تقريبًا بين الطرفين.",
 hist:"المدرج التكراري لمتوسطات العيّنات؛ الخط العمودي هو متوسط المجتمع μ.",
 aria:(p,n)=>"مدرج تكراري لـ 20,000 متوسط عيّنة بحجم "+n+" من مجتمع "+p+"."}
:{err:"Choose a population and a whole-number n from 2 to 200.",
 note:(c,l,b,a)=>"Actual coverage "+c+" against a nominal "+l+"%. The whole interval fell below μ in "+b+" of samples and above it in "+a+".",
 lop:"The misses are lopsided: the interval fails much more often on one side than the other — the signature of skewness.",
 ok:"The misses are roughly balanced between the two sides.",
 hist:"Histogram of the sample means; the vertical line is the population mean μ.",
 aria:(p,n)=>"Histogram of 20,000 sample means of size "+n+" from the "+p+" population."};
function mk(tag,attrs,text){const e=document.createElementNS(NS,tag);for(const [k,v] of Object.entries(attrs))e.setAttribute(k,String(v));if(text!==undefined)e.textContent=String(text);return e;}
function hist(r){
 const svg=$("chart"),W=460,H=170,B=22,bins=30,ms=Array.from(r.means).sort((a,b)=>a-b);
 const lo=ms[Math.floor(0.001*ms.length)],hi=ms[Math.ceil(0.999*ms.length)-1],w=(hi-lo)/bins||1,cnt=new Array(bins).fill(0);
 for(const m of ms){const k=Math.floor((m-lo)/w);if(k>=0&&k<bins)cnt[k]++;}
 const top=Math.max(...cnt),sx=v=>10+(W-20)*(v-lo)/(hi-lo),kids=[mk("title",{},T.hist)];
 cnt.forEach((c,k)=>kids.push(mk("rect",{x:sx(lo+k*w)+0.5,y:H-B-(H-B-8)*c/top,width:Math.max(1,(W-20)/bins-1),height:(H-B-8)*c/top,fill:"#2563eb","fill-opacity":0.75})));
 if(r.mu>=lo&&r.mu<=hi)kids.push(mk("line",{x1:sx(r.mu),x2:sx(r.mu),y1:4,y2:H-B,stroke:"#b42318","stroke-width":2}));
 kids.push(mk("text",{x:10,y:H-6,"font-size":11,fill:"currentColor"},lo.toFixed(3)),mk("text",{x:W-60,y:H-6,"font-size":11,fill:"currentColor"},hi.toFixed(3)));
 svg.replaceChildren(...kids);svg.setAttribute("aria-label",T.aria($("pop").selectedOptions[0].textContent,r.n));
}
function update(){
 const nRaw=$("n").value.trim();
 const r=nRaw===""?null:simulate($("pop").value,Number(nRaw),Number($("level").value),20000);
 $("n").setAttribute("aria-invalid",r?"false":"true");
 if(!r){$("error").hidden=false;$("error").textContent=T.err;$("results").hidden=true;return;}
 $("error").hidden=true;$("error").textContent="";$("results").hidden=false;
 $("coverage").textContent=r.coverage.toFixed(4);
 $("mcse").textContent=r.se.toFixed(4);
 $("below").textContent=r.missBelow.toFixed(4);
 $("above").textContent=r.missAbove.toFixed(4);
 $("crit").textContent=r.q.toFixed(4);
 const lop=Math.max(r.missBelow,r.missAbove)>2*Math.min(r.missBelow,r.missAbove)+0.005;
 $("note").textContent=T.note(r.coverage.toFixed(4),r.level,r.missBelow.toFixed(4),r.missAbove.toFixed(4))+" "+(lop?T.lop:T.ok);
 hist(r);
}
let timer=null;const schedule=()=>{clearTimeout(timer);timer=setTimeout(update,150);};
["pop","level"].forEach(k=>$(k).addEventListener("change",update));
$("n").addEventListener("input",schedule);
const set=v=>{for(const k in v)$(k).value=v[k];update();};
$("exp10").addEventListener("click",()=>set({pop:"exponential",n:"10",level:"95"}));
$("exp100").addEventListener("click",()=>set({pop:"exponential",n:"100",level:"95"}));
$("norm10").addEventListener("click",()=>set({pop:"normal",n:"10",level:"95"}));
update();
})();
