---
layout: default
title: Z-Scores
description: Learn what z-scores are, how they standardize observations, and how they help compare values across different distributions.
permalink: /descriptive/shape/z-scores/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_descriptive_shape_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/descriptive/shape/z-scores/",
    label: "Z-Scores",
    ts: Date.now()
  }));

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Descriptive Statistics</span>
      <span class="badge">Block 6</span>
      <span class="badge">Shape</span>
      <span class="badge">Standardization</span>
    </div>

    <h1>Z-Scores</h1>

    <p class="lead">
      The Empirical Rule tells us how observations are distributed around the mean.
    </p>

    <p class="lead">
      But how can we determine exactly how far a particular observation lies from the mean?
      Z-scores provide the answer by expressing distance in units of standard deviation.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/descriptive/shape/empirical-rule/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/descriptive/shape/standardization-when-and-when-not/">
         Next: Standardization — When and When Not →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section class="section">

  <div class="content-narrow">

    <h2>What Is a Z-Score?</h2>

    <p>
      A <strong>z-score</strong> measures how far an observation is from the mean,
      expressed in standard deviation units.
    </p>

    <p>
      Instead of describing distance using the original measurement units,
      z-scores describe distance using standard deviations.
    </p>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        A z-score tells us how many standard deviations an observation is above or below the mean.
      </p>

    </div>

    <h2>Why Do We Need Z-Scores?</h2>

    <p>
      Raw values can be difficult to compare across different situations.
    </p>

    <p>
      For example,
      is a score of 85 on an exam more impressive than a score of 1,200 on a standardized test?
    </p>

    <p>
      The answer depends on the distributions of those scores.
    </p>

    <p>
      Z-scores place observations onto a common scale,
      allowing meaningful comparisons.
    </p>

    <h2>The Formula</h2>

    <p>
      The z-score of an observation is calculated by subtracting the mean and dividing by the standard deviation.
    </p>

    0

    <p>
      For sample-based calculations,
      the sample mean and sample standard deviation may be used instead.
    </p>

    <h2>Understanding the Formula</h2>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Symbol</th>
            <th>Meaning</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>x</td>
            <td>The observation</td>
          </tr>

          <tr>
            <td>μ</td>
            <td>Population mean</td>
          </tr>

          <tr>
            <td>σ</td>
            <td>Population standard deviation</td>
          </tr>

          <tr>
            <td>z</td>
            <td>Standardized score</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>A Simple Example</h2>

    <p>
      Suppose exam scores have:
    </p>

    <div class="example-box">

      <p>
        Mean = 70
      </p>

      <p>
        Standard Deviation = 10
      </p>

    </div>

    <p>
      A student scores:
    </p>

    <div class="example-box">

      <p>
        x = 80
      </p>

    </div>

    <p>
      The z-score is:
    </p>

    1

    <p>
      This score is one standard deviation above the mean.
    </p>

    <h2>Interpreting Positive Z-Scores</h2>

    <p>
      Positive z-scores indicate observations above the mean.
    </p>

    <div class="example-box">

      <p>
        z = 1 → one standard deviation above the mean
      </p>

      <p>
        z = 2 → two standard deviations above the mean
      </p>

      <p>
        z = 3 → three standard deviations above the mean
      </p>

    </div>

    <p>
      Larger positive z-scores indicate increasingly unusual high values.
    </p>

    <h2>Interpreting Negative Z-Scores</h2>

    <p>
      Negative z-scores indicate observations below the mean.
    </p>

    <div class="example-box">

      <p>
        z = -1 → one standard deviation below the mean
      </p>

      <p>
        z = -2 → two standard deviations below the mean
      </p>

      <p>
        z = -3 → three standard deviations below the mean
      </p>

    </div>

    <p>
      Larger negative magnitudes indicate increasingly unusual low values.
    </p>

    <h2>What Does a Z-Score of Zero Mean?</h2>

    <p>
      When an observation equals the mean,
      the numerator becomes zero.
    </p>

    2

    <p>
      Therefore,
      a z-score of zero indicates that the observation lies exactly at the mean.
    </p>

    <h2>Z-Scores and the Empirical Rule</h2>

    <p>
      The Empirical Rule can be expressed directly in terms of z-scores.
    </p>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Z-Score Range</th>
            <th>Approximate Percentage</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>-1 to +1</td>
            <td>68%</td>
          </tr>

          <tr>
            <td>-2 to +2</td>
            <td>95%</td>
          </tr>

          <tr>
            <td>-3 to +3</td>
            <td>99.7%</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      This connection makes z-scores especially useful for identifying unusual observations.
    </p>

    <h2>Comparing Different Variables</h2>

    <p>
      One of the greatest advantages of z-scores is that they allow comparisons across different variables.
    </p>

    <p>
      Consider:
    </p>

    <ul class="bullets">

      <li>Exam score = 90</li>

      <li>Basketball points = 24</li>

      <li>Sales revenue = $5,000</li>

    </ul>

    <p>
      These values use completely different units.
    </p>

    <p>
      Z-scores place them on a common scale.
    </p>

    <h2>An Example of Comparison</h2>

    <p>
      Student A:
    </p>

    <div class="example-box">

      <p>
        Exam score z = 2.1
      </p>

    </div>

    <p>
      Student B:
    </p>

    <div class="example-box">

      <p>
        Athletic performance z = 1.3
      </p>

    </div>

    <p>
      Student A performed farther above their group's average than Student B did.
    </p>

    <p>
      This comparison would be difficult using raw scores alone.
    </p>

    <h2>Z-Scores and Outliers</h2>

    <p>
      Large absolute z-scores often indicate unusual observations.
    </p>

    <p>
      Common guidelines include:
    </p>

    <ul class="bullets">

      <li>|z| > 2 → somewhat unusual</li>

      <li>|z| > 3 → very unusual</li>

    </ul>

    <p>
      These are guidelines rather than strict rules.
    </p>

    <h2>Standardization Creates a Common Scale</h2>

    <p>
      Converting observations into z-scores is called
      <strong>standardization</strong>.
    </p>

    <p>
      Standardization transforms values so they can be interpreted relative to their distribution.
    </p>

    <p>
      This process is fundamental throughout statistics and data science.
    </p>

    <h2>Properties of Standardized Data</h2>

    <p>
      After standardization:
    </p>

    <ul class="bullets">

      <li>The mean becomes 0</li>

      <li>The standard deviation becomes 1</li>

      <li>The overall shape remains unchanged</li>

    </ul>

    <p>
      Only the scale changes.
    </p>

    <h2>Z-Scores in Practice</h2>

    <p>
      Z-scores are widely used in:
    </p>

    <ul class="bullets">

      <li>Educational testing</li>

      <li>Psychology</li>

      <li>Quality control</li>

      <li>Finance</li>

      <li>Medical research</li>

      <li>Machine learning</li>

    </ul>

    <p>
      They provide a universal way to compare observations.
    </p>

    <h2>Shape Still Matters</h2>

    <p>
      Z-scores can be calculated for any numerical dataset.
    </p>

    <p>
      However,
      their interpretation is often most meaningful when distributions are reasonably symmetric and bell-shaped.
    </p>

    <p>
      Shape and standardization remain closely connected concepts.
    </p>

    <h2>Why Z-Scores Matter</h2>

    <p>
      Z-scores transform raw observations into standardized measurements.
    </p>

    <p>
      They tell us where an observation stands relative to the rest of the distribution.
    </p>

    <p>
      This makes them one of the most important tools in descriptive statistics,
      probability,
      and inferential statistics.
    </p>

    <h2>Looking Ahead</h2>

    <p>
      Standardization is powerful,
      but it is not always appropriate.
    </p>

    <p>
      The next lesson examines when standardization is useful,
      when it may be misleading,
      and how to decide whether z-scores should be used in practice.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>A z-score measures distance from the mean in standard deviation units</li>

        <li>Positive z-scores indicate values above the mean</li>

        <li>Negative z-scores indicate values below the mean</li>

        <li>A z-score of zero indicates an observation equal to the mean</li>

        <li>Z-scores allow comparisons across different variables and units</li>

        <li>Large absolute z-scores often indicate unusual observations</li>

        <li>Standardization transforms data to a common scale while preserving shape</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/descriptive/shape/empirical-rule/">
         ← Previous: Empirical Rule
      </a>

      <a class="btn"
         href="/descriptive/shape/standardization-when-and-when-not/">
         Next: Standardization — When and When Not →
      </a>

    </div>

  </div>

</section>