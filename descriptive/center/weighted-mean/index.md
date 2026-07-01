---
layout: default
title: Weighted Mean
description: Learn how weighted means account for observations with different levels of importance and why they are widely used in education, economics, finance, and statistics.
permalink: /descriptive/center/weighted-mean/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_descriptive_center_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/descriptive/center/weighted-mean/",
    label: "Weighted Mean",
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
      <span class="badge">Weighted Mean</span>
    </div>

    <h1>Weighted Mean</h1>

    <p class="lead">
      The arithmetic mean assumes every observation contributes equally to the final average.
    </p>

    <p class="lead">
      In many real-world situations,
      however,
      some observations are more important than others.
      The weighted mean accounts for these differences by assigning weights to observations.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/descriptive/center/mean-vs-median/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/descriptive/center/trimmed-mean/">
         Next: Trimmed Mean →
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

        <li>Explain why weighted means are used.</li>

        <li>Calculate a weighted mean using the appropriate formula.</li>

        <li>Interpret weighted averages in practical situations.</li>

        <li>Distinguish between arithmetic and weighted means.</li>

        <li>Recognize situations where weighting is appropriate.</li>

      </ul>

    </div>

  </div>

</section>

  <div class="content-narrow">

    <h2>Why Do We Need a Weighted Mean?</h2>

    <p>
      Consider a student whose course grade is determined by:
    </p>

    <ul class="bullets">

      <li>Homework: 20%</li>

      <li>Midterm Exam: 30%</li>

      <li>Final Exam: 50%</li>

    </ul>

    <p>
      These components do not contribute equally.
    </p>

    <p>
      The final exam is more important than the homework assignments.
    </p>

    <p>
      A simple arithmetic mean would ignore these differences.
    </p>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        A weighted mean gives different levels of importance to different observations.
      </p>

    </div>

    <h2>What Is a Weighted Mean?</h2>

    <p>
      A <strong>weighted mean</strong>
      is an average in which each observation is multiplied by a weight before averaging.
    </p>

    <p>
      Larger weights have a greater influence on the final result.
    </p>

    <p>
      Smaller weights have less influence.
    </p>

    <h2>The Formula</h2>

    <p>
      The weighted mean is calculated as:
    </p>

    <div class="formula-box">

\[
\bar{x}_w=\frac{\sum_{i=1}^{n}w_i x_i}{\sum_{i=1}^{n}w_i}
\]

</div>

    <p>
      where:
    </p>

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
            <td>xᵢ</td>
            <td>Observation value</td>
          </tr>

          <tr>
            <td>wᵢ</td>
            <td>Weight assigned to the observation</td>
          </tr>

          <tr>
            <td>Σ</td>
            <td>Summation symbol</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>How the Formula Works</h2>

    <p>
      The calculation involves two steps:
    </p>

    <ol>

      <li>Multiply each value by its weight.</li>

      <li>Divide the sum of weighted values by the sum of the weights.</li>

    </ol>

    <p>
      This ensures that observations with larger weights contribute more to the final average.
    </p>

    <h2>Example: Course Grades</h2>

    <img src="{{ 'descriptive/images/course-grade-weights.png' | relative_url }}"
     alt="Course components with different weights"
     style="margin-top:15px; max-width:100%; height:auto;">

<p>
The final examination contributes the largest share to the overall course grade.
</p>

    <p>
      Suppose a student receives:
    </p>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Component</th>
            <th>Score</th>
            <th>Weight</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>Homework</td>
            <td>90</td>
            <td>20%</td>
          </tr>

          <tr>
            <td>Midterm</td>
            <td>80</td>
            <td>30%</td>
          </tr>

          <tr>
            <td>Final Exam</td>
            <td>70</td>
            <td>50%</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      Calculate weighted contributions:
    </p>

    <div class="example-box">

      <p>
        (90 × 0.20) + (80 × 0.30) + (70 × 0.50)
      </p>
    </div>

    <div class="example-box">

      <p>
        18 + 24 + 35 = 77
      </p>

    </div>

    <p>
      Therefore:
    </p>

    <div class="example-box">

      <p>
        Weighted Mean = 77
      </p>

    </div>

    <h2>Comparison with the Arithmetic Mean</h2>

    <p>
      If we ignored the weights:
    </p>

    <div class="formula-box">

