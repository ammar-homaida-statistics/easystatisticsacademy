/* Batch #73 — one bilingual, shared 2x2 conditional probability engine. */
(function() {
  "use strict";
  const root=document.getElementById("esa-conditional-lab"); if(!root) return;
  const ar=document.documentElement.lang==="ar";
  const $=name=>root.querySelector("#esa-cp-"+name);
  const ids=["ab","aonly","bonly","neither"];
  const format=n=>n===null?"—":n.toFixed(6);
  function compute(ab,aonly,bonly,neither) {
    const v=[ab,aonly,bonly,neither];
    if(v.some(x=>!Number.isSafeInteger(x)||x<0||x>1000000)) return null;
    const n=v.reduce((a,b)=>a+b,0);
    if(!Number.isSafeInteger(n)||n<1) return null;
    const A=ab+aonly,B=ab+bonly;
    const pa=A/n,pb=B/n,pab=ab/n;
    return {n,A,B,ab,aonly,bonly,neither,
      pa,pb,pab,agivenb:B===0?null:ab/B,bgivena:A===0?null:ab/A,
      independent:Math.abs(pab-pa*pb)<1e-12};
  }
  // Expose only the pure calculation for independent automated numerical checks.
  window.esaConditionalMath={compute};
  function render(){
    const parsed=ids.map(id=>{
      const v=$(id).value.trim();
      return /^\d+$/.test(v)?Number(v):NaN;
    });
    const o=compute(...parsed);
    const warning=$("warning"),results=$("results");
    if(!o){
      results.hidden=true;warning.hidden=false;
      warning.textContent=ar?
        "أدخل أربع قيم صحيحة غير سالبة، مجموعها موجب، ولا تتجاوز كل قيمة مليونًا.":
        "Enter four nonnegative whole-number cell counts, each at most one million, with a positive total.";
      return;
    }
    results.hidden=false;
    for(const key of ["pa","pb","pab","agivenb","bgivena"]){
      $(key).textContent=format(o[key]);
    }
    $("total").textContent=String(o.n);
    $("nA").textContent=String(o.A);
    $("nB").textContent=String(o.B);
    const alerts=[];
    if(o.B===0)alerts.push(ar?
      "الحدث B مستحيل في الجدول: P(B)=0 ولذلك P(A|B) غير معرّف.":"B has zero frequency: P(B)=0 and P(A|B) is undefined.");
    if(o.A===0)alerts.push(ar?
      "الحدث A مستحيل في الجدول: P(A)=0 ولذلك P(B|A) غير معرّف.":"A has zero frequency: P(A)=0 and P(B|A) is undefined.");
    warning.hidden=alerts.length===0;
    warning.textContent=alerts.join(" ");
    $("interpretation").textContent=ar?
      (o.independent?"وفق جدول التكرارات هذا، يتحقق شرط الاستقلال P(A∩B)=P(A)P(B).":"وفق جدول التكرارات هذا، لا يتحقق شرط الاستقلال P(A∩B)=P(A)P(B)."):
      (o.independent?"For these cell frequencies, P(A∩B)=P(A)P(B): the events are independent.":"For these cell frequencies, P(A∩B) differs from P(A)P(B): the events are dependent.");
    for(const [cell,count] of [["ab",o.ab],["aonly",o.aonly],["bonly",o.bonly],["neither",o.neither]]){
      $("cell-"+cell).textContent=String(count);
    }
  }
  ids.forEach(id=>$(id).addEventListener("input",render));
  $("reset").addEventListener("click",()=>{
    const defaults={ab:"20",aonly:"10",bonly:"30",neither:"40"};
    for(const [id,value] of Object.entries(defaults))$(id).value=value;
    render();
  });
  render();
})();