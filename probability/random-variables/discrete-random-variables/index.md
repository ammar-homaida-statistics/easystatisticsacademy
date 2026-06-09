---
layout: default
title: Discrete Random Variables
description: Learn what discrete random variables are, how they differ from continuous variables, and how probabilities are assigned to countable outcomes.
permalink: /probability/random-variables/discrete-random-variables/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_probability_random_variables_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/probability/random-variables/discrete-random-variables/",
    label: "Discrete Random Variables",
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
      <span class="badge">Discrete Variables</span>
    </div>

    <h1>Discrete Random Variables</h1>

    <p class="lead">
      Many random variables take values that can be counted one by one.
    </p>

    <p class="lead">
      These variables are called discrete random variables and form the foundation of many probability models involving counts and occurrences.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/probability/random-variables/what-is-a-random-variable/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/probability/random-variables/continuous-random-variables/">
         Next: Continuous Random Variables →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>What Is a Discrete Random Variable?</h2>

    <p>
      A discrete random variable can take only a countable set of possible values.
    </p>

    <p>
      The values may be finite or countably infinite,
      but they can always be listed individually.
    </p>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        Discrete random variables have distinct, countable outcomes.
      </p>

    </div>

    <h2>Examples of Discrete Random Variables</h2>

    <div class="example-box">

      <p>
        Number of children in a family
      </p>

      <p>
        Number of customers entering a store
      </p>

      <p>
        Number of defective products in a shipment
      </p>

      <p>
        Number of goals scored in a match
      </p>

    </div>

    <p>
      Each example involves counting occurrences.
    </p>

    <p>
      Fractional values such as 2.5 children or 3.7 defects are not possible.
    </p>

    <h2>A Simple Coin Toss Example</h2>

    <p>
      Suppose a coin is tossed once.
    </p>

    <p>
      Define:
    </p>

    <div class="example-box">

      <p>
        X = Number of heads observed
      </p>

    </div>

    <p>
      The possible values are:
    </p>

    <div class="example-box">

      <p>
        X = 0
      </p>

      <p>
        X = 1
      </p>

    </div>

    <p>
      No other values are possible.
    </p>

    <h2>A Die-Roll Example</h2>

    <p>
      Let:
    </p>

    <div class="example-box">

      <p>
        X = Number shown on a fair six-sided die
      </p>

    </div>

    <p>
      Then:
    </p>

    <div class="example-box">

      <p>
        X ∈ {1, 2, 3, 4, 5, 6}
      </p>

    </div>

    <p>
      The variable has six possible outcomes.
    </p>

    <h2>Probability Mass Function (PMF)</h2>

    <p>
      For discrete random variables,
      probabilities are assigned directly to individual values.
    </p>

    <p>
      The function describing these probabilities is called the probability mass function.
    </p>

    <div class="concept-box">

      <strong>Definition:</strong>

      <p>
        A probability mass function gives the probability associated with each possible value of a discrete random variable.
      </p>

    </div>

    <h2>PMF Notation</h2>

    <p>
      The probability that a discrete random variable takes a specific value is written as:
    </p>

    0

    <p>
      where x is a particular possible value.
    </p>

    <h2>PMF Example: Fair Die</h2>

    <p>
      For a fair die:
    </p>

    <div class="example-box">

      <p>
        P(X = 1) = 1/6
      </p>

      <p>
        P(X = 2) = 1/6
      </p>

      <p>
        ...
      </p>

      <p>
        P(X = 6) = 1/6
      </p>

    </div>

    <p>
      Every outcome has equal probability.
    </p>

    <h2>Properties of a PMF</h2>

    <p>
      Every probability mass function must satisfy two conditions.
    </p>

    <h3>Property 1: Non-Negativity</h3>

    <p>
      Every probability must be nonnegative.
    </p>

    1

    <h3>Property 2: Total Probability Equals One</h3>

    <p>
      The probabilities of all possible outcomes must sum to one.
    </p>

    2

    <p>
      This reflects the fact that one of the possible outcomes must occur.
    </p>

    <h2>Example: Number of Heads in Two Tosses</h2>

    <p>
      Suppose two fair coins are tossed.
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
      Possible outcomes:
    </p>

    <div class="example-box">

      <p>
        HH → 2 heads
      </p>

      <p>
        HT → 1 head
      </p>

      <p>
        TH → 1 head
      </p>

      <p>
        TT → 0 heads
      </p>

    </div>

    <p>
      Therefore:
    </p>

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
            <td>0.25</td>
          </tr>

          <tr>
            <td>1</td>
            <td>0.50</td>
          </tr>

          <tr>
            <td>2</td>
            <td>0.25</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>Visualizing a PMF</h2>

    <p>
      Probability mass functions are often displayed using bar charts.
    </p>

    <p>
      Each bar represents the probability associated with a specific value.
    </p>

    <p>
      Because the variable is discrete,
      gaps may exist between values.
    </p>

    <h2>Discrete Does Not Mean Small</h2>

    <p>
      Some students mistakenly believe discrete variables always have only a few values.
    </p>

    <p>
      This is not true.
    </p>

    <div class="example-box">

      <p>
        Number of emails received
      </p>

      <p>
        Number of website visits
      </p>

      <p>
        Number of customers arriving
      </p>

    </div>

    <p>
      These variables may take many possible values,
      but they remain countable.
    </p>

    <h2>Finite and Infinite Discrete Variables</h2>

    <p>
      Some discrete variables have a finite number of outcomes.
    </p>

    <div class="example-box">

      <p>
        Die roll: six outcomes
      </p>
    </div>

    <p>
      Others have infinitely many possible values.
    </p>

    <div class="example-box">

      <p>
        Number of customers arriving today
      </p>
    </div>

    <p>
      In principle,
      there is no upper limit.
    </p>

    <p>
      Both are discrete because the values remain countable.
    </p>

    <h2>Why Discrete Random Variables Matter</h2>

    <p>
      Discrete random variables appear throughout statistics and data science.
    </p>

    <ul class="bullets">

      <li>Counting defects</li>

      <li>Counting successes</li>

      <li>Counting arrivals</li>

      <li>Counting purchases</li>

      <li>Counting events over time</li>

    </ul>

    <p>
      Many important probability distributions are built for discrete variables.
    </p>

    <h2>Examples of Future Distributions</h2>

    <p>
      Later probability courses study distributions such as:
    </p>

    <ul class="bullets">

      <li>Bernoulli distribution</li>

      <li>Binomial distribution</li>

      <li>Poisson distribution</li>

    </ul>

    <p>
      Each of these describes a specific type of discrete random variable.
    </p>

    <h2>Discrete vs Continuous Thinking</h2>

    <p>
      Discrete variables count outcomes.
    </p>

    <p>
      Continuous variables measure quantities.
    </p>

    <div class="example-box">

      <p>
        Number of students → Discrete
      </p>

      <p>
        Height of students → Continuous
      </p>

    </div>

    <p>
      This distinction affects how probabilities are calculated.
    </p>

    <h2>Looking Ahead</h2>

    <p>
      Not all random variables are countable.
    </p>

    <p>
      Many important measurements,
      such as height,
      weight,
      temperature,
      and time,
      can take values from a continuum.
    </p>

    <p>
      The next lesson introduces continuous random variables and explains how probability behaves differently when infinitely many values are possible.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>Discrete random variables have countable possible values</li>

        <li>They are commonly used to represent counts</li>

        <li>Probabilities are assigned through a probability mass function (PMF)</li>

        <li>PMFs must contain nonnegative probabilities</li>

        <li>All PMF probabilities must sum to one</li>

        <li>Discrete variables may have finite or countably infinite outcomes</li>

        <li>Many important probability distributions are discrete</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/probability/random-variables/what-is-a-random-variable/">
         ← Previous: What Is a Random Variable?
      </a>

      <a class="btn"
         href="/probability/random-variables/continuous-random-variables/">
         Next: Continuous Random Variables →
      </a>

    </div>

  </div>

</section>