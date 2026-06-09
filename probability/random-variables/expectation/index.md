---
layout: default
title: Expectation
description: Learn how expected value summarizes the long-run average outcome of a random variable and serves as the center of a probability distribution.
permalink: /probability/random-variables/expectation/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_probability_random_variables_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/probability/random-variables/expectation/",
    label: "Expectation",
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
      <span class="badge">Center</span>
    </div>

    <h1>Expectation</h1>

    <p class="lead">
      Probability distributions describe possible outcomes and their probabilities.
    </p>

    <p class="lead">
      Expectation summarizes those outcomes with a single number that represents the long-run average value of a random variable.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/probability/random-variables/cumulative-distribution-function/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/probability/random-variables/variance-and-standard-deviation/">
         Next: Variance and Standard Deviation →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>What Is Expectation?</h2>

    <p>
      Expectation,
      also called the expected value,
      is the probability-weighted average of all possible values of a random variable.
    </p>

    <p>
      It describes the value we would expect to observe on average over many repetitions of a random process.
    </p>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        Expectation represents the long-run average outcome of a random variable.
      </p>

    </div>

    <h2>Why Expectation Matters</h2>

    <p>
      Individual outcomes are uncertain.
    </p>

    <p>
      However,
      when a random process is repeated many times,
      average behavior becomes predictable.
    </p>

    <div class="example-box">

      <p>
        A single die roll is unpredictable.
      </p>

      <p>
        Thousands of die rolls have a predictable average.
      </p>

    </div>

    <p>
      Expectation captures this average behavior.
    </p>

    <h2>The Expected Value Formula</h2>

    <p>
      For a discrete random variable:
    </p>

    0

    <p>
      This formula multiplies each possible value by its probability and then sums the results.
    </p>

    <h2>Understanding the Formula</h2>

    <p>
      The expected value is a weighted average.
    </p>

    <p>
      Values with larger probabilities contribute more heavily to the final result.
    </p>

    <div class="example-box">

      <p>
        Large probability → greater influence
      </p>

      <p>
        Small probability → less influence
      </p>

    </div>

    <p>
      The weights are the probabilities themselves.
    </p>

    <h2>Example: Fair Die</h2>

    <p>
      Let:
    </p>

    <div class="example-box">

      <p>
        X = Number shown on a fair die
      </p>

    </div>

    <p>
      Each outcome has probability 1/6.
    </p>

    <p>
      Therefore:
    </p>

    1

    <p>
      Simplifying:
    </p>

    2

    <h2>A Common Question</h2>

    <p>
      Can a random variable have an expected value that is not a possible outcome?
    </p>

    <p>
      Yes.
    </p>

    <div class="example-box">

      <p>
        A die can never show 3.5.
      </p>

      <p>
        Yet its expected value is 3.5.
      </p>

    </div>

    <p>
      Expectation describes an average,
      not necessarily an attainable outcome.
    </p>

    <h2>Example: Coin Toss</h2>

    <p>
      Define:
    </p>

    <div class="example-box">

      <p>
        X = 1 if Heads
      </p>

      <p>
        X = 0 if Tails
      </p>

    </div>

    <p>
      Since:
    </p>

    <div class="example-box">

      <p>
        P(Heads) = 0.5
      </p>

      <p>
        P(Tails) = 0.5
      </p>

    </div>

    <p>
      The expected value is:
    </p>

    3

    <p>
      This reflects the long-run proportion of heads.
    </p>

    <h2>Expectation and Long-Run Averages</h2>

    <p>
      If an experiment is repeated many times,
      the sample average tends to move toward the expected value.
    </p>

    <p>
      This principle is connected to the Law of Large Numbers,
      which will be studied later.
    </p>

    <div class="example-box">

      <p>
        More repetitions → average approaches expectation.
      </p>

    </div>

    <h2>Expectation in Everyday Life</h2>

    <p>
      Expected values appear in many real-world decisions.
    </p>

    <ul class="bullets">

      <li>Insurance pricing</li>

      <li>Investment analysis</li>

      <li>Risk management</li>

      <li>Quality control</li>

      <li>Business forecasting</li>

    </ul>

    <p>
      Many decisions are based on expected outcomes.
    </p>

    <h2>Expected Profit Example</h2>

    <p>
      Suppose a game pays:
    </p>

    <div class="example-box">

      <p>
        $100 with probability 0.10
      </p>

      <p>
        $0 with probability 0.90
      </p>

    </div>

    <p>
      The expected payout is:
    </p>

    4

    <p>
      The average payout over many plays is $10.
    </p>

    <h2>Expectation Is Not a Guarantee</h2>

    <p>
      Expected value describes average behavior,
      not individual outcomes.
    </p>

    <div class="example-box">

      <p>
        Expected payout = $10
      </p>

      <p>
        Actual payout = $0 or $100
      </p>

    </div>

    <p>
      Individual observations may differ substantially from the expectation.
    </p>

    <h2>Expectation for Continuous Variables</h2>

    <p>
      Continuous random variables also have expected values.
    </p>

    <p>
      The calculation uses probability densities rather than probability masses.
    </p>

    <p>
      Although the mathematical details differ,
      the interpretation remains the same:
      a probability-weighted average.
    </p>

    <h2>Properties of Expectation</h2>

    <p>
      Expectation has several useful mathematical properties.
    </p>

    <h3>Adding a Constant</h3>

    5

    <p>
      Adding a constant shifts the expected value by that amount.
    </p>

    <h3>Multiplying by a Constant</h3>

    6

    <p>
      Scaling the variable scales its expectation.
    </p>

    <h2>Expectation as the Center of a Distribution</h2>

    <p>
      Expectation is often viewed as a measure of center.
    </p>

    <p>
      It provides a single value around which the distribution balances.
    </p>

    <p>
      However,
      expectation alone does not describe variability.
    </p>

    <div class="example-box">

      <p>
        Two distributions can have the same expected value but very different spreads.
      </p>

    </div>

    <h2>The Limitation of Expectation</h2>

    <p>
      Knowing only the expected value is rarely sufficient.
    </p>

    <p>
      We also need to know how much outcomes vary around that average.
    </p>

    <p>
      This motivates the next major concept:
      variance.
    </p>

    <h2>Expectation and Statistics</h2>

    <p>
      Expected value plays a central role throughout probability and statistics.
    </p>

    <ul class="bullets">

      <li>Population means</li>

      <li>Statistical estimation</li>

      <li>Machine learning objectives</li>

      <li>Decision theory</li>

      <li>Economic models</li>

    </ul>

    <p>
      It is one of the most important summaries of a probability distribution.
    </p>

    <h2>Looking Ahead</h2>

    <p>
      Expectation tells us where a distribution is centered.
    </p>

    <p>
      The next question is:
    </p>

    <div class="example-box">

      <p>
        How far do observations tend to fall from that center?
      </p>

    </div>

    <p>
      The next lesson introduces variance and standard deviation,
      the primary measures of variability in probability distributions.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Expectation is the probability-weighted average of a random variable</li>

        <li>Expected value represents long-run average behavior</li>

        <li>Expectation may not be a possible outcome</li>

        <li>Expected value is a measure of the center of a distribution</li>

        <li>Expectation is widely used in decision-making and statistical modeling</li>

        <li>Expected value describes average behavior, not guaranteed outcomes</li>

        <li>Expectation alone does not describe variability</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/probability/random-variables/cumulative-distribution-function/">
         ← Previous: Cumulative Distribution Function
      </a>

      <a class="btn"
         href="/probability/random-variables/variance-and-standard-deviation/">
         Next: Variance and Standard Deviation →
      </a>

    </div>

  </div>

</section>