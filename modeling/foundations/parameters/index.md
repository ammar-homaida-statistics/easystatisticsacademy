---
layout: default
title: Parameters
description: Learn what parameters are, how they describe models, and why estimating unknown parameters is one of the central goals of statistical modeling.
permalink: /modeling/foundations/parameters/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_modeling_foundations_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/modeling/foundations/parameters/",
    label: "Parameters",
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
      <span class="badge">Parameters</span>
    </div>

    <h1>Parameters</h1>

    <p class="lead">
      Models use parameters to describe important characteristics of relationships, populations, and processes.
    </p>

    <p class="lead">
      Estimating unknown parameters from data is one of the most important goals of statistical modeling.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/modeling/foundations/signal-noise/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/modeling/foundations/prediction-vs-explanation/">
         Next: Prediction vs Explanation →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>What Is a Parameter?</h2>

    <p>
      A parameter is a numerical quantity that describes some aspect of a population, process, or statistical model.
    </p>

    <p>
      Parameters determine how a model behaves and what relationships it represents.
    </p>

    <div class="concept-box">

      <strong>Definition:</strong>

      <p>
        A parameter is a fixed but usually unknown numerical value that characterizes a population or model.
      </p>

    </div>

    <h2>Why Parameters Matter</h2>

    <p>
      Statistical models use parameters to summarize important features of reality.
    </p>

    <p>
      Examples include:
    </p>

    <ul class="bullets">

      <li>Population means</li>

      <li>Population proportions</li>

      <li>Regression slopes</li>

      <li>Correlations</li>

      <li>Variances</li>

    </ul>

    <p>
      Learning about these quantities helps us understand the systems being studied.
    </p>

    <h2>A Familiar Example</h2>

    <p>
      Consider a population of all adults in a country.
    </p>

    <p>
      The true average height of that population is a parameter.
    </p>

    <p>
      Although the value exists, it is usually unknown because measuring every individual is impractical.
    </p>

    <h2>Parameters vs Statistics</h2>

    <p>
      Parameters and statistics are closely related but fundamentally different.
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Quantity</th>
            <th>Describes</th>
            <th>Known?</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Parameter</td>
            <td>Population</td>
            <td>Usually unknown</td>
          </tr>

          <tr>
            <td>Statistic</td>
            <td>Sample</td>
            <td>Known once calculated</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      Statistics are often used to estimate parameters.
    </p>

    <h2>An Example of Estimation</h2>

    <p>
      Suppose the true population mean income is unknown.
    </p>

    <p>
      We collect a sample and compute the sample mean.
    </p>

    <p>
      The sample mean is a statistic that serves as an estimate of the population-mean parameter.
    </p>

    <div class="example-box">

      <p>
        Parameter → Unknown population value
      </p>

      <p>
        Statistic → Sample-based estimate
      </p>

    </div>

    <h2>Parameters in Models</h2>

    <p>
      Parameters are not limited to populations.
    </p>

    <p>
      They also define the structure of statistical models.
    </p>

    <p>
      For example, a linear model might be written as:
    </p>

    

    <p>
      Here, β₀ and β₁ are parameters.
    </p>

    <p>
      They determine the position and slope of the relationship.
    </p>

    <h2>The Intercept Parameter</h2>

    <p>
      The intercept parameter describes the expected outcome when the predictor equals zero.
    </p>

    <p>
      It establishes the baseline level of the model.
    </p>

    <h2>The Slope Parameter</h2>

    <p>
      The slope parameter describes how the expected outcome changes when the predictor changes.
    </p>

    <p>
      In many applications, the slope is one of the most important quantities of interest.
    </p>

    <h2>Parameters Control Model Behavior</h2>

    <p>
      Different parameter values produce different models.
    </p>

    <p>
      For example:
    </p>

    <ul class="bullets">

      <li>A larger slope implies a stronger relationship</li>

      <li>A smaller slope implies a weaker relationship</li>

      <li>A positive slope implies an increasing relationship</li>

      <li>A negative slope implies a decreasing relationship</li>

    </ul>

    <p>
      Parameters determine the shape and behavior of models.
    </p>

    <h2>Unknown but Fixed</h2>

    <p>
      In classical statistics, parameters are usually treated as fixed but unknown.
    </p>

    <p>
      The value exists, but we do not know it exactly.
    </p>

    <p>
      Data provide information that helps us estimate it.
    </p>

    <div class="concept-box">

      <strong>Important idea:</strong>

      <p>
        Parameters are not random properties of the population. Our uncertainty comes from not knowing their values.
      </p>

    </div>

    <h2>Why We Estimate Parameters</h2>

    <p>
      Direct observation of population parameters is often impossible.
    </p>

    <p>
      Instead, we:
    </p>

    <ol>

      <li>Collect data</li>

      <li>Compute statistics</li>

      <li>Estimate parameters</li>

      <li>Quantify uncertainty</li>

    </ol>

    <p>
      This process connects data to scientific conclusions.
    </p>

    <h2>Many Models Have Multiple Parameters</h2>

    <p>
      Real-world models often contain several parameters.
    </p>

    <p>
      Examples include:
    </p>

    <ul class="bullets">

      <li>Multiple regression coefficients</li>

      <li>Several group means</li>

      <li>Variance parameters</li>

      <li>Probability parameters</li>

    </ul>

    <p>
      Each parameter captures a different aspect of the system.
    </p>

    <h2>Parameters and Interpretation</h2>

    <p>
      One reason statistical models are useful is that parameters often have meaningful interpretations.
    </p>

    <p>
      For example:
    </p>

    <ul class="bullets">

      <li>Average income</li>

      <li>Average treatment effect</li>

      <li>Probability of success</li>

      <li>Expected change in outcome</li>

    </ul>

    <p>
      Parameters transform raw data into interpretable quantities.
    </p>

    <h2>Parameters and Prediction</h2>

    <p>
      Estimated parameters are also used to make predictions.
    </p>

    <p>
      Once parameters are estimated, the model can generate expected outcomes for new observations.
    </p>

    <p>
      Prediction therefore depends heavily on accurate parameter estimation.
    </p>

    <h2>Parameter Estimation Is Never Perfect</h2>

    <p>
      Because estimates come from samples:
    </p>

    <ul class="bullets">

      <li>Sampling variability exists</li>

      <li>Different samples produce different estimates</li>

      <li>Uncertainty remains unavoidable</li>

    </ul>

    <p>
      This is why confidence intervals and standard errors are important.
    </p>

    <h2>Parameters and Learning From Data</h2>

    <p>
      Much of statistical modeling can be viewed as learning parameter values from data.
    </p>

    <p>
      The model structure defines what parameters exist.
    </p>

    <p>
      The data help determine their likely values.
    </p>

    <h2>The Bigger Picture</h2>

    <p>
      Parameters connect abstract models to real-world questions.
    </p>

    <p>
      They describe important characteristics of populations and relationships among variables.
    </p>

    <p>
      Estimating parameters accurately is one of the central objectives of statistical modeling.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        Parameters are fixed but usually unknown quantities that describe populations and models. Statistical modeling uses data to estimate parameters and quantify uncertainty about their values.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      Not all models are built for the same purpose.
    </p>

    <p>
      Some models aim to understand why relationships exist, while others focus primarily on making accurate predictions.
    </p>

    <p>
      The next lesson explores the important distinction between prediction and explanation in statistical modeling.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Parameters are numerical quantities that describe populations or models</li>

        <li>Parameters are usually unknown and must be estimated from data</li>

        <li>Statistics are sample-based quantities used to estimate parameters</li>

        <li>Model parameters determine how relationships are represented</li>

        <li>Regression slopes and intercepts are examples of parameters</li>

        <li>Parameters often have meaningful interpretations</li>

        <li>Prediction depends on estimated parameter values</li>

        <li>Estimating parameters is a central goal of statistical modeling</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/modeling/foundations/signal-noise/">
         ← Previous: Signal and Noise
      </a>

      <a class="btn"
         href="/modeling/foundations/prediction-vs-explanation/">
         Next: Prediction vs Explanation →
      </a>

    </div>

  </div>

</section>