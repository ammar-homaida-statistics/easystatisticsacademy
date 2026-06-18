---
layout: default
title: Generalized Linear Models (GLMs)
description: Learn what Generalized Linear Models are, why they were developed, and how they unify many important statistical models within a single framework.
permalink: /modeling/extensions/glm/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_modeling_extensions_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/modeling/extensions/glm/",
    label: "Generalized Linear Models (GLMs)",
    ts: Date.now()
  }));

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Modeling</span>
      <span class="badge">Block 7</span>
      <span class="badge">Extensions</span>
      <span class="badge">GLMs</span>
    </div>

    <h1>Generalized Linear Models (GLMs)</h1>

    <p class="lead">
      Linear regression and logistic regression may seem like completely different techniques.
    </p>

    <p class="lead">
      In reality, both belong to a broader family called Generalized Linear Models (GLMs).
    </p>

    <p class="lead">
      GLMs provide a unified framework for modeling many different types of outcomes while preserving familiar regression ideas.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/modeling/extensions/interpreting-logistic-coefficients/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/modeling/extensions/link-functions/">
         Next: Link Functions →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>Why Were GLMs Developed?</h2>

    <p>
      Ordinary linear regression works well for continuous outcomes under certain assumptions.
    </p>

    <p>
      However, many real-world outcomes do not satisfy those assumptions.
    </p>

    <p>
      Examples include:
    </p>

    <ul class="bullets">

      <li>Binary outcomes</li>

      <li>Count outcomes</li>

      <li>Proportions</li>

      <li>Rates</li>

    </ul>

    <p>
      Researchers needed a framework that could accommodate different types of data while retaining the structure of regression analysis.
    </p>

    <div class="concept-box">

      <strong>Main idea:</strong>

      <p>
        Generalized Linear Models extend regression ideas so that many different outcome types can be modeled within a common framework.
      </p>

    </div>

    <h2>The Core Idea</h2>

    <p>
      GLMs preserve the central regression concept:
    </p>

    <div class="example-box">

      <p>
        Predict an outcome using one or more predictors.
      </p>
    </div>

    <p>
      What changes is how the outcome is connected to the predictors.
    </p>

    <p>
      Different outcome types require different probability distributions and transformations.
    </p>

    <h2>Three Components of a GLM</h2>

    <p>
      Every GLM contains three fundamental components:
    </p>

    <ol>

      <li>A random component</li>

      <li>A systematic component</li>

      <li>A link function</li>

    </ol>

    <p>
      Together these components define the model.
    </p>

    <h2>The Random Component</h2>

    <p>
      The random component specifies the probability distribution of the outcome variable.
    </p>

    <p>
      Different outcomes require different distributions.
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Outcome Type</th>
            <th>Common Distribution</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Continuous</td>
            <td>Normal</td>
          </tr>

          <tr>
            <td>Binary</td>
            <td>Binomial</td>
          </tr>

          <tr>
            <td>Counts</td>
            <td>Poisson</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>The Systematic Component</h2>

    <p>
      The systematic component is the familiar linear predictor:
    </p>

    

    <p>
      This part closely resembles ordinary regression.
    </p>

    <p>
      Predictors and coefficients are combined into a linear expression.
    </p>

    <h2>The Link Function</h2>

    <p>
      The link function connects the expected outcome to the linear predictor.
    </p>

    <p>
      It transforms the outcome scale into a form suitable for regression modeling.
    </p>

    <p>
      Different GLMs use different link functions.
    </p>

    <div class="concept-box">

      <strong>Key insight:</strong>

      <p>
        The link function is what allows the same regression framework to handle many different outcome types.
      </p>

    </div>

    <h2>Linear Regression as a GLM</h2>

    <p>
      Ordinary linear regression is actually a special case of a GLM.
    </p>

    <p>
      It uses:
    </p>

    <ul class="bullets">

      <li>Normal distribution</li>

      <li>Identity link function</li>

    </ul>

    <p>
      In this case, no transformation is required.
    </p>

    <p>
      The outcome is modeled directly.
    </p>

    <h2>Logistic Regression as a GLM</h2>

    <p>
      Logistic regression is another GLM.
    </p>

    <p>
      It uses:
    </p>

    <ul class="bullets">

      <li>Binomial distribution</li>

      <li>Logit link function</li>

    </ul>

    <p>
      The logit transformation allows probabilities to be modeled using a linear predictor.
    </p>

    <h2>Poisson Regression as a GLM</h2>

    <p>
      Poisson regression is used for count data.
    </p>

    <p>
      It uses:
    </p>

    <ul class="bullets">

      <li>Poisson distribution</li>

      <li>Log link function</li>

    </ul>

    <p>
      This combination is appropriate for nonnegative count outcomes.
    </p>

    <h2>A Unified Framework</h2>

    <p>
      One of the greatest strengths of GLMs is that they place many models under a single conceptual umbrella.
    </p>

    <p>
      Rather than learning completely unrelated methods, analysts learn variations of the same underlying framework.
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Model</th>
            <th>Distribution</th>
            <th>Link Function</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Linear Regression</td>
            <td>Normal</td>
            <td>Identity</td>
          </tr>

          <tr>
            <td>Logistic Regression</td>
            <td>Binomial</td>
            <td>Logit</td>
          </tr>

          <tr>
            <td>Poisson Regression</td>
            <td>Poisson</td>
            <td>Log</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>Why This Matters</h2>

    <p>
      Without GLMs, analysts would need entirely separate theories for different outcome types.
    </p>

    <p>
      GLMs show that many commonly used statistical models are variations of the same basic idea.
    </p>

    <p>
      This creates a more coherent understanding of statistical modeling.
    </p>

    <h2>Choosing the Right GLM</h2>

    <p>
      Model choice depends largely on the outcome variable.
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Outcome</th>
            <th>Common GLM</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Continuous measurement</td>
            <td>Linear regression</td>
          </tr>

          <tr>
            <td>Yes/No outcome</td>
            <td>Logistic regression</td>
          </tr>

          <tr>
            <td>Count data</td>
            <td>Poisson regression</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      Selecting an appropriate model begins with understanding the nature of the outcome.
    </p>

    <h2>GLMs Preserve Familiar Concepts</h2>

    <p>
      Despite their flexibility, GLMs still rely on familiar statistical ideas:
    </p>

    <ul class="bullets">

      <li>Predictors</li>

      <li>Coefficients</li>

      <li>Hypothesis testing</li>

      <li>Confidence intervals</li>

      <li>Model comparison</li>

    </ul>

    <p>
      The framework extends regression rather than replacing it.
    </p>

    <h2>GLMs in Practice</h2>

    <p>
      Generalized Linear Models are widely used throughout:
    </p>

    <ul class="bullets">

      <li>Medicine</li>

      <li>Public health</li>

      <li>Economics</li>

      <li>Social science</li>

      <li>Marketing</li>

      <li>Machine learning</li>

    </ul>

    <p>
      They form the foundation of many applied statistical analyses.
    </p>

    <div class="concept-box">

      <strong>Important perspective:</strong>

      <p>
        GLMs are powerful because they preserve the simplicity of regression while dramatically expanding the range of outcomes that can be modeled.
      </p>

    </div>

    <h2>The Bigger Picture</h2>

    <p>
      Generalized Linear Models provide a unifying framework that connects linear regression, logistic regression, Poisson regression, and many other techniques.
    </p>

    <p>
      By combining distributions, linear predictors, and link functions, GLMs allow analysts to model diverse types of data using a common conceptual structure.
    </p>

    <p>
      Understanding GLMs reveals the deeper connections between many statistical methods that initially appear unrelated.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        Generalized Linear Models extend regression ideas to different outcome types by combining an appropriate probability distribution, a linear predictor, and a link function. Many important statistical models are special cases of the GLM framework.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      One of the defining features of a GLM is the link function.
    </p>

    <p>
      Link functions connect outcomes to linear predictors and make it possible to model probabilities, counts, and other non-continuous outcomes.
    </p>

    <p>
      The next lesson explores link functions in greater detail and explains how they enable different types of generalized linear models.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>GLMs extend regression to many different outcome types</li>

        <li>Linear regression and logistic regression are both GLMs</li>

        <li>Every GLM contains a distribution, a linear predictor, and a link function</li>

        <li>Different outcomes require different probability distributions</li>

        <li>Link functions connect outcomes to linear predictors</li>

        <li>GLMs provide a unified framework for many statistical models</li>

        <li>Model selection often depends on the outcome type being analyzed</li>

        <li>GLMs preserve familiar regression concepts while increasing flexibility</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/modeling/extensions/interpreting-logistic-coefficients/">
         ← Previous: Interpreting Logistic Coefficients
      </a>

      <a class="btn"
         href="/modeling/extensions/link-functions/">
         Next: Link Functions →
      </a>

    </div>

  </div>

</section>