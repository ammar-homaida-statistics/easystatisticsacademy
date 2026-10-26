/* Batch #73: one-sample Z inference with KNOWN population standard deviation. */
(function(){
"use strict";
const root=document.getElementById("esa-one-mean-z-lab");if(!root)return;
const $=id=>root.querySelector("#esa-omz-"+id);
// Complementary error-function rational approximation (absolute error ~1.5e-7).
const erfcPositive=x=>{
 const t=1/(1+0.3275911*x);
 return t*(0.254829592+t*(-0.284496736+t*(1.421413741+
        t*(-1.453152027+t*1.061405429))))*Math.exp(-x*x);
};
const upperTail=z=>{
 if(z===0)return 0.5;
 return z>0?0.5*erfcPositive(z/Math.SQRT2):1-0.5*erfcPositive(-z/Math.SQRT2);
};
const z975=1.959963984540054;
function compute(n,mean,sigma,mu0,side="two-sided"){
 if(!Number.isSafeInteger(n)||n<1||n>1000000||
    !Number.isFinite(mean)||!Number.isFinite(sigma)||!Number.isFinite(mu0)||
    sigma<=0||sigma>1e9||Math.abs(mean)>1e9||Math.abs(mu0)>1e9||
    !["two-sided","greater","less"].includes(side))return null;
 const se=sigma/Math.sqrt(n),z=(mean-mu0)/se;
 if(!Number.isFinite(z))return null;
 const sf=upperTail(Math.abs(z)),pvalue=side==="two-sided"?Math.min(1,2*sf):
   side==="greater"?upperTail(z):upperTail(-z);
 const margin=z975*se;
 return {n,mean,sigma,mu0,se,z,pvalue,lower:mean-margin,upper:mean+margin,side};
}
window.esaOneMeanZMath={compute,upperTail};
const fmt=x=>x.toFixed(6);
const ns="http://www.w3.org/2000/svg";
const svg=(tag,attributes={},text)=>{
 const e=document.createElementNS(ns,tag);
 for(const [key,value] of Object.entries(attributes))e.setAttribute(key,String(value));
 if(text!==undefined)e.textContent=String(text);
 return e;
};
function renderPlot(o){
 const chart=$("plot"),limit=Math.max(4.25,Math.min(18,Math.abs(o.z)+1.5)),n=180;
 const x=t=>35+(t+limit)*550/(2*limit),y=t=>196-162*Math.exp(-t*t/2);
 const elems=[svg("title",{},"Standard normal distribution with selected test tail(s)"),
  svg("desc",{},"Teal shading represents the requested Z-test p-value region; orange line marks the observed Z statistic.")];
 let path="";
 for(let i=0;i<=n;i++){
  const a=-limit+2*limit*i/n;
  path+=(i?"L":"M")+x(a).toFixed(2)+","+y(a).toFixed(2);
  if(i<n){
   const b=-limit+2*limit*(i+1)/n,m=(a+b)/2;
   const selected=o.side==="two-sided"?Math.abs(m)>=Math.abs(o.z):
      o.side==="greater"?m>=o.z:m<=o.z;
   if(selected)elems.push(svg("rect",{x:x(a),y:y(m),width:x(b)-x(a)+.3,
     height:196-y(m),fill:"#0f766e",opacity:.44}));
  }
 }
 elems.push(svg("path",{d:path,fill:"none",stroke:"#2563eb","stroke-width":2.4}),
  svg("line",{x1:35,x2:585,y1:196,y2:196,stroke:"currentColor"}),
  svg("line",{x1:x(o.z),x2:x(o.z),y1:20,y2:196,stroke:"#b45309","stroke-width":2,"stroke-dasharray":"5 4"}),
  svg("text",{x:35,y:216,fill:"currentColor","font-size":12},(-limit).toFixed(1)),
  svg("text",{x:310,y:216,fill:"currentColor","font-size":12,"text-anchor":"middle"},"0"),
  svg("text",{x:585,y:216,fill:"currentColor","font-size":12,"text-anchor":"end"},limit.toFixed(1)));
 chart.replaceChildren(...elems);
 chart.setAttribute("aria-label","Standard normal distribution, Z="+fmt(o.z)+
   ", "+o.side+" approximate p-value "+fmt(o.pvalue)+".");
}
function render(){
 const raw=[$("n").value.trim(),$("mean").value.trim(),$("sigma").value.trim(),$("mu0").value.trim()];
 const n=/^\d+$/.test(raw[0])?Number(raw[0]):NaN;
 const args=raw.slice(1).map(s=>s===""?NaN:Number(s));
 const o=compute(n,...args,$("side").value);
 if(!o){
  $("results").hidden=true;$("error").hidden=false;
  $("error").textContent="Enter n=1–1,000,000 (integer), finite sample and null means, and KNOWN population σ>0; absolute means and σ must be ≤1,000,000,000.";
  return;
 }
 $("results").hidden=false;$("error").hidden=true;$("error").textContent="";
 for(const id of ["se","z","pvalue","lower","upper"])$(id).textContent=fmt(o[id]);
 $("assumptions").textContent=o.n<30?
   "Small sample: the population should be approximately normally distributed and observations independent; knowledge of σ alone does not make the Z approximation valid.":
   "Large-sample approximation requires independent observations and appropriate Central Limit Theorem conditions. Extremely skewed populations or influential observations can still matter.";
 $("decision").textContent=(o.pvalue<0.05?"Reject":"Do not reject")+" H₀: μ=μ₀ at α=0.05 if the assumptions hold.";
 $("interpretation").textContent="The 95% interval is two-sided for all alternatives. σ must be the known POPULATION standard deviation, not estimated sample s. If σ is unknown, consider the one-sample Student t-test. A p-value is not the probability that H₀ is true.";
 renderPlot(o);
}
for(const id of ["n","mean","sigma","mu0","side"]){
 $(id).addEventListener("input",render);$(id).addEventListener("change",render);
}
$("reset").addEventListener("click",()=>{
 for(const [id,val] of Object.entries({n:"100",mean:"492",sigma:"20",mu0:"500",side:"two-sided"}))$(id).value=val;
 render();
});
render();
})();