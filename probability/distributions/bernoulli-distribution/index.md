---
layout: default
title: Bernoulli Distribution
description: Learn the Bernoulli distribution, the simplest probability distribution for modeling a single success-or-failure outcome.
permalink: /probability/distributions/bernoulli-distribution/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_probability_distributions_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/probability/distributions/bernoulli-distribution/",
    label: "Bernoulli Distribution",
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

    <h1>Bernoulli Distribution</h1>

    <p class="lead">
      Many random processes have only two possible outcomes: success or failure.
    </p>

    <p class="lead">
      The Bernoulli distribution is the simplest probability distribution and serves as the foundation for many other distributions in probability and statistics.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/probability/distributions/">
         ← Distributions Home
      </a>

      <a class="btn btn-outline"
         href="/probability/distributions/binomial-distribution/">
         Next: Binomial Distribution →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>What Is a Bernoulli Distribution?</h2>

    <p>
      A Bernoulli distribution describes a random variable with exactly two possible outcomes.
    </p>

    <div class="concept-box">

      <strong>Definition:</strong>

      <p>
        A Bernoulli random variable takes the value 1 for success and 0 for failure.
      </p>

    </div>

    <h2>Examples of Bernoulli Outcomes</h2>

    <div class="example-box">

      <p>
        Coin toss: Heads or tails
      </p>

      <p>
        Exam result: Pass or fail
      </p>

      <p>
        Email: Spam or not spam
      </p>

      <p>
        Customer: Purchase or no purchase
      </p>

      <p>
        Advertisement: Click or no click
      </p>

    </div>

    <p>
      Each situation has only two possible outcomes.
    </p>

    <h2>The Bernoulli Random Variable</h2>

    <p>
      Let X be a Bernoulli random variable.
    </p>

    <div class="example-box">

      <p>
        X = 1 if success occurs
      </p>

      <p>
        X = 0 if failure occurs
      </p>

    </div>

    <p>
      The probability of success is denoted by p.
    </p>

    <p>
      The probability of failure is:
    </p>

    0

    <h2>The Probability Mass Function</h2>

    <p>
      The Bernoulli distribution has the following probability mass function:
    </p>

    1

    <p>
      and:
    </p>

    2

    <p>
      These two probabilities always sum to one.
    </p>

    <h2>A Coin Toss Example</h2>

    <p>
      Suppose a fair coin is tossed.
    </p>

    <p>
      Define:
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
      Since the coin is fair:
    </p>

    3

    <p>
      Therefore:
    </p>

    <div class="example-box">

      <p>
        P(X=1)=0.5
      </p>

      <p>
        P(X=0)=0.5
      </p>

    </div>

    <h2>The Distribution Table</h2>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>x</th>
            <th>P(X=x)</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>0</td>
            <td>1 − p</td>
          </tr>

          <tr>
            <td>1</td>
            <td>p</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      Every Bernoulli distribution can be summarized using this table.
    </p>

    <h2>Expected Value of a Bernoulli Variable</h2>

    <p>
      Using the expectation formula:
    </p>

    4

    <p>
      Simplifying:
    </p>

    5

    <div class="concept-box">

      <strong>Result:</strong>

      <p>
        The mean of a Bernoulli distribution equals its success probability.
      </p>

    </div>

    <h2>Interpreting the Mean</h2>

    <p>
      The expected value represents the long-run proportion of successes.
    </p>

    <div class="example-box">

      <p>
        If p = 0.70,
        approximately 70% of trials are expected to be successes.
      </p>

    </div>

    <h2>Variance of a Bernoulli Variable</h2>

    <p>
      The variance of a Bernoulli random variable is:
    </p>

    6

    <p>
      This formula appears frequently throughout probability theory.
    </p>

    <h2>How Variance Changes with p</h2>

    <p>
      Variance depends on both success and failure probabilities.
    </p>

    <div class="example-box">

      <p>
        If p is near 0 or 1,
        variability is small.
      </p>

      <p>
        If p is near 0.5,
        variability is larger.
      </p>

    </div>

    <p>
      Maximum uncertainty occurs when success and failure are equally likely.
    </p>

    <h2>The Maximum Variance</h2>

    <p>
      Variance is largest when:
    </p>

    7

    <p>
      In that case:
    </p>

    8

    <p>
      This is the maximum possible Bernoulli variance.
    </p>

    <h2>Bernoulli Variables and Indicators</h2>

    <p>
      Bernoulli random variables are essentially the same as indicator variables.
    </p>

    <div class="example-box">

      <p>
        Success → 1
      </p>

      <p>
        Failure → 0
      </p>

    </div>

    <p>
      The indicator variables studied previously follow Bernoulli distributions.
    </p>

    <h2>Why Bernoulli Distributions Matter</h2>

    <p>
      Although simple,
      Bernoulli distributions are the building blocks of many more complex models.
    </p>

    <div class="example-box">

      <p>
        Customer clicks
      </p>

      <p>
        Product defects
      </p>

      <p>
        Medical test outcomes
      </p>

      <p>
        Fraud detection
      </p>

    </div>

    <p>
      Many real-world systems begin with binary outcomes.
    </p>

    <h2>From One Trial to Many Trials</h2>

    <p>
      A Bernoulli distribution describes a single trial.
    </p>

    <p>
      What happens when we repeat the trial many times?
    </p>

    <div class="example-box">

      <p>
        Ten coin tosses
      </p>

      <p>
        One hundred customer visits
      </p>

      <p>
        Fifty quality inspections
      </p>

    </div>

    <p>
      The resulting count of successes follows a different distribution.
    </p>

    <p>
      That distribution is the binomial distribution.
    </p>

    <h2>Applications in Data Science</h2>

    <p>
      Bernoulli variables appear throughout analytics and machine learning.
    </p>

    <ul class="bullets">

      <li>Binary classification labels</li>

      <li>Email spam detection</li>

      <li>Customer conversion analysis</li>

      <li>Medical diagnosis systems</li>

      <li>A/B testing outcomes</li>

    </ul>

    <p>
      They are among the most frequently used probability models.
    </p>

    <h2>The Big Picture</h2>

    <p>
      The Bernoulli distribution models the simplest possible random experiment.
    </p>

    <p>
      Despite its simplicity,
      it provides the foundation for many important probability distributions and statistical models.
    </p>

    <p>
      Understanding Bernoulli variables makes it easier to understand more advanced distributions.
    </p>

    <h2>Looking Ahead</h2>

    <p>
      A Bernoulli distribution models a single success-or-failure trial.
    </p>

    <p>
      The next lesson extends this idea to repeated independent trials and introduces one of the most important distributions in probability:
      the binomial distribution.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>A Bernoulli distribution has two possible outcomes: success and failure</li>

        <li>Bernoulli variables take values 1 and 0</li>

        <li>The probability of success is denoted by p</li>

        <li>The mean of a Bernoulli variable equals p</li>

        <li>The variance equals p(1 − p)</li>

        <li>Indicator variables follow Bernoulli distributions</li>

        <li>Bernoulli distributions are building blocks for many other probability models</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/probability/distributions/">
         Distributions Home
      </a>

      <a class="btn"
         href="/probability/distributions/binomial-distribution/">
         Next: Binomial Distribution →
      </a>

    </div>

  </div>

</section>