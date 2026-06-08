---
layout: default
title: Interquartile Range (IQR)
description: Learn what the Interquartile Range (IQR) is, how it is calculated, and why it is one of the most important resistant measures of variability.
permalink: /descriptive/spread/interquartile-range/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_descriptive_spread_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/descriptive/spread/interquartile-range/",
    label: "Interquartile Range (IQR)",
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
      <span class="badge">IQR</span>
    </div>

    <h1>Interquartile Range (IQR)</h1>

    <p class="lead">
      The range measures spread using only the smallest and largest observations.
    </p>

    <p class="lead">
      Because extreme values can strongly influence the range,
      statisticians often prefer a more resistant measure of variability:
      the Interquartile Range, or IQR.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/descriptive/spread/range/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/descriptive/spread/variance/">
         Next: Variance →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section class="section">

  <div class="content-narrow">

    <h2>What Is the Interquartile Range?</h2>

    <p>
      The <strong>Interquartile Range (IQR)</strong>
      measures the spread of the middle 50% of a dataset.
    </p>

    <p>
      Instead of focusing on extreme observations,
      the IQR concentrates on the central portion of the data.
    </p>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        The IQR measures the distance between the first quartile (Q1) and the third quartile (Q3).
      </p>

    </div>

    <h2>What Are Quartiles?</h2>

    <p>
      Quartiles divide an ordered dataset into four approximately equal parts.
    </p>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Quartile</th>
            <th>Description</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>Q1</td>
            <td>25th percentile</td>
          </tr>

          <tr>
            <td>Q2</td>
            <td>50th percentile (Median)</td>
          </tr>

          <tr>
            <td>Q3</td>
            <td>75th percentile</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      Together,
      these quartiles divide the data into four sections.
    </p>

    <h2>The Formula</h2>

    <p>
      The Interquartile Range is calculated as:
    </p>

    0

    <p>
      The result represents the spread of the middle half of the observations.
    </p>

    <h2>Why Focus on the Middle 50%?</h2>

    <p>
      Extreme observations often distort measures of variability.
    </p>

    <p>
      By focusing on the middle portion of the data,
      the IQR provides a more stable summary of spread.
    </p>

    <p>
      This makes it resistant to outliers.
    </p>

    <h2>A Simple Example</h2>

    <p>
      Consider the ordered dataset:
    </p>

    <div class="example-box">

      <p>
        2, 4, 6, 8, 10, 12, 14, 16, 18
      </p>

    </div>

    <p>
      The median (Q2) is:
    </p>

    <div class="example-box">

      <p>
        10
      </p>

    </div>

    <p>
      The lower half is:
    </p>

    <div class="example-box">

      <p>
        2, 4, 6, 8
      </p>

    </div>

    <p>
      Q1 is the median of the lower half:
    </p>

    <div class="example-box">

      <p>
        Q1 = 5
      </p>

    </div>

    <p>
      The upper half is:
    </p>

    <div class="example-box">

      <p>
        12, 14, 16, 18
      </p>

    </div>

    <p>
      Q3 is the median of the upper half:
    </p>

    <div class="example-box">

      <p>
        Q3 = 15
      </p>

    </div>

    <p>
      Therefore:
    </p>

    1

    <p>
      The Interquartile Range is 10.
    </p>

    <h2>Interpreting the IQR</h2>

    <p>
      The IQR tells us how widely the middle 50% of observations are spread.
    </p>

    <p>
      A small IQR indicates that the central observations are clustered closely together.
    </p>

    <p>
      A large IQR indicates that the central observations are more dispersed.
    </p>

    <h2>Resistance to Outliers</h2>

    <p>
      One of the most important features of the IQR is its resistance.
    </p>

    <p>
      Consider:
    </p>

    <div class="example-box">

      <p>
        10, 11, 12, 13, 14
      </p>

    </div>

    <p>
      Now replace 14 with 100.
    </p>

    <div class="example-box">

      <p>
        10, 11, 12, 13, 100
      </p>

    </div>

    <p>
      The range changes dramatically.
    </p>

    <p>
      However,
      the middle observations remain largely unchanged.
    </p>

    <p>
      As a result,
      the IQR changes very little compared with the range.
    </p>

    <div class="example-box">

      <strong>Important:</strong>

      <p>
        The IQR is a resistant measure of variability.
      </p>

    </div>

    <h2>IQR and Boxplots</h2>

    <p>
      The IQR plays a central role in boxplots.
    </p>

    <p>
      In a boxplot:
    </p>

    <ul class="bullets">

      <li>The bottom of the box represents Q1</li>

      <li>The top of the box represents Q3</li>

      <li>The height or width of the box equals the IQR</li>

    </ul>

    <p>
      Thus,
      the size of the box visually represents the spread of the middle half of the data.
    </p>

    <h2>Comparing Range and IQR</h2>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Range</th>
            <th>IQR</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>Uses minimum and maximum</td>
            <td>Uses Q1 and Q3</td>
          </tr>

          <tr>
            <td>Highly sensitive to outliers</td>
            <td>Resistant to outliers</td>
          </tr>

          <tr>
            <td>Uses only two observations</td>
            <td>Uses the middle 50% of observations</td>
          </tr>

          <tr>
            <td>Measures total spread</td>
            <td>Measures central spread</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>When Should the IQR Be Used?</h2>

    <p>
      The IQR is particularly useful when:
    </p>

    <ul class="bullets">

      <li>Outliers are present</li>

      <li>Distributions are skewed</li>

      <li>A resistant measure of spread is needed</li>

      <li>The median is used as the measure of center</li>

    </ul>

    <p>
      In descriptive statistics,
      the median and IQR are often reported together.
    </p>

    <h2>Median and IQR: A Common Pair</h2>

    <p>
      Just as the mean is often paired with standard deviation,
      the median is often paired with the IQR.
    </p>

    <p>
      This combination provides resistant summaries of both center and spread.
    </p>

    <p>
      It is especially useful for skewed distributions.
    </p>

    <h2>Applications of the IQR</h2>

    <p>
      The IQR is commonly used in:
    </p>

    <ul class="bullets">

      <li>Exploratory data analysis</li>

      <li>Boxplots</li>

      <li>Outlier detection</li>

      <li>Medical research</li>

      <li>Business analytics</li>

      <li>Survey analysis</li>

    </ul>

    <p>
      It is one of the most frequently reported measures of spread.
    </p>

    <h2>The IQR and Outlier Detection</h2>

    <p>
      Later,
      the IQR will help identify unusually small or unusually large observations.
    </p>

    <p>
      Many standard outlier-detection methods are based directly on the IQR.
    </p>

    <p>
      This makes it important not only as a descriptive statistic,
      but also as a diagnostic tool.
    </p>

    <h2>Why the IQR Matters</h2>

    <p>
      The IQR solves one of the biggest weaknesses of the range:
      excessive sensitivity to extreme values.
    </p>

    <p>
      By focusing on the middle of the distribution,
      it provides a more reliable picture of variability in many practical situations.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>The Interquartile Range (IQR) measures the spread of the middle 50% of observations</li>

        <li>The IQR is calculated as Q3 − Q1</li>

        <li>Quartiles divide data into four approximately equal parts</li>

        <li>The IQR is resistant to outliers</li>

        <li>The IQR is commonly paired with the median</li>

        <li>The IQR is a key component of boxplots</li>

        <li>The IQR provides a more robust measure of spread than the range</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/descriptive/spread/range/">
         ← Previous: Range
      </a>

      <a class="btn"
         href="/descriptive/spread/variance/">
         Next: Variance →
      </a>

    </div>

  </div>

</section>