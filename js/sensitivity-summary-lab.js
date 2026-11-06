/* Batch #82: a bounded, fixed-design illustration of descriptive-statistic sensitivity. */
(function(){
"use strict";
const baseline=[2,4,5,6,8,9,10,12,14,15];
function summarize(outlier){
 if(!Number.isFinite(outlier)||outlier< -1000||outlier>1000)return null;
 const observations=baseline.concat([outlier]);
 const sorted=observations.slice().sort((a,b)=>a-b);
 const n=sorted.length, mean=observations.reduce((a,x)=>a+x,0)/n,median=sorted[5];
 // Exactly 10% trimmed on each side with floor(0.1*n)=1.
 const trimmed=sorted.slice(1,-1).reduce((a,x)=>a+x,0)/(n-2);
 return {n,mean,median,trimmed,sorted,baselineMean:baseline.reduce((a,x)=>a+x,0)/baseline.length};
}
window.esaSensitivityMath={summarize};
const root=document.getElementById("esa-sensitivity-lab");if(!root)return;
const get=id=>root.querySelector("#esa-sens-"+id);
const ns="http://www.w3.org/2000/svg";
function svg(tag,attrs={},content){const e=document.createElementNS(ns,tag);for(const [k,v]of Object.entries(attrs))e.setAttribute(k,String(v));if(content!==undefined)e.textContent=String(content);return e;}
function render(){
 const raw=get("value").value.trim(),x=raw===""?NaN:Number(raw),out=summarize(x);
 const error=get("error"),results=get("results"),chart=get("chart");
 error.hidden=!!out;results.hidden=!out;chart.hidden=!out;chart.style.display=out?"block":"none";
 get("value").setAttribute("aria-invalid",out?"false":"true");
 if(!out){error.textContent="Enter a finite replacement value between -1000 and 1000.";return;}
 for(const name of ["mean","median","trimmed"])get(name).textContent=out[name].toFixed(3);
 get("observations").textContent=out.sorted.join(", ");
 const statistics=[["Mean",out.mean],["Median",out.median],["10% trimmed mean",out.trimmed]];
 const range=Math.max(1,...statistics.map(v=>Math.abs(v[1]))),scale=x=>200+150*x/range;
 const elements=[svg("title",{},"Mean, median and trimmed mean under one changed observation"),svg("desc",{},"The vertical reference is zero; each marker represents a calculated statistic for the same eleven observations."),svg("line",{x1:200,x2:200,y1:28,y2:180,stroke:"currentColor","stroke-dasharray":"5 5"})];
 statistics.forEach(([label,value],i)=>{const y=54+i*55;elements.push(svg("text",{x:12,y:y+4,"font-size":13,fill:"currentColor"},label),svg("line",{x1:200,x2:scale(value),y1:y,y2:y,stroke:"#0f766e","stroke-width":3}),svg("circle",{cx:scale(value),cy:y,r:6,fill:"#b45309"}),svg("text",{x:370,y:y+4,"font-size":13,fill:"currentColor"},value.toFixed(2)));});
 chart.replaceChildren(...elements);
 chart.setAttribute("aria-label","Mean "+out.mean.toFixed(3)+", median "+out.median.toFixed(3)+", trimmed mean "+out.trimmed.toFixed(3)+" for eleven observations.");
}
get("value").addEventListener("input",render);
get("reset").addEventListener("click",()=>{get("value").value="11";render();});
render();
})();