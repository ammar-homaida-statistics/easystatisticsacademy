/* Shared bilingual Lognormal probability explorer (Batch #70). */
(function(){
"use strict";
const root=document.getElementById("esa-lognormal-lab");if(!root)return;
const ar=document.documentElement.lang==="ar",get=x=>root.querySelector("#esa-ln-"+x);
const muEl=get("mu"),sigmaEl=get("sigma"),aEl=get("a"),bEl=get("b"),modeEl=get("mode"),
      error=get("error"),plot=get("plot"),results=get("results");
function erfcPositive(x){
 const t=1/(1+0.3275911*x);
 return t*(0.254829592+t*(-0.284496736+
 t*(1.421413741+t*(-1.453152027+t*1.061405429))))*Math.exp(-x*x);
}
function Phi(z){return z<0?0.5*erfcPositive(-z/Math.SQRT2):1-0.5*erfcPositive(z/Math.SQRT2)}
function SF(z){return z>=0?0.5*erfcPositive(z/Math.SQRT2):1-0.5*erfcPositive(-z/Math.SQRT2)}
function cdf(x,mu,sigma){if(x<=0)return 0;return Phi((Math.log(x)-mu)/sigma)}
function survival(x,mu,sigma){if(x<=0)return 1;return SF((Math.log(x)-mu)/sigma)}
function compute(mu,sigma,a,b,mode){
 if(!Number.isFinite(mu)||Math.abs(mu)>15||!Number.isFinite(sigma)||!(sigma>0)||sigma>4||
    !Number.isFinite(a)||!Number.isFinite(b)||a<0||b<0||a>1e12||b>1e12||
    !["between","left","right"].includes(mode)||(mode==="between"&&a>=b))return null;
 const mean=Math.exp(mu+sigma*sigma/2);
 const variance=Math.expm1(sigma*sigma)*Math.exp(2*mu+sigma*sigma);
 const median=Math.exp(mu),modeValue=Math.exp(mu-sigma*sigma);
 const p=mode==="left"?cdf(a,mu,sigma):mode==="right"?survival(b,mu,sigma):
   ((a>0&&Math.log(a)>=mu)?survival(a,mu,sigma)-survival(b,mu,sigma):
   cdf(b,mu,sigma)-cdf(a,mu,sigma));
 return {mu,sigma,a,b,probability:Math.max(0,Math.min(1,p)),mean,
         median,modeValue,variance,sd:Math.sqrt(variance),region:mode};
}
window.esaLognormalMath={compute,cdf,survival,Phi,SF};
function number(x){return x.toFixed(6)}
const svgNS="http://www.w3.org/2000/svg";
function node(tag,attrs={},label){
 const n=document.createElementNS(svgNS,tag);
 for(const [k,v] of Object.entries(attrs))n.setAttribute(k,String(v));
 if(label!==undefined)n.textContent=String(label);return n;
}
function draw(s){
 const zMin=-3.5,zMax=3.5,left=37,right=584,base=185,top=24;
 const sx=z=>left+(z-zMin)/(zMax-zMin)*(right-left);
 const f=z=>Math.exp(-z*z/2-s.sigma*z-s.mu)/(s.sigma*Math.sqrt(2*Math.PI));
 const peakZ=Math.max(zMin,Math.min(zMax,-s.sigma));
 const peak=f(peakZ),sy=z=>base-(base-top)*f(z)/peak;
 const za=s.a>0?(Math.log(s.a)-s.mu)/s.sigma:-Infinity;
 const zb=s.b>0?(Math.log(s.b)-s.mu)/s.sigma:-Infinity;
 const lower=s.region==="right"?zb:s.region==="left"?-Infinity:za;
 const upper=s.region==="right"?Infinity:s.region==="left"?za:zb;
 function path(from,to,area){
  if(from>=to)return "";
  const n=140;let d=area?"M "+sx(from).toFixed(2)+" "+base:"";
  for(let i=0;i<=n;i++){
   const z=from+(to-from)*i/n;d+=(area||i?" L ":"M ")+sx(z).toFixed(2)+" "+sy(z).toFixed(2);
  }
  return area?d+" L "+sx(to).toFixed(2)+" "+base+" Z":d;
 }
 plot.replaceChildren(node("title",{},ar?"كثافة التوزيع اللوغاريتمي الطبيعي":"Lognormal probability density"),
   node("desc",{},ar?"منحنى كثافة لوغاريتمي طبيعي مع منطقة احتمالية مظللة":"Lognormal density with selected probability region shaded"),
   node("line",{x1:left,x2:right,y1:base,y2:base,stroke:"currentColor"}),
   node("path",{d:path(zMin,zMax,false),fill:"none",stroke:"#0d9488","stroke-width":2.4}),
   node("path",{d:path(Math.max(zMin,lower),Math.min(zMax,upper),true),
         fill:"#0d9488","fill-opacity":.35}),
   node("text",{x:left,y:213,fill:"currentColor","font-size":11},"exp(μ−3.5σ)"),
   node("text",{x:right,y:213,fill:"currentColor","font-size":11,"text-anchor":"end"},"exp(μ+3.5σ)"),
   node("text",{x:sx(0),y:213,fill:"currentColor","font-size":11,"text-anchor":"middle"},"e^μ"));
 plot.setAttribute("aria-label",(ar?"منطقة الاحتمال: ":"Probability: ")+number(s.probability)+
   (ar?"؛ ذيول التوزيع خارج الرسم مشمولة في الحساب.":"; tails outside the chart are included in calculations."));
 get("warning").textContent=(ar?"الرسم يعرض المجال من exp(μ−3.5σ) إلى exp(μ+3.5σ)، بينما تحسب الاحتمالات على المجال الموجب كله.":"The graph shows exp(μ−3.5σ) to exp(μ+3.5σ), but probability calculations include the full positive support.");
}
function refresh(){
 const vals=[muEl,sigmaEl,aEl,bEl].map(x=>x.value.trim()===""?NaN:Number(x.value));
 const s=compute(...vals,modeEl.value);
 if(!s){error.hidden=false;error.textContent=ar?
  "أدخل قيمًا منتهية: −15≤μ≤15 و 0<σ≤4 وحدودًا غير سالبة ≤10¹²، ويجب أن يكون a<b لاحتمال الفترة.":
  "Enter finite values: −15≤μ≤15, 0<σ≤4, nonnegative bounds ≤10¹², and a<b for a between-region.";
  results.hidden=true;return;}
 error.hidden=true;error.textContent="";results.hidden=false;
 for(const k of ["probability","mean","median","modeValue","variance","sd"]){
  get(k).textContent=number(s[k]);
 }
 get("percent").textContent=(100*s.probability).toFixed(4);
 get("region").textContent=s.region==="between"?"P(a ≤ X ≤ b)":s.region==="left"?"P(X ≤ a)":"P(X ≥ b)";
 draw(s);
}
[muEl,sigmaEl,aEl,bEl,modeEl].forEach(el=>{el.addEventListener("input",refresh);el.addEventListener("change",refresh)});
get("reset").addEventListener("click",()=>{
 muEl.value="0";sigmaEl.value=".5";aEl.value="1";bEl.value="2";modeEl.value="between";refresh();
});
refresh();
})();