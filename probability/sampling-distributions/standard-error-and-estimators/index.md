---
layout: default
title: Standard Error and Estimators
description: Learn what estimators are, why they vary across samples, and how standard error measures estimation uncertainty.
permalink: /probability/sampling-distributions/standard-error-and-estimators/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_probability_sampling_distributions_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/probability/sampling-distributions/standard-error-and-estimators/",
    label: "Standard Error and Estimators",
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
      <span class="badge">Inference Basics</span>
    </div>

    <h1>Standard Error and Estimators</h1>

    <p class="lead">
      Statistical inference begins with estimation.
    </p>

    <p class="lead">
      Every estimate comes from a sample and therefore contains uncertainty. Standard error measures that uncertainty and helps us understand how reliable an estimate is.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/probability/sampling-distributions/what-is-a-sampling-distribution/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/probability/sampling-distributions/z-statistic-and-ci/">
         Next: Z Statistic and CI →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>What Is an Estimator?</h2>

    <p>
      An estimator is a rule or formula used to estimate an unknown population parameter from sample data.
    </p>

    <div class="concept-box">

      <strong>Definition:</strong>

      <p>
        An estimator is a statistic designed to estimate a population parameter.
      </p>

    </div>

    <h2>Parameter vs Estimator</h2>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Population Quantity</th>
            <th>Estimator</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>μ (population mean)</td>
            <td>x̄ (sample mean)</td>
          </tr>

          <tr>
            <td>p (population proportion)</td>
            <td>p̂ (sample proportion)</td>
          </tr>

          <tr>
            <td>σ² (population variance)</td>
            <td>s² (sample variance)</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      Parameters are fixed but unknown.
    </p>

    <p>
      Estimators are random because samples vary.
    </p>

    <h2>Why Estimates Change</h2>

    <p>
      Different samples produce different estimates.
    </p>

    <div class="example-box">

      <p>
        Sample 1 → Mean = 48
      </p>

      <p>
        Sample 2 → Mean = 52
      </p>

      <p>
        Sample 3 → Mean = 50
      </p>

    </div>

    <p>
      None of these estimates are necessarily wrong.
    </p>

    <p>
      They differ because of sampling variability.
    </p>

    <h2>The Sampling Distribution of an Estimator</h2>

    <p>
      Every estimator has a sampling distribution.
    </p>

    <p>
      For example,
      the sample mean:
    </p>

    0

    <p>
      has a distribution across repeated samples.
    </p>

    <p>
      This distribution describes how estimates vary from sample to sample.
    </p>

    <h2>Good Estimators</h2>

    <p>
      Statisticians typically want estimators that are:
    </p>

    <ul class="bullets">

      <li>Accurate</li>

      <li>Unbiased</li>

      <li>Consistent</li>

      <li>Stable</li>

    </ul>

    <p>
      Stability is closely connected to standard error.
    </p>

    <h2>What Is Standard Error?</h2>

    <p>
      Standard error measures the variability of an estimator across repeated samples.
    </p>

    <div class="concept-box">

      <strong>Definition:</strong>

      <p>
        Standard error is the standard deviation of a sampling distribution.
      </p>

    </div>

    <h2>Why Standard Error Matters</h2>

    <p>
      Two estimators may have the same center but different levels of variability.
    </p>

    <div class="example-box">

      <p>
        Small standard error → precise estimates
      </p>

      <p>
        Large standard error → less precise estimates
      </p>

    </div>

    <p>
      Precision is one of the most important concepts in inference.
    </p>

    <h2>Standard Error of the Mean</h2>

    <p>
      For independent observations:
    </p>

    1

    <p>
      where:
    </p>

    <ul class="bullets">

      <li>σ = population standard deviation</li>

      <li>n = sample size</li>

    </ul>

    <h2>Understanding the Formula</h2>

    <p>
      The formula reveals an important fact:
    </p>

    <p>
      Increasing sample size decreases uncertainty.
    </p>

    <p>
      Because:
    </p>

    2

    <p>
      larger samples produce more precise estimates.
    </p>

    <h2>Example: Sample Means</h2>

    <p>
      Suppose:
    </p>

    <div class="example-box">

      <p>
        σ = 20
      </p>

      <p>
        n = 100
      </p>

    </div>

    <p>
      Then:
    </p>

    3

    <p>
      Sample means typically fluctuate by about 2 units around the population mean.
    </p>

    <h2>Standard Error Versus Standard Deviation</h2>

    <p>
      These concepts are often confused.
    </p>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Standard Deviation</th>
            <th>Standard Error</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>Variability of data</td>
            <td>Variability of estimates</td>
          </tr>

          <tr>
            <td>Describes observations</td>
            <td>Describes a statistic</td>
          </tr>

          <tr>
            <td>Population characteristic</td>
            <td>Sampling characteristic</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>Visual Interpretation</h2>

    <p>
      Imagine repeatedly drawing samples and computing sample means.
    </p>

    <p>
      The standard error measures the spread of those means.
    </p>

    <div class="example-box">

      <p>
        Small spread → small SE
      </p>

      <p>
        Large spread → large SE
      </p>

    </div>

    <h2>Standard Error of a Sample Proportion</h2>

    <p>
      For a sample proportion:
    </p>

    4

    <p>
      This formula describes how sample proportions vary across samples.
    </p>

    <h2>Why Sample Size Is Powerful</h2>

    <p>
      Consider increasing sample size:
    </p>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Sample Size</th>
            <th>Effect on SE</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>25</td>
            <td>Relatively large</td>
          </tr>

          <tr>
            <td>100</td>
            <td>Half as large</td>
          </tr>

          <tr>
            <td>400</td>
            <td>Half again</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      Larger samples reduce uncertainty,
      but the improvement follows a square-root relationship.
    </p>

    <h2>Estimators and Precision</h2>

    <p>
      A useful estimator should not only be centered correctly.
    </p>

    <p>
      It should also have a reasonably small standard error.
    </p>

    <p>
      Accurate estimation requires both correctness and precision.
    </p>

    <h2>Connection to Confidence Intervals</h2>

    <p>
      Standard error determines how wide a confidence interval will be.
    </p>

    <div class="example-box">

      <p>
        Smaller SE → narrower interval
      </p>

      <p>
        Larger SE → wider interval
      </p>

    </div>

    <p>
      Confidence intervals are built directly from standard errors.
    </p>

    <h2>Connection to Hypothesis Testing</h2>

    <p>
      Hypothesis tests compare observed results to expected variability.
    </p>

    <p>
      Standard error provides the scale for those comparisons.
    </p>

    <p>
      Without standard error,
      significance testing would not be possible.
    </p>

    <h2>The Big Picture</h2>

    <p>
      Estimators help us learn about unknown parameters.
    </p>

    <p>
      Standard errors quantify how much those estimates fluctuate.
    </p>

    <p>
      Together,
      they form the foundation of modern statistical inference.
    </p>

    <h2>Looking Ahead</h2>

    <p>
      Once we know an estimate and its standard error,
      we can standardize the result and construct confidence intervals.
    </p>

    <p>
      The next lesson introduces z-statistics and shows how confidence intervals are built from sampling distributions.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>An estimator is a statistic used to estimate a population parameter</li>

        <li>Estimators vary because samples vary</li>

        <li>Every estimator has a sampling distribution</li>

        <li>Standard error is the standard deviation of a sampling distribution</li>

        <li>Smaller standard errors imply more precise estimates</li>

        <li>The standard error of the mean equals σ/√n</li>

        <li>Standard error decreases as sample size increases</li>

        <li>Confidence intervals and hypothesis tests depend on standard errors</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/probability/sampling-distributions/what-is-a-sampling-distribution/">
         ← Previous: What Is a Sampling Distribution?
      </a>

      <a class="btn"
         href="/probability/sampling-distributions/z-statistic-and-ci/">
         Next: Z Statistic and CI →
      </a>

    </div>

  </div>

</section>