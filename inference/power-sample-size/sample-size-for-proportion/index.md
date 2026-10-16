---
layout: default
title: Sample Size for a Proportion
description: Learn how sample-size requirements are determined when estimating or testing population proportions and percentages.
permalink: /inference/power-sample-size/sample-size-for-proportion/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_inference_power_sample_size_lesson_v0";

  try {
    localStorage.setItem(KEY, JSON.stringify({
    url: "/inference/power-sample-size/sample-size-for-proportion/",
    label: "Sample Size for a Proportion",
    ts: Date.now()
  }));
  } catch (_) {
    // The lesson and calculator remain available when persistence is blocked.
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
      <span class="badge">Proportions</span>
    </div>

    <h1>Sample Size for a Proportion</h1>

    <p class="lead">
      Many studies focus on proportions rather than means.
    </p>

    <p class="lead">
      Polling, surveys, quality control, public-health studies, and A/B tests often require determining how many observations are needed to estimate or detect differences in population proportions.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/inference/power-sample-size/sample-size-for-mean/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/inference/power-sample-size/precision-vs-detectability/">
         Next: Precision vs Detectability →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>Why Proportions Matter</h2>

    <p>
      Many important questions involve percentages or probabilities.
    </p>

    <ul class="bullets">

      <li>What proportion of voters support a candidate?</li>

      <li>What fraction of customers make a purchase?</li>

      <li>What percentage of patients respond to treatment?</li>

      <li>What proportion of manufactured items are defective?</li>

    </ul>

    <p>
      Accurate answers require adequate sample sizes.
    </p>

    <h2>Planning for Precision</h2>

    <p>
      Suppose we want to estimate a population proportion:
    </p>

    \[
p
\]

    <p>
      with a specified margin of error.
    </p>

    <p>
      The question becomes:
    </p>

    <div class="example-box">

      <p>
        How many observations are needed to estimate the proportion with sufficient precision?
      </p>
    </div>

    <h2>Recall the Confidence Interval</h2>

    <p>
      For large samples, a confidence interval for a proportion has the form:
    </p>

    \[
\hat p\ \pm\ z_{1-\alpha/2}\sqrt{\frac{\hat p(1-\hat p)}{n}}
\]

    <p>
      The margin of error is therefore:
    </p>

    \[
E\ \approx\ z_{1-\alpha/2}\sqrt{\frac{p_{\mathrm{plan}}(1-p_{\mathrm{plan}})}{n}}
\]

    <h2>Solving for Sample Size</h2>

    <p>
      Rearranging the margin-of-error formula gives:
    </p>

    \[
n_0=\frac{z_{1-\alpha/2}^{\,2}\,p_{\mathrm{plan}}(1-p_{\mathrm{plan}})}{E^2}
\]

    <p>
      This is the classical planning formula for the large-sample Wald margin of error for one population proportion. Choose the planning value p_plan before collecting data; the formula estimates precision, not the sample size needed for statistical hypothesis-testing power.
    </p>

    <h2>The Unknown Proportion Problem</h2>

    <p>
      The formula requires a value of:
    </p>

    \[
p_{\mathrm{plan}}
\]

    <p>
      but the true population proportion is usually unknown before data collection.
    </p>

    <p>
      Researchers often use:
    </p>

    <ul class="bullets">

      <li>Pilot studies</li>

      <li>Historical data</li>

      <li>Expert knowledge</li>

    </ul>

    <p>
      to obtain an estimate.
    </p>

    <h2>The Conservative Choice</h2>

    <p>
      When no information is available, a common strategy is:
    </p>

    \[
p_{\mathrm{plan}}=0.5
\]

    <p>
      because:
    </p>

    \[
p_{\mathrm{plan}}(1-p_{\mathrm{plan}})\le\frac14
\]

    <p>
      is maximized at 0.5.
    </p>

    <p>
      This maximizes the variance factor in this approximate formula, making it conservative with respect to the unknown planning proportion. It does not guarantee actual interval coverage, especially near 0 or 1, or correct for nonrandom sampling or design effects.
    </p>

    <h2>The Conservative Formula</h2>

    <p>
      Substituting:
    </p>

    \[
p_{\mathrm{plan}}=\frac12
\]

    <p>
      yields:
    </p>

    \[
n_0=\frac{z_{1-\alpha/2}^{\,2}}{4E^2}
\]

    <p>
      This is frequently used as a preliminary sample-size calculation for simple random sampling. Real surveys may need finite-population corrections, clustering/design-effect inflation, and allowances for expected nonresponse.
    </p>

    <h2>Example Calculation</h2>

    <p>
      Suppose we want:
    </p>

    <div class="example-box">

      <p>95% confidence</p>
      <p>Margin of error = 0.03</p>

    </div>

    <p>
      Using:
    </p>

    \[
z_{0.975}\approx1.96
\]

    <p>
      and the conservative assumption:
    </p>

    \[
p_{\mathrm{plan}}=0.5
\]

    <p>
      gives:
    </p>

    \[
n_0=\frac{(1.96)^2(0.5)(0.5)}{(0.03)^2}\approx1067.111,\qquad n=\lceil n_0\rceil=1068
\]

    <p>
      Therefore:
    </p>

    <div class="example-box">

      <p>
        Required sample size = 1068
      </p>
    </div>

    <h2>Always Round Up</h2>

    <p>
      As with all sample-size calculations:
    </p>

    <div class="concept-box">

      <strong>Rule:</strong>

      <p>
        Always round the calculated n₀ upward, since rounding down would exceed the planned margin of error in this approximation. The actual sampling error and realized interval width still vary from sample to sample.
      </p>

    </div>


    <!-- PROPORTION SAMPLE SIZE CALCULATOR -->
    <section id="esa-proportion-calculator" class="esa-proportion-calculator concept-box"
             aria-labelledby="esa-proportion-calculator-heading">
      <h2 id="esa-proportion-calculator-heading">Interactive Sample Size for a Proportion</h2>
      <p>Plan an approximate <strong>two-sided confidence interval for one population proportion</strong>.
         Enter a planning proportion and an absolute margin of error (for example, 0.03 means ±3 percentage points).</p>
      <form id="esa-proportion-calculator-form" novalidate>
        <div class="esa-proportion-calculator-fields">
          <div>
            <label for="esa-sample-confidence">Confidence level</label>
            <select id="esa-sample-confidence" name="confidence">
              <option value="90">90% (z = 1.645)</option>
              <option value="95" selected>95% (z = 1.96)</option>
              <option value="99">99% (z = 2.576)</option>
            </select>
          </div>
          <div>
            <label for="esa-sample-margin">Target margin of error E (0–1)</label>
            <input type="number" inputmode="decimal" id="esa-sample-margin"
                   name="margin" required min="0.000001" max="0.999999" step="any" value="0.03">
          </div>
          <div>
            <label for="esa-sample-proportion">Expected proportion p (0–1)</label>
            <input type="number" inputmode="decimal" id="esa-sample-proportion"
                   name="proportion" required min="0.000001" max="0.999999" step="any"
                   value="0.5" disabled>
          </div>
          <div class="esa-proportion-checkbox">
            <label for="esa-sample-conservative">
              <input type="checkbox" id="esa-sample-conservative" name="conservative" checked>
              Use conservative p = 0.5 when the proportion is unknown
            </label>
          </div>
        </div>
        <p class="esa-proportion-formula">Planning formula: <strong>n = ⌈z² × p(1 − p) / E²⌉</strong>,
          where E is the desired half-width, z is the two-sided critical value, and n is always rounded up.</p>
        <div class="example-box">
          <p><strong>Required minimum: <output id="esa-sample-result" for="esa-sample-confidence esa-sample-margin esa-sample-proportion esa-sample-conservative" role="status" aria-live="polite">1,068</output> observations</strong></p>
          <p id="esa-sample-details">The 95% planning calculation uses p = 0.5 and E = 0.03.</p>
          <p id="esa-sample-warning"></p>
        </div>
        <p id="esa-sample-error" role="alert" hidden></p>
      </form>
      <p class="muted-mini"><strong>Assumptions and exclusions:</strong> This is an approximate,
        large-sample Wald-interval precision calculation for independent Bernoulli observations
        under simple random sampling (or a comparable design). It does not apply a
        finite-population correction, complex-sample design effect, anticipated nonresponse
        inflation, or guaranteed-coverage/Wilson adjustment. It is not a hypothesis-test power
        calculator or a guarantee that any realized confidence interval meets the chosen margin.
        In particular, Wald coverage may be poor near p = 0 or p = 1.</p>
    </section>
    <style>
      #esa-proportion-calculator {max-width:100%; min-width:0; overflow-wrap:anywhere;}
      .esa-proportion-calculator-fields {display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px;margin:16px 0;}
      .esa-proportion-calculator-fields > div {min-width:0;}
      #esa-proportion-calculator label {display:block;font-weight:650;margin:0 0 7px;}
      #esa-proportion-calculator input[type="number"],#esa-proportion-calculator select {
        width:100%;max-width:100%;min-width:0;box-sizing:border-box;border:1px solid var(--border-strong);
        background:var(--surface);color:var(--text);border-radius:8px;padding:10px;font:inherit;
      }
      #esa-proportion-calculator input:focus-visible,#esa-proportion-calculator select:focus-visible {
        outline:2px solid var(--accent);outline-offset:2px;
      }
      #esa-proportion-calculator .esa-proportion-checkbox {align-self:center;}
      #esa-proportion-calculator .esa-proportion-checkbox label {display:flex;align-items:flex-start;gap:10px;cursor:pointer;}
      #esa-proportion-calculator input[type="checkbox"] {margin:5px 0 0;flex:0 0 auto;accent-color:var(--brand);}
      #esa-proportion-calculator .esa-proportion-formula {overflow-wrap:anywhere;}
      #esa-sample-error {color:#b42318;font-weight:650;}
      @media (max-width:600px) {
        .esa-proportion-calculator-fields {grid-template-columns:minmax(0,1fr);}
      }
    </style>
    <script>
    (function () {
      const form = document.getElementById("esa-proportion-calculator-form");
      if (!form) return;
      const confidence = document.getElementById("esa-sample-confidence");
      const margin = document.getElementById("esa-sample-margin");
      const proportion = document.getElementById("esa-sample-proportion");
      const conservative = document.getElementById("esa-sample-conservative");
      const result = document.getElementById("esa-sample-result");
      const details = document.getElementById("esa-sample-details");
      const warning = document.getElementById("esa-sample-warning");
      const error = document.getElementById("esa-sample-error");
      // Deliberately use the rounded critical values taught in this lesson.
      const criticalValues = Object.freeze({"90":1.645,"95":1.96,"99":2.576});
      function render() {
        proportion.disabled = conservative.checked;
        const z = criticalValues[confidence.value];
        const p = conservative.checked ? 0.5 : Number(proportion.value);
        const e = Number(margin.value);
        let message = "";
        if (!z) message = "Choose a supported confidence level (90%, 95%, or 99%).";
        else if (!conservative.checked &&
                 (proportion.value.trim() === "" || !Number.isFinite(p) || p <= 0 || p >= 1)) {
          message = "Enter an expected proportion strictly between 0 and 1.";
        } else if (margin.value.trim() === "" || !Number.isFinite(e) || e <= 0 || e >= 1) {
          message = "Enter an absolute margin of error strictly between 0 and 1.";
        }
        if (message) {
          result.textContent = "—";
          details.textContent = "";
          warning.textContent = "";
          error.textContent = message;
          error.hidden = false;
          return;
        }
        const unrounded = z * z * p * (1 - p) / (e * e);
        const n = Math.ceil(unrounded);
        if (!Number.isFinite(unrounded) || !Number.isSafeInteger(n) || n < 1) {
          result.textContent = "—";
          details.textContent = "";
          warning.textContent = "";
          error.textContent = "These inputs exceed the calculator's reliable numerical range.";
          error.hidden = false;
          return;
        }
        error.textContent = "";
        error.hidden = true;
        result.textContent = n.toLocaleString("en-US");
        details.textContent = confidence.value + "% confidence: z = " + z +
          ", planning p = " + p + ", E = " + e +
          ". Unrounded n = " + unrounded.toFixed(3) + "; round up to " +
          n.toLocaleString("en-US") + ".";
        warning.textContent = (n * p < 10 || n * (1 - p) < 10)
          ? "Caution: fewer than 10 expected successes or failures under the planning values; the Wald normal approximation can be poor."
          : "";
      }
      form.addEventListener("submit", event => { event.preventDefault(); render(); });
      form.addEventListener("input", render);
      form.addEventListener("change", render);
      render();
    })();
    </script>

    <h2>Effect of Margin of Error</h2>

    <p>
      Notice that:
    </p>

    \[
n_0\propto\frac{1}{E^2}
\]

    <p>
      Just as with means, halving the margin of error approximately quadruples the required sample size.
    </p>

    <h2>A Precision Illustration</h2>

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
            <td>6%</td>
            <td>1×</td>
          </tr>

          <tr>
            <td>3%</td>
            <td>4×</td>
          </tr>

          <tr>
            <td>1.5%</td>
            <td>16×</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      Small gains in precision can require substantial increases in sample size.
    </p>

    <h2>Planning for Hypothesis Testing</h2>

    <p>
      When testing hypotheses about proportions, sample-size determination depends on:
    </p>

    <ul class="bullets">

      <li>Desired power</li>

      <li>Significance level</li>

      <li>Target effect size</li>

      <li>Baseline proportion</li>

    </ul>

    <h2>The Role of Effect Size</h2>

    <p>
      Suppose a company wants to detect an increase in conversion rate.
    </p>

    <div class="example-box">

      <p>
        From 10% to 11%
      </p>
    </div>

    <p>
      This is a much smaller effect than:
    </p>

    <div class="example-box">

      <p>
        From 10% to 20%
      </p>
    </div>

    <p>
      Smaller effects generally require larger samples to detect at fixed significance level, power, and experimental design. The precision calculator below is not a power calculator.
    </p>

    <h2>The Role of Baseline Proportion</h2>

    <p>
      Variability for proportions depends on:
    </p>

    \[
p_{\mathrm{plan}}(1-p_{\mathrm{plan}})
\]

    <p>
      Variability is highest near:
    </p>

    \[
p_{\mathrm{plan}}=0.5
\]

    <p>
      and decreases as proportions approach 0 or 1.
    </p>

    <p>
      Consequently, required sample sizes also depend on the expected baseline proportion.
    </p>

    <h2>Polling Example</h2>

    <p>
      National election polls often target margins of error around:
    </p>

    <div class="example-box">

      <p>
        ±3%
      </p>
    </div>

    <p>
      which explains why many polls collect roughly one thousand respondents.
    </p>

    <h2>A/B Testing Example</h2>

    <p>
      Online experiments frequently require thousands or even millions of observations because conversion-rate differences can be very small.
    </p>

    <p>
      Detecting tiny effects demands substantial sample sizes.
    </p>

    <h2>Balancing Precision and Cost</h2>

    <p>
      Larger samples improve precision and power, but they also increase:
    </p>

    <ul class="bullets">

      <li>Financial costs</li>

      <li>Time requirements</li>

      <li>Data collection effort</li>

      <li>Operational complexity</li>

    </ul>

    <p>
      Sample-size planning is therefore a balance between statistical goals and practical constraints.
    </p>

    <h2>Modern Software</h2>

    <p>
      Statistical software can compute sample sizes quickly.
    </p>

    <p>
      Researchers must still specify meaningful design targets. The confidence-interval precision formula here does not address effect-size/power calculations for hypothesis tests.
    </p>

    <h2>The Bigger Picture</h2>

    <p>
      Sample-size planning for proportions follows the same principles as planning for means.
    </p>

    <p>
      Researchers specify desired precision or power, then determine the number of observations needed to achieve those goals.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        Sample-size calculations for proportions depend on confidence level, margin of error, baseline proportion, and desired power. Smaller margins of error and smaller detectable effects require substantially larger samples.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      Precision and detectability are closely related but distinct study-design goals.
    </p>

    <p>
      Some studies aim for narrow confidence intervals, while others focus on detecting meaningful effects.
    </p>

    <p>
      The next lesson explores the difference between precision and detectability and explains how these goals influence study design.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Sample-size planning for proportions often focuses on confidence intervals or power</li>

        <li>The classic formula approximates a desired Wald margin of error under simple random sampling</li>

        <li>When p is unknown, p = 0.5 provides a conservative sample-size estimate</li>

        <li>Smaller margins of error require much larger samples</li>

        <li>Required sample size depends on baseline proportion and variability</li>

        <li>Smaller effects require larger samples to detect</li>

        <li>Polling and A/B testing rely heavily on proportion-based sample-size calculations</li>

        <li>Effective study design balances statistical goals and practical limitations</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/inference/power-sample-size/sample-size-for-mean/">
         ← Previous: Sample Size for a Mean
      </a>

      <a class="btn"
         href="/inference/power-sample-size/precision-vs-detectability/">
         Next: Precision vs Detectability →
      </a>

    </div>

  </div>

</section>