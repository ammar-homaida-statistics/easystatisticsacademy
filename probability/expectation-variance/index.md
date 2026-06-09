---
layout: default
title: Block 4 — Expectation & Variability
description: Deepen your understanding of expectation, variance, covariance, correlation, and indicator variables—the mathematical tools that power statistical modeling and inference.
permalink: /probability/expectation-variance/
sidebar: false
---

<!-- SAVE BLOCK PROGRESS -->
<script>
(function () {

  const KEY = "esa_continue_probability_last_block_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/probability/expectation-variance/",
    label: "Block 4 — Expectation & Variability",
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
        <span class="badge">Block 4</span>
        <span class="badge">Expectation</span>
        <span class="badge">Variability</span>
      </div>

      <h1>Block 4 — Expectation & Variability</h1>

      <p class="lead">
        Probability distributions describe uncertainty.
      </p>

      <p class="lead">
        This block develops the mathematical tools used to summarize,
        compare, and analyze random variables. These ideas are essential
        for statistical inference, regression, machine learning,
        and quantitative decision-making.
      </p>

      <p class="muted-mini">
        6 lessons • Mathematical foundations • Builds on Random Variables • Prepares for Common Distributions
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
          📐
        </div>

        <div>

          <strong>Why this block matters</strong>

          <p>
            Expectation and variance are among the most important concepts
            in all of probability and statistics.
            They allow us to quantify typical behavior,
            uncertainty, dependence, and long-run outcomes.
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
          <div class="mini-body">Core probability theory</div>
        </div>

        <div class="mini">
          <div class="mini-title">Main skill</div>
          <div class="mini-body">
            Analyze random variables mathematically
          </div>
        </div>

        <div class="mini">
          <div class="mini-title">Next block</div>
          <div class="mini-body">
            Common Distributions
          </div>
        </div>

      </div>

    </div>

  </div>

</section>

<!-- CONTINUE READING -->

<section
  class="section"
  id="continue-reading-probability-ev"
  style="display:none;"
>

  <div class="callout">

    <div class="callout-copy">

      <h2>Continue reading</h2>

      <p
        id="continue-reading-probability-ev-label"
        class="muted-mini"
      ></p>

      <a
        class="btn"
        id="continue-reading-probability-ev-btn"
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
      These lessons develop the mathematical operators used throughout
      probability, statistical inference, machine learning, and quantitative modeling.
    </p>

  </div>

  <div class="grid grid-2">

    <!-- LESSON 1 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/probability/expectation-variance/linearity-of-expectation/">
          Linearity of Expectation
        </a>
      </h3>

      <p>
        Learn the most powerful rule in probability:
        expectations combine linearly even when variables are not independent.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Expectation</span>
        <span class="pill">Linearity</span>
        <span class="pill">Core Rule</span>
      </div>

      <a
        class="btn btn-outline"
        href="/probability/expectation-variance/linearity-of-expectation/"
      >
        Open lesson
      </a>

    </div>

    <!-- LESSON 2 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/probability/expectation-variance/variance-rules-and-sums/">
          Variance Rules & Sums of Variables
        </a>
      </h3>

      <p>
        Learn how variance changes under scaling,
        shifting, and addition,
        and when variances can be added directly.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Variance</span>
        <span class="pill">Sums</span>
        <span class="pill">Variability</span>
      </div>

      <a
        class="btn btn-outline"
        href="/probability/expectation-variance/variance-rules-and-sums/"
      >
        Open lesson
      </a>

    </div>

    <!-- LESSON 3 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/probability/expectation-variance/covariance/">
          Covariance
        </a>
      </h3>

      <p>
        Learn how covariance measures whether random variables
        tend to move together and why it appears in variance formulas.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Covariance</span>
        <span class="pill">Dependence</span>
        <span class="pill">Joint Behavior</span>
      </div>

      <a
        class="btn btn-outline"
        href="/probability/expectation-variance/covariance/"
      >
        Open lesson
      </a>

    </div>

    <!-- LESSON 4 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/probability/expectation-variance/correlation/">
          Correlation
        </a>
      </h3>

      <p>
        Learn how correlation standardizes covariance,
        how to interpret it correctly,
        and why correlation does not imply causation.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Correlation</span>
        <span class="pill">Association</span>
        <span class="pill">Interpretation</span>
      </div>

      <a
        class="btn btn-outline"
        href="/probability/expectation-variance/correlation/"
      >
        Open lesson
      </a>

    </div>

    <!-- LESSON 5 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/probability/expectation-variance/indicator-random-variables/">
          Indicator Random Variables
        </a>
      </h3>

      <p>
        Transform events into algebraic objects and simplify
        complex counting and expectation problems.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Indicators</span>
        <span class="pill">Counting</span>
        <span class="pill">Technique</span>
      </div>

      <a
        class="btn btn-outline"
        href="/probability/expectation-variance/indicator-random-variables/"
      >
        Open lesson
      </a>

    </div>

    <!-- LESSON 6 -->

    <div class="card lesson-card lesson-block-card">

      <h3>
        <a href="/probability/expectation-variance/applications-mini-cases/">
          Applications: Mini Cases
        </a>
      </h3>

      <p>
        Apply expectation, variance, covariance,
        and indicator-variable techniques to realistic probability problems.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Applications</span>
        <span class="pill">Modeling</span>
        <span class="pill">Practice</span>
      </div>

      <a
        class="btn btn-outline"
        href="/probability/expectation-variance/applications-mini-cases/"
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
        Random variables describe uncertainty.
        This block develops the mathematical tools used to summarize
        and compare random variables before studying the major probability distributions.
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
              <td>Expectation</td>
              <td>Foundation of statistical estimation and prediction</td>
            </tr>

            <tr>
              <td>Variance</td>
              <td>Measures uncertainty and sampling variability</td>
            </tr>

            <tr>
              <td>Covariance</td>
              <td>Used in multivariate statistics and regression</td>
            </tr>

            <tr>
              <td>Correlation</td>
              <td>Measures association between variables</td>
            </tr>

            <tr>
              <td>Indicator Variables</td>
              <td>Powerful tools for probability proofs and counting</td>
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

        <li>Use linearity of expectation confidently</li>

        <li>Apply variance rules correctly</li>

        <li>Understand when variances add</li>

        <li>Interpret covariance appropriately</li>

        <li>Interpret correlation correctly and cautiously</li>

        <li>Use indicator variables to simplify probability problems</li>

        <li>Prepare for Common Probability Distributions</li>

      </ul>

    </div>

    <div class="callout-side">

      <div class="mini">

        <div class="mini-title">Next block</div>

        <div class="mini-body">
          Continue to <strong>Common Distributions</strong>
        </div>

      </div>

      <div class="mini">

        <div class="mini-title">Core idea</div>

        <div class="mini-body">
          Expectation describes typical behavior while variance describes uncertainty.
        </div>

      </div>

      <div class="mini">

        <div class="mini-title">Big transition</div>

        <div class="mini-body">
          These tools become the language used to compare probability models.
        </div>

      </div>

    </div>

  </div>

</section>

<!-- NAVIGATION -->

<section class="section section-slim">

  <div class="lesson-nav">

    <a class="btn btn-outline" href="/probability/random-variables/">
      ← Previous Block: Random Variables
    </a>

    <a class="btn" href="/probability/distributions/">
      Next Block: Common Distributions →
    </a>

  </div>

</section>

<!-- CONTINUE READING SCRIPT -->

<script>
(function () {

  try {

    const KEY =
      "esa_continue_probability_expectation_variance_lesson_v0";

    const raw = localStorage.getItem(KEY);

    if (!raw) return;

    const data = JSON.parse(raw);

    if (!data || !data.url || !data.label) return;

    const wrap =
      document.getElementById(
        "continue-reading-probability-ev"
      );

    const label =
      document.getElementById(
        "continue-reading-probability-ev-label"
      );

    const btn =
      document.getElementById(
        "continue-reading-probability-ev-btn"
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