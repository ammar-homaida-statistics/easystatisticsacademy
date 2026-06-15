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

  localStorage.setItem(KEY, JSON.stringify({
    url: "/inference/power-sample-size/power-curve-and-tradeoffs/",
    label: "Power Curves and Trade-Offs",
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

    0

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

    1

    <p>
      As:
    </p>

    2

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

    3

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

    4

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