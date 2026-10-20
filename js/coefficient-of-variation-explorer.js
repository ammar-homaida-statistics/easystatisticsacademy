/* Coefficient of variation: sample/population descriptive statistics and responsible scale warnings. */
(function(){
  "use strict";
  if(!document.getElementById("esa-cv-lab"))return;
  const $=id=>document.getElementById(id);
  const ar=document.documentElement.lang==="ar";
  const t=ar?{
    limit:"أدخل ما لا يزيد على 200 مشاهدة لكل مجموعة.",
    count:"أدخل بين مشاهدتين و200 مشاهدة لكل مجموعة.",
    input:"يجب أن تكون المشاهدات أعداداً منتهية تفصل بينها فواصل أو فاصلة منقوطة أو مسافات.",
    magnitude:"يجب أن تكون كل مشاهدة عدداً منتهياً لا تتجاوز قيمته المطلقة 10^100.",
    overflow:"حدث تجاوز عددي؛ استخدم مقادير قياس أصغر.",
    undefined:"غير معرّف",
    a:"المجموعة أ",
    b:"المجموعة ب",
    interval:"لا يناسب معامل الاختلاف مقياس الفترة الذي لا يملك صفراً مطلقاً ذا معنى (مثل درجات المئوية). تُعرض العمليات الحسابية فقط دون ترتيب للمجموعتين.",
    mean:"يشترط تفسير معامل الاختلاف هنا متوسطاً موجباً غير صفري؛ ولا تُفسَّر النسبة عند متوسط صفري أو سالب.",
    near:"المتوسط صغير مقارنة بالانحراف المعياري (المتوسط ≤ 0.1 × الانحراف المعياري). يصبح معامل الاختلاف غير مستقر؛ تجنب ترتيب المجموعتين.",
    equal:"معامل الاختلاف متساوٍ في المجموعتين ضمن الافتراضات المحددة.",
    greater:"أعلى في التشتت النسبي (معامل الاختلاف).",
    ok:"حُسبت القيم محلياً. يناسب معامل الاختلاف البيانات النسبية ذات الصفر ذي المعنى والمتوسط الموجب والمقارنة الموضوعية الملائمة.",
    no:"لا يُنصح بالمقارنة في هذه الحالة."
  }:{
    limit:"Please enter at most 200 numbers per dataset.",
    count:"Enter between 2 and 200 observations for each dataset.",
    input:"Observations must be finite numbers separated by commas, semicolons, or spaces.",
    magnitude:"Each observation must be finite and have magnitude no greater than 10^100.",
    overflow:"Numerical overflow: use measurements of more moderate size.",
    undefined:"Undefined",
    a:"Dataset A",
    b:"Dataset B",
    interval:"CV is inappropriate for interval scales without a meaningful absolute zero (for example Celsius). Results are shown only as arithmetic; no relative-spread ranking is given.",
    mean:"CV requires a positive nonzero mean; for zero or negative means it is not interpreted.",
    near:"A mean is small relative to its SD (mean ≤ 0.1 × SD). CV is unstable: avoid ranking datasets.",
    equal:t.equal,
    greater:" has greater relative variability (CV).",
    ok:t.ok,
    no:t.no
  };
  function parse(text){
    if(text.length>1600)return {error:t.limit};
    const tokens=text.trim().split(/[\s,;]+/).filter(Boolean);
    if(tokens.length<2||tokens.length>200)return {error:t.count};
    const numbers=[];
    for(const v of tokens){
      if(!/^[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?$/.test(v))
        return {error:t.input};
      const num=Number(v);
      if(!Number.isFinite(num)||Math.abs(num)>1e100)
        return {error:t.magnitude};
      numbers.push(num);
    }
    return {numbers};
  }
  function describe(values,sample){
    const n=values.length;
    // Online central moments reduce cancellation for large values with small spread.
    let mean=0,m2=0,k=0;
    for(const x of values){
      k++;
      const delta=x-mean;
      mean+=delta/k;
      m2+=delta*(x-mean);
    }
    const sd=Math.sqrt(Math.max(0,m2/(sample?n-1:n)));
    if(!Number.isFinite(mean)||!Number.isFinite(sd))
      return {error:t.overflow};
    const cv=mean>0?100*sd/mean:null;
    const near=mean>0&&sd>0&&mean<=0.1*sd;
    return {n,mean,sd,cv:Number.isFinite(cv)?cv:null,near};
  }
  function number(x){return Number(x).toFixed(4).replace(/\.?0+$/,"");}
  function resetResults(){
    for(const id of ["esa-cv-a-n","esa-cv-a-mean","esa-cv-a-sd","esa-cv-a-cv",
                      "esa-cv-b-n","esa-cv-b-mean","esa-cv-b-sd","esa-cv-b-cv"])
      $(id).textContent="—";
    $("esa-cv-comparison").textContent="—";
  }
  function run(){
    resetResults();
    const a=parse($("esa-cv-a").value),b=parse($("esa-cv-b").value);
    if(a.error||b.error){
      $("esa-cv-status").textContent=(a.error?t.a+": "+a.error+" ":"")+(b.error?t.b+": "+b.error:"");
      return;
    }
    const sample=$("esa-cv-mode").value==="sample";
    const A=describe(a.numbers,sample),B=describe(b.numbers,sample);
    if(A.error||B.error){
      $("esa-cv-status").textContent=A.error||B.error;return;
    }
    for(const [id,obj] of [["a",A],["b",B]]){
      $("esa-cv-"+id+"-n").textContent=String(obj.n);
      $("esa-cv-"+id+"-mean").textContent=number(obj.mean);
      $("esa-cv-"+id+"-sd").textContent=number(obj.sd);
      $("esa-cv-"+id+"-cv").textContent=obj.cv===null?t.undefined:obj.cv.toFixed(2)+"%";
    }
    const ratio=$("esa-cv-scale").value==="ratio";
    const warnings=[];
    if(!ratio)warnings.push(t.interval);
    if(A.cv===null||B.cv===null)warnings.push(t.mean);
    if(A.near||B.near)warnings.push(t.near);
    if(!warnings.length){
      const diff=A.cv-B.cv;
      $("esa-cv-comparison").textContent=Math.abs(diff)<1e-10?
        "Equal coefficients of variation under these assumptions.":
        (diff>0?t.a:t.b)+(ar?" ":"")+t.greater;
      $("esa-cv-status").textContent="Calculated locally. CV is meaningful only for positive-mean ratio-scale data with comparable substantive interpretation.";
    }else{
      $("esa-cv-comparison").textContent="Comparison not recommended for these data.";
      $("esa-cv-status").textContent=warnings.join(" ");
    }
  }
  $("esa-cv-run").addEventListener("click",run);
  $("esa-cv-reset").addEventListener("click",()=>{
    $("esa-cv-a").value="8, 10, 12";
    $("esa-cv-b").value="45, 50, 55";
    $("esa-cv-mode").value="sample";
    $("esa-cv-scale").value="ratio";
    run();
  });
  for(const id of ["esa-cv-mode","esa-cv-scale"])$(id).addEventListener("change",run);
  run();
})();