---
layout: default
title: Model Assumptions vs Design Assumptions
description: Learn the difference between model assumptions and design assumptions, and why both influence the validity of statistical conclusions.
permalink: /inference/assumptions-robustness/model-assumptions-vs-design-assumptions/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_inference_assumptions_robustness_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/inference/assumptions-robustness/model-assumptions-vs-design-assumptions/",
    label: "Model Assumptions vs Design Assumptions",
    ts: Date.now()
  }));

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Inference</span>
      <span class="badge">Block 7</span>
      <span class="badge">Assumptions & Robustness</span>
      <span class="badge">Foundations</span>
    </div>

    <h1>Model Assumptions vs Design Assumptions</h1>

    <p class="lead">
      Not all assumptions in statistics come from the same place.
    </p>

    <p class="lead">
      Some assumptions concern the mathematical model used for analysis, while others concern how data were collected. Understanding the distinction is essential for valid inference.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/inference/assumptions-robustness/assumptions-vs-robustness-mindset/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/inference/assumptions-robustness/checking-normality-what-and-why/">
         Next: Checking Normality: What and Why →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>Two Sources of Assumptions</h2>

    <p>
      Statistical methods rely on assumptions, but those assumptions arise from two different sources.
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Type</th>
            <th>Main Question</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Design Assumptions</td>
            <td>How were the data collected?</td>
          </tr>

          <tr>
            <td>Model Assumptions</td>
            <td>How are the data represented mathematically?</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      Both types influence the quality of statistical conclusions.
    </p>

    <h2>What Are Design Assumptions?</h2>

    <p>
      Design assumptions concern the process used to obtain data.
    </p>

    <p>
      They focus on whether observations provide a trustworthy representation of the population or phenomenon being studied.
    </p>

    <div class="concept-box">

      <strong>Definition:</strong>

      <p>
        Design assumptions describe how observations enter the dataset and whether the sampling or experimental process supports valid inference.
      </p>

    </div>

    <h2>Common Design Assumptions</h2>

    <p>
      Examples include:
    </p>

    <ul class="bullets">

      <li>Random sampling</li>

      <li>Random assignment</li>

      <li>Representative observations</li>

      <li>Independent selection of units</li>

      <li>Minimal nonresponse bias</li>

    </ul>

    <p>
      These assumptions are primarily about data collection rather than mathematics.
    </p>

    <h2>Why Design Assumptions Matter</h2>

    <p>
      Even a mathematically perfect model cannot rescue poor data collection.
    </p>

    <p>
      If a sample is badly biased:
    </p>

    <ul class="bullets">

      <li>Estimates may be misleading</li>

      <li>Confidence intervals may be irrelevant</li>

      <li>Hypothesis tests may answer the wrong question</li>

    </ul>

    <h2>An Example of Design Failure</h2>

    <p>
      Suppose a survey is conducted only through a social-media platform.
    </p>

    <p>
      Even if the statistical calculations are flawless:
    </p>

    <div class="example-box">

      <p>
        The sample may not represent the target population.
      </p>
    </div>

    <p>
      The problem arises before any analysis begins.
    </p>

    <h2>What Are Model Assumptions?</h2>

    <p>
      Model assumptions concern the mathematical framework used to analyze data.
    </p>

    <p>
      They specify how variables, errors, and probabilities behave within a statistical procedure.
    </p>

    <div class="concept-box">

      <strong>Definition:</strong>

      <p>
        Model assumptions describe the probabilistic structure that allows statistical formulas and theoretical results to work.
      </p>

    </div>

    <h2>Common Model Assumptions</h2>

    <p>
      Examples include:
    </p>

    <ul class="bullets">

      <li>Normality</li>

      <li>Equal variances</li>

      <li>Linearity</li>

      <li>Independent errors</li>

      <li>Specified probability distributions</li>

    </ul>

    <p>
      These assumptions appear inside statistical models and methods.
    </p>

    <h2>An Example of a Model Assumption</h2>

    <p>
      A classical t-test assumes that observations come from populations that are approximately normal, particularly for small sample sizes.
    </p>

    <p>
      This assumption affects the accuracy of the test procedure itself.
    </p>

    <h2>The Key Difference</h2>

    <p>
      Design assumptions concern:
    </p>

    <div class="example-box">

      <p>
        Whether the data are trustworthy.
      </p>
    </div>

    <p>
      Model assumptions concern:
    </p>

    <div class="example-box">

      <p>
        Whether the mathematical analysis is appropriate.
      </p>
    </div>

    <h2>Which Type Is More Important?</h2>

    <p>
      Both matter, but design assumptions are often more fundamental.
    </p>

    <p>
      A strong design can sometimes tolerate imperfect models.
    </p>

    <p>
      A weak design can undermine even sophisticated analyses.
    </p>

    <div class="concept-box">

      <strong>Important principle:</strong>

      <p>
        Good modeling cannot fully compensate for poor study design.
      </p>

    </div>

    <h2>Design Before Analysis</h2>

    <p>
      Statistical inference begins long before calculations.
    </p>

    <p>
      Questions about:
    </p>

    <ul class="bullets">

      <li>Who was sampled?</li>

      <li>How were units selected?</li>

      <li>How were treatments assigned?</li>

      <li>Who did not respond?</li>

    </ul>

    <p>
      often have greater consequences than model details.
    </p>

    <h2>A Comparison</h2>

    

    <p>
      Both contribute to valid inference, but failures in study design often have broader consequences.
    </p>

    <h2>Can Model Assumptions Be Checked?</h2>

    <p>
      Often, yes.
    </p>

    <p>
      Analysts may inspect:
    </p>

    <ul class="bullets">

      <li>Residual plots</li>

      <li>Histograms</li>

      <li>QQ plots</li>

      <li>Variance diagnostics</li>

    </ul>

    <p>
      These tools help evaluate whether assumptions appear reasonable.
    </p>

    <h2>Can Design Assumptions Be Checked?</h2>

    <p>
      Usually, only partially.
    </p>

    <p>
      For example, we may know:
    </p>

    <ul class="bullets">

      <li>How sampling occurred</li>

      <li>How randomization was performed</li>

      <li>Response rates</li>

    </ul>

    <p>
      But some biases may remain difficult to measure directly.
    </p>

    <h2>Why the Distinction Matters</h2>

    <p>
      Analysts sometimes focus heavily on model diagnostics while ignoring design weaknesses.
    </p>

    <p>
      This can create false confidence in conclusions.
    </p>

    <p>
      Strong inference requires attention to both types of assumptions.
    </p>

    <h2>A Practical Example</h2>

    <p>
      Imagine two studies:
    </p>

    <ul class="bullets">

      <li>Study A has excellent random sampling but mildly non-normal data.</li>

      <li>Study B has perfect normality but severe selection bias.</li>

    </ul>

    <p>
      In many situations, Study A may produce more trustworthy conclusions because the design problem in Study B affects representativeness.
    </p>

    <h2>The Robustness Perspective</h2>

    <p>
      Robustness applies differently to the two types of assumptions.
    </p>

    <ul class="bullets">

      <li>Many methods are robust to mild model-assumption violations.</li>

      <li>Few methods are robust to severe design flaws.</li>

    </ul>

    <p>
      This distinction is one reason design quality is often emphasized in statistical practice.
    </p>

    <h2>The Bigger Picture</h2>

    <p>
      Statistical validity depends on both how data are collected and how they are analyzed.
    </p>

    <p>
      Design assumptions determine whether data support meaningful inference.
    </p>

    <p>
      Model assumptions determine whether analytical procedures operate as intended.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        Design assumptions concern the quality of data collection, while model assumptions concern the mathematical structure of analysis. Sound statistical conclusions require attention to both.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      One of the most frequently discussed model assumptions is normality.
    </p>

    <p>
      Many classical methods refer to normal distributions, yet the importance of normality is often misunderstood.
    </p>

    <p>
      The next lesson examines what normality means, why it matters, and when departures from normality become a concern.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Statistical assumptions come from both study design and mathematical models</li>

        <li>Design assumptions concern how data are collected</li>

        <li>Model assumptions concern how data are analyzed</li>

        <li>Random sampling and random assignment are design assumptions</li>

        <li>Normality and equal variances are model assumptions</li>

        <li>Strong models cannot fully correct weak study designs</li>

        <li>Model assumptions are often easier to diagnose than design assumptions</li>

        <li>Reliable inference requires attention to both types of assumptions</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/inference/assumptions-robustness/assumptions-vs-robustness-mindset/">
         ← Previous: Assumptions vs Robustness Mindset
      </a>

      <a class="btn"
         href="/inference/assumptions-robustness/checking-normality-what-and-why/">
         Next: Checking Normality: What and Why →
      </a>

    </div>

  </div>

</section>