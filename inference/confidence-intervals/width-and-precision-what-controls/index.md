---
layout: default
title: Width and Precision — What Controls Them?
description: Learn why some confidence intervals are narrow, others are wide, and what factors determine statistical precision.
permalink: /inference/confidence-intervals/width-and-precision-what-controls/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_inference_confidence_intervals_lesson_v0";

  try {
    localStorage.setItem(KEY, JSON.stringify({
    url: "/inference/confidence-intervals/width-and-precision-what-controls/",
    label: "Width and Precision — What Controls Them?",
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
      <span class="badge">Precision</span>
    </div>

    <h1>Width and Precision — What Controls Them?</h1>

    <p class="lead">
      Two studies may estimate the same parameter but produce very different confidence intervals.
    </p>

    <p class="lead">
      Understanding what controls interval width is essential because interval width reflects statistical precision.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/inference/confidence-intervals/ci-for-paired-mean-difference/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/inference/confidence-intervals/common-mistakes-and-interpretation/">
         Next: Common Mistakes and Interpretation →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>Why Interval Width Matters</h2>

    <p>
      Confidence intervals do more than estimate parameters.
    </p>

    <p>
      Their width tells us how precisely the parameter has been estimated.
    </p>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        Narrow intervals indicate greater precision. Wide intervals indicate greater uncertainty.
      </p>

    </div>

    <h2>Precision vs Accuracy</h2>

    <p>
      Precision and accuracy are not the same concept.
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Concept</th>
            <th>Meaning</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Accuracy</td>
            <td>Closeness to the true value</td>
          </tr>

          <tr>
            <td>Precision</td>
            <td>Amount of uncertainty</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      Confidence interval width primarily reflects precision.
    </p>

    <h2>Recall the Interval Blueprint</h2>

    <p>
      Most confidence intervals have the form:
    </p>

    
    \[
    \text{estimate}\pm(\text{critical value})(\text{standard error})
    \]


    <p>
      Therefore interval width is determined by:
    </p>

    <ul class="bullets">

      <li>Critical value</li>

      <li>Standard error</li>

    </ul>

    <h2>The Width Formula</h2>

    <p>
      Since intervals extend equally in both directions,
      total width is:
    </p>

    
    \[
    \text{interval width}=2(\text{critical value})(\text{standard error})
    \]


    <p>
      Any factor that changes the critical value or standard error changes the interval width.
    </p>

    <h2>Factor 1: Confidence Level</h2>

    <p>
      Higher confidence requires wider intervals.
    </p>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Confidence Level</th>
            <th>Approximate z*</th>
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
      As confidence increases,
      the critical value increases.
    </p>

    <p>
      Larger critical values create wider intervals.
    </p>

    <h2>The Confidence Tradeoff</h2>

    <div class="concept-box">

      <strong>Tradeoff:</strong>

      <p>
        More confidence requires sacrificing precision.
      </p>

    </div>

    <p>
      You can have:
    </p>

    <ul class="bullets">

      <li>Higher confidence</li>

      <li>Narrower intervals</li>

    </ul>

    <p>
      but generally not both simultaneously.
    </p>

    <h2>Factor 2: Sample Size</h2>

    <p>
      Sample size is often the most important practical factor.
    </p>

    <p>
      Larger samples reduce standard errors.
    </p>

    <p>
      Smaller standard errors create narrower intervals.
    </p>

    <h2>The Mathematical Relationship</h2>

    <p>
      For many estimators:
    </p>

    
    \[
    \operatorname{SE}\propto\frac{1}{\sqrt n}
    \]


    <p>
      This relationship explains why larger samples increase precision.
    </p>

    <h2>A Common Misunderstanding</h2>

    <p>
      Doubling sample size does not cut interval width in half.
    </p>

    <p>
      Because the square root appears:
    </p>

    <div class="example-box">

      <p>
        To cut the standard error roughly in half, sample size must be increased by about four times.
      </p>

    </div>

    <!-- Batch #75: practical known-sigma precision explorer -->
<section class="concept-box" id="esa-precision-lab" aria-labelledby="esa-pr-heading">
<h2 id="esa-pr-heading">Interactive Confidence Interval Precision and Sample-Size Planning</h2>
<p>Explore the <strong>two-sided normal confidence interval for a population mean with known population σ</strong>. The margin of error is z × σ/√n; the full width is twice the margin. This planning model does not use an estimated sample SD.</p>
<div class="esa-pr-grid">
<div><label for="esa-pr-n">Sample size n (positive integer)</label><input type="number" id="esa-pr-n" min="1" max="1000000000" step="1" value="100"></div>
<div><label for="esa-pr-sigma">Known population standard deviation σ</label><input type="number" id="esa-pr-sigma" min="0" step="any" value="20"></div>
<div><label for="esa-pr-level">Two-sided confidence level</label><select id="esa-pr-level">
<option value="90">90%</option><option value="95" selected>95%</option><option value="99">99%</option>
</select></div>
<div><label for="esa-pr-target">Desired maximum margin of error (same units)</label><input type="number" id="esa-pr-target" min="0" step="any" value="3"></div>
</div>
<button type="button" id="esa-pr-reset" class="btn btn-outline">Restore worked example</button>
<p id="esa-pr-error" role="alert" aria-live="assertive" hidden></p>
<section id="esa-pr-results" aria-label="Confidence interval precision results" aria-live="polite">
<div class="table-wrap"><table><caption>Confidence-interval planning results, six decimal places</caption><tbody>
<tr><th scope="row">Normal critical value z</th><td id="esa-pr-critical">—</td></tr>
<tr><th scope="row">Standard error σ/√n</th><td id="esa-pr-stderr">—</td></tr>
<tr><th scope="row">Margin of error ±</th><td id="esa-pr-margin">—</td></tr>
<tr><th scope="row">Total interval width</th><td id="esa-pr-width">—</td></tr>
<tr><th scope="row">Minimum required integer sample size for target margin</th><td id="esa-pr-needed">—</td></tr>
<tr><th scope="row">Margin at 4n</th><td id="esa-pr-margin4">—</td></tr>
<tr><th scope="row">Width at 4n</th><td id="esa-pr-width4">—</td></tr>
</tbody></table></div>
<svg id="esa-pr-chart" viewBox="0 0 530 210" role="img" aria-label="Interval width at selected sample size and four times the sample size" style="display:block;width:100%;height:auto;max-width:100%"></svg>
<p id="esa-pr-explain"></p>
</section>
<p class="muted-mini">Planning formula: n ≥ (zσ/E)²; use the smallest integer that meets target E. Higher confidence and higher σ widen the interval; increasing n narrows it at a square-root rate. Narrow does not automatically mean accurate or unbiased. Correlation, clustering, selection bias, and unknown σ require a different design or inference model. This is a precision planning exercise—not a calculated CI for observed data.</p>
</section>
<style>
#esa-precision-lab,#esa-precision-lab *{box-sizing:border-box}
#esa-precision-lab{max-width:100%;min-width:0;overflow-wrap:anywhere}
#esa-precision-lab .esa-pr-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px;margin:12px 0}
#esa-precision-lab label{display:block;font-weight:650;margin-bottom:5px}
#esa-precision-lab :is(input,select){width:100%;min-width:0;font:inherit;padding:10px;border:1px solid #777;border-radius:6px}
#esa-precision-lab .table-wrap{max-width:100%;overflow-x:auto}
#esa-precision-lab [hidden]{display:none!important}
#esa-precision-lab :is(input,select,button):focus-visible{outline:2px solid #0f766e;outline-offset:3px}
@media(max-width:640px){#esa-precision-lab .esa-pr-grid{grid-template-columns:minmax(0,1fr)}}
</style>
<script defer src="/js/ci-precision-explorer.js"></script>
<h2>Example of the Sample Size Effect</h2>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Sample Size</th>
            <th>Relative SE</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>100</td>
            <td>1.00</td>
          </tr>

          <tr>
            <td>400</td>
            <td>0.50</td>
          </tr>

          <tr>
            <td>900</td>
            <td>0.33</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      Larger samples improve precision, but with diminishing returns.
    </p>

    <h2>Factor 3: Variability</h2>

    <p>
      More variable data produce larger standard errors.
    </p>

    <p>
      Larger standard errors create wider intervals.
    </p>

    <div class="concept-box">

      <strong>Interpretation:</strong>

      <p>
        Greater variability means less certainty about the parameter.
      </p>

    </div>

    <h2>Example: Mean Estimation</h2>

    <p>
      For means:
    </p>

    
    \[
    \operatorname{SE}(\bar X)=\frac{\sigma}{\sqrt n}
    \]


    <p>
      Notice that larger:
    </p>

    
    \[
    \sigma
    \]


    <p>
      directly increases uncertainty.
    </p>

    <h2>Example: Proportion Estimation</h2>

    <p>
      For proportions:
    </p>

    
    \[
    \widehat{\operatorname{SE}}(\hat p)=\sqrt{\frac{\hat p(1-\hat p)}{n}}
    \]


    <p>
      Variability depends on:
    </p>

    
    \[
    \hat p(1-\hat p)
    \]


    <h2>When Proportion Variability Is Largest</h2>

    <p>
      The quantity:
    </p>

    
    \[
    p(1-p)
    \]


    <p>
      is largest when:
    </p>

    
    \[
    p=0.5
    \]


    <p>
      Therefore proportions near 50% often produce the widest intervals.
    </p>

    <h2>Factor 4: Study Design</h2>

    <p>
      Different designs can affect precision dramatically.
    </p>

    <p>
      For example,
      paired designs often reduce variability.
    </p>

    <div class="example-box">

      <p>
        Before-and-after studies may produce narrower intervals than independent-group studies.
      </p>

    </div>

    <p>
      This occurs because each subject serves as their own control.
    </p>

    <h2>The Precision Triangle</h2>

    <p>
      Interval width is primarily controlled by:
    </p>

    <ul class="bullets">

      <li>Confidence level</li>

      <li>Sample size</li>

      <li>Variability</li>

    </ul>

    <p>
      These three factors appear repeatedly throughout statistical inference.
    </p>

    <h2>What Researchers Can Control</h2>

    <p>
      Before collecting data,
      researchers often have direct control over:
    </p>

    <ul class="bullets">

      <li>Sample size</li>

      <li>Study design</li>

      <li>Desired confidence level</li>

    </ul>

    <p>
      These choices affect the precision of future estimates.
    </p>

    <h2>Margin of Error and Width</h2>

    <p>
      News reports often quote:
    </p>

    <div class="example-box">

      <p>
        Margin of Error = ±3%
      </p>

    </div>

    <p>
      This is simply half of the interval width.
    </p>

    <p>
      Smaller margins of error correspond to more precise estimates.
    </p>

    <h2>Why Extremely Narrow Intervals Are Rare</h2>

    <p>
      Perfect precision is impossible because sampling uncertainty never completely disappears.
    </p>

    <p>
      Extremely narrow intervals typically require:
    </p>

    <ul class="bullets">

      <li>Very large samples</li>

      <li>Low variability</li>

      <li>Moderate confidence levels</li>

    </ul>

    <h2>Interpreting Width Correctly</h2>

    <p>
      A narrow interval suggests:
    </p>

    <div class="example-box">

      <p>
        The parameter has been estimated precisely.
      </p>

    </div>

    <p>
      It does not necessarily imply:
    </p>

    <div class="example-box">

      <p>
        The estimate is correct.
      </p>

    </div>

    <p>
      Bias and poor sampling can still produce misleading results.
    </p>

    <h2>The Bigger Picture</h2>

    <p>
      Confidence intervals communicate both estimates and uncertainty.
    </p>

    <p>
      Their width is one of the most important pieces of information they provide.
    </p>

    <p>
      Understanding what controls interval width helps researchers design studies and interpret results more effectively.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        Confidence interval width is controlled primarily by confidence level, sample size, and variability. Narrow intervals indicate greater precision, while wide intervals indicate greater uncertainty.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      Confidence intervals are frequently misunderstood.
    </p>

    <p>
      Even experienced researchers sometimes make incorrect interpretations.
    </p>

    <p>
      The next lesson examines the most common confidence interval mistakes and how to interpret intervals correctly.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Interval width measures statistical precision</li>

        <li>Precision and accuracy are different concepts</li>

        <li>Higher confidence levels create wider intervals</li>

        <li>Larger samples create narrower intervals</li>

        <li>Greater variability creates wider intervals</li>

        <li>Standard errors often shrink at a rate of 1/√n</li>

        <li>Study design can influence interval precision</li>

        <li>Narrow intervals indicate more precise estimation but not necessarily greater accuracy</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/inference/confidence-intervals/ci-for-paired-mean-difference/">
         ← Previous: CI for Paired Mean Difference
      </a>

      <a class="btn"
         href="/inference/confidence-intervals/common-mistakes-and-interpretation/">
         Next: Common Mistakes and Interpretation →
      </a>

    </div>

  </div>

</section>