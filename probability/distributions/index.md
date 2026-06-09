---
layout: default
title: Block 5 — Common Distributions
description: Learn the most important probability distributions, how to recognize them, interpret their parameters, and use them to model real-world uncertainty.
permalink: /probability/distributions/
sidebar: false
---

<!-- SAVE BLOCK PROGRESS -->
<script>
(function () {

  const KEY = "esa_continue_probability_last_block_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/probability/distributions/",
    label: "Block 5 — Common Distributions",
    ts: Date.now()
  }));

})();
</script>

<!-- HERO -->

<section class="hero hero-section">

  <div class="hero-card hero-split">

    <!-- LEFT -->

    <div class="hero-copy">

      <div class="badge-row">
        <span class="badge">Probability</span>
        <span class="badge">Block 5</span>
        <span class="badge">Distributions</span>
        <span class="badge">Modeling</span>
      </div>

      <h1>Block 5 — Common Distributions</h1>

      <p class="lead">
        Probability distributions are reusable models of uncertainty.
      </p>

      <p class="lead">
        This block introduces the most important discrete and continuous
        probability distributions used throughout statistics,
        machine learning, engineering, economics, and science.
      </p>

      <p class="muted-mini">
        12 lessons • Applied probability modeling • Builds on Expectation & Variability • Prepares for LLN & CLT
      </p>

      <div class="hero-actions">

        <a class="btn" href="#lessons">
          Open Lessons
        </a>

        <a class="btn btn-outline" href="/probability/">
          Back to Probability
        </a>

      </div>

      <div class="hero-highlight">

        <div class="hero-highlight-icon">
          📊
        </div>

        <div>

          <strong>Why this block matters</strong>

          <p>
            Most real-world probability problems are solved using probability
            distributions. Learning to recognize the correct distribution is one
            of the most valuable skills in probability and statistics.
          </p>

        </div>

      </div>

    </div>

    <!-- RIGHT -->

    <div class="hero-panel">

      <div class="panel-card">

        <h2 class="panel-title">Block overview</h2>

        <div class="mini">
          <div class="mini-title">Lessons</div>
          <div class="mini-body">12 structured lessons</div>
        </div>

        <div class="mini">
          <div class="mini-title">Level</div>
          <div class="mini-body">Applied probability</div>
        </div>

        <div class="mini">
          <div class="mini-title">Main skill</div>
          <div class="mini-body">
            Match distributions to real situations
          </div>
        </div>

        <div class="mini">
          <div class="mini-title">Next block</div>
          <div class="mini-body">
            Law of Large Numbers & CLT
          </div>
        </div>

      </div>

    </div>

  </div>

</section>

<!-- CONTINUE READING -->

<section
  class="section"
  id="continue-reading-probability-distributions"
  style="display:none;"
>

  <div class="callout">

    <div class="callout-copy">

      <h2>Continue reading</h2>

      <p
        id="continue-reading-probability-distributions-label"
        class="muted-mini"
      ></p>

      <a
        class="btn"
        id="continue-reading-probability-distributions-btn"
        href="#"
      >
        Continue
      </a>

    </div>

  </div>

</section>

<!-- LESSONS -->

