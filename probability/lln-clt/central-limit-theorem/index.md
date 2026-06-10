---
layout: default
title: Central Limit Theorem
description: Learn the Central Limit Theorem and understand why normal distributions appear throughout statistics.
permalink: /probability/lln-clt/central-limit-theorem/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_probability_lln_clt_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/probability/lln-clt/central-limit-theorem/",
    label: "Central Limit Theorem",
    ts: Date.now()
  }));

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Probability</span>
      <span class="badge">Block 6</span>
      <span class="badge">LLN & CLT</span>
      <span class="badge">Core Theorem</span>
    </div>

    <h1>Central Limit Theorem</h1>

    <p class="lead">
      The Law of Large Numbers explains why averages become stable.
    </p>

    <p class="lead">
      The Central Limit Theorem explains the distribution of those averages and why normal distributions appear everywhere in statistics.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/probability/lln-clt/weak-vs-strong-lln/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/probability/lln-clt/normal-approximation/">
         Next: Normal Approximation →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>Why the Central Limit Theorem Matters</h2>

    <p>
      The Central Limit Theorem (CLT) is one of the most important results in all of mathematics and statistics.
    </p>

    <p>
      It explains why normal distributions appear so frequently,
      even when the original data are not normally distributed.
    </p>

    <div class="concept-box">

      <strong>Big idea:</strong>

      <p>
        Averages of many independent observations tend to have an approximately normal distribution.
      </p>

    </div>

    <h2>The Question the CLT Answers</h2>

    <p>
      Suppose a population has an unusual shape.
    </p>

    <div class="example-box">

      <p>
        Strongly skewed
      </p>

      <p>
        Multi-modal
      </p>

      <p>
        Non-normal
      </p>

    </div>

    <p>
      What happens if we repeatedly take samples and compute sample means?
    </p>

    <p>
      The CLT provides the answer.
    </p>

    <h2>The Main Result</h2>

    <p>
      If observations are independent and identically distributed with finite mean and variance,
      then the distribution of sample means becomes approximately normal as sample size grows.
    </p>

    <p>
      Symbolically:
    </p>

    0

    <p>
      for sufficiently large sample sizes.
    </p>

    <h2>What Is Changing?</h2>

    <p>
      The theorem is not describing the original observations.
    </p>

    <p>
      It describes the distribution of sample means.
    </p>

    <div class="concept-box">

      <strong>Important:</strong>

      <p>
        The CLT concerns averages, not individual observations.
      </p>

    </div>

    <h2>A Sampling Thought Experiment</h2>

    <p>
      Imagine a highly skewed population.
    </p>

    <p>
      Repeatedly:
    </p>

    <ul class="bullets">

      <li>Take a random sample</li>

      <li>Compute its mean</li>

      <li>Record the result</li>

    </ul>

    <p>
      After many repetitions,
      we obtain a collection of sample means.
    </p>

    <p>
      The CLT says those means form an approximately normal distribution.
    </p>

    <h2>Why This Is Surprising</h2>

    <p>
      The original population does not need to be normal.
    </p>

    <p>
      It can be:
    </p>

    <ul class="bullets">

      <li>Right-skewed</li>

      <li>Left-skewed</li>

      <li>Irregularly shaped</li>

      <li>Multi-peaked</li>

    </ul>

    <p>
      Yet the sampling distribution of the mean often becomes bell-shaped.
    </p>

    <h2>The Sampling Distribution</h2>

    <p>
      The collection of all possible sample means forms a distribution called the sampling distribution of the mean.
    </p>

    <p>
      The CLT describes the shape of this distribution.
    </p>

    <h2>The Mean of Sample Means</h2>

    <p>
      The center of the sampling distribution equals the population mean.
    </p>

    1

    <p>
      Sample means are centered correctly on average.
    </p>

    <h2>The Variability of Sample Means</h2>

    <p>
      The variance of sample means is:
    </p>

    2

    <p>
      Therefore the standard deviation of sample means is:
    </p>

    3

    <p>
      This quantity is called the standard error.
    </p>

    <h2>Understanding Standard Error</h2>

    <p>
      Standard error measures how much sample means vary from sample to sample.
    </p>

    <p>
      Larger samples reduce standard error.
    </p>

    <div class="example-box">

      <p>
        n = 25 → denominator = 5
      </p>

      <p>
        n = 100 → denominator = 10
      </p>

    </div>

    <p>
      Larger samples produce more precise estimates.
    </p>

    <h2>Visualizing the CLT</h2>

    <p>
      Imagine increasing sample size.
    </p>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Sample Size</th>
            <th>Sampling Distribution</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>n = 1</td>
            <td>Looks like the population</td>
          </tr>

          <tr>
            <td>n = 5</td>
            <td>Less skewed</td>
          </tr>

          <tr>
            <td>n = 30</td>
            <td>Often approximately normal</td>
          </tr>

          <tr>
            <td>n = 100</td>
            <td>Very close to normal</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>The Famous "n = 30" Rule</h2>

    <p>
      Introductory statistics often uses:
    </p>

    <div class="example-box">

      <p>
        n ≥ 30
      </p>

    </div>

    <p>
      as a rough guideline for normal approximation.
    </p>

    <p>
      However,
      the required sample size depends on how non-normal the population is.
    </p>

    <h2>When the CLT Works Well</h2>

    <ul class="bullets">

      <li>Independent observations</li>

      <li>Random sampling</li>

      <li>Finite variance</li>

      <li>Moderate to large sample size</li>

    </ul>

    <p>
      Under these conditions,
      normal approximations are often highly accurate.
    </p>

    <h2>When Caution Is Needed</h2>

    <ul class="bullets">

      <li>Very small samples</li>

      <li>Extremely skewed populations</li>

      <li>Strong dependence between observations</li>

      <li>Heavy-tailed distributions</li>

    </ul>

    <p>
      In such situations,
      convergence may be slower.
    </p>

    <h2>Why the CLT Is So Important</h2>

    <p>
      Most statistical procedures rely on normal approximations.
    </p>

    <ul class="bullets">

      <li>Confidence intervals</li>

      <li>Hypothesis tests</li>

      <li>Regression analysis</li>

      <li>Survey estimation</li>

      <li>Machine learning evaluation</li>

    </ul>

    <p>
      The CLT provides the theoretical justification.
    </p>

    <h2>Connection to the Law of Large Numbers</h2>

    <p>
      The two theorems answer different questions.
    </p>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Theorem</th>
            <th>Main Question</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>Law of Large Numbers</td>
            <td>Do averages approach the true mean?</td>
          </tr>

          <tr>
            <td>Central Limit Theorem</td>
            <td>How are sample means distributed?</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      Together,
      they form the foundation of statistical inference.
    </p>

    <h2>Why It Is Called "Central"</h2>

    <p>
      The theorem is considered central because it connects probability theory,
      sampling,
      estimation,
      and statistical inference.
    </p>

    <p>
      Few results have had a greater impact on modern science.
    </p>

    <h2>Looking Ahead</h2>

    <p>
      The CLT allows us to approximate many distributions using the normal distribution.
    </p>

    <p>
      The next lesson explores normal approximation and shows how the theorem is applied in practical probability calculations.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>The Central Limit Theorem describes the distribution of sample means</li>

        <li>Sample means become approximately normal as sample size increases</li>

        <li>The population itself does not need to be normal</li>

        <li>The mean of the sampling distribution equals μ</li>

        <li>The standard error equals σ/√n</li>

        <li>Larger samples produce more precise estimates</li>

        <li>The CLT provides the foundation for confidence intervals and hypothesis testing</li>

        <li>The CLT is one of the most important results in all of statistics</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/probability/lln-clt/weak-vs-strong-lln/">
         ← Previous: Weak vs Strong LLN
      </a>

      <a class="btn"
         href="/probability/lln-clt/normal-approximation/">
         Next: Normal Approximation →
      </a>

    </div>

  </div>

</section>