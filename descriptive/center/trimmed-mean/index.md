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

<!-- LEARNING OBJECTIVES -->

<section class="section section-slim">

  <div class="content-narrow">

    <div class="objectives-box">

      <h2>Learning Objectives</h2>

      <p>By the end of this lesson, you should be able to:</p>

      <ul class="bullets">

        <li>Explain why trimmed means are used.</li>

        <li>Calculate a trimmed mean for a simple dataset.</li>

        <li>Describe how trimming reduces the influence of outliers.</li>

        <li>Compare the trimmed mean with the arithmetic mean and the median.</li>

        <li>Recognize situations where a trimmed mean is appropriate.</li>

      </ul>

    </div>

  </div>

</section>

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

    <div class="formula-box">

\[
\bar{x}=\frac{10+11+12+13+14+15+100}{7}
=\frac{175}{7}=25
\]

</div>

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

    <div class="formula-box">

\[
\bar{x}_{\text{trimmed}}
=
\frac{11+12+13+14+15}{5}
=
13
\]

</div>

    <p>
      This value better reflects where most observations are located.
    </p>

    <img src="{{ 'descriptive/images/trimmed-mean-example.png' | relative_url }}"
     alt="Dataset before and after trimming"
     style="margin-top:15px; max-width:100%; height:auto;">

<p>
The smallest and largest observations are removed before calculating the trimmed mean.
</p>

    <h2>How Much Data Should Be Trimmed?</h2>

    <img src="{{ 'descriptive/images/trimming-percentages.png' | relative_url }}"
     alt="Illustration of common trimming percentages"
     style="margin-top:15px; max-width:100%; height:auto;">

<p>
Common trimming levels remove equal percentages from both ends of the ordered data.
</p>

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

    <div class="concept-box">

<strong>Remember:</strong>

<p>

A statistic is considered <strong>robust</strong> if it continues to provide reliable results even when the data contain outliers or deviate from ideal assumptions.

</p>

</div>

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

    <img src="{{ 'descriptive/images/trimmed-mean-robustness.png' | relative_url }}"
     alt="Trimmed mean is less affected by an outlier"
     style="margin-top:15px; max-width:100%; height:auto;">

<p>
The trimmed mean is less influenced by extreme values than the arithmetic mean.
</p>

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

    <img src="{{ 'descriptive/images/mean-trimmed-median-comparison.png' | relative_url }}"
     alt="Comparison of mean, trimmed mean, and median"
     style="margin-top:15px; max-width:100%; height:auto;">

<p>
The trimmed mean usually falls between the arithmetic mean and the median when outliers are present.
</p>

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

    <h2>Common Mistakes</h2>

<div class="warning-box">

  <ul class="bullets">

    <li>Removing observations without first sorting the data.</li>

    <li>Using different trimming percentages for the lower and upper tails unless there is a justified reason.</li>

    <li>Trimming too many observations, which may discard valuable information.</li>

    <li>Confusing a trimmed mean with a winsorized mean.</li>

    <li>Assuming a trimmed mean completely eliminates the effect of unusual observations.</li>

  </ul>

</div>

<h2>Calculating a Trimmed Mean in SPSS</h2>

<p>
SPSS can compute trimmed means automatically as part of several descriptive procedures.
A common choice is the 5% trimmed mean, which removes the lowest and highest 5% of observations before calculating the average.
</p>

<div class="step-box">

  <h3>Using Explore</h3>

  <ol>

    <li>Select <strong>Analyze → Descriptive Statistics → Explore...</strong>.</li>

    <li>Move the numerical variable into the <strong>Dependent List</strong>.</li>

    <li>Click <strong>Statistics...</strong> if needed and ensure descriptive statistics are selected.</li>

    <li>Click <strong>OK</strong>.</li>

  </ol>

</div>

<div class="tip-box">

<strong>Interpretation Tip:</strong>

<p>

Compare the trimmed mean with the arithmetic mean. If the two values are very similar, outliers are unlikely to have much influence. A noticeable difference suggests that extreme observations may be affecting the ordinary mean.

</p>

</div>

<h3>Python Example</h3>

<p>
This example compares the arithmetic mean with a 10% trimmed mean.
</p>

<pre><code>from scipy.stats import trim_mean
import numpy as np

scores = [10,11,12,13,14,15,100]

print("Mean =", np.mean(scores))
print("20% Trimmed Mean =", trim_mean(scores, 0.20))
</code></pre>

<h3>R Example</h3>

<p>
This example compares the arithmetic mean with a trimmed mean.
</p>

<pre><code>scores <- c(10,11,12,13,14,15,100)

mean(scores)

mean(scores, trim = 1/7)
</code></pre>

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
