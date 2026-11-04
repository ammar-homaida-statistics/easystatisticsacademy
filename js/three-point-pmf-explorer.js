/* Batch #80: a validated finite three-point probability mass function. */
(function(){
"use strict";
function compute(weights,values=[0,1,2]){
 if(!Array.isArray(weights)||weights.length!==3||!Array.isArray(values)||values.length!==3||
  !weights.every(v=>Number.isFinite(v)&&v>=0&&v<=1)||!values.every(Number.isFinite))return null;
 const total=weights.reduce((s,v)=>s+v,0);
 if(Math.abs(total-1)>1e-9)return null;
 const mean=weights.reduce((s,p,i)=>s+p*values[i],0);
 const variance=weights.reduce((s,p,i)=>s+p*(values[i]-mean)**2,0);
 return {weights,total,mean,variance};
}
window.esaThreePointPMFMath={compute};
const root=document.getElementById("esa-three-pmf-lab");if(!root)return;
const get=id=>root.querySelector("#esa-pmf-"+id);
const ns="http://www.w3.org/2000/svg";
const node=(tag,attrs={},content)=>{const e=document.createElementNS(ns,tag);for(const [k,v] of Object.entries(attrs))e.setAttribute(k,String(v));if(content!==undefined)e.textContent=content;return e;};
function render(){
 const inputs=[0,1,2].map(i=>get("p"+i).value.trim());
 const numbers=inputs.map(s=>s===""?NaN:Number(s));
 const result=compute(numbers),error=get("error"),results=get("results"),plot=get("chart");
 error.hidden=!!result;results.hidden=!result;plot.hidden=!result;
 [0,1,2].forEach(i=>get("p"+i).setAttribute("aria-invalid",result?"false":"true"));
 if(!result){error.textContent="أدخل ثلاثة احتمالات بين 0 و1 مجموعها 1، دون قيم سالبة.";return;}
 get("sum").textContent=result.total.toFixed(4);
 get("mean").textContent=result.mean.toFixed(4);
 get("variance").textContent=result.variance.toFixed(4);
 const shapes=[node("title",{},"دالة الكتلة الاحتمالية لقيم X صفر وواحد واثنين"),
  node("desc",{},"المخطط يوضح الأعمدة الثلاثة عند القيم صفر وواحد واثنين مع احتمالاتها؛ تُعرض القيم أيضاً في مخرجات النص."),
  node("line",{x1:30,x2:450,y1:180,y2:180,stroke:"currentColor"})];
 result.weights.forEach((p,i)=>{
  const x=63+i*135;shapes.push(node("rect",{x,y:180-145*p,width:70,height:145*p,fill:"#0f766e"}));
  shapes.push(node("text",{x:x+35,y:199,"text-anchor":"middle",fill:"currentColor","font-size":14},String(i)));
  shapes.push(node("text",{x:x+35,y:Math.max(18,174-145*p),"text-anchor":"middle",fill:"currentColor","font-size":13},p.toFixed(3)));
 });
 plot.replaceChildren(...shapes);plot.setAttribute("aria-label","احتمالات القيم صفر وواحد واثنين: "+result.weights.map(p=>p.toFixed(3)).join("، "));
}
[0,1,2].forEach(i=>get("p"+i).addEventListener("input",render));
get("reset").addEventListener("click",()=>{["0.2","0.5","0.3"].forEach((v,i)=>get("p"+i).value=v);render();});
render();
})();