/* Batch #81: two-sided normal Z power, known population sigma, independent sample.
   Pure math is exposed before DOM initialization for independent benchmarks. */
(function(){
"use strict";
function normalCDF(z){
 if(!Number.isFinite(z))return NaN;
 const x=Math.abs(z),t=1/(1+0.2316419*x);
 const phi=Math.exp(-x*x/2)/Math.sqrt(2*Math.PI);
 const p=1-phi*t*(0.319381530+t*(-0.356563782+t*(1.781477937+t*(-1.821255978+t*1.330274429))));
 return z>=0?p:1-p;
}
function inverseCDF(p){
 if(!Number.isFinite(p)||p<=0||p>=1)return NaN;
 let low=-12,high=12;
 for(let i=0;i<80;i++){const mid=(low+high)/2;if(normalCDF(mid)<p)low=mid;else high=mid;}
 return (low+high)/2;
}
function power(effect,n,alpha){
 if(!Number.isFinite(effect)||Math.abs(effect)>3||!Number.isSafeInteger(n)||n<2||n>10000||
    ![0.01,0.05,0.1].includes(alpha))return null;
 const critical=inverseCDF(1-alpha/2),noncentrality=effect*Math.sqrt(n);
 const value=normalCDF(-critical-noncentrality)+normalCDF(noncentrality-critical);
 return {effect,n,alpha,critical,noncentrality,power:Math.min(1,Math.max(0,value)),beta:1-Math.min(1,Math.max(0,value))};
}
window.esaPowerCurveMath={normalCDF,inverseCDF,power};
const root=document.getElementById("esa-power-curve-lab");if(!root)return;
const get=k=>root.querySelector("#esa-power-"+k);
const ns="http://www.w3.org/2000/svg";
function node(tag,attrs={},content){const e=document.createElementNS(ns,tag);Object.entries(attrs).forEach(([k,v])=>e.setAttribute(k,String(v)));if(content!==undefined)e.textContent=String(content);return e;}
function render(){
 const effectRaw=get("effect").value.trim(),nRaw=get("n").value.trim();
 const result=power(effectRaw===""?NaN:Number(effectRaw),nRaw===""?NaN:Number(nRaw),Number(get("alpha").value));
 const error=get("error"),out=get("results"),chart=get("chart");
 error.hidden=!!result;out.hidden=!result;chart.hidden=!result;
 if(!result){error.textContent="Enter an effect size between -3 and 3, integer sample size from 2 to 10000, and an available significance level.";return;}
 for(const k of ["power","beta","critical"])get(k).textContent=result[k].toFixed(5);
 get("noncentrality").textContent=result.noncentrality.toFixed(4);
 const maxN=Math.max(100,Math.min(10000,Math.ceil(result.n*1.5/10)*10));
 const sx=n=>45+540*(n-2)/(maxN-2),sy=p=>200-160*p;
 const pts=[];for(let i=0;i<=100;i++){const n=Math.max(2,Math.round(2+(maxN-2)*i/100));pts.push([sx(n),sy(power(result.effect,n,result.alpha).power)]);}
 const shapes=[node("title",{},"Normal approximation power as sample size changes"),node("desc",{},"Two-sided Z test, fixed standardized effect and significance level. The point marks the selected sample size."),node("line",{x1:45,x2:585,y1:200,y2:200,stroke:"currentColor"}),node("line",{x1:45,x2:45,y1:40,y2:200,stroke:"currentColor"}),node("line",{x1:45,x2:585,y1:72,y2:72,stroke:"#64748b","stroke-dasharray":"5 5"}),node("text",{x:50,y:68,fill:"currentColor","font-size":11},"80% power"),node("polyline",{points:pts.map(p=>p.join(",")).join(" "),fill:"none",stroke:"#0f766e","stroke-width":3}),node("circle",{cx:sx(result.n),cy:sy(result.power),r:6,fill:"#b45309"}),node("text",{x:45,y:222,fill:"currentColor","font-size":12},"n = 2"),node("text",{x:585,y:222,fill:"currentColor","font-size":12,"text-anchor":"end"},"n = "+maxN)];
 chart.replaceChildren(...shapes);chart.setAttribute("aria-label","Power curve for standardized effect "+result.effect+", alpha "+result.alpha+". Selected sample size "+result.n+" gives power "+result.power.toFixed(4)+".");
}
["effect","n","alpha"].forEach(id=>get(id).addEventListener("input",render));
get("reset").addEventListener("click",()=>{get("effect").value="0.5";get("n").value="40";get("alpha").value="0.05";render();});
render();
})();