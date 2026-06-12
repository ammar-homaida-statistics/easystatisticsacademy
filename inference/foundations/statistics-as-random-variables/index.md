---
layout: default
title: Statistics as Random Variables
description: Learn why statistics are random variables and why this idea is the foundation of statistical inference.
permalink: /inference/foundations/statistics-as-random-variables/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_inference_foundations_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/inference/foundations/statistics-as-random-variables/",
    label: "Statistics as Random Variables",
    ts: Date.now()
  }));

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Inference</span>
      <span class="badge">Block 1</span>
      <span class="badge">Foundations</span>
      <span class="badge">Core Theory</span>
    </div>

    <h1>Statistics as Random Variables</h1>

    <p class="lead">
      Population parameters are fixed but unknown.
    </p>

    <p class="lead">
      Statistics are calculated from samples, and because samples vary, statistics vary as well. This makes statistics random variables and creates the uncertainty that statistical inference seeks to understand.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/inference/foundations/populations-parameters-target/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/inference/foundations/estimators-vs-estimates/">
         Next: Estimators vs Estimates →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>A Common Misunderstanding</h2>

    <p>
      Many beginners view statistics as fixed numbers.
    </p>

    <p>
      After all, once a sample is collected,
      the sample mean appears to be a single value.
    </p>

    <div class="example-box">

      <p>
        Sample mean = 52.4
      </p>

      <p>
        Sample proportion = 0.61
      </p>

    </div>

    <p>
      However,
      before the sample was collected,
      those values were unknown.
    </p>

    <p>
      Different samples could have produced different results.
    </p>

    <h2>Where Randomness Comes From</h2>

    <p>
      The randomness does not come from the formula.
    </p>

    <p>
      It comes from the sample selection process.
    </p>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        If samples are random, then statistics computed from those samples are random as well.
      </p>

    </div>

    <h2>What Is a Random Variable?</h2>

    <p>
      A random variable is a quantity whose value depends on the outcome of a random process.
    </p>

    <p>
      Since samples are random,
      statistics calculated from samples are random variables.
    </p>

    <h2>A Simple Example</h2>

    <p>
      Suppose a population has an unknown mean:
    </p>

    <p>
      μ = 50
    </p>

    <p>
      Draw a random sample and calculate:
    </p>

    0

    <p>
      One sample may produce:
    </p>

    <div class="example-box">

      <p>
        x̄ = 48
      </p>

    </div>

    <p>
      Another sample may produce:
    </p>

    <div class="example-box">

      <p>
        x̄ = 53
      </p>

    </div>

    <p>
      Another may produce:
    </p>

    <div class="example-box">

      <p>
        x̄ = 50
      </p>

    </div>

    <p>
      The sample mean changes because the sample changes.
    </p>

    <h2>The Sample Mean Is Random</h2>

    <p>
      Before observing the sample,
      the sample mean could take many possible values.
    </p>

    <p>
      Therefore:
    </p>

    1

    <p>
      is a random variable.
    </p>

    <h2>Other Statistics Are Random Too</h2>

    <p>
      The same logic applies to many common statistics.
    </p>

    <ul class="bullets">

      <li>Sample mean</li>

      <li>Sample proportion</li>

      <li>Sample variance</li>

      <li>Sample standard deviation</li>

      <li>Regression coefficients</li>

    </ul>

    <p>
      All vary from sample to sample.
    </p>

    <h2>Parameters vs Statistics</h2>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Parameter</th>
            <th>Statistic</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>Fixed</td>
            <td>Random</td>
          </tr>

          <tr>
            <td>Population quantity</td>
            <td>Sample quantity</td>
          </tr>

          <tr>
            <td>Unknown</td>
            <td>Observed after sampling</td>
          </tr>

        </tbody>

      </table>

    </div>

    <div class="concept-box">

      <strong>Important distinction:</strong>

      <p>
        Parameters do not vary from sample to sample. Statistics do.
      </p>

    </div>

    <h2>The Distribution of a Statistic</h2>

    <p>
      Because statistics are random variables,
      they have probability distributions.
    </p>

    <p>
      These are called sampling distributions.
    </p>

    <p>
      For example,
      the sample mean has its own distribution across repeated samples.
    </p>

    <h2>Why Sampling Distributions Matter</h2>

    <p>
      Sampling distributions tell us:
    </p>

    <ul class="bullets">

      <li>Expected values</li>

      <li>Typical variability</li>

      <li>Unusual outcomes</li>

      <li>Precision of estimates</li>

    </ul>

    <p>
      They form the mathematical basis of inference.
    </p>

    <h2>Expected Value of a Statistic</h2>

    <p>
      Since statistics are random variables,
      they have expected values.
    </p>

    <p>
      For the sample mean:
    </p>

    2

    <p>
      The sample mean is centered on the population mean.
    </p>

    <h2>Variability of a Statistic</h2>

    <p>
      Random variables also have variance.
    </p>

    <p>
      For the sample mean:
    </p>

    3

    <p>
      This tells us how much sample means fluctuate across repeated samples.
    </p>

    <h2>The Source of Inferential Uncertainty</h2>

    <p>
      Why do confidence intervals exist?
    </p>

    <p>
      Why are hypothesis tests necessary?
    </p>

    <p>
      Because statistics are random.
    </p>

    <p>
      If statistics were fixed,
      there would be no uncertainty to quantify.
    </p>

    <h2>The Inferential Framework</h2>

    <p>
      Statistical inference works because:
    </p>

    <ol>

      <li>Parameters are fixed but unknown.</li>

      <li>Statistics are random.</li>

      <li>Sampling distributions describe that randomness.</li>

      <li>Probability theory quantifies uncertainty.</li>

    </ol>

    <p>
      This framework underlies all inferential procedures.
    </p>

    <h2>A Useful Thought Experiment</h2>

    <p>
      Imagine collecting thousands of independent samples from the same population.
    </p>

    <p>
      Each sample produces a different statistic.
    </p>

    <p>
      The collection of those statistics forms a sampling distribution.
    </p>

    <p>
      Statistical inference studies that distribution.
    </p>

    <h2>Observed Value vs Random Variable</h2>

    <p>
      Before sampling:
    </p>

    <div class="example-box">

      <p>
        x̄ is random.
      </p>

    </div>

    <p>
      After sampling:
    </p>

    <div class="example-box">

      <p>
        x̄ = 52.4 (observed value)
      </p>

    </div>

    <p>
      The random variable becomes a realized outcome.
    </p>

    <h2>Why This Idea Is So Important</h2>

    <p>
      Much of statistical theory can be summarized as studying the behavior of random statistics.
    </p>

    <p>
      Confidence intervals,
      p-values,
      standard errors,
      and hypothesis tests all depend on this concept.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        Statistical inference is possible because statistics behave as random variables with predictable probability distributions.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      Statistics are random variables,
      but not every statistic serves the same purpose.
    </p>

    <p>
      Some statistics are specifically designed to estimate population parameters.
    </p>

    <p>
      The next lesson introduces estimators and explains the important distinction between estimators and estimates.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Statistics are random variables because samples are random</li>

        <li>Different samples produce different statistic values</li>

        <li>Parameters are fixed but unknown</li>

        <li>Statistics vary from sample to sample</li>

        <li>Random statistics have sampling distributions</li>

        <li>Expected values and variances can be defined for statistics</li>

        <li>Sampling variability creates inferential uncertainty</li>

        <li>Statistical inference studies the behavior of random statistics</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/inference/foundations/populations-parameters-target/">
         ← Previous: Populations, Parameters, and Targets
      </a>

      <a class="btn"
         href="/inference/foundations/estimators-vs-estimates/">
         Next: Estimators vs Estimates →
      </a>

    </div>

  </div>

</section>