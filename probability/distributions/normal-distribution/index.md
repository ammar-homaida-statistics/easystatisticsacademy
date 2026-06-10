---
layout: default
title: Normal Distribution
description: Learn why the normal distribution is the most important distribution in statistics and how it models many natural phenomena.
permalink: /probability/distributions/normal-distribution/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_probability_distributions_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/probability/distributions/normal-distribution/",
    label: "Normal Distribution",
    ts: Date.now()
  }));

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Probability</span>
      <span class="badge">Block 5</span>
      <span class="badge">Distributions</span>
      <span class="badge">Continuous</span>
    </div>

    <h1>Normal Distribution</h1>

    <p class="lead">
      The normal distribution is the most widely used probability distribution in statistics.
    </p>

    <p class="lead">
      Its appearance throughout science, engineering, economics, psychology, and data science makes it one of the most important concepts in quantitative analysis.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/probability/distributions/beta-distribution/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/probability/distributions/lognormal-distribution/">
         Next: Lognormal Distribution →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>What Is a Normal Distribution?</h2>

    <p>
      A normal distribution is a continuous probability distribution with a symmetric bell-shaped curve.
    </p>

    <div class="concept-box">

      <strong>Definition:</strong>

      <p>
        The normal distribution is a continuous distribution characterized by its mean and standard deviation.
      </p>

    </div>

    <h2>Why It Is Famous</h2>

    <p>
      Many natural and human-made measurements approximately follow a normal distribution.
    </p>

    <div class="example-box">

      <p>
        Human heights
      </p>

      <p>
        IQ scores
      </p>

      <p>
        Measurement errors
      </p>

      <p>
        Manufacturing dimensions
      </p>

      <p>
        Test scores
      </p>

    </div>

    <p>
      This widespread appearance makes the normal distribution central to statistics.
    </p>

    <h2>The Bell Curve</h2>

    <p>
      The graph of a normal distribution is commonly called a bell curve.
    </p>

    <p>
      It has several important characteristics:
    </p>

    <ul class="bullets">

      <li>Symmetric around the mean</li>

      <li>Single peak</li>

      <li>Smooth shape</li>

      <li>Tails extend infinitely in both directions</li>

    </ul>

    <h2>The Parameters</h2>

    <p>
      A normal distribution is completely determined by two parameters:
    </p>

    <ul class="bullets">

      <li>μ (mean)</li>

      <li>σ (standard deviation)</li>

    </ul>

    <p>
      The mean controls location.
    </p>

    <p>
      The standard deviation controls spread.
    </p>

    <h2>Notation</h2>

    <p>
      A normal random variable is written as:
    </p>

    <div class="example-box">

      <p>
        X ~ N(μ, σ²)
      </p>

    </div>

    <p>
      The notation uses variance rather than standard deviation.
    </p>

    <h2>The Probability Density Function</h2>

    <p>
      The normal density function is:
    </p>

    0

    <p>
      Although the formula appears complex,
      the distribution has simple and powerful properties.
    </p>

    <h2>Symmetry</h2>

    <p>
      The normal distribution is perfectly symmetric.
    </p>

    <p>
      This implies:
    </p>

    <div class="example-box">

      <p>
        Mean = Median = Mode
      </p>

    </div>

    <p>
      All three measures of center occur at the same location.
    </p>

    <h2>The Role of the Mean</h2>

    <p>
      The mean determines where the bell curve is centered.
    </p>

    <div class="example-box">

      <p>
        Larger μ shifts the curve right.
      </p>

      <p>
        Smaller μ shifts the curve left.
      </p>

    </div>

    <p>
      The overall shape remains unchanged.
    </p>

    <h2>The Role of Standard Deviation</h2>

    <p>
      The standard deviation determines spread.
    </p>

    <div class="example-box">

      <p>
        Small σ → narrow curve
      </p>

      <p>
        Large σ → wider curve
      </p>

    </div>

    <p>
      Greater variability produces a flatter distribution.
    </p>

    <h2>Total Probability Equals One</h2>

    <p>
      As with all probability distributions,
      the total area under the normal curve equals one.
    </p>

    <p>
      Probabilities correspond to areas under the curve.
    </p>

    <h2>The Standard Normal Distribution</h2>

    <p>
      A particularly important normal distribution has:
    </p>

    1

    <p>
      This distribution is called the standard normal distribution.
    </p>

    <h2>The Standard Normal Variable</h2>

    <p>
      A standard normal random variable is often denoted:
    </p>

    <div class="example-box">

      <p>
        Z
      </p>

    </div>

    <p>
      and follows:
    </p>

    <div class="example-box">

      <p>
        Z ~ N(0,1)
      </p>

    </div>

    <h2>Z-Scores</h2>

    <p>
      Any normal observation can be converted into a standard normal value using:
    </p>

    2

    <p>
      This transformation measures how many standard deviations an observation lies from the mean.
    </p>

    <h2>Interpreting Z-Scores</h2>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Z-Score</th>
            <th>Interpretation</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>0</td>
            <td>At the mean</td>
          </tr>

          <tr>
            <td>+1</td>
            <td>One standard deviation above the mean</td>
          </tr>

          <tr>
            <td>-1</td>
            <td>One standard deviation below the mean</td>
          </tr>

          <tr>
            <td>+2</td>
            <td>Two standard deviations above the mean</td>
          </tr>

          <tr>
            <td>-2</td>
            <td>Two standard deviations below the mean</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>The Empirical Rule</h2>

    <p>
      One of the most famous properties of the normal distribution is the 68–95–99.7 Rule.
    </p>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Range</th>
            <th>Approximate Probability</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>μ ± 1σ</td>
            <td>68%</td>
          </tr>

          <tr>
            <td>μ ± 2σ</td>
            <td>95%</td>
          </tr>

          <tr>
            <td>μ ± 3σ</td>
            <td>99.7%</td>
          </tr>

        </tbody>

      </table>

    </div>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        Almost all observations in a normal distribution fall within three standard deviations of the mean.
      </p>

    </div>

    <h2>The Central Limit Theorem</h2>

    <p>
      One reason the normal distribution appears so often is the Central Limit Theorem.
    </p>

    <p>
      This theorem states that averages of many independent observations tend to become approximately normal.
    </p>

    <p>
      Even when the original data are not normally distributed.
    </p>

    <h2>Why This Matters</h2>

    <p>
      The Central Limit Theorem allows statisticians to use normal methods in a wide variety of situations.
    </p>

    <p>
      It forms the foundation of many statistical procedures.
    </p>

    <h2>Applications of the Normal Distribution</h2>

    <ul class="bullets">

      <li>Confidence intervals</li>

      <li>Hypothesis testing</li>

      <li>Quality control</li>

      <li>Measurement systems</li>

      <li>Forecasting</li>

      <li>Machine learning</li>

      <li>Risk analysis</li>

    </ul>

    <p>
      Few distributions are used more extensively.
    </p>

    <h2>When the Normal Distribution Is Not Appropriate</h2>

    <p>
      Some variables cannot be negative.
    </p>

    <div class="example-box">

      <p>
        Income
      </p>

      <p>
        Company size
      </p>

      <p>
        Stock prices
      </p>

      <p>
        Biological concentrations
      </p>

    </div>

    <p>
      These variables are often strongly right-skewed.
    </p>

    <p>
      The normal distribution may not fit them well.
    </p>

    <h2>Why the Normal Distribution Matters</h2>

    <p>
      The normal distribution is often called the "workhorse" of statistics.
    </p>

    <p>
      Its mathematical simplicity,
      widespread applicability,
      and connection to the Central Limit Theorem make it indispensable.
    </p>

    <p>
      A strong understanding of the normal distribution is essential for advanced statistics.
    </p>

    <h2>Looking Ahead</h2>

    <p>
      Many real-world measurements are positive and right-skewed rather than symmetric.
    </p>

    <p>
      The next lesson introduces the lognormal distribution,
      which models positive quantities whose logarithms follow a normal distribution.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>The normal distribution is a symmetric bell-shaped distribution</li>

        <li>It is determined by a mean μ and standard deviation σ</li>

        <li>Mean, median, and mode are equal</li>

        <li>The standard normal distribution has μ = 0 and σ = 1</li>

        <li>Z-scores standardize observations</li>

        <li>The 68–95–99.7 rule summarizes normal probabilities</li>

        <li>The Central Limit Theorem explains the widespread importance of normal distributions</li>

        <li>The normal distribution underlies much of modern statistical inference</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/probability/distributions/beta-distribution/">
         ← Previous: Beta Distribution
      </a>

      <a class="btn"
         href="/probability/distributions/lognormal-distribution/">
         Next: Lognormal Distribution →
      </a>

    </div>

  </div>

</section>