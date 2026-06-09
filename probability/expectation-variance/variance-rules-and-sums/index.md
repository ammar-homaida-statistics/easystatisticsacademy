---
layout: default
title: Variance Rules and Sums
description: Learn how variance behaves when random variables are added together and why independence plays a crucial role.
permalink: /probability/expectation-variance/variance-rules-and-sums/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_probability_expectation_variance_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/probability/expectation-variance/variance-rules-and-sums/",
    label: "Variance Rules and Sums",
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
      <span class="badge">Variability</span>
    </div>

    <h1>Variance Rules and Sums</h1>

    <p class="lead">
      Expectation adds beautifully regardless of dependence.
    </p>

    <p class="lead">
      Variance behaves differently. Understanding how variances combine is essential for analyzing uncertainty in sums of random variables.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/probability/expectation-variance/linearity-of-expectation/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/probability/expectation-variance/covariance/">
         Next: Covariance →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>From Expectation to Variance</h2>

    <p>
      In the previous lesson,
      we learned that expectations always add.
    </p>

    0

    <p>
      Variance is more complicated because it depends not only on individual variability but also on how variables move together.
    </p>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        The variance of a sum depends on both the individual variances and the relationship between the variables.
      </p>

    </div>

    <h2>Review: What Variance Measures</h2>

    <p>
      Variance measures the average squared distance from the mean.
    </p>

    1

    <p>
      Larger variances indicate greater spread around the expected value.
    </p>

    <h2>Variance of a Constant</h2>

    <p>
      A constant never changes.
    </p>

    <p>
      Therefore,
      it has no variability.
    </p>

    2

    <p>
      for any constant c.
    </p>

    <h2>Adding a Constant</h2>

    <p>
      Adding a constant shifts the center of a distribution but does not change its spread.
    </p>

    3

    <p>
      The variability remains exactly the same.
    </p>

    <h2>Multiplying by a Constant</h2>

    <p>
      Scaling a variable changes its variability.
    </p>

    <p>
      The variance rule is:
    </p>

    4

    <p>
      Notice the square.
    </p>

    <p>
      Variance responds to scaling more strongly than expectation.
    </p>

    <h2>Example: Scaling Measurements</h2>

    <p>
      Suppose:
    </p>

    <div class="example-box">

      <p>
        Var(X) = 4
      </p>

    </div>

    <p>
      Let:
    </p>

    <div class="example-box">

      <p>
        Y = 3X
      </p>

    </div>

    <p>
      Then:
    </p>

    5

    <p>
      The variance increases by a factor of nine.
    </p>

    <h2>Variance of a Sum</h2>

    <p>
      Now consider two random variables:
    </p>

    <div class="example-box">

      <p>
        X
      </p>

      <p>
        Y
      </p>

    </div>

    <p>
      What is:
    </p>

    6

    <p>
      Unlike expectation,
      the answer is not always the simple sum of the variances.
    </p>

    <h2>The General Formula</h2>

    <p>
      The complete variance rule is:
    </p>

    7

    <p>
      The additional term involves covariance,
      which measures how variables move together.
    </p>

    <h2>Why the Extra Term Appears</h2>

    <p>
      If X and Y tend to increase together,
      the total variability becomes larger.
    </p>

    <p>
      If one tends to increase while the other decreases,
      the total variability becomes smaller.
    </p>

    <p>
      Covariance captures this relationship.
    </p>

    <h2>The Special Case of Independence</h2>

    <p>
      When X and Y are independent:
    </p>

    8

    <p>
      Therefore:
    </p>

    9

    <p>
      This is the variance rule most frequently used in introductory probability.
    </p>

    <div class="concept-box">

      <strong>Important:</strong>

      <p>
        Variances add only when variables are independent (or at least uncorrelated).
      </p>

    </div>

    <h2>Example: Two Independent Dice</h2>

    <p>
      Let:
    </p>

    <div class="example-box">

      <p>
        X = First die
      </p>

      <p>
        Y = Second die
      </p>

    </div>

    <p>
      Each die has variance:
    </p>

    10

    <p>
      Since the dice are independent:
    </p>

    11

    <p>
      The variances simply add.
    </p>

    <h2>Variance of a Difference</h2>

    <p>
      A similar rule applies to subtraction.
    </p>

    12

    <p>
      The covariance term changes sign.
    </p>

    <h2>Independent Variables and Differences</h2>

    <p>
      If X and Y are independent:
    </p>

    13

    <p>
      Surprisingly,
      the same addition rule appears.
    </p>

    <p>
      Variance does not care whether the variables are added or subtracted when independence holds.
    </p>

    <h2>Extending to Many Variables</h2>

    <p>
      For independent variables:
    </p>

    14

    <p>
      This rule is essential in probability theory,
      statistics,
      and data science.
    </p>

    <h2>Why This Matters</h2>

    <p>
      Many real-world quantities are sums.
    </p>

    <div class="example-box">

      <p>
        Total sales
      </p>

      <p>
        Total claims
      </p>

      <p>
        Total arrivals
      </p>

      <p>
        Total profits
      </p>

    </div>

    <p>
      Understanding how variability accumulates is critical for risk assessment and forecasting.
    </p>

    <h2>Expectation Versus Variance</h2>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Quantity</th>
            <th>Addition Rule</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>Expectation</td>
            <td>Always adds</td>
          </tr>

          <tr>
            <td>Variance</td>
            <td>Depends on covariance</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      This distinction is one of the most important ideas in probability.
    </p>

    <h2>The Missing Piece</h2>

    <p>
      We have repeatedly mentioned covariance,
      but we have not yet defined it.
    </p>

    <p>
      Covariance is the quantity that explains whether variables move together,
      move apart,
      or behave independently.
    </p>

    <p>
      It is the key to understanding how variances combine.
    </p>

    <h2>Looking Ahead</h2>

    <p>
      The next lesson introduces covariance,
      a measure of joint variability between random variables.
    </p>

    <p>
      Covariance provides the missing connection between expectation,
      variance,
      dependence,
      and correlation.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Var(c) = 0 for any constant</li>

        <li>Var(X + c) = Var(X)</li>

        <li>Var(cX) = c²Var(X)</li>

        <li>Variance of a sum depends on covariance</li>

        <li>Var(X + Y) = Var(X) + Var(Y) + 2Cov(X,Y)</li>

        <li>Independent variables have covariance zero</li>

        <li>Variances add directly only when variables are independent or uncorrelated</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/probability/expectation-variance/linearity-of-expectation/">
         ← Previous: Linearity of Expectation
      </a>

      <a class="btn"
         href="/probability/expectation-variance/covariance/">
         Next: Covariance →
      </a>

    </div>

  </div>

</section>