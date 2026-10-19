---
layout: default
title: Power Curves and Trade-Offs
description: Learn how power changes with effect size, sample size, significance level, and variability, and understand the key trade-offs in study design.
permalink: /inference/power-sample-size/power-curve-and-tradeoffs/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_inference_power_sample_size_lesson_v0";

  try {
    localStorage.setItem(KEY, JSON.stringify({
    url: "/inference/power-sample-size/power-curve-and-tradeoffs/",
    label: "Power Curves and Trade-Offs",
    ts: Date.now()
    }));
  } catch (_) {
    // Progress is optional if browser storage is denied or unavailable.
  }

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Inference</span>
      <span class="badge">Block 5</span>
      <span class="badge">Power & Sample Size</span>
      <span class="badge">Study Design</span>
    </div>

    <h1>Power Curves and Trade-Offs</h1>

    <p class="lead">
      Statistical power depends on several interacting factors.
    </p>

    <p class="lead">
      Understanding these relationships helps researchers design studies that are both efficient and informative.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/inference/power-sample-size/effect-size-and-practical-importance/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/inference/power-sample-size/sample-size-for-mean/">
         Next: Sample Size for a Mean →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>Review: What Is Power?</h2>

    <p>
      Statistical power is the probability of correctly detecting a real effect.
    </p>

    <p>
      It is defined as:
    </p>

    
    \[
    \text{Power}=P(\text{reject }H_0\mid H_0\text{ false; specified alternative})=1-\beta
    \]


    <p>
      where:
    </p>

    <ul class="bullets">

      <li>β = probability of a Type II error</li>

      <li>1 − β = probability of detecting a true effect</li>

    </ul>

    <h2>Power Is Not Fixed</h2>

    <p>
      Power is not an inherent property of a hypothesis test.
    </p>

    <p>
      Instead, it changes depending on study conditions.
    </p>

    <div class="concept-box">

      <strong>Important idea:</strong>

      <p>
        The same statistical test can have very low power in one study and very high power in another.
      </p>

    </div>

    <h2>The Four Major Drivers of Power</h2>

    <p>
      Power depends primarily on:
    </p>

    <ul class="bullets">

      <li>Effect size</li>

      <li>Sample size</li>

      <li>Significance level (α)</li>

      <li>Variability (noise)</li>

    </ul>

    <p>
      These factors interact to determine how likely a study is to detect a real effect.
    </p>

    <h2>What Is a Power Curve?</h2>

    <p>
      A power curve shows how statistical power changes as the true effect size changes.
    </p>

    <p>
      Conceptually:
    </p>

    <div class="example-box">

      <p>
        Small effects → Lower power
      </p>

      <p>
        Large effects → Higher power
      </p>

    </div>

    <p>
      The curve usually rises as effect size increases.
    </p>


    <!-- POWER CURVE EXPLORER: exact normal-model power; no remote dependencies -->
    <section class="concept-box esa-power-lab" id="esa-power-lab"
             role="group" aria-labelledby="esa-power-lab-heading">
      <h2 id="esa-power-lab-heading">Interactive Two-Sided z-Test Power Explorer</h2>
      <p id="esa-power-lab-assumptions">
        Assume independent observations from a <strong>normal population</strong>,
        a <strong>known population standard deviation σ</strong>, and a
        two-sided test H₀: μ = μ₀ versus H₁: μ ≠ μ₀. The signed true effect
        Δ = μ − μ₀ is specified for planning (not estimated from the
        observed data). The test rejects H₀ if |Z| exceeds its two-sided
        critical value. The curve is an <em>analytical sampling-model calculation</em>,
        not a simulation or a universal power guarantee.
      </p>
      <div class="esa-power-fields">
        <div>
          <label for="esa-power-n">Sample size n:
            <output for="esa-power-n" id="esa-power-n-value">50</output></label>
          <input id="esa-power-n" type="range" min="10" max="200" step="10" value="50"/>
        </div>
        <div>
          <label for="esa-power-delta">True mean difference Δ:
            <output for="esa-power-delta" id="esa-power-delta-value">0.50</output></label>
          <input id="esa-power-delta" type="range" min="-1.5" max="1.5" step="0.05" value="0.5"/>
        </div>
        <div>
          <label for="esa-power-sigma">Known standard deviation σ:
            <output for="esa-power-sigma" id="esa-power-sigma-value">1.00</output></label>
          <input id="esa-power-sigma" type="range" min="0.5" max="3" step="0.25" value="1"/>
        </div>
        <div>
          <label for="esa-power-alpha">Significance level α</label>
          <select id="esa-power-alpha">
            <option value="0.01">0.01 (1%)</option>
            <option value="0.05" selected>0.05 (5%)</option>
            <option value="0.10">0.10 (10%)</option>
          </select>
        </div>
      </div>
      <h3>Probability of rejection by true mean difference</h3>
      <svg id="esa-power-chart" viewBox="0 0 560 268" role="img"
           aria-label="Two-sided normal z-test rejection probability curve, with sample size 50, known standard deviation 1, alpha 0.05 and selected mean difference 0.5"
           aria-describedby="esa-power-lab-chart-caption">
        <line x1="52" y1="30" x2="52" y2="208" class="esa-power-axis"/>
        <line x1="52" y1="208" x2="532" y2="208" class="esa-power-axis"/>
        <line x1="52" y1="119" x2="532" y2="119" class="esa-power-gridline"/>
        <line id="esa-power-null-line" x1="52" y1="199.10"
              x2="532" y2="199.10" class="esa-power-baseline"/>
        <g class="esa-power-ticks" aria-hidden="true">
          <text x="43" y="211" text-anchor="end">0</text>
          <text x="43" y="122" text-anchor="end">0.5</text>
          <text x="43" y="33" text-anchor="end">1</text>
          <text x="52" y="228" text-anchor="middle">−1.5</text>
          <text x="172" y="228" text-anchor="middle">−0.75</text>
          <text x="292" y="228" text-anchor="middle">0</text>
          <text x="412" y="228" text-anchor="middle">0.75</text>
          <text x="532" y="228" text-anchor="middle">1.5</text>
          <text x="292" y="253" text-anchor="middle">True mean difference Δ (population units)</text>
          <text x="13" y="20">Rejection probability</text>
        </g>
        <path id="esa-power-curve" class="esa-power-curve" d="M52.00,NaN L56.00,NaN L60.00,NaN L64.00,NaN L68.00,NaN L72.00,NaN L76.00,NaN L80.00,NaN L84.00,NaN L88.00,NaN L92.00,NaN L96.00,NaN L100.00,NaN L104.00,NaN L108.00,NaN L112.00,NaN L116.00,NaN L120.00,NaN L124.00,NaN L128.00,NaN L132.00,NaN L136.00,NaN L140.00,NaN L144.00,NaN L148.00,NaN L152.00,NaN L156.00,NaN L160.00,NaN L164.00,NaN L168.00,NaN L172.00,NaN L176.00,NaN L180.00,NaN L184.00,NaN L188.00,NaN L192.00,NaN L196.00,NaN L200.00,NaN L204.00,NaN L208.00,NaN L212.00,NaN L216.00,NaN L220.00,NaN L224.00,NaN L228.00,NaN L232.00,NaN L236.00,NaN L240.00,NaN L244.00,NaN L248.00,NaN L252.00,NaN L256.00,NaN L260.00,NaN L264.00,NaN L268.00,NaN L272.00,NaN L276.00,NaN L280.00,NaN L284.00,NaN L288.00,NaN L292.00,199.10 L296.00,NaN L300.00,NaN L304.00,NaN L308.00,NaN L312.00,NaN L316.00,NaN L320.00,NaN L324.00,NaN L328.00,NaN L332.00,NaN L336.00,NaN L340.00,NaN L344.00,NaN L348.00,NaN L352.00,NaN L356.00,NaN L360.00,NaN L364.00,NaN L368.00,NaN L372.00,NaN L376.00,NaN L380.00,NaN L384.00,NaN L388.00,NaN L392.00,NaN L396.00,NaN L400.00,NaN L404.00,NaN L408.00,NaN L412.00,NaN L416.00,NaN L420.00,NaN L424.00,NaN L428.00,NaN L432.00,NaN L436.00,NaN L440.00,NaN L444.00,NaN L448.00,NaN L452.00,NaN L456.00,NaN L460.00,NaN L464.00,NaN L468.00,NaN L472.00,NaN L476.00,NaN L480.00,NaN L484.00,NaN L488.00,NaN L492.00,NaN L496.00,NaN L500.00,NaN L504.00,NaN L508.00,NaN L512.00,NaN L516.00,NaN L520.00,NaN L524.00,NaN L528.00,NaN L532.00,NaN"/>
        <circle id="esa-power-marker" class="esa-power-marker"
                cx="372.00" cy="NaN" r="6"/>
      </svg>
      <p id="esa-power-lab-chart-caption" class="muted-mini">
        Solid curve: probability that the two-sided test rejects H₀ at each
        possible true Δ. Dashed horizontal line: α, the false-rejection
        probability at Δ = 0. Dot: the currently selected Δ.
        Negative and positive effects of equal magnitude have equal power
        under this symmetric two-sided model.
      </p>
      <div class="esa-power-summary" role="status" aria-live="polite" aria-atomic="true">
        <dl>
          <div><dt id="esa-power-rate-label">Power at the specified alternative</dt>
            <dd><output id="esa-power-result-power">0.9424</output></dd></div>
          <div><dt>Type I error probability α (under H₀)</dt>
            <dd><output id="esa-power-result-alpha">0.0500</output></dd></div>
          <div><dt>Type II error probability β (at the specified alternative)</dt>
            <dd><output id="esa-power-result-beta">0.0576</output></dd></div>
          <div><dt>Standardized effect Δ/σ</dt>
            <dd><output id="esa-power-result-effect">0.5000</output></dd></div>
          <div><dt>Noncentral z mean δ = Δ√n/σ</dt>
            <dd><output id="esa-power-result-noncentral">3.5355</output></dd></div>
          <div><dt>Critical threshold ±z₁₋α/₂</dt>
            <dd><output id="esa-power-result-critical">±1.9600</output></dd></div>
        </dl>
        <p class="muted-mini" id="esa-power-null-note">
          β = 1 − power only when Δ ≠ 0 is a specified true alternative.
          At Δ = 0, H₀ is true: the displayed rejection probability equals
          α, and the Type II error concept does not apply.
        </p>
      </div>
      <button type="button" class="btn btn-outline" id="esa-power-reset">
        Reset power example
      </button>
      <p class="muted-mini">
        Calculations use the sampling distribution
        Z ∼ N(δ, 1) when σ is known and the population is normal.
        Increasing α can increase power <em>at the cost of more Type I error</em>.
        This illustration does not model nuisance parameters, unknown σ,
        t-critical values, multiple testing, design effects, or missing data.
      </p>
      \[
      \delta=\frac{\Delta\sqrt{n}}{\sigma},\quad c=z_{1-\alpha/2},
      \qquad\pi(\Delta)=\Phi(-c-\delta)+\Phi(\delta-c).
      \]
    </section>
    <style>
      #esa-power-lab {box-sizing:border-box;width:100%;max-width:100%;min-width:0;overflow-wrap:anywhere}
      #esa-power-lab .esa-power-fields {
        display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,190px),1fr));
        gap:16px;margin:20px 0
      }
      #esa-power-lab .esa-power-fields>div {min-width:0}
      #esa-power-lab .esa-power-fields label {display:block;font-weight:600;margin-bottom:8px}
      #esa-power-lab input[type=range],#esa-power-lab select {
        box-sizing:border-box;display:block;width:100%;max-width:100%;min-width:0;
        min-height:28px;margin:0
      }
      #esa-power-lab h3 {font-size:1.05em;margin:18px 0 8px}
      #esa-power-lab svg {display:block;width:100%;max-width:100%;height:auto;min-width:0;overflow:visible}
      #esa-power-lab .esa-power-axis {stroke:currentColor;stroke-width:1.5}
      #esa-power-lab .esa-power-gridline {stroke:#94a3b8;stroke-width:1;opacity:.5}
      #esa-power-lab .esa-power-baseline {stroke:#64748b;stroke-width:2;stroke-dasharray:6 4}
      #esa-power-lab .esa-power-curve {stroke:#0f766e;stroke-width:3;fill:none}
      #esa-power-lab .esa-power-marker {fill:#0f766e;stroke:currentColor;stroke-width:1}
      #esa-power-lab .esa-power-ticks text {font-size:12px;fill:currentColor}
      #esa-power-lab .esa-power-summary dl {
        display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,230px),1fr));
        gap:12px;margin:18px 0
      }
      #esa-power-lab .esa-power-summary dl>div {
        min-width:0;padding:10px;border:1px solid #9ca3af;border-radius:6px
      }
      #esa-power-lab .esa-power-summary dt {margin:0 0 5px}
      #esa-power-lab .esa-power-summary dd {font-weight:700;margin:0;font-variant-numeric:tabular-nums}
      #esa-power-lab #esa-power-reset {margin:8px 0 14px}
      @media (prefers-contrast:more) {
        #esa-power-lab .esa-power-curve {stroke-width:5}
        #esa-power-lab .esa-power-marker {stroke-width:3}
      }
      @media print {
        #esa-power-lab svg {max-width:520px}
        #esa-power-lab .esa-power-fields {display:none}
      }
    </style>
    <script>
    (function () {
      "use strict";
      const root=document.getElementById("esa-power-lab");
      if (!root) return;
      const elem=id=>root.querySelector("#"+id);
      const nInput=elem("esa-power-n"), dInput=elem("esa-power-delta"),
            sInput=elem("esa-power-sigma"), aInput=elem("esa-power-alpha");
      const critical={"0.01":2.5758293035489004,
                      "0.05":1.959963984540054,
                      "0.10":1.6448536269514722};
      // Standard normal CDF, A&S 26.2.17; absolute error below ~8e-8.
      function phi(x) {
        const ax=Math.abs(x),t=1/(1+0.2316419*ax);
        const poly=t*(0.319381530+
          t*(-0.356563782+
          t*(1.781477937+
          t*(-1.821255978+t*1.330274429))));
        const upper=Math.exp(-ax*ax/2)/Math.sqrt(2*Math.PI)*poly;
        return x>=0?1-upper:upper;
      }
      function rejection(n,d,sigma,alpha) {
        if (d===0) return alpha; // Equal to the Type I error probability by construction.
        const nc=d*Math.sqrt(n)/sigma,c=critical[alpha.toFixed(2)];
        return Math.max(0,Math.min(1,phi(-c-nc)+phi(nc-c)));
      }
      const xPos=d=>52+(d+1.5)*160,yPos=p=>208-p*178;
      const show=(id,x,places=4)=>{elem(id).textContent=x.toFixed(places);};
      function update() {
        const n=Number(nInput.value), d=Number(dInput.value),
              sigma=Number(sInput.value), alpha=Number(aInput.value);
        const c=critical[alpha.toFixed(2)];
        const nc=d*Math.sqrt(n)/sigma,p=rejection(n,d,sigma,alpha);
        const isNull=Math.abs(d)<1e-12;
        show("esa-power-n-value",n,0);
        show("esa-power-delta-value",d,2);
        show("esa-power-sigma-value",sigma,2);
        show("esa-power-result-power",p);
        show("esa-power-result-alpha",alpha);
        show("esa-power-result-effect",d/sigma);
        show("esa-power-result-noncentral",nc);
        elem("esa-power-result-critical").textContent="±"+c.toFixed(4);
        elem("esa-power-result-beta").textContent=isNull?
          "N/A (null true)":(1-p).toFixed(4);
        elem("esa-power-rate-label").textContent=isNull?
          "Rejection probability under H₀ (Type I error)":
          "Power at the specified true alternative";
        const pts=[];
        for(let i=0;i<=120;i++) {
          const x=-1.5+3*i/120,prob=rejection(n,x,sigma,alpha);
          pts.push((i?"L":"M")+xPos(x).toFixed(2)+","+yPos(prob).toFixed(2));
        }
        elem("esa-power-curve").setAttribute("d",pts.join(" "));
        elem("esa-power-marker").setAttribute("cx",xPos(d).toFixed(2));
        elem("esa-power-marker").setAttribute("cy",yPos(p).toFixed(2));
        const line=elem("esa-power-null-line");
        line.setAttribute("y1",yPos(alpha).toFixed(2));
        line.setAttribute("y2",yPos(alpha).toFixed(2));
        elem("esa-power-chart").setAttribute("aria-label",
          "Two-sided normal z-test rejection probability curve. Sample size "+n+
          ", known standard deviation "+sigma.toFixed(2)+
          ", alpha "+alpha.toFixed(2)+", selected mean difference "+d.toFixed(2)+
          ", rejection probability "+p.toFixed(4));
      }
      [nInput,dInput,sInput].forEach(x=>x.addEventListener("input",update));
      aInput.addEventListener("change",update);
      elem("esa-power-reset").addEventListener("click",()=>{
        nInput.value="50";dInput.value="0.5";sInput.value="1";aInput.value="0.05";
        update();
      });
      update();
    })();
    </script>

    <h2>Interpreting a Power Curve</h2>

    <p>
      Imagine a study with a fixed sample size.
    </p>

    <p>
      If the true effect is extremely small:
    </p>

    <div class="example-box">

      <p>
        Detection becomes difficult.
      </p>
    </div>

    <p>
      As the effect becomes larger, detection becomes easier and power rises.
    </p>

    <h2>Effect Size and Power</h2>

    <p>
      Larger effects are easier to distinguish from random variation.
    </p>

    <p>
      Therefore:
    </p>

    <div class="concept-box">

      <strong>General rule:</strong>

      <p>
        Increasing effect size increases power.
      </p>

    </div>

    <p>
      This relationship is one of the strongest determinants of statistical power.
    </p>

    <h2>Sample Size and Power</h2>

    <p>
      Larger samples reduce sampling variability.
    </p>

    <p>
      As uncertainty decreases, true effects become easier to detect.
    </p>

    <div class="concept-box">

      <strong>General rule:</strong>

      <p>
        Increasing sample size increases power.
      </p>

    </div>

    <h2>Why Larger Samples Help</h2>

    <p>
      Recall that many standard errors include:
    </p>

    
    \[
    \operatorname{SE}(\bar X)=\frac{\sigma}{\sqrt n}
    \]


    <p>
      As:
    </p>

    
    \[
    n
    \]


    <p>
      grows, standard errors shrink.
    </p>

    <p>
      Smaller standard errors make genuine effects easier to identify.
    </p>

    <h2>Significance Level and Power</h2>

    <p>
      The significance level:
    </p>

    
    \[
    \alpha
    \]


    <p>
      determines how much evidence is required to reject the null hypothesis.
    </p>

    <p>
      A larger α creates a less strict decision rule.
    </p>

    <div class="concept-box">

      <strong>General rule:</strong>

      <p>
        Increasing α increases power.
      </p>

    </div>

    <h2>The Cost of Increasing α</h2>

    <p>
      Raising:
    </p>

    
    \[
    \alpha
    \]


    <p>
      increases power, but it also increases the probability of Type I errors.
    </p>

    <p>
      This illustrates one of the most important trade-offs in statistical inference.
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Change</th>
            <th>Power</th>
            <th>Type I Error Risk</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Increase α</td>
            <td>Higher</td>
            <td>Higher</td>
          </tr>

          <tr>
            <td>Decrease α</td>
            <td>Lower</td>
            <td>Lower</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>Variability and Power</h2>

    <p>
      Greater variability creates more noise in the data.
    </p>

    <p>
      Noise makes it harder to distinguish real effects from random fluctuations.
    </p>

    <div class="concept-box">

      <strong>General rule:</strong>

      <p>
        Increasing variability decreases power.
      </p>

    </div>

    <h2>Signal Versus Noise</h2>

    <p>
      Statistical inference often involves distinguishing:
    </p>

    <ul class="bullets">

      <li>Signal (real effect)</li>

      <li>Noise (random variation)</li>

    </ul>

    <p>
      Higher power occurs when the signal is large relative to the noise.
    </p>

    <h2>A Practical Example</h2>

    <p>
      Suppose two studies investigate the same treatment.
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Study</th>
            <th>Sample Size</th>
            <th>Power</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>A</td>
            <td>50</td>
            <td>Lower</td>
          </tr>

          <tr>
            <td>B</td>
            <td>500</td>
            <td>Higher</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      Assuming all other factors are equal, Study B is more likely to detect the effect.
    </p>

    <h2>Why We Cannot Maximize Everything</h2>

    <p>
      Researchers face practical constraints:
    </p>

    <ul class="bullets">

      <li>Budget limitations</li>

      <li>Time limitations</li>

      <li>Participant availability</li>

      <li>Ethical considerations</li>

    </ul>

    <p>
      Therefore, study design often involves balancing competing objectives.
    </p>

    <h2>The Main Trade-Off</h2>

    <p>
      Researchers want:
    </p>

    <ul class="bullets">

      <li>High power</li>

      <li>Low Type I error rate</li>

      <li>Reasonable sample size</li>

    </ul>

    <p>
      Achieving all three simultaneously is often difficult.
    </p>

    <div class="concept-box">

      <strong>Design challenge:</strong>

      <p>
        Statistical planning is fundamentally a process of balancing risk, precision, and available resources.
      </p>

    </div>

    <h2>Power Analysis Before Data Collection</h2>

    <p>
      Researchers frequently perform power analysis before a study begins.
    </p>

    <p>
      Typical questions include:
    </p>

    <div class="example-box">

      <p>
        How many participants are needed?
      </p>

      <p>
        What effect size can realistically be detected?
      </p>

      <p>
        What power level should be targeted?
      </p>

    </div>

    <p>
      These questions guide sample-size determination.
    </p>

    <h2>The Role of Target Power</h2>

    <p>
      Common targets include:
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Power</th>
            <th>Typical Interpretation</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>0.80</td>
            <td>Widely used minimum target</td>
          </tr>

          <tr>
            <td>0.90</td>
            <td>Stronger protection against Type II errors</td>
          </tr>

          <tr>
            <td>0.95</td>
            <td>Very high detection capability</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>Connecting Everything Together</h2>

    <p>
      Power analysis combines several concepts from previous lessons:
    </p>

    <ul class="bullets">

      <li>Effect size</li>

      <li>Sampling variability</li>

      <li>Hypothesis testing</li>

      <li>Type I errors</li>

      <li>Type II errors</li>

      <li>Study design</li>

    </ul>

    <p>
      These ideas work together to determine whether a study can answer its research question effectively.
    </p>

    <h2>The Bigger Picture</h2>

    <p>
      Statistical power is not determined by a single quantity.
    </p>

    <p>
      Instead, it emerges from the interaction of effect size, sample size, significance level, and variability.
    </p>

    <p>
      Understanding these relationships is essential for designing reliable and informative studies.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        Power curves illustrate how the probability of detecting a real effect changes as study conditions change. Larger effects, larger samples, and higher significance levels generally increase power, while greater variability reduces it.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      One of the most common applications of power analysis is determining how many observations are needed for a study.
    </p>

    <p>
      The next lesson introduces sample-size calculations for estimating and testing population means.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Power curves show how power changes as effect size changes</li>

        <li>Larger effect sizes generally increase power</li>

        <li>Larger sample sizes generally increase power</li>

        <li>Increasing α increases power but also increases Type I error risk</li>

        <li>Greater variability reduces power</li>

        <li>Power reflects the balance between signal and noise</li>

        <li>Study design involves balancing power, error rates, and resources</li>

        <li>Power analysis is a key tool for planning studies before data collection</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/inference/power-sample-size/effect-size-and-practical-importance/">
         ← Previous: Effect Size and Practical Importance
      </a>

      <a class="btn"
         href="/inference/power-sample-size/sample-size-for-mean/">
         Next: Sample Size for a Mean →
      </a>

    </div>

  </div>

</section>