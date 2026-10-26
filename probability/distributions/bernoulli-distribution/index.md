---
layout: default
title: Bernoulli Distribution
description: Learn the Bernoulli distribution, the simplest probability distribution for modeling a single success-or-failure outcome.
permalink: /probability/distributions/bernoulli-distribution/
sidebar: false
translation_pair: bernoulli-distribution
math: true
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_probability_distributions_lesson_v0";

  try {
    localStorage.setItem(KEY, JSON.stringify({
    url: "/probability/distributions/bernoulli-distribution/",
    label: "Bernoulli Distribution",
    ts: Date.now()
    }));
  } catch (_) {
    // Storage may be disabled; the lesson must still load and remain navigable.
  }

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
<p><a href="/ar/probability/distributions/bernoulli-distribution/" lang="ar" dir="rtl">اقرأ الدرس باللغة العربية</a></p>

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
      Each example can be encoded into two categories, success and failure. The labels must be defined for the question being studied.
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

    \[
P(\text{failure})=1-p
\]

    <h2>The Probability Mass Function</h2>

    <p>
      The Bernoulli distribution has the following probability mass function:
    </p>

    \[
P(X=1)=p
\]

    <p>
      and:
    </p>

    \[
P(X=0)=1-p
\]

    <p>
      These two probabilities always sum to one.
    </p>

    <!-- Batch #72: shared Bernoulli numerical probability explorer -->
<section class="concept-box esa-bern-lab" id="esa-bernoulli-explorer" aria-labelledby="esa-bern-heading">
<h2 id="esa-bern-heading">Interactive Bernoulli Distribution Explorer</h2>
<p>Set the probability of success <strong>p</strong> and observe the probabilities of failure and success, the expected value and the variance. At p=0 or p=1 the distribution is degenerate: the outcome is certain and the variance is zero.</p>
<label for="esa-bern-p">Success probability p (0–1)</label>
<input id="esa-bern-p" type="number" min="0" max="1" step="any" value="0.3" inputmode="decimal">
<button id="esa-bern-reset" type="button" class="btn btn-outline">Restore example</button>
<p id="esa-bern-error" role="alert" hidden></p>
<div class="table-wrap"><table><caption>Bernoulli distribution results (six decimal places)</caption>
<tbody><tr><th scope="row">P(X=0) = 1−p</th><td id="esa-bern-p0">—</td></tr>
<tr><th scope="row">P(X=1) = p</th><td id="esa-bern-p1">—</td></tr>
<tr><th scope="row">Mean E(X) = p</th><td id="esa-bern-mean">—</td></tr>
<tr><th scope="row">Variance Var(X) = p(1−p)</th><td id="esa-bern-variance">—</td></tr></tbody></table></div>
<svg id="esa-bern-chart" role="img" viewBox="0 0 610 260" aria-label="Bernoulli probabilities for failure and success"></svg>
<p class="muted-mini">The bars display the two point probabilities, not continuous densities. Changing the parameter recalculates the exact formulas directly.</p>
</section>
<script src="/js/bernoulli-explorer.js" defer></script>
<style>
.esa-bern-lab{max-width:100%;min-width:0;box-sizing:border-box;overflow-wrap:anywhere}
.esa-bern-lab *{box-sizing:border-box}
.esa-bern-lab label{display:block;font-weight:650;margin-bottom:6px}
.esa-bern-lab input{display:block;width:min(100%,290px);padding:10px;font:inherit;border:1px solid #777;border-radius:6px;margin-bottom:12px}
.esa-bern-lab .table-wrap{max-width:100%;overflow-x:auto}
.esa-bern-lab svg{display:block;width:100%;height:auto;max-width:610px}
.esa-bern-lab [hidden]{display:none!important}
.esa-bern-lab :is(input,button):focus-visible{outline:2px solid #0f766e;outline-offset:3px}
</style>
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

    \[
p=\tfrac12
\]

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

    \[
\operatorname{E}(X)=0(1-p)+1p
\]

    <p>
      Simplifying:
    </p>

    \[
\operatorname{E}(X)=p
\]

    <div class="concept-box">

      <strong>Result:</strong>

      <p>
        The mean of a Bernoulli distribution equals its success probability.
      </p>

    </div>

    <h2>Interpreting the Mean</h2>

    <p>
      For repeated identically distributed Bernoulli trials, the expected value equals the success probability; with independent repetitions, the observed proportion also converges to p in the long run.
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

    \[
\operatorname{Var}(X)=\operatorname{E}(X^2)-[\operatorname{E}(X)]^2=p-p^2=p(1-p)
\]

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

    \[
p=\frac12
\]

    <p>
      In that case:
    </p>

    \[
\operatorname{Var}(X)=\tfrac12(1-\tfrac12)=\tfrac14=0.25
\]

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
      Each zero–one event indicator has a Bernoulli distribution with p equal to that event's probability; indicators need not be independent of each other.
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
      If those trials are independent and have the same success probability p, their total successes follow a binomial distribution. Without these conditions, the count need not be binomial.
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