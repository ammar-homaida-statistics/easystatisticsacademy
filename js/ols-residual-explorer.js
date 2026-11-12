/* Batch #92: bounded centered simple OLS calculation, visualization without HTML injection. */
(function(){
"use strict";
function compute(xs,ys){
 if(!Array.isArray(xs)||!Array.isArray(ys)||xs.length!==ys.length||xs.length<3||xs.length>12)return null;
 if([...xs,...ys].some(v=>!Number.isFinite(v)||Math.abs(v)>1000))return null;
 const n=xs.length, mx=xs.reduce((a,b)=>a+b,0)/n, my=ys.reduce((a,b)=>a+b,0)/n;
 const sxx=xs.reduce((s,x)=>s+(x-mx)**2,0);
 if(sxx<=1e-12)return null;
 const sxy=xs.reduce((s,x,i)=>s+(x-mx)*(ys[i]-my),0);
 const slope=sxy/sxx,intercept=my-slope*mx;
 const fitted=xs.map(x=>intercept+slope*x),residuals=ys.map((y,i)=>y-fitted[i]);
 const sse=residuals.reduce((s,e)=>s+e*e,0);
 const sst=ys.reduce((s,y)=>s+(y-my)**2,0);
 if(!(sst>1e-12))return null; // Constant responses give an ambiguous R² convention.
 const r2=1-sse/sst;
 if([slope,intercept,sse,r2].some(v=>!Number.isFinite(v)))return null;
 return {n,slope,intercept,fitted,residuals,sse,sst,r2,xs,ys};
}
window.esaResidualOLS={compute};
const root=document.getElementById("esa-residual-lab");if(!root)return;
const get=id=>root.querySelector("#esa-residual-"+id);
const x=get("x"),y=get("y"),error=get("error"),results=get("results");
const parse=t=>{
 const parts=t.split(/[,;\n]+/).map(v=>v.trim());
 if(parts.length<3||parts.length>12||parts.some(v=>!v||!/^[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:e[+-]?\d+)?$/i.test(v)))return null;
 const a=parts.map(Number);
 return a.every(v=>Number.isFinite(v)&&Math.abs(v)<=1000)?a:null;
};
const fmt=n=>n.toFixed(6);
const ns="http://www.w3.org/2000/svg";
function svg(name,attrs,text){const e=document.createElementNS(ns,name);for(const [k,v] of Object.entries(attrs||{}))e.setAttribute(k,String(v));if(text!==undefined)e.textContent=String(text);return e;}
function draw(s){
 const plot=get("plot"),xmin=Math.min(...s.xs),xmax=Math.max(...s.xs);
 const values=[...s.ys,...s.fitted],ymin=Math.min(...values),ymax=Math.max(...values),xspan=Math.max(1e-9,xmax-xmin),yspan=Math.max(1e-9,ymax-ymin);
 const px=v=>45+(v-xmin)/xspan*465,py=v=>243-(v-ymin)/yspan*195;
 plot.replaceChildren(svg("title",{},"Observed points, fitted OLS line, vertical residuals"),svg("desc",{},"Blue points show observations, a green line shows fitted predictions and dashed orange lines show vertical residuals."),svg("line",{x1:45,y1:243,x2:520,y2:243,stroke:"currentColor"}),svg("line",{x1:45,y1:40,x2:45,y2:243,stroke:"currentColor"}));
 plot.appendChild(svg("line",{x1:px(xmin),y1:py(s.intercept+s.slope*xmin),x2:px(xmax),y2:py(s.intercept+s.slope*xmax),stroke:"#0f766e","stroke-width":2}));
 s.xs.forEach((xi,i)=>{plot.appendChild(svg("line",{x1:px(xi),y1:py(s.fitted[i]),x2:px(xi),y2:py(s.ys[i]),stroke:"#c2410c","stroke-dasharray":"4 3","stroke-width":2}));plot.appendChild(svg("circle",{cx:px(xi),cy:py(s.ys[i]),r:4.5,fill:"#1d4ed8"}));});
 plot.setAttribute("aria-label","OLS residuals: "+s.residuals.map((v,i)=>"point "+(i+1)+" residual "+fmt(v)).join("; "));
}
function render(){
 const a=parse(x.value),b=parse(y.value),s=a&&b?compute(a,b):null;
 x.setAttribute("aria-invalid",String(!a||!b||!s));y.setAttribute("aria-invalid",String(!b||!a||!s));
 if(!s){error.textContent="Enter matching lists of 3–12 finite numbers within ±1000. Predictor values must vary and observed outcomes cannot all be equal.";error.hidden=false;results.hidden=true;get("plot").replaceChildren();return;}
 error.textContent="";error.hidden=true;results.hidden=false;
 for(const key of ["intercept","slope","sse","r2"])get(key).textContent=fmt(s[key]);
 const rows=s.xs.map((xi,i)=>{const tr=document.createElement("tr");for(const v of [xi,s.ys[i],s.fitted[i],s.residuals[i]]){const td=document.createElement("td");td.textContent=fmt(v);tr.appendChild(td);}return tr;});
 get("table").replaceChildren(...rows);get("interpretation").textContent="The line minimizes the sum of squared vertical residuals. Inspect how the fitted slope, SSE and R² change after editing an observation.";draw(s);
}
x.addEventListener("input",render);y.addEventListener("input",render);
get("base").addEventListener("click",()=>{x.value="1, 2, 3, 4, 5";y.value="2, 4, 5, 4, 5";render()});
get("outlier").addEventListener("click",()=>{x.value="1, 2, 3, 4, 5";y.value="2, 4, 5, 4, 15";render()});
render();
})();