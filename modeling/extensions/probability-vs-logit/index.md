---
layout: default
title: Probability vs Logit
description: Learn the difference between probabilities and logits, why logistic regression uses logits internally, and how the logit transformation makes binary outcome modeling possible.
permalink: /modeling/extensions/probability-vs-logit/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_modeling_extensions_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/modeling/extensions/probability-vs-logit/",
    label: "Probability vs Logit",
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
      <span class="badge">Logistic Regression</span>
    </div>

    <h1>Probability vs Logit</h1>

    <p class="lead">
      Logistic regression predicts probabilities, but the model itself is built using something called the logit.
    </p>

    <p class="lead">
      Understanding the distinction between probabilities and logits is essential for interpreting logistic regression coefficients.
    </p>

    <p class="lead">
      The logit transformation is what allows regression methods to work with binary outcomes.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/modeling/extensions/logistic-regression/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/modeling/extensions/odds/">
         Next: Odds →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>Start With Probability</h2>

    <p>
      A probability represents the chance that an event occurs.
    </p>

    <p>
      Probabilities always lie between:
    </p>

    <ul class="bullets">

      <li>0 (impossible)</li>

      <li>1 (certain)</li>

    </ul>

    <p>
      For example:
    </p>

    <div class="example-box">

      <p>0.10 = 10% chance</p>
      <p>0.50 = 50% chance</p>
      <p>0.90 = 90% chance</p>
    </div>

    <p>
      Probabilities are intuitive and easy to interpret.
    </p>

    <div class="concept-box">

      <strong>Main idea:</strong>

      <p>
        Probabilities describe chances directly, but their restricted range creates challenges for regression modeling.
      </p>

    </div>

    <h2>The Problem With Modeling Probabilities Directly</h2>

    <p>
      Ordinary regression assumes the outcome can vary freely across the number line.
    </p>

    <p>
      Probabilities cannot do this because they are constrained between 0 and 1.
    </p>

    <p>
      A straight-line model could produce impossible predictions such as:
    </p>

    <div class="example-box">

      <p>-0.20</p>
      <p>1.35</p>
    </div>

    <p>
      Both values are invalid probabilities.
    </p>

    <h2>A Solution: Transformation</h2>

    <p>
      Logistic regression solves this problem by transforming probabilities into another quantity that can range from negative infinity to positive infinity.
    </p>

    <p>
      This transformed quantity is called the <strong>logit</strong>.
    </p>

    <p>
      Regression is performed on logits rather than directly on probabilities.
    </p>

    <h2>What Is a Logit?</h2>

    <p>
      A logit is the logarithm of the odds of an event occurring.
    </p>

    <p>
      Conceptually:
    </p>

    <div class="example-box">

      <p>
        Probability → Odds → Logit
      </p>
    </div>

    <p>
      Logistic regression converts probabilities into logits, fits a linear model, and then converts results back into probabilities.
    </p>

    <h2>Why Use Logits?</h2>

    <p>
      Unlike probabilities, logits are not restricted to the interval from 0 to 1.
    </p>

    <p>
      Logits can take any real value:
    </p>

    <ul class="bullets">

      <li>Very large negative numbers</li>

      <li>Zero</li>

      <li>Very large positive numbers</li>

    </ul>

    <p>
      This makes them compatible with linear modeling techniques.
    </p>

    <div class="concept-box">

      <strong>Key insight:</strong>

      <p>
        Logistic regression is linear in the logit, not linear in the probability.
      </p>

    </div>

    <h2>The Probability Scale</h2>

    <p>
      The probability scale is bounded.
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Probability</th>
            <th>Interpretation</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>0.00</td>
            <td>Impossible</td>
          </tr>

          <tr>
            <td>0.25</td>
            <td>Unlikely</td>
          </tr>

          <tr>
            <td>0.50</td>
            <td>Even chance</td>
          </tr>

          <tr>
            <td>0.75</td>
            <td>Likely</td>
          </tr>

          <tr>
            <td>1.00</td>
            <td>Certain</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      No probability can be smaller than 0 or larger than 1.
    </p>

    <h2>The Logit Scale</h2>

    <p>
      The logit scale removes these restrictions.
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Probability</th>
            <th>Approximate Logit</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>0.01</td>
            <td>-4.60</td>
          </tr>

          <tr>
            <td>0.10</td>
            <td>-2.20</td>
          </tr>

          <tr>
            <td>0.50</td>
            <td>0.00</td>
          </tr>

          <tr>
            <td>0.90</td>
            <td>2.20</td>
          </tr>

          <tr>
            <td>0.99</td>
            <td>4.60</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      Notice that probabilities near 0 and 1 correspond to increasingly extreme logit values.
    </p>

    <h2>The Logistic Curve Connects Them</h2>

    <p>
      Logistic regression uses a logistic function to translate logits back into probabilities.
    </p>

    <p>
      This creates the familiar S-shaped logistic curve.
    </p>

    

    <p>
      Small changes in logit values can produce different changes in probability depending on where you are on the curve.
    </p>

    <h2>Why This Matters for Coefficients</h2>

    <p>
      In linear regression, coefficients describe changes in the outcome itself.
    </p>

    <p>
      In logistic regression, coefficients describe changes in the logit.
    </p>

    <p>
      This makes interpretation slightly less direct.
    </p>

    <p>
      Analysts often convert results into odds ratios or probabilities for easier interpretation.
    </p>

    <h2>What Happens at Probability 0.5?</h2>

    <p>
      A probability of 0.5 represents an even chance.
    </p>

    <p>
      On the logit scale:
    </p>

    <div class="example-box">

      <p>
        Probability = 0.5 → Logit = 0
      </p>
    </div>

    <p>
      Zero is therefore a special point on the logit scale.
    </p>

    <h2>Why Probabilities Near 0 and 1 Behave Differently</h2>

    <p>
      Near the middle of the probability scale, small logit changes can produce noticeable probability changes.
    </p>

    <p>
      Near 0 or 1, the same logit change may produce much smaller probability changes.
    </p>

    <p>
      This nonlinear relationship is a key feature of logistic regression.
    </p>

    <div class="concept-box">

      <strong>Important perspective:</strong>

      <p>
        Equal changes in logits do not necessarily correspond to equal changes in probability.
      </p>

    </div>

    <h2>Logits Make Regression Possible</h2>

    <p>
      The logit transformation allows logistic regression to:
    </p>

    <ul class="bullets">

      <li>Use linear predictors</li>

      <li>Maintain valid probabilities</li>

      <li>Avoid impossible predictions</li>

      <li>Model binary outcomes effectively</li>

    </ul>

    <p>
      Without this transformation, standard regression techniques would not work well for binary outcomes.
    </p>

    <h2>The Bigger Picture</h2>

    <p>
      Logistic regression appears to predict probabilities directly, but internally it operates on the logit scale.
    </p>

    <p>
      This transformation converts a bounded quantity into one that can be modeled using linear methods.
    </p>

    <p>
      Understanding this distinction provides the foundation for interpreting odds and odds ratios.
    </p>

    <div class="concept-box">

      <strong>Core message:</strong>

      <p>
        Probabilities describe chances between 0 and 1, while logits transform those probabilities onto an unrestricted scale. Logistic regression models logits because they can be analyzed using linear regression principles while still producing valid probabilities.
      </p>

    </div>

    <h2>Looking Ahead</h2>

    <p>
      The logit is built from another important concept: odds.
    </p>

    <p>
      Odds provide the bridge between probabilities and logits and are central to interpreting logistic regression results.
    </p>

    <p>
      The next lesson introduces odds and explains how they differ from probabilities.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Probabilities are restricted to values between 0 and 1</li>

        <li>Directly modeling probabilities creates challenges for regression</li>

        <li>Logits transform probabilities onto an unrestricted scale</li>

        <li>Logistic regression is linear in the logit, not in the probability</li>

        <li>The logistic curve converts logits back into probabilities</li>

        <li>Probability 0.5 corresponds to a logit of 0</li>

        <li>Equal changes in logits do not imply equal probability changes</li>

        <li>The logit transformation makes binary outcome modeling possible</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/modeling/extensions/logistic-regression/">
         ← Previous: Logistic Regression
      </a>

      <a class="btn"
         href="/modeling/extensions/odds/">
         Next: Odds →
      </a>

    </div>

  </div>

</section>