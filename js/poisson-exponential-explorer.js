/* Shared Poisson–Exponential calculator, with identical numerical logic in both languages. */
(function () {
  "use strict";
  const form = document.getElementById("esa-event-explorer-form");
  if (!form) return;
  const ar = document.documentElement.lang === "ar";
  const rate = document.getElementById("esa-event-rate");
  const time = document.getElementById("esa-event-time");
  const error = document.getElementById("esa-event-error");
  const outputs = ["esa-event-none","esa-event-survival","esa-event-at-least-one",
                   "esa-event-expected","esa-event-meanwait"]
                   .map(id => document.getElementById(id));
  const explanation = document.getElementById("esa-event-explanation");

  function probabilities(r,t) {
    if (!Number.isFinite(r) || r <= 0 || r > 20 ||
        !Number.isFinite(t) || t < 0 || t > 60) return null;
    const expected=r*t;
    const none=Math.exp(-expected);
    return [none,none,-Math.expm1(-expected),expected,1/r];
  }
  window.esaPoissonExponential = probabilities;
  function render() {
    const r=Number(rate.value),t=Number(time.value);
    const invalidRate=rate.value.trim()==="" || !Number.isFinite(r) || r<=0 || r>20;
    const invalidTime=time.value.trim()==="" || !Number.isFinite(t) || t<0 || t>60;
    if (invalidRate || invalidTime) {
      error.textContent=invalidRate
        ? (ar?"أدخل معدلًا أكبر من الصفر ولا يتجاوز 20 حدثًا في الدقيقة.":"Rate must be greater than 0 and at most 20 events per minute.")
        : (ar?"أدخل مدة تتراوح من 0 إلى 60 دقيقة.":"Time must be between 0 and 60 minutes.");
      error.hidden=false;
      outputs.forEach(out=>{out.textContent="—";});
      explanation.textContent=ar?"أدخل قيمًا صالحة للمقارنة بين التوزيعين.":"Enter valid inputs to compare the distributions.";
      return;
    }
    error.hidden=true;
    probabilities(r,t).forEach((value,i)=>{outputs[i].textContent=value.toFixed(6);});
    explanation.textContent=ar
      ? "بمعدل "+r+" حدث/دقيقة وخلال "+t+" دقيقة، يتساوى احتمال عدم وقوع أي حدث مع احتمال انتظار أكثر من t دقيقة للحدث التالي: exp(−rt)."
      : "With rate "+r+" events/minute over "+t+" minutes, P(N(t) = 0) = P(T > t) = exp(−rt).";
  }
  form.addEventListener("submit",event=>event.preventDefault());
  rate.addEventListener("input",render);
  time.addEventListener("input",render);
  document.getElementById("esa-event-reset").addEventListener("click",()=>{
    rate.value="2";time.value="1";render();
  });
  render();
})();