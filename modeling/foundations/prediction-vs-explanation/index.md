---
layout: default
title: Prediction vs Explanation
description: Learn the difference between predictive and explanatory modeling and why the purpose of a model influences how it is built, evaluated, and interpreted.
permalink: /modeling/foundations/prediction-vs-explanation/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_modeling_foundations_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/modeling/foundations/prediction-vs-explanation/",
    label: "Prediction vs Explanation",
    ts: Date.now()
  }));

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Modeling</span>
      <span class="badge">Block 1</span>
      <span class="badge">Foundations</span>
      <span class="badge">Model Goals</span>
    </div>

    <h1>Prediction vs Explanation</h1>

    <p class="lead">
      Not all statistical models are built for the same purpose.
    </p>

    <p class="lead">
      Some models are designed to explain relationships and generate understanding, while others are designed primarily to make accurate predictions.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/modeling/foundations/parameters/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/modeling/simple-linear-regression/">
         Continue to Simple Linear Regression →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>Why This Distinction Matters</h2>

    <p>
      Two models can analyze the same data yet pursue entirely different objectives.
    </p>

    <p>
      One model may focus on understanding why an outcome occurs.
    </p>

    <p>
      Another may focus only on accurately predicting future outcomes.
    </p>

    <div class="concept-box">

      <strong>Main idea:</strong>

      <p>
        Explanation seeks understanding, while prediction seeks accuracy.
      </p>

    </div>

    <h2>What Is Explanatory Modeling?</h2>

    <p>
      Explanatory models aim to understand relationships among variables.
    </p>

    <p>
      Analysts often ask questions such as:
    </p>

    <ul class="bullets">

      <li>Does education affect income?</li>

      <li>Does smoking affect health outcomes?</li>

      <li>Does advertising influence sales?</li>

      <li>Which factors drive customer satisfaction?</li>

    </ul>

    <p>
      The emphasis is on understanding mechanisms and relationships.
    </p>

    <h2>Goals of Explanation</h2>

    <p>
      Explanatory modeling typically focuses on:
    </p>

    <ul class="bullets">

      <li>Understanding relationships</li>

      <li>Estimating effects</li>

      <li>Testing theories</li>

      <li>Supporting scientific interpretation</li>

    </ul>

    <p>
      Interpretability is often extremely important.
    </p>

    <h2>What Is Predictive Modeling?</h2>

    <p>
      Predictive models focus on forecasting outcomes for new observations.
    </p>

    <p>
      Typical questions include:
    </p>

    <ul class="bullets">

      <li>What will tomorrow's sales be?</li>

      <li>Will a customer churn?</li>

      <li>What house price should we expect?</li>

      <li>Will a loan default?</li>

    </ul>

    <p>
      The primary objective is accurate prediction rather than explanation.
    </p>

    <h2>Goals of Prediction</h2>

    <p>
      Predictive modeling generally focuses on:
    </p>

    <ul class="bullets">

      <li>Forecast accuracy</li>

      <li>Generalization to new data</li>

      <li>Reducing prediction error</li>

      <li>Operational decision-making</li>

    </ul>

    <p>
      Understanding the underlying mechanism may be secondary.
    </p>

    <h2>A Simple Example</h2>

    <p>
      Imagine a company wants to understand employee turnover.
    </p>

    <p>
      An explanatory analysis might ask:
    </p>

    <div class="example-box">

      <p>
        Which workplace factors contribute to employee resignations?
      </p>
    </div>

    <p>
      A predictive analysis might ask:
    </p>

    <div class="example-box">

      <p>
        Which employees are most likely to resign next month?
      </p>
    </div>

    <p>
      Both questions involve the same outcome but different objectives.
    </p>

    <h2>Interpretability vs Accuracy</h2>

    <p>
      Explanation often values interpretability.
    </p>

    <p>
      Prediction often values accuracy.
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Priority</th>
            <th>Explanation</th>
            <th>Prediction</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Interpretability</td>
            <td>High</td>
            <td>May be less important</td>
          </tr>

          <tr>
            <td>Prediction Accuracy</td>
            <td>Important but secondary</td>
            <td>Primary objective</td>
          </tr>

          <tr>
            <td>Theory Testing</td>
            <td>Often central</td>
            <td>Often unnecessary</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>Different Models for Different Goals</h2>

    <p>
      The best explanatory model is not always the best predictive model.
    </p>

    <p>
      For example:
    </p>

    <ul class="bullets">

      <li>A simple model may be easy to interpret</li>

      <li>A more complex model may predict more accurately</li>

      <li>The preferred choice depends on the objective</li>

    </ul>

    <h2>Prediction Without Explanation</h2>

    <p>
      A model can make accurate predictions even when the underlying reasons are not fully understood.
    </p>

    <p>
      Many machine learning systems operate in this way.
    </p>

    <p>
      They may identify useful patterns without providing simple explanations.
    </p>

    <h2>Explanation Without Strong Prediction</h2>

    <p>
      Conversely, a model may reveal meaningful relationships while having only modest predictive performance.
    </p>

    <p>
      Scientific research often prioritizes understanding mechanisms rather than maximizing forecast accuracy.
    </p>

    <h2>The Role of Causality</h2>

    <p>
      Explanatory modeling frequently involves causal questions.
    </p>

    <p>
      Researchers may wish to determine whether changes in one variable actually influence another.
    </p>

    <p>
      Prediction alone does not establish causation.
    </p>

    <div class="concept-box">

      <strong>Important distinction:</strong>

      <p>
        A variable can improve prediction without being the cause of the outcome.
      </p>

    </div>

    <h2>Evaluating Explanatory Models</h2>

    <p>
      Explanatory models are often evaluated based on:
    </p>

    <ul class="bullets">

      <li>Interpretability</li>

      <li>Theoretical consistency</li>

      <li>Parameter estimates</li>

      <li>Statistical significance</li>

      <li>Scientific plausibility</li>

    </ul>

    <h2>Evaluating Predictive Models</h2>

    <p>
      Predictive models are often evaluated based on:
    </p>

    <ul class="bullets">

      <li>Prediction error</li>

      <li>Forecast accuracy</li>

      <li>Performance on unseen data</li>

      <li>Generalization ability</li>

    </ul>

    <p>
      The emphasis is on future performance rather than interpretation.
    </p>

    <h2>Can a Model Do Both?</h2>

    <p>
      Some models provide both explanatory insight and predictive value.
    </p>

    <p>
      However, there is often a trade-off.
    </p>

    <p>
      Improving one objective may sometimes reduce the other.
    </p>

    <h2>Why Purpose Comes First</h2>

    <p>
      Before building a model, analysts should ask:
    </p>

    <div class="example-box">

      <p>
        Are we trying to understand the world or predict the world?
      </p>
    </div>

    <p>
      The answer influences:
    </p>

    <ul class="bullets">

      <li>Variable selection</li>

      <li>Model complexity</li>

      <li>Evaluation metrics</li>

      <li>Interpretation strategy</li>

    </ul>

    <h2>Real-World Examples</h2>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Problem</th>
            <th>Primary Goal</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Testing a scientific theory</td>
            <td>Explanation</td>
          </tr>

          <tr>
            <td>Predicting loan defaults</td>
            <td>Prediction</td>
          </tr>

          <tr>
            <td>Studying disease mechanisms</td>
            <td>Explanation</td>
          </tr>

          <tr>
            <td>Forecasting product demand</td>
            <td>Prediction</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>The Bigger Picture</h2>

    <p>
      Statistical modeling serves multiple purposes.
    </p>

    <p>
      Some models help us understand relationships and mechanisms.
    </p>

    <p>
      Others help us forecast outcomes and make decisions.
    </p>

    <p>
      Recognizing the distinction between explanation and prediction helps ensure that models are built and evaluated appropriately.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        Explanatory models aim to understand relationships and mechanisms, while predictive models aim to forecast future outcomes accurately. The purpose of a model should guide how it is designed, interpreted, and evaluated.
      </p>

    </div>

    <h2>Completing the Foundations Block</h2>

    <p>
      You have now completed the Foundations block.
    </p>

    <p>
      This block introduced the core concepts underlying all statistical modeling, including models, variables, signal and noise, parameters, and the distinction between explanation and prediction.
    </p>

    <p>
      These ideas provide the conceptual framework needed for understanding more advanced modeling techniques.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Explanation focuses on understanding relationships and mechanisms</li>

        <li>Prediction focuses on forecasting future outcomes accurately</li>

        <li>The same data can support both explanatory and predictive analyses</li>

        <li>Interpretability is often more important for explanation</li>

        <li>Accuracy is often more important for prediction</li>

        <li>Prediction does not imply causation</li>

        <li>Different goals require different evaluation criteria</li>

        <li>The purpose of a model should guide its design and interpretation</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/modeling/foundations/parameters/">
         ← Previous: Parameters
      </a>

      <a class="btn"
         href="/modeling/simple-linear-regression/">
         Continue to Simple Linear Regression →
      </a>

    </div>

  </div>

</section>