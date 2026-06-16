---
layout: default
title: Interpreting Effect Sizes
description: Learn how to interpret effect sizes, understand their practical meaning, and use them alongside p-values and confidence intervals.
permalink: /inference/interpretation-reporting/interpreting-effect-sizes/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_inference_interpretation_reporting_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/inference/interpretation-reporting/interpreting-effect-sizes/",
    label: "Interpreting Effect Sizes",
    ts: Date.now()
  }));

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Inference</span>
      <span class="badge">Block 6</span>
      <span class="badge">Interpretation & Reporting</span>
      <span class="badge">Effect Sizes</span>
    </div>

    <h1>Interpreting Effect Sizes</h1>

    <p class="lead">
      Statistical significance tells us whether evidence exists for an effect.
    </p>

    <p class="lead">
      Effect sizes help answer a different question: how large is that effect, and does it matter in practice?
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/inference/interpretation-reporting/interpreting-confidence-intervals/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/inference/interpretation-reporting/multiple-testing-and-false-positives/">
         Next: Multiple Testing and False Positives →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>Why Effect Sizes Matter</h2>

    <p>
      Suppose two studies both produce:
    </p>

    <div class="example-box">

      <p>
        p &lt; 0.001
      </p>
    </div>

    <p>
      Both results are statistically significant.
    </p>

    <p>
      Yet one effect may be tiny while the other is substantial.
    </p>

    <p>
      To understand magnitude, we need effect sizes.
    </p>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        Effect sizes measure the strength or magnitude of a phenomenon rather than merely its detectability.
      </p>

    </div>

    <h2>Statistical Significance vs Effect Size</h2>

    <p>
      These quantities answer different questions.
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Measure</th>
            <th>Main Question</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>P-Value</td>
            <td>Is there evidence against H₀?</td>
          </tr>

          <tr>
            <td>Effect Size</td>
            <td>How large is the effect?</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      Both pieces of information are important.
    </p>

    <h2>Raw Effect Sizes</h2>

    <p>
      Some effect sizes are reported directly in the original measurement units.
    </p>

    <p>
      Examples include:
    </p>

    <ul class="bullets">

      <li>Increase of 5 test-score points</li>

      <li>Decrease of 10 mmHg in blood pressure</li>

      <li>Increase of $500 in monthly revenue</li>

    </ul>

    <p>
      These measures are often intuitive because they retain their original units.
    </p>

    <h2>Standardized Effect Sizes</h2>

    <p>
      Sometimes researchers want to compare effects measured on different scales.
    </p>

    <p>
      Standardized effect sizes remove units and place effects on a common scale.
    </p>

    <h2>Cohen's d</h2>

    <p>
      One of the most common standardized effect-size measures is:
    </p>

    

    <p>
      Cohen's d expresses a mean difference relative to the variability in the data.
    </p>

    <h2>Traditional Guidelines</h2>

    <p>
      Cohen proposed rough benchmarks:
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Cohen's d</th>
            <th>Traditional Interpretation</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>0.2</td>
            <td>Small</td>
          </tr>

          <tr>
            <td>0.5</td>
            <td>Medium</td>
          </tr>

          <tr>
            <td>0.8</td>
            <td>Large</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      These values are useful starting points, but they should never replace subject-matter knowledge.
    </p>

    <h2>Context Matters</h2>

    <p>
      An effect considered small in one field may be extremely important in another.
    </p>

    <p>
      For example:
    </p>

    <ul class="bullets">

      <li>A small reduction in mortality may save thousands of lives</li>

      <li>A small increase in manufacturing defects may be costly</li>

      <li>A small educational improvement may affect millions of students</li>

    </ul>

    <p>
      Practical significance depends on context.
    </p>

    <h2>Correlation Effect Sizes</h2>

    <p>
      Correlation coefficients are also effect-size measures.
    </p>

    <p>
      They describe the strength of a relationship between variables.
    </p>

    <p>
      Values closer to:
    </p>

    <div class="example-box">

      <p>
        -1 or +1
      </p>
    </div>

    <p>
      indicate stronger associations.
    </p>

    <p>
      Values near:
    </p>

    <div class="example-box">

      <p>
        0
      </p>
    </div>

    <p>
      indicate weak relationships.
    </p>

    <h2>Effect Sizes for Proportions</h2>

    <p>
      For categorical outcomes, effect sizes may be reported using:
    </p>

    <ul class="bullets">

      <li>Difference in proportions</li>

      <li>Risk ratios</li>

      <li>Odds ratios</li>

      <li>Relative risk reduction</li>

    </ul>

    <p>
      Different contexts require different measures.
    </p>

    <h2>Effect Size and Sample Size</h2>

    <p>
      Unlike p-values, effect sizes are not directly driven by sample size.
    </p>

    <p>
      A large sample may make a tiny effect statistically significant, but the effect size itself remains small.
    </p>

    <div class="concept-box">

      <strong>Important distinction:</strong>

      <p>
        Statistical significance can change with sample size, while effect size describes magnitude.
      </p>

    </div>

    <h2>Why Confidence Intervals Help</h2>

    <p>
      Effect-size estimates are subject to sampling variability.
    </p>

    <p>
      Therefore researchers often report:
    </p>

    <ul class="bullets">

      <li>Effect size estimate</li>

      <li>Confidence interval for the effect size</li>

    </ul>

    <p>
      This communicates both magnitude and uncertainty.
    </p>

    <h2>An Example</h2>

    <p>
      Consider two reports:
    </p>

    <div class="example-box">

      <p>
        Cohen's d = 0.60
      </p>

      <p>
        95% CI: (0.15, 1.05)
      </p>

    </div>

    <p>
      The estimated effect is moderate, but the interval indicates considerable uncertainty about the exact magnitude.
    </p>

    <h2>Practical Decision-Making</h2>

    <p>
      Effect sizes often drive real-world decisions.
    </p>

    <p>
      Examples include:
    </p>

    <ul class="bullets">

      <li>Approving medical treatments</li>

      <li>Implementing educational interventions</li>

      <li>Launching new business strategies</li>

      <li>Changing public policies</li>

    </ul>

    <p>
      Decision-makers care about how much improvement occurs, not merely whether a p-value falls below a threshold.
    </p>

    <h2>A Large Effect Without Significance</h2>

    <p>
      In small studies, substantial effects may fail to reach statistical significance.
    </p>

    <p>
      This often occurs because:
    </p>

    <ul class="bullets">

      <li>Sample sizes are small</li>

      <li>Power is limited</li>

      <li>Estimates are imprecise</li>

    </ul>

    <p>
      Looking only at p-values can obscure potentially important findings.
    </p>

    <h2>A Tiny Effect With Significance</h2>

    <p>
      In very large studies, extremely small effects can become highly significant.
    </p>

    <p>
      Such results should not automatically be interpreted as important.
    </p>

    <p>
      The magnitude of the effect must still be examined.
    </p>

    <h2>Reporting Best Practices</h2>

    <p>
      Modern statistical reporting often includes:
    </p>

    <ul class="bullets">

      <li>P-values</li>

      <li>Effect sizes</li>

      <li>Confidence intervals</li>

      <li>Study limitations</li>

    </ul>

    <p>
      Together these provide a richer understanding of the evidence.
    </p>

    <h2>Common Mistakes</h2>

    <div class="concept-box">

      <strong>Avoid these errors:</strong>

      <ul class="bullets">

        <li>Ignoring effect size and focusing only on p-values</li>

        <li>Assuming statistically significant effects are automatically important</li>

        <li>Applying generic benchmarks without considering context</li>

        <li>Ignoring uncertainty around effect-size estimates</li>

      </ul>

    </div>

    <h2>The Bigger Picture</h2>

    <p>
      Effect sizes help bridge the gap between statistical results and real-world interpretation.
    </p>

    <p>
      They provide information about magnitude, practical importance, and decision relevance.
    </p>

    <p>
      Without effect sizes, statistical conclusions are often incomplete.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        Effect sizes quantify the magnitude of an effect. They complement p-values by helping researchers and decision-makers evaluate whether statistically detectable effects are also practically meaningful.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      Statistical inference often involves many simultaneous tests.
    </p>

    <p>
      When researchers perform numerous hypothesis tests, the chance of obtaining false positives increases.
    </p>

    <p>
      The next lesson examines multiple testing and explains why false-positive rates become a concern when many comparisons are made.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Effect sizes measure the magnitude of an effect</li>

        <li>P-values and effect sizes answer different questions</li>

        <li>Raw effect sizes retain original measurement units</li>

        <li>Standardized effect sizes allow comparison across studies</li>

        <li>Cohen's d is a common measure of standardized mean differences</li>

        <li>Context is essential when interpreting effect sizes</li>

        <li>Confidence intervals communicate uncertainty around effect-size estimates</li>

        <li>Practical decisions should consider effect size, not just statistical significance</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/inference/interpretation-reporting/interpreting-confidence-intervals/">
         ← Previous: Interpreting Confidence Intervals
      </a>

      <a class="btn"
         href="/inference/interpretation-reporting/multiple-testing-and-false-positives/">
         Next: Multiple Testing and False Positives →
      </a>

    </div>

  </div>

</section>