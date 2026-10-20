/* Exact variance vs first-order delta approximation for a normal sample mean. */
(function(){
  "use strict";
  if(!document.getElementById("esa-delta-lab"))return;
  const $=id=>document.getElementById(id);
  const ids=["variance-input","derivative","approx","exact","difference","relative"];
  const reset=()=>ids.forEach(id=>{$("esa-delta-"+id).textContent="—";});
  const fmt=x=>Number(x.toPrecision(7)).toString();
  function run(){
    const rawTheta=$("esa-delta-theta").value.trim();
    const rawSigma=$("esa-delta-sigma").value.trim();
    const rawN=$("esa-delta-n").value.trim();
    const theta=Number(rawTheta),sigma=Number(rawSigma),n=Number(rawN);
    const transform=$("esa-delta-transform").value;
    if(!rawTheta||!rawSigma||!rawN||!Number.isFinite(theta)||
       theta< -2||theta>2||!Number.isFinite(sigma)||sigma<.1||sigma>2||
       !Number.isSafeInteger(n)||n<2||n>500||
       !["identity","square","exponential"].includes(transform)){
      reset();
      $("esa-delta-status").textContent=
        "Enter a mean from −2 to 2, a positive standard deviation from 0.1 to 2, and an integer sample size from 2 to 500.";
      return;
    }
    // Xbar ~ Normal(theta, sigma^2 / n) exactly for IID normal observations.
    const v=sigma*sigma/n;
    let derivative,deltaVariance,exactVariance;
    if(transform==="identity"){
      derivative=1;
      deltaVariance=v;
      exactVariance=v;
    }else if(transform==="square"){
      derivative=2*theta;
      deltaVariance=derivative*derivative*v;
      // Normal noncentral fourth moment: Var(Xbar^2)=4 theta^2 v + 2 v^2.
      exactVariance=deltaVariance+2*v*v;
    }else{
      derivative=Math.exp(theta);
      deltaVariance=derivative*derivative*v;
      // Normal MGF / lognormal variance; expm1 preserves accuracy for small v.
      exactVariance=Math.exp(2*theta+v)*Math.expm1(v);
    }
    const fields={
      "variance-input":v,
      derivative,
      approx:deltaVariance,
      exact:exactVariance,
      difference:exactVariance-deltaVariance,
      relative:exactVariance>0?100*deltaVariance/exactVariance:0
    };
    for(const [id,value] of Object.entries(fields))
      $("esa-delta-"+id).textContent=fmt(value)+(id==="relative"?"%":"");
    $("esa-delta-status").textContent=transform==="square"&&theta===0?
      "The first derivative is zero at theta=0, so the first-order delta approximation is zero even though the exact variance is positive. A higher-order expansion is needed.":
      "The exact variance refers to a normal sample mean; the first-order approximation may differ at finite sample sizes.";
  }
  $("esa-delta-run").addEventListener("click",run);
  $("esa-delta-reset").addEventListener("click",()=>{
    $("esa-delta-theta").value="0";
    $("esa-delta-sigma").value="1";
    $("esa-delta-n").value="20";
    $("esa-delta-transform").value="square";
    run();
  });
  ["esa-delta-theta","esa-delta-sigma","esa-delta-n","esa-delta-transform"]
    .forEach(id=>$(id).addEventListener("change",run));
  run();
})();