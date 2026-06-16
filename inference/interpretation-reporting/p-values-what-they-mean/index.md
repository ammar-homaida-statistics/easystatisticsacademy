---
layout: default
title: P-Values: What They Mean
description: Learn what p-values measure, how they are interpreted in hypothesis testing, and the common misconceptions surrounding them.
permalink: /inference/interpretation-reporting/p-values-what-they-mean/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_inference_interpretation_reporting_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/inference/interpretation-reporting/p-values-what-they-mean/",
    label: "P-Values: What They Mean",
    ts: Date.now()
  }));

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Inference</span>
      <span class="badge">Block 6</span>
      <span class="badge">Interpretation & Reporting</span>
      <span class="badge">P-Values</span>
    </div>

    <h1>P-Values: What They Mean</h1>

    <p class="lead">
      The p-value is one of the most widely reported and widely misunderstood quantities in statistics.
    </p>

    <p class="lead">
      Understanding what a p-value actually measures—and what it does not measure—is essential for interpreting statistical results correctly.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/inference/interpretation-reporting/">
         ← Block Home
      </a>

      <a class="btn btn-outline"
         href="/inference/interpretation-reporting/statistical-vs-practical-significance/">
         Next: Statistical vs Practical Significance →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>Why P-Values Matter</h2>

    <p>
      Most classical hypothesis tests ultimately produce a p-value.
    </p>

    <p>
      Researchers often use that number to decide whether observed evidence is strong enough to reject a null hypothesis.
    </p>

    <p>
      Despite its importance, the p-value is frequently misinterpreted.
    </p>

    <div class="concept-box">

      <strong>Core challenge:</strong>

      <p>
        Many people know how to calculate a p-value but misunderstand what it actually represents.
      </p>

    </div>

    <h2>Recall the Hypothesis-Testing Framework</h2>

    <p>
      Hypothesis testing begins with:
    </p>

    <ul class="bullets">

      <li>Null hypothesis (H₀)</li>

      <li>Alternative hypothesis (Hₐ)</li>

      <li>Test statistic</li>

      <li>Sampling distribution</li>

    </ul>

    <p>
      The p-value summarizes how unusual the observed data would be if the null hypothesis were true.
    </p>

    <h2>The Formal Definition</h2>

    <div class="concept-box">

      <strong>Definition:</strong>

      <p>
        A p-value is the probability of obtaining results at least as extreme as those observed, assuming the null hypothesis is true.
      </p>

    </div>

    <p>
      The key phrase is:
    </p>

    <div class="example-box">

      <p>
        Assuming the null hypothesis is true.
      </p>
    </div>

    <h2>Interpreting Small P-Values</h2>

    <p>
      A small p-value means:
    </p>

    <div class="example-box">

      <p>
        The observed data would be unusual if H₀ were true.
      </p>
    </div>

    <p>
      Therefore, researchers may view the data as evidence against the null hypothesis.
    </p>

    <h2>Interpreting Large P-Values</h2>

    <p>
      A large p-value means:
    </p>

    <div class="example-box">

      <p>
        The observed data are reasonably consistent with H₀.
      </p>
    </div>

    <p>
      In that situation, there is insufficient evidence to reject the null hypothesis.
    </p>

    <h2>A Simple Example</h2>

    <p>
      Suppose a hypothesis test produces:
    </p>

    <div class="example-box">

      <p>
        p = 0.03
      </p>
    </div>

    <p>
      This means:
    </p>

    <p>
      If the null hypothesis were true, results at least as extreme as the observed data would occur about 3% of the time.
    </p>

    <p>
      Because this probability is relatively small, the evidence may be considered inconsistent with H₀.
    </p>

    <h2>The Decision Rule</h2>

    <p>
      Statistical decisions are often based on:
    </p>

    <div class="example-box">

      <p>
        Significance level α
      </p>
    </div>

    <p>
      The common rule is:
    </p>

    <ul class="bullets">

      <li>If p ≤ α, reject H₀</li>

      <li>If p > α, fail to reject H₀</li>

    </ul>

    <h2>A Common Threshold</h2>

    <p>
      Many studies use:
    </p>

    <div class="example-box">

      <p>
        α = 0.05
      </p>
    </div>

    <p>
      Although widely used, this threshold is a convention rather than a universal law.
    </p>

    <h2>What a P-Value Is NOT</h2>

    <p>
      One of the most important lessons in statistics is understanding what a p-value does not represent.
    </p>

    <h2>Misconception #1</h2>

    <div class="concept-box">

      <strong>Incorrect:</strong>

      <p>
        The p-value is the probability that the null hypothesis is true.
      </p>

    </div>

    <p>
      This interpretation is wrong.
    </p>

    <p>
      The p-value assumes H₀ is true; it does not calculate the probability that H₀ is true.
    </p>

    <h2>Misconception #2</h2>

    <div class="concept-box">

      <strong>Incorrect:</strong>

      <p>
        The p-value is the probability that the observed results occurred by chance.
      </p>

    </div>

    <p>
      This statement oversimplifies and often misrepresents the meaning of the p-value.
    </p>

    <p>
      The calculation specifically assumes the null hypothesis is true and evaluates the extremeness of the observed data.
    </p>

    <h2>Misconception #3</h2>

    <div class="concept-box">

      <strong>Incorrect:</strong>

      <p>
        A smaller p-value means a larger effect.
      </p>

    </div>

    <p>
      Effect size and p-values measure different things.
    </p>

    <p>
      Very small effects can produce extremely small p-values when sample sizes are large.
    </p>

    <h2>P-Values and Sample Size</h2>

    <p>
      Sample size strongly influences p-values.
    </p>

    <p>
      Large samples make it easier to detect even tiny effects.
    </p>

    <p>
      Consequently:
    </p>

    <div class="concept-box">

      <strong>Important:</strong>

      <p>
        Statistical significance does not automatically imply practical importance.
      </p>

    </div>

    <h2>P-Values and Effect Size</h2>

    <p>
      To understand a result fully, researchers should examine:
    </p>

    <ul class="bullets">

      <li>P-value</li>

      <li>Effect size</li>

      <li>Confidence interval</li>

    </ul>

    <p>
      Together these provide a more complete picture than a p-value alone.
    </p>

    <h2>Continuous Evidence</h2>

    <p>
      P-values are continuous measures of evidence.
    </p>

    <p>
      Consider:
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>P-Value</th>
            <th>General Interpretation</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>0.40</td>
            <td>Little evidence against H₀</td>
          </tr>

          <tr>
            <td>0.10</td>
            <td>Weak evidence against H₀</td>
          </tr>

          <tr>
            <td>0.03</td>
            <td>Moderate evidence against H₀</td>
          </tr>

          <tr>
            <td>0.001</td>
            <td>Strong evidence against H₀</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      Evidence changes gradually rather than abruptly.
    </p>

    <h2>The Problem with Bright Lines</h2>

    <p>
      Consider two studies:
    </p>

    <div class="example-box">

      <p>
        Study A: p = 0.049
      </p>

      <p>
        Study B: p = 0.051
      </p>

    </div>

    <p>
      These studies provide very similar evidence.
    </p>

    <p>
      Yet a strict significance threshold would classify one as "significant" and the other as "not significant."
    </p>

    <p>
      This illustrates why thoughtful interpretation is important.
    </p>

    <h2>P-Values and Replication</h2>

    <p>
      A statistically significant result does not guarantee that future studies will obtain the same outcome.
    </p>

    <p>
      Replication depends on:
    </p>

    <ul class="bullets">

      <li>Effect size</li>

      <li>Power</li>

      <li>Study quality</li>

      <li>Sampling variation</li>

    </ul>

    <h2>Modern Recommendations</h2>

    <p>
      Many statisticians recommend reporting:
    </p>

    <ul class="bullets">

      <li>P-values</li>

      <li>Confidence intervals</li>

      <li>Effect sizes</li>

      <li>Study limitations</li>

    </ul>

    <p>
      rather than relying solely on a significance threshold.
    </p>

    <h2>The Bigger Picture</h2>

    <p>
      P-values are useful tools for evaluating evidence against a null hypothesis.
    </p>

    <p>
      However, they do not measure effect size, practical importance, or the probability that a hypothesis is true.
    </p>

    <p>
      Proper interpretation requires combining p-values with other statistical information and subject-matter knowledge.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        A p-value measures how unusual the observed data would be if the null hypothesis were true. Small p-values provide evidence against H₀, but p-values alone are not sufficient for understanding the importance or size of an effect.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      Statistical significance is often confused with practical importance.
    </p>

    <p>
      A result can be statistically significant yet have little real-world impact, while an important effect may fail to reach significance in a small study.
    </p>

    <p>
      The next lesson explores the distinction between statistical significance and practical significance.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>A p-value measures how unusual the observed data would be if H₀ were true</li>

        <li>Small p-values provide evidence against the null hypothesis</li>

        <li>Large p-values indicate insufficient evidence to reject H₀</li>

        <li>P-values are not the probability that H₀ is true</li>

        <li>P-values do not measure effect size</li>

        <li>Sample size strongly influences p-values</li>

        <li>Statistical significance and practical importance are different concepts</li>

        <li>P-values should be interpreted alongside confidence intervals and effect sizes</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/inference/interpretation-reporting/">
         ← Back to Block Home
      </a>

      <a class="btn"
         href="/inference/interpretation-reporting/statistical-vs-practical-significance/">
         Next: Statistical vs Practical Significance →
      </a>

    </div>

  </div>

</section>