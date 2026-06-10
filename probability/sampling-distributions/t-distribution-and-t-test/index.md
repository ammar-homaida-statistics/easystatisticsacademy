---
layout: default
title: t Distribution and t Test
description: Learn why the t-distribution is needed, how it differs from the normal distribution, and how t-tests are used for inference about means.
permalink: /probability/sampling-distributions/t-distribution-and-t-test/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_probability_sampling_distributions_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/probability/sampling-distributions/t-distribution-and-t-test/",
    label: "t Distribution and t Test",
    ts: Date.now()
  }));

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Probability</span>
      <span class="badge">Block 7</span>
      <span class="badge">Sampling Distributions</span>
      <span class="badge">Inference</span>
    </div>

    <h1>t Distribution and t Test</h1>

    <p class="lead">
      The z-distribution works well when population variability is known.
    </p>

    <p class="lead">
      In practice, population standard deviations are rarely known. The t-distribution provides a solution and forms the basis of one of the most important statistical procedures: the t-test.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/probability/sampling-distributions/z-statistic-and-ci/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/probability/sampling-distributions/chi-square-and-variance/">
         Next: Chi-Square and Variance →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>The Problem with Z Procedures</h2>

    <p>
      Earlier confidence intervals and z-statistics used:
    </p>

    0

    <p>
      where:
    </p>

    <ul class="bullets">

      <li>σ = population standard deviation</li>

    </ul>

    <p>
      The difficulty is that σ is usually unknown.
    </p>

    <p>
      Most real studies only have sample data.
    </p>

    <h2>The Solution</h2>

    <p>
      Instead of using the population standard deviation,
      we estimate it using the sample standard deviation:
    </p>

    1

    <p>
      This replacement introduces additional uncertainty.
    </p>

    <p>
      The t-distribution accounts for that uncertainty.
    </p>

    <h2>What Is the t Distribution?</h2>

    <p>
      The t-distribution is a probability distribution used when population variability is unknown and must be estimated from the sample.
    </p>

    <div class="concept-box">

      <strong>Definition:</strong>

      <p>
        The t-distribution is a family of distributions that resemble the normal distribution but have heavier tails.
      </p>

    </div>

    <h2>Why Heavier Tails?</h2>

    <p>
      Because σ is estimated rather than known,
      estimates are less certain.
    </p>

    <p>
      The t-distribution reflects this extra uncertainty by placing more probability in the tails.
    </p>

    <div class="example-box">

      <p>
        More extreme values become slightly more likely.
      </p>

    </div>

    <h2>Comparing Normal and t Distributions</h2>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Feature</th>
            <th>Normal Distribution</th>
            <th>t Distribution</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>Center</td>
            <td>0</td>
            <td>0</td>
          </tr>

          <tr>
            <td>Symmetry</td>
            <td>Symmetric</td>
            <td>Symmetric</td>
          </tr>

          <tr>
            <td>Tails</td>
            <td>Lighter</td>
            <td>Heavier</td>
          </tr>

          <tr>
            <td>Depends on Sample Size</td>
            <td>No</td>
            <td>Yes</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>Degrees of Freedom</h2>

    <p>
      Every t-distribution is determined by its degrees of freedom.
    </p>

    <p>
      For a one-sample mean:
    </p>

    2

    <p>
      where:
    </p>

    <ul class="bullets">

      <li>n = sample size</li>

    </ul>

    <h2>Effect of Degrees of Freedom</h2>

    <p>
      Small degrees of freedom produce heavier tails.
    </p>

    <p>
      Large degrees of freedom make the t-distribution resemble the normal distribution.
    </p>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        As sample size increases, the t-distribution approaches the standard normal distribution.
      </p>

    </div>

    <h2>The t Statistic</h2>

    <p>
      The t-statistic is calculated similarly to a z-statistic.
    </p>

    <p>
      The difference is that the sample standard deviation is used.
    </p>

    3

    <p>
      This statistic follows a t-distribution under appropriate assumptions.
    </p>

    <h2>Interpreting a t Statistic</h2>

    <p>
      A t-statistic measures how many estimated standard errors separate the sample mean from a hypothesized population mean.
    </p>

    <div class="example-box">

      <p>
        t = 0 → perfect agreement
      </p>

      <p>
        Large positive t → sample mean is much larger
      </p>

      <p>
        Large negative t → sample mean is much smaller
      </p>

    </div>

    <h2>What Is a t Test?</h2>

    <p>
      A t-test evaluates whether observed sample data provide evidence against a hypothesized population mean.
    </p>

    <div class="concept-box">

      <strong>Purpose:</strong>

      <p>
        Determine whether a difference is larger than would be expected from sampling variability alone.
      </p>

    </div>

    <h2>A Simple Example</h2>

    <p>
      Suppose a manufacturer claims:
    </p>

    <div class="example-box">

      <p>
        Average battery life = 10 hours
      </p>

    </div>

    <p>
      A sample of batteries is tested.
    </p>

    <p>
      If the sample mean differs substantially from 10 hours,
      a t-test can determine whether the difference is statistically meaningful.
    </p>

    <h2>The Logic of a t Test</h2>

    <ol>

      <li>Assume a population mean.</li>

      <li>Collect sample data.</li>

      <li>Compute a t-statistic.</li>

      <li>Evaluate how unusual the result would be if the assumption were true.</li>

    </ol>

    <h2>Confidence Intervals Using t</h2>

    <p>
      Confidence intervals for means often use the t-distribution.
    </p>

    <p>
      The general structure is:
    </p>

    4

    <p>
      where:
    </p>

    <ul class="bullets">

      <li>t* is a critical value from the t-distribution</li>

      <li>s is the sample standard deviation</li>

    </ul>

    <h2>Why Small Samples Need t Procedures</h2>

    <p>
      Small samples contain more uncertainty.
    </p>

    <p>
      The heavier tails of the t-distribution account for this uncertainty and produce wider confidence intervals.
    </p>

    <p>
      Wider intervals provide more realistic assessments of precision.
    </p>

    <h2>Common Types of t Tests</h2>

    <ul class="bullets">

      <li>One-sample t-test</li>

      <li>Two-sample t-test</li>

      <li>Paired t-test</li>

    </ul>

    <p>
      These tests address different research questions but share the same underlying principles.
    </p>

    <h2>Assumptions of t Procedures</h2>

    <ul class="bullets">

      <li>Random sampling</li>

      <li>Independent observations</li>

      <li>Approximately normal population for small samples</li>

    </ul>

    <p>
      Large samples often reduce sensitivity to normality assumptions.
    </p>

    <h2>When Z and t Become Similar</h2>

    <p>
      As sample size grows:
    </p>

    5

    <p>
      The distinction between z and t procedures becomes increasingly small.
    </p>

    <p>
      For very large samples,
      the results are often nearly identical.
    </p>

    <h2>Why the t Distribution Matters</h2>

    <p>
      Most real analyses do not know the population standard deviation.
    </p>

    <p>
      The t-distribution allows valid inference despite this uncertainty.
    </p>

    <p>
      It is one of the most frequently used tools in applied statistics.
    </p>

    <h2>Looking Ahead</h2>

    <p>
      The t-distribution is not the only important sampling distribution.
    </p>

    <p>
      Another key distribution arises when studying variability itself.
    </p>

    <p>
      The next lesson introduces the chi-square distribution and shows how it is used for variance estimation and inference.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>The t-distribution is used when population standard deviation is unknown</li>

        <li>It resembles the normal distribution but has heavier tails</li>

        <li>Degrees of freedom determine the exact shape</li>

        <li>The t-distribution approaches the normal distribution as sample size increases</li>

        <li>The t-statistic uses the sample standard deviation</li>

        <li>t-tests evaluate claims about population means</li>

        <li>t-based confidence intervals account for additional uncertainty</li>

        <li>The t-distribution is one of the most important tools in statistical inference</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/probability/sampling-distributions/z-statistic-and-ci/">
         ← Previous: Z Statistic and Confidence Intervals
      </a>

      <a class="btn"
         href="/probability/sampling-distributions/chi-square-and-variance/">
         Next: Chi-Square and Variance →
      </a>

    </div>

  </div>

</section>