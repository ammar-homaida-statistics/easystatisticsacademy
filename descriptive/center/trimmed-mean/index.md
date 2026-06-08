---
layout: default
title: Trimmed Mean
description: Learn what a trimmed mean is, how it reduces the influence of extreme values, and why it provides a compromise between the mean and median.
permalink: /descriptive/center/trimmed-mean/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_descriptive_center_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/descriptive/center/trimmed-mean/",
    label: "Trimmed Mean",
    ts: Date.now()
  }));

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Descriptive Statistics</span>
      <span class="badge">Block 4</span>
      <span class="badge">Center</span>
      <span class="badge">Robust Statistics</span>
    </div>

    <h1>Trimmed Mean</h1>

    <p class="lead">
      The arithmetic mean uses all observations,
      which makes it sensitive to outliers.
    </p>

    <p class="lead">
      The median is resistant to outliers,
      but it ignores much of the information contained in the dataset.
      The trimmed mean provides a compromise by removing extreme observations before calculating the mean.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/descriptive/center/weighted-mean/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/descriptive/center/winsorized-mean/">
         Next: Winsorized Mean →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section class="section">

  <div class="content-narrow">

    <h2>Why Was the Trimmed Mean Created?</h2>

    <p>
      The ordinary mean is strongly affected by unusually large or unusually small observations.
    </p>

    <p>
      In some datasets,
      a few extreme values can pull the mean away from where most observations are located.
    </p>

    <p>
      Statisticians developed the trimmed mean to reduce this problem.
    </p>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        A trimmed mean removes a small percentage of the smallest and largest observations before calculating the mean.
      </p>

    </div>

    <h2>What Is a Trimmed Mean?</h2>

    <p>
      A <strong>trimmed mean</strong>
      is calculated by:
    </p>

    <ol>

      <li>Ordering the data.</li>

      <li>Removing a specified percentage of the smallest values.</li>

      <li>Removing the same percentage of the largest values.</li>

      <li>Computing the arithmetic mean of the remaining observations.</li>

    </ol>

    <p>
      The result is less sensitive to outliers than the ordinary mean.
    </p>

    <h2>A Simple Example</h2>

    <p>
      Consider the dataset:
    </p>

    <div class="example-box">

      <p>
        10, 11, 12, 13, 14, 15, 100
      </p>

    </div>

    <p>
      The value 100 is an extreme observation.
    </p>

    <p>
      The ordinary mean is:
    </p>

    0

    <p>
      The mean of 25 is much larger than most observations.
    </p>

    <h2>Applying a Trim</h2>

    <p>
      Suppose we remove:
    </p>

    <ul class="bullets">

      <li>The smallest observation (10)</li>

      <li>The largest observation (100)</li>

    </ul>

    <p>
      The remaining data become:
    </p>

    <div class="example-box">

      <p>
        11, 12, 13, 14, 15
      </p>

    </div>

    <p>
      The trimmed mean is:
    </p>

    1

    <p>
      This value better reflects where most observations are located.
    </p>

    <h2>How Much Data Should Be Trimmed?</h2>

    <p>
      There is no single rule.
    </p>

    <p>
      Common choices include:
    </p>

    <ul class="bullets">

      <li>5% trimmed mean</li>

      <li>10% trimmed mean</li>

      <li>20% trimmed mean</li>

    </ul>

    <p>
      The percentage refers to each tail of the distribution.
    </p>

    <h2>What Does a 10% Trim Mean?</h2>

    <p>
      A 10% trimmed mean removes:
    </p>

    <ul class="bullets">

      <li>10% of observations from the lower end</li>

      <li>10% of observations from the upper end</li>

    </ul>

    <p>
      The mean is then computed using the remaining 80% of observations.
    </p>

    <h2>The Trimmed Mean Lies Between Mean and Median</h2>

    <p>
      The trimmed mean is often viewed as a compromise.
    </p>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Measure</th>
            <th>Uses All Data?</th>
            <th>Resistant to Outliers?</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>Mean</td>
            <td>Yes</td>
            <td>No</td>
          </tr>

          <tr>
            <td>Trimmed Mean</td>
            <td>Mostly</td>
            <td>Partially</td>
          </tr>

          <tr>
            <td>Median</td>
            <td>No</td>
            <td>Yes</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>Why Not Always Use the Median?</h2>

    <p>
      The median is extremely resistant to outliers,
      but it ignores the actual magnitudes of many observations.
    </p>

    <p>
      The trimmed mean still uses most of the data.
    </p>

    <p>
      This often allows it to estimate center more efficiently than the median.
    </p>

    <h2>Robust Statistics</h2>

    <p>
      The trimmed mean belongs to a family of methods known as
      <strong>robust statistics</strong>.
    </p>

    <p>
      Robust methods are designed to perform well even when unusual observations are present.
    </p>

    <p>
      Modern data analysis frequently relies on robust techniques.
    </p>

    <h2>Advantages of the Trimmed Mean</h2>

    <ul class="bullets">

      <li>Less affected by outliers</li>

      <li>Uses most observations</li>

      <li>More stable than the ordinary mean</li>

      <li>Often performs well for skewed data</li>

      <li>Widely used in robust statistics</li>

    </ul>

    <h2>Limitations of the Trimmed Mean</h2>

    <ul class="bullets">

      <li>Requires selecting a trimming percentage</li>

      <li>Some information is discarded</li>

      <li>Different trim levels may produce different results</li>

      <li>Less familiar than the ordinary mean</li>

    </ul>

    <h2>Trimmed Mean and Skewed Data</h2>

    <p>
      In highly skewed distributions,
      a trimmed mean can provide a more representative summary than the arithmetic mean.
    </p>

    <p>
      It reduces the influence of extreme tails while retaining most observations.
    </p>

    <h2>Applications of Trimmed Means</h2>

    <p>
      Trimmed means are used in:
    </p>

    <ul class="bullets">

      <li>Research studies</li>

      <li>Psychology</li>

      <li>Economics</li>

      <li>Quality control</li>

      <li>Sports judging systems</li>

      <li>Robust statistical analysis</li>

    </ul>

    <p>
      In some judged competitions,
      unusually high and low scores may be removed before averaging.
    </p>

    <p>
      This is essentially a trimmed mean.
    </p>

    <h2>Mean, Median, and Trimmed Mean</h2>

    <p>
      These three measures form a useful progression:
    </p>

    <ul class="bullets">

      <li>Mean → uses all observations</li>

      <li>Trimmed Mean → removes a few extremes</li>

      <li>Median → relies only on position</li>

    </ul>

    <p>
      As resistance increases,
      sensitivity to outliers decreases.
    </p>

    <h2>Trimmed Mean vs Winsorized Mean</h2>

    <p>
      The trimmed mean removes extreme observations entirely.
    </p>

    <p>
      The next lesson introduces the
      <strong>winsorized mean</strong>,
      which takes a different approach.
    </p>

    <p>
      Instead of removing extreme values,
      it replaces them with less extreme values before averaging.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>A trimmed mean removes extreme observations before averaging</li>

        <li>It reduces the influence of outliers</li>

        <li>Common trim levels include 5%, 10%, and 20%</li>

        <li>The trimmed mean balances efficiency and robustness</li>

        <li>It uses more information than the median</li>

        <li>It is less sensitive to outliers than the ordinary mean</li>

        <li>The trimmed mean is an important tool in robust statistics</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/descriptive/center/weighted-mean/">
         ← Previous: Weighted Mean
      </a>

      <a class="btn"
         href="/descriptive/center/winsorized-mean/">
         Next: Winsorized Mean →
      </a>

    </div>

  </div>

</section>