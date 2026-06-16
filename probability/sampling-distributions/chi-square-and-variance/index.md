---
layout: default
title: Chi-Square and Variance
description: Learn the chi-square distribution and how it is used to study population variance and variability.
permalink: /probability/sampling-distributions/chi-square-and-variance/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_probability_sampling_distributions_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/probability/sampling-distributions/chi-square-and-variance/",
    label: "Chi-Square and Variance",
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
      <span class="badge">Variance Inference</span>
    </div>

    <h1>Chi-Square and Variance</h1>

    <p class="lead">
      Means are important, but variability is equally important.
    </p>

    <p class="lead">
      The chi-square distribution provides the foundation for statistical inference about population variance and standard deviation.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/probability/sampling-distributions/t-distribution-and-t-test/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/probability/sampling-distributions/f-distribution-and-anova-preview/">
         Next: F Distribution and ANOVA Preview →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>Why Study Variance?</h2>

    <p>
      Two datasets can have the same mean while having very different levels of variability.
    </p>

    <div class="example-box">

      <p>
        Exam scores clustered tightly around 80
      </p>

      <p>
        Exam scores ranging from 20 to 100
      </p>

    </div>

    <p>
      Both datasets may share the same average,
      but their variability tells very different stories.
    </p>

    <h2>The Need for a New Distribution</h2>

    <p>
      The normal distribution helps analyze means.
    </p>

    <p>
      The t-distribution helps analyze means when population variability is unknown.
    </p>

    <p>
      To analyze variance itself,
      statisticians use the chi-square distribution.
    </p>

    <h2>What Is the Chi-Square Distribution?</h2>

    <div class="concept-box">

      <strong>Definition:</strong>

      <p>
        The chi-square distribution is a probability distribution that arises from sums of squared standard normal variables.
      </p>

    </div>

    <p>
      It is one of the most important distributions in statistical inference.
    </p>

    <h2>How It Is Constructed</h2>

    <p>
      Suppose:
    </p>

    <div class="example-box">

      <p>
        Z₁, Z₂, ..., Zₖ
      </p>

    </div>

    <p>
      are independent standard normal variables.
    </p>

    <p>
      Then:
    </p>

    0

    <p>
      follows a chi-square distribution with:
    </p>

    <p>
      k degrees of freedom.
    </p>

    <h2>Key Characteristics</h2>

    <ul class="bullets">

      <li>Always positive</li>

      <li>Right-skewed</li>

      <li>Depends on degrees of freedom</li>

      <li>Used extensively in inference</li>

    </ul>

    <h2>The Shape of the Distribution</h2>

    <p>
      Small degrees of freedom produce strong right skewness.
    </p>

    <p>
      Larger degrees of freedom make the distribution more symmetric.
    </p>

    <div class="concept-box">

      <strong>Observation:</strong>

      <p>
        As degrees of freedom increase, the chi-square distribution becomes less skewed.
      </p>

    </div>

    <h2>Degrees of Freedom</h2>

    <p>
      Degrees of freedom determine the exact shape of the chi-square distribution.
    </p>

    <p>
      For variance estimation:
    </p>

    1

    <p>
      where:
    </p>

    <ul class="bullets">

      <li>n = sample size</li>

    </ul>

    <h2>Connection to Sample Variance</h2>

    <p>
      One of the most important results in statistics is:
    </p>

    2

    <p>
      when data come from a normal population.
    </p>

    <p>
      This result forms the basis of variance inference.
    </p>

    <h2>What This Means</h2>

    <p>
      The sample variance:
    </p>

    3

    <p>
      changes from sample to sample.
    </p>

    <p>
      The chi-square distribution describes exactly how that variability behaves.
    </p>

    <h2>Estimating Population Variance</h2>

    <p>
      Most studies do not know:
    </p>

    4

    <p>
      the true population variance.
    </p>

    <p>
      Instead,
      researchers estimate it using:
    </p>

    5

    <p>
      from the sample.
    </p>

    <h2>Confidence Intervals for Variance</h2>

    <p>
      The chi-square distribution allows confidence intervals for:
    </p>

    <ul class="bullets">

      <li>Population variance</li>

      <li>Population standard deviation</li>

    </ul>

    <p>
      These intervals quantify uncertainty about variability.
    </p>

    <h2>Variance Hypothesis Tests</h2>

    <p>
      Researchers may wish to test claims such as:
    </p>

    <div class="example-box">

      <p>
        Process variability equals a target value
      </p>

      <p>
        Manufacturing consistency has changed
      </p>

      <p>
        Measurement systems meet quality standards
      </p>

    </div>

    <p>
      Chi-square tests provide a framework for evaluating such claims.
    </p>

    <h2>Applications in Quality Control</h2>

    <p>
      Variability is often more important than the average.
    </p>

    <p>
      Manufacturers frequently monitor variance to ensure consistent product quality.
    </p>

    <div class="example-box">

      <p>
        Bottle filling volumes
      </p>

      <p>
        Component dimensions
      </p>

      <p>
        Production tolerances
      </p>

    </div>

    <h2>Applications in Measurement Systems</h2>

    <p>
      Scientists often evaluate whether measurement procedures produce stable and reliable results.
    </p>

    <p>
      Variance-based methods help assess measurement precision.
    </p>

    <h2>Chi-Square Goodness-of-Fit Tests</h2>

    <p>
      Beyond variance estimation,
      chi-square methods are also used to compare observed counts with expected counts.
    </p>

    <div class="example-box">

      <p>
        Survey categories
      </p>

      <p>
        Genetic inheritance patterns
      </p>

      <p>
        Customer preference distributions
      </p>

    </div>

    <p>
      These applications become important later in statistical inference.
    </p>

    <h2>Comparing Distributions Used in Inference</h2>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Distribution</th>
            <th>Main Use</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>Normal (Z)</td>
            <td>Inference for means when variability is known</td>
          </tr>

          <tr>
            <td>t</td>
            <td>Inference for means when variability is estimated</td>
          </tr>

          <tr>
            <td>Chi-Square</td>
            <td>Inference for variance and variability</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>Why Variance Matters</h2>

    <p>
      Means describe location.
    </p>

    <p>
      Variances describe spread.
    </p>

    <p>
      Understanding both is necessary for a complete understanding of data.
    </p>

    <h2>The Next Step</h2>

    <p>
      Sometimes researchers want to compare variability across multiple groups simultaneously.
    </p>

    <p>
      This requires another important distribution:
    </p>

    <div class="example-box">

      <p>
        The F distribution
      </p>

    </div>

    <p>
      The F distribution forms the basis of ANOVA, one of the most widely used techniques in statistical analysis.
    </p>

    <h2>Looking Ahead</h2>

    <p>
      The next lesson introduces the F distribution and provides a preview of Analysis of Variance (ANOVA), a method used to compare multiple groups at the same time.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>The chi-square distribution is built from sums of squared standard normal variables</li>

        <li>It is always positive and usually right-skewed</li>

        <li>Its shape depends on degrees of freedom</li>

        <li>Chi-square distributions describe the behavior of sample variances</li>

        <li>They are used to estimate and test population variance</li>

        <li>Variance confidence intervals rely on chi-square methods</li>

        <li>Chi-square procedures are important in quality control and measurement analysis</li>

        <li>The chi-square distribution is one of the core distributions of statistical inference</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/probability/sampling-distributions/t-distribution-and-t-test/">
         ← Previous: t Distribution and t Test
      </a>

      <a class="btn"
         href="/probability/sampling-distributions/f-distribution-and-anova-preview/">
         Next: F Distribution and ANOVA Preview →
      </a>

    </div>

  </div>

</section>