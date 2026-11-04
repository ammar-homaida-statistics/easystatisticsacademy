/* Batch #80: uniform-density interval probability with exact overlap integral.
   The true density need not be at most one: it is 1/(b-a). */
(function(){
"use strict";
function calculate(a,b,c,d){
 if(![a,b,c,d].every(Number.isFinite)||[a,b,c,d].some(x=>Math.abs(x)>1e6)||!(a<b)||!(c<=d)||b-a<1e-6)return null;
 const length=b-a,overlap=Math.max(0,Math.min(b,d)-Math.max(a,c)),density=1/length;
 return {a,b,c,d,density,probability:overlap/length,overlap,integral:1,pointProbability:0,mean:(a+b)/2,variance:length*length/12};
}
window.esaUniformPDFMath={calculate};
const root=document.getElementById("esa-uniform-pdf-lab");if(!root)return;
const get=k=>root.querySelector("#esa-updf-"+k),keys=["a","b","c","d"],ns="http://www.w3.org/2000/svg";
const node=(tag,attrs={},content)=>{const el=document.createElementNS(ns,tag);for(const [k,v] of Object.entries(attrs))el.setAttribute(k,String(v));if(content!==undefined)el.textContent=String(content);return el;};
function render(){
 const fields=keys.map(k=>get(k).value.trim()),values=fields.map(s=>s===""?NaN:Number(s));
 const out=calculate(...values),error=get("error"),results=get("results"),chart=get("chart");
 error.hidden=Boolean(out);results.hidden=!out;chart.hidden=!out;
 if(!out){error.textContent="Enter finite bounds a < b, interval c ≤ d and a support width of at least 0.000001.";return;}
 ["density","probability","integral","pointProbability","mean","variance"].forEach(k=>get(k).textContent=out[k].toFixed(6));
 get("interpretation").textContent="Interval probability equals the shaded overlap length ("+out.overlap.toFixed(4)+") divided by support width ("+(out.b-out.a).toFixed(4)+"). A density value may exceed 1 without violating probability axioms.";
 const xmin=Math.min(out.a,out.c)-Math.max(1,(out.b-out.a)*.15),xmax=Math.max(out.b,out.d)+Math.max(1,(out.b-out.a)*.15);
 const x=v=>35+540*(v-xmin)/(xmax-xmin),baseline=175,top=35;
 const shapes=[node("title",{},"Uniform probability density and shaded interval"),node("desc",{},"Rectangle is uniform density on support; shaded portion is interval intersection. Probability uses exact overlap, including regions outside the plot."),node("line",{x1:35,x2:575,y1:baseline,y2:baseline,stroke:"currentColor"}),node("rect",{x:x(out.a),y:top,width:x(out.b)-x(out.a),height:baseline-top,fill:"#0f766e","fill-opacity":".3",stroke:"#0f766e","stroke-width":2})];
 const l=Math.max(out.a,out.c),u=Math.min(out.b,out.d);
 if(u>l)shapes.push(node("rect",{x:x(l),y:top,width:x(u)-x(l),height:baseline-top,fill:"#2563eb","fill-opacity":".65"}));
 for(const [key,value] of [["a",out.a],["b",out.b],["c",out.c],["d",out.d]])shapes.push(node("text",{x:x(value),y:key==="c"||key==="d"?213:193,"text-anchor":"middle",fill:"currentColor","font-size":12},key+"="+value.toFixed(2)));
 chart.replaceChildren(...shapes);
 chart.setAttribute("aria-label","Uniform density from "+out.a+" to "+out.b+"; selected interval "+out.c+" to "+out.d+"; shaded probability "+out.probability.toFixed(6)+".");
}
keys.forEach(k=>get(k).addEventListener("input",render));
get("reset").addEventListener("click",()=>{["0","4","1","3"].forEach((s,i)=>get(keys[i]).value=s);render();});
render();
})();