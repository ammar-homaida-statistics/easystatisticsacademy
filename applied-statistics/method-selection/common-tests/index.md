---
layout: default
title: Common Tests
description: Learn the purpose of common statistical tests, when they are used, and how analysts match research questions to appropriate methods.
permalink: /applied-statistics/method-selection/common-tests/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_applied_statistics_method_selection_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/applied-statistics/method-selection/common-tests/",
    label: "Common Tests",
    ts: Date.now()
  }));

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Applied Statistics</span>
      <span class="badge">Block 1</span>
      <span class="badge">Method Selection</span>
      <span class="badge">Statistical Tests</span>
    </div>

    <h1>Common Tests</h1>

    <p class="lead">
      Once a research question and variable types have been identified, the next step is selecting an appropriate statistical method.
    </p>

    <p class="lead">
      Although hundreds of statistical techniques exist, a relatively small number of tests account for a large portion of practical analyses.
    </p>

    <p class="lead">
      Understanding these common methods provides a strong foundation for statistical decision-making.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/applied-statistics/method-selection/comparisons-vs-relationships/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/applied-statistics/method-selection/decision-framework/">
         Next: Decision Framework →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>Why Learn Common Tests?</h2>

    <p>
      Statistical software offers a large number of analytical options.
    </p>

    <p>
      For beginners, the challenge is often knowing where to start.
    </p>

    <p>
      Fortunately, many research questions fall into a handful of recurring patterns.
    </p>

    <p>
      These patterns are addressed by a relatively small set of commonly used methods.
    </p>

    <div class="concept-box">

      <strong>Main idea:</strong>

      <p>
        Most introductory statistical analyses can be approached using a small collection of widely used tests and modeling methods.
      </p>

    </div>

    <h2>Methods Are Tools</h2>

    <p>
      Statistical methods should be viewed as tools rather than goals.
    </p>

    <p>
      Different tools are designed for different types of questions.
    </p>

    <p>
      Choosing an appropriate method depends on:
    </p>

    <ul class="bullets">

      <li>The research question</li>

      <li>The variable types</li>

      <li>The study design</li>

      <li>The assumptions that can reasonably be made</li>

    </ul>

    <h2>The t-Test</h2>

    <p>
      One of the most common statistical tests is the t-test.
    </p>

    <p>
      It is typically used to compare the means of two groups.
    </p>

    <p>
      Example:
    </p>

    <div class="example-box">

      <p>
        Do students using Method A score differently than students using Method B?
      </p>
    </div>

    <p>
      Here the outcome is numerical and the grouping variable contains two categories.
    </p>

    <h2>ANOVA</h2>

    <p>
      Analysis of Variance (ANOVA) extends the comparison idea to more than two groups.
    </p>

    <p>
      Example:
    </p>

    <div class="example-box">

      <p>
        Do average incomes differ across four geographic regions?
      </p>
    </div>

    <p>
      ANOVA is often used when comparing multiple group means simultaneously.
    </p>

    <h2>Chi-Square Tests</h2>

    <p>
      Chi-square tests are commonly used when variables are categorical.
    </p>

    <p>
      Example:
    </p>

    <div class="example-box">

      <p>
        Is voting preference associated with age group?
      </p>
    </div>

    <p>
      These tests evaluate whether categorical variables appear related.
    </p>

    <h2>Correlation</h2>

    <p>
      Correlation measures the strength and direction of association between numerical variables.
    </p>

    <p>
      Example:
    </p>

    <div class="example-box">

      <p>
        Is study time related to exam performance?
      </p>
    </div>

    <p>
      Correlation focuses on relationships rather than group differences.
    </p>

    <h2>Regression</h2>

    <p>
      Regression extends relationship analysis by modeling how outcomes change as predictors change.
    </p>

    <p>
      Example:
    </p>

    <div class="example-box">

      <p>
        How much does income increase with each additional year of education?
      </p>
    </div>

    <p>
      Regression supports explanation, prediction, and adjustment for multiple variables.
    </p>

    <div class="concept-box">

      <strong>Key insight:</strong>

      <p>
        Correlation describes relationships, while regression models and explains them.
      </p>

    </div>

    <h2>Logistic Regression</h2>

    <p>
      When outcomes are binary rather than continuous, logistic regression is often appropriate.
    </p>

    <p>
      Example:
    </p>

    <div class="example-box">

      <p>
        Can age and blood pressure predict disease status?
      </p>
    </div>

    <p>
      Logistic regression models probabilities rather than continuous outcomes.
    </p>

    <h2>A Quick Overview</h2>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Method</th>
            <th>Typical Purpose</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>t-Test</td>
            <td>Compare two means</td>
          </tr>

          <tr>
            <td>ANOVA</td>
            <td>Compare multiple means</td>
          </tr>

          <tr>
            <td>Chi-Square Test</td>
            <td>Analyze categorical associations</td>
          </tr>

          <tr>
            <td>Correlation</td>
            <td>Measure relationships</td>
          </tr>

          <tr>
            <td>Regression</td>
            <td>Model numerical outcomes</td>
          </tr>

          <tr>
            <td>Logistic Regression</td>
            <td>Model binary outcomes</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>Matching Questions to Tests</h2>

    <p>
      Analysts often begin method selection by asking:
    </p>

    <ul class="bullets">

      <li>Am I comparing groups?</li>

      <li>Am I studying relationships?</li>

      <li>What types of variables are involved?</li>

    </ul>

    <p>
      These questions help narrow the list of possible methods.
    </p>

    <h2>Not Every Analysis Uses a Hypothesis Test</h2>

    <p>
      Statistical analysis is broader than hypothesis testing.
    </p>

    <p>
      Many projects focus on:
    </p>

    <ul class="bullets">

      <li>Description</li>

      <li>Prediction</li>

      <li>Visualization</li>

      <li>Estimation</li>

    </ul>

    <p>
      In these situations, formal significance tests may play a smaller role.
    </p>

    <h2>Assumptions Matter</h2>

    <p>
      Every method relies on assumptions.
    </p>

    <p>
      Examples include:
    </p>

    <ul class="bullets">

      <li>Independent observations</li>

      <li>Normality</li>

      <li>Equal variances</li>

      <li>Linear relationships</li>

    </ul>

    <p>
      Method selection should consider whether assumptions are reasonably satisfied.
    </p>

    <h2>Methods Can Be Related</h2>

    <p>
      Many statistical methods are connected.
    </p>

    <p>
      For example:
    </p>

    <ul class="bullets">

      <li>t-tests and ANOVA both compare means</li>

      <li>Correlation and regression both study relationships</li>

      <li>Linear and logistic regression belong to the broader GLM family</li>

    </ul>

    <p>
      Learning one method often makes related methods easier to understand.
    </p>

    <h2>Method Selection Is Often Iterative</h2>

    <p>
      Analysts do not always choose the perfect method immediately.
    </p>

    <p>
      Data exploration may reveal issues that require:
    </p>

    <ul class="bullets">

      <li>Alternative methods</li>

      <li>Transformations</li>

      <li>Robust procedures</li>

      <li>Different assumptions</li>

    </ul>

    <p>
      Method selection is often refined as analysis progresses.
    </p>

    <div class="concept-box">

      <strong>Important perspective:</strong>

      <p>
        The best statistical method is the one that appropriately answers the research question while respecting the structure of the data.
      </p>

    </div>

    <h2>Beyond Memorization</h2>

    <p>
      Effective analysts do not simply memorize lists of tests.
    </p>

    <p>
      Instead, they understand:
    </p>

    <ul class="bullets">

      <li>What question is being asked</li>

      <li>What variables are involved</li>

      <li>What assumptions apply</li>

      <li>What conclusions the method supports</li>

    </ul>

    <p>
      This deeper understanding improves method selection dramatically.
    </p>

    <h2>The Bigger Picture</h2>

    <p>
      Common statistical methods provide practical solutions to recurring analytical problems.
    </p>

    <p>
      By understanding what each method is designed to accomplish, analysts can move from research questions to appropriate analytical tools more confidently.
    </p>

    <p>
      Method selection becomes much easier when viewed as matching questions to tools.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        Common statistical methods such as t-tests, ANOVA, chi-square tests, correlation, and regression address recurring analytical situations. Choosing among them depends on the research question, variable types, and study design.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      Analysts often need a systematic way to move from research questions to statistical methods.
    </p>

    <p>
      Rather than memorizing tests individually, it can be helpful to use a structured decision process.
    </p>

    <p>
      The next lesson introduces a practical decision framework for selecting statistical methods based on variables, questions, and study goals.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>A small set of methods accounts for many common analyses</li>

        <li>t-tests compare two group means</li>

        <li>ANOVA compares means across multiple groups</li>

        <li>Chi-square tests analyze categorical associations</li>

        <li>Correlation measures relationships between numerical variables</li>

        <li>Regression models and explains relationships</li>

        <li>Logistic regression is used for binary outcomes</li>

        <li>Method selection depends on questions, variables, and assumptions</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/applied-statistics/method-selection/comparisons-vs-relationships/">
         ← Previous: Comparisons vs Relationships
      </a>

      <a class="btn"
         href="/applied-statistics/method-selection/decision-framework/">
         Next: Decision Framework →
      </a>

    </div>

  </div>

</section>