\[
\bar{x}=\frac{90+80+70}{3}=80
\]

</div>

    <p>
      The ordinary mean would be 80.
    </p>

    <p>
      The weighted mean is 77.
    </p>

    <p>
      The difference occurs because the lowest score received the largest weight.
    </p>

    <img src="{{ 'descriptive/images/arithmetic-vs-weighted-mean.png' | relative_url }}"
     alt="Comparison of arithmetic and weighted means"
     style="margin-top:15px; max-width:100%; height:auto;">

<p>
When observations have different importance, the weighted mean shifts toward the values with larger weights.
</p>

    <h2>When Are Weighted Means Used?</h2>

    <p>
      Weighted means appear frequently in practice.
    </p>

    <ul class="bullets">

      <li>Course grades</li>

      <li>Stock market indexes</li>

      <li>Economic indicators</li>

      <li>Survey analysis</li>

      <li>Performance evaluations</li>

      <li>Machine learning models</li>

    </ul>

    <h2>Example: Survey Data</h2>

    <p>
      Large surveys often use weights because some groups may be overrepresented or underrepresented in the sample.
    </p>

    <p>
      Weighting helps make survey results more representative of the target population.
    </p>

    <p>
      Modern polling frequently relies on weighted averages.
    </p>

    <h2>Example: Stock Market Indexes</h2>

    <p>
      In many stock indexes,
      large companies influence the index more than small companies.
    </p>

    <p>
      This is achieved through weighting.
    </p>

    <p>
      A company's size determines how much influence it has on the overall average.
    </p>

    <h2>Equal Weights Produce the Arithmetic Mean</h2>

    <img src="{{ 'descriptive/images/equal-weights-arithmetic-mean.png' | relative_url }}"
     alt="Equal weights produce the arithmetic mean"
     style="margin-top:15px; max-width:100%; height:auto;">

<p>
When every observation has the same weight, the weighted mean equals the arithmetic mean.
</p>

    <p>
      If every observation has the same weight,
      the weighted mean becomes the ordinary arithmetic mean.
    </p>

    <p>
      Therefore,
      the arithmetic mean can be viewed as a special case of the weighted mean.
    </p>

    <h2>Choosing Appropriate Weights</h2>

    <p>
      Weights should have a meaningful interpretation.
    </p>

    <p>
      They may represent:
    </p>

    <ul class="bullets">

      <li>Importance</li>

      <li>Frequency</li>

      <li>Population representation</li>

      <li>Reliability</li>

      <li>Sample size</li>

    </ul>

    <p>
      Arbitrary weights can produce misleading results.
    </p>

    <h2>Strengths of the Weighted Mean</h2>

    <ul class="bullets">

      <li>Accounts for unequal importance</li>

      <li>Provides realistic summaries</li>

      <li>Widely applicable</li>

      <li>Flexible and adaptable</li>

      <li>Uses all observations</li>

    </ul>

    <h2>Limitations of the Weighted Mean</h2>

    <ul class="bullets">

      <li>Requires appropriate weights</li>

      <li>Can be manipulated through weighting choices</li>

      <li>Sensitive to outliers</li>

      <li>May be harder to interpret than a simple mean</li>

    </ul>

    <h2>Weighted Means and Outliers</h2>

    <p>
      Like the arithmetic mean,
      the weighted mean uses every observation.
    </p>

    <p>
      Therefore,
      it is still sensitive to extreme values.
    </p>

    <p>
      An outlier with a large weight can have an especially strong influence on the result.
    </p>

    <h2>Interpreting a Weighted Mean</h2>

    <img src="{{ 'descriptive/images/large-weight-influence.png' | relative_url }}"
     alt="Influence of a large weight on the weighted mean"
     style="margin-top:15px; max-width:100%; height:auto;">

