/* Easy Statistics Academy Batch #83: exact three-point discrete moments. */
(function(){
"use strict";
function calculate(x,p){
 if(!Array.isArray(x)||!Array.isArray(p)||x.length!==3||p.length!==3||
    x.some(v=>!Number.isFinite(v)||Math.abs(v)>1000000)||
    p.some(v=>!Number.isFinite(v)||v<0||v>1))return null;
 const sum=p.reduce((a,v)=>a+v,0);
 if(Math.abs(sum-1)>1e-9)return null;
 const mean=x.reduce((a,v,i)=>a+v*p[i],0);
 const second=x.reduce((a,v,i)=>a+v*v*p[i],0);
 const variance=x.reduce((a,v,i)=>a+p[i]*(v-mean)**2,0);
 return {sum,mean,second,variance,sd:Math.sqrt(variance)};
}
window.esaThreePointMomentsMath={calculate};
const root=document.getElementById("esa-moments-lab");if(!root)return;
const ar=root.getAttribute("lang")==="ar",get=k=>root.querySelector("#esa-mom-"+k);
const ns="http://www.w3.org/2000/svg",elt=(tag,attrs={},content)=>{
 const el=document.createElementNS(ns,tag);
 for(const [k,v] of Object.entries(attrs))el.setAttribute(k,String(v));
 if(content!==undefined)el.textContent=String(content);
 return el;
};
function update(){
 const ids=["x0","x1","x2","p0","p1","p2"];
 const values=ids.map(k=>get(k).value.trim()===""?NaN:Number(get(k).value));
 const out=calculate(values.slice(0,3),values.slice(3));
 get("error").hidden=!!out;get("results").hidden=!out;
 get("chart").hidden=!out;get("chart").style.display=out?"block":"none";
 ids.forEach(k=>get(k).setAttribute("aria-invalid",out?"false":"true"));
 if(!out){get("error").textContent=ar?"أدخل ثلاث قيم منتهية واحتمالات بين صفر وواحد مجموعها يساوي واحداً.":"Enter three finite outcomes and probabilities between 0 and 1 that sum to exactly 1.";return;}
 for(const k of ["sum","mean","second","variance","sd"])get(k).textContent=out[k].toFixed(6);
 const [x0,x1,x2,p0,p1,p2]=values;
 const chart=get("chart"),mx=Math.max(1,p0,p1,p2);
 const bars=[p0,p1,p2].map((p,i)=>{
  const left=55+i*150,y=171-130*p/mx;
  return [elt("rect",{x:left,y,width:75,height:171-y,fill:"#0f766e"}),elt("text",{x:left+37,y:191,"text-anchor":"middle","font-size":12,fill:"currentColor"},String(values[i])),elt("text",{x:left+37,y:y-6,"text-anchor":"middle","font-size":12,fill:"currentColor"},p.toFixed(3))];
 }).flat();
 chart.replaceChildren(elt("title",{},ar?"دالة الكتلة الاحتمالية":"Probability mass function"),elt("desc",{},ar?"ثلاثة أعمدة تمثل احتمالات النتائج المختارة.":"Three bars display the selected outcome probabilities."),elt("line",{x1:25,x2:470,y1:171,y2:171,stroke:"currentColor"}),...bars);
 chart.setAttribute("aria-label",(ar?"قيم النتائج واحتمالاتها: ":"Outcomes and probabilities: ")+values.slice(0,3).map((x,i)=>x+": "+values[i+3].toFixed(3)).join("; "));
}
["x0","x1","x2","p0","p1","p2"].forEach(k=>get(k).addEventListener("input",update));
get("reset").addEventListener("click",()=>{
 const defaults={x0:"0",x1:"1",x2:"2",p0:"0.2",p1:"0.5",p2:"0.3"};
 Object.entries(defaults).forEach(([k,v])=>get(k).value=v);update();
});
update();
})();