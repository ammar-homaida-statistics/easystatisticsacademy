---
layout: default
title: Block 3 — Random Variables
description: Learn how random variables transform probability into quantitative models through PMFs, PDFs, CDFs, expectation, and variance.
permalink: /probability/random-variables/
sidebar: false
---

<!-- SAVE BLOCK PROGRESS -->
<script>
(function () {

  const KEY = "esa_continue_probability_last_block_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/probability/random-variables/",
    label: "Block 3 — Random Variables",
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
        <span class="badge">Block 3</span>
        <span class="badge">Random Variables</span>
        <span class="badge">Distributions</span>
      </div>

      <h1>Block 3 — Random Variables</h1>

      <p class="lead">
        Random variables transform uncertainty into numbers.
      </p>

      <p class="lead">
        This block moves probability from events and sets into quantitative models.
        It introduces probability distributions, expectation, variance,
        and the mathematical language used throughout modern statistics.
      </p>

      <p class="muted-mini">
        6 lessons • Core probability theory • Builds on Conditional Probability • Prepares for Expectation & Variability
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
          📈
        </div>

        <div>

          <strong>Why this block matters</strong>

          <p>
            Statistical inference, machine learning, forecasting,
            and data science all rely on probability distributions.
            Random variables provide the framework that makes these ideas possible.
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
          <div class="mini-body">6 structured lessons</div>
        </div>

        <div class="mini">
          <div class="mini-title">Level</div>
          <div class="mini-body">Core theory</div>
        </div>

        <div class="mini">
          <div class="mini-title">Main skill</div>
          <div class="mini-body">
            Model uncertainty numerically
          </div>
        </div>

        <div class="mini">
          <div class="mini-title">Next block</div>
          <div class="mini-body">
            Expectation & Variability
          </div>
        </div>

      </div>

    </div>

  </div>

</section>

<!-- CONTINUE READING -->

<section
  class="section"
  id="continue-reading-probability-rv"
  style="display:none;"
>

  <div class="callout">

    <div class="callout-copy">

      <h2>Continue reading</h2>

      <p
        id="continue-reading-probability-rv-label"
        class="muted-mini"
      ></p>

      <a
        class="btn"
        id="continue-reading-probability-rv-btn"
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
      These lessons introduce the mathematical objects that connect
      probability theory to statistical modeling and inference.
    </p>

  </div>

  <div class="grid grid-2">

    <!-- LESSON 1 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/probability/random-variables/what-is-a-random-variable/">
          What Is a Random Variable?
        </a>
      </h3>

      <p>
        Learn how random variables assign numerical values to outcomes
        and why this idea transforms probability into mathematics.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Definition</span>
        <span class="pill">Mapping</span>
        <span class="pill">Foundation</span>
      </div>

      <a
        class="btn btn-outline"
        href="/probability/random-variables/what-is-a-random-variable/"
      >
        Open lesson
      </a>

    </div>

    <!-- LESSON 2 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/probability/random-variables/discrete-random-variables/">
          Discrete Random Variables & PMF
        </a>
      </h3>

      <p>
        Learn probability mass functions,
        supports, summation rules,
        and modeling with discrete outcomes.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Discrete</span>
        <span class="pill">PMF</span>
        <span class="pill">Counting</span>
      </div>

      <a
        class="btn btn-outline"
        href="/probability/random-variables/discrete-random-variables/"
      >
        Open lesson
      </a>

    </div>

    <!-- LESSON 3 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/probability/random-variables/continuous-random-variables/">
          Continuous Random Variables & PDF
        </a>
      </h3>

      <p>
        Learn density functions,
        integration,
        and why individual values have probability zero.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Continuous</span>
        <span class="pill">PDF</span>
        <span class="pill">Density</span>
      </div>

      <a
        class="btn btn-outline"
        href="/probability/random-variables/continuous-random-variables/"
      >
        Open lesson
      </a>

    </div>

    <!-- LESSON 4 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/probability/random-variables/cumulative-distribution-function/">
          Cumulative Distribution Function (CDF)
        </a>
      </h3>

      <p>
        Learn the CDF,
        the one probability function that works for both
        discrete and continuous random variables.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">CDF</span>
        <span class="pill">Probability</span>
        <span class="pill">Distribution</span>
      </div>

      <a
        class="btn btn-outline"
        href="/probability/random-variables/cumulative-distribution-function/"
      >
        Open lesson
      </a>

    </div>

    <!-- LESSON 5 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/probability/random-variables/expectation/">
          Expectation (Mean of a Random Variable)
        </a>
      </h3>

      <p>
        Learn weighted averages,
        expected values,
        and one of the most important concepts in probability.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Expectation</span>
        <span class="pill">Mean</span>
        <span class="pill">Average</span>
      </div>

      <a
        class="btn btn-outline"
        href="/probability/random-variables/expectation/"
      >
        Open lesson
      </a>

    </div>

    <!-- LESSON 6 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/probability/random-variables/variance-and-standard-deviation/">
          Variance & Standard Deviation
        </a>
      </h3>

      <p>
        Learn how probability models measure variability,
        uncertainty,
        and dispersion around expected values.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Variance</span>
        <span class="pill">Spread</span>
        <span class="pill">Uncertainty</span>
      </div>

      <a
        class="btn btn-outline"
        href="/probability/random-variables/variance-and-standard-deviation/"
      >
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
        Previous blocks focused on events and probabilities.
        This block introduces probability distributions,
        which become the primary objects studied throughout statistics.
      </p>

      <div class="table-wrap">

        <table>

          <thead>

            <tr>
              <th>Concept</th>
              <th>Why it matters later</th>
            </tr>

          </thead>

          <tbody>

            <tr>
              <td>Random Variables</td>
              <td>Foundation of statistical models</td>
            </tr>

            <tr>
              <td>PMF & PDF</td>
              <td>Describe probability distributions</td>
            </tr>

            <tr>
              <td>CDF</td>
              <td>Supports probability calculations and theory</td>
            </tr>

            <tr>
              <td>Expectation</td>
              <td>Central concept in inference and prediction</td>
            </tr>

            <tr>
              <td>Variance</td>
              <td>Measures uncertainty and variability</td>
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

        <li>Translate random experiments into random variables</li>

        <li>Work correctly with PMFs and PDFs</li>

        <li>Interpret cumulative distribution functions</li>

        <li>Compute expectations and expected values</li>

        <li>Compute variance and standard deviation</li>

        <li>Understand probability distributions as models of uncertainty</li>

        <li>Prepare for Expectation & Variability</li>

      </ul>

    </div>

    <div class="callout-side">

      <div class="mini">

        <div class="mini-title">Next block</div>

        <div class="mini-body">
          Continue to <strong>Expectation & Variability</strong>
        </div>

      </div>

      <div class="mini">

        <div class="mini-title">Core idea</div>

        <div class="mini-body">
          Random variables convert uncertainty into mathematics.
        </div>

      </div>

      <div class="mini">

        <div class="mini-title">Big transition</div>

        <div class="mini-body">
          This is where probability becomes statistical modeling.
        </div>

      </div>

    </div>

  </div>

</section>

<!-- NAVIGATION -->

<section class="section section-slim">

  <div class="lesson-nav">

    <a class="btn btn-outline" href="/probability/conditional/">
      ← Previous Block: Conditional Probability & Bayes
    </a>

    <a class="btn" href="/probability/expectation-variability/">
      Next Block: Expectation & Variability →
    </a>

  </div>

</section>

<!-- CONTINUE READING SCRIPT -->

<script>
(function () {

  try {

    const KEY =
      "esa_continue_probability_random_variables_lesson_v0";

    const raw = localStorage.getItem(KEY);

    if (!raw) return;

    const data = JSON.parse(raw);

    if (!data || !data.url || !data.label) return;

    const wrap =
      document.getElementById(
        "continue-reading-probability-rv"
      );

    const label =
      document.getElementById(
        "continue-reading-probability-rv-label"
      );

    const btn =
      document.getElementById(
        "continue-reading-probability-rv-btn"
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