<p>
Observations with larger weights pull the weighted mean closer to their values.
</p>

    <p>
      A weighted mean should be interpreted as a balance point that reflects the assigned weights.
    </p>

    <p>
      Observations with larger weights pull the average toward themselves more strongly.
    </p>

    <p>
      The result represents a weighted center rather than a simple center.
    </p>

    <h2>Weighted Mean vs Mean</h2>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Arithmetic Mean</th>
            <th>Weighted Mean</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>Equal importance</td>
            <td>Unequal importance</td>
          </tr>

          <tr>
            <td>Simple average</td>
            <td>Weighted average</td>
          </tr>

          <tr>
            <td>All weights identical</td>
            <td>Weights may differ</td>
          </tr>

          <tr>
            <td>Simpler calculation</td>
            <td>More flexible calculation</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>Common Mistakes</h2>

<div class="warning-box">

  <ul class="bullets">

    <li>Using a simple mean when observations have different weights.</li>

    <li>Assigning arbitrary or incorrect weights.</li>

    <li>Forgetting to divide by the sum of the weights.</li>

    <li>Confusing percentages with decimal weights in calculations.</li>

    <li>Assuming a weighted mean is always more appropriate than an arithmetic mean.</li>

  </ul>

</div>

    <h2>Why Weighted Means Matter</h2>

    <p>
      Many important averages in business,
      economics,
      education,
      and science are actually weighted means.
    </p>

    <p>
      Understanding weighting helps explain how many reported statistics are produced.
    </p>

    <p>
      It is one of the most practical applications of measures of center.
    </p>

    <h2>Calculating a Weighted Mean in SPSS</h2>

<p>
SPSS can calculate weighted statistics after you specify a weighting variable.
Each case is then counted according to its assigned weight.
</p>

<div class="step-box">

  <h3>Using Case Weights</h3>

  <ol>

    <li>Select <strong>Data → Weight Cases...</strong>.</li>

    <li>Choose <strong>Weight cases by</strong>.</li>

    <li>Select the variable containing the weights.</li>

    <li>Click <strong>OK</strong>.</li>

    <li>Then choose <strong>Analyze → Descriptive Statistics → Descriptives</strong> (or another descriptive procedure) to calculate the weighted mean.</li>

  </ol>

</div>

<div class="tip-box">

<strong>Interpretation Tip:</strong>

<p>

Always verify that the weighting variable is appropriate before enabling case weights.
When you are finished, return to <strong>Data → Weight Cases...</strong> and select <strong>Do not weight cases</strong> to prevent weights from affecting later analyses unintentionally.

</p>

</div>

<h3>Python Example</h3>

<p>
This example calculates both the arithmetic mean and the weighted mean.
</p>

<pre><code>import numpy as np

scores = [90, 80, 70]
weights = [0.20, 0.30, 0.50]

print("Arithmetic Mean =", np.mean(scores))
print("Weighted Mean =", np.average(scores, weights=weights))
</code></pre>

<h3>R Example</h3>

<p>
This example compares the arithmetic mean and the weighted mean.
</p>

<pre><code>scores <- c(90, 80, 70)
weights <- c(0.20, 0.30, 0.50)

mean(scores)

weighted.mean(scores, weights)
</code></pre>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>A weighted mean allows observations to have different levels of importance</li>

        <li>The weighted mean multiplies values by their weights before averaging</li>

        <li>Equal weights produce the ordinary arithmetic mean</li>

        <li>Weighted means are common in grades, surveys, and economic statistics</li>

        <li>Weights should have meaningful interpretations</li>

        <li>The weighted mean remains sensitive to outliers</li>

        <li>Many real-world averages are weighted averages rather than simple averages</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/descriptive/center/mean-vs-median/">
         ← Previous: Mean vs Median
      </a>

      <a class="btn"
         href="/descriptive/center/trimmed-mean/">
         Next: Trimmed Mean →
      </a>

    </div>

  </div>

</section>
