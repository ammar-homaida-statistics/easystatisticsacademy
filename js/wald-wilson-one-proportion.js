/* Batch #86: single-proportion Wald and Wilson comparison; reuse the #85 Wilson kernel. */
(function(){
"use strict";
const Z=Object.freeze({90:1.6448536269514722,95:1.959963984540054,99:2.5758293035489004});
function calculate(x,n,level){
 const z=Z[level];
 if(z===undefined||!Number.isSafeInteger(x)||!Number.isSafeInteger(n)||n<1||n>10000000||x<0||x>n)return null;
 const base=window.esaNewcombeMath;
 if(!base||typeof base.wilson!=="function")return null;
 const p=x/n,margin=z*Math.sqrt(p*(1-p)/n);
 return {p,level,wald:[p-margin,p+margin],wilson:base.wilson(x,n,z),margin};
}
window.esaWaldWilsonMath={calculate};
const root=document.getElementById("esa-single-proportion-lab");if(!root)return;
const field=id=>root.querySelector("#esa-sp-"+id);
const x=field("x"),n=field("n"),level=field("level"),err=field("error"),results=field("results"),chart=field("chart");
const svgNS="http://www.w3.org/2000/svg";
function add(type,attrs,text){
 const el=document.createElementNS(svgNS,type);
 Object.entries(attrs).forEach(([name,value])=>el.setAttribute(name,String(value)));
 if(text!==undefined)el.textContent=String(text);
 chart.appendChild(el);
}
function render(){
 const vals=[x,n].map(a=>a.value.trim()===""?NaN:Number(a.value));
 const r=calculate(vals[0],vals[1],Number(level.value));
 for(const f of [x,n])f.setAttribute("aria-invalid",r?"false":"true");
 if(!r){
  err.hidden=false;err.textContent="Enter integer successes between zero and a positive sample size no larger than 10,000,000.";
  results.hidden=true;chart.hidden=true;chart.replaceChildren();return;
 }
 err.hidden=true;err.textContent="";results.hidden=false;chart.hidden=false;
 for(const [id,v] of Object.entries({estimate:r.p,waldlo:r.wald[0],waldhi:r.wald[1],wilsonlo:r.wilson[0],wilsonhi:r.wilson[1]}))field(id).textContent=(100*v).toFixed(4);
 field("confidence").textContent=String(r.level);
 field("warning").textContent=vals[0]<10||vals[1]-vals[0]<10?
  "Small success or failure counts: the Wald interval can have poor coverage, especially near 0 or 1. Wilson often behaves better; neither guarantees exact nominal coverage.":
  "Even with at least ten successes and failures, nominal coverage is not guaranteed for either method.";
 chart.replaceChildren();
 const min=Math.min(0,r.wald[0],r.wilson[0]),max=Math.max(1,r.wald[1],r.wilson[1]);
 const pad=Math.max(.05,.05*(max-min)),lo=min-pad,hi=max+pad;
 const sx=v=>70+355*(v-lo)/(hi-lo);
 add("line",{x1:sx(0),y1:13,x2:sx(0),y2:105,stroke:"currentColor","stroke-dasharray":"4 4"});
 add("line",{x1:sx(1),y1:13,x2:sx(1),y2:105,stroke:"currentColor","stroke-dasharray":"4 4"});
 for(const [i,interval] of [r.wald,r.wilson].entries()){
  const y=35+i*48,stroke=i?"#0f766e":"#2563eb";
  add("text",{x:5,y:y+4,fill:"currentColor","font-size":12},i?"Wilson":"Wald");
  add("line",{x1:sx(interval[0]),x2:sx(interval[1]),y1:y,y2:y,stroke,"stroke-width":4});
  for(const bound of interval)add("circle",{cx:sx(bound),cy:y,r:4,fill:stroke});
 }
 chart.setAttribute("aria-label",r.level+"% intervals, percentages. Wald "+(100*r.wald[0]).toFixed(2)+" to "+(100*r.wald[1]).toFixed(2)+"; Wilson "+(100*r.wilson[0]).toFixed(2)+" to "+(100*r.wilson[1]).toFixed(2)+". Reference lines at zero and one.");
}
[x,n,level].forEach(el=>{el.addEventListener("input",render);el.addEventListener("change",render);});
field("reset").addEventListener("click",()=>{x.value="310";n.value="500";level.value="95";render();});
render();
})();