<section class="section" id="lessons">

  <div class="section-head">

    <h2>Lessons</h2>

    <p>
      These distributions appear repeatedly throughout probability,
      statistical inference, machine learning, operations research,
      and applied data analysis.
    </p>

  </div>

  <!-- DISCRETE -->

  <h3>Discrete Distributions</h3>

  <div class="grid grid-2">

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/probability/distributions/bernoulli-distribution/">
          Bernoulli Distribution
        </a>
      </h3>

      <p>
        Model a single success-or-failure trial,
        the foundation of many probability models.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Bernoulli</span>
        <span class="pill">Binary</span>
        <span class="pill">Success</span>
      </div>

      <a class="btn btn-outline"
         href="/probability/distributions/bernoulli-distribution/">
         Open lesson
      </a>

    </div>

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/probability/distributions/binomial-distribution/">
          Binomial Distribution
        </a>
      </h3>

      <p>
        Count the number of successes in a fixed number
        of independent Bernoulli trials.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Binomial</span>
        <span class="pill">Counts</span>
        <span class="pill">Trials</span>
      </div>

      <a class="btn btn-outline"
         href="/probability/distributions/binomial-distribution/">
         Open lesson
      </a>

    </div>

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/probability/distributions/geometric-distribution/">
          Geometric Distribution
        </a>
      </h3>

      <p>
        Model the waiting time until the first success occurs.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Geometric</span>
        <span class="pill">Waiting Time</span>
        <span class="pill">Memoryless</span>
      </div>

      <a class="btn btn-outline"
         href="/probability/distributions/geometric-distribution/">
         Open lesson
      </a>

    </div>

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/probability/distributions/negative-binomial-distribution/">
          Negative Binomial Distribution
        </a>
      </h3>

      <p>
        Generalize geometric waiting times to the occurrence
        of multiple successes.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Negative Binomial</span>
        <span class="pill">Waiting Time</span>
        <span class="pill">Counts</span>
      </div>

      <a class="btn btn-outline"
         href="/probability/distributions/negative-binomial-distribution/">
         Open lesson
      </a>

    </div>

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/probability/distributions/poisson-distribution/">
          Poisson Distribution
        </a>
      </h3>

      <p>
        Model counts of events occurring randomly through time,
        distance, area, or volume.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Poisson</span>
        <span class="pill">Counts</span>
        <span class="pill">Rate</span>
      </div>

      <a class="btn btn-outline"
         href="/probability/distributions/poisson-distribution/">
         Open lesson
      </a>

    </div>

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/probability/distributions/hypergeometric-distribution/">
          Hypergeometric Distribution
        </a>
      </h3>

      <p>
        Model sampling without replacement and compare it
        with the binomial model.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Hypergeometric</span>
        <span class="pill">Sampling</span>
        <span class="pill">Without Replacement</span>
      </div>

      <a class="btn btn-outline"
         href="/probability/distributions/hypergeometric-distribution/">
         Open lesson
      </a>

    </div>

  </div>

  <!-- CONTINUOUS -->

  <h3 style="margin-top:2rem;">
    Continuous Distributions
  </h3>

  <div class="grid grid-2">

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/probability/distributions/uniform-distribution/">
          Uniform Distribution
        </a>
      </h3>

      <p>
        Model situations where all values within an interval
        are equally plausible.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Uniform</span>
        <span class="pill">Continuous</span>
        <span class="pill">Equal Density</span>
      </div>

      <a class="btn btn-outline"
         href="/probability/distributions/uniform-distribution/">
         Open lesson
      </a>

    </div>

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/probability/distributions/exponential-distribution/">
          Exponential Distribution
        </a>
      </h3>

      <p>
        Model waiting times between events and explore
        the memoryless property.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Exponential</span>
        <span class="pill">Waiting Time</span>
        <span class="pill">Memoryless</span>
      </div>

      <a class="btn btn-outline"
         href="/probability/distributions/exponential-distribution/">
         Open lesson
      </a>

    </div>

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/probability/distributions/gamma-distribution/">
          Gamma Distribution
        </a>
      </h3>

      <p>
        Extend exponential models into a flexible family
        of waiting-time distributions.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Gamma</span>
        <span class="pill">Waiting Time</span>
        <span class="pill">Flexible</span>
      </div>

      <a class="btn btn-outline"
         href="/probability/distributions/gamma-distribution/">
         Open lesson
      </a>

    </div>

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/probability/distributions/beta-distribution/">
          Beta Distribution
        </a>
      </h3>

      <p>
        Model probabilities themselves and build foundations
        for Bayesian statistics.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Beta</span>
        <span class="pill">Probabilities</span>
        <span class="pill">Bayesian</span>
      </div>

      <a class="btn btn-outline"
         href="/probability/distributions/beta-distribution/">
         Open lesson
      </a>

    </div>

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/probability/distributions/normal-distribution/">
          Normal Distribution
        </a>
      </h3>

      <p>
        Study the most important distribution in statistics,
        including standardization and approximation.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Normal</span>
        <span class="pill">Gaussian</span>
        <span class="pill">Standardization</span>
      </div>

      <a class="btn btn-outline"
         href="/probability/distributions/normal-distribution/">
         Open lesson
      </a>

    </div>

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/probability/distributions/lognormal-distribution/">
          Lognormal Distribution
        </a>
      </h3>

      <p>
        Model positively skewed quantities generated through
        multiplicative processes.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Lognormal</span>
        <span class="pill">Skewed</span>
        <span class="pill">Growth</span>
      </div>

      <a class="btn btn-outline"
         href="/probability/distributions/lognormal-distribution/">
         Open lesson
      </a>

    </div>

  </div>

