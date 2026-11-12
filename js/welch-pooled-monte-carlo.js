/* Batch #89: deterministic Monte Carlo experiment for independent normal samples. No external calls. */
(function(){
"use strict";
function rng(seed){
 let state=seed>>>0;
 if(!state)state=0x6d2b79f5;
 return function(){state^=state<<13;state^=state>>>17;state^=state<<5;return ((state>>>0)+.5)/4294967296;};
}
function normal(random){
 const u=random(),v=random();
 return Math.sqrt(-2*Math.log(u))*Math.cos(2*Math.PI*v);
}
function validate(o){
 return o&&Number.isInteger(o.n1)&&o.n1>=5&&o.n1<=100&&
 Number.isInteger(o.n2)&&o.n2>=5&&o.n2<=100&&
 Number.isFinite(o.sd1)&&o.sd1>=.2&&o.sd1<=5&&
 Number.isFinite(o.sd2)&&o.sd2>=.2&&o.sd2<=5&&
 Number.isFinite(o.effect)&&Math.abs(o.effect)<=3&&
 Number.isInteger(o.reps)&&o.reps>=100&&o.reps<=1200&&
 Number.isSafeInteger(o.seed)&&o.seed>=1&&o.seed<=2147483647;
}
function simulate(o){
 if(!validate(o)||!window.esaWelchMath||!window.esaPooledTMath)return null;
 const rand=rng(o.seed);
 const counts={nullWelch:0,nullPooled:0,altWelch:0,altPooled:0};
 let valid=0;
 for(let i=0;i<o.reps;i++){
  const a=Array.from({length:o.n1},()=>o.sd1*normal(rand));
  const b=Array.from({length:o.n2},()=>o.sd2*normal(rand));
  const aAlt=a.map(v=>v+o.effect);
  const w0=window.esaWelchMath.compute(a,b),p0=window.esaPooledTMath.compute(a,b);
  const w1=window.esaWelchMath.compute(aAlt,b),p1=window.esaPooledTMath.compute(aAlt,b);
  if(!w0||!p0||!w1||!p1||w0.degenerate||p0.degenerate||w1.degenerate||p1.degenerate)return null;
  valid++;
  if(w0.p<.05)counts.nullWelch++;
  if(p0.p<.05)counts.nullPooled++;
  if(w1.p<.05)counts.altWelch++;
  if(p1.p<.05)counts.altPooled++;
 }
 const result={};
 for(const [k,c]of Object.entries(counts)){
  const estimate=c/valid;
  result[k]={count:c,rate:estimate,mcse:Math.sqrt(estimate*(1-estimate)/valid)};
 }
 return {reps:valid,seed:o.seed,parameters:{...o},...result};
}
window.esaT89Simulation={simulate,rng,normal};
const root=document.getElementById("esa-t89-simulation");
if(!root)return;
const field=id=>root.querySelector("#esa-sim-"+id);
const ids=["n1","n2","sd1","sd2","effect","reps","seed"];
const status=field("status"),results=field("results"),chart=field("chart");
function read(){
 const o={};for(const id of ids)o[id]=Number(field(id).value);
 if(ids.some(id=>field(id).value.trim()===""))return null;
 return validate(o)?o:null;
}
function draw(r){
 chart.replaceChildren();
 const ns="http://www.w3.org/2000/svg";
 function add(tag,attrs,label){
  const e=document.createElementNS(ns,tag);
  for(const [k,v]of Object.entries(attrs||{}))e.setAttribute(k,String(v));
  if(label!==undefined)e.textContent=label;
  chart.append(e);
 }
 add("title",{},"Monte Carlo rejection proportions for Welch and pooled t tests");
 add("desc",{},"Four horizontal bars show estimated rejection rates under the null and under the specified effect. Rates are Monte Carlo estimates.");
 const specs=[["nullWelch","Null · Welch"],["nullPooled","Null · pooled"],["altWelch","Alternative · Welch"],["altPooled","Alternative · pooled"]];
 specs.forEach(([key,name],i)=>{
  const y=20+i*42,rate=r[key].rate;
  add("text",{x:8,y:y+12,fill:"currentColor","font-size":12},name);
  add("rect",{x:187,y:y-2,width:Math.max(0,rate*335),height:17,fill:i%2?"#2563eb":"#0f766e"});
  add("text",{x:530,y:y+12,fill:"currentColor","font-size":12},(100*rate).toFixed(1)+"%");
 });
 add("line",{x1:187+335*.05,x2:187+335*.05,y1:7,y2:177,stroke:"currentColor","stroke-dasharray":"3 3"});
 chart.setAttribute("aria-label",specs.map(([k,name])=>name+": "+(100*r[k].rate).toFixed(1)+" percent").join("; "));
}
function render(){
 const o=read();
 for(const id of ids)field(id).setAttribute("aria-invalid",o?"false":"true");
 if(!o){results.hidden=true;status.hidden=false;status.textContent="Enter valid bounded values for every field. Replications: 100–1200; sample sizes: 5–100; standard deviations: 0.2–5; seed: 1–2147483647.";return;}
 status.hidden=false;status.textContent="Calculating seeded Monte Carlo estimates…";
 const r=simulate(o);
 if(!r){results.hidden=true;status.textContent="The simulation could not calculate finite test statistics. Change the inputs.";return;}
 results.hidden=false;
 status.textContent="Completed "+r.reps+" seeded replications. Values are estimates, not exact probabilities.";
 for(const key of ["nullWelch","nullPooled","altWelch","altPooled"]){
  const x=r[key];field(key).textContent=(100*x.rate).toFixed(2)+"% (MC SE "+(100*x.mcse).toFixed(2)+" pp; "+x.count+"/"+r.reps+")";
 }
 draw(r);
}
field("run").addEventListener("click",render);
field("reset").addEventListener("click",()=>{
 const defaults={n1:12,n2:30,sd1:1,sd2:2,effect:1,reps:300,seed:2026};
 for(const [key,value]of Object.entries(defaults))field(key).value=String(value);
 render();
});
render();
})();