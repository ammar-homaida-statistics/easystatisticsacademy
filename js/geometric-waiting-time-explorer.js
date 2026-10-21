/* Shared bilingual geometric calculations; the support is trials until the first success. */
    (function () {
      "use strict";
      const root=document.getElementById("esa-geometric-wait-explorer");
      if (!root) return;
      const el=id=>root.querySelector("#"+id);
      const probability=el("esa-geom-p"),trial=el("esa-geom-k");
      const ar=document.documentElement.lang==="ar";
      function probabilities(p,k) {
        if(!Number.isFinite(p)||p<=0||p>1||!Number.isSafeInteger(k)||k<1)return null;
        const q=1-p,tail=Math.pow(q,k);
        return {pmf:Math.pow(q,k-1)*p,cdf:1-tail,tail,mean:1/p,variance:q/(p*p)};
      }
      window.esaGeometricMath=probabilities;
      function update() {
        const p=Number(probability.value),k=Number(trial.value);
        const q=1-p,results=probabilities(p,k);
        if(!results)return;
        const {pmf,cdf,tail}=results;
        el("esa-geom-p-value").textContent=p.toFixed(2);
        el("esa-geom-k-value").textContent=String(k);
        el("esa-geom-pmf").textContent=pmf.toFixed(6);
        el("esa-geom-cdf").textContent=cdf.toFixed(6);
        el("esa-geom-tail").textContent=tail.toFixed(6);
        el("esa-geom-mean").textContent=results.mean.toFixed(4);
        el("esa-geom-variance").textContent=results.variance.toFixed(4);
        const historyPossible=p<1;
        el("esa-geom-memoryless-next").textContent=historyPossible?p.toFixed(4):(ar?"غير معرّف":"Undefined");
        el("esa-geom-memoryless-tail").textContent=historyPossible?
          Math.pow(q,3).toFixed(6):(ar?"غير معرّف":"Undefined");
        el("esa-geom-memoryless-note").hidden=historyPossible;
        for(const bar of root.querySelectorAll("#esa-geom-bars rect[data-trial]")) {
          const j=Number(bar.getAttribute("data-trial"));
          const pj=Math.pow(q,j-1)*p;
          const height=110*pj;
          bar.setAttribute("y",String(136-height));
          bar.setAttribute("height",String(height));
          bar.setAttribute("fill",j===k?"#0d9488":"#64748b");
        }
        el("esa-geom-pmf-plot").setAttribute("aria-label",
          (ar?"احتمال أول نجاح خلال المحاولات الاثنتي عشرة الأولى؛ p = ":"Geometric probability of first success on each of the first twelve trials, p = ")+
          p.toFixed(2)+(ar?"، المحاولة المحددة k = ":", selected trial k = ")+k+
          ", P(X=k) = "+pmf.toFixed(6)+
          (ar?"، والاحتمالان التراكمي والذيلي محسوبان على جميع المحاولات الممكنة.":". Cumulative and tail calculations use all possible trials."));
      }
      [probability,trial].forEach(input=>input.addEventListener("input",update));
      el("esa-geom-reset").addEventListener("click",()=>{
        probability.value="0.25";trial.value="3";update();
      });
      update();
    })();
