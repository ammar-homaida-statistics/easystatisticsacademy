/* Batch #84: independent three-point affine transformation laboratory. */
(function(){
"use strict";
function calculate(x,p,a,b){
 if(!Array.isArray(x)||!Array.isArray(p)||x.length!==3||p.length!==3 ||
 x.some(v=>!Number.isFinite(v)||Math.abs(v)>10000)||
 p.some(v=>!Number.isFinite(v)||v<0||v>1)||
 !Number.isFinite(a)||!Number.isFinite(b)||Math.abs(a)>10000||Math.abs(b)>10000)return null;
 const total=p.reduce((s,v)=>s+v,0);if(Math.abs(total-1)>1e-9)return null;
 const y=x.map(v=>a+b*v);
 const mean=x.reduce((s,v,i)=>s+v*p[i],0);
 const variance=x.reduce((s,v,i)=>s+p[i]*(v-mean)**2,0);
 const meanY=y.reduce((s,v,i)=>s+v*p[i],0);
 const varianceY=y.reduce((s,v,i)=>s+p[i]*(v-meanY)**2,0);
 return {mean,variance,sd:Math.sqrt(variance),meanY,varianceY,sdY:Math.sqrt(varianceY),rule:b*b*variance,y};
}
window.esaAffineVarianceMath={calculate};
const root=document.getElementById("esa-affine-lab");if(!root)return;
const get=id=>root.querySelector("#esa-affine-"+id);
const ids=["x0","x1","x2","p0","p1","p2","a","b"], ns="http://www.w3.org/2000/svg";
function render(x,p,y){
 const svg=get("chart");svg.replaceChildren();
 const node=(tag,attrs,label)=>{const el=document.createElementNS(ns,tag);for(const [k,v] of Object.entries(attrs))el.setAttribute(k,String(v));if(label!==undefined)el.textContent=String(label);svg.append(el);};
 for(let j=0;j<2;j++){
  const vals=j?y:x,base=j?164:78;
  node("text",{x:8,y:base-54,"font-size":13,fill:"currentColor"},j?"Transformed Y":"Original X");
  p.forEach((prob,i)=>{const cx=76+i*148,h=prob*49;
   node("rect",{x:cx-20,y:base-h,width:40,height:h,fill:j?"#147d70":"#4267b2"});
   node("text",{x:cx,y:base+13,"text-anchor":"middle","font-size":12,fill:"currentColor"},Number(vals[i].toPrecision(5)));
   node("text",{x:cx,y:base-h-4,"text-anchor":"middle","font-size":11,fill:"currentColor"},prob.toFixed(2));
  });
 }
 svg.setAttribute("aria-label","PMF: original outcomes "+x.join(", ")+"; transformed outcomes "+y.join(", ")+"; probabilities "+p.join(", "));
}
function update(){
 const values=ids.map(k=>get(k).value.trim()===""?NaN:Number(get(k).value));
 const x=values.slice(0,3),p=values.slice(3,6),a=values[6],b=values[7],out=calculate(x,p,a,b);
 get("error").hidden=!!out;get("results").hidden=!out;get("chart").hidden=!out;
 ids.forEach(k=>get(k).setAttribute("aria-invalid",out?"false":"true"));
 if(!out){get("error").textContent="Enter three outcomes and constants between −10,000 and 10,000, and three probabilities between 0 and 1 summing to one.";get("chart").replaceChildren();return;}
 get("error").textContent="";
 for(const [k,v] of Object.entries({mx:out.mean,vx:out.variance,sx:out.sd,my:out.meanY,vy:out.varianceY,sy:out.sdY,rule:out.rule}))get(k).textContent=v.toFixed(6);
 render(x,p,out.y);
}
ids.forEach(k=>get(k).addEventListener("input",update));
get("reset").addEventListener("click",()=>{[0,1,2,.2,.5,.3,3,-2].forEach((v,i)=>get(ids[i]).value=String(v));update();});
update();
})();