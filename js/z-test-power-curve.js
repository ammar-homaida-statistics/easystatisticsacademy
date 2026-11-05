/* Batch #81: two-sided normal Z power, known population sigma, independent sample.
   Pure math is exposed before DOM initialization for independent benchmarks. */
(function(){
"use strict";
// Cephes-style rational approximation for erf/erfc, accurate in normal tails.
const T=[9.60497373987051638749,90.0260197203842689217,2232.00534594684319226,7003.32514112805075473,55592.3013010394962768];
const U=[33.5617141647503099647,521.357949780152679795,4594.32382970980127987,22629.0000613890934246,49267.3942608635921086];
const P=[2.46196981473530512524e-10,.564189564831068821977,7.46321056442269912687,48.6371970985681366614,196.520832956077098242,526.445194995477358631,934.52852717195760754,1027.55188689515710272,557.535335369399327526];
const Q=[13.2281951154744992508,86.7072140885989742329,354.937778887819891062,975.708501743205489753,1823.90916687909736289,2246.33760818710981792,1656.66309194161350182,557.535340817727675546];
const R=[.564189583547755073984,1.27536670759978104416,5.01905042251180477414,6.16021097993053585195,7.40974269950448939160,2.97886665372100240670];
const S=[2.26052863220117276590,9.39603524938001434673,12.0489539808096656605,17.0814450747565897222,9.60896809063285878198,3.36907645100081516050];
function polevl(x,a){let y=a[0];for(let i=1;i<a.length;i++)y=y*x+a[i];return y;}
function p1evl(x,a){let y=x+a[0];for(let i=1;i<a.length;i++)y=y*x+a[i];return y;}
function erfcPositive(x){
 if(x<0)return 2-erfcPositive(-x);
 if(x<1){const y=x*polevl(x*x,T)/p1evl(x*x,U);return 1-y;}
 if(x>27)return 0;
 const value=x<8?polevl(x,P)/p1evl(x,Q):polevl(x,R)/p1evl(x,S);
 return Math.exp(-x*x)*value;
}
function normalCDF(z){
 if(!Number.isFinite(z))return NaN;
 return z<0?0.5*erfcPositive(-z/Math.SQRT2):1-0.5*erfcPositive(z/Math.SQRT2);
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
const get=k=>root.querySelector("#esa-pcurve-"+k);
const ns="http://www.w3.org/2000/svg";
function node(tag,attrs={},content){const e=document.createElementNS(ns,tag);Object.entries(attrs).forEach(([k,v])=>e.setAttribute(k,String(v)));if(content!==undefined)e.textContent=String(content);return e;}
function render(){
 const effectRaw=get("effect").value.trim(),nRaw=get("n").value.trim();
 const result=power(effectRaw===""?NaN:Number(effectRaw),nRaw===""?NaN:Number(nRaw),Number(get("alpha").value));
 const error=get("error"),out=get("results"),chart=get("chart");
 error.hidden=!!result;out.hidden=!result;chart.hidden=!result;
 // SVG display:block overrides the UA [hidden] rule; explicitly hide invalid charts.
 chart.style.display=result?"block":"none";
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