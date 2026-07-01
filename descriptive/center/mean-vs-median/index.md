---
layout: default
title: Mean vs Median
description: Learn the differences between the mean and median, when each measure should be used, and how distribution shape influences the choice.
permalink: /descriptive/center/mean-vs-median/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_descriptive_center_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/descriptive/center/mean-vs-median/",
    label: "Mean vs Median",
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
      <span class="badge">Comparison</span>
    </div>

    <h1>Mean vs Median</h1>

    <p class="lead">
      The mean and the median are the two most important measures of center in statistics.
    </p>

    <p class="lead">
      Both attempt to describe what is typical in a dataset,
      but they do so in different ways.
      Understanding when to use each one is a fundamental statistical skill.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/descriptive/center/mode/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/descriptive/center/weighted-mean/">
         Next: Weighted Mean →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<!-- LEARNING OBJECTIVES -->

<section class="section section-slim">

  <div class="content-narrow">

    <div class="objectives-box">

      <h2>Learning Objectives</h2>

      <p>By the end of this lesson, you should be able to:</p>

      <ul class="bullets">

        <li>Compare the arithmetic mean and the median.</li>

        <li>Explain why the two measures may differ.</li>

        <li>Recognize the effect of outliers on each measure.</li>

        <li>Choose the most appropriate measure based on the distribution.</li>

        <li>Use the relationship between the mean and median to describe skewness.</li>

      </ul>

    </div>

  </div>

</section>

<section class="section">

  <div class="content-narrow">

    <h2>Why Compare Them?</h2>

    <p>
      The mean and median often produce similar results,
      but not always.
    </p>

    <p>
      In some datasets the difference is small.
      In others the difference can be substantial.
    </p>

    <p>
      Choosing the wrong measure can create a misleading description of the data.
    </p>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        The mean uses all values, while the median uses only position.
      </p>

    </div>

    <h2>A Quick Review</h2>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Measure</th>
            <th>Definition</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>Mean</td>
            <td>Sum of observations divided by the number of observations</td>
          </tr>

          <tr>
            <td>Median</td>
            <td>Middle value of an ordered dataset</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      Both describe center,
      but they respond differently to unusual observations.
    </p>

    <h2>A Dataset Without Outliers</h2>

    <p>
      Consider:
    </p>

    <div class="example-box">

      <p>
        10, 12, 14, 16, 18
      </p>

    </div>

    <p>
      The mean is:
    </p>

    <div class="formula-box">

\[
\bar{x}=\frac{10+12+14+16+18}{5}=14
\]

</div>

    <p>
      The median is:
    </p>

    <div class="example-box">

      <p>
        14
      </p>

    </div>

    <p>
      Both measures produce the same result.
    </p>

    <img src="{{ 'descriptive/images/mean-equals-median.png' | relative_url }}"
     alt="Mean and median in a symmetric distribution"
     style="margin-top:15px; max-width:100%; height:auto;">

<p>
For symmetric data, the mean and median are usually the same or very close.
</p>

    <h2>Why They Often Agree</h2>

    <p>
      In symmetric distributions,
      observations are balanced around a central point.
    </p>

    <p>
      Because of this balance,
      the mean and median are often very close or identical.
    </p>

    <p>
      Many introductory examples are designed this way.
    </p>

    <h2>A Dataset With an Outlier</h2>

    <img src="{{ 'descriptive/images/outlier-pulls-mean.png' | relative_url }}"
     alt="Outlier affects the mean more than the median"
     style="margin-top:15px; max-width:100%; height:auto;">

<p>
The outlier shifts the mean toward the extreme value, while the median remains stable.
</p>

    <p>
      Now consider:
    </p>

    <div class="example-box">

      <p>
        10, 12, 14, 16, 100
      </p>

    </div>

    <p>
      The mean becomes:
    </p>

    <div class="formula-box">

