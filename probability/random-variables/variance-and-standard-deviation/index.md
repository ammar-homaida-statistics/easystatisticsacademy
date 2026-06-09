---
layout: default
title: Variance and Standard Deviation
description: Learn how variance and standard deviation measure the spread of a probability distribution around its expected value.
permalink: /probability/random-variables/variance-and-standard-deviation/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_probability_random_variables_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/probability/random-variables/variance-and-standard-deviation/",
    label: "Variance and Standard Deviation",
    ts: Date.now()
  }));

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Probability</span>
      <span class="badge">Block 3</span>
      <span class="badge">Random Variables</span>
      <span class="badge">Variability</span>
    </div>

    <h1>Variance and Standard Deviation</h1>

    <p class="lead">
      Expectation tells us where a probability distribution is centered.
    </p>

    <p class="lead">
      Variance and standard deviation tell us how widely outcomes are spread around that center.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/probability/random-variables/expectation/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/probability/expectation-variance/">
         Next Block: Expectation & Variance →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>Why Variability Matters</h2>

    <p>
      Two random variables can have the same expected value but behave very differently.
    </p>

    <div class="example-box">

      <p>
        Investment A always returns $100.
      </p>

      <p>
        Investment B returns either $0 or $200.
      </p>

    </div>

    <p>
      Both investments have the same expected value of $100.
    </p>

    <p>
      However,
      the second investment is much more variable.
    </p>

    <p>
      We need a way to measure that variability.
    </p>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        Variance and standard deviation measure how far outcomes tend to fall from the expected value.
      </p>

    </div>

    <h2>Measuring Distance from the Mean</h2>

    <p>
      A natural idea is to examine the difference between an outcome and the expected value.
    </p>

    <p>
      This difference is called a deviation.
    </p>

    <div class="example-box">

      <p>
        Deviation = Outcome − Mean
      </p>

    </div>

    <p>
      Large deviations indicate outcomes far from the center.
    </p>

    <h2>The Problem with Simple Deviations</h2>

    <p>
      Positive and negative deviations cancel one another.
    </p>

    <div class="example-box">

      <p>
        +5 and −5 sum to zero.
      </p>

    </div>

    <p>
      As a result,
      averaging raw deviations always produces zero.
    </p>

    <p>
      A different approach is needed.
    </p>

    <h2>Squaring the Deviations</h2>

    <p>
      Variance solves the cancellation problem by squaring deviations before averaging them.
    </p>

    <p>
      Squaring makes all values nonnegative.
    </p>

    <div class="example-box">

      <p>
        (+5)² = 25
      </p>

      <p>
        (−5)² = 25
      </p>

    </div>

    <p>
      Both contribute equally to variability.
    </p>

    <h2>The Variance Formula</h2>

    <p>
      For a random variable X:
    </p>

    0

    <p>
      This formula represents the expected squared distance from the mean.
    </p>

    <h2>Alternative Notation</h2>

    <p>
      Variance is often written using the symbol:
    </p>

    1

    <p>
      when referring to a population distribution.
    </p>

    <h2>Interpreting Variance</h2>

    <p>
      A larger variance indicates greater spread.
    </p>

    <div class="example-box">

      <p>
        Small variance → outcomes cluster near the mean.
      </p>

      <p>
        Large variance → outcomes spread farther from the mean.
      </p>

    </div>

    <p>
      Variance quantifies uncertainty around the expected value.
    </p>

    <h2>Example: Fair Coin</h2>

    <p>
      Let:
    </p>

    <div class="example-box">

      <p>
        X = 1 if heads
      </p>

      <p>
        X = 0 if tails
      </p>

    </div>

    <p>
      We already know:
    </p>

    2

    <p>
      The variance can be calculated using the variance formula.
    </p>

    <p>
      The result is:
    </p>

    3

    <p>
      This value measures the variability of the coin toss outcomes.
    </p>

    <h2>The Units Problem</h2>

    <p>
      Variance has an important limitation.
    </p>

    <p>
      Because deviations are squared,
      the units are also squared.
    </p>

    <div class="example-box">

      <p>
        Height measured in centimeters
      </p>

      <p>
        Variance measured in square centimeters
      </p>

    </div>

    <p>
      These units are often difficult to interpret directly.
    </p>

    <h2>Introducing Standard Deviation</h2>

    <p>
      Standard deviation solves this problem by taking the square root of variance.
    </p>

    4

    <p>
      Standard deviation returns the measure of spread to the original units.
    </p>

    <h2>Why Standard Deviation Is Popular</h2>

    <p>
      Standard deviation is easier to interpret because it uses the same units as the data.
    </p>

    <div class="example-box">

      <p>
        Height → centimeters
      </p>

      <p>
        Weight → kilograms
      </p>

      <p>
        Time → minutes
      </p>

    </div>

    <p>
      This makes standard deviation one of the most widely reported measures of variability.
    </p>

    <h2>Interpreting Standard Deviation</h2>

    <p>
      Standard deviation provides a typical distance from the mean.
    </p>

    <p>
      Larger values indicate greater variability.
    </p>

    <div class="example-box">

      <p>
        Small standard deviation → observations are tightly clustered.
      </p>

      <p>
        Large standard deviation → observations are more dispersed.
      </p>

    </div>

    <h2>Variance and Risk</h2>

    <p>
      Variance is frequently used as a measure of risk.
    </p>

    <p>
      In finance,
      investments with larger variances are generally considered riskier.
    </p>

    <p>
      More variability means less predictability.
    </p>

    <h2>Properties of Variance</h2>

    <h3>Variance Is Never Negative</h3>

    5

    <p>
      Because squared values cannot be negative,
      variance cannot be negative.
    </p>

    <h3>Constant Variables Have Zero Variance</h3>

    <p>
      If a variable always takes the same value,
      there is no variability.
    </p>

    6

    <p>
      when every observation is identical.
    </p>

    <h2>Expectation and Variability Together</h2>

    <p>
      Expectation and variance provide complementary information.
    </p>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Measure</th>
            <th>Describes</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>Expectation</td>
            <td>Center</td>
          </tr>

          <tr>
            <td>Variance</td>
            <td>Spread</td>
          </tr>

          <tr>
            <td>Standard Deviation</td>
            <td>Spread in original units</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      Together,
      these measures provide a much more complete description of a distribution.
    </p>

    <h2>Applications of Variance and Standard Deviation</h2>

    <ul class="bullets">

      <li>Risk management</li>

      <li>Financial modeling</li>

      <li>Machine learning</li>

      <li>Quality control</li>

      <li>Forecasting</li>

      <li>Statistical inference</li>

    </ul>

    <p>
      They are among the most important quantities in all of statistics.
    </p>

    <h2>What We Learned in Block 3</h2>

    <p>
      This block introduced random variables and probability distributions.
    </p>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Topic</th>
            <th>Main Idea</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>Random Variables</td>
            <td>Assign numbers to uncertain outcomes.</td>
          </tr>

          <tr>
            <td>Discrete Variables</td>
            <td>Countable outcomes.</td>
          </tr>

          <tr>
            <td>Continuous Variables</td>
            <td>Measured outcomes.</td>
          </tr>

          <tr>
            <td>CDF</td>
            <td>Accumulated probability up to a value.</td>
          </tr>

          <tr>
            <td>Expectation</td>
            <td>Center of a distribution.</td>
          </tr>

          <tr>
            <td>Variance & Standard Deviation</td>
            <td>Spread of a distribution.</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>Preparing for the Next Block</h2>

    <p>
      We now know how to describe a random variable using:
    </p>

    <ul class="bullets">

      <li>Its distribution</li>

      <li>Its expected value</li>

      <li>Its variability</li>

    </ul>

    <p>
      The next block explores expectation and variance in greater depth.
    </p>

    <p>
      We will learn how these quantities behave under transformations,
      combinations of variables,
      and repeated random experiments.
    </p>

    <!-- BLOCK TAKEAWAYS -->

    <div class="summary-box">

      <h2>Block 3 Takeaways</h2>

      <ul class="bullets">

        <li>Random variables convert outcomes into numerical values</li>

        <li>Discrete variables represent counts</li>

        <li>Continuous variables represent measurements</li>

        <li>CDFs provide a unified description of distributions</li>

        <li>Expectation measures the center of a distribution</li>

        <li>Variance measures spread around the mean</li>

        <li>Standard deviation measures spread in the original units</li>

        <li>Center and spread together describe a distribution more completely</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/probability/random-variables/expectation/">
         ← Previous: Expectation
      </a>

      <a class="btn"
         href="/probability/random-variables/">
         Random Variables Home
      </a>

      <a class="btn btn-outline"
         href="/probability/expectation-variance/">
         Next Block: Expectation & Variance →
      </a>

    </div>

  </div>

</section>