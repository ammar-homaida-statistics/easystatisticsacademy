---
layout: default
title: Binomial Distribution
description: Learn how the binomial distribution models the number of successes in a fixed number of independent Bernoulli trials.
permalink: /probability/distributions/binomial-distribution/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_probability_distributions_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/probability/distributions/binomial-distribution/",
    label: "Binomial Distribution",
    ts: Date.now()
  }));

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Probability</span>
      <span class="badge">Block 5</span>
      <span class="badge">Distributions</span>
      <span class="badge">Discrete</span>
    </div>

    <h1>Binomial Distribution</h1>

    <p class="lead">
      The Bernoulli distribution models a single success-or-failure trial.
    </p>

    <p class="lead">
      The binomial distribution extends this idea to multiple independent trials and counts the total number of successes.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/probability/distributions/bernoulli-distribution/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/probability/distributions/geometric-distribution/">
         Next: Geometric Distribution →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>What Is a Binomial Distribution?</h2>

    <p>
      A binomial distribution describes the number of successes obtained in a fixed number of independent Bernoulli trials.
    </p>

    <div class="concept-box">

      <strong>Definition:</strong>

      <p>
        A binomial random variable counts how many successes occur in n independent trials when each trial has success probability p.
      </p>

    </div>

    <h2>The Four Conditions</h2>

    <p>
      A situation follows a binomial distribution when all four conditions are satisfied.
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Condition</th>
            <th>Description</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Fixed Number of Trials</td>
            <td>The number of trials is predetermined.</td>
          </tr>

          <tr>
            <td>Independent Trials</td>
            <td>One outcome does not affect another.</td>
          </tr>

          <tr>
            <td>Two Outcomes</td>
            <td>Success or failure.</td>
          </tr>

          <tr>
            <td>Constant Probability</td>
            <td>The success probability remains the same.</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>A Coin Toss Example</h2>

    <p>
      Suppose a fair coin is tossed 10 times.
    </p>

    <p>
      Let:
    </p>

    <div class="example-box">

      <p>
        X = Number of heads
      </p>
    </div>

    <p>
      Then X follows a binomial distribution because:
    </p>

    <ul class="bullets">

      <li>There are 10 trials.</li>

      <li>Each toss is independent.</li>

      <li>Each toss results in heads or tails.</li>

      <li>The probability of heads remains 0.5.</li>

    </ul>

    <h2>Notation</h2>

    <p>
      A binomial random variable is written as:
    </p>

    0

    <p>
      where:
    </p>

    <ul class="bullets">

      <li>n = number of trials</li>

      <li>p = probability of success</li>

    </ul>

    <h2>Possible Values</h2>

    <p>
      A binomial variable can take values:
    </p>

    1

    <p>
      because any number of successes from zero to n is possible.
    </p>

    <h2>The Probability Formula</h2>

    <p>
      The probability of observing exactly k successes is:
    </p>

    2

    <p>
      This is called the binomial probability mass function.
    </p>

    <h2>Understanding the Formula</h2>

    <p>
      The formula contains three parts.
    </p>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Part</th>
            <th>Meaning</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>n choose k</td>
            <td>Number of possible arrangements</td>
          </tr>

          <tr>
            <td>p<sup>k</sup></td>
            <td>Probability of k successes</td>
          </tr>

          <tr>
            <td>(1-p)<sup>n-k</sup></td>
            <td>Probability of remaining failures</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>The Combination Term</h2>

    <p>
      The notation:
    </p>

    3

    <p>
      counts the number of ways k successes can be placed among n trials.
    </p>

    <p>
      It is read as:
    </p>

    <div class="example-box">

      <p>
        "n choose k"
      </p>

    </div>

    <h2>Example: Exactly Two Heads</h2>

    <p>
      Suppose:
    </p>

    <div class="example-box">

      <p>
        n = 3
      </p>

      <p>
        p = 0.5
      </p>

    </div>

    <p>
      What is the probability of exactly two heads?
    </p>

    <p>
      Applying the formula:
    </p>

    4

    <p>
      Since:
    </p>

    5

    <p>
      the probability becomes:
    </p>

    6

    <h2>Mean of a Binomial Distribution</h2>

    <p>
      The expected value is:
    </p>

    7

    <div class="concept-box">

      <strong>Interpretation:</strong>

      <p>
        The expected number of successes equals the number of trials multiplied by the success probability.
      </p>

    </div>

    <h2>Example of the Mean</h2>

    <p>
      If:
    </p>

    <div class="example-box">

      <p>
        n = 100
      </p>

      <p>
        p = 0.2
      </p>

    </div>

    <p>
      Then:
    </p>

    8

    <p>
      We expect about 20 successes.
    </p>

    <h2>Variance of a Binomial Distribution</h2>

    <p>
      The variance is:
    </p>

    9

    <p>
      The standard deviation is:
    </p>

    10

    <h2>Why the Formula Makes Sense</h2>

    <p>
      A binomial variable is the sum of n independent Bernoulli variables.
    </p>

    <p>
      Since each Bernoulli trial has:
    </p>

    11

    <p>
      the variances add together:
    </p>

    12

    <h2>Shape of the Distribution</h2>

    <p>
      The shape depends on p.
    </p>

    <div class="example-box">

      <p>
        p = 0.5 → symmetric
      </p>

      <p>
        p &lt; 0.5 → right-skewed
      </p>

      <p>
        p &gt; 0.5 → left-skewed
      </p>

    </div>

    <p>
      As n increases,
      the distribution becomes more bell-shaped.
    </p>

    <h2>Real-World Applications</h2>

    <ul class="bullets">

      <li>Number of customers who purchase a product</li>

      <li>Number of defective items in a batch</li>

      <li>Number of successful sales calls</li>

      <li>Number of patients responding to treatment</li>

      <li>Number of voters supporting a candidate</li>

    </ul>

    <p>
      Any situation involving repeated success/failure trials may be modeled with a binomial distribution.
    </p>

    <h2>Bernoulli Versus Binomial</h2>

    <div class="table-wrap">

      <table>

        <thead>
          <tr>
            <th>Distribution</th>
            <th>Models</th>
          </tr>
        </thead>

        <tbody>

          <tr>
            <td>Bernoulli</td>
            <td>One trial</td>
          </tr>

          <tr>
            <td>Binomial</td>
            <td>Multiple trials</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      The binomial distribution is essentially a collection of Bernoulli trials summarized by their total number of successes.
    </p>

    <h2>The Limitation</h2>

    <p>
      The binomial distribution answers:
    </p>

    <div class="example-box">

      <p>
        How many successes occur in n trials?
      </p>

    </div>

    <p>
      Sometimes we are interested in a different question:
    </p>

    <div class="example-box">

      <p>
        How long must we wait until the first success occurs?
      </p>

    </div>

    <p>
      This leads to the geometric distribution.
    </p>

    <h2>Looking Ahead</h2>

    <p>
      The geometric distribution models the number of trials required to obtain the first success.
    </p>

    <p>
      It introduces waiting-time models, an important class of probability distributions.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>A binomial distribution counts successes in n independent Bernoulli trials</li>

        <li>Binomial variables are written as Bin(n,p)</li>

        <li>The probability formula uses combinations and success probabilities</li>

        <li>The mean equals np</li>

        <li>The variance equals np(1 − p)</li>

        <li>The binomial distribution is built from repeated Bernoulli trials</li>

        <li>It is widely used for modeling repeated success/failure experiments</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/probability/distributions/bernoulli-distribution/">
         ← Previous: Bernoulli Distribution
      </a>

      <a class="btn"
         href="/probability/distributions/geometric-distribution/">
         Next: Geometric Distribution →
      </a>

    </div>

  </div>

</section>