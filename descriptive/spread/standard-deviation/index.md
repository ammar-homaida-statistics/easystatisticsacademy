---
layout: default
title: Standard Deviation
description: Learn what standard deviation is, how it relates to variance, and why it is the most widely used measure of variability in statistics.
permalink: /descriptive/spread/standard-deviation/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_descriptive_spread_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/descriptive/spread/standard-deviation/",
    label: "Standard Deviation",
    ts: Date.now()
  }));

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Descriptive Statistics</span>
      <span class="badge">Block 5</span>
      <span class="badge">Spread</span>
      <span class="badge">Standard Deviation</span>
    </div>

    <h1>Standard Deviation</h1>

    <p class="lead">
      Variance is one of the most important measures of variability,
      but it has a practical drawback:
      its units are squared.
    </p>

    <p class="lead">
      Standard deviation solves this problem by expressing variability in the same units as the original data,
      making it the most widely reported measure of spread in statistics.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/descriptive/spread/variance/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/descriptive/spread/coefficient-of-variation/">
         Next: Coefficient of Variation →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section class="section">

  <div class="content-narrow">

    <h2>What Is Standard Deviation?</h2>

    <p>
      The <strong>standard deviation</strong>
      measures the typical distance between observations and the mean.
    </p>

    <p>
      It is derived directly from variance and provides a more interpretable measure of spread.
    </p>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        Standard deviation measures how far observations typically fall from the mean.
      </p>

    </div>

    <h2>Why Was Standard Deviation Created?</h2>

    <p>
      Variance measures average squared deviations from the mean.
    </p>

    <p>
      While mathematically useful,
      squared units are difficult to interpret.
    </p>

    <p>
      Standard deviation fixes this problem by taking the square root of the variance.
    </p>

    <h2>The Formula</h2>

    <p>
      For a sample:
    </p>

    0

    <p>
      For a population:
    </p>

    1

    <p>
      Standard deviation is simply the square root of variance.
    </p>

    <h2>Connecting Variance and Standard Deviation</h2>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Measure</th>
            <th>Symbol</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Sample Variance</td>
            <td>s²</td>
          </tr>

          <tr>
            <td>Sample Standard Deviation</td>
            <td>s</td>
          </tr>

          <tr>
            <td>Population Variance</td>
            <td>σ²</td>
          </tr>

          <tr>
            <td>Population Standard Deviation</td>
            <td>σ</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>A Simple Example</h2>

    <p>
      Suppose a dataset has:
    </p>

    <div class="example-box">

      <p>
        Variance = 25
      </p>

    </div>

    <p>
      Then:
    </p>

    2

    <p>
      The standard deviation equals 5.
    </p>

    <p>
      Notice how the result is now expressed in the original measurement units.
    </p>

    <h2>What Does Standard Deviation Tell Us?</h2>

    <p>
      Standard deviation describes the typical amount by which observations differ from the mean.
    </p>

    <p>
      Small standard deviations indicate observations are clustered closely around the mean.
    </p>

    <p>
      Large standard deviations indicate observations are more widely dispersed.
    </p>

    <h2>Low Standard Deviation</h2>

    <p>
      Consider:
    </p>

    <div class="example-box">

      <p>
        98, 99, 100, 101, 102
      </p>

    </div>

    <p>
      These values are tightly concentrated around the center.
    </p>

    <p>
      Their standard deviation is small.
    </p>

    <p>
      The observations are highly consistent.
    </p>

    <h2>High Standard Deviation</h2>

    <p>
      Consider:
    </p>

    <div class="example-box">

      <p>
        20, 40, 60, 80, 100
      </p>

    </div>

    <p>
      These values are spread much farther apart.
    </p>

    <p>
      Their standard deviation is larger.
    </p>

    <p>
      The observations are less consistent.
    </p>

    <h2>Standard Deviation Equals Zero</h2>

    <p>
      If every observation is identical,
      there is no variability.
    </p>

    <div class="example-box">

      <p>
        10, 10, 10, 10, 10
      </p>

    </div>

    <p>
      Every observation equals the mean.
    </p>

    <p>
      Therefore:
    </p>

    3

    <p>
      Standard deviation equals zero.
    </p>

    <h2>Interpreting the Units</h2>

    <p>
      One major advantage of standard deviation is that it uses the same units as the original variable.
    </p>

    <p>
      For example:
    </p>

    <ul class="bullets">

      <li>Height measured in centimeters produces standard deviation in centimeters</li>

      <li>Weight measured in kilograms produces standard deviation in kilograms</li>

      <li>Income measured in dollars produces standard deviation in dollars</li>

    </ul>

    <p>
      This makes interpretation much easier than variance.
    </p>

    <h2>Standard Deviation and the Mean</h2>

    <p>
      Standard deviation is calculated relative to the mean.
    </p>

    <p>
      Because of this,
      it is most informative when used together with the mean.
    </p>

    <p>
      The pair:
    </p>

    <div class="example-box">

      <p>
        Mean ± Standard Deviation
      </p>

    </div>

    <p>
      is one of the most common summaries in statistics.
    </p>

    <h2>Mean and Standard Deviation as a Pair</h2>

    <p>
      For roughly symmetric numerical distributions,
      statisticians often report:
    </p>

    <div class="example-box">

      <p>
        Mean = 72.4<br>
        Standard Deviation = 8.1
      </p>

    </div>

    <p>
      Together,
      these values describe both center and spread.
    </p>

    <h2>The Effect of Outliers</h2>

    <p>
      Standard deviation is based on variance.
    </p>

    <p>
      Since variance squares deviations,
      large deviations receive extra weight.
    </p>

    <p>
      Consequently,
      standard deviation is sensitive to outliers.
    </p>

    <div class="example-box">

      <strong>Important:</strong>

      <p>
        Standard deviation is not resistant to outliers.
      </p>

    </div>

    <h2>Standard Deviation and Distribution Shape</h2>

    <p>
      Standard deviation describes spread,
      but it does not describe skewness,
      modality,
      or other aspects of shape.
    </p>

    <p>
      Graphs and additional statistics are often needed to obtain a complete picture of a distribution.
    </p>

    <h2>The Empirical Rule</h2>

    <p>
      For many approximately bell-shaped distributions,
      standard deviation has a particularly useful interpretation.
    </p>

    <p>
      A large proportion of observations tend to lie within a few standard deviations of the mean.
    </p>

    <p>
      This idea becomes important when studying normal distributions later.
    </p>

    <h2>Applications of Standard Deviation</h2>

    <p>
      Standard deviation is used extensively in:
    </p>

    <ul class="bullets">

      <li>Research studies</li>

      <li>Business analytics</li>

      <li>Economics</li>

      <li>Finance</li>

      <li>Engineering</li>

      <li>Machine learning</li>

      <li>Quality control</li>

    </ul>

    <p>
      It is one of the most frequently reported statistics in scientific publications.
    </p>

    <h2>Why Standard Deviation Matters</h2>

    <p>
      Standard deviation provides a balance between mathematical rigor and practical interpretation.
    </p>

    <p>
      It uses information from every observation,
      yet remains understandable because it shares the same units as the original data.
    </p>

    <p>
      For this reason,
      it has become the standard measure of spread in many fields.
    </p>

    <h2>Looking Ahead</h2>

    <p>
      Standard deviation measures absolute variability.
    </p>

    <p>
      However,
      comparing variability across variables with different units or different scales can be difficult.
    </p>

    <p>
      The next lesson introduces the
      <strong>Coefficient of Variation (CV)</strong>,
      which measures variability relative to the size of the mean.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Standard deviation is the square root of variance</li>

        <li>It measures the typical distance from the mean</li>

        <li>Standard deviation uses the same units as the original data</li>

        <li>Small standard deviations indicate less variability</li>

        <li>Large standard deviations indicate greater variability</li>

        <li>Standard deviation is sensitive to outliers</li>

        <li>Standard deviation is one of the most widely used measures of spread</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/descriptive/spread/variance/">
         ← Previous: Variance
      </a>

      <a class="btn"
         href="/descriptive/spread/coefficient-of-variation/">
         Next: Coefficient of Variation →
      </a>

    </div>

  </div>

</section>