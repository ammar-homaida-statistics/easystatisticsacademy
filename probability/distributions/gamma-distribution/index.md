---
layout: default
title: Gamma Distribution
description: Learn how the gamma distribution generalizes the exponential distribution and models waiting times until multiple events occur.
permalink: /probability/distributions/gamma-distribution/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_probability_distributions_lesson_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/probability/distributions/gamma-distribution/",
    label: "Gamma Distribution",
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
      <span class="badge">Continuous</span>
    </div>

    <h1>Gamma Distribution</h1>

    <p class="lead">
      The exponential distribution models waiting for a single event.
    </p>

    <p class="lead">
      The gamma distribution extends this idea and models waiting times until multiple events occur.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/probability/distributions/exponential-distribution/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/probability/distributions/beta-distribution/">
         Next: Beta Distribution →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>What Is a Gamma Distribution?</h2>

    <p>
      The gamma distribution models the waiting time until a specified number of events occur in a Poisson process.
    </p>

    <div class="concept-box">

      <strong>Definition:</strong>

      <p>
        A gamma random variable represents the total waiting time required for multiple random events to occur.
      </p>

    </div>

    <h2>The Main Idea</h2>

    <p>
      Suppose events occur randomly over time.
    </p>

    <div class="example-box">

      <p>
        Time until the first customer arrives
      </p>

      <p>
        Time until the fifth customer arrives
      </p>

      <p>
        Time until the tenth phone call
      </p>

      <p>
        Time until the third machine failure
      </p>

    </div>

    <p>
      The exponential distribution handles the first event.
    </p>

    <p>
      The gamma distribution handles multiple events.
    </p>

    <h2>Connection to the Exponential Distribution</h2>

    <p>
      If waiting times between events are exponential,
      then the sum of several such waiting times follows a gamma distribution.
    </p>

    <div class="concept-box">

      <strong>Key idea:</strong>

      <p>
        A gamma distribution is the distribution of the sum of independent exponential waiting times.
      </p>

    </div>

    <h2>The Parameters</h2>

    <p>
      A gamma distribution is commonly defined using:
    </p>

    <ul class="bullets">

      <li>α (shape parameter)</li>

      <li>λ (rate parameter)</li>

    </ul>

    <p>
      The shape parameter determines how many events are being accumulated.
    </p>

    <p>
      The rate parameter controls how frequently events occur.
    </p>

    <h2>Notation</h2>

    <p>
      A gamma random variable is often written as:
    </p>

    <div class="example-box">

      <p>
        X ~ Gamma(α, λ)
      </p>

    </div>

    <h2>The Probability Density Function</h2>

    <p>
      The gamma density function is:
    </p>

    0

    <p>
      for:
    </p>

    1

    <p>
      where Γ(α) is the gamma function.
    </p>

    <h2>The Gamma Function</h2>

    <p>
      The gamma function extends the factorial function to non-integer values.
    </p>

    <p>
      For positive integers:
    </p>

    2

    <p>
      This connection explains the name of the distribution.
    </p>

    <h2>A Special Case</h2>

    <p>
      When:
    </p>

    3

    <p>
      the gamma distribution becomes:
    </p>

    4

    <div class="concept-box">

      <strong>Important:</strong>

      <p>
        The exponential distribution is a special case of the gamma distribution.
      </p>

    </div>

    <h2>Interpreting the Shape Parameter</h2>

    <p>
      The shape parameter α determines how many events are being waited for.
    </p>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Shape α</th>
            <th>Interpretation</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>1</td>
            <td>Wait for first event</td>
          </tr>

          <tr>
            <td>2</td>
            <td>Wait for second event</td>
          </tr>

          <tr>
            <td>5</td>
            <td>Wait for fifth event</td>
          </tr>

          <tr>
            <td>10</td>
            <td>Wait for tenth event</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>The Mean</h2>

    <p>
      The expected value is:
    </p>

    5

    <div class="concept-box">

      <strong>Interpretation:</strong>

      <p>
        Expected waiting time increases with the number of required events and decreases as the event rate increases.
      </p>

    </div>

    <h2>Example of the Mean</h2>

    <p>
      Suppose:
    </p>

    <div class="example-box">

      <p>
        α = 4
      </p>

      <p>
        λ = 2
      </p>

    </div>

    <p>
      Then:
    </p>

    6

    <p>
      The average waiting time equals 2 time units.
    </p>

    <h2>The Variance</h2>

    <p>
      The variance is:
    </p>

    7

    <p>
      Greater shape values increase variability,
      while larger rates decrease it.
    </p>

    <h2>The Shape of the Distribution</h2>

    <p>
      The gamma distribution can take many forms.
    </p>

    <div class="example-box">

      <p>
        Small α → highly right-skewed
      </p>

      <p>
        Moderate α → smoother peak
      </p>

      <p>
        Large α → increasingly bell-shaped
      </p>

    </div>

    <p>
      This flexibility makes the gamma distribution extremely useful.
    </p>

    <h2>The Erlang Distribution</h2>

    <p>
      When the shape parameter is a positive integer,
      the gamma distribution is often called an Erlang distribution.
    </p>

    <p>
      Erlang models are widely used in queueing theory and telecommunications.
    </p>

    <h2>Applications of the Gamma Distribution</h2>

    <ul class="bullets">

      <li>Waiting for multiple customer arrivals</li>

      <li>Reliability engineering</li>

      <li>Queueing systems</li>

      <li>Insurance claim modeling</li>

      <li>Rainfall and environmental processes</li>

      <li>Service-time analysis</li>

    </ul>

    <p>
      Gamma models appear throughout operations research and applied statistics.
    </p>

    <h2>Relationship to Other Distributions</h2>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Distribution</th>
            <th>Relationship</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>Exponential</td>
            <td>Gamma with α = 1</td>
          </tr>

          <tr>
            <td>Erlang</td>
            <td>Gamma with integer α</td>
          </tr>

          <tr>
            <td>Chi-Square</td>
            <td>Special gamma distribution</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>Why the Gamma Distribution Matters</h2>

    <p>
      The gamma distribution is one of the most flexible continuous distributions.
    </p>

    <p>
      It generalizes the exponential distribution and provides realistic models for many waiting-time processes.
    </p>

    <p>
      Its mathematical properties also make it important in Bayesian statistics and statistical inference.
    </p>

    <h2>The Limitation</h2>

    <p>
      Gamma distributions model positive continuous quantities such as waiting times.
    </p>

    <p>
      Sometimes we are interested in proportions and probabilities instead.
    </p>

    <div class="example-box">

      <p>
        Conversion rate
      </p>

      <p>
        Probability of success
      </p>

      <p>
        Market share
      </p>

      <p>
        Fraction of defective items
      </p>

    </div>

    <p>
      Values like these are naturally restricted between 0 and 1.
    </p>

    <p>
      Such situations are often modeled using the beta distribution.
    </p>

    <h2>Looking Ahead</h2>

    <p>
      The beta distribution is one of the most important distributions for modeling probabilities and proportions.
    </p>

    <p>
      It plays a central role in Bayesian statistics and uncertainty quantification.
    </p>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>The gamma distribution models waiting times until multiple events occur</li>

        <li>It generalizes the exponential distribution</li>

        <li>The exponential distribution is the special case α = 1</li>

        <li>The mean equals α/λ</li>

        <li>The variance equals α/λ²</li>

        <li>The gamma function extends factorials to non-integer values</li>

        <li>Gamma distributions are widely used in reliability, queueing, and Bayesian statistics</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/probability/distributions/exponential-distribution/">
         ← Previous: Exponential Distribution
      </a>

      <a class="btn"
         href="/probability/distributions/beta-distribution/">
         Next: Beta Distribution →
      </a>

    </div>

  </div>

</section>