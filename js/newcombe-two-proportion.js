/* Batch #85 — Newcombe (1998) method 10, unpaired Wilson score difference interval. */
(function(){
"use strict";
const Z=Object.freeze({90:1.6448536269514722,95:1.959963984540054,99:2.5758293035489004});
function wilson(x,n,z){
 if(!Number.isSafeInteger(x)||!Number.isSafeInteger(n)||n<1||x<0||x>n||!Number.isFinite(z)||z<=0)return null;
 const p=x/n,z2=z*z,den=1+z2/n;
 const center=(p+z2/(2*n))/den;
 const radius=z*Math.sqrt(p*(1-p)/n+z2/(4*n*n))/den;
 return [Math.max(0,center-radius),Math.min(1,center+radius)];
}
function compare(x1,n1,x2,n2,level){
 const z=Z[level];
 if(z===undefined)return null;
 const one=wilson(x1,n1,z),two=wilson(x2,n2,z);
 if(!one||!two)return null;
 const p1=x1/n1,p2=x2/n2,d=p1-p2;
 const se=Math.sqrt(p1*(1-p1)/n1+p2*(1-p2)/n2);
 const wald=[d-z*se,d+z*se];
 // Newcombe method 10 combines Wilson score endpoints with squared distances.
 // This is NOT the overly conservative [L1-U2,U1-L2] interval.
 const newcombe=[d-Math.hypot(p1-one[0],two[1]-p2),
                 d+Math.hypot(one[1]-p1,p2-two[0])];
 return {difference:d,wald,newcombe,wilson1:one,wilson2:two,level};
}
window.esaNewcombeMath={wilson,compare};
const root=document.getElementById("esa-two-proportion-ci-calculator");
if(!root)return;
const get=id=>root.querySelector("#esa-prop-"+id);
const inputKeys=["x1","n1","x2","n2"];
const fields=inputKeys.map(get),level=get("level");
function update(){
 const vals=fields.map(el=>el.value.trim()===""?NaN:Number(el.value));
 const result=compare(...vals,Number(level.value));
 const display=get("newcombe-results"),error=get("newcombe-error");
 display.hidden=!result;
 error.hidden=!!result;
 fields.forEach(el=>el.setAttribute("aria-invalid",result?"false":"true"));
 if(!result){error.textContent="Enter valid integer successes and positive sample sizes for both groups to compare intervals.";get("compare-chart").replaceChildren();return;}
 error.textContent="";
 get("newcombe-lower").textContent=(result.newcombe[0]*100).toFixed(4);
 get("newcombe-upper").textContent=(result.newcombe[1]*100).toFixed(4);
 get("newcombe-level").textContent=String(result.level);
 get("newcombe-zero").textContent=result.newcombe[0]<=0&&result.newcombe[1]>=0?
  "Newcombe interval includes zero; equal population proportions are not excluded by this interval.":
  "Newcombe interval excludes zero; interpretation still requires the sampling assumptions.";
 const chart=get("compare-chart"),ns="http://www.w3.org/2000/svg";
 chart.replaceChildren();
 const pad=.015,min=Math.min(0,result.wald[0],result.newcombe[0])-pad,max=Math.max(0,result.wald[1],result.newcombe[1])+pad;
 const scale=x=>52+388*(x-min)/(max-min);
 const el=(tag,attrs,label)=>{const e=document.createElementNS(ns,tag);Object.entries(attrs).forEach(([k,v])=>e.setAttribute(k,String(v)));if(label!==undefined)e.textContent=String(label);chart.append(e);};
 el("line",{x1:scale(0),x2:scale(0),y1:14,y2:105,stroke:"currentColor","stroke-dasharray":"4 4"});
 for(const [i,pair] of [result.wald,result.newcombe].entries()){
  const y=39+i*48;
  el("text",{x:8,y:y-13,"font-size":12,fill:"currentColor"},i?"Newcombe":"Wald");
  el("line",{x1:scale(pair[0]),x2:scale(pair[1]),y1:y,y2:y,stroke:i?"#0f766e":"#4267b2","stroke-width":4});
  for(const x of pair)el("circle",{cx:scale(x),cy:y,r:4,fill:i?"#0f766e":"#4267b2"});
 }
 chart.setAttribute("aria-label",result.level+"% intervals in percentage points. Wald "+(100*result.wald[0]).toFixed(2)+" to "+(100*result.wald[1]).toFixed(2)+"; Newcombe "+(100*result.newcombe[0]).toFixed(2)+" to "+(100*result.newcombe[1]).toFixed(2)+". Vertical reference marks zero.");
}
[...fields,level].forEach(el=>{el.addEventListener("input",update);el.addEventListener("change",update);});
get("reset").addEventListener("click",()=>queueMicrotask(update));
update();
})();