/* Batch #75: shared, audited conditional probability tree (English + Arabic). */
(function() {
"use strict";
function calculate(study,passGivenStudy,passGivenNoStudy) {
 const values=[study,passGivenStudy,passGivenNoStudy];
 if(values.some(x=>!Number.isFinite(x)||x<0||x>1))return null;
 // The slider intentionally restricts P(Study) to (0,1), ensuring
 // both original conditional factors are defined by elementary conditional P.
 if(study===0||study===1)return null;
 const noStudy=1-study,studyPass=study*passGivenStudy,
   studyFail=study*(1-passGivenStudy),
   noStudyPass=noStudy*passGivenNoStudy,
   noStudyFail=noStudy*(1-passGivenNoStudy);
 const pass=studyPass+noStudyPass;
 return {study,noStudy,passGivenStudy,passGivenNoStudy,studyPass,studyFail,
  noStudyPass,noStudyFail,pass,
  studyGivenPass:pass===0?null:studyPass/pass};
}
window.esaConditionalTreeMath={calculate};
const root=document.getElementById("esa-conditional-tree-explorer");
if(!root)return;
const ar=document.documentElement.lang==="ar",field=id=>root.querySelector("#"+id);
const study=field("esa-tree-study"),ps=field("esa-tree-pass-study"),pn=field("esa-tree-pass-no-study");
const display=(id,value)=>{field(id).textContent=value.toFixed(4)};
const NS="http://www.w3.org/2000/svg";
function make(tag,attrs={},value){
 const e=document.createElementNS(NS,tag);
 for(const [key,val] of Object.entries(attrs))e.setAttribute(key,String(val));
 if(value!==undefined)e.textContent=String(value);
 return e;
}
function chart(result){
 const plot=field("esa-tree-chart");
 if(!plot)return;
 const joint=[result.studyPass,result.studyFail,result.noStudyPass,result.noStudyFail],
   colors=["#2563eb","#93c5fd","#0f766e","#5eead4"];
 const labels=ar?["درس ونجح","درس ولم ينجح","لم يدرس ونجح","لم يدرس ولم ينجح"]:
 ["Study + pass","Study + fail","No study + pass","No study + fail"];
 const kids=[make("title",{},ar?"توزيع المسارات الأربعة النهائية":"Four terminal path probabilities"),
   make("desc",{},ar?"طول كل عمود يتناسب مع احتمال المسار المشترك":"Each bar has height proportional to a joint path probability"),
   make("line",{x1:25,x2:595,y1:215,y2:215,stroke:"currentColor"})];
 joint.forEach((v,i)=>{
   const w=110,x=30+i*145,h=150*v,y=215-h;
   kids.push(make("rect",{x,y,width:w,height:h,fill:colors[i],rx:3}),
     make("text",{x:x+w/2,y:Math.max(15,y-5),"text-anchor":"middle",
       fill:"currentColor","font-size":14},v.toFixed(4)),
     make("text",{x:x+w/2,y:238,"text-anchor":"middle",
       fill:"currentColor","font-size":12},labels[i]));
 });
 plot.replaceChildren(...kids);
 plot.setAttribute("aria-label",labels.map((l,i)=>l+": "+joint[i].toFixed(4)).join("; "));
}
function update(){
 const result=calculate(Number(study.value),Number(ps.value),Number(pn.value));
 if(!result)return;
 const map={
  "esa-tree-p-study":result.study,
  "esa-tree-p-no-study":result.noStudy,
  "esa-tree-p-pass-study":result.passGivenStudy,
  "esa-tree-p-fail-study":1-result.passGivenStudy,
  "esa-tree-p-pass-no-study":result.passGivenNoStudy,
  "esa-tree-p-fail-no-study":1-result.passGivenNoStudy,
  "esa-tree-joint-study-pass":result.studyPass,
  "esa-tree-joint-study-fail":result.studyFail,
  "esa-tree-joint-no-study-pass":result.noStudyPass,
  "esa-tree-joint-no-study-fail":result.noStudyFail,
  "esa-tree-multiply":result.studyPass,
  "esa-tree-total-pass":result.pass};
 for(const [id,value] of Object.entries(map))display(id,value);
 field("esa-tree-study-value").textContent=result.study.toFixed(2);
 field("esa-tree-pass-study-value").textContent=result.passGivenStudy.toFixed(2);
 field("esa-tree-pass-no-study-value").textContent=result.passGivenNoStudy.toFixed(2);
 field("esa-tree-bayes").textContent=result.studyGivenPass===null?
   (ar?"غير معرّف":"Undefined"):result.studyGivenPass.toFixed(4);
 field("esa-tree-undefined-note").hidden=result.studyGivenPass!==null;
 chart(result);
}
[study,ps,pn].forEach(control=>control.addEventListener("input",update));
field("esa-tree-reset").addEventListener("click",()=>{
 study.value="0.6";ps.value="0.9";pn.value="0.4";update();
});
update();
})();