\[
\bar{x}=\frac{10+12+14+16+100}{5}=30.4
\]

</div>

    <p>
      The median remains:
    </p>

    <div class="example-box">

      <p>
        14
      </p>

    </div>

    <p>
      The outlier pulls the mean upward,
      but the median is unchanged.
    </p>

    <h2>The Core Difference</h2>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Mean</th>
            <th>Median</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>Uses every observation</td>
            <td>Uses position only</td>
          </tr>

          <tr>
            <td>Sensitive to outliers</td>
            <td>Resistant to outliers</td>
          </tr>

          <tr>
            <td>Balance point</td>
            <td>Middle observation</td>
          </tr>

          <tr>
            <td>Affected by skewness</td>
            <td>Less affected by skewness</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>Resistance to Outliers</h2>

    <p>
      A statistic is called
      <strong>resistant</strong>
      if it is not strongly affected by extreme values.
    </p>

    <p>
      The median is resistant.
    </p>

    <p>
      The mean is not.
    </p>

    <p>
      This difference is one of the main reasons statisticians frequently prefer the median for skewed data.
    </p>

    <h2>Symmetric Distributions</h2>

    <p>
      For roughly symmetric distributions:
    </p>

    <ul class="bullets">

      <li>The mean performs very well</li>

      <li>The median performs very well</li>

      <li>The two measures are usually similar</li>

    </ul>

    <p>
      Either measure often provides a reasonable summary.
    </p>

    <h2>Right-Skewed Distributions</h2>

    <p>
      In right-skewed distributions,
      a small number of large observations create a long right tail.
    </p>

    <p>
      Examples include:
    </p>

    <ul class="bullets">

      <li>Income</li>

      <li>Wealth</li>

      <li>House prices</li>

      <li>Medical expenses</li>

    </ul>

    <p>
      In these cases:
    </p>

    <ul class="bullets">

      <li>Mean is usually greater than median</li>

      <li>Median often provides a more representative summary</li>

    </ul>

    <h2>Left-Skewed Distributions</h2>

    <p>
      In left-skewed distributions,
      a few unusually small values create a long left tail.
    </p>

    <p>
      In these cases:
    </p>

    <ul class="bullets">

      <li>Mean is usually smaller than median</li>

      <li>The median remains more resistant</li>

    </ul>

    <h2>Mean and Median as Indicators of Shape</h2>

    <img src="{{ 'descriptive/images/mean-median-skewness.png' | relative_url }}"
     alt="Relationship between the mean and median in different distribution shapes"
     style="margin-top:15px; max-width:100%; height:auto;">

<p>
The relative positions of the mean and median provide clues about distribution shape.
</p>

    <p>
      Comparing the two measures often reveals information about distribution shape.
    </p>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Relationship</th>
            <th>Possible Interpretation</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>Mean ≈ Median</td>
            <td>Approximately symmetric</td>
          </tr>

          <tr>
            <td>Mean > Median</td>
            <td>Right skewness</td>
          </tr>

          <tr>
            <td>Mean < Median</td>
            <td>Left skewness</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>Income: A Famous Example</h2>

    <img src="{{ 'descriptive/images/income-mean-vs-median.png' | relative_url }}"
     alt="Income distribution showing the difference between mean and median"
     style="margin-top:15px; max-width:100%; height:auto;">

