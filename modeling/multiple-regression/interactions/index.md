---
layout: default
title: Interactions
description: Learn how interaction effects allow the relationship between a predictor and an outcome to depend on another predictor.
permalink: /modeling/multiple-regression/interactions/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_modeling_multiple_regression_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/modeling/multiple-regression/interactions/",
    label: "Interactions",
    ts: Date.now()
  }));

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Modeling</span>
      <span class="badge">Block 3</span>
      <span class="badge">Multiple Regression</span>
      <span class="badge">Interactions</span>
    </div>

    <h1>Interactions</h1>

    <p class="lead">
      Standard regression models assume that the effect of a predictor is constant across all observations.
    </p>

    <p class="lead">
      Interaction effects allow relationships to vary, making regression models flexible enough to capture more realistic patterns in data.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/modeling/multiple-regression/dummy-variables/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/modeling/multiple-regression/model-building/">
         Next: Model Building →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>Why Interactions Matter</h2>

    <p>
      Many relationships in the real world are not constant.
    </p>

    <p>
      The effect of one variable may depend on the value of another variable.
    </p>

    <p>
      For example, a training program might improve performance more for beginners than for experts.
    </p>

    <div class="concept-box">

      <strong>Main idea:</strong>

      <p>
        An interaction occurs when the effect of one predictor on the outcome depends on the value of another predictor.
      </p>

    </div>

    <h2>Main Effects vs Interaction Effects</h2>

    <p>
      Before introducing interactions, regression models contain only main effects.
    </p>

    <p>
      A main effect describes the average relationship between a predictor and the outcome.
    </p>

    <p>
      An interaction effect describes how that relationship changes across different situations.
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Effect Type</th>
            <th>Meaning</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Main Effect</td>
            <td>Average predictor-outcome relationship</td>
          </tr>

          <tr>
            <td>Interaction Effect</td>
            <td>Change in that relationship across conditions</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>A Study Hours Example</h2>

    <p>
      Suppose exam scores depend on:
    </p>

    <ul class="bullets">

      <li>Study hours</li>

      <li>Attendance rate</li>

    </ul>

    <p>
      A standard model assumes each additional study hour has the same effect regardless of attendance.
    </p>

    <p>
      However, study time might be more effective for students who attend class regularly.
    </p>

    <p>
      In that case, an interaction may exist.
    </p>

    <h2>The Idea Behind an Interaction Term</h2>

    <p>
      To model interactions, regression includes an additional predictor formed by multiplying two variables together.
    </p>

    <p>
      For predictors X₁ and X₂:
    </p>

    <div class="example-box">

      <p>
        Interaction = X₁ × X₂
      </p>
    </div>

    <p>
      This new variable allows the effect of one predictor to change as the other predictor changes.
    </p>

    <h2>The Interaction Model</h2>

    <p>
      A simple interaction model can be written as:
    </p>

    <div class="example-box">

      <p>
        y = β₀ + β₁X₁ + β₂X₂ + β₃(X₁X₂)
      </p>
    </div>

    <p>
      The coefficient β₃ represents the interaction effect.
    </p>

    <h2>Interpreting the Interaction Coefficient</h2>

    <p>
      The interaction coefficient describes how the effect of one predictor changes as another predictor changes.
    </p>

    <p>
      Unlike ordinary coefficients, interaction coefficients do not usually have a simple stand-alone interpretation.
    </p>

    <p>
      Instead, they modify the interpretation of the main effects.
    </p>

    <div class="concept-box">

      <strong>Key insight:</strong>

      <p>
        An interaction coefficient tells us whether the effect of one predictor depends on another predictor.
      </p>

    </div>

    <h2>Graphical Interpretation</h2>

    <p>
      Interactions are often easiest to understand visually.
    </p>

    <p>
      Without an interaction:
    </p>

    <ul class="bullets">

      <li>Regression lines remain parallel</li>

    </ul>

    <p>
      With an interaction:
    </p>

    <ul class="bullets">

      <li>Regression lines may diverge</li>

      <li>Regression lines may converge</li>

      <li>Regression lines may cross</li>

    </ul>

    <p>
      Nonparallel lines are often evidence of interaction effects.
    </p>

    <h2>Interactions with Dummy Variables</h2>

    <p>
      Interactions frequently involve categorical variables represented by dummy variables.
    </p>

    <p>
      Example:
    </p>

    <ul class="bullets">

      <li>Study Hours</li>

      <li>Treatment Group</li>

    </ul>

    <p>
      The interaction asks:
    </p>

    <div class="example-box">

      <p>
        Does the effect of study hours differ between groups?
      </p>
    </div>

    <p>
      This is one of the most common uses of interaction terms.
    </p>

    <h2>A Marketing Example</h2>

    <p>
      Suppose sales depend on:
    </p>

    <ul class="bullets">

      <li>Advertising spending</li>

      <li>Region</li>

    </ul>

    <p>
      The effectiveness of advertising may differ across regions.
    </p>

    <p>
      An interaction term allows the model to capture these differences.
    </p>

    <h2>When Interactions Are Important</h2>

    <p>
      Interactions are useful when theory or experience suggests that effects vary across situations.
    </p>

    <p>
      Common examples include:
    </p>

    <ul class="bullets">

      <li>Treatment effects varying by age</li>

      <li>Advertising effects varying by region</li>

      <li>Income effects varying by education level</li>

      <li>Exercise effects varying by health status</li>

    </ul>

    <p>
      Many scientific questions are fundamentally interaction questions.
    </p>

    <h2>When Interactions Are Unnecessary</h2>

    <p>
      Not every model requires interaction terms.
    </p>

    <p>
      Adding unnecessary interactions can:
    </p>

    <ul class="bullets">

      <li>Increase complexity</li>

      <li>Reduce interpretability</li>

      <li>Increase uncertainty</li>

      <li>Promote overfitting</li>

    </ul>

    <p>
      Interactions should generally be motivated by substantive reasoning or empirical evidence.
    </p>

    <h2>Main Effects Still Matter</h2>

    <p>
      Even when interactions are included, main effects usually remain part of the model.
    </p>

    <p>
      Removing main effects often makes interpretation difficult and can produce misleading results.
    </p>

    <p>
      Most interaction models include both the interaction term and the associated main effects.
    </p>

    <h2>Interactions Increase Model Flexibility</h2>

    <p>
      One reason interactions are valuable is that they allow regression models to move beyond simple additive relationships.
    </p>

    <p>
      Instead of assuming predictors operate independently, interactions allow predictors to influence one another's effects.
    </p>

    <p>
      This often produces more realistic models.
    </p>

    <h2>Interactions and Interpretation</h2>

    <p>
      Interaction models are often more difficult to interpret than ordinary regression models.
    </p>

    <p>
      Analysts frequently use:
    </p>

    <ul class="bullets">

      <li>Plots</li>

      <li>Predicted values</li>

      <li>Marginal effects</li>

      <li>Scenario comparisons</li>

    </ul>

    <p>
      to communicate interaction effects clearly.
    </p>

    <h2>The Bigger Picture</h2>

    <p>
      Multiple regression allows analysts to move beyond simple one-variable-at-a-time relationships.
    </p>

    <p>
      Interaction terms provide a framework for studying situations where effects change across groups, contexts, or conditions.
    </p>

    <p>
      This flexibility makes regression a powerful tool for understanding complex systems.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        An interaction effect occurs when the relationship between a predictor and an outcome depends on another predictor. Interaction terms allow regression models to capture these changing relationships and represent more realistic patterns in data.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      Building a regression model involves more than simply adding variables and interactions.
    </p>

    <p>
      Analysts must decide which predictors to include, how to balance complexity and interpretability, and how to evaluate model performance.
    </p>

    <p>
      The next lesson introduces model-building strategies and discusses how analysts construct useful regression models.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Interactions occur when one predictor's effect depends on another predictor</li>

        <li>Main effects describe average relationships, while interactions describe changing relationships</li>

        <li>Interaction terms are created by multiplying predictors together</li>

        <li>Interaction coefficients indicate whether effects vary across conditions</li>

        <li>Interactions are often visualized using nonparallel regression lines</li>

        <li>Dummy variables are commonly involved in interaction models</li>

        <li>Interactions increase model flexibility but also increase complexity</li>

        <li>Interaction terms help capture more realistic relationships in data</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/modeling/multiple-regression/dummy-variables/">
         ← Previous: Dummy Variables
      </a>

      <a class="btn"
         href="/modeling/multiple-regression/model-building/">
         Next: Model Building →
      </a>

    </div>

  </div>

</section>