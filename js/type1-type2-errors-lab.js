/* Decision-error laboratory: exact normal sampling-statistic model, seeded simulations. */
(function(){
  "use strict";
  if(!document.getElementById("esa-errors-lab"))return;
  const $=id=>document.getElementById(id);
  const ar=document.documentElement.lang==="ar";
  const messages=ar?{
    invalid:"اختر إعدادات النموذج المسموح بها، وأدخل بذرة عشوائية صحيحة بين 1 و2147483647.",
    ready:"النتائج قابلة لإعادة الإنتاج باستخدام البذرة المحددة. يمثّل كل صف تجارب مستقلة في حالة صحة فرضية العدم أو صحة البديل المحدد، وليسا مجتمعاً واحداً."
  }:{
    invalid:"Select permitted model parameters and a whole-number seed from 1 to 2147483647.",
    ready:"Results reproduced from the selected seed. Rows represent separate repeated-study scenarios: H₀ true and specified H₁ true; they are not one joint population."
  };
  const R=1000;
  const thresholds={"0.01":2.5758293035489,"0.05":1.959963984540054,"0.10":1.64485362695147};
  function rng(seed){
    let state=seed>>>0;
    return function(){
      state^=state<<13;state^=state>>>17;state^=state<<5;
      return ((state>>>0)+0.5)/4294967296;
    };
  }
  function normal(random){
    return Math.sqrt(-2*Math.log(random()))*Math.cos(2*Math.PI*random());
  }
  /* Abramowitz–Stegun 7.1.26: maximum erf approximation error ~1.5e-7. */
  function erf(x){
    const sign=x<0?-1:1, a=Math.abs(x), t=1/(1+0.3275911*a);
    const poly=(((((1.061405429*t-1.453152027)*t)+1.421413741)*t-0.284496736)*t+0.254829592)*t;
    return sign*(1-poly*Math.exp(-a*a));
  }
  function cdf(x){return 0.5*(1+erf(x/Math.SQRT2));}
  function fmt(x){return (100*x).toFixed(2)+"%";}
  function run(){
    const n=Number($("esa-errors-n").value),
      delta=Number($("esa-errors-effect").value),
      alpha=$("esa-errors-alpha").value,
      raw=$("esa-errors-seed").value.trim(),
      seed=Number(raw);
    if(![10,30,100].includes(n)||![0.2,0.5,1].includes(delta)||
       !Object.prototype.hasOwnProperty.call(thresholds,alpha)||
       !/^\d+$/.test(raw)||!Number.isSafeInteger(seed)||seed<1||seed>2147483647){
      $("esa-errors-status").textContent=messages.invalid;
      return;
    }
    const c=thresholds[alpha], shift=delta*Math.sqrt(n), random=rng(seed);
    let falsePositive=0,trueNegative=0,truePositive=0,falseNegative=0;
    for(let i=0;i<R;i++){
      /* For independent N(mu,1) data, sqrt(n)*(Xbar-0) is exactly N(sqrt(n)*mu,1). */
      const zNull=normal(random), zAlternative=shift+normal(random);
      if(Math.abs(zNull)>c)falsePositive++;else trueNegative++;
      if(Math.abs(zAlternative)>c)truePositive++;else falseNegative++;
    }
    const a=Number(alpha);
    const power=cdf(-c-shift)+(1-cdf(c-shift));
    [["esa-errors-fp",falsePositive],["esa-errors-tn",trueNegative],
     ["esa-errors-tp",truePositive],["esa-errors-fn",falseNegative]]
      .forEach(([id,count])=>{$(id).textContent=String(count);});
    [["esa-errors-alpha-theory",a],["esa-errors-power-theory",power],
     ["esa-errors-beta-theory",1-power],
     ["esa-errors-alpha-empirical",falsePositive/R],
     ["esa-errors-power-empirical",truePositive/R],
     ["esa-errors-beta-empirical",falseNegative/R]]
      .forEach(([id,value])=>{$(id).textContent=fmt(value);});
    $("esa-errors-n-rep").textContent=String(R);
    $("esa-errors-status").textContent=messages.ready;
  }
  $("esa-errors-run").addEventListener("click",run);
  $("esa-errors-reset").addEventListener("click",()=>{
    $("esa-errors-n").value="30";
    $("esa-errors-effect").value="0.5";
    $("esa-errors-alpha").value="0.05";
    $("esa-errors-seed").value="2026";
    run();
  });
  run();
})();