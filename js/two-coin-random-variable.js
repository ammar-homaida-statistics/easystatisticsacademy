/* Batch #78: two independent coin flips and X = number of heads.
   All computation is client-side; no requests or persistence. */
(function(){
"use strict";
const root=document.getElementById("esa-two-coin-rv");if(!root)return;
const get=x=>root.querySelector("#esa-rv-"+x);
const outcomes=[["TT",0],["TH",1],["HT",1],["HH",2]];
function distribution(p){
 if(!Number.isFinite(p)||p<0||p>1)return null;
 const probabilities=[(1-p)*(1-p),2*p*(1-p),p*p];
 const rows=outcomes.map(([o,x])=>({outcome:o,x,probability:(o[0]==="H"?p:1-p)*(o[1]==="H"?p:1-p)}));
 return {rows,probabilities,expectation:2*p,variance:2*p*(1-p)};
}
window.esaTwoCoinRVMath={distribution};
function render(){
 const raw=get("prob").value.trim(),p=raw===""?NaN:Number(raw),result=distribution(p);
 const error=get("error"),output=get("results");
 if(!result){error.hidden=false;output.hidden=true;return;}
 error.hidden=true;output.hidden=false;
 get("prob-label").textContent=(100*p).toFixed(0)+"%";
 for(const row of result.rows){
  const code=row.outcome.toLowerCase();
  get(code+"-x").textContent=String(row.x);
  get(code+"-p").textContent=row.probability.toFixed(4);
 }
 for(let x=0;x<=2;x++)get("x"+x).textContent=result.probabilities[x].toFixed(4);
 get("mean").textContent=result.expectation.toFixed(4);
 get("variance").textContent=result.variance.toFixed(4);
 get("sum").textContent=result.probabilities.reduce((a,c)=>a+c,0).toFixed(4);
 const svg=get("chart"),ns="http://www.w3.org/2000/svg";
 const node=(tag,props,text)=>{let el=document.createElementNS(ns,tag);for(const [k,v] of Object.entries(props))el.setAttribute(k,String(v));if(text!==undefined)el.textContent=text;return el;};
 const parts=[node("title",{},"توزيع عدد مرات ظهور الصورة في رميتين مستقلتين"),node("line",{x1:35,y1:178,x2:430,y2:178,stroke:"currentColor"})];
 for(let x=0;x<=2;x++){const q=result.probabilities[x],x0=80+136*x;
  parts.push(node("rect",{x:x0,y:178-135*q,width:67,height:135*q,fill:"#0f766e"}));
  parts.push(node("text",{x:x0+33,y:195,"text-anchor":"middle",fill:"currentColor","font-size":15},String(x)));
  parts.push(node("text",{x:x0+33,y:Math.max(15,173-135*q),"text-anchor":"middle",fill:"currentColor","font-size":13},q.toFixed(3)));
 }
 svg.replaceChildren(...parts);svg.setAttribute("aria-label","احتمالات X تساوي صفر وواحد واثنين: "+result.probabilities.map(q=>q.toFixed(4)).join("، "));
}
get("prob").addEventListener("input",render);
get("reset").addEventListener("click",()=>{get("prob").value="0.5";render();});
render();
})();