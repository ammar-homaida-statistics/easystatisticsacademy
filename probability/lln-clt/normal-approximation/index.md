---
layout: default
title: Normal Approximation
description: Learn how the Central Limit Theorem allows normal distributions to approximate many probability distributions in practice.
permalink: /probability/lln-clt/normal-approximation/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_probability_lln_clt_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/probability/lln-clt/normal-approximation/",
    label: "Normal Approximation",
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
      <span class="badge">Applications</span>
    </div>

    <h1>Normal Approximation</h1>

    <p class="lead">
      The Central Limit Theorem is powerful because it allows complicated probability distributions to be approximated by a normal distribution.
    </p>

    <p class="lead">
      This idea makes many probability and statistical calculations far simpler and forms the practical bridge between probability theory and statistical inference.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/probability/lln-clt/central-limit-theorem/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/probability/lln-clt/inference-bridge/">
         Next: Inference Bridge →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>What Is Normal Approximation?</h2>

    <p>
      Normal approximation means replacing a complicated distribution with a normal distribution that behaves similarly.
    </p>

    <div class="concept-box">

      <strong>Core idea:</strong>

      <p>
        When sample sizes are sufficiently large, many statistics can be treated as approximately normal.
      </p>

    </div>

    <h2>Why Approximate?</h2>

    <p>
      Exact probability calculations are often difficult.
    </p>

    <div class="example-box">

      <p>
        Large binomial distributions
      </p>

      <p>
        Sample means from unknown populations
      </p>

      <p>
        Complex counting processes
      </p>

    </div>

    <p>
      The normal distribution provides a convenient approximation that is often remarkably accurate.
    </p>

    <h2>The Role of the Central Limit Theorem</h2>

    <p>
      The Central Limit Theorem tells us that sample means tend toward a normal distribution.
    </p>

    <p>
      Specifically:
    </p>

    0

    <p>
      when the sample size is sufficiently large.
    </p>

    <p>
      This approximation becomes better as sample size increases.
    </p>

    <h2>Approximating Sample Means</h2>

    <p>
      Suppose a population has:
    </p>

    <div class="example-box">

      <p>
        Mean = μ
      </p>

      <p>
        Standard deviation = σ
      </p>

    </div>

    <p>
      Then for large n:
    </p>

    1

    <p>
      approximately.
    </p>

    <p>
      This allows probability calculations using the normal curve.
    </p>

    <h2>The Standard Error</h2>

    <p>
      The standard deviation of the sampling distribution is:
    </p>

    2

    <p>
      called the standard error.
    </p>

    <p>
      Standard error determines the spread of sample means.
    </p>

    <h2>Using Z-Scores</h2>

    <p>
      Once a normal approximation is available,
      probabilities can be calculated using standardized values.
    </p>

    3

    <p>
      This converts sample means into standard normal values.
    </p>

    <h2>Example: Average Heights</h2>

    <p>
      Suppose a population has:
    </p>

    <div class="example-box">

      <p>
        μ = 170 cm
      </p>

      <p>
        σ = 12 cm
      </p>

      <p>
        n = 100
      </p>

    </div>

    <p>
      Then:
    </p>

    4

    <p>
      The distribution of sample means is much narrower than the original population distribution.
    </p>

    <h2>Why Sample Means Are Less Variable</h2>

    <p>
      Individual observations vary considerably.
    </p>

    <p>
      Averages smooth out random fluctuations.
    </p>

    <p>
      As sample size increases,
      the sampling distribution becomes increasingly concentrated around the population mean.
    </p>

    <h2>Normal Approximation for Proportions</h2>

    <p>
      The CLT also applies to sample proportions.
    </p>

    <p>
      If:
    </p>

    5

    <p>
      is the true population proportion,
      then:
    </p>

    6

    <p>
      for sufficiently large sample sizes.
    </p>

    <h2>Example: Survey Results</h2>

    <p>
      Suppose:
    </p>

    <div class="example-box">

      <p>
        True support = 60%
      </p>

      <p>
        Sample size = 400
      </p>

    </div>

    <p>
      The sample proportion varies from sample to sample,
      but its distribution is approximately normal.
    </p>

    <p>
      This fact underlies opinion polling.
    </p>

    <h2>Normal Approximation to the Binomial</h2>

    <p>
      Large binomial distributions can often be approximated by a normal distribution.
    </p>

    <p>
      If:
    </p>

    7

    <p>
      then for sufficiently large n:
    </p>

    8

    <p>
      This approximation simplifies probability calculations substantially.
    </p>

    <h2>The Continuity Correction</h2>

    <p>
      Binomial distributions are discrete,
      while normal distributions are continuous.
    </p>

    <p>
      To improve accuracy,
      statisticians often use a continuity correction.
    </p>

    <div class="example-box">

      <p>
        Replace 10 with 10.5
      </p>

      <p>
        Replace 20 with 19.5
      </p>

    </div>

    <p>
      This adjustment helps align discrete and continuous probabilities.
    </p>

    <h2>When Normal Approximation Works Well</h2>

    <ul class="bullets">

      <li>Large sample sizes</li>

      <li>Independent observations</li>

      <li>Moderate skewness</li>

      <li>Finite variance</li>

    </ul>

    <p>
      Under these conditions,
      approximations are often extremely accurate.
    </p>

    <h2>When Caution Is Needed</h2>

    <ul class="bullets">

      <li>Very small samples</li>

      <li>Extreme skewness</li>

      <li>Heavy-tailed populations</li>

      <li>Strong dependence</li>

    </ul>

    <p>
      In such situations,
      the normal approximation may be poor.
    </p>

    <h2>Why Normal Approximation Changed Statistics</h2>

    <p>
      Before modern computers,
      exact probability calculations were often impractical.
    </p>

    <p>
      Normal approximations allowed statisticians to solve complex problems using tables and relatively simple mathematics.
    </p>

    <p>
      Even today,
      normal approximations remain fundamental.
    </p>

    <h2>Connection to Statistical Inference</h2>

    <p>
      Most inferential methods rely on normal approximations.
    </p>

    <ul class="bullets">

      <li>Confidence intervals</li>

      <li>Hypothesis tests</li>

      <li>Margin of error calculations</li>

      <li>Regression inference</li>

    </ul>

    <p>
      Without normal approximation,
      many standard statistical procedures would not exist.
    </p>

    <h2>The Bridge to Inference</h2>

    <p>
      The Central Limit Theorem provides a probability model for sample means and proportions.
    </p>

    <p>
      Once we know how sample statistics behave,
      we can begin making statements about unknown population parameters.
    </p>

    <p>
      This transition marks the beginning of statistical inference.
    </p>

    <h2>Looking Ahead</h2>

    <p>
      The next lesson connects probability theory to inferential statistics.
    </p>

    <p>
      It explains how the Law of Large Numbers and Central Limit Theorem provide the foundation for estimation, confidence intervals, and hypothesis testing.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Normal approximation replaces complex distributions with normal distributions</li>

        <li>The Central Limit Theorem justifies many normal approximations</li>

        <li>Sample means are approximately normal for large samples</li>

        <li>The standard error equals σ/√n</li>

        <li>Sample proportions are also approximately normal under suitable conditions</li>

        <li>Large binomial distributions can often be approximated by normal distributions</li>

        <li>Normal approximation underlies many statistical procedures</li>

        <li>It provides the bridge from probability to inference</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/probability/lln-clt/central-limit-theorem/">
         ← Previous: Central Limit Theorem
      </a>

      <a class="btn"
         href="/probability/lln-clt/inference-bridge/">
         Next: Inference Bridge →
      </a>

    </div>

  </div>

</section>