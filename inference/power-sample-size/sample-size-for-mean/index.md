---
layout: default
title: Sample Size for a Mean
description: Learn how sample size requirements are determined for estimating and testing population means with desired precision and power.
permalink: /inference/power-sample-size/sample-size-for-mean/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_inference_power_sample_size_lesson_v0";

  try {
    localStorage.setItem(KEY, JSON.stringify({
    url: "/inference/power-sample-size/sample-size-for-mean/",
    label: "Sample Size for a Mean",
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
      <span class="badge">Study Planning</span>
    </div>

    <h1>Sample Size for a Mean</h1>

    <p class="lead">
      One of the most important questions in study design is determining how many observations are needed before collecting data.
    </p>

    <p class="lead">
      Sample-size calculations help researchers achieve desired precision and statistical power while using resources efficiently.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/inference/power-sample-size/power-curve-and-tradeoffs/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/inference/power-sample-size/sample-size-for-proportion/">
         Next: Sample Size for a Proportion →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>Why Sample Size Matters</h2>

    <p>
      Sample size influences nearly every aspect of statistical inference.
    </p>

    <ul class="bullets">

      <li>Precision of estimates</li>

      <li>Width of confidence intervals</li>

      <li>Statistical power</li>

      <li>Reliability of conclusions</li>

    </ul>

    <p>
      Studies that are too small may miss important effects, while studies that are unnecessarily large may waste time and resources.
    </p>

    <div class="concept-box">

      <strong>Goal:</strong>

      <p>
        Choose a sample size that is large enough to answer the research question but not larger than necessary.
      </p>

    </div>

    <h2>Two Common Objectives</h2>

    <p>
      Sample-size calculations for means typically arise in two situations:
    </p>

    <ul class="bullets">

      <li>Estimating a population mean with desired precision</li>

      <li>Testing hypotheses with desired statistical power</li>

    </ul>

    <p>
      Although related, these objectives use slightly different approaches.
    </p>

    <h2>Precision-Based Planning</h2>

    <p>
      Suppose we want to estimate a population mean and construct a confidence interval.
    </p>

    <p>
      We may ask:
    </p>

    <div class="example-box">

      <p>
        How large should the sample be so the estimate is accurate within a desired margin of error?
      </p>
    </div>

    <h2>Recall the Confidence Interval Formula</h2>

    <p>
      For a mean with known population standard deviation:
    </p>

    
    \[
    \bar x\pm z_{1-\alpha/2}\frac{\sigma}{\sqrt n}
    \]


    <p>
      The margin of error is:
    </p>

    
    \[
    E=z_{1-\alpha/2}\frac{\sigma}{\sqrt n}
    \]


    <h2>Solving for Sample Size</h2>

    <p>
      Rearranging the margin-of-error formula gives:
    </p>

    
    \[
    n=\left(\frac{z_{1-\alpha/2}\sigma}{E}\right)^2
    \]


    <p>
      This is the classic sample-size formula for estimating a population mean.
    </p>

    <h2>Interpreting the Formula</h2>

    <p>
      The required sample size increases when:
    </p>

    <ul class="bullets">

      <li>Higher confidence is desired</li>

      <li>Population variability is larger</li>

      <li>Greater precision is required</li>

    </ul>

    <p>
      Smaller margins of error require substantially larger samples.
    </p>

    <h2>Example Calculation</h2>

    <p>
      Suppose:
    </p>

    <div class="example-box">

      <p>95% confidence</p>
      <p>σ = 20</p>
      <p>Desired margin of error = 4</p>

    </div>

    <p>
      Using:
    </p>

    
    \[
    n=\left(\frac{1.96\times20}{4}\right)^2
    \]


    <p>
      gives:
    </p>

    
    \[
    n=96.04\quad\Longrightarrow\quad n_{\min}=\lceil96.04\rceil=97
    \]


    <p>
      Since sample size must be an integer and rounding down could reduce precision:
    </p>

    <div class="example-box">

      <p>
        Required sample size = 97
      </p>
    </div>


    <!-- INTERACTIVE PRECISION-BASED SAMPLE SIZE FOR A MEAN -->
    <section id="esa-mean-sample-calculator" class="concept-box esa-mean-calc"
             role="group" aria-labelledby="esa-mean-calc-heading">
      <h2 id="esa-mean-calc-heading">Interactive Sample Size for a Mean</h2>
      <p>
        Plan the number of <strong>independent observations</strong> needed for a
        two-sided confidence interval for a population mean with <strong>known or
        assumed planning standard deviation &sigma;</strong>. Choose the desired
        confidence level and absolute margin of error (in the units of the mean).
      </p>
      <div class="esa-mean-fields">
        <div>
          <label for="esa-mean-confidence">Confidence level</label>
          <select id="esa-mean-confidence">
            <option value="90">90% (z = 1.645)</option>
            <option value="95" selected>95% (z = 1.96)</option>
            <option value="99">99% (z = 2.576)</option>
          </select>
        </div>
        <div>
          <label for="esa-mean-sigma">Population standard deviation &sigma; (&gt; 0)</label>
          <input id="esa-mean-sigma" type="number" inputmode="decimal"
                 min="0.000001" step="any" value="20" required>
        </div>
        <div>
          <label for="esa-mean-margin">Target margin of error E (&gt; 0)</label>
          <input id="esa-mean-margin" type="number" inputmode="decimal"
                 min="0.000001" step="any" value="4" required>
        </div>
      </div>
      <div class="esa-mean-output" role="status" aria-live="polite" aria-atomic="true">
        <p id="esa-mean-error" class="esa-mean-error" hidden></p>
        <p><strong>Unrounded required n:</strong> <output id="esa-mean-unrounded">96.0400</output></p>
        <p><strong>Minimum whole observations:</strong> <output id="esa-mean-required">97</output></p>
        <p><strong>Planned margin after rounding:</strong>
          <output id="esa-mean-achieved">3.9802</output></p>
        <p class="muted-mini" id="esa-mean-formula-detail">
          Calculation: (1.96 × 20 / 4)² = 96.0400; round upward to 97.
        </p>
      </div>
      <button type="button" class="btn btn-outline" id="esa-mean-reset">Reset worked example</button>
      <p class="muted-mini">
        Assumptions: simple independent random observations; a specified
        population standard deviation or a credible planning estimate; and a
        normally distributed sample mean (exact for a normal population with
        known &sigma;, otherwise potentially approximate for sufficiently large
        samples). Critical values use the lesson's stated rounding.
        This calculation concerns <strong>confidence-interval precision, not
        hypothesis-testing power</strong>. It does not ensure an estimate lands
        within E of the true mean in every sample, and it does not incorporate
        nonresponse, clustering/design effects or finite-population corrections.
      </p>
    </section>
    <style>
      #esa-mean-sample-calculator {box-sizing:border-box;max-width:100%;min-width:0}
      #esa-mean-sample-calculator * {box-sizing:border-box}
      #esa-mean-sample-calculator .esa-mean-fields {
        display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,180px),1fr));
        gap:.9rem;margin:1rem 0
      }
      #esa-mean-sample-calculator .esa-mean-fields > div {min-width:0}
      #esa-mean-sample-calculator label {display:block;font-weight:650;margin-bottom:.4rem}
      #esa-mean-sample-calculator input,#esa-mean-sample-calculator select {
        display:block;width:100%;max-width:100%;padding:.65rem;
        border:1px solid #888;border-radius:.4rem;
        background:var(--surface,#fff);color:inherit;font:inherit
      }
      #esa-mean-sample-calculator .esa-mean-output {
        padding:.65rem 1rem;border:1px solid #888;border-radius:.5rem;
        margin:1rem 0;overflow-wrap:anywhere
      }
      #esa-mean-sample-calculator .esa-mean-output p {margin:.45rem 0}
      #esa-mean-sample-calculator .esa-mean-error {color:#a12d20;font-weight:650}
      #esa-mean-sample-calculator output {font-variant-numeric:tabular-nums;font-weight:700}
      #esa-mean-sample-calculator button {max-width:100%;white-space:normal}
      @media print {#esa-mean-sample-calculator button {display:none}}
    </style>
    <script>
    (function () {
      "use strict";
      const section = document.getElementById("esa-mean-sample-calculator");
      if (!section) return;
      const byId = (id) => document.getElementById(id);
      const confidence = byId("esa-mean-confidence");
      const sigmaInput = byId("esa-mean-sigma");
      const marginInput = byId("esa-mean-margin");
      const critical = {90:1.645,95:1.96,99:2.576};
      const error = byId("esa-mean-error");
      const unrounded = byId("esa-mean-unrounded");
      const rounded = byId("esa-mean-required");
      const achieved = byId("esa-mean-achieved");
      const details = byId("esa-mean-formula-detail");
      function invalidate(message) {
        error.textContent = message;
        error.hidden = false;
        unrounded.textContent = "—";
        rounded.textContent = "—";
        achieved.textContent = "—";
        details.textContent = "Enter valid positive planning values to calculate.";
      }
      function calculate() {
        const z = critical[Number(confidence.value)];
        const sigma = Number(sigmaInput.value), E = Number(marginInput.value);
        if (!Number.isFinite(sigma) || sigma <= 0 ||
            !Number.isFinite(E) || E <= 0 || sigmaInput.value.trim() === "" ||
            marginInput.value.trim() === "") {
          invalidate("Standard deviation and target margin of error must both be finite numbers greater than zero.");
          return;
        }
        // n0=(z*sigma/E)^2; ceil gives the smallest whole n meeting the
        // planned precision under this normal-model approximation.
        const ratio = z * sigma / E, raw = ratio * ratio;
        if (!Number.isFinite(raw) || raw <= 0 || raw > Number.MAX_SAFE_INTEGER) {
          invalidate("These values give a sample-size requirement outside the reliable numeric range; revise the inputs.");
          return;
        }
        const minimum = Math.max(1, Math.ceil(raw));
        const plannedE = z * sigma / Math.sqrt(minimum);
        if (!Number.isFinite(plannedE)) {
          invalidate("These values produce an unreliable result; revise the inputs.");
          return;
        }
        error.hidden = true;
        error.textContent = "";
        unrounded.textContent = raw.toFixed(4);
        rounded.textContent = minimum.toLocaleString("en-US");
        achieved.textContent = plannedE.toFixed(4);
        details.textContent = "Calculation: (" + z + " × " + sigma + " / " + E +
          ")² = " + raw.toFixed(4) + "; round upward to " +
          minimum.toLocaleString("en-US") + ".";
      }
      function reset() {
        confidence.value = "95";
        sigmaInput.value = "20";
        marginInput.value = "4";
        calculate();
      }
      confidence.addEventListener("change", calculate);
      sigmaInput.addEventListener("input", calculate);
      marginInput.addEventListener("input", calculate);
      byId("esa-mean-reset").addEventListener("click", reset);
      calculate();
    })();
    </script>

    <h2>Always Round Up</h2>

    <p>
      Sample-size calculations are always rounded upward.
    </p>

    <p>
      Rounding down could fail to achieve the desired confidence or precision.
    </p>

    <h2>The Effect of Margin of Error</h2>

    <p>
      Notice that:
    </p>

    
    \[
    n\propto\frac{1}{E^2}\quad(\sigma\text{ and confidence fixed})
    \]


    <p>
      This means reducing the margin of error by half requires approximately four times the sample size.
    </p>

    <h2>A Practical Illustration</h2>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Margin of Error</th>
            <th>Relative Sample Size</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>8</td>
            <td>1×</td>
          </tr>

          <tr>
            <td>4</td>
            <td>4×</td>
          </tr>

          <tr>
            <td>2</td>
            <td>16×</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      Precision can be expensive.
    </p>

    <h2>Planning for Hypothesis Testing</h2>

    <p>
      Sample-size planning for hypothesis testing includes additional considerations.
    </p>

    <p>
      Researchers must specify:
    </p>

    <ul class="bullets">

      <li>Desired power</li>

      <li>Significance level</li>

      <li>Target effect size</li>

      <li>Population variability</li>

    </ul>

    <h2>The Role of Effect Size</h2>

    <p>
      Recall that larger effects are easier to detect.
    </p>

    <p>
      Therefore:
    </p>

    <div class="concept-box">

      <strong>General rule:</strong>

      <p>
        Smaller target effects require larger sample sizes.
      </p>

    </div>

    <h2>The Role of Variability</h2>

    <p>
      Greater variability creates more noise.
    </p>

    <p>
      More observations are needed to separate signal from noise.
    </p>

    <div class="concept-box">

      <strong>General rule:</strong>

      <p>
        Larger standard deviations require larger samples.
      </p>

    </div>

    <h2>The Role of Confidence Level</h2>

    <p>
      Higher confidence levels require larger critical values.
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Confidence Level</th>
            <th>Critical Value</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>90%</td>
            <td>1.645</td>
          </tr>

          <tr>
            <td>95%</td>
            <td>1.96</td>
          </tr>

          <tr>
            <td>99%</td>
            <td>2.576</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      As confidence increases, sample-size requirements also increase.
    </p>

    <h2>Estimating σ in Practice</h2>

    <p>
      The population standard deviation is often unknown before a study begins.
    </p>

    <p>
      Researchers may use:
    </p>

    <ul class="bullets">

      <li>Pilot studies</li>

      <li>Historical studies</li>

      <li>Subject-matter expertise</li>

    </ul>

    <p>
      to obtain a reasonable estimate.
    </p>

    <h2>Balancing Resources and Precision</h2>

    <p>
      Larger samples improve statistical performance, but they also increase:
    </p>

    <ul class="bullets">

      <li>Cost</li>

      <li>Time requirements</li>

      <li>Data collection burden</li>

      <li>Operational complexity</li>

    </ul>

    <p>
      Study planning therefore involves balancing statistical goals against practical constraints.
    </p>

    <h2>When Very Large Samples Are Not Necessary</h2>

    <p>
      Researchers sometimes assume that larger samples are always better.
    </p>

    <p>
      In reality, once a study achieves adequate precision and power, additional observations may provide limited benefit.
    </p>

    <h2>Modern Software</h2>

    <p>
      Most sample-size calculations are performed using statistical software.
    </p>

    <p>
      However, understanding the underlying relationships remains important because software only automates calculations—it does not choose meaningful design goals.
    </p>

    <h2>The Bigger Picture</h2>

    <p>
      Sample-size determination is one of the most important stages of study planning.
    </p>

    <p>
      It connects confidence intervals, statistical power, variability, and effect size into a single design decision.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        Sample-size calculations for means help researchers achieve desired precision and power. Required sample size increases with confidence level, variability, and desired precision, and decreases when larger effects are acceptable.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      Many real-world studies focus on proportions rather than means.
    </p>

    <p>
      Polling, surveys, clinical trials, and quality-control studies frequently estimate percentages and probabilities.
    </p>

    <p>
      The next lesson introduces sample-size calculations for population proportions.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Sample-size planning can focus on precision or power</li>

        <li>The classic precision formula for means is based on the margin of error</li>

        <li>Required sample size increases as desired precision increases</li>

        <li>Higher confidence levels require larger samples</li>

        <li>Greater variability requires larger samples</li>

        <li>Smaller effects require larger samples to detect</li>

        <li>Sample sizes should always be rounded upward</li>

        <li>Sample-size planning balances statistical goals and practical constraints</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/inference/power-sample-size/power-curve-and-tradeoffs/">
         ← Previous: Power Curves and Trade-Offs
      </a>

      <a class="btn"
         href="/inference/power-sample-size/sample-size-for-proportion/">
         Next: Sample Size for a Proportion →
      </a>

    </div>

  </div>

</section>