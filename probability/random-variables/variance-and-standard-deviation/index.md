---
layout: default
title: Variance and Standard Deviation
description: Learn how variance and standard deviation measure the spread of a probability distribution around its expected value.
permalink: /probability/random-variables/variance-and-standard-deviation/
sidebar: false
math: true
translation_pair: random-variable-variance
learning_resource: true
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_probability_random_variables_lesson_v0";

  try {
  localStorage.setItem(KEY, JSON.stringify({
    url: "/probability/random-variables/variance-and-standard-deviation/",
    label: "Variance & Standard Deviation",
    ts: Date.now()
  }));
  } catch (_) {
    // Browser storage may be unavailable; reading the lesson must still work.
  }

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
<p><a href="/ar/probability/random-variables/variance-and-standard-deviation/" lang="ar" dir="rtl">اقرأ الدرس بالعربية: التباين والانحراف المعياري</a></p>

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

    
    \[
    \operatorname{Var}(X)=E[(X-E[X])^2]
    \]


    <p>
      This formula represents the expected squared distance from the mean.
    </p>

    <h2>Alternative Notation</h2>

    <p>
      Variance is often written using the symbol:
    </p>

    
    \[
    \sigma^2=\operatorname{Var}(X)
    \]


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

    
    \[
    E[X]=0.5
    \]


    <p>
      The variance can be calculated using the variance formula.
    </p>

    <p>
      The result is:
    </p>

    
    \[
    \operatorname{Var}(X)=(1-0.5)^2(0.5)+(0-0.5)^2(0.5)=0.25
    \]


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

    
    \[
    \operatorname{SD}(X)=\sqrt{\operatorname{Var}(X)}
    \]


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

    
    \[
    \operatorname{Var}(X)\ge0
    \]


    <p>
      Because squared values cannot be negative,
      variance cannot be negative.
    </p>

    <h3>Constant Variables Have Zero Variance</h3>

    <p>
      If a variable always takes the same value,
      there is no variability.
    </p>

    
    \[
    \operatorname{Var}(c)=0\quad\text{for every constant }c
    \]


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

    <!-- Batch #84: affine variance explorer. -->
<section class="concept-box" id="esa-affine-lab" aria-labelledby="esa-affine-heading">
<h2 id="esa-affine-heading">Interactive: variance under a linear transformation</h2>
<p>Choose a discrete three-outcome distribution and transform Y = a + bX. The probabilities must sum to one. This calculates theoretical, not sample, variance.</p>
<div class="esa-affine-grid">
<label for="esa-affine-x0">Outcome 1<input id="esa-affine-x0" type="number" step="any" value="0" aria-describedby="esa-affine-error"></label>
<label for="esa-affine-x1">Outcome 2<input id="esa-affine-x1" type="number" step="any" value="1" aria-describedby="esa-affine-error"></label>
<label for="esa-affine-x2">Outcome 3<input id="esa-affine-x2" type="number" step="any" value="2" aria-describedby="esa-affine-error"></label>
<label for="esa-affine-p0">Probability 1<input id="esa-affine-p0" type="number" step="any" value="0.2" aria-describedby="esa-affine-error"></label>
<label for="esa-affine-p1">Probability 2<input id="esa-affine-p1" type="number" step="any" value="0.5" aria-describedby="esa-affine-error"></label>
<label for="esa-affine-p2">Probability 3<input id="esa-affine-p2" type="number" step="any" value="0.3" aria-describedby="esa-affine-error"></label>
<label for="esa-affine-a">Offset a<input id="esa-affine-a" type="number" step="any" value="3" aria-describedby="esa-affine-error"></label>
<label for="esa-affine-b">Multiplier b<input id="esa-affine-b" type="number" step="any" value="-2" aria-describedby="esa-affine-error"></label>
</div>
<p id="esa-affine-error" role="alert" hidden></p>
<div id="esa-affine-results" role="status" aria-live="polite" aria-atomic="true">
<p>E(X): <output id="esa-affine-mx">1.100000</output>; Var(X): <output id="esa-affine-vx">0.490000</output>; SD(X): <output id="esa-affine-sx">0.700000</output></p>
<p>E(Y): <output id="esa-affine-my">0.800000</output>; Var(Y): <output id="esa-affine-vy">1.960000</output>; SD(Y): <output id="esa-affine-sy">1.400000</output></p>
<p>Check b² Var(X): <output id="esa-affine-rule">1.960000</output></p>
</div>
<svg id="esa-affine-chart" viewBox="0 0 480 185" role="img" aria-label="Comparative discrete probability mass plots for X and transformed Y" style="width:100%;height:auto;display:block"></svg>
<button type="button" class="btn btn-outline" id="esa-affine-reset">Reset example</button>
<noscript><p>With X taking 0, 1, 2 at probabilities 0.2, 0.5, 0.3 and a = 3, b = −2, Var(X) = 0.49 and Var(Y) = 1.96.</p></noscript>
<p class="muted-mini">Adding a constant does not change variance; multiplying by b multiplies variance by b². For b=0, the transformed variable is constant. A negative b reverses the order of outcomes.</p>
</section>
<style>#esa-affine-lab{min-width:0;overflow-wrap:anywhere}#esa-affine-lab .esa-affine-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}#esa-affine-lab label{display:block;min-width:0}#esa-affine-lab input{width:100%;min-width:0;box-sizing:border-box;padding:9px;font:inherit}#esa-affine-lab [hidden]{display:none!important}@media(max-width:480px){#esa-affine-lab .esa-affine-grid{grid-template-columns:minmax(0,1fr)}}</style>
<script defer src="/js/affine-variance-lab.js"></script>
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