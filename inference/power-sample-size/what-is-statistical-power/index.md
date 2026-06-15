---
layout: default
title: What Is Statistical Power?
description: Learn what statistical power means, why it matters, and how it connects to Type II errors, effect size, and study design.
permalink: /inference/power-sample-size/what-is-statistical-power/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_inference_power_sample_size_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/inference/power-sample-size/what-is-statistical-power/",
    label: "What Is Statistical Power?",
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

    <h1>What Is Statistical Power?</h1>

    <p class="lead">
      Before collecting data, researchers want to know whether a study has a realistic chance of detecting an important effect.
    </p>

    <p class="lead">
      Statistical power measures a test's ability to discover real effects when they truly exist.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/inference/power-sample-size/">
         ← Block Home
      </a>

      <a class="btn btn-outline"
         href="/inference/power-sample-size/effect-size-and-practical-importance/">
         Next: Effect Size and Practical Importance →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>Why Power Matters</h2>

    <p>
      Imagine a new medical treatment genuinely improves patient outcomes.
    </p>

    <p>
      A study is conducted, but the results are not statistically significant.
    </p>

    <p>
      Does this mean the treatment does not work?
    </p>

    <p>
      Not necessarily.
    </p>

    <p>
      The study may simply have lacked enough power to detect the effect.
    </p>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        A non-significant result does not automatically imply that no effect exists.
      </p>

    </div>

    <h2>Review: Type II Errors</h2>

    <p>
      Recall the two major testing mistakes:
    </p>

    <ul class="bullets">

      <li>Type I Error: Rejecting a true null hypothesis</li>

      <li>Type II Error: Failing to reject a false null hypothesis</li>

    </ul>

    <p>
      The probability of a Type II error is denoted by:
    </p>

    0

    <h2>Defining Statistical Power</h2>

    <p>
      Statistical power is the probability of correctly detecting a real effect.
    </p>

    <p>
      Mathematically:
    </p>

    1

    <p>
      where:
    </p>

    <ul class="bullets">

      <li>β = probability of a Type II error</li>

      <li>1 − β = probability of correctly rejecting a false null hypothesis</li>

    </ul>

    <h2>Interpreting Power</h2>

    <p>
      Suppose:
    </p>

    2

    <p>
      This means:
    </p>

    <div class="example-box">

      <p>
        If the effect truly exists, the study will detect it about 80% of the time.
      </p>
    </div>

    <p>
      The remaining 20% corresponds to Type II errors.
    </p>

    <h2>Visualizing the Idea</h2>

    <p>
      Consider two situations:
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Reality</th>
            <th>Decision</th>
            <th>Outcome</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Effect Exists</td>
            <td>Reject H₀</td>
            <td>Correct Detection</td>
          </tr>

          <tr>
            <td>Effect Exists</td>
            <td>Fail to Reject H₀</td>
            <td>Type II Error</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      Power measures the probability of the first outcome.
    </p>

    <h2>Why Low Power Is Dangerous</h2>

    <p>
      Low-power studies often fail to detect meaningful effects.
    </p>

    <p>
      This can lead researchers to conclude:
    </p>

    <div class="example-box">

      <p>
        "There is no effect."
      </p>
    </div>

    <p>
      when an important effect actually exists.
    </p>

    <p>
      Such conclusions can influence policy decisions, medical treatments, and scientific understanding.
    </p>

    <h2>Common Power Targets</h2>

    <p>
      Researchers often choose a target power before collecting data.
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Power</th>
            <th>Interpretation</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>0.80</td>
            <td>Common minimum standard</td>
          </tr>

          <tr>
            <td>0.90</td>
            <td>Stronger ability to detect effects</td>
          </tr>

          <tr>
            <td>0.95</td>
            <td>Very high detection probability</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>Power and Hypothesis Testing</h2>

    <p>
      Traditional hypothesis testing focuses heavily on:
    </p>

    3

    <p>
      which controls Type I errors.
    </p>

    <p>
      Power focuses on the other side of the problem:
    </p>

    4

    <p>
      and the ability to detect real effects.
    </p>

    <div class="concept-box">

      <strong>Important perspective:</strong>

      <p>
        Good study design balances protection against false positives and false negatives.
      </p>

    </div>

    <h2>Power Depends on Several Factors</h2>

    <p>
      Statistical power is not fixed.
    </p>

    <p>
      It depends on:
    </p>

    <ul class="bullets">

      <li>Effect size</li>

      <li>Sample size</li>

      <li>Significance level</li>

      <li>Data variability</li>

      <li>Study design</li>

    </ul>

    <p>
      The remainder of this block explores each of these factors.
    </p>

    <h2>A Thought Experiment</h2>

    <p>
      Suppose two studies investigate the same treatment effect.
    </p>

    <div class="example-box">

      <p>
        Study A: 20 participants
      </p>

      <p>
        Study B: 2,000 participants
      </p>

    </div>

    <p>
      Which study is more likely to detect the effect?
    </p>

    <p>
      Usually Study B.
    </p>

    <p>
      Larger samples generally increase power.
    </p>

    <h2>Power and Evidence</h2>

    <p>
      High power does not guarantee significance.
    </p>

    <p>
      Low power does not guarantee non-significance.
    </p>

    <p>
      Instead, power describes long-run performance across repeated studies.
    </p>

    <h2>Planning Before Data Collection</h2>

    <p>
      One of the most important uses of power is study planning.
    </p>

    <p>
      Researchers often ask:
    </p>

    <div class="example-box">

      <p>
        How many observations are needed to reliably detect an important effect?
      </p>
    </div>

    <p>
      This question leads directly to sample-size determination.
    </p>

    <h2>Power and Scientific Reproducibility</h2>

    <p>
      Low-powered studies contribute to replication problems because genuine effects may frequently be missed.
    </p>

    <p>
      Well-powered studies produce more reliable and stable conclusions.
    </p>

    <h2>The Bigger Picture</h2>

    <p>
      Hypothesis testing asks whether evidence is strong enough to reject a null hypothesis.
    </p>

    <p>
      Statistical power asks whether the study is capable of finding an effect if one truly exists.
    </p>

    <p>
      Both perspectives are necessary for responsible statistical inference.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        Statistical power is the probability of detecting a real effect. It equals 1 − β, where β is the probability of a Type II error. High power makes meaningful effects easier to detect and helps ensure that studies provide informative results.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      Power depends heavily on the size of the effect being studied.
    </p>

    <p>
      Some effects are so small that enormous samples are needed to detect them, while larger effects can be detected with much smaller studies.
    </p>

    <p>
      The next lesson introduces effect size and explains why statistical significance alone is not enough for evaluating practical importance.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Statistical power is the probability of detecting a real effect</li>

        <li>Power equals 1 − β</li>

        <li>β represents the probability of a Type II error</li>

        <li>Low power increases the chance of missing meaningful effects</li>

        <li>Common target power levels are 0.80 and 0.90</li>

        <li>Power depends on effect size, sample size, significance level, and variability</li>

        <li>Power is a key component of study design</li>

        <li>Well-powered studies produce more reliable scientific conclusions</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/inference/power-sample-size/">
         ← Back to Block Home
      </a>

      <a class="btn"
         href="/inference/power-sample-size/effect-size-and-practical-importance/">
         Next: Effect Size and Practical Importance →
      </a>

    </div>

  </div>

</section>