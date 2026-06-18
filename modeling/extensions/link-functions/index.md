---
layout: default
title: Link Functions
description: Learn what link functions are, why they are used in Generalized Linear Models, and how they connect different types of outcomes to regression models.
permalink: /modeling/extensions/link-functions/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_modeling_extensions_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/modeling/extensions/link-functions/",
    label: "Link Functions",
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

    <h1>Link Functions</h1>

    <p class="lead">
      One of the defining features of Generalized Linear Models is the use of a link function.
    </p>

    <p class="lead">
      Link functions allow regression methods to work with outcomes that are not naturally suited to ordinary linear regression.
    </p>

    <p class="lead">
      They create the connection between the outcome and the linear predictor.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/modeling/extensions/glm/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/modeling/extensions/comparing-linear-and-logistic/">
         Next: Comparing Linear and Logistic Regression →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>What Is a Link Function?</h2>

    <p>
      A link function is a mathematical transformation that connects the expected value of an outcome variable to a linear predictor.
    </p>

    <p>
      In simpler terms, it creates a bridge between:
    </p>

    <ul class="bullets">

      <li>The outcome being modeled</li>

      <li>The regression equation</li>

    </ul>

    <p>
      Without link functions, many important types of outcomes could not be modeled effectively using regression methods.
    </p>

    <div class="concept-box">

      <strong>Main idea:</strong>

      <p>
        A link function transforms an outcome into a form that can be modeled using a linear combination of predictors.
      </p>

    </div>

    <h2>Why Are Link Functions Needed?</h2>

    <p>
      Ordinary linear regression assumes outcomes can vary freely across the entire number line.
    </p>

    <p>
      Many outcomes do not behave this way.
    </p>

    <p>
      Examples include:
    </p>

    <ul class="bullets">

      <li>Probabilities (restricted to 0–1)</li>

      <li>Counts (cannot be negative)</li>

      <li>Rates and proportions</li>

    </ul>

    <p>
      Link functions solve this problem by transforming outcomes onto a scale that is compatible with linear modeling.
    </p>

    <h2>The General Structure</h2>

    <p>
      In a GLM, the link function connects the expected outcome to the linear predictor:
    </p>

    <div class="example-box">

      <p>
        Link(Expected Outcome) = Linear Predictor
      </p>
    </div>

    <p>
      The linear predictor remains familiar:
    </p>

    0

    <p>
      The link function determines how the outcome is connected to that predictor.
    </p>

    <h2>The Identity Link</h2>

    <p>
      Linear regression uses the identity link.
    </p>

    <p>
      The transformation does nothing:
    </p>

    <div class="example-box">

      <p>
        Outcome = Linear Predictor
      </p>
    </div>

    <p>
      This works because continuous outcomes can take a wide range of values.
    </p>

    <h2>The Logit Link</h2>

    <p>
      Logistic regression uses the logit link.
    </p>

    <p>
      The logit transforms probabilities into log-odds.
    </p>

    <p>
      This converts values restricted to 0–1 into values that can range from negative infinity to positive infinity.
    </p>

    <p>
      As a result, probabilities can be modeled using a linear predictor.
    </p>

    <div class="concept-box">

      <strong>Key insight:</strong>

      <p>
        The logit link allows logistic regression to model probabilities while ensuring predicted values remain between 0 and 1.
      </p>

    </div>

    <h2>The Log Link</h2>

    <p>
      Poisson regression commonly uses the log link.
    </p>

    <p>
      Count outcomes cannot be negative.
    </p>

    <p>
      The logarithm transforms positive values onto a scale suitable for linear modeling.
    </p>

    <p>
      This guarantees nonnegative predicted counts.
    </p>

    <h2>Common Link Functions</h2>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Model</th>
            <th>Link Function</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Linear Regression</td>
            <td>Identity</td>
          </tr>

          <tr>
            <td>Logistic Regression</td>
            <td>Logit</td>
          </tr>

          <tr>
            <td>Poisson Regression</td>
            <td>Log</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>What Makes a Good Link Function?</h2>

    <p>
      A useful link function should:
    </p>

    <ul class="bullets">

      <li>Respect the outcome's natural range</li>

      <li>Allow linear modeling</li>

      <li>Produce meaningful predictions</li>

      <li>Be mathematically stable</li>

    </ul>

    <p>
      Different outcome types require different transformations.
    </p>

    <h2>An Intuitive Analogy</h2>

    <p>
      Imagine trying to fit different-shaped objects through the same doorway.
    </p>

    <p>
      A link function acts like an adapter that reshapes each object so it can pass through the doorway.
    </p>

    <p>
      The doorway represents the linear predictor, while the adapter represents the transformation.
    </p>

    <h2>Link Functions Preserve Regression Structure</h2>

    <p>
      One reason GLMs are powerful is that they preserve familiar regression ideas.
    </p>

    <p>
      Regardless of the outcome type, analysts still work with:
    </p>

    <ul class="bullets">

      <li>Predictors</li>

      <li>Coefficients</li>

      <li>Model fitting</li>

      <li>Hypothesis testing</li>

    </ul>

    <p>
      The link function simply modifies how outcomes connect to the regression equation.
    </p>

    <h2>Different Links, Different Interpretations</h2>

    <p>
      Because link functions transform outcomes, coefficient interpretation depends on the chosen link.
    </p>

    <p>
      For example:
    </p>

    <ul class="bullets">

      <li>Linear regression coefficients describe changes in the outcome</li>

      <li>Logistic regression coefficients describe changes in log-odds</li>

      <li>Poisson regression coefficients describe changes in log-counts</li>

    </ul>

    <p>
      The link function therefore influences interpretation.
    </p>

    <h2>Why Analysts Should Care</h2>

    <p>
      Analysts do not always need to derive link functions mathematically.
    </p>

    <p>
      However, understanding their purpose helps explain:
    </p>

    <ul class="bullets">

      <li>Why different GLMs exist</li>

      <li>Why coefficients are interpreted differently</li>

      <li>Why predictions remain valid for different outcome types</li>

    </ul>

    <p>
      Link functions are one of the key ideas underlying modern regression modeling.
    </p>

    <div class="concept-box">

      <strong>Important perspective:</strong>

      <p>
        Different regression models often look different on the surface, but many of their differences arise simply because they use different link functions.
      </p>

    </div>

    <h2>How Link Functions Enable Flexibility</h2>

    <p>
      By choosing an appropriate link function and probability distribution, GLMs can handle:
    </p>

    <ul class="bullets">

      <li>Continuous outcomes</li>

      <li>Binary outcomes</li>

      <li>Counts</li>

      <li>Rates</li>

      <li>Proportions</li>

    </ul>

    <p>
      This flexibility is one reason GLMs are so widely used.
    </p>

    <h2>The Bigger Picture</h2>

    <p>
      Link functions are the mechanism that allows generalized linear models to extend beyond ordinary regression.
    </p>

    <p>
      They transform outcomes into a scale that can be modeled linearly while respecting the natural constraints of the data.
    </p>

    <p>
      Understanding link functions helps reveal the common structure underlying many different statistical models.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        A link function connects an outcome variable to a linear predictor. By transforming outcomes appropriately, link functions allow regression methods to handle probabilities, counts, and many other types of data within the GLM framework.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      Linear regression and logistic regression are closely related, yet they differ in important ways.
    </p>

    <p>
      Comparing them side by side helps clarify how outcome type, link functions, interpretation, and prediction change across models.
    </p>

    <p>
      The next lesson directly compares linear and logistic regression and highlights their similarities and differences.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Link functions connect outcomes to linear predictors</li>

        <li>They allow regression methods to handle restricted outcome ranges</li>

        <li>Linear regression uses the identity link</li>

        <li>Logistic regression uses the logit link</li>

        <li>Poisson regression commonly uses the log link</li>

        <li>Link functions influence coefficient interpretation</li>

        <li>Different outcome types require different link functions</li>

        <li>Link functions are a central component of Generalized Linear Models</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/modeling/extensions/glm/">
         ← Previous: Generalized Linear Models
      </a>

      <a class="btn"
         href="/modeling/extensions/comparing-linear-and-logistic/">
         Next: Comparing Linear and Logistic Regression →
      </a>

    </div>

  </div>

</section>