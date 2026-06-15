---
layout: default
title: Underpowered Studies
description: Learn what underpowered studies are, why they are problematic, and how insufficient power can lead to unreliable scientific conclusions.
permalink: /inference/power-sample-size/underpowered-studies/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_inference_power_sample_size_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/inference/power-sample-size/underpowered-studies/",
    label: "Underpowered Studies",
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
      <span class="badge">Study Quality</span>
    </div>

    <h1>Underpowered Studies</h1>

    <p class="lead">
      A study can be perfectly designed, carefully executed, and analyzed correctly yet still fail to answer its research question.
    </p>

    <p class="lead">
      One of the most common reasons is insufficient statistical power.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/inference/power-sample-size/precision-vs-detectability/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/inference/power-sample-size/software-and-power-analysis/">
         Next: Software and Power Analysis →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>What Does Underpowered Mean?</h2>

    <p>
      A study is underpowered when it has a low probability of detecting a meaningful effect that truly exists.
    </p>

    <p>
      In other words:
    </p>

    <div class="example-box">

      <p>
        The study is too weak to reliably answer its research question.
      </p>
    </div>

    <p>
      Even genuine effects may go unnoticed.
    </p>

    <h2>Review: Statistical Power</h2>

    <p>
      Recall that power is:
    </p>

    0

    <p>
      where:
    </p>

    <ul class="bullets">

      <li>β is the probability of a Type II error</li>

      <li>Power is the probability of detecting a true effect</li>

    </ul>

    <p>
      Low power means a larger chance of missing real effects.
    </p>

    <h2>What Counts as Low Power?</h2>

    <p>
      There is no universal threshold, but many fields consider:
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
            <td>0.50</td>
            <td>Very low</td>
          </tr>

          <tr>
            <td>0.60</td>
            <td>Low</td>
          </tr>

          <tr>
            <td>0.80</td>
            <td>Common target</td>
          </tr>

          <tr>
            <td>0.90</td>
            <td>Strong design</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      A study with 50% power misses true effects about half the time.
    </p>

    <h2>The Most Obvious Consequence</h2>

    <p>
      Underpowered studies produce more:
    </p>

    <div class="example-box">

      <p>
        Type II Errors
      </p>
    </div>

    <p>
      Real effects may exist, but the study fails to detect them.
    </p>

    <h2>A Clinical Trial Example</h2>

    <p>
      Suppose a new treatment genuinely improves patient outcomes.
    </p>

    <p>
      A small study enrolls only a few participants.
    </p>

    <p>
      The resulting p-value is not statistically significant.
    </p>

    <p>
      Researchers may conclude:
    </p>

    <div class="example-box">

      <p>
        "The treatment does not work."
      </p>
    </div>

    <p>
      Yet the real problem may simply be insufficient power.
    </p>

    <h2>Absence of Evidence vs Evidence of Absence</h2>

    <div class="concept-box">

      <strong>Critical distinction:</strong>

      <p>
        Failing to find evidence of an effect is not the same as proving that no effect exists.
      </p>

    </div>

    <p>
      This distinction becomes especially important when studies are underpowered.
    </p>

    <h2>Low Power Creates Uncertainty</h2>

    <p>
      In low-power studies:
    </p>

    <ul class="bullets">

      <li>Confidence intervals tend to be wide</li>

      <li>Estimates are less stable</li>

      <li>Results vary substantially across samples</li>

      <li>Conclusions become less reliable</li>

    </ul>

    <h2>Small Samples Are a Common Cause</h2>

    <p>
      One of the most common reasons for low power is:
    </p>

    <div class="example-box">

      <p>
        Insufficient sample size
      </p>
    </div>

    <p>
      Small samples contain less information and produce larger standard errors.
    </p>

    <h2>The Signal-to-Noise Problem</h2>

    <p>
      Statistical inference often involves separating:
    </p>

    <ul class="bullets">

      <li>Signal (real effect)</li>

      <li>Noise (random variation)</li>

    </ul>

    <p>
      Underpowered studies struggle because the signal is difficult to distinguish from the noise.
    </p>

    <h2>Effect Size Matters Too</h2>

    <p>
      Studies can become underpowered even with moderate sample sizes if the target effect is very small.
    </p>

    <p>
      Smaller effects require more data to detect reliably.
    </p>

    <div class="concept-box">

      <strong>General rule:</strong>

      <p>
        The smaller the effect being studied, the larger the required sample size.
      </p>

    </div>

    <h2>The Replication Problem</h2>

    <p>
      Low-powered studies contribute to replication difficulties.
    </p>

    <p>
      Because estimates vary greatly from sample to sample:
    </p>

    <ul class="bullets">

      <li>One study may find significance</li>

      <li>A later study may not</li>

      <li>Results appear inconsistent</li>

    </ul>

    <p>
      This has been a major concern in many scientific fields.
    </p>

    <h2>Unstable Effect Estimates</h2>

    <p>
      Underpowered studies do not merely miss effects.
    </p>

    <p>
      They also tend to produce highly variable estimates.
    </p>

    <p>
      Observed effect sizes may fluctuate substantially across repeated samples.
    </p>

    <h2>Publication Bias and Power</h2>

    <p>
      Scientific journals often favor statistically significant results.
    </p>

    <p>
      In low-power environments:
    </p>

    <ul class="bullets">

      <li>Many studies fail to find significance</li>

      <li>Only a subset gets published</li>

      <li>Published effects may appear larger than reality</li>

    </ul>

    <p>
      This can distort the scientific literature.
    </p>

    <h2>A Visual Intuition</h2>

    <p>
      Consider two studies investigating the same effect.
    </p>

    

    <p>
      The larger study has a much greater chance of discovering the true effect.
    </p>

    <h2>Why Researchers Perform Power Analysis</h2>

    <p>
      Power analysis is intended to prevent underpowered studies before data collection begins.
    </p>

    <p>
      Researchers estimate:
    </p>

    <ul class="bullets">

      <li>Target effect size</li>

      <li>Desired power</li>

      <li>Significance level</li>

      <li>Required sample size</li>

    </ul>

    <p>
      This planning step helps ensure that the study can answer its intended question.
    </p>

    <h2>Resource Constraints</h2>

    <p>
      Unfortunately, ideal sample sizes are not always feasible.
    </p>

    <p>
      Researchers may face:
    </p>

    <ul class="bullets">

      <li>Limited funding</li>

      <li>Limited participant availability</li>

      <li>Time restrictions</li>

      <li>Ethical constraints</li>

    </ul>

    <p>
      These limitations often create difficult design decisions.
    </p>

    <h2>Interpreting Non-Significant Results Carefully</h2>

    <p>
      When a study reports a non-significant result, it is useful to ask:
    </p>

    <div class="example-box">

      <p>
        Did the study have enough power to detect a meaningful effect?
      </p>
    </div>

    <p>
      Without that information, interpreting the result can be difficult.
    </p>

    <h2>Modern Reporting Practices</h2>

    <p>
      Increasingly, researchers report:
    </p>

    <ul class="bullets">

      <li>Power analyses</li>

      <li>Confidence intervals</li>

      <li>Effect sizes</li>

      <li>Sample-size justifications</li>

    </ul>

    <p>
      These details help readers evaluate the strength of the evidence.
    </p>

    <h2>The Bigger Picture</h2>

    <p>
      Statistical significance alone does not guarantee a useful study.
    </p>

    <p>
      A study must also have sufficient power to detect effects that matter.
    </p>

    <p>
      Underpowered studies can miss important discoveries, produce unstable results, and contribute to misleading scientific conclusions.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        Underpowered studies have a low probability of detecting real effects. They increase the risk of Type II errors, produce less reliable estimates, and can lead researchers to overlook meaningful findings.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      Power analysis has become a standard component of modern statistical practice.
    </p>

    <p>
      Researchers routinely use software tools to estimate power, calculate required sample sizes, and evaluate alternative study designs.
    </p>

    <p>
      The next lesson introduces common software tools and practical workflows used for power analysis.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Underpowered studies have a low probability of detecting real effects</li>

        <li>Low power increases the risk of Type II errors</li>

        <li>Non-significant results do not necessarily imply no effect exists</li>

        <li>Small sample sizes are a common cause of underpowered studies</li>

        <li>Smaller effects require larger samples to detect</li>

        <li>Low-powered studies often produce unstable estimates</li>

        <li>Underpowered research contributes to replication problems</li>

        <li>Power analysis helps prevent these issues during study planning</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/inference/power-sample-size/precision-vs-detectability/">
         ← Previous: Precision vs Detectability
      </a>

      <a class="btn"
         href="/inference/power-sample-size/software-and-power-analysis/">
         Next: Software and Power Analysis →
      </a>

    </div>

  </div>

</section>