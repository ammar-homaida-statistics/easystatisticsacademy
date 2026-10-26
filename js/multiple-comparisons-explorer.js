/* Batch #74 — unadjusted, Bonferroni and Holm adjusted p-value teaching lab. */
(function(){
"use strict";
const root=document.getElementById("esa-multiple-comparisons-lab");if(!root)return;
const $=id=>root.querySelector("#esa-mc-"+id),NS="http://www.w3.org/2000/svg";
function svg(tag,attrs={},txt){const e=document.createElementNS(NS,tag);
 for(const [k,v] of Object.entries(attrs))e.setAttribute(k,String(v));
 if(txt!==undefined)e.textContent=String(txt);return e;
}
function compute(pvalues,alpha){
 if(!Array.isArray(pvalues)||pvalues.length<2||pvalues.length>12||
    !Number.isFinite(alpha)||alpha<=0||alpha>=1||
    pvalues.some(p=>!Number.isFinite(p)||p<0||p>1))return null;
 const m=pvalues.length,bonf=pvalues.map(p=>Math.min(1,m*p)),holm=Array(m).fill(0);
 const order=pvalues.map((p,index)=>({p,index})).sort((a,b)=>a.p-b.p||a.index-b.index);
 let running=0;
 order.forEach(({p,index},j)=>{
  running=Math.max(running,(m-j)*p);
  holm[index]=Math.min(1,running);
 });
 return {m,alpha,pvalues,bonf,holm,
  raw:pvalues.map(p=>p<=alpha),bonfDecision:bonf.map(p=>p<=alpha),
  holmDecision:holm.map(p=>p<=alpha),
  independenceFWER:1-Math.pow(1-alpha,m),unionBound:Math.min(1,m*alpha)};
}
window.esaMultipleComparisonsMath={compute};
function format(x){return x.toFixed(6)}
function plot(o){
 const chart=$("chart"),n=o.m,colors=["#a16207","#2563eb","#0f766e"],names=["raw","bonf","holm"];
 const width=610,left=42,right=14,top=12,base=235,range=base-top,step=(width-left-right)/n;
 const drawn=[svg("title",{},"Original and multiplicity-adjusted p-values"),
 svg("desc",{},"For each hypothesis: unadjusted, Bonferroni, and Holm adjusted p-values. Dashed line is alpha.")];
 for(let i=0;i<n;i++){
  names.forEach((kind,k)=>{
   const v=kind==="raw"?o.pvalues[i]:kind==="bonf"?o.bonf[i]:o.holm[i];
   const barW=Math.max(4,step/4.2),x=left+i*step+(k+.25)*barW,y=base-range*v;
   drawn.push(svg("rect",{x,y,width:barW*.92,height:range*v,fill:colors[k]}));
  });
  drawn.push(svg("text",{x:left+(i+.5)*step,y:252,fill:"currentColor",
    "font-size":"12","text-anchor":"middle"},String(i+1)));
 }
 const alphaY=base-range*o.alpha;
 drawn.push(svg("line",{x1:left,x2:width-right,y1:alphaY,y2:alphaY,
  stroke:"#dc2626","stroke-width":2,"stroke-dasharray":"5 3"}),
  svg("line",{x1:left,x2:width-right,y1:base,y2:base,stroke:"currentColor"}),
  svg("text",{x:width-right,y:Math.max(12,alphaY-5),fill:"currentColor",
    "text-anchor":"end","font-size":"12"},"α="+o.alpha.toFixed(3)));
 chart.replaceChildren(...drawn);
 chart.setAttribute("aria-label","Comparison of "+n+" original and adjusted p-values at alpha "+
   o.alpha+"; values listed in results table.");
}
function render(){
 const source=$("values").value.trim();
 const parts=source.split(/[,;\s]+/).filter(Boolean);
 const nums=parts.map(x=>Number(x));
 const alphaRaw=$("alpha").value.trim();
 const alpha=alphaRaw===""?NaN:Number(alphaRaw);
 const result=compute(nums,alpha);
 if(!source||nums.some((v,i)=>!Number.isFinite(v)||!/^(?:(?:\d+\.?\d*)|(?:\.\d+))(?:[eE][+-]?\d+)?$/.test(parts[i]))||!result){
  $("error").hidden=false;
  $("error").textContent="Enter 2–12 p-values from 0 to 1, separated by commas, spaces, or newlines, and α strictly between 0 and 1. Invalid, missing, or negative values are rejected.";
  $("results").hidden=true;return;
 }
 $("error").hidden=true;$("error").textContent="";$("results").hidden=false;
 const body=$("rows");body.replaceChildren();
 const marks=(b)=>b?"Reject H₀":"Do not reject H₀";
 result.pvalues.forEach((p,i)=>{
  const tr=document.createElement("tr");
  const values=[String(i+1),format(p),format(result.bonf[i]),format(result.holm[i]),
    marks(result.raw[i]),marks(result.bonfDecision[i]),marks(result.holmDecision[i])];
  for(let c=0;c<values.length;c++){
   const td=document.createElement(c===0?"th":"td");if(c===0)td.scope="row";
   td.textContent=values[c];tr.appendChild(td);
  }
  body.appendChild(tr);
 });
 $("count").textContent=String(result.m);
 $("fwer").textContent=format(result.independenceFWER);
 $("bound").textContent=format(result.unionBound);
 $("summary").textContent="Holm rejects "+result.holmDecision.filter(Boolean).length+
   " of "+result.m+" hypotheses; Bonferroni rejects "+
   result.bonfDecision.filter(Boolean).length+
   ". Both procedures control family-wise error at α for a predefined family of valid p-values, without requiring test independence.";
 plot(result);
}
for(const id of ["values","alpha"])$(id).addEventListener("input",render);
$("reset").addEventListener("click",()=>{$("values").value="0.003, 0.018, 0.041, 0.22";$("alpha").value="0.05";render()});
render();
})();