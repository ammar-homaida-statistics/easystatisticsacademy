/* Batch #87 — Practical significance teaching explorer, Student t engine reused. */
(function(){
"use strict";
function compute(n,mean,sd,mu0,threshold){
 if(!Number.isSafeInteger(n)||n<2||n>1000000||![mean,sd,mu0,threshold].every(Number.isFinite)||
    sd<=0||sd>1e9||Math.abs(mean)>1e9||Math.abs(mu0)>1e9||threshold<0||threshold>1e9)return null;
 const engine=window.esaStudentTMath;
 if(!engine||typeof engine.compute!=="function")return null;
 const t=engine.compute(n,mean,sd,mu0,"two-sided");
 if(!t)return null;
 const difference=mean-mu0,d=difference/sd;
 return {n,difference,d,t:t.t,df:t.df,pvalue:t.pvalue,
  statistical:t.pvalue<=0.05,practical:Math.abs(difference)>=threshold,
  lower:t.lower-mu0,upper:t.upper-mu0,threshold};
}
window.esaPracticalMath={compute};
const root=document.getElementById("esa-practical-significance-lab");if(!root)return;
const get=id=>root.querySelector("#esa-ps-"+id);
const keys=["n","mean","sd","mu0","threshold"],inputs=keys.map(get);
function update(){
 const vals=inputs.map(el=>el.value.trim()===""?NaN:Number(el.value));
 const r=compute(...vals),out=get("results"),error=get("error"),graph=get("graph");
 for(const el of inputs)el.setAttribute("aria-invalid",r?"false":"true");
 if(!r){error.hidden=false;error.textContent="Enter valid sample size (2–1,000,000), finite means, positive sample SD and a nonnegative practical threshold, all within the displayed bounds.";out.hidden=true;graph.hidden=true;graph.replaceChildren();return;}
 error.hidden=true;error.textContent="";out.hidden=false;graph.hidden=false;
 for(const [name,num] of Object.entries({t:r.t,df:r.df,p:r.pvalue,d:r.d,effect:r.difference,low:r.lower,high:r.upper})){
  get(name).textContent=name==="df"?String(num):Number(num).toFixed(6);
 }
 get("statistical").textContent=r.statistical?"Statistically significant at 5% (conditional on assumptions).":"Not statistically significant at 5%; this does not establish no effect.";
 get("practical").textContent=r.practical?"Observed absolute difference meets the chosen practical threshold.":"Observed absolute difference is below the chosen practical threshold.";
 get("interpret").textContent="This descriptive threshold comparison is NOT a formal equivalence or minimum-effect test. Evaluate the confidence interval and study context: an interval that crosses ± the practical threshold leaves practical importance uncertain. Cohen's d is a standardized descriptive effect size; its importance is context-dependent.";
 const svgNS="http://www.w3.org/2000/svg";graph.replaceChildren();
 const pad=Math.max(.15,Math.abs(r.difference)*.25,r.threshold*.25);
 const xmin=Math.min(r.lower,-r.threshold,0)-pad,xmax=Math.max(r.upper,r.threshold,0)+pad;
 const x=v=>40+(v-xmin)*410/(xmax-xmin);
 function el(tag,attrs,text){const node=document.createElementNS(svgNS,tag);for(const [k,v] of Object.entries(attrs))node.setAttribute(k,String(v));if(text!==undefined)node.textContent=String(text);graph.append(node);}
 for(const v of [-r.threshold,r.threshold])el("line",{x1:x(v),y1:8,x2:x(v),y2:104,stroke:"#b45309","stroke-dasharray":"5 4"});
 el("line",{x1:x(0),y1:8,x2:x(0),y2:104,stroke:"currentColor","stroke-dasharray":"2 3"});
 el("line",{x1:x(r.lower),x2:x(r.upper),y1:57,y2:57,stroke:"#0f766e","stroke-width":5});
 for(const v of [r.lower,r.upper])el("circle",{cx:x(v),cy:57,r:4,fill:"#0f766e"});
 el("circle",{cx:x(r.difference),cy:57,r:6,fill:"#2563eb"});
 el("text",{x:9,y:118,"font-size":10,fill:"currentColor"},"95% CI for mean difference; dashed orange = ± practical threshold");
 graph.setAttribute("aria-label","95% Student t interval for mean difference "+r.lower.toFixed(3)+" to "+r.upper.toFixed(3)+"; observed difference "+r.difference.toFixed(3)+"; practical threshold plus or minus "+r.threshold.toFixed(3)+".");
}
inputs.forEach(el=>{el.addEventListener("input",update);el.addEventListener("change",update);});
get("reset").addEventListener("click",()=>{for(const [id,v] of Object.entries({n:"400",mean:"0.2",sd:"1",mu0:"0",threshold:"0.5"}))get(id).value=v;update();});
update();
})();