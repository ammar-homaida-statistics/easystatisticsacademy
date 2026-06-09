---
layout: default
title: Covariance
description: Learn how covariance measures whether two random variables tend to move together and why it plays a central role in variance calculations.
permalink: /probability/expectation-variance/covariance/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_probability_expectation_variance_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/probability/expectation-variance/covariance/",
    label: "Covariance",
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
      <span class="badge">Dependence</span>
    </div>

    <h1>Covariance</h1>

    <p class="lead">
      Variance measures how a single random variable varies around its mean.
    </p>

    <p class="lead">
      Covariance extends this idea to two random variables and measures whether they tend to move together.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/probability/expectation-variance/variance-rules-and-sums/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/probability/expectation-variance/correlation/">
         Next: Correlation →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>Why Covariance Exists</h2>

    <p>
      Many probability problems involve more than one random variable.
    </p>

    <div class="example-box">

      <p>
        Hours studied and exam scores
      </p>

      <p>
        Advertising spending and sales
      </p>

      <p>
        Temperature and electricity usage
      </p>

    </div>

    <p>
      In these situations,
      we often want to know whether the variables tend to increase or decrease together.
    </p>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        Covariance measures the direction of joint movement between two random variables.
      </p>

    </div>

    <h2>The Basic Idea</h2>

    <p>
      Recall that variance examines deviations from a mean.
    </p>

    <p>
      Covariance examines deviations from two means simultaneously.
    </p>

    <p>
      It asks:
    </p>

    <div class="example-box">

      <p>
        When X is above its mean,
        is Y also above its mean?
      </p>
    </div>

    <p>
      If the answer is often yes,
      covariance tends to be positive.
    </p>

    <h2>The Covariance Formula</h2>

    <p>
      Covariance between X and Y is defined as:
    </p>

    0

    <p>
      This formula measures the average product of the deviations from their respective means.
    </p>

    <h2>Understanding the Formula</h2>

    <p>
      Consider the product:
    </p>

    1

    <p>
      This product can be positive or negative.
    </p>

    <ul class="bullets">

      <li>Both deviations positive → positive product</li>

      <li>Both deviations negative → positive product</li>

      <li>One positive and one negative → negative product</li>

    </ul>

    <p>
      Averaging these products reveals the overall tendency of the variables to move together.
    </p>

    <h2>Positive Covariance</h2>

    <p>
      Positive covariance occurs when variables tend to move in the same direction.
    </p>

    <div class="example-box">

      <p>
        More study time → higher exam scores
      </p>

      <p>
        Higher temperatures → greater ice cream sales
      </p>

    </div>

    <p>
      In such cases:
    </p>

    2

    <h2>Negative Covariance</h2>

    <p>
      Negative covariance occurs when variables tend to move in opposite directions.
    </p>

    <div class="example-box">

      <p>
        Product price and demand
      </p>

      <p>
        Distance from city center and housing density
      </p>

    </div>

    <p>
      In these situations:
    </p>

    3

    <h2>Zero Covariance</h2>

    <p>
      When no consistent linear relationship exists,
      covariance may be zero.
    </p>

    4

    <p>
      This means positive and negative joint deviations balance one another.
    </p>

    <h2>Covariance and Independence</h2>

    <p>
      If two random variables are independent:
    </p>

    5

    <p>
      Independence guarantees zero covariance.
    </p>

    <div class="concept-box">

      <strong>Important:</strong>

      <p>
        Zero covariance does not necessarily imply independence.
      </p>

    </div>

    <p>
      Variables can have complex nonlinear relationships while still having covariance equal to zero.
    </p>

    <h2>An Alternative Formula</h2>

    <p>
      Covariance is often computed using:
    </p>

    6

    <p>
      This equivalent formula is frequently easier to apply in calculations.
    </p>

    <h2>Why Covariance Matters for Variance</h2>

    <p>
      In the previous lesson,
      we saw:
    </p>

    7

    <p>
      Covariance determines whether combining variables increases or decreases overall variability.
    </p>

    <h2>Positive Covariance and Variance</h2>

    <p>
      When covariance is positive,
      variables reinforce one another.
    </p>

    <p>
      The variability of their sum becomes larger.
    </p>

    <div class="example-box">

      <p>
        Two variables rising together create more fluctuation in their total.
      </p>

    </div>

    <h2>Negative Covariance and Variance</h2>

    <p>
      When covariance is negative,
      one variable tends to offset the other.
    </p>

    <p>
      This reduces the variability of the sum.
    </p>

    <div class="example-box">

      <p>
        Gains in one variable partially cancel losses in another.
      </p>

    </div>

    <h2>A Financial Example</h2>

    <p>
      Covariance plays a major role in portfolio management.
    </p>

    <p>
      Investors often combine assets that do not move together.
    </p>

    <p>
      Negative covariance can reduce overall portfolio risk.
    </p>

    <p>
      This principle forms the basis of diversification.
    </p>

    <h2>The Units Problem</h2>

    <p>
      Covariance has a drawback.
    </p>

    <p>
      Its magnitude depends on the units of the variables.
    </p>

    <div class="example-box">

      <p>
        Changing units from meters to centimeters changes covariance.
      </p>

    </div>

    <p>
      This makes raw covariance values difficult to interpret.
    </p>

    <h2>Why Sign Is Often More Important</h2>

    <p>
      The sign of covariance usually provides the most useful information.
    </p>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Covariance</th>
            <th>Interpretation</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>Positive</td>
            <td>Variables tend to move together</td>
          </tr>

          <tr>
            <td>Negative</td>
            <td>Variables tend to move in opposite directions</td>
          </tr>

          <tr>
            <td>Zero</td>
            <td>No linear tendency</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      The sign immediately reveals the direction of the relationship.
    </p>

    <h2>The Need for Standardization</h2>

    <p>
      Because covariance depends on measurement units,
      it is difficult to compare across different variables.
    </p>

    <p>
      We need a standardized measure that always lies within a fixed range.
    </p>

    <p>
      That measure is correlation.
    </p>

    <h2>The Big Picture</h2>

    <p>
      Covariance extends the idea of variance from one variable to two variables.
    </p>

    <p>
      It explains how variables move together and determines how variability accumulates in sums of random variables.
    </p>

    <p>
      It is one of the fundamental concepts underlying dependence and association.
    </p>

    <h2>Looking Ahead</h2>

    <p>
      Covariance tells us the direction of a relationship,
      but its magnitude is difficult to interpret because it depends on units.
    </p>

    <p>
      The next lesson introduces correlation,
      a standardized version of covariance that provides a clearer measure of association.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Covariance measures joint variability between two random variables</li>

        <li>Positive covariance indicates variables tend to move together</li>

        <li>Negative covariance indicates variables tend to move in opposite directions</li>

        <li>Zero covariance indicates no linear tendency</li>

        <li>Independent variables have covariance equal to zero</li>

        <li>Covariance affects the variance of sums</li>

        <li>Covariance depends on measurement units, making interpretation difficult</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/probability/expectation-variance/variance-rules-and-sums/">
         ← Previous: Variance Rules and Sums
      </a>

      <a class="btn"
         href="/probability/expectation-variance/correlation/">
         Next: Correlation →
      </a>

    </div>

  </div>

</section>