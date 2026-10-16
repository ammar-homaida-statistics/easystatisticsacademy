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

  try {
    localStorage.setItem(KEY, JSON.stringify({
    url: "/probability/distributions/poisson-distribution/",
    label: "Poisson Distribution",
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

      <li>The average event intensity is constant over the interval.</li>

      <li>Counts in disjoint intervals are independent (independent increments).</li>

      <li>The average rate remains constant.</li>

      <li>Two or more events in a sufficiently short interval have probability negligible relative to its duration.</li>

    </ul>

    <p>
      These are standard features of a homogeneous Poisson process. A Poisson count distribution alone does not establish that the underlying process is Poisson.
    </p>

    <h2>The Rate Parameter</h2>

    <p>
      The Poisson distribution is controlled by a single parameter:
    </p>

    \[\lambda\ge 0\]

    <p>
      called the rate parameter.
    </p>

    <p>
      Here λ ≥ 0 is the expected event count for the specified interval. If r denotes the event rate per time unit and t the observation duration, λ = rt. Always state the exposure.
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

    \[X\sim\operatorname{Poisson}(\lambda)\]

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

    \[X\in\{0,1,2,\ldots\}\]

    <p>
      There is no fixed upper limit.
    </p>

    <h2>The Probability Mass Function</h2>

    <p>
      The probability of observing exactly k events is:
    </p>

    \[P(X=k)=\frac{e^{-\lambda}\lambda^k}{k!},\qquad k=0,1,2,\ldots\]

    <p>
      where:
    </p>

    <ul class="bullets">

      <li>e is Euler's number</li>

      <li>λ is the average rate</li>

      <li>k is a nonnegative integer counting events</li>

    </ul>

    <p>At λ = 0, the count is identically zero: P(X = 0) = 1 and P(X &gt; 0) = 0. The PMF is interpreted by continuity at this endpoint.</p>

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

    \[\lambda=3\ \text{arrivals per hour}\]

    <p>
      The probability of exactly two arrivals is:
    </p>

    \[P(X=2)=\frac{e^{-3}3^2}{2!}\approx 0.224042\]

    <p>
      The formula converts the average rate into a probability for a specific count.
    </p>

    <h2>The Mean of a Poisson Distribution</h2>

    <p>
      One of the most elegant properties of the Poisson distribution is:
    </p>

    \[\operatorname{E}(X)=\lambda\]

    <p>
      The mean equals the rate parameter.
    </p>

    <h2>The Variance</h2>

    <p>
      Another remarkable property is:
    </p>

    \[\operatorname{Var}(X)=\lambda\]

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

    \[\operatorname{SD}(X)=\sqrt{\lambda}\]

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
      with the expected count:
    </p>

    \[\lambda=np\]

    <p>
      remains moderate. The classical limit has n → ∞, p → 0, and np → λ; accuracy at finite n depends on n and p.
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
      Homogeneous Poisson processes have independent increments and a constant intensity. Some real event counts violate these assumptions.
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


    <!-- POISSON–EXPONENTIAL EXPLORER -->
    <section class="concept-box" id="esa-poisson-exponential-explorer"
             aria-labelledby="esa-poisson-exponential-heading">
      <h2 id="esa-poisson-exponential-heading">Interactive Poisson–Exponential Explorer</h2>
      <p>In a homogeneous Poisson process with rate r events per minute,
         N(t) has expected count rt, while T is the exponential waiting time
         to the next event. Compare their probabilities for the same t.</p>
      <form id="esa-event-explorer-form" novalidate>
        <div class="esa-event-input-grid">
          <div><label for="esa-event-rate">Rate (events per minute)</label>
            <input id="esa-event-rate" type="number" inputmode="decimal"
                   min="0.01" max="20" step="any" value="2" required></div>
          <div><label for="esa-event-time">Observation time (minutes)</label>
            <input id="esa-event-time" type="number" inputmode="decimal"
                   min="0" max="60" step="any" value="1" required></div>
        </div>
        <p id="esa-event-error" role="alert" hidden></p>
        <div id="esa-event-results" role="status" aria-live="polite" aria-atomic="true">
          <div class="esa-event-result-grid">
            <p>P(N(t) = 0): <strong><output id="esa-event-none">0.135335</output></strong></p>
            <p>P(T &gt; t): <strong><output id="esa-event-survival">0.135335</output></strong></p>
            <p>P(N(t) ≥ 1): <strong><output id="esa-event-at-least-one">0.864665</output></strong></p>
            <p>Expected count (rt): <strong><output id="esa-event-expected">2.000000</output></strong></p>
            <p>Mean waiting time (1/r), minutes: <strong><output id="esa-event-meanwait">0.500000</output></strong></p>
          </div>
          <p id="esa-event-explanation">The two no-event probabilities equal e<sup>−rt</sup>.</p>
        </div>
        <button type="button" id="esa-event-reset" class="btn btn-outline">Reset example</button>
      </form>
      <p><strong>Assumptions:</strong> These identities connect the two distributions
         for a <em>homogeneous Poisson process</em>. Clustering, dependent increments,
         or changing rates may invalidate the exponential waiting-time model.</p>
    </section>
    <style>
      #esa-poisson-exponential-explorer{min-width:0;max-width:100%;overflow-wrap:anywhere}
      #esa-poisson-exponential-explorer .esa-event-input-grid,
      #esa-poisson-exponential-explorer .esa-event-result-grid{
        display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px 16px;margin:12px 0}
      #esa-poisson-exponential-explorer .esa-event-input-grid>div,
      #esa-poisson-exponential-explorer .esa-event-result-grid>p{min-width:0;margin:5px 0}
      #esa-poisson-exponential-explorer label{display:block;font-weight:650;margin:0 0 6px}
      #esa-poisson-exponential-explorer input[type="number"]{
        display:block;width:100%;max-width:100%;min-width:0;box-sizing:border-box;
        padding:10px;font:inherit;background:var(--surface);color:var(--text);
        border:1px solid var(--border-strong);border-radius:8px}
      #esa-poisson-exponential-explorer input:focus-visible,
      #esa-poisson-exponential-explorer button:focus-visible{
        outline:2px solid var(--accent);outline-offset:2px}
      #esa-poisson-exponential-explorer #esa-event-error{color:#b42318;font-weight:650}
      #esa-poisson-exponential-explorer [hidden]{display:none!important}
      @media(max-width:600px){
        #esa-poisson-exponential-explorer .esa-event-input-grid,
        #esa-poisson-exponential-explorer .esa-event-result-grid{
          grid-template-columns:minmax(0,1fr)}
      }
    </style>
    <script>
    (function () {
      "use strict";
      const form = document.getElementById("esa-event-explorer-form");
      const rate = document.getElementById("esa-event-rate");
      const time = document.getElementById("esa-event-time");
      const error = document.getElementById("esa-event-error");
      const outputs = ["esa-event-none","esa-event-survival","esa-event-at-least-one",
                       "esa-event-expected","esa-event-meanwait"]
                       .map(id => document.getElementById(id));
      const explanation = document.getElementById("esa-event-explanation");
      function render() {
        const r = Number(rate.value), t = Number(time.value);
        const invalidRate = rate.value.trim() === "" || !Number.isFinite(r) || r <= 0 || r > 20;
        const invalidTime = time.value.trim() === "" || !Number.isFinite(t) || t < 0 || t > 60;
        if (invalidRate || invalidTime) {
          error.textContent = invalidRate
            ? "Rate must be greater than 0 and at most 20 events per minute."
            : "Time must be between 0 and 60 minutes.";
          error.hidden = false;
          outputs.forEach(out => { out.textContent = "—"; });
          explanation.textContent = "Enter valid inputs to compare the distributions.";
          return;
        }
        error.hidden = true;
        const expected = r*t, noEvents = Math.exp(-expected);
        // expm1 prevents catastrophic cancellation near zero.
        const atLeastOne = -Math.expm1(-expected);
        [noEvents,noEvents,atLeastOne,expected,1/r].forEach((value,i) => {
          outputs[i].textContent = value.toFixed(6);
        });
        explanation.textContent = "With rate " + r + " events/minute over " + t +
          " minutes, P(N(t) = 0) = P(T > t) = exp(−rt).";
      }
      form.addEventListener("submit", event => event.preventDefault());
      rate.addEventListener("input",render);
      time.addEventListener("input",render);
      document.getElementById("esa-event-reset").addEventListener("click",() => {
        rate.value = "2"; time.value = "1"; render();
      });
      render();
    })();
    </script>

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