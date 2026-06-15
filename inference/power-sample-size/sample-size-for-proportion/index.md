---
layout: default
title: Precision vs Detectability
description: Learn the difference between estimating parameters precisely and detecting effects statistically, and understand how sample size influences both goals.
permalink: /inference/power-sample-size/precision-vs-detectability/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_inference_power_sample_size_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/inference/power-sample-size/precision-vs-detectability/",
    label: "Precision vs Detectability",
    ts: Date.now()
  }));

})();
</script>

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Inference</span>
      <span class="badge">Block 5</span>
      <span class="badge">Power & Sample Size</span>
      <span class="badge">Study Design</span>
    </div>

    <h1>Precision vs Detectability</h1>

    <p class="lead">
      Researchers often assume that increasing sample size serves a single purpose.
    </p>

    <p class="lead">
      In reality, sample size affects two related but distinct goals: estimating parameters precisely and detecting meaningful effects.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/inference/power-sample-size/sample-size-for-mean/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/inference/power-sample-size/sample-size-for-proportion/">
         Next: Sample Size for a Proportion →
      </a>

    </div>

  </div>

</section>

<section>

  <div class="content-narrow">

    <h2>Two Different Goals</h2>

    <p>
      Statistical studies are often designed for one of two purposes:
    </p>

    <ul class="bullets">

      <li>Estimating a quantity accurately</li>

      <li>Detecting whether an effect exists</li>

    </ul>

    <p>
      These goals are related but not identical.
    </p>

    <h2>What Is Precision?</h2>

    <p>
      Precision refers to how accurately a parameter can be estimated.
    </p>

    <p>
      High precision produces:
    </p>

    <ul class="bullets">

      <li>Narrow confidence intervals</li>

      <li>Small margins of error</li>

      <li>More stable estimates</li>

    </ul>

    <div class="concept-box">

      <strong>Precision focuses on estimation quality.</strong>
    </div>

    <h2>What Is Detectability?</h2>

    <p>
      Detectability refers to a study's ability to identify a real effect.
    </p>

    <p>
      This idea is captured by statistical power.
    </p>

    <p>
      A highly detectable effect is likely to be identified as statistically significant when it truly exists.
    </p>

    <div class="concept-box">

      <strong>Detectability focuses on hypothesis testing.</strong>
    </div>

    <h2>The Connection</h2>

    <p>
      Both precision and detectability improve as sample size increases.
    </p>

    <p>
      However, they answer different questions.
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Goal</th>
            <th>Main Question</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Precision</td>
            <td>How accurately can we estimate?</td>
          </tr>

          <tr>
            <td>Detectability</td>
            <td>Can we detect a real effect?</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>An Estimation Example</h2>

    <p>
      Suppose a survey estimates average household income.
    </p>

    <p>
      The primary goal may be obtaining a confidence interval with a small margin of error.
    </p>

    <p>
      Here, precision is more important than hypothesis testing.
    </p>

    <h2>A Testing Example</h2>

    <p>
      Suppose researchers compare two medical treatments.
    </p>

    <p>
      The primary goal is determining whether the treatments differ.
    </p>

    <p>
      Here, statistical power becomes the main concern.
    </p>

    <h2>How Sample Size Affects Precision</h2>

    <p>
      Recall that standard errors often contain:
    </p>

    0

    <p>
      Increasing sample size reduces standard errors and narrows confidence intervals.
    </p>

    <h2>How Sample Size Affects Detectability</h2>

    <p>
      Smaller standard errors also make true effects easier to distinguish from random variation.
    </p>

    <p>
      Therefore, power generally increases as sample size increases.
    </p>

    <h2>Can a Study Be Precise but Underpowered?</h2>

    <p>
      In some situations, yes.
    </p>

    <p>
      A study may estimate a parameter reasonably well but still lack enough power to detect very small effects.
    </p>

    <p>
      The answer depends on the effect size being investigated.
    </p>

    <h2>Can a Study Detect Tiny Effects?</h2>

    <p>
      Very large samples can detect extremely small effects.
    </p>

    <p>
      However, those effects may have little practical importance.
    </p>

    <div class="concept-box">

      <strong>Important:</strong>

      <p>
        Detectability does not automatically imply practical significance.
      </p>

    </div>

    <h2>The Trade-Off</h2>

    <p>
      Researchers often face a design choice:
    </p>

    <ul class="bullets">

      <li>Estimate precisely</li>

      <li>Detect small effects</li>

      <li>Control costs</li>

    </ul>

    <p>
      Achieving all three simultaneously may require substantial resources.
    </p>

    <h2>Precision-Based Planning</h2>

    <p>
      When estimation is the goal, sample size is usually chosen based on:
    </p>

    <ul class="bullets">

      <li>Margin of error</li>

      <li>Confidence level</li>

      <li>Population variability</li>

    </ul>

    <h2>Power-Based Planning</h2>

    <p>
      When testing is the goal, sample size is usually chosen based on:
    </p>

    <ul class="bullets">

      <li>Target power</li>

      <li>Significance level</li>

      <li>Effect size</li>

      <li>Variability</li>

    </ul>

    <h2>Which Goal Should Come First?</h2>

    <p>
      The answer depends on the research objective.
    </p>

    <div class="example-box">

      <p>
        Surveys often prioritize precision.
      </p>

      <p>
        Experiments often prioritize detectability.
      </p>

    </div>

    <h2>The Bigger Picture</h2>

    <p>
      Precision and detectability are two complementary perspectives on study quality.
    </p>

    <p>
      Both improve with larger samples, but they serve different scientific goals.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        Precision concerns how accurately parameters can be estimated, while detectability concerns whether real effects can be identified. Effective study design requires understanding both objectives and balancing them appropriately.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      Many practical studies focus on estimating or testing population proportions rather than means.
    </p>

    <p>
      The next lesson introduces sample-size calculations for proportions and shows how precision and power concepts extend to percentage-based outcomes.
    </p>

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Precision and detectability are distinct study goals</li>

        <li>Precision focuses on estimation quality</li>

        <li>Detectability focuses on hypothesis testing and power</li>

        <li>Larger samples improve both precision and detectability</li>

        <li>Detecting an effect does not guarantee practical importance</li>

        <li>Estimation studies often prioritize precision</li>

        <li>Experimental studies often prioritize detectability</li>

        <li>Study design requires balancing statistical and practical considerations</li>

      </ul>

    </div>

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/inference/power-sample-size/sample-size-for-mean/">
         ← Previous: Sample Size for a Mean
      </a>

      <a class="btn"
         href="/inference/power-sample-size/sample-size-for-proportion/">
         Next: Sample Size for a Proportion →
      </a>

    </div>

  </div>

</section>