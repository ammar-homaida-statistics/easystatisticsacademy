---
layout: default
title: Confidence Interval for Difference of Proportions
description: Learn how to construct and interpret confidence intervals for the difference between two population proportions.
permalink: /inference/confidence-intervals/ci-for-difference-of-proportions/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_inference_confidence_intervals_lesson_v0";

  try {
    localStorage.setItem(KEY, JSON.stringify({
    url: "/inference/confidence-intervals/ci-for-difference-of-proportions/",
    label: "Confidence Interval for Difference of Proportions",
    ts: Date.now()
  }));
  } catch (_) {
    // Gracefully continue when the browser denies persistent storage.
  }

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Inference</span>
      <span class="badge">Block 2</span>
      <span class="badge">Confidence Intervals</span>
      <span class="badge">Comparing Percentages</span>
    </div>

    <h1>Confidence Interval for Difference of Proportions</h1>

    <p class="lead">
      Many important statistical questions compare percentages between two groups.
    </p>

    <p class="lead">
      Confidence intervals for differences in proportions help estimate how much two population proportions differ while accounting for sampling uncertainty.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/inference/confidence-intervals/ci-for-difference-of-means-independent/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/inference/confidence-intervals/ci-for-paired-mean-difference/">
         Next: CI for Paired Mean Difference →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>The Research Question</h2>

    <p>
      Instead of comparing averages,
      we now compare proportions.
    </p>

    <div class="example-box">

      <p>
        Approval rates for two political candidates
      </p>

      <p>
        Conversion rates for two website designs
      </p>

      <p>
        Recovery rates for two medical treatments
      </p>

      <p>
        Defect rates from two manufacturing processes
      </p>

    </div>

    <p>
      The goal is to estimate how different the population proportions are.
    </p>

    <h2>The Parameter of Interest</h2>

    <p>
      Let:
    </p>

    <ul class="bullets">

      <li>p₁ = population proportion for Group 1</li>

      <li>p₂ = population proportion for Group 2</li>

    </ul>

    <p>
      The parameter of interest is:
    </p>

    \[
p_1-p_2
\]

    <p>
      which represents the true difference between the two population proportions.
    </p>

    <h2>The Estimator</h2>

    <p>
      We estimate the population difference using:
    </p>

    \[
\hat p_1-\hat p_2
\]

    <p>
      where each sample proportion is calculated separately from its own sample.
    </p>

    <h2>Interpreting the Difference</h2>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Difference</th>
            <th>Interpretation</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Positive</td>
            <td>Group 1 has the larger proportion</td>
          </tr>

          <tr>
            <td>Negative</td>
            <td>Group 2 has the larger proportion</td>
          </tr>

          <tr>
            <td>Zero</td>
            <td>No population proportion difference</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>The Confidence Interval Blueprint</h2>

    <p>
      Once again:
    </p>

    \[
\text{Estimate}\ \pm\ \text{Margin of error}
\]

    <p>
      The estimate becomes:
    </p>

    \[
\hat p_1-\hat p_2
\]

    <p>
      and the margin of error is based on the standard error of the difference.
    </p>

    <h2>The Standard Error</h2>

    <p>
      For independent samples:
    </p>

    \[
\widehat{\operatorname{SE}}(\hat p_1-\hat p_2)=\sqrt{\frac{\hat p_1(1-\hat p_1)}{n_1}+\frac{\hat p_2(1-\hat p_2)}{n_2}}
\]

    <p>
      This combines uncertainty from both sample proportions.
    </p>

    <h2>The Confidence Interval Formula</h2>

    <p>
      The standard confidence interval becomes:
    </p>

    \[
(\hat p_1-\hat p_2)\pm z_{1-\alpha/2}\sqrt{\frac{\hat p_1(1-\hat p_1)}{n_1}+\frac{\hat p_2(1-\hat p_2)}{n_2}}
\]

    <p>
      This is the standard large-sample unpooled Wald confidence interval for a difference of two independent population proportions. It can have poor coverage, particularly for small samples or proportions near 0 or 1; score-based methods such as Newcombe's interval are useful alternatives.
    </p>

    <h2>Why z Critical Values Are Used</h2>

    <p>
      The sampling distribution of the difference in sample proportions is approximately normal with independent groups and sufficiently many successes and failures in each group; this approximation and Wald coverage must still be assessed in context.
    </p>

    <p>
      Therefore:
    </p>

    <div class="example-box">

      <p>
        z critical values are used rather than t critical values.
      </p>

    </div>


    <!-- Interactive unpooled Wald difference-in-proportions teaching calculator. -->
    <section class="example-box" id="esa-two-proportion-ci-calculator" aria-labelledby="esa-two-proportion-ci-heading">
      <h2 id="esa-two-proportion-ci-heading">Interactive Two-Proportion Confidence Interval</h2>
      <p>Enter independent-group conversion totals to compute the <strong>unpooled large-sample Wald interval</strong> for Group 1 minus Group 2. The initial values reproduce the A/B example below.</p>
      <div class="esa-proportion-fields">
        <label>Group 1 successes <input id="esa-prop-x1" type="number" min="0" max="10000000" step="1" inputmode="numeric" value="240"></label>
        <label>Group 1 sample size <input id="esa-prop-n1" type="number" min="1" max="10000000" step="1" inputmode="numeric" value="600"></label>
        <label>Group 2 successes <input id="esa-prop-x2" type="number" min="0" max="10000000" step="1" inputmode="numeric" value="180"></label>
        <label>Group 2 sample size <input id="esa-prop-n2" type="number" min="1" max="10000000" step="1" inputmode="numeric" value="600"></label>
        <label>Confidence level
          <select id="esa-prop-level">
            <option value="90">90%</option>
            <option value="95" selected>95%</option>
            <option value="99">99%</option>
          </select>
        </label>
      </div>
      <p role="alert" id="esa-prop-error" hidden></p>
      <div role="status" aria-live="polite" aria-atomic="true" class="esa-proportion-results">
        <p>Estimated Group 1 − Group 2 difference = <output id="esa-prop-difference">10.0000</output> percentage points.</p>
        <p>Unpooled estimated SE = <output id="esa-prop-se">0.027386</output> (proportion units);
           margin of error = <output id="esa-prop-margin">5.3676</output> percentage points.</p>
        <p><output id="esa-prop-confidence">95</output>% Wald confidence interval =
           [<output id="esa-prop-lower">4.6324</output>, <output id="esa-prop-upper">15.3676</output>] percentage points.</p>
      </div>
      <svg id="esa-prop-interval-chart" viewBox="0 0 360 112" width="360" height="112"
           role="img" aria-label="95% confidence interval for Group 1 minus Group 2, 4.63 to 15.37 percentage points; zero is outside the interval">
        <line x1="24" y1="62" x2="336" y2="62" stroke="currentColor"/>
        <line x1="24" y1="57" x2="24" y2="67" stroke="currentColor"/>
        <line x1="336" y1="57" x2="336" y2="67" stroke="currentColor"/>
        <line id="esa-prop-zero" x1="100" x2="100" y1="20" y2="77" stroke="#64748b" stroke-dasharray="3 3"/>
        <line id="esa-prop-range" x1="140" x2="270" y1="42" y2="42" stroke="#0d9488" stroke-width="5" stroke-linecap="round"/>
        <circle id="esa-prop-point" cx="205" cy="42" r="6" fill="#0d9488"/>
        <text id="esa-prop-axis-low" x="24" y="89" font-size="11" text-anchor="start" fill="currentColor">−5 pp</text>
        <text id="esa-prop-axis-high" x="336" y="89" font-size="11" text-anchor="end" fill="currentColor">20 pp</text>
        <text id="esa-prop-zero-label" x="100" y="103" font-size="11" text-anchor="middle" fill="currentColor">0 pp</text>
      </svg>
      <p id="esa-prop-zero-interpretation">Zero is outside this interval; the interval excludes no difference between the population proportions.</p>
      <p id="esa-prop-warning">Each group has at least 10 successes and at least 10 failures.</p>
      <p class="muted-mini">This calculator estimates a difference, not a pooled-null Z test, and does not establish causation. It assumes independent observations in two independent groups. Wald coverage can be poor even when a simple count rule is satisfied; use a score-based or other more reliable procedure when appropriate.</p>
      <button type="button" class="btn btn-outline" id="esa-prop-reset">Reset worked example</button>
    </section>
    <style>
      #esa-two-proportion-ci-calculator{box-sizing:border-box;max-width:100%;min-width:0;overflow-wrap:anywhere}
      #esa-two-proportion-ci-calculator .esa-proportion-fields{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,185px),1fr));gap:12px;margin:14px 0}
      #esa-two-proportion-ci-calculator label{display:flex;flex-direction:column;gap:6px;font-weight:600;min-width:0}
      #esa-two-proportion-ci-calculator input,#esa-two-proportion-ci-calculator select{box-sizing:border-box;width:100%;max-width:100%;padding:8px;font:inherit}
      #esa-two-proportion-ci-calculator svg{display:block;width:100%;height:auto;max-width:550px;margin:12px auto;overflow:visible}
      #esa-two-proportion-ci-calculator p{margin:10px 0}
      #esa-two-proportion-ci-calculator [role="alert"]{font-weight:700}
      @media print{#esa-two-proportion-ci-calculator button,#esa-two-proportion-ci-calculator .esa-proportion-fields{display:none}}
    </style>
    <script>
    (function () {
      "use strict";
      const root=document.getElementById("esa-two-proportion-ci-calculator");
      if(!root)return;
      const el=id=>root.querySelector("#"+id);
      const inputs=["x1","n1","x2","n2"].map(x=>el("esa-prop-"+x));
      const level=el("esa-prop-level");
      const Z={90:1.6448536269514722,95:1.959963984540054,99:2.5758293035489004};
      const outputs=["difference","se","margin","confidence","lower","upper"];
      function clear(message) {
        el("esa-prop-error").hidden=false;
        el("esa-prop-error").textContent=message;
        outputs.forEach(s=>el("esa-prop-"+s).textContent="—");
        el("esa-prop-interval-chart").hidden=true;
        el("esa-prop-zero-interpretation").textContent="Provide valid counts to interpret the interval.";
        el("esa-prop-warning").textContent="";
      }
      function update() {
        const nums=inputs.map(input=>input.value.trim()===""?NaN:Number(input.value));
        const [x1,n1,x2,n2]=nums;
        if(nums.some(n=>!Number.isSafeInteger(n)||n<0||n>10000000)||
           n1===0||n2===0||x1>n1||x2>n2) {
          clear("Use positive whole-number sample sizes up to 10,000,000 and successes between 0 and the matching sample size.");
          return;
        }
        const p1=x1/n1,p2=x2/n2,d=p1-p2;
        const se=Math.sqrt(p1*(1-p1)/n1+p2*(1-p2)/n2);
        const margin=Z[Number(level.value)]*se;
        const lower=d-margin,upper=d+margin;
        el("esa-prop-error").hidden=true;
        el("esa-prop-error").textContent="";
        el("esa-prop-difference").textContent=(100*d).toFixed(4);
        el("esa-prop-se").textContent=se.toFixed(6);
        el("esa-prop-margin").textContent=(100*margin).toFixed(4);
        el("esa-prop-confidence").textContent=level.value;
        el("esa-prop-lower").textContent=(100*lower).toFixed(4);
        el("esa-prop-upper").textContent=(100*upper).toFixed(4);
        const zeroIncluded=lower<=0&&upper>=0;
        el("esa-prop-zero-interpretation").textContent=zeroIncluded?
          "Zero lies inside this interval. The interval does not exclude equal population proportions at the selected confidence level.":
          "Zero lies outside this interval. The interval excludes equal population proportions at the selected confidence level, subject to the method’s assumptions.";
        const small=[x1,n1-x1,x2,n2-x2].some(n=>n<10);
        el("esa-prop-warning").textContent=small?
          "Warning: at least one group has fewer than 10 successes or fewer than 10 failures. The normal approximation and Wald coverage may be unreliable; consider a score-based interval such as Newcombe’s.":
          "Both groups have at least 10 successes and 10 failures. This is a screening rule, not a guarantee of Wald interval coverage.";
        const chart=el("esa-prop-interval-chart");
        chart.hidden=false;
        const pad=Math.max(0.03,margin*0.2);
        const axisMin=Math.min(-0.03,lower-pad),axisMax=Math.max(0.03,upper+pad);
        const sx=x=>24+(x-axisMin)*312/(axisMax-axisMin);
        el("esa-prop-range").setAttribute("x1",sx(lower).toFixed(2));
        el("esa-prop-range").setAttribute("x2",sx(upper).toFixed(2));
        el("esa-prop-point").setAttribute("cx",sx(d).toFixed(2));
        const zeroX=sx(0).toFixed(2);
        ["x1","x2"].forEach(a=>el("esa-prop-zero").setAttribute(a,zeroX));
        el("esa-prop-zero-label").setAttribute("x",zeroX);
        el("esa-prop-axis-low").textContent=(100*axisMin).toFixed(1)+" pp";
        el("esa-prop-axis-high").textContent=(100*axisMax).toFixed(1)+" pp";
        chart.setAttribute("aria-label",level.value+"% Wald confidence interval for Group 1 minus Group 2: "+
          (100*lower).toFixed(2)+" to "+(100*upper).toFixed(2)+
          " percentage points; zero "+(zeroIncluded?"is included.":"is excluded."));
      }
      [...inputs,level].forEach(input=>{
        input.addEventListener("input",update);
        input.addEventListener("change",update);
      });
      el("esa-prop-reset").addEventListener("click",()=>{
        [240,600,180,600].forEach((n,i)=>inputs[i].value=String(n));
        level.value="95";update();
      });
      update();
    })();
    </script>

    <h2>Example Setup</h2>

    <p>
      Suppose an A/B test compares two website versions.
    </p>

    <div class="example-box">

      <p>
        Version A: 240 conversions out of 600 visitors
      </p>

      <p>
        Version B: 180 conversions out of 600 visitors
      </p>

      <p>
        Confidence level = 95%
      </p>

    </div>

    <h2>Step 1: Compute the Sample Proportions</h2>

    <p>
      For Version A:
    </p>

    \[
\hat p_1=\frac{240}{600}=0.40
\]

    <p>
      For Version B:
    </p>

    \[
\hat p_2=\frac{180}{600}=0.30
\]

    <h2>Step 2: Compute the Estimated Difference</h2>

    <p>
      Difference:
    </p>

    \[
\hat p_1-\hat p_2=0.40-0.30=0.10
\]

    <p>
      The sample suggests a 10 percentage-point advantage for Version A.
    </p>

    <h2>Step 3: Compute the Standard Error</h2>

    <p>
      Using:
    </p>

    \[
\widehat{\operatorname{SE}}=\sqrt{\frac{0.40(0.60)}{600}+\frac{0.30(0.70)}{600}}
\]

    <p>
      gives approximately:
    </p>

    \[
\widehat{\operatorname{SE}}=\sqrt{0.00075}\approx0.0273861
\]

    <h2>Step 4: Compute the Margin of Error</h2>

    <p>
      For 95% confidence:
    </p>

    <div class="example-box">

      <p>
        z* = 1.96
      </p>

    </div>

    <p>
      Therefore:
    </p>

    \[
\operatorname{ME}=1.96(0.0273861)\approx0.053676
\]

    <h2>Step 5: Construct the Interval</h2>

    <p>
      Therefore:
    </p>

    \[
0.10\pm0.053676\approx(0.046324,\ 0.153676)
\]

    <p>
      yielding:
    </p>

    <div class="example-box">

      <p>
        (0.0463, 0.1537)
      </p>

    </div>

    <h2>Interpreting the Interval</h2>

    <p>
      Plausible values for:
    </p>

    \[
p_1-p_2
\]

    <p>
      range from approximately:
    </p>

    <div class="example-box">

      <p>
        4.6% to 15.4%
      </p>

    </div>

    <p>
      Under the independent-sample conditions and with a large-sample Wald procedure, the data suggest that Version A's population conversion rate exceeds Version B's by roughly 4.6 to 15.4 percentage points.
    </p>

    <h2>The Importance of Zero</h2>

    <p>
      Just as with mean differences,
      zero has a special interpretation.
    </p>

    <div class="concept-box">

      <strong>Zero difference:</strong>

      <p>
        A difference of zero means the population proportions are equal.
      </p>

    </div>

    <h2>When Zero Is Not in the Interval</h2>

    <p>
      Consider:
    </p>

    <div class="example-box">

      <p>
        (0.046, 0.154)
      </p>

    </div>

    <p>
      Since zero is excluded,
      equal population proportions are not among the plausible values.
    </p>

    <p>
      Evidence suggests a genuine difference exists.
    </p>

    <h2>When Zero Is in the Interval</h2>

    <p>
      Suppose instead the interval were:
    </p>

    <div class="example-box">

      <p>
        (-0.04, 0.08)
      </p>

    </div>

    <p>
      Since zero lies inside the interval,
      equal population proportions remain plausible.
    </p>

    <p>
      Strong evidence for a difference is lacking.
    </p>

    <h2>Conditions for the Interval</h2>

    <p>
      Several assumptions should be checked.
    </p>

    <ul class="bullets">

      <li>Random sampling for population inference; random assignment for a randomized experiment (assignment alone does not ensure population representativeness)</li>

      <li>Independent observations within each group</li>

      <li>Independent groups</li>

      <li>Large enough sample sizes for normal approximations</li>

    </ul>

    <h2>The Success-Failure Conditions</h2>

    <p>
      For each sample:
    </p>

    <div class="concept-box">

      <strong>Check both:</strong>

      <p>
        n₁p̂₁ ≥ 10 and n₁(1−p̂₁) ≥ 10
      </p>

      <p>
        n₂p̂₂ ≥ 10 and n₂(1−p̂₂) ≥ 10
      </p>

    </div>

    <p>
      These conditions support the normal approximation.
    </p>

    <h2>Where These Intervals Are Used</h2>

    <ul class="bullets">

      <li>Election polling</li>

      <li>A/B testing</li>

      <li>Clinical trials</li>

      <li>Marketing studies</li>

      <li>Quality-control comparisons</li>

    </ul>

    <p>
      Comparing percentages is one of the most common tasks in applied statistics.
    </p>

    <h2>Difference of Means vs Difference of Proportions</h2>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Feature</th>
            <th>Means</th>
            <th>Proportions</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>Parameter</td>
            <td>μ₁ − μ₂</td>
            <td>p₁ − p₂</td>
          </tr>

          <tr>
            <td>Estimator</td>
            <td>x̄₁ − x̄₂</td>
            <td>p̂₁ − p̂₂</td>
          </tr>

          <tr>
            <td>Critical Value</td>
            <td>Usually t</td>
            <td>z</td>
          </tr>

        </tbody>

      </table>

    </div>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        Confidence intervals for differences in proportions estimate how much two population percentages differ while accounting for uncertainty from both samples.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      Not all comparisons involve independent groups.
    </p>

    <p>
      Many studies measure the same subjects twice, such as before-and-after experiments.
    </p>

    <p>
      The next lesson introduces confidence intervals for paired mean differences, where observations are naturally linked rather than independent.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>The parameter of interest is p₁ − p₂</li>

        <li>The estimator is p̂₁ − p̂₂</li>

        <li>The standard error combines uncertainty from both samples</li>

        <li>The interval uses z critical values</li>

        <li>Zero represents equal population proportions</li>

        <li>If zero is outside the interval, evidence suggests a true difference</li>

        <li>Success-failure conditions should be checked in both groups</li>

        <li>Difference-of-proportion intervals are widely used in polling, experiments, and A/B testing</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/inference/confidence-intervals/ci-for-difference-of-means-independent/">
         ← Previous: CI for Difference of Means
      </a>

      <a class="btn"
         href="/inference/confidence-intervals/ci-for-paired-mean-difference/">
         Next: CI for Paired Mean Difference →
      </a>

    </div>

  </div>

</section>