---
layout: default
title: Geometric Distribution
description: Learn how the geometric distribution models waiting times and answers the question: how many trials are needed until the first success occurs?
permalink: /probability/distributions/geometric-distribution/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_probability_distributions_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/probability/distributions/geometric-distribution/",
    label: "Geometric Distribution",
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
      <span class="badge">Waiting Times</span>
    </div>

    <h1>Geometric Distribution</h1>

    <p class="lead">
      The binomial distribution counts how many successes occur in a fixed number of trials.
    </p>

    <p class="lead">
      The geometric distribution answers a different question: how many trials are required until the first success occurs?
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/probability/distributions/binomial-distribution/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/probability/distributions/negative-binomial-distribution/">
         Next: Negative Binomial Distribution →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>What Is a Geometric Distribution?</h2>

    <p>
      A geometric distribution models the number of trials needed to obtain the first success in a sequence of independent Bernoulli trials.
    </p>

    <div class="concept-box">

      <strong>Definition:</strong>

      <p>
        A geometric random variable counts how many trials occur before the first success is observed.
      </p>

    </div>

    <h2>The Main Question</h2>

    <p>
      Unlike the binomial distribution,
      which counts successes,
      the geometric distribution measures waiting time.
    </p>

    <div class="example-box">

      <p>
        How many coin tosses until the first head?
      </p>

      <p>
        How many customers until the first purchase?
      </p>

      <p>
        How many calls until the first sale?
      </p>

      <p>
        How many inspections until the first defect?
      </p>

    </div>

    <h2>Conditions for a Geometric Distribution</h2>

    <p>
      A geometric model applies when:
    </p>

    <ul class="bullets">

      <li>Trials are independent.</li>

      <li>Each trial has two outcomes.</li>

      <li>The probability of success remains constant.</li>

      <li>We are interested in the first success.</li>

    </ul>

    <p>
      These conditions are very similar to those of the binomial distribution.
    </p>

    <h2>Notation</h2>

    <p>
      A geometric random variable is commonly written as:
    </p>

    0

    <p>
      where p represents the probability of success on each trial.
    </p>

    <h2>Possible Values</h2>

    <p>
      The first success may occur:
    </p>

    <div class="example-box">

      <p>
        On trial 1
      </p>

      <p>
        On trial 2
      </p>

      <p>
        On trial 3
      </p>

      <p>
        And so on...
      </p>

    </div>

    <p>
      Therefore the possible values are:
    </p>

    1

    <h2>The Probability Formula</h2>

    <p>
      The probability that the first success occurs on trial k is:
    </p>

    2

    <p>
      This formula contains two parts:
    </p>

    <ul class="bullets">

      <li>k − 1 failures</li>

      <li>One success on trial k</li>

    </ul>

    <h2>Understanding the Formula</h2>

    <p>
      To achieve the first success on trial k:
    </p>

    <div class="example-box">

      <p>
        Trial 1: Failure
      </p>

      <p>
        Trial 2: Failure
      </p>

      <p>
        ...
      </p>

      <p>
        Trial k − 1: Failure
      </p>

      <p>
        Trial k: Success
      </p>

    </div>

    <p>
      Multiplying those probabilities gives the geometric formula.
    </p>

    <h2>Example: Coin Tosses</h2>

    <p>
      Suppose a fair coin is tossed repeatedly.
    </p>

    <p>
      Let:
    </p>

    <div class="example-box">

      <p>
        X = Trial on which the first head appears
      </p>

    </div>

    <p>
      Since:
    </p>

    3

    <p>
      The probability that the first head occurs on toss 3 is:
    </p>

    4

    <p>
      Two tails followed by one head.
    </p>

    <h2>The Mean of a Geometric Distribution</h2>

    <p>
      The expected value is:
    </p>

    5

    <div class="concept-box">

      <strong>Interpretation:</strong>

      <p>
        The expected waiting time until the first success equals the reciprocal of the success probability.
      </p>

    </div>

    <h2>Example of the Mean</h2>

    <p>
      If:
    </p>

    <div class="example-box">

      <p>
        p = 0.25
      </p>

    </div>

    <p>
      Then:
    </p>

    6

    <p>
      On average,
      four trials are needed before the first success.
    </p>

    <h2>The Variance</h2>

    <p>
      The variance of a geometric distribution is:
    </p>

    7

    <p>
      Variability increases as successes become rarer.
    </p>

    <h2>Rare Successes Mean Longer Waiting Times</h2>

    <p>
      As p decreases:
    </p>

    <ul class="bullets">

      <li>The mean increases.</li>

      <li>The variance increases.</li>

      <li>The distribution becomes more spread out.</li>

    </ul>

    <p>
      Rare events require longer waits on average.
    </p>

    <h2>The Memoryless Property</h2>

    <p>
      The geometric distribution has a remarkable property called memorylessness.
    </p>

    <div class="concept-box">

      <strong>Memoryless Property:</strong>

      <p>
        Past failures do not affect future waiting times.
      </p>

    </div>

    <h2>What Memoryless Means</h2>

    <p>
      Suppose you have already observed ten failures.
    </p>

    <p>
      The probability of success on the next trial remains:
    </p>

    8

    <p>
      exactly as before.
    </p>

    <p>
      Previous failures provide no additional information about future success.
    </p>

    <h2>A Common Misconception</h2>

    <p>
      People often believe that after many failures,
      success becomes "due."
    </p>

    <div class="example-box">

      <p>
        "The coin has landed tails ten times.
        Heads must come soon."
      </p>

    </div>

    <p>
      This is known as the gambler's fallacy.
    </p>

    <p>
      For independent trials,
      the probability remains unchanged.
    </p>

    <h2>Geometric Versus Binomial</h2>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Distribution</th>
            <th>Question Answered</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>Binomial</td>
            <td>How many successes occur?</td>
          </tr>

          <tr>
            <td>Geometric</td>
            <td>How long until the first success?</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      Both distributions arise from repeated Bernoulli trials but answer different questions.
    </p>

    <h2>Applications of the Geometric Distribution</h2>

    <ul class="bullets">

      <li>Waiting for the first customer purchase</li>

      <li>Waiting for the first equipment failure</li>

      <li>Waiting for the first successful network transmission</li>

      <li>Waiting for the first disease detection</li>

      <li>Waiting for the first sales conversion</li>

    </ul>

    <p>
      Any first-success waiting problem may be modeled geometrically.
    </p>

    <h2>The Shape of the Distribution</h2>

    <p>
      Geometric distributions are always right-skewed.
    </p>

    <p>
      Small waiting times are common,
      while very long waiting times become progressively less likely.
    </p>

    <p>
      The probability decreases exponentially as the number of trials increases.
    </p>

    <h2>The Limitation</h2>

    <p>
      The geometric distribution focuses on the first success only.
    </p>

    <p>
      Sometimes we want to know:
    </p>

    <div class="example-box">

      <p>
        How many trials are needed until the fifth success?
      </p>

      <p>
        How many customers until the third purchase?
      </p>

    </div>

    <p>
      This broader waiting-time problem leads to the negative binomial distribution.
    </p>

    <h2>Looking Ahead</h2>

    <p>
      The negative binomial distribution generalizes the geometric distribution.
    </p>

    <p>
      Instead of waiting for the first success,
      it models the number of trials required to achieve a specified number of successes.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>The geometric distribution models waiting time until the first success</li>

        <li>It arises from repeated independent Bernoulli trials</li>

        <li>The probability formula is P(X = k) = (1 − p)<sup>k−1</sup>p</li>

        <li>The mean equals 1/p</li>

        <li>The variance equals (1 − p)/p²</li>

        <li>The geometric distribution is memoryless</li>

        <li>It is commonly used for first-success waiting-time problems</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/probability/distributions/binomial-distribution/">
         ← Previous: Binomial Distribution
      </a>

      <a class="btn"
         href="/probability/distributions/negative-binomial-distribution/">
         Next: Negative Binomial Distribution →
      </a>

    </div>

  </div>

</section>