---
layout: default
title: What Is a Sampling Distribution?
description: Learn what a sampling distribution is and why it is one of the most important ideas in statistical inference.
permalink: /probability/sampling-distributions/what-is-a-sampling-distribution/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_probability_sampling_distributions_lesson_v0";

  try {
    localStorage.setItem(KEY, JSON.stringify({
    url: "/probability/sampling-distributions/what-is-a-sampling-distribution/",
    label: "What Is a Sampling Distribution?",
    ts: Date.now()
    }));
  } catch (_) {
    // Browser storage can be blocked or full without preventing reading.
  }

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Probability</span>
      <span class="badge">Block 7</span>
      <span class="badge">Sampling Distributions</span>
      <span class="badge">Foundations</span>
    </div>

    <h1>What Is a Sampling Distribution?</h1>

    <p class="lead">
      Every sample produces slightly different results.
    </p>

    <p class="lead">
      A sampling distribution describes how a statistic varies across all possible samples and provides the foundation for confidence intervals, hypothesis tests, and statistical inference.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/probability/sampling-distributions/">
         ← Back to Sampling Distributions
      </a>

      <a class="btn btn-outline"
         href="/probability/sampling-distributions/standard-error-and-estimators/">
         Next: Standard Error and Estimators →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>Why Sampling Distributions Exist</h2>

    <p>
      Imagine drawing a sample from a population and calculating a statistic.
    </p>

    <div class="example-box">

      <p>
        Sample mean
      </p>

      <p>
        Sample proportion
      </p>

      <p>
        Sample variance
      </p>

    </div>

    <p>
      If you drew a different sample,
      the statistic would usually have a different value.
    </p>

    <p>
      Sampling distributions describe this natural variation.
    </p>

    <h2>A Simple Example</h2>

    <p>
      Suppose a population contains:
    </p>

    <div class="example-box">

      <p>
        2, 4, 6, 8
      </p>

    </div>

    <p>
      Draw samples of size 2 without replacement and calculate the
      sample mean for each of the six equally likely unordered pairs.
      This finite-population illustration differs from the independent
      sampling model used for the standard-error formula below.
    </p>

    <p>
      Different samples produce different means.
    </p>

    <div class="example-box">

      <p>
        (2,4) → Mean = 3
      </p>

      <p>
        (2,6) → Mean = 4
      </p>

      <p>
        (2,8) → Mean = 5
      </p>

      <p>
        (4,6) → Mean = 5
      </p>

      <p>
        (4,8) → Mean = 6
      </p>

      <p>
        (6,8) → Mean = 7
      </p>

    </div>

    <p>
      These means themselves form a distribution.
    </p>

    <p>
      That distribution is a sampling distribution.
    </p>

    <h2>Formal Definition</h2>

    <div class="concept-box">

      <strong>Definition:</strong>

      <p>
        A sampling distribution is the probability distribution of a statistic computed from all possible samples of a fixed size from a population.
      </p>

    </div>

    <h2>Population Distribution vs Sampling Distribution</h2>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Population Distribution</th>
            <th>Sampling Distribution</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>Distribution of individual observations</td>
            <td>Distribution of a statistic</td>
          </tr>

          <tr>
            <td>Describes data values</td>
            <td>Describes sample summaries</td>
          </tr>

          <tr>
            <td>Usually unknown</td>
            <td>Can often be modeled mathematically</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>The Statistic Is Random</h2>

    <p>
      Before a sample is collected,
      the value of a statistic is unknown.
    </p>

    <p>
      Different samples lead to different outcomes.
    </p>

    <p>
      Therefore statistics are random variables.
    </p>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        Sampling distributions exist because sample statistics are random variables.
      </p>

    </div>

    <h2>Common Sampling Distributions</h2>

    <ul class="bullets">

      <li>Sampling distribution of the sample mean</li>

      <li>Sampling distribution of a sample proportion</li>

      <li>Sampling distribution of a sample variance</li>

      <li>Sampling distribution of regression coefficients</li>

    </ul>

    <p>
      These distributions play a central role in inference.
    </p>

    <h2>The Sampling Distribution of the Mean</h2>

    <p>
      One of the most important examples is the distribution of:
    </p>

    \[
\bar X_n=\frac{1}{n}\sum_{i=1}^{n}X_i
\]

    <p>
      across repeated samples.
    </p>

    <p>
      Under independent, identically distributed sampling with finite,
      positive variance, the Central Limit Theorem gives an approximately
      normal sampling distribution for the standardized sample mean as n
      grows. This asymptotic approximation is distinct from the exact
      expectation and variance results below.
    </p>

    <h2>The Center of a Sampling Distribution</h2>

    <p>
      For independent, identically distributed observations with finite
      mean μ, linearity of expectation gives the exact result:
    </p>

    \[
\operatorname{E}(\bar X_n)=\mu
\]

    <p>
      This means sample means are centered on the population mean.
    </p>

    <p>
      On average,
      the sample mean hits the correct target.
    </p>

    <h2>The Spread of a Sampling Distribution</h2>

    <p>
      Sample means vary from sample to sample.
    </p>

    <p>
      For independent, identically distributed observations with finite
      population variance σ², their theoretical sampling variability is:
    </p>

    \[
\operatorname{SE}(\bar X_n)
=\sqrt{\operatorname{Var}(\bar X_n)}
=\frac{\sigma}{\sqrt n}
\]

    <p>
      This is the theoretical standard error of the mean. If σ is
      unknown, s/√n is the usual sample-based estimate of this SE.
      Dependent sampling and sampling without replacement from a finite
      population require an appropriate variance calculation.
    </p>

    <h2>Why Larger Samples Help</h2>

    <p>
      Under the same i.i.d. sampling model and population variance,
      quadrupling the sample size gives:
    </p>

    \[
\operatorname{SE}(\bar X_{4n})
=\frac12\,\operatorname{SE}(\bar X_n)
\qquad(\sigma\text{ fixed})
\]

    <p>
      Thus the standard error is halved. It decreases with n as
      1/√n when the population SD remains fixed.
    </p>

    <p>
      In this model, sample means become more concentrated around μ as
      n increases. The scaling need not hold unchanged for dependent data
      or a different sampling design.
    </p>

    <h2>The Central Role in Inference</h2>

    <p>
      Sampling distributions allow us to answer questions such as:
    </p>

    <div class="example-box">

      <p>
        How accurate is this estimate?
      </p>

      <p>
        How much uncertainty is present?
      </p>

      <p>
        Is this result surprising?
      </p>

      <p>
        Could this difference be due to chance?
      </p>

    </div>

    <p>
      These are the core questions of statistical inference.
    </p>

    <h2>Confidence Intervals Depend on Sampling Distributions</h2>

    <p>
      Confidence intervals use the variability of a statistic to create a range of plausible parameter values.
    </p>

    <p>
      Without a sampling distribution,
      confidence intervals could not be constructed.
    </p>

    <h2>Hypothesis Tests Depend on Sampling Distributions</h2>

    <p>
      Hypothesis testing asks whether an observed statistic is unusual.
    </p>

    <p>
      To answer that question,
      we must know the distribution of the statistic under repeated sampling.
    </p>

    <p>
      That information comes from the sampling distribution.
    </p>

    <h2>Sampling Distributions Are Usually Theoretical</h2>

    <p>
      In practice,
      we rarely generate all possible samples.
    </p>

    <p>
      Instead,
      probability theory provides mathematical formulas that describe the sampling distribution.
    </p>

    <p>
      The Central Limit Theorem is one of the most important tools for doing this.
    </p>

    <h2>The Big Picture</h2>

    <p>
      Data values vary.
    </p>

    <p>
      Statistics vary because samples vary.
    </p>

    <p>
      Sampling distributions quantify that variation.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        Statistical inference is fundamentally the study of sampling distributions.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      Understanding a sampling distribution requires understanding its variability.
    </p>

    <p>
      The next lesson introduces estimators and standard errors, which measure how much estimates vary across samples.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>A sampling distribution is the distribution of a statistic across all possible samples</li>

        <li>Statistics are random variables because samples vary</li>

        <li>Population distributions and sampling distributions are different concepts</li>

        <li>The sampling distribution of the mean is especially important</li>

        <li>Sample means are centered at the population mean</li>

        <li>Sampling distributions become narrower as sample size increases</li>

        <li>Confidence intervals and hypothesis tests rely on sampling distributions</li>

        <li>Statistical inference is built on understanding sampling variability</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/probability/sampling-distributions/">
         ← Back to Sampling Distributions
      </a>

      <a class="btn"
         href="/probability/sampling-distributions/standard-error-and-estimators/">
         Next: Standard Error and Estimators →
      </a>

    </div>

  </div>

</section>