</section>

<!-- BLOCK MAP -->

<section class="section section-slim">

  <div class="callout">

    <div class="callout-copy">

      <h2>How this block fits into probability</h2>

      <p>
        Previous blocks developed probability tools.
        This block introduces the probability models that repeatedly appear
        throughout applied statistics and scientific analysis.
      </p>

      <div class="table-wrap">

        <table>

          <thead>

            <tr>
              <th>Distribution Family</th>
              <th>Typical Use</th>
            </tr>

          </thead>

          <tbody>

            <tr>
              <td>Bernoulli / Binomial</td>
              <td>Successes and failures</td>
            </tr>

            <tr>
              <td>Geometric / Negative Binomial</td>
              <td>Waiting times for successes</td>
            </tr>

            <tr>
              <td>Poisson</td>
              <td>Event counts</td>
            </tr>

            <tr>
              <td>Uniform</td>
              <td>Equal plausibility</td>
            </tr>

            <tr>
              <td>Exponential / Gamma</td>
              <td>Continuous waiting times</td>
            </tr>

            <tr>
              <td>Beta</td>
              <td>Modeling probabilities</td>
            </tr>

            <tr>
              <td>Normal</td>
              <td>Natural variation and inference</td>
            </tr>

            <tr>
              <td>Lognormal</td>
              <td>Multiplicative growth processes</td>
            </tr>

          </tbody>

        </table>

      </div>

    </div>

  </div>

</section>

<!-- GOALS -->

<section class="section section-slim">

  <div class="callout">

    <div class="callout-copy">

      <h2>Goal of this block</h2>

      <ul class="bullets">

        <li>Recognize common probability distributions from context</li>

        <li>Interpret parameters correctly</li>

        <li>Understand discrete and continuous distribution families</li>

        <li>Compute probabilities using PMFs, PDFs, and CDFs</li>

        <li>Understand relationships between distributions</li>

        <li>Recognize approximation patterns between models</li>

        <li>Prepare for the Law of Large Numbers and Central Limit Theorem</li>

      </ul>

    </div>

    <div class="callout-side">

      <div class="mini">

        <div class="mini-title">Next block</div>

        <div class="mini-body">
          Continue to <strong>Law of Large Numbers & CLT</strong>
        </div>

      </div>

      <div class="mini">

        <div class="mini-title">Core idea</div>

        <div class="mini-body">
          Distributions are reusable mathematical models of uncertainty.
        </div>

      </div>

      <div class="mini">

        <div class="mini-title">Big transition</div>

        <div class="mini-body">
          These models become the building blocks of inference.
        </div>

      </div>

    </div>

  </div>

</section>

<!-- NAVIGATION -->

<section class="section section-slim">

  <div class="lesson-nav">

    <a class="btn btn-outline" href="/probability/expectation-variance/">
      ← Previous Block: Expectation & Variability
    </a>

    <a class="btn" href="/probability/lln-clt/">
      Next Block: Law of Large Numbers & CLT →
    </a>

  </div>

</section>

<!-- CONTINUE READING SCRIPT -->

<script>
(function () {

  try {

    const KEY =
      "esa_continue_probability_distributions_lesson_v0";

    const raw = localStorage.getItem(KEY);

    if (!raw) return;

    const data = JSON.parse(raw);

    if (!data || !data.url || !data.label) return;

    const wrap =
      document.getElementById(
        "continue-reading-probability-distributions"
      );

    const label =
      document.getElementById(
        "continue-reading-probability-distributions-label"
      );

    const btn =
      document.getElementById(
        "continue-reading-probability-distributions-btn"
      );

    if (!wrap || !label || !btn) return;

    label.innerHTML =
      "You last visited: <strong>" +
      data.label +
      "</strong>";

    btn.href = data.url;

    wrap.style.display = "block";

  } catch (e) {}

})();
</script>