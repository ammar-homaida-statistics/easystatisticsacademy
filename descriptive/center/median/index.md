---
layout: default
title: Median
description: Learn what the median is, how it is calculated, and why it is often preferred when data contain outliers or skewed distributions.
permalink: /descriptive/center/median/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_descriptive_center_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/descriptive/center/median/",
    label: "Median",
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
      <span class="badge">Median</span>
    </div>

    <h1>Median</h1>

    <p class="lead">
      The mean uses every observation in a dataset,
      but this makes it sensitive to extreme values.
    </p>

    <p class="lead">
      The median provides an alternative measure of center that focuses on position rather than magnitude.
      Because it is resistant to outliers,
      it is one of the most important statistics in data analysis.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/descriptive/center/arithmetic-mean/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/descriptive/center/mode/">
         Next: Mode →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section class="section">

  <div class="content-narrow">

    <h2>What Is the Median?</h2>

    <p>
      The <strong>median</strong>
      is the middle value in an ordered dataset.
    </p>

    <p>
      After arranging observations from smallest to largest,
      the median divides the data into two equal halves.
    </p>

    <p>
      Half of the observations lie below the median,
      and half lie above it.
    </p>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        The median is the value that sits in the middle of an ordered dataset.
      </p>

    </div>

    <h2>Why Order Matters</h2>

    <p>
      Unlike the mean,
      the median depends on the position of observations.
    </p>

    <p>
      Therefore,
      data must first be arranged in ascending or descending order.
    </p>

    <p>
      Without ordering,
      the median cannot be determined correctly.
    </p>

    <h2>Finding the Median: Odd Number of Observations</h2>

    <p>
      Consider the ordered dataset:
    </p>

    <div class="example-box">

      <p>
        2, 4, 6, 8, 10
      </p>

    </div>

    <p>
      There are five observations.
    </p>

    <p>
      The middle value is:
    </p>

    <div class="example-box">

      <p>
        6
      </p>

    </div>

    <p>
      Therefore,
      the median equals 6.
    </p>

    <h2>Another Odd-Sized Example</h2>

    <div class="example-box">

      <p>
        5, 7, 9, 11, 13, 15, 17
      </p>

    </div>

    <p>
      The fourth observation lies exactly in the middle.
    </p>

    <div class="example-box">

      <p>
        Median = 11
      </p>

    </div>

    <h2>Finding the Median: Even Number of Observations</h2>

    <p>
      Consider:
    </p>

    <div class="example-box">

      <p>
        2, 4, 6, 8, 10, 12
      </p>

    </div>

    <p>
      There is no single middle observation.
    </p>

    <p>
      Instead,
      we average the two middle values.
    </p>

    <div class="example-box">

      <p>
        Middle values: 6 and 8
      </p>

    </div>

    0

    <p>
      Therefore,
      the median is 7.
    </p>

    <h2>A General Procedure</h2>

    <p>
      To find the median:
    </p>

    <ol>

      <li>Order the observations.</li>

      <li>Determine whether the sample size is odd or even.</li>

      <li>If odd, select the middle observation.</li>

      <li>If even, average the two middle observations.</li>

    </ol>

    <p>
      This process works for any numerical dataset.
    </p>

    <h2>The Median as the 50th Percentile</h2>

    <p>
      The median has another important interpretation.
    </p>

    <p>
      It is the
      <strong>50th percentile</strong>.
    </p>

    <p>
      This means:
    </p>

    <ul class="bullets">

      <li>50% of observations lie below the median</li>

      <li>50% of observations lie above the median</li>

    </ul>

    <p>
      Percentiles will be studied in greater detail later.
    </p>

    <h2>The Median and Outliers</h2>

    <p>
      One of the median's greatest strengths is its resistance to extreme values.
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
      The median is:
    </p>

    <div class="example-box">

      <p>
        12
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
      The median remains:
    </p>

    <div class="example-box">

      <p>
        12
      </p>

    </div>

    <p>
      Even though one observation changed dramatically,
      the median did not change.
    </p>

    <h2>Comparing Mean and Median</h2>

    <p>
      Recall that the mean for:
    </p>

    <div class="example-box">

      <p>
        10, 11, 12, 13, 100
      </p>

    </div>

    <p>
      was:
    </p>

    <div class="example-box">

      <p>
        29.2
      </p>

    </div>

    <p>
      while the median remained:
    </p>

    <div class="example-box">

      <p>
        12
      </p>

    </div>

    <p>
      This illustrates why the median is often preferred for skewed data.
    </p>

    <h2>Resistance</h2>

    <p>
      A statistic that is not strongly affected by extreme observations
      is called
      <strong>resistant</strong>.
    </p>

    <p>
      The median is a resistant measure of center.
    </p>

    <p>
      The mean is not.
    </p>

    <div class="concept-box">

      <strong>Important idea:</strong>

      <p>
        The median is resistant to outliers,
        whereas the mean is sensitive to them.
      </p>

    </div>

    <h2>Median and Skewed Distributions</h2>

    <p>
      Many real-world datasets are skewed.
    </p>

    <p>
      Examples include:
    </p>

    <ul class="bullets">

      <li>Income</li>

      <li>Wealth</li>

      <li>House prices</li>

      <li>Medical expenses</li>

      <li>Insurance claims</li>

    </ul>

    <p>
      In these situations,
      the median often provides a better summary of a typical observation.
    </p>

    <h2>Why News Reports Often Use the Median</h2>

    <p>
      News organizations frequently report:
    </p>

    <ul class="bullets">

      <li>Median income</li>

      <li>Median house price</li>

      <li>Median rent</li>

    </ul>

    <p>
      This is because a small number of extremely large values
      can make means misleading.
    </p>

    <h2>When the Median Works Best</h2>

    <p>
      The median is especially useful when:
    </p>

    <ul class="bullets">

      <li>Outliers are present</li>

      <li>Distributions are skewed</li>

      <li>A resistant measure is desired</li>

      <li>The middle position is more important than exact magnitudes</li>

    </ul>

    <h2>When the Mean May Be Preferred</h2>

    <p>
      The mean still has advantages.
    </p>

    <p>
      It uses all observations and supports many advanced statistical methods.
    </p>

    <p>
      When distributions are roughly symmetric,
      the mean often performs very well.
    </p>

    <h2>Mean and Median Together</h2>

    <p>
      Statisticians frequently examine both measures.
    </p>

    <p>
      Comparing them can reveal information about distribution shape.
    </p>

    <ul class="bullets">

      <li>Mean ≈ Median often suggests symmetry</li>

      <li>Mean > Median often suggests right skewness</li>

      <li>Mean < Median often suggests left skewness</li>

    </ul>

    <p>
      This idea becomes important when studying distributions.
    </p>

    <h2>Applications of the Median</h2>

    <p>
      The median is widely used in:
    </p>

    <ul class="bullets">

      <li>Economics</li>

      <li>Public policy</li>

      <li>Housing markets</li>

      <li>Healthcare</li>

      <li>Business analytics</li>

    </ul>

    <p>
      It is one of the most trusted descriptive statistics.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>The median is the middle value of an ordered dataset</li>

        <li>For even sample sizes, the median is the average of the two middle values</li>

        <li>The median is the 50th percentile</li>

        <li>The median is resistant to outliers</li>

        <li>The median is often preferred for skewed distributions</li>

        <li>Mean and median provide different perspectives on center</li>

        <li>The median is widely used in real-world reporting and decision-making</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/descriptive/center/arithmetic-mean/">
         ← Previous: Arithmetic Mean
      </a>

      <a class="btn"
         href="/descriptive/center/mode/">
         Next: Mode →
      </a>

    </div>

  </div>

</section>