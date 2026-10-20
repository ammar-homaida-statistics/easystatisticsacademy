/* Bayes' theorem evidence explorer: independent 2x2 probability calculations. */
(function(){
  "use strict";
  if(!document.getElementById("esa-bayes-lab"))return;
  const $=id=>document.getElementById(id);
  const ar=document.documentElement.lang==="ar";
  const messages=ar?{
    undefined:"غير معرّف (احتمال الدليل يساوي صفراً)",
    invalid:"أدخل الانتشار والحساسية والنوعية كنسب مئوية بين 0 و100.",
    ready:"حُسبت الاحتمالات باستخدام قانون الاحتمال الكلي. خلايا الجدول تكرارات متوقعة من كل 10,000 فرد افتراضي، وليست بيانات مرضى حقيقيين."
  }:{
    undefined:"Undefined (evidence has probability zero)",
    invalid:"Enter prevalence, sensitivity, and specificity as percentages from 0 to 100.",
    ready:"Calculated from the law of total probability. Table cells are expected counts per 10,000, not observed patient data."
  };
  const outputs=["esa-bayes-pos","esa-bayes-neg","esa-bayes-tp","esa-bayes-fp","esa-bayes-fn","esa-bayes-tn","esa-bayes-plus-prob","esa-bayes-minus-prob"];
  function clear(){outputs.forEach(id=>{$(id).textContent="—";});}
  function percentage(id){
    const s=$(id).value.trim();
    if(!/^(?:\d+(?:\.\d*)?|\.\d+)$/.test(s))return null;
    const x=Number(s);
    return Number.isFinite(x)&&x>=0&&x<=100?x/100:null;
  }
  function pct(x){return x===null?messages.undefined:(100*x).toFixed(2)+"%";}
  function count(x){return (10000*x).toFixed(2);}
  function run(){
    const p=percentage("esa-bayes-prev"),
      se=percentage("esa-bayes-sens"),
      sp=percentage("esa-bayes-spec");
    if([p,se,sp].some(x=>x===null)){
      clear();$("esa-bayes-status").textContent=messages.invalid;return;
    }
    const tp=p*se,fn=p*(1-se),fp=(1-p)*(1-sp),tn=(1-p)*sp;
    const positive=tp+fp,negative=fn+tn;
    $("esa-bayes-pos").textContent=pct(positive?tp/positive:null);
    $("esa-bayes-neg").textContent=pct(negative?fn/negative:null);
    $("esa-bayes-plus-prob").textContent=pct(positive);
    $("esa-bayes-minus-prob").textContent=pct(negative);
    [["esa-bayes-tp",tp],["esa-bayes-fp",fp],["esa-bayes-fn",fn],["esa-bayes-tn",tn]]
      .forEach(([id,value])=>{$(id).textContent=count(value);});
    $("esa-bayes-status").textContent=messages.ready;
  }
  $("esa-bayes-run").addEventListener("click",run);
  $("esa-bayes-reset").addEventListener("click",()=>{
    $("esa-bayes-prev").value="1";
    $("esa-bayes-sens").value="90";
    $("esa-bayes-spec").value="95";
    run();
  });
  run();
})();