---
layout: default
title: Exponential Distribution
description: Learn how the exponential distribution models waiting times between random events and why it is the continuous counterpart of the geometric distribution.
permalink: /probability/distributions/exponential-distribution/
sidebar: false
---

<!-- SAVE LESSON PROGRESS -->
<script>
(function () {

  const KEY =
    "esa_continue_probability_distributions_lesson_v0";

  try {
    localStorage.setItem(KEY, JSON.stringify({
    url: "/probability/distributions/exponential-distribution/",
    label: "Exponential Distribution",
    ts: Date.now()
    }));
  } catch (_) {
    // Storage may be disabled; the page still works without saved progress.
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
      <span class="badge">Continuous</span>
    </div>

    <h1>Exponential Distribution</h1>

    <p class="lead">
      Many probability problems focus on waiting times.
    </p>

    <p class="lead">
      The exponential distribution is one of the most important continuous distributions because it models the time between random events.
    </p>

    <div class="hero-actions">

      <a class="btn"
         href="/probability/distributions/uniform-distribution/">
         ← Previous Lesson
      </a>

      <a class="btn btn-outline"
         href="/probability/distributions/gamma-distribution/">
         Next: Gamma Distribution →
      </a>

    </div>

  </div>

</section>

<!-- LESSON -->

<section>

  <div class="content-narrow">

    <h2>What Is an Exponential Distribution?</h2>

    <p>
      The exponential distribution describes the waiting time until the next occurrence of a random event.
    </p>

    <div class="concept-box">

      <strong>Definition:</strong>

      <p>
        For a homogeneous Poisson process, an exponential variable measures the waiting time between consecutive events. This does not generally hold for other event-arrival mechanisms.
      </p>

    </div>

    <h2>The Main Question</h2>

    <p>
      Instead of counting events,
      we ask:
    </p>

    <div class="example-box">

      <p>
        How long until the next customer arrives?
      </p>

      <p>
        How long until the next phone call?
      </p>

      <p>
        How long until a machine fails?
      </p>

      <p>
        How long until the next website visit?
      </p>

    </div>

    <p>
      These are waiting-time questions.
    </p>

    <h2>Connection to the Poisson Distribution</h2>

    <p>
      The Poisson distribution counts events.
    </p>

    <p>
      The exponential distribution measures the time between those events.
    </p>

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
            <td>Poisson</td>
            <td>Number of events</td>
          </tr>

          <tr>
            <td>Exponential</td>
            <td>Waiting time between events</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>The Rate Parameter</h2>

    <p>
      The exponential distribution uses the same rate parameter:
    </p>

    \[\lambda>0\]

    <p>
      that appears in the Poisson distribution.
    </p>

    <p>
      λ represents the average number of events per unit time.
    </p>

    <div class="example-box">

      <p>
        λ = 4 means four events per hour on average.
      </p>

    </div>

    <h2>Notation</h2>

    <p>
      An exponential random variable is written as:
    </p>

    <div class="example-box">

      <p>
        X ~ Exponential(λ), with λ &gt; 0
      </p>

    </div>

    <p>
      where λ is the event rate.
    </p>

    <h2>The Probability Density Function</h2>

    <p>
      The exponential density function is:
    </p>

    \[f_X(x)=\lambda e^{-\lambda x},\qquad x\ge 0\]

    <p>
      for:
    </p>

    \[x\ge 0\]

    <p>
      and zero otherwise.
    </p>

    <h2>The Shape of the Density</h2>

    <p>
      The density starts high and decreases continuously.
    </p>

    <div class="example-box">

      <p>
        Short waiting times are common.
      </p>

      <p>
        Long waiting times are increasingly rare.
      </p>

    </div>

    <p>
      This creates a strongly right-skewed distribution.
    </p>

    <h2>The Cumulative Distribution Function</h2>

    <p>
      The probability that an event occurs within time x is:
    </p>

    \[F_X(x)=P(X\le x)=1-e^{-\lambda x},\qquad x\ge 0\]

    <p>
      This is the cumulative distribution function (CDF).
    </p>

    <h2>Probabilities of Waiting Longer</h2>

    <p>
      The probability of waiting more than x units of time is:
    </p>

    \[P(X>x)=e^{-\lambda x},\qquad x\ge 0\]

    <p>
      This is called the survival function.
    </p>

    <h2>Example: Customer Arrivals</h2>

    <p>
      Suppose customers arrive at an average rate of:
    </p>

    <div class="example-box">

      <p>
        λ = 2 per minute
      </p>

    </div>

    <p>
      What is the probability the next customer arrives within one minute?
    </p>

    <p>
      Using the CDF:
    </p>

    \[P(X\le 1)=1-e^{-2}\approx 0.864665\]

    <p>
      This evaluates to approximately 0.865.
    </p>

    <h2>The Mean</h2>

    <p>
      The expected value is:
    </p>

    \[\operatorname{E}(X)=\frac{1}{\lambda}\]

    <div class="concept-box">

      <strong>Interpretation:</strong>

      <p>
        The average waiting time equals the reciprocal of the event rate.
      </p>

    </div>

    <h2>Example of the Mean</h2>

    <p>
      If:
    </p>

    <div class="example-box">

      <p>
        λ = 4 per hour
      </p>

    </div>

    <p>
      Then:
    </p>

    \[\operatorname{E}(X)=\frac14\ \text{hour}=15\ \text{minutes}\]

    <p>
      hours,
      or approximately 15 minutes.
    </p>

    <h2>The Variance</h2>

    <p>
      The variance is:
    </p>

    \[\operatorname{Var}(X)=\frac{1}{\lambda^2}\]

    <p>
      The standard deviation is:
    </p>

    \[\operatorname{SD}(X)=\frac{1}{\lambda}\]

    <p>
      Interestingly,
      the standard deviation equals the mean.
    </p>

    <h2>The Memoryless Property</h2>

    <p>
      The exponential distribution has a remarkable property:
    </p>

    <div class="concept-box">

      <strong>Memoryless Property:</strong>

      <p>
        Future waiting time does not depend on how long you have already waited.
      </p>

    </div>

    <h2>The Memoryless Formula</h2>

    <p>
      Mathematically:
    </p>

    \[P(X>s+t\mid X>s)=P(X>t)=e^{-\lambda t},\qquad s,t\ge 0\]

    <p>
      The remaining waiting time has the same distribution regardless of past waiting.
    </p>

    <h2>Understanding Memorylessness</h2>

    <p>
      Under a constant event rate, suppose no customer has arrived for 20 minutes.
    </p>

    <p>
      The expected future waiting time remains unchanged.
    </p>

    <p>
      The process does not become "due" for an event.
    </p>

    <h2>Connection to the Geometric Distribution</h2>

    <p>
      The geometric distribution is the discrete waiting-time model.
    </p>

    <p>
      The exponential distribution is its continuous counterpart.
    </p>

    <div class="table-wrap">

      <table>

        <thead>

          <tr>
            <th>Distribution</th>
            <th>Waiting-Time Type</th>
          </tr>

        </thead>

        <tbody>

          <tr>
            <td>Geometric</td>
            <td>Discrete trials</td>
          </tr>

          <tr>
            <td>Exponential</td>
            <td>Continuous time</td>
          </tr>

        </tbody>

      </table>

    </div>

    <h2>Applications of the Exponential Distribution</h2>

    <ul class="bullets">

      <li>Customer arrival times</li>

      <li>Machine lifetimes</li>

      <li>Queueing systems</li>

      <li>Network packet arrivals</li>

      <li>Service waiting times</li>

      <li>Reliability engineering</li>

    </ul>

    <p>
      It is one of the most widely used continuous distributions.
    </p>

    <h2>Why It Matters</h2>

    <p>
      The exponential distribution provides a simple model for random waiting times.
    </p>

    <p>
      Its connection to Poisson processes makes it fundamental in probability theory,
      operations research,
      reliability analysis,
      and data science.
    </p>

    <h2>The Limitation</h2>

    <p>
      The exponential distribution models the waiting time to the next event under a constant hazard rate.
    </p>

    <p>
      Sometimes we need to model waiting for multiple events.
    </p>

    <div class="example-box">

      <p>
        Time until the third customer arrives
      </p>

      <p>
        Time until the fifth failure occurs
      </p>

      <p>
        Time until ten calls arrive
      </p>

    </div>

    <p>
      These situations lead to the gamma distribution.
    </p>

    <h2>Looking Ahead</h2>

    <p>
      The gamma distribution generalizes the exponential distribution by modeling waiting times until multiple events occur.
    </p>

    <p>
      It is one of the most flexible and useful continuous distributions in probability and statistics.
    </p>

    <div class="concept-box"><p><strong>Explore the connection:</strong> Use the <a href="/probability/distributions/poisson-distribution/#esa-poisson-exponential-explorer">Poisson–Exponential interactive explorer</a> to compare the probability of zero events with the probability of waiting longer than the same observation time.</p></div>

    <!-- TAKEAWAYS -->

    <div class="summary-box">

      <h2>Lesson Takeaways</h2>

      <ul class="bullets">

        <li>The exponential distribution models waiting times between random events</li>

        <li>It is governed by the rate parameter λ</li>

        <li>The density function is λe<sup>−λx</sup></li>

        <li>The mean equals 1/λ</li>

        <li>The variance equals 1/λ²</li>

        <li>It possesses the memoryless property</li>

        <li>It is the continuous counterpart of the geometric distribution</li>

        <li>It is closely connected to Poisson processes</li>

      </ul>

    </div>

    <!-- NAVIGATION -->

    <div class="lesson-nav">

      <a class="btn btn-outline"
         href="/probability/distributions/uniform-distribution/">
         ← Previous: Uniform Distribution
      </a>

      <a class="btn"
         href="/probability/distributions/gamma-distribution/">
         Next: Gamma Distribution →
      </a>

    </div>

  </div>

</section>