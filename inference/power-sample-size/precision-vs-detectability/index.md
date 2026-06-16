---
layout: default
title: Precision vs Detectability
description: Learn the difference between estimating quantities precisely and detecting meaningful effects, and understand how these goals influence study design.
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

<!-- HERO -->

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
      Researchers often assume that all sample-size calculations serve the same purpose.
    </p>

    <p class="lead">
      In reality, some studies prioritize estimating parameters accurately, while others prioritize detecting meaningful effects.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/inference/power-sample-size/sample-size-for-proportion/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/inference/power-sample-size/underpowered-studies/">
         Next: Underpowered Studies →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>Two Different Goals</h2>

    <p>
      Statistical studies are often designed around one of two objectives:
    </p>

    <ul class="bullets">

      <li>Estimating a parameter accurately</li>

      <li>Detecting an effect reliably</li>

    </ul>

    <p>
      These goals are related, but they are not identical.
    </p>

    <div class="concept-box">

      <strong>Key distinction:</strong>

      <p>
        Precision focuses on estimation quality, while detectability focuses on hypothesis-testing performance.
      </p>

    </div>

    <h2>What Is Precision?</h2>

    <p>
      Precision describes how accurately a parameter can be estimated.
    </p>

    <p>
      High precision means estimates tend to fall close to the true value.
    </p>

    <p>
      Precision is commonly assessed through:
    </p>

    <ul class="bullets">

      <li>Margin of error</li>

      <li>Standard error</li>

      <li>Confidence interval width</li>

    </ul>

    <h2>Precision Example</h2>

    <p>
      Suppose a survey estimates voter support at:
    </p>

    <div class="example-box">

      <p>
        52% ± 2%
      </p>
    </div>

    <p>
      This estimate is more precise than:
    </p>

    <div class="example-box">

      <p>
        52% ± 8%
      </p>
    </div>

    <p>
      because the confidence interval is narrower.
    </p>

    <h2>What Is Detectability?</h2>

    <p>
      Detectability refers to the ability of a study to identify a real effect when it exists.
    </p>

    <p>
      Detectability is measured through:
    </p>

    0

    <p>
      High power means real effects are more likely to be discovered.
    </p>

    <h2>Detectability Example</h2>

    <p>
      Suppose a clinical trial investigates whether a treatment improves outcomes.
    </p>

    <p>
      Even if estimates are somewhat noisy, the study may still have enough power to detect a large treatment effect.
    </p>

    <p>
      In this situation:
    </p>

    <div class="example-box">

      <p>
        Detectability is strong even if precision is not perfect.
      </p>
    </div>

    <h2>Comparing the Two Goals</h2>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Goal</th>
            <th>Main Focus</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Precision</td>
            <td>Accurate estimation</td>
          </tr>

          <tr>
            <td>Detectability</td>
            <td>Finding real effects</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>Different Questions</h2>

    <p>
      Precision-based studies ask:
    </p>

    <div class="example-box">

      <p>
        How close is our estimate to the truth?
      </p>
    </div>

    <p>
      Detectability-based studies ask:
    </p>

    <div class="example-box">

      <p>
        Can we reliably discover an effect if it exists?
      </p>
    </div>

    <h2>Confidence Intervals and Precision</h2>

    <p>
      Precision is closely connected to confidence intervals.
    </p>

    <p>
      Narrow intervals imply greater precision.
    </p>

    <p>
      Wide intervals imply greater uncertainty.
    </p>

    <div class="concept-box">

      <strong>Rule:</strong>

      <p>
        Smaller standard errors produce narrower confidence intervals and greater precision.
      </p>

    </div>

    <h2>Power and Detectability</h2>

    <p>
      Detectability is closely connected to hypothesis testing.
    </p>

    <p>
      Larger power means a greater chance of rejecting a false null hypothesis.
    </p>

    <p>
      Low power makes real effects easy to miss.
    </p>

    <h2>Can a Study Have High Precision but Low Detectability?</h2>

    <p>
      Surprisingly, yes.
    </p>

    <p>
      Imagine researchers seek to detect an extremely tiny effect.
    </p>

    <p>
      Estimates may be quite precise, yet the study may still struggle to distinguish the tiny effect from zero.
    </p>

    <h2>Can a Study Have High Detectability but Lower Precision?</h2>

    <p>
      Yes.
    </p>

    <p>
      Large effects are often easy to detect even when confidence intervals remain relatively wide.
    </p>

    <p>
      Detectability and precision are related but not identical objectives.
    </p>

    <h2>The Role of Sample Size</h2>

    <p>
      Increasing sample size generally improves both:
    </p>

    <ul class="bullets">

      <li>Precision</li>

      <li>Detectability</li>

    </ul>

    <p>
      However, the required sample size may differ depending on the study's primary goal.
    </p>

    <h2>Survey Research</h2>

    <p>
      Many surveys focus primarily on precision.
    </p>

    <p>
      Researchers often specify:
    </p>

    <div class="example-box">

      <p>
        Desired margin of error = ±3%
      </p>
    </div>

    <p>
      Sample size is then chosen to achieve that precision target.
    </p>

    <h2>Clinical Trials</h2>

    <p>
      Clinical trials frequently focus on detectability.
    </p>

    <p>
      Researchers often ask:
    </p>

    <div class="example-box">

      <p>
        How many participants are needed to detect a clinically meaningful effect with 80% power?
      </p>
    </div>

    <p>
      Here, power drives the sample-size calculation.
    </p>

    <h2>A Practical Comparison</h2>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Study Type</th>
            <th>Primary Goal</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Opinion Poll</td>
            <td>Precision</td>
          </tr>

          <tr>
            <td>Market Survey</td>
            <td>Precision</td>
          </tr>

          <tr>
            <td>Clinical Trial</td>
            <td>Detectability</td>
          </tr>

          <tr>
            <td>A/B Test</td>
            <td>Detectability</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>The Cost Perspective</h2>

    <p>
      Greater precision requires larger samples.
    </p>

    <p>
      Detecting smaller effects also requires larger samples.
    </p>

    <p>
      Researchers must decide which goal deserves priority given available resources.
    </p>

    <h2>When Both Goals Matter</h2>

    <p>
      Many modern studies aim for:
    </p>

    <ul class="bullets">

      <li>Adequate power</li>

      <li>Reasonably narrow confidence intervals</li>

    </ul>

    <p>
      This approach supports both hypothesis testing and accurate estimation.
    </p>

    <h2>Designing Around Meaningful Effects</h2>

    <p>
      Researchers should not simply maximize sample size.
    </p>

    <p>
      Instead, they should identify:
    </p>

    <ul class="bullets">

      <li>The smallest meaningful effect</li>

      <li>The desired level of precision</li>

      <li>The available budget and resources</li>

    </ul>

    <p>
      Study design becomes a balancing problem.
    </p>

    <h2>Connecting Previous Lessons</h2>

    <p>
      This lesson brings together many earlier concepts:
    </p>

    <ul class="bullets">

      <li>Confidence intervals</li>

      <li>Margin of error</li>

      <li>Statistical power</li>

      <li>Effect size</li>

      <li>Sample-size determination</li>

    </ul>

    <p>
      These concepts work together when planning effective studies.
    </p>

    <h2>The Bigger Picture</h2>

    <p>
      Statistical studies can be designed for different purposes.
    </p>

    <p>
      Some emphasize estimating parameters accurately, while others emphasize detecting meaningful effects.
    </p>

    <p>
      Understanding the distinction helps researchers choose appropriate sample sizes and interpret results more effectively.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        Precision focuses on how accurately a parameter can be estimated, while detectability focuses on the ability to discover real effects. Effective study design requires understanding which objective is most important for the research question.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      One of the most common consequences of poor planning is conducting studies that are too small.
    </p>

    <p>
      Such studies often fail to detect meaningful effects and can lead to misleading conclusions.
    </p>

    <p>
      The next lesson examines underpowered studies and the problems they create for statistical inference and scientific research.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Precision and detectability are related but distinct goals</li>

        <li>Precision focuses on estimation accuracy</li>

        <li>Detectability focuses on discovering real effects</li>

        <li>Confidence intervals are central to precision</li>

        <li>Statistical power is central to detectability</li>

        <li>Sample size influences both objectives</li>

        <li>Different study types may prioritize different goals</li>

        <li>Effective study design balances precision, power, effect size, and resources</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/inference/power-sample-size/sample-size-for-proportion/">
         ← Previous: Sample Size for a Proportion
      </a>

      <a class="btn"
         href="/inference/power-sample-size/underpowered-studies/">
         Next: Underpowered Studies →
      </a>

    </div>

  </div>

</section>