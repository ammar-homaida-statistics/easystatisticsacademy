---
layout: default
title: Poisson Distribution
description: Learn how the Poisson distribution models counts of events occurring within a fixed interval of time, space, or area.
permalink: /probability/distributions/poisson-distribution/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_probability_distributions_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/probability/distributions/poisson-distribution/",
    label: "Poisson Distribution",
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
      <span class="badge">Count Models</span>
    </div>

    <h1>Poisson Distribution</h1>

    <p class="lead">
      Many real-world problems involve counting how often events occur.
    </p>

    <p class="lead">
      The Poisson distribution provides a powerful model for counts of events occurring within a fixed interval of time, space, area, or volume.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/probability/distributions/negative-binomial-distribution/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/probability/distributions/hypergeometric-distribution/">
         Next: Hypergeometric Distribution →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>What Is a Poisson Distribution?</h2>

    <p>
      A Poisson distribution models the number of events occurring within a fixed interval when events occur randomly and independently.
    </p>

    <div class="concept-box">

      <strong>Definition:</strong>

      <p>
        A Poisson random variable counts how many events occur in a specified interval of time, space, area, or volume.
      </p>

    </div>

    <h2>Examples of Poisson Processes</h2>

    <div class="example-box">

      <p>
        Number of customer arrivals in an hour
      </p>

      <p>
        Number of emails received during a day
      </p>

      <p>
        Number of accidents at an intersection per month
      </p>

      <p>
        Number of defects on a sheet of material
      </p>

      <p>
        Number of phone calls arriving each minute
      </p>

    </div>

    <p>
      Each example involves counting events over a fixed interval.
    </p>

    <h2>The Key Assumptions</h2>

    <p>
      A Poisson model is appropriate when:
    </p>

    <ul class="bullets">

      <li>Events occur randomly.</li>

      <li>Events occur independently.</li>

      <li>The average rate remains constant.</li>

      <li>Two events cannot occur at exactly the same instant.</li>

    </ul>

    <p>
      These assumptions define a Poisson process.
    </p>

    <h2>The Rate Parameter</h2>

    <p>
      The Poisson distribution is controlled by a single parameter:
    </p>

    0

    <p>
      called the rate parameter.
    </p>

    <p>
      λ represents the average number of events expected in the interval.
    </p>

    <div class="example-box">

      <p>
        λ = 5 means an average of five events per interval.
      </p>

    </div>

    <h2>Notation</h2>

    <p>
      A Poisson random variable is written as:
    </p>

    1

    <p>
      where λ is the average event rate.
    </p>

    <h2>Possible Values</h2>

    <p>
      A Poisson variable counts events.
    </p>

    <p>
      Therefore possible values are:
    </p>

    2

    <p>
      There is no fixed upper limit.
    </p>

    <h2>The Probability Mass Function</h2>

    <p>
      The probability of observing exactly k events is:
    </p>

    3

    <p>
      where:
    </p>

    <ul class="bullets">

      <li>e is Euler's number</li>

      <li>λ is the average rate</li>

      <li>k is the number of observed events</li>

    </ul>

    <h2>Understanding the Formula</h2>

    <p>
      The formula balances three factors:
    </p>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Term</th>
            <th>Role</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>e<sup>-λ</sup></td>
            <td>Adjusts total probability</td>
          </tr>

          <tr>
            <td>λ<sup>k</sup></td>
            <td>Accounts for event frequency</td>
          </tr>

          <tr>
            <td>k!</td>
            <td>Adjusts for arrangements</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>Example: Customer Arrivals</h2>

    <p>
      Suppose:
    </p>

    <div class="example-box">

      <p>
        Average arrivals = 3 customers per hour
      </p>
    </div>

    <p>
      Then:
    </p>

    4

    <p>
      The probability of exactly two arrivals is:
    </p>

    5

    <p>
      The formula converts the average rate into a probability for a specific count.
    </p>

    <h2>The Mean of a Poisson Distribution</h2>

    <p>
      One of the most elegant properties of the Poisson distribution is:
    </p>

    6

    <p>
      The mean equals the rate parameter.
    </p>

    <h2>The Variance</h2>

    <p>
      Another remarkable property is:
    </p>

    7

    <p>
      The variance also equals the rate parameter.
    </p>

    <div class="concept-box">

      <strong>Important:</strong>

      <p>
        For a Poisson distribution, the mean and variance are equal.
      </p>

    </div>

    <h2>Standard Deviation</h2>

    <p>
      Since variance equals λ:
    </p>

    8

    <p>
      Standard deviation grows as the event rate increases.
    </p>

    <h2>Shape of the Distribution</h2>

    <p>
      The shape depends on λ.
    </p>

    <div class="example-box">

      <p>
        Small λ → strongly right-skewed
      </p>

      <p>
        Moderate λ → less skewed
      </p>

      <p>
        Large λ → approximately bell-shaped
      </p>

    </div>

    <p>
      As λ increases,
      the distribution becomes more symmetric.
    </p>

    <h2>The Rare Event Model</h2>

    <p>
      The Poisson distribution is often called a rare-event model.
    </p>

    <p>
      It is particularly useful when:
    </p>

    <ul class="bullets">

      <li>Events are uncommon.</li>

      <li>Many opportunities for occurrence exist.</li>

      <li>The average rate remains stable.</li>

    </ul>

    <h2>Poisson as a Binomial Approximation</h2>

    <p>
      A Poisson distribution can approximate a binomial distribution when:
    </p>

    <ul class="bullets">

      <li>n is very large</li>

      <li>p is very small</li>

    </ul>

    <p>
      and:
    </p>

    9

    <p>
      remains moderate.
    </p>

    <p>
      This approximation is frequently used in practice.
    </p>

    <h2>Applications in Data Science</h2>

    <ul class="bullets">

      <li>Website traffic analysis</li>

      <li>Customer arrival forecasting</li>

      <li>Call center modeling</li>

      <li>Manufacturing defect analysis</li>

      <li>Healthcare event monitoring</li>

      <li>Network traffic modeling</li>

    </ul>

    <p>
      Poisson models appear throughout operations research and analytics.
    </p>

    <h2>Poisson Versus Binomial</h2>

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
            <td>Binomial</td>
            <td>Successes in a fixed number of trials</td>
          </tr>

          <tr>
            <td>Poisson</td>
            <td>Events in a fixed interval</td>
          </tr>

        </tbody>

      </table>

    </div>

    <p>
      Both count occurrences,
      but they arise from different assumptions and contexts.
    </p>

    <h2>The Limitation</h2>

    <p>
      Poisson models assume independent events occurring within a continuous domain.
    </p>

    <p>
      Sometimes sampling occurs without replacement from a finite population.
    </p>

    <div class="example-box">

      <p>
        Drawing cards from a deck
      </p>

      <p>
        Selecting defective products from a shipment
      </p>

      <p>
        Sampling individuals from a population
      </p>

    </div>

    <p>
      These situations require a different model.
    </p>

    <h2>Looking Ahead</h2>

    <p>
      The next lesson introduces the hypergeometric distribution,
      which models counts of successes when sampling without replacement from a finite population.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>The Poisson distribution models counts of events in a fixed interval</li>

        <li>It is governed by the rate parameter λ</li>

        <li>The probability formula uses λ, e, and factorials</li>

        <li>The mean equals λ</li>

        <li>The variance also equals λ</li>

        <li>Poisson distributions are often used for rare-event modeling</li>

        <li>They can approximate binomial distributions under certain conditions</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/probability/distributions/negative-binomial-distribution/">
         ← Previous: Negative Binomial Distribution
      </a>

      <a class="btn"
         href="/probability/distributions/hypergeometric-distribution/">
         Next: Hypergeometric Distribution →
      </a>

    </div>

  </div>

</section>