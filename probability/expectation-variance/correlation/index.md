---
layout: default
title: Correlation
description: Learn how correlation standardizes covariance and provides a clear measure of the strength and direction of linear relationships.
permalink: /probability/expectation-variance/correlation/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_probability_expectation_variance_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/probability/expectation-variance/correlation/",
    label: "Correlation",
    ts: Date.now()
  }));

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Probability</span>
      <span class="badge">Block 4</span>
      <span class="badge">Expectation & Variance</span>
      <span class="badge">Association</span>
    </div>

    <h1>Correlation</h1>

    <p class="lead">
      Covariance tells us whether variables move together, but its magnitude depends on measurement units.
    </p>

    <p class="lead">
      Correlation solves this problem by providing a standardized measure of the strength and direction of a linear relationship.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/probability/expectation-variance/covariance/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/probability/expectation-variance/indicator-random-variables/">
         Next: Indicator Random Variables →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>Why Correlation Exists</h2>

    <p>
      In the previous lesson,
      we learned that covariance measures how two variables move together.
    </p>

    <p>
      However,
      covariance has a major limitation.
    </p>

    <div class="example-box">

      <p>
        Changing measurement units changes covariance.
      </p>

      <p>
        Converting meters to centimeters changes its value.
      </p>

    </div>

    <p>
      This makes comparisons difficult.
    </p>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        Correlation is a standardized version of covariance that always falls between −1 and +1.
      </p>

    </div>

    <h2>The Correlation Formula</h2>

    <p>
      The correlation between two random variables X and Y is:
    </p>

    0

    <p>
      where:
    </p>

    <ul class="bullets">

      <li>Cov(X,Y) is the covariance</li>

      <li>σX is the standard deviation of X</li>

      <li>σY is the standard deviation of Y</li>

    </ul>

    <p>
      Dividing by the standard deviations removes the influence of measurement units.
    </p>

    <h2>The Correlation Symbol</h2>

    <p>
      Correlation is commonly represented by:
    </p>

    1

    <p>
      for population correlation.
    </p>

    <p>
      Sample correlation is often represented by:
    </p>

    <div class="example-box">

      <p>
        r
      </p>

    </div>

    <h2>The Range of Correlation</h2>

    <p>
      Correlation always satisfies:
    </p>

    2

    <p>
      This fixed range makes interpretation straightforward.
    </p>

    <h2>Positive Correlation</h2>

    <p>
      Positive correlation indicates that variables tend to move in the same direction.
    </p>

    <div class="example-box">

      <p>
        More study time → higher exam scores
      </p>

      <p>
        More advertising → higher sales
      </p>

    </div>

    <p>
      Positive correlations satisfy:
    </p>

    3

    <h2>Negative Correlation</h2>

    <p>
      Negative correlation indicates that variables tend to move in opposite directions.
    </p>

    <div class="example-box">

      <p>
        Higher prices → lower demand
      </p>

      <p>
        More distance traveled → less fuel remaining
      </p>

    </div>

    <p>
      Negative correlations satisfy:
    </p>

    4

    <h2>Zero Correlation</h2>

    <p>
      A correlation of zero indicates no linear relationship.
    </p>

    5

    <p>
      Knowledge of one variable does not provide information about a linear trend in the other.
    </p>

    <h2>Interpreting Correlation Strength</h2>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Correlation</th>
            <th>Interpretation</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>+1</td>
            <td>Perfect positive linear relationship</td>
          </tr>

          <tr>
            <td>0.7 to 0.9</td>
            <td>Strong positive relationship</td>
          </tr>

          <tr>
            <td>0.3 to 0.7</td>
            <td>Moderate positive relationship</td>
          </tr>

          <tr>
            <td>0</td>
            <td>No linear relationship</td>
          </tr>

          <tr>
            <td>-0.3 to -0.7</td>
            <td>Moderate negative relationship</td>
          </tr>

          <tr>
            <td>-0.7 to -0.9</td>
            <td>Strong negative relationship</td>
          </tr>

          <tr>
            <td>-1</td>
            <td>Perfect negative linear relationship</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      These ranges are rough guidelines rather than strict rules.
    </p>

    <h2>Perfect Positive Correlation</h2>

    <p>
      When:
    </p>

    6

    <p>
      all observations lie exactly on an increasing straight line.
    </p>

    <div class="example-box">

      <p>
        Y = 2X
      </p>

    </div>

    <p>
      Every increase in X produces a perfectly predictable increase in Y.
    </p>

    <h2>Perfect Negative Correlation</h2>

    <p>
      When:
    </p>

    7

    <p>
      all observations lie exactly on a decreasing straight line.
    </p>

    <div class="example-box">

      <p>
        Y = 100 − X
      </p>

    </div>

    <p>
      Increases in X correspond perfectly to decreases in Y.
    </p>

    <h2>Correlation Measures Linear Relationships</h2>

    <p>
      Correlation is specifically designed to detect linear relationships.
    </p>

    <p>
      A strong nonlinear relationship can still produce a correlation near zero.
    </p>

    <div class="concept-box">

      <strong>Important:</strong>

      <p>
        Zero correlation does not necessarily mean no relationship exists.
      </p>

    </div>

    <h2>A Nonlinear Example</h2>

    <p>
      Suppose:
    </p>

    <div class="example-box">

      <p>
        Y = X²
      </p>

    </div>

    <p>
      The relationship is clearly strong.
    </p>

    <p>
      Yet under some symmetric settings,
      correlation may be close to zero because the relationship is not linear.
    </p>

    <h2>Correlation and Independence</h2>

    <p>
      Independent variables always have zero correlation.
    </p>

    <div class="example-box">

      <p>
        Independence ⇒ Zero Correlation
      </p>

    </div>

    <p>
      However,
      the reverse is generally false.
    </p>

    <div class="concept-box">

      <strong>Important:</strong>

      <p>
        Zero correlation does not imply independence.
      </p>

    </div>

    <h2>Correlation in Data Analysis</h2>

    <p>
      Correlation is widely used in:
    </p>

    <ul class="bullets">

      <li>Statistics</li>

      <li>Machine learning</li>

      <li>Finance</li>

      <li>Economics</li>

      <li>Quality control</li>

      <li>Scientific research</li>

    </ul>

    <p>
      It provides a quick summary of linear association between variables.
    </p>

    <h2>Correlation Is Not Causation</h2>

    <p>
      One of the most important principles in statistics is:
    </p>

    <div class="concept-box">

      <strong>Warning:</strong>

      <p>
        Correlation does not imply causation.
      </p>

    </div>

    <p>
      Two variables can be strongly correlated even when neither causes the other.
    </p>

    <p>
      Hidden factors or coincidence may create the observed relationship.
    </p>

    <h2>Why Correlation Matters</h2>

    <p>
      Correlation provides a standardized measure of dependence.
    </p>

    <p>
      Unlike covariance,
      it can be interpreted consistently across different datasets and measurement scales.
    </p>

    <p>
      This makes it one of the most widely reported statistical measures.
    </p>

    <h2>The Connection to Probability</h2>

    <p>
      Correlation helps us understand how random variables interact.
    </p>

    <p>
      Combined with expectation,
      variance,
      and covariance,
      it forms a complete toolkit for describing uncertainty and dependence.
    </p>

    <h2>Looking Ahead</h2>

    <p>
      So far,
      we have focused on expectation,
      variance,
      covariance,
      and correlation.
    </p>

    <p>
      The next lesson introduces indicator random variables,
      a simple but extremely powerful tool used throughout probability theory and combinatorics.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Correlation standardizes covariance</li>

        <li>Correlation always lies between −1 and +1</li>

        <li>Positive values indicate variables move together</li>

        <li>Negative values indicate variables move in opposite directions</li>

        <li>Zero correlation indicates no linear relationship</li>

        <li>Correlation measures linear association only</li>

        <li>Zero correlation does not imply independence</li>

        <li>Correlation does not imply causation</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/probability/expectation-variance/covariance/">
         ← Previous: Covariance
      </a>

      <a class="btn"
         href="/probability/expectation-variance/indicator-random-variables/">
         Next: Indicator Random Variables →
      </a>

    </div>

  </div>

</section>