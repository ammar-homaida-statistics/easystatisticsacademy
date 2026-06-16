---
layout: default
title: Lognormal Distribution
description: Learn how the lognormal distribution models positive, right-skewed variables and why it appears frequently in economics, finance, biology, and data science.
permalink: /probability/distributions/lognormal-distribution/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_probability_distributions_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/probability/distributions/lognormal-distribution/",
    label: "Lognormal Distribution",
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

    <h1>Lognormal Distribution</h1>

    <p class="lead">
      Many real-world variables are positive, highly right-skewed, and cannot take negative values.
    </p>

    <p class="lead">
      The lognormal distribution provides a natural model for such quantities and appears throughout finance, biology, economics, engineering, and data science.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/probability/distributions/normal-distribution/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/probability/lln-clt/">
         Next: LLN & CLT →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>What Is a Lognormal Distribution?</h2>

    <p>
      A random variable follows a lognormal distribution when its logarithm follows a normal distribution.
    </p>

    <div class="concept-box">

      <strong>Definition:</strong>

      <p>
        A variable X is lognormally distributed if ln(X) follows a normal distribution.
      </p>

    </div>

    <h2>The Core Idea</h2>

    <p>
      Instead of modeling X directly,
      we model its logarithm.
    </p>

    <p>
      If:
    </p>

    0

    <p>
      then:
    </p>

    <div class="example-box">

      <p>
        X follows a lognormal distribution.
      </p>

    </div>

    <h2>Why Logarithms Matter</h2>

    <p>
      Many processes grow multiplicatively rather than additively.
    </p>

    <div class="example-box">

      <p>
        Investment growth
      </p>

      <p>
        Population growth
      </p>

      <p>
        Company revenue growth
      </p>

      <p>
        Biological growth
      </p>

    </div>

    <p>
      Repeated multiplication naturally leads to lognormal behavior.
    </p>

    <h2>Examples of Lognormal Variables</h2>

    <ul class="bullets">

      <li>Personal income</li>

      <li>Stock prices</li>

      <li>Company sizes</li>

      <li>House prices</li>

      <li>Biological concentrations</li>

      <li>Internet traffic volumes</li>

      <li>Insurance claim amounts</li>

    </ul>

    <p>
      These variables are positive and often strongly right-skewed.
    </p>

    <h2>Notation</h2>

    <p>
      A lognormal random variable is often written as:
    </p>

    <div class="example-box">

      <p>
        X ~ Lognormal(μ, σ²)
      </p>

    </div>

    <p>
      The parameters μ and σ describe the normal distribution of ln(X), not X itself.
    </p>

    <h2>The Probability Density Function</h2>

    <p>
      The lognormal density is:
    </p>

    1

    <p>
      for:
    </p>

    2

    <p>
      and zero otherwise.
    </p>

    <h2>Key Characteristics</h2>

    <ul class="bullets">

      <li>Only positive values are possible.</li>

      <li>Strong right skewness is common.</li>

      <li>Large values occur occasionally.</li>

      <li>The distribution is asymmetric.</li>

    </ul>

    <h2>The Shape</h2>

    <p>
      A lognormal distribution typically has:
    </p>

    <div class="example-box">

      <p>
        A peak near smaller values
      </p>

      <p>
        A long right tail
      </p>

      <p>
        No negative values
      </p>

    </div>

    <p>
      This shape often resembles real-world financial and economic data.
    </p>

    <h2>Mean, Median, and Mode</h2>

    <p>
      Unlike the normal distribution,
      these measures are not equal.
    </p>

    <div class="concept-box">

      <strong>Ordering:</strong>

      <p>
        Mode &lt; Median &lt; Mean
      </p>

    </div>

    <p>
      The right tail pulls the mean upward.
    </p>

    <h2>The Median</h2>

    <p>
      The median of a lognormal distribution is:
    </p>

    3

    <p>
      Half the observations lie below this value.
    </p>

    <h2>The Mean</h2>

    <p>
      The expected value is:
    </p>

    4

    <p>
      Notice that the mean exceeds the median whenever:
    </p>

    5

    <h2>The Variance</h2>

    <p>
      The variance is:
    </p>

    6

    <p>
      Larger σ values create dramatically larger variability.
    </p>

    <h2>Why Log Transformation Is Useful</h2>

    <p>
      Many skewed datasets become approximately normal after taking logarithms.
    </p>

    <div class="example-box">

      <p>
        Income data
      </p>

      <p>
        Sales revenue
      </p>

      <p>
        Biological measurements
      </p>

      <p>
        Financial quantities
      </p>

    </div>

    <p>
      This transformation often simplifies statistical analysis.
    </p>

    <h2>Normal Versus Lognormal</h2>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Feature</th>
            <th>Normal</th>
            <th>Lognormal</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>Support</td>
            <td>All real numbers</td>
            <td>Positive values only</td>
          </tr>

          <tr>
            <td>Symmetry</td>
            <td>Symmetric</td>
            <td>Right-skewed</td>
          </tr>

          <tr>
            <td>Mean = Median?</td>
            <td>Yes</td>
            <td>No</td>
          </tr>

          <tr>
            <td>Negative Values Possible?</td>
            <td>Yes</td>
            <td>No</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>Applications in Finance</h2>

    <p>
      Financial analysts frequently use lognormal models because prices and values cannot fall below zero.
    </p>

    <ul class="bullets">

      <li>Stock prices</li>

      <li>Asset values</li>

      <li>Investment growth</li>

      <li>Risk modeling</li>

    </ul>

    <p>
      Many classical financial models assume lognormal behavior.
    </p>

    <h2>Applications in Science and Engineering</h2>

    <ul class="bullets">

      <li>Particle sizes</li>

      <li>Environmental concentrations</li>

      <li>Biological growth processes</li>

      <li>Reliability measurements</li>

    </ul>

    <p>
      Lognormal distributions appear whenever growth occurs through repeated multiplicative effects.
    </p>

    <h2>Why the Lognormal Distribution Matters</h2>

    <p>
      Many datasets encountered in practice are positive and skewed.
    </p>

    <p>
      The lognormal distribution often provides a much better description than the normal distribution.
    </p>

    <p>
      Understanding lognormal behavior is particularly important in finance, economics, and applied data science.
    </p>

    <h2>From Individual Distributions to Fundamental Theorems</h2>

    <p>
      We have now studied many of the most important probability distributions.
    </p>

    <p>
      The next block introduces two foundational results that explain why probability and statistics work so well:
    </p>

    <div class="example-box">

      <p>
        Law of Large Numbers (LLN)
      </p>

      <p>
        Central Limit Theorem (CLT)
      </p>

    </div>

    <p>
      These theorems connect probability theory to statistical inference and data analysis.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>A lognormal variable has a normally distributed logarithm</li>

        <li>Lognormal distributions are positive and right-skewed</li>

        <li>They naturally model multiplicative growth processes</li>

        <li>Mean, median, and mode are not equal</li>

        <li>The median equals e<sup>μ</sup></li>

        <li>The mean equals e<sup>μ + σ²/2</sup></li>

        <li>Log transformations often make skewed data approximately normal</li>

        <li>Lognormal models are widely used in finance, economics, biology, and engineering</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/probability/distributions/normal-distribution/">
         ← Previous: Normal Distribution
      </a>

      <a class="btn"
         href="/probability/lln-clt/">
         Next: LLN & CLT →
      </a>

    </div>

  </div>

</section>