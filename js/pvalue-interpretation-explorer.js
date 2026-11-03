/* Batch #77: independent standard-normal p-value visualization; accurate gamma-tail calculation. */
(function(){
"use strict";
const lanczos=[0.99999999999980993,676.5203681218851,-1259.1392167224028,771.32342877765313,
 -176.61502916214059,12.507343278686905,-0.13857109526572012,9.984369578019572e-6,1.5056327351493116e-7];
function logGamma(z){
 if(!(z>0)||!Number.isFinite(z))return NaN;
 if(z<.5)return Math.log(Math.PI)-Math.log(Math.sin(Math.PI*z))-logGamma(1-z);
 z-=1;let a=lanczos[0];for(let i=1;i<lanczos.length;i++)a+=lanczos[i]/(z+i);
 const t=z+7.5;return .5*Math.log(2*Math.PI)+(z+.5)*Math.log(t)-t+Math.log(a);
}
// Q(a,x)=Γ(a,x)/Γ(a); lower-series when x<a+1, upper continued fraction otherwise.
function gammaQ(a,x){
 if(!Number.isFinite(x)||x<0||!(a>0))return NaN;
 if(x===0)return 1;
 const factor=Math.exp(a*Math.log(x)-x-logGamma(a));
 if(x<a+1){
  let term=1/a,sum=term;
  for(let i=1;i<=1000;i++){term*=x/(a+i);sum+=term;if(Math.abs(term)<=Math.abs(sum)*2e-15)break;}
  return Math.min(1,Math.max(0,1-sum*factor));
 }
 let b=x+1-a,c=1e300,d=1/Math.max(b,1e-300),h=d;
 for(let i=1;i<=1000;i++){
  const an=-i*(i-a);b+=2;d=an*d+b;if(Math.abs(d)<1e-300)d=1e-300;
  c=b+an/c;if(Math.abs(c)<1e-300)c=1e-300;
  d=1/d;const delta=d*c;h*=delta;
  if(Math.abs(delta-1)<2e-15)break;
 }
 return Math.min(1,Math.max(0,factor*h));
}
const positiveTail=x=>.5*gammaQ(.5,x*x/2);
function pvalue(z,side){
 if(!Number.isFinite(z)||Math.abs(z)>35||!["left","right","two-sided"].includes(side))return null;
 const tail=positiveTail(Math.abs(z));
 return side==="two-sided"?2*tail:side==="right"?(z>=0?tail:1-tail):(z<=0?tail:1-tail);
}
window.esaPvalueMath={pvalue,gammaQ};
const root=document.getElementById("esa-pvalue-explorer");if(!root)return;
const get=k=>root.querySelector("#esa-p-"+k),zInput=get("z"),side=get("side"),alpha=get("alpha"),graph=get("chart");
const ns="http://www.w3.org/2000/svg";
function node(tag,props={},text){const e=document.createElementNS(ns,tag);Object.entries(props).forEach(([k,v])=>e.setAttribute(k,String(v)));if(text!==undefined)e.textContent=text;return e;}
function draw(z,mode,p){
 const xPixel=x=>36+(x+4.5)/9*548,yPixel=x=>207-175*Math.exp(-x*x/2);
 const l=-4.5,r=4.5;
 const pieces=[node("title",{},"Standard normal distribution and highlighted rejection-side probability"),
 node("desc",{},"Blue shading shows area more extreme than the observed statistic under the selected alternative; values beyond the displayed axis are included in the calculated probability."),
 node("line",{x1:36,x2:584,y1:207,y2:207,stroke:"currentColor"})];
 let outline="",shade="";
 for(let i=0;i<=360;i++){const x=l+(r-l)*i/360;outline+=(i?"L":"M")+xPixel(x).toFixed(2)+","+yPixel(x).toFixed(2);}
 pieces.push(node("path",{d:outline,fill:"none",stroke:"#0f766e","stroke-width":2}));
 function area(from,to){from=Math.max(l,from);to=Math.min(r,to);if(to<=from)return;
  let d="M"+xPixel(from)+",207";const num=Math.max(1,Math.ceil((to-from)/.025));
  for(let i=0;i<=num;i++){const x=from+(to-from)*i/num;d+="L"+xPixel(x).toFixed(3)+","+yPixel(x).toFixed(3);}
  d+="L"+xPixel(to)+",207Z";pieces.push(node("path",{d,fill:"#2563eb","fill-opacity":".35"}));}
 if(mode==="left")area(l,z);
 else if(mode==="right")area(z,r);
 else{area(l,-Math.abs(z));area(Math.abs(z),r);}
 if(z>=l&&z<=r)pieces.push(node("line",{x1:xPixel(z),x2:xPixel(z),y1:36,y2:207,stroke:"#b45309","stroke-width":2,"stroke-dasharray":"5 4"}));
 for(let t=-4;t<=4;t+=2)pieces.push(node("text",{x:xPixel(t),y:223,fill:"currentColor","text-anchor":"middle","font-size":12},String(t)));
 graph.replaceChildren(...pieces);
 graph.setAttribute("aria-label","Standard normal curve; observed z "+z.toFixed(3)+
 "; "+mode+" p-value "+p.toExponential(5)+". Highlighted probability tails, plot from -4.5 to +4.5.");
}
function render(){
 const z=zInput.value.trim()===""?NaN:Number(zInput.value),a=Number(alpha.value),p=pvalue(z,side.value);
 const err=get("error"),results=get("results");
 if(p===null||![.01,.05,.1].includes(a)){err.hidden=false;results.hidden=true;graph.hidden=true;return;}
 err.hidden=true;results.hidden=false;graph.hidden=false;
 get("prob").textContent=p<.000001?p.toExponential(6):p.toFixed(7);
 get("decision").textContent=(p<a?"Reject":"Do not reject")+" the null at α = "+a.toFixed(2)+
 " (only under the assumed normal null model). A p-value is not the probability that the null hypothesis is true.";
 draw(z,side.value,p);
}
[zInput,side,alpha].forEach(input=>input.addEventListener("input",render));
get("reset").addEventListener("click",()=>{zInput.value="2";side.value="two-sided";alpha.value=".05";render();});
render();
})();