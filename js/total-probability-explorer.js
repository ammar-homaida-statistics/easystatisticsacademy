/* Batch #74: bilingual Law of Total Probability, three exhaustive exclusive groups. */
(function(){
"use strict";
const root=document.getElementById("esa-total-probability-lab");if(!root)return;
const ar=document.documentElement.lang==="ar", $=id=>root.querySelector("#esa-tp-"+id);
const svgNS="http://www.w3.org/2000/svg";
function svg(tag,attrs={},txt){const e=document.createElementNS(svgNS,tag);
 for(const [k,v] of Object.entries(attrs))e.setAttribute(k,String(v));
 if(txt!==undefined)e.textContent=String(txt);return e;
}
function compute(weights,conditional){
 if(!Array.isArray(weights)||!Array.isArray(conditional)||weights.length!==3||conditional.length!==3)return null;
 if([...weights,...conditional].some(v=>!Number.isFinite(v)||v<0||v>1))return null;
 const sum=weights.reduce((a,b)=>a+b,0);
 if(Math.abs(sum-1)>1e-9)return null; // no silent normalization or misleading result
 const contributions=weights.map((w,i)=>w*conditional[i]);
 const total=contributions.reduce((a,b)=>a+b,0);
 return {weights,conditional,contributions,total,sum};
}
window.esaTotalProbabilityMath={compute};
const labels=ar?["المجموعة الأولى","المجموعة الثانية","المجموعة الثالثة"]:
 ["Group 1","Group 2","Group 3"];
function draw(r){
 const chart=$("chart");
 const colors=["#2563eb","#0f766e","#b45309"],shapes=[
  svg("title",{},ar?"مساهمات المجموعات الثلاث في الاحتمال الكلي":"Three group contributions to total probability"),
  svg("desc",{},ar?"كل عمود يمثل وزن المجموعة مضروبًا في احتمال الحدث داخلها":"Each bar is the group weight times the conditional event probability."),
  svg("line",{x1:38,x2:566,y1:222,y2:222,stroke:"currentColor"})];
 for(let i=0;i<3;i++){
  const c=r.contributions[i],height=175*c,x=63+i*175;
  shapes.push(svg("rect",{x,y:222-height,width:105,height,rx:3,fill:colors[i]}),
    svg("text",{x:x+52.5,y:Math.max(20,212-height),"text-anchor":"middle",
      fill:"currentColor","font-size":"15"},c.toFixed(4)),
    svg("text",{x:x+52.5,y:246,"text-anchor":"middle",
      fill:"currentColor","font-size":"14"},String(i+1)));
 }
 chart.replaceChildren(...shapes);
 chart.setAttribute("aria-label",(ar?"مساهمات المجموعات: ":"Group contributions: ")+
  r.contributions.map(c=>c.toFixed(6)).join(", ")+
  (ar?"، الاحتمال الكلي ":"; total probability ")+r.total.toFixed(6));
}
function render(){
 const ids=["w1","w2","w3","p1","p2","p3"];
 const raw=ids.map(id=>$(id).value.trim());
 const nums=raw.map(s=>s===""?NaN:Number(s));
 const result=compute(nums.slice(0,3),nums.slice(3));
 if(!result){
   $("error").hidden=false;
   $("error").textContent=ar?
     "أدخل ست قيم بين 0 و1، ويجب أن يكون مجموع أوزان المجموعات الثلاث مساويًا 1 تمامًا (بهامش تقريبي صغير).":
     "Enter six probabilities from 0 to 1; the three disjoint exhaustive group weights must sum to 1 (within a small rounding tolerance).";
   $("results").hidden=true;return;
 }
 $("error").hidden=true;$("error").textContent="";
 $("results").hidden=false;
 for(let i=0;i<3;i++)$("c"+(i+1)).textContent=result.contributions[i].toFixed(6);
 $("total").textContent=result.total.toFixed(6);
 $("sum").textContent=result.sum.toFixed(6);
 $("explain").textContent=ar?
  "الاحتمال الكلي يساوي مجموع المساهمات الثلاث دون تكرار الأحداث:":
  "The overall event probability is the sum of the three mutually exclusive contributions:";
 draw(result);
}
for(const id of ["w1","w2","w3","p1","p2","p3"])$(id).addEventListener("input",render);
$("reset").addEventListener("click",()=>{
  for(const [id,value] of Object.entries({w1:"0.2",w2:"0.3",w3:"0.5",p1:"0.1",p2:"0.5",p3:"0.8"}))$(id).value=value;
  render();
});
render();
})();