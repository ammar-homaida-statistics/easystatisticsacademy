---
layout: default
title: What Are Assumptions?
description: Learn what statistical assumptions are, why they exist, and how they support the validity of statistical methods and conclusions.
permalink: /applied-statistics/assumptions/what-is-assumptions/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_applied_statistics_assumptions_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/applied-statistics/assumptions/what-is-assumptions/",
    label: "What Are Assumptions?",
    ts: Date.now()
  }));

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Applied Statistics</span>
      <span class="badge">Block 3</span>
      <span class="badge">Assumptions</span>
      <span class="badge">Foundations</span>
    </div>

    <h1>What Are Assumptions?</h1>

    <p class="lead">
      Every statistical method is built upon a set of assumptions about the data and how the data were generated.
    </p>

    <p class="lead">
      These assumptions help justify the mathematical procedures used in statistical analysis.
    </p>

    <p class="lead">
      Understanding assumptions is essential because the validity of statistical conclusions often depends on whether those assumptions are reasonably satisfied.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/applied-statistics/assumptions/">
         ← Block Home
      </a>

      <a class="btn btn-outline"
         href="/applied-statistics/assumptions/why-assumptions-matter/">
         Next: Why Assumptions Matter →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>Why Talk About Assumptions?</h2>

    <p>
      Statistical methods do not operate in a vacuum.
    </p>

    <p>
      Every test, model, and procedure relies on certain conditions being approximately true.
    </p>

    <p>
      These conditions are called assumptions.
    </p>

    <p>
      Without assumptions, statistical methods would have little theoretical basis for producing reliable results.
    </p>

    <div class="concept-box">

      <strong>Main idea:</strong>

      <p>
        Statistical assumptions are conditions that justify the use and interpretation of statistical methods.
      </p>

    </div>

    <h2>What Is an Assumption?</h2>

    <p>
      An assumption is a statement about how data behave or how they were generated.
    </p>

    <p>
      Statistical methods use these assumptions to derive formulas, calculate probabilities, and estimate uncertainty.
    </p>

    <p>
      Assumptions are not guaranteed truths; they are working conditions that help methods function appropriately.
    </p>

    <h2>A Simple Analogy</h2>

    <p>
      Imagine using a map to navigate a city.
    </p>

    <p>
      The map assumes roads are located where they are shown and that major routes are accessible.
    </p>

    <p>
      If those assumptions are badly violated, the map becomes less useful.
    </p>

    <p>
      Statistical methods work in a similar way.
    </p>

    <div class="example-box">

      <p>
        Methods rely on assumptions just as navigation relies on maps.
      </p>
    </div>

    <h2>Assumptions Are Everywhere</h2>

    <p>
      Assumptions appear throughout statistics.
    </p>

    <p>
      Examples include assumptions about:
    </p>

    <ul class="bullets">

      <li>Independence of observations</li>

      <li>Random sampling</li>

      <li>Normality</li>

      <li>Equal variability</li>

      <li>Linear relationships</li>

    </ul>

    <p>
      Different methods rely on different assumptions.
    </p>

    <h2>Why Methods Need Assumptions</h2>

    <p>
      Statistical procedures often use mathematical results that hold only under specific conditions.
    </p>

    <p>
      Assumptions provide those conditions.
    </p>

    <p>
      When assumptions are approximately satisfied, statistical methods tend to perform as expected.
    </p>

    <div class="concept-box">

      <strong>Key insight:</strong>

      <p>
        Assumptions are the foundation that connects statistical theory to practical data analysis.
      </p>

    </div>

    <h2>Assumptions Are Usually Approximate</h2>

    <p>
      A common misconception is that assumptions must be perfectly satisfied.
    </p>

    <p>
      In practice, assumptions are often evaluated as approximations.
    </p>

    <p>
      Many statistical methods remain useful even when assumptions are not perfectly met.
    </p>

    <p>
      What matters is whether violations are severe enough to affect conclusions.
    </p>

    <h2>Examples from Everyday Analysis</h2>

    <p>
      Consider a simple regression model.
    </p>

    <p>
      Common assumptions may include:
    </p>

    <ul class="bullets">

      <li>Independent observations</li>

      <li>Linear relationships</li>

      <li>Stable variance</li>

      <li>Reasonably well-behaved residuals</li>

    </ul>

    <p>
      These assumptions help justify estimation and inference procedures.
    </p>

    <h2>Different Methods, Different Assumptions</h2>

    <p>
      Not all methods require the same assumptions.
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Method</th>
            <th>Typical Assumptions</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>t-Test</td>
            <td>Normality, independence</td>
          </tr>

          <tr>
            <td>ANOVA</td>
            <td>Normality, equal variance</td>
          </tr>

          <tr>
            <td>Regression</td>
            <td>Linearity, independence, homoscedasticity</td>
          </tr>

          <tr>
            <td>Chi-Square Test</td>
            <td>Expected counts sufficiently large</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      Understanding assumptions helps analysts select appropriate methods.
    </p>

    <h2>Assumptions and Data Quality</h2>

    <p>
      Assumptions are closely connected to data quality.
    </p>

    <p>
      Problems such as:
    </p>

    <ul class="bullets">

      <li>Biased sampling</li>

      <li>Measurement errors</li>

      <li>Missing data</li>

      <li>Dependent observations</li>

    </ul>

    <p>
      may create assumption violations.
    </p>

    <p>
      Good study design helps support important assumptions.
    </p>

    <h2>Assumptions Are Not Obstacles</h2>

    <p>
      Beginners sometimes view assumptions as technical obstacles.
    </p>

    <p>
      A more useful perspective is that assumptions provide information about when methods work well and when caution is needed.
    </p>

    <p>
      They are tools for understanding the limits of statistical procedures.
    </p>

    <div class="concept-box">

      <strong>Important perspective:</strong>

      <p>
        Assumptions help analysts understand the strengths and limitations of statistical methods.
      </p>

    </div>

    <h2>Checking Assumptions</h2>

    <p>
      Because assumptions matter, analysts often evaluate them before interpreting results.
    </p>

    <p>
      Common approaches include:
    </p>

    <ul class="bullets">

      <li>Diagnostic plots</li>

      <li>Summary statistics</li>

      <li>Formal tests</li>

      <li>Subject-matter knowledge</li>

    </ul>

    <p>
      Assumption checking is an important part of applied statistics.
    </p>

    <h2>Assumptions and Robustness</h2>

    <p>
      Some methods are highly sensitive to assumption violations.
    </p>

    <p>
      Others are relatively robust and continue performing well despite moderate departures from ideal conditions.
    </p>

    <p>
      Understanding robustness helps analysts judge the seriousness of assumption violations.
    </p>

    <h2>Assumptions Guide Interpretation</h2>

    <p>
      Statistical results should always be interpreted in the context of underlying assumptions.
    </p>

    <p>
      Confidence intervals, p-values, and model estimates are meaningful only to the extent that the assumptions supporting them are reasonable.
    </p>

    <p>
      Ignoring assumptions can lead to misleading conclusions.
    </p>

    <div class="example-box">

      <p>
        Statistical conclusions are only as trustworthy as the assumptions that support them.
      </p>
    </div>

    <h2>The Bigger Picture</h2>

    <p>
      Assumptions are a fundamental part of statistical reasoning.
    </p>

    <p>
      They define the conditions under which statistical methods operate effectively and help analysts evaluate the credibility of their results.
    </p>

    <p>
      Understanding assumptions improves method selection, analysis, and interpretation.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        Statistical assumptions are conditions that support the use of statistical methods. They connect theory to practice and help determine whether conclusions are reliable and appropriately interpreted.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      Knowing that assumptions exist is only the first step.
    </p>

    <p>
      Analysts must also understand why assumptions matter and what can happen when they are violated.
    </p>

    <p>
      The next lesson explores the role assumptions play in statistical inference and explains why assumption checking is such an important part of data analysis.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Statistical methods rely on assumptions</li>

        <li>Assumptions describe conditions about data and data generation</li>

        <li>Different methods rely on different assumptions</li>

        <li>Assumptions connect statistical theory to practice</li>

        <li>Assumptions are often evaluated approximately rather than perfectly</li>

        <li>Assumption violations can affect statistical conclusions</li>

        <li>Assumptions help analysts understand method limitations</li>

        <li>Checking assumptions is an important part of applied statistics</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/applied-statistics/assumptions/">
         ← Back to Block Home
      </a>

      <a class="btn"
         href="/applied-statistics/assumptions/why-assumptions-matter/">
         Next: Why Assumptions Matter →
      </a>

    </div>

  </div>

</section>