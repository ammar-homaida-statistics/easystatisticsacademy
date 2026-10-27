/* Batch #75 — precision/sample-size planning, known population sigma only. */
(function(){
"use strict";
const root=document.getElementById("esa-precision-lab");if(!root)return;
const $=id=>root.querySelector("#esa-pr-"+id),NS="http://www.w3.org/2000/svg";
const critical={90:1.6448536269514722,95:1.959963984540054,99:2.5758293035489004};
function compute(n,sigma,confidence,target){
 if(!Number.isSafeInteger(n)||n<1||n>1e9||
    !Number.isFinite(sigma)||sigma<=0||sigma>1e9||
    !Object.prototype.hasOwnProperty.call(critical,confidence)||
    !Number.isFinite(target)||target<=0||target>1e9)return null;
 const z=critical[confidence],margin=z*sigma/Math.sqrt(n);
 const square=(z*sigma/target)**2;
 if(!Number.isFinite(square)||square>Number.MAX_SAFE_INTEGER)return null;
 // Floating-point noise near integer planning thresholds needs tolerant rounding.
 const nearest=Math.round(square);
 const adjusted=Math.abs(square-nearest)<=8*Number.EPSILON*Math.max(1,square)?
  nearest:Math.ceil(square);
 let required=Math.max(1,adjusted);
 // Verify the literal bound at the selected n with the very same floating inputs.
 while(required<=Number.MAX_SAFE_INTEGER &&
       z*sigma/Math.sqrt(required)>target*(1+8*Number.EPSILON))required++;
 if(required>Number.MAX_SAFE_INTEGER)return null;
 const width=2*margin,margin4=z*sigma/Math.sqrt(4*n);
 return {n,sigma,confidence,target,z,margin,width,required,margin4,
   width4:2*margin4};
}
window.esaPrecisionMath={compute,critical};
function mk(tag,attrs={},label){
 const e=document.createElementNS(NS,tag);
 for(const [k,v] of Object.entries(attrs))e.setAttribute(k,String(v));
 if(label!==undefined)e.textContent=String(label);
 return e;
}
function chart(o){
 const svg=$("chart"),max=475;
 const values=[o.width,o.width4],captions=["n="+o.n,"n="+(4*o.n)];
 const kids=[mk("title",{},"Compare interval widths at n and four times n"),
   mk("desc",{},"With fixed known sigma and confidence level, quadrupling sample size halves interval width.")];
 values.forEach((v,i)=>{
  const y=38+i*82;
  kids.push(mk("text",{x:15,y:y-9,fill:"currentColor","font-size":14},captions[i]),
    mk("rect",{x:15,y,width:max*(v/values[0]),height:26,rx:4,
      fill:i===0?"#2563eb":"#0f766e"}),
    mk("text",{x:15,y:y+49,fill:"currentColor","font-size":13},
      "Width = "+v.toFixed(6)));
 });
 svg.replaceChildren(...kids);
 svg.setAttribute("aria-label",captions.map((x,i)=>x+": width "+values[i].toFixed(6)).join("; "));
}
function render(){
 const raw=[$("n").value.trim(),$("sigma").value.trim(),$("level").value,$("target").value.trim()];
 const n=/^\d+$/.test(raw[0])?Number(raw[0]):NaN;
 const sigma=raw[1]===""?NaN:Number(raw[1]);
 const target=raw[3]===""?NaN:Number(raw[3]);
 const o=compute(n,sigma,Number(raw[2]),target);
 if(!o){$("results").hidden=true;$("error").hidden=false;
  $("error").textContent="Use an integer sample size 1–1,000,000,000; known σ>0; confidence 90%, 95%, or 99%; and target margin of error >0. Planning results must fit a safe integer.";
  return;
 }
 $("error").hidden=true;$("error").textContent="";$("results").hidden=false;
 for(const [key,value] of Object.entries({
  critical:o.z,stderr:o.sigma/Math.sqrt(o.n),margin:o.margin,
  width:o.width,margin4:o.margin4,width4:o.width4})){
  $(key).textContent=value.toFixed(6);
 }
 $("needed").textContent=o.required.toLocaleString("en-US");
 $("explain").textContent=
  "At fixed confidence and known σ, multiplying n by four halves the interval width. The planning n assumes independent observations and a normal sampling distribution (exact for normally distributed observations or approximate under suitable CLT conditions).";
 chart(o);
}
for(const id of ["n","sigma","level","target"]){
 $(id).addEventListener("input",render);$(id).addEventListener("change",render);
}
$("reset").addEventListener("click",()=>{
  for(const [id,value] of Object.entries({n:"100",sigma:"20",level:"95",target:"3"}))$(id).value=value;
  render();
});
render();
})();