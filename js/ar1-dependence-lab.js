/* Batch #103: how serial dependence (stationary AR(1), lag-k correlation ρ^k) changes the
   variance of the sample mean, the effective sample size, and the real type I error rate
   of a z test that wrongly assumes independence. Bilingual (data-locale="ar"). */
(function(){
"use strict";
function erfc(x){
 if(x<0)return 2-erfc(-x);
 if(x<2.5){let sum=x,term=x;const x2=x*x;
  for(let n=1;n<200;n++){term*=-x2/n;const add=term/(2*n+1);sum+=add;if(Math.abs(add)<1e-17*Math.abs(sum))break;}
  return 1-2/Math.sqrt(Math.PI)*sum;}
 const TINY=1e-300;let f=x,C=x,D=0;
 for(let n=1;n<500;n++){const a=n/2;D=x+a*D;if(Math.abs(D)<TINY)D=TINY;C=x+a/C;if(Math.abs(C)<TINY)C=TINY;
  D=1/D;const del=C*D;f*=del;if(Math.abs(del-1)<1e-16)break;}
 return Math.exp(-x*x)/Math.sqrt(Math.PI)/f;
}
const upperNormal=z=>0.5*erfc(z/Math.SQRT2);
function zQuantile(tail){ // z with P(Z ≥ z) = tail, 0 < tail ≤ 0.5
 if(tail===0.5)return 0;let lo=0,hi=1;while(upperNormal(hi)>tail)hi*=2;
 for(let i=0;i<200;i++){const m=(lo+hi)/2;if(upperNormal(m)>tail)lo=m;else hi=m;if(hi-lo<=1e-15*hi)break;}
 return (lo+hi)/2;
}
/* Variance inflation factor n·Var(x̄)/σ² = 1 + 2 Σ_{k=1}^{n−1} (1 − k/n) ρ^k (direct summation). */
function inflation(n,rho){
 let s=0,p=1;for(let k=1;k<n;k++){p*=rho;s+=(1-k/n)*p;}
 return 1+2*s;
}
function compute(n,rho,alpha){
 if(!Number.isSafeInteger(n)||n<2||n>100000)return null;
 if(!Number.isFinite(rho)||rho<-0.95||rho>0.95)return null;
 if(!Number.isFinite(alpha)||alpha<0.001||alpha>0.5)return null;
 const vif=inflation(n,rho),ratio=Math.sqrt(vif),z=zQuantile(alpha/2);
 const typeI=Math.min(1,2*upperNormal(z/ratio));
 return {n,rho,alpha,vif,neff:n/vif,ratio,z,typeI,coverage:1-typeI};
}
window.esaAR1={compute,inflation,erfc,zQuantile};

const root=document.getElementById("esa-ar1-lab");if(!root)return;
const $=id=>document.getElementById("esa-ar1-"+id);
const AR=root.dataset.locale==="ar";
const T=AR?{err:"أدخل حجم عيّنة صحيحًا من 2 إلى 100,000، ومعامل ارتباط ρ بين −0.95 و0.95، وقيمة α بين 0.001 و0.5.",
 over:(e,a)=>"الاختبار الذي يتجاهل الارتباط يرفض فرضية صفرية صحيحة بنسبة "+e+" بدل "+a+"، والفترة «"+(100*(1-Number(a))).toFixed(1).replace(/\.0$/,"")+"%» أضيق مما ينبغي.",
 under:(e,a)=>"مع الارتباط السالب يبالغ الاختبار الساذج في تقدير الخطأ المعياري: يرفض بنسبة "+e+" فقط بدل "+a+"، فيصبح محافظًا ويفقد القوة.",
 same:"المشاهدات مستقلة (ρ = 0): الخطأ المعياري الساذج صحيح ومعدل الخطأ من النوع الأول يساوي α."}
:{err:"Enter a whole-number n from 2 to 100,000, a correlation ρ between −0.95 and 0.95, and α between 0.001 and 0.5.",
 over:(e,a)=>"A test that ignores the correlation rejects a true null hypothesis "+e+" of the time instead of "+a+", and its nominal "+(100*(1-Number(a))).toFixed(1).replace(/\.0$/,"")+"% interval is too narrow.",
 under:(e,a)=>"With negative correlation the naive standard error is too large: the test rejects only "+e+" of the time instead of "+a+", so it is conservative and loses power.",
 same:"Observations are independent (ρ = 0): the naive standard error is correct and the type I error rate equals α."};
const fmt=(x,d)=>x.toFixed(d).replace("-","−");
const fmtP=p=>p<1e-6?p.toExponential(3):p.toFixed(6);
function update(){
 const raw=["n","rho","alpha"].map(k=>$(k).value.trim());
 const r=raw.some(v=>v==="")?null:compute(Number(raw[0]),Number(raw[1]),Number(raw[2]));
 ["n","rho","alpha"].forEach(k=>$(k).setAttribute("aria-invalid",r?"false":"true"));
 if(!r){$("error").hidden=false;$("error").textContent=T.err;$("results").hidden=true;return;}
 $("error").hidden=true;$("error").textContent="";$("results").hidden=false;
 $("vif").textContent=fmt(r.vif,4);
 $("neff").textContent=r.neff.toFixed(1);
 $("ratio").textContent=fmt(r.ratio,4);
 $("typeI").textContent=fmtP(r.typeI);
 $("coverage").textContent=fmtP(r.coverage);
 const a=String(r.alpha),e=fmtP(r.typeI);
 $("note").textContent=r.rho===0?T.same:(r.vif>1?T.over(e,a):T.under(e,a));
}
function set(v){for(const k in v)$(k).value=v[k];update();}
["n","rho","alpha"].forEach(k=>$(k).addEventListener("input",update));
$("pos").addEventListener("click",()=>set({n:"100",rho:"0.5",alpha:"0.05"}));
$("neg").addEventListener("click",()=>set({n:"100",rho:"-0.5",alpha:"0.05"}));
$("ind").addEventListener("click",()=>set({n:"100",rho:"0",alpha:"0.05"}));
update();
})();
