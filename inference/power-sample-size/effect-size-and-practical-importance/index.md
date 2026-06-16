---
layout: default
title: Effect Size and Practical Importance
description: Learn what effect size measures, why statistical significance is not enough, and how practical importance influences statistical decision-making.
permalink: /inference/power-sample-size/effect-size-and-practical-importance/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_inference_power_sample_size_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/inference/power-sample-size/effect-size-and-practical-importance/",
    label: "Effect Size and Practical Importance",
    ts: Date.now()
  }));

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Inference</span>
      <span class="badge">Block 5</span>
      <span class="badge">Power & Sample Size</span>
      <span class="badge">Effect Size</span>
    </div>

    <h1>Effect Size and Practical Importance</h1>

    <p class="lead">
      Statistical significance tells us whether an effect is detectable, but it does not tell us whether that effect matters.
    </p>

    <p class="lead">
      Effect size provides a measure of the magnitude of a phenomenon and helps connect statistical results to real-world importance.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/inference/power-sample-size/what-is-statistical-power/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/inference/power-sample-size/power-curve-and-tradeoffs/">
         Next: Power Curves and Trade-Offs →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>Statistical Significance Is Not Everything</h2>

    <p>
      Consider a study comparing two treatments.
    </p>

    <p>
      With a sufficiently large sample size, even extremely small differences can become statistically significant.
    </p>

    <p>
      For example:
    </p>

    <div class="example-box">

      <p>
        Mean improvement = 0.05 units
      </p>

      <p>
        p-value &lt; 0.001
      </p>

    </div>

    <p>
      Although statistically significant, such a tiny improvement may have little practical value.
    </p>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        Statistical significance answers "Is there evidence of an effect?" while effect size answers "How large is the effect?"
      </p>

    </div>

    <h2>What Is Effect Size?</h2>

    <p>
      Effect size quantifies the magnitude of a relationship, difference, or association.
    </p>

    <p>
      Unlike p-values, effect sizes focus on practical importance rather than statistical evidence.
    </p>

    <h2>Why Effect Size Matters</h2>

    <p>
      Researchers often care about:
    </p>

    <ul class="bullets">

      <li>How much a treatment improves outcomes</li>

      <li>How large a difference exists between groups</li>

      <li>How strong a relationship is</li>

      <li>Whether an effect is meaningful in practice</li>

    </ul>

    <p>
      Effect sizes address these questions directly.
    </p>

    <h2>Statistical vs Practical Significance</h2>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Question</th>
            <th>Statistical Significance</th>
            <th>Effect Size</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Does an effect exist?</td>
            <td>Yes</td>
            <td>No</td>
          </tr>

          <tr>
            <td>How large is the effect?</td>
            <td>No</td>
            <td>Yes</td>
          </tr>

          <tr>
            <td>Depends strongly on sample size?</td>
            <td>Yes</td>
            <td>No</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>An Illustration</h2>

    <p>
      Imagine two studies investigating the same treatment effect.
    </p>

    <div class="example-box">

      <p>
        Study A: Small sample, large effect
      </p>

      <p>
        Study B: Huge sample, tiny effect
      </p>

    </div>

    <p>
      Study B may produce a much smaller p-value even though its effect is less meaningful.
    </p>

    <p>
      This is why effect size is essential.
    </p>

    <h2>Raw Effect Sizes</h2>

    <p>
      Sometimes effect size is expressed directly in original measurement units.
    </p>

    <div class="example-box">

      <p>
        Blood pressure reduced by 12 mmHg
      </p>

      <p>
        Exam score increased by 8 points
      </p>

      <p>
        Revenue increased by $500 per customer
      </p>

    </div>

    <p>
      These values are often easy to interpret.
    </p>

    <h2>Standardized Effect Sizes</h2>

    <p>
      In many situations, researchers want a scale-free measure that allows comparisons across studies.
    </p>

    <p>
      Standardized effect sizes accomplish this goal.
    </p>

    <h2>Cohen's d</h2>

    <p>
      One of the most common standardized measures is:
    </p>

    0

    <p>
      Cohen's d measures the size of a mean difference relative to variability.
    </p>

    <h2>Interpreting Cohen's d</h2>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Approximate d</th>
            <th>Interpretation</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>0.2</td>
            <td>Small effect</td>
          </tr>

          <tr>
            <td>0.5</td>
            <td>Medium effect</td>
          </tr>

          <tr>
            <td>0.8</td>
            <td>Large effect</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      These guidelines are only rough conventions.
    </p>

    <p>
      Context always matters.
    </p>

    <h2>Effect Size for Proportions</h2>

    <p>
      For proportion-based studies, practical importance may be expressed through:
    </p>

    <ul class="bullets">

      <li>Difference in proportions</li>

      <li>Relative risk</li>

      <li>Odds ratios</li>

    </ul>

    <p>
      The appropriate measure depends on the application.
    </p>

    <h2>Effect Size for Relationships</h2>

    <p>
      When studying associations between variables, common effect-size measures include:
    </p>

    <ul class="bullets">

      <li>Correlation coefficients</li>

      <li>R² values</li>

      <li>Cramér's V</li>

    </ul>

    <p>
      Different statistical methods use different effect-size metrics.
    </p>

    <h2>Effect Size and Power</h2>

    <p>
      Effect size plays a central role in power analysis.
    </p>

    <p>
      Larger effects are easier to detect.
    </p>

    <p>
      Smaller effects require larger samples.
    </p>

    <div class="concept-box">

      <strong>Fundamental relationship:</strong>

      <p>
        As effect size increases, statistical power generally increases.
      </p>

    </div>

    <h2>A Simple Example</h2>

    <p>
      Suppose two studies have identical sample sizes.
    </p>

    <div class="example-box">

      <p>
        Effect A: Very small
      </p>

      <p>
        Effect B: Very large
      </p>

    </div>

    <p>
      The study investigating Effect B is much more likely to achieve statistical significance.
    </p>

    <h2>Clinical Importance</h2>

    <p>
      In medicine, statistical significance alone is rarely sufficient.
    </p>

    <p>
      Researchers also ask:
    </p>

    <div class="example-box">

      <p>
        Is the improvement large enough to help patients?
      </p>
    </div>

    <p>
      Practical significance often drives real-world decisions.
    </p>

    <h2>Business Importance</h2>

    <p>
      In business settings, a statistically significant change may still be economically irrelevant.
    </p>

    <p>
      For example:
    </p>

    <div class="example-box">

      <p>
        A conversion-rate increase of 0.01%
      </p>
    </div>

    <p>
      may or may not justify implementation costs.
    </p>

    <h2>Reporting Best Practices</h2>

    <p>
      Modern statistical reporting often includes:
    </p>

    <ul class="bullets">

      <li>Effect size estimates</li>

      <li>Confidence intervals</li>

      <li>p-values</li>

      <li>Power considerations</li>

    </ul>

    <p>
      Together these provide a more complete picture than any single statistic.
    </p>

    <h2>Effect Size and Research Planning</h2>

    <p>
      Before data collection, researchers often specify the smallest effect that would be scientifically or practically meaningful.
    </p>

    <p>
      This target effect size becomes a key input for sample-size calculations.
    </p>

    <h2>The Bigger Picture</h2>

    <p>
      Statistical inference is not only about determining whether effects exist.
    </p>

    <p>
      It is also about understanding whether those effects matter.
    </p>

    <p>
      Effect size provides the bridge between statistical conclusions and real-world importance.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        Effect size measures the magnitude of an effect, while statistical significance measures evidence for its existence. Practical decision-making requires understanding both.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      Power depends strongly on effect size, but it is also influenced by sample size and significance level.
    </p>

    <p>
      Understanding how these quantities interact helps researchers design efficient studies.
    </p>

    <p>
      The next lesson introduces power curves and the trade-offs among effect size, sample size, power, and significance thresholds.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Statistical significance and practical importance are different concepts</li>

        <li>Effect size measures the magnitude of an effect</li>

        <li>Large samples can make tiny effects statistically significant</li>

        <li>Cohen's d is a common standardized effect-size measure</li>

        <li>Different analyses use different effect-size metrics</li>

        <li>Larger effects are easier to detect and increase power</li>

        <li>Effect size is essential for sample-size planning</li>

        <li>Modern reporting should include both significance measures and effect-size measures</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/inference/power-sample-size/what-is-statistical-power/">
         ← Previous: What Is Statistical Power?
      </a>

      <a class="btn"
         href="/inference/power-sample-size/power-curve-and-tradeoffs/">
         Next: Power Curves and Trade-Offs →
      </a>

    </div>

  </div>

</section>