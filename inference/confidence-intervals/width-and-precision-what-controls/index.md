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

  localStorage.setItem(KEY, JSON.stringify({
    url: "/inference/confidence-intervals/width-and-precision-what-controls/",
    label: "Width and Precision — What Controls Them?",
    ts: Date.now()
  }));

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

    0

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

    1

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

    2

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

    3

    <p>
      Notice that larger:
    </p>

    4

    <p>
      directly increases uncertainty.
    </p>

    <h2>Example: Proportion Estimation</h2>

    <p>
      For proportions:
    </p>

    5

    <p>
      Variability depends on:
    </p>

    6

    <h2>When Proportion Variability Is Largest</h2>

    <p>
      The quantity:
    </p>

    7

    <p>
      is largest when:
    </p>

    8

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