<p>
A very high income increases the mean substantially, while the median remains closer to a typical income.
</p>

    <p>
      Suppose five people earn:
    </p>

    <div class="example-box">

      <p>
        $30,000, $35,000, $40,000, $45,000, $500,000
      </p>

    </div>

    <p>
      The mean income is heavily influenced by the very large salary.
    </p>

    <p>
      The median remains near the middle of the group.
    </p>

    <p>
      This is why economists often report median income instead of mean income.
    </p>

    <h2>When Should You Use the Mean?</h2>

    <p>
      The mean is usually preferred when:
    </p>

    <ul class="bullets">

      <li>The data are numerical</li>

      <li>The distribution is roughly symmetric</li>

      <li>Outliers are absent or unimportant</li>

      <li>Further statistical analysis is planned</li>

    </ul>

    <h2>When Should You Use the Median?</h2>

    <p>
      The median is usually preferred when:
    </p>

    <ul class="bullets">

      <li>The distribution is skewed</li>

      <li>Outliers are present</li>

      <li>A resistant measure is needed</li>

      <li>The goal is to describe a typical observation</li>

    </ul>

    <h2>Can One Be Better Than the Other?</h2>

    <img src="{{ 'descriptive/images/mean-vs-median-decision-guide.png' | relative_url }}"
     alt="Decision guide for choosing between the mean and median"
     style="margin-top:15px; max-width:100%; height:auto;">

    <p>
      Neither measure is universally better.
    </p>

    <p>
      The appropriate choice depends on the data and the purpose of the analysis.
    </p>

    <p>
      Skilled statisticians evaluate both the distribution and the research question before deciding.
    </p>

    <h2>Common Mistakes</h2>

<div class="warning-box">

  <ul class="bullets">

    <li>Assuming the mean is always the best measure of center.</li>

    <li>Ignoring the presence of outliers before choosing a measure.</li>

    <li>Using only one measure without examining the distribution.</li>

    <li>Thinking that the mean and median should always be equal.</li>

    <li>Interpreting a large difference between the mean and median without considering skewness or unusual observations.</li>

  </ul>

</div>

    <h2>Why This Comparison Matters</h2>

    <p>
      Many real-world misunderstandings occur because people report only one measure of center.
    </p>

    <p>
      Understanding the strengths and weaknesses of both measures leads to more accurate interpretations.
    </p>

    <p>
      Statistical thinking requires choosing the right summary rather than blindly applying formulas.
    </p>

    <h2>Comparing the Mean and Median in SPSS</h2>

<p>
SPSS can calculate both the mean and median in a single analysis, making it easy to compare these measures of center.
</p>

<div class="step-box">

  <h3>Using Frequencies</h3>

  <ol>

    <li>Select <strong>Analyze → Descriptive Statistics → Frequencies</strong>.</li>

    <li>Move the numerical variable into the <strong>Variable(s)</strong> box.</li>

    <li>Click <strong>Statistics...</strong>.</li>

    <li>Select both <strong>Mean</strong> and <strong>Median</strong>.</li>

    <li>Click <strong>Continue</strong>, then <strong>OK</strong>.</li>

  </ol>

</div>

<div class="tip-box">

<strong>Interpretation Tip:</strong>

<p>

If the mean and median are nearly equal, the distribution is often approximately symmetric.

If the mean is noticeably larger than the median, the distribution may be right-skewed.

If the mean is noticeably smaller than the median, the distribution may be left-skewed.

</p>

</div>

<h3>Python Example</h3>

<p>
This example compares the mean and median of an income dataset.
</p>

<pre><code>import statistics

income = [30000,35000,40000,45000,500000]

print("Mean =", statistics.mean(income))
print("Median =", statistics.median(income))
</code></pre>

<h3>R Example</h3>

<p>
This example compares the mean and median of an income dataset.
</p>

<pre><code>income <- c(30000,35000,40000,45000,500000)

mean(income)
median(income)
</code></pre>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Both the mean and median measure center</li>

        <li>The mean uses every observation</li>

        <li>The median uses positional information</li>

        <li>The mean is sensitive to outliers</li>

        <li>The median is resistant to outliers</li>

        <li>Mean and median often differ in skewed distributions</li>

        <li>The best choice depends on the data and the purpose of the analysis</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/descriptive/center/mode/">
         ← Previous: Mode
      </a>

      <a class="btn"
         href="/descriptive/center/weighted-mean/">
         Next: Weighted Mean →
      </a>

    </div>

  </div>

</section>
