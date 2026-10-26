/* Batch #72: shared Bernoulli PMF, moments and probability explorer. */
(function(){
"use strict";
const root=document.getElementById("esa-bernoulli-explorer");if(!root)return;
const arabic=document.documentElement.lang==="ar";
const el=id=>root.querySelector("#esa-bern-"+id);
const NS="http://www.w3.org/2000/svg";
const node=(tag,attrs={},text)=>{
 const n=document.createElementNS(NS,tag);
 Object.entries(attrs).forEach(([k,v])=>n.setAttribute(k,String(v)));
 if(text!==undefined)n.textContent=String(text);
 return n;
};
function compute(p){
 if(!Number.isFinite(p)||p<0||p>1)return null;
 return {p0:1-p,p1:p,mean:p,variance:p*(1-p)};
}
window.esaBernoulliMath={compute};
function render(){
 const raw=el("p").value.trim();
 const result=raw===""?null:compute(Number(raw));
 const error=el("error"),chart=el("chart");
 if(!result){
  for(const id of ["p0","p1","mean","variance"])el(id).textContent="—";
  error.hidden=false;error.textContent=arabic?"أدخل احتمالًا بين 0 و1.":"Enter a success probability between 0 and 1.";
  chart.replaceChildren();chart.hidden=true;chart.style.display="none";
  return;
 }
 error.hidden=true;error.textContent="";
 for(const id of ["p0","p1","mean","variance"])el(id).textContent=result[id].toFixed(6);
 const pValues=[result.p0,result.p1],scale=175;
 const labels=arabic?["إخفاق (X=0)","نجاح (X=1)"]:["Failure (X=0)","Success (X=1)"];
 const shapes=[node("title",{},arabic?"توزيع برنولي الاحتمالي":"Bernoulli probability mass function"),
  node("line",{x1:45,y1:216,x2:555,y2:216,stroke:"currentColor"})];
 for(let i=0;i<2;i++){
  const h=pValues[i]*scale,x=110+i*285;
  const rect=node("rect",{x,y:216-h,width:125,height:h,rx:3,fill:i?"#b45309":"#0f766e"});
  rect.appendChild(node("title",{},labels[i]+": "+pValues[i].toFixed(6)));
  shapes.push(rect,node("text",{x:x+62.5,y:236,fill:"currentColor","text-anchor":"middle","font-size":16},String(i)),
   node("text",{x:x+62.5,y:Math.max(22,209-h),fill:"currentColor","text-anchor":"middle","font-size":14},pValues[i].toFixed(3)));
 }
 chart.replaceChildren(...shapes);chart.hidden=false;chart.style.display="block";
 chart.setAttribute("aria-label",arabic?
 "احتمال الإخفاق "+result.p0.toFixed(6)+" واحتمال النجاح "+result.p1.toFixed(6):
 "Failure probability "+result.p0.toFixed(6)+"; success probability "+result.p1.toFixed(6));
}
el("p").addEventListener("input",render);
el("reset").addEventListener("click",()=>{el("p").value="0.3";render()});
render();
})();