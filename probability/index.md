---
layout: default
title: Probability & Theory
description: Build correct probability intuition: events, random variables, distributions, and the theory needed for statistical inference.
permalink: /probability/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:1.5rem; border-radius:10px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem; letter-spacing:0.5px;">
        🚧 This Section Is Under Construction
      </h2>
      <p style="margin:0; font-size:1.05rem; color:#5d4037; line-height:1.6;">
        The Probability unit is currently being developed in a structured, block-by-block format.
        Pages and lessons are being published in a fixed pedagogical order to ensure clarity, stability,
        and long-term academic consistency.
      </p>
    </div>
  </div>
</section>

<section class="hero hero-section">
  <div class="hero-card hero-split">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Core theory</span>
        <span class="badge">Randomness</span>
        <span class="badge">Distributions</span>
        <span class="badge">Inference bridge</span>
      </div>

      <h1>Probability &amp; Theory</h1>
      <p class="lead">
        Learn probability correctly: events, conditional probability, random variables, distributions,
        and the key theoretical tools that power statistical inference and machine learning.
      </p>

      <div class="hero-actions">
        <a class="btn" href="/descriptive/">Prerequisite: Descriptive</a>
        <a class="btn btn-outline" href="/inference/">Next: Statistical Inference</a>
      </div>

      <p class="muted-mini">
        This landing page is the permanent structure for the Probability unit. Lessons are published block-by-block.
      </p>
    </div>

    <div class="hero-panel">
      <div class="panel-card">
        <h2 class="panel-title">Suggested learning order</h2>
        <ol class="quickstart">
          <li><a href="#blocks">Probability basics</a><span class="meta">Events, rules, intuition</span></li>
          <li><a href="#blocks">Conditional probability</a><span class="meta">Bayes, total probability</span></li>
          <li><a href="#blocks">Random variables</a><span class="meta">PMF/PDF/CDF</span></li>
          <li><a href="#blocks">Expectation &amp; variance</a><span class="meta">Mean, variance, covariance</span></li>
          <li><a href="#blocks">Common distributions</a><span class="meta">Binomial, Normal, etc.</span></li>
          <li><a href="#blocks">LLN &amp; CLT</a><span class="meta">Why averages stabilize</span></li>
          <li><a href="#blocks">Sampling distributions</a><span class="meta">Bridge to inference</span></li>
        </ol>
      </div>
    </div>
  </div>
</section>

<section class="section" id="blocks">
  <div class="section-head">
    <h2>Blocks (Unit Structure)</h2>
    <p>
      Probability is organized into seven blocks. Each block has its own page and a growing set of lessons.
      The blocks below are active; lessons inside each block will be marked as coming soon until published.
    </p>
  </div>

  <!-- ✅ Continue reading (Probability home → last visited BLOCK) -->
  <div id="continue-reading-probability" style="display:none; margin-top:0.75rem;">
    <div class="callout">
      <div class="callout-copy">
        <h2>Continue reading</h2>
        <p class="muted-mini" id="continue-reading-probability-label" style="margin:0 0 .75rem 0;"></p>
        <a class="btn" id="continue-reading-probability-btn" href="#">Continue</a>
      </div>
    </div>
  </div>

  <div class="grid grid-2">

    <!-- Block 1 -->
    <div class="card lesson-card">
      <h3>
        <a href="/probability/basics/">Block 1 — Probability Basics (Events &amp; Rules)</a>
      </h3>

      <p>
        Build correct intuition about randomness: sample spaces and events, probability rules,
        complements and unions, independence vs disjointness, and common beginner mistakes.
      </p>

      <div class="pill-row">
        <a class="btn btn-outline" href="/probability/basics/">Open block</a>
      </div>
    </div>

    <!-- Block 2 -->
    <div class="card lesson-card">
      <h3>
        <a href="/probability/conditional/">Block 2 — Conditional Probability &amp; Bayes</a>
      </h3>

      <p>
        Learn conditional probability, multiplication rules, the law of total probability,
        and Bayes’ theorem with diagnostic and real-world interpretation.
      </p>

      <div class="pill-row">
        <a class="btn btn-outline" href="/probability/conditional/">Open block</a>
      </div>
    </div>

    <!-- Block 3 -->
    <div class="card lesson-card">
      <h3>
        <a href="/probability/random-variables/">Block 3 — Random Variables</a>
      </h3>

      <p>
        Define random variables properly and interpret distributions using PMF, PDF, and CDF.
        Understand discrete vs continuous and why “density is not probability.”
      </p>

      <div class="pill-row">
        <a class="btn btn-outline" href="/probability/random-variables/">Open block</a>
      </div>
    </div>

    <!-- Block 4 -->
    <div class="card lesson-card">
      <h3>
        <a href="/probability/expectation-variance/">Block 4 — Expectation &amp; Variability</a>
      </h3>

      <p>
        Work with expectation, variance, covariance, correlation, linearity,
        and foundational tools like indicator variables (with practical intuition).
      </p>

      <div class="pill-row">
        <a class="btn btn-outline" href="/probability/expectation-variance/">Open block</a>
      </div>
    </div>

    <!-- Block 5 -->
    <div class="card lesson-card">
      <h3>
        <a href="/probability/distributions/">Block 5 — Common Distributions</a>
      </h3>

      <p>
        Learn the core distributions used everywhere: Bernoulli, Binomial, Geometric, Poisson,
        Uniform, Exponential, and Normal—plus when each applies.
      </p>

      <div class="pill-row">
        <a class="btn btn-outline" href="/probability/distributions/">Open block</a>
      </div>
    </div>

    <!-- Block 6 -->
    <div class="card lesson-card">
      <h3>
        <a href="/probability/lln-clt/">Block 6 — Law of Large Numbers &amp; CLT</a>
      </h3>

      <p>
        Understand convergence and why averages stabilize. Learn the CLT intuition that explains
        normal approximations and supports inference methods.
      </p>

      <div class="pill-row">
        <a class="btn btn-outline" href="/probability/lln-clt/">Open block</a>
      </div>
    </div>

    <!-- Block 7 -->
    <div class="card lesson-card">
      <h3>
        <a href="/probability/sampling-distributions/">Block 7 — Sampling Distributions (Bridge to Inference)</a>
      </h3>

      <p>
        Connect probability to inference: parameters vs statistics, sampling distributions, standard error,
        and the core idea behind t/chi-square/F distributions (preview only).
      </p>

      <div class="pill-row">
        <a class="btn btn-outline" href="/probability/sampling-distributions/">Open block</a>
      </div>
    </div>

  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Goal of this unit</h2>
      <ul class="bullets">
        <li>Build correct probability intuition (not memorization)</li>
        <li>Understand events, conditional probability, and independence</li>
        <li>Model randomness using random variables and distributions</li>
        <li>Prepare cleanly for Statistical Inference and later Modeling/ML</li>
      </ul>
    </div>

    <div class="callout-side">
      <div class="mini">
        <div class="mini-title">Publishing strategy</div>
        <div class="mini-body">Lessons are published block-by-block to keep the unit coherent.</div>
      </div>
      <div class="mini">
        <div class="mini-title">Next section</div>
        <div class="mini-body">Continue to <strong>Statistical Inference</strong> after completing this unit.</div>
      </div>
      <div class="mini">
        <div class="mini-title">Software later</div>
        <div class="mini-body">Examples will later include SPSS/R/Python/Excel workflows.</div>
      </div>
    </div>
  </div>
</section>

<script>
  (function () {
    // ✅ Probability HOME continues the last visited BLOCK (not lessons)
    // Separate key so it never affects other site sections
    var KEY = "esa_continue_probability_last_block_v0";
    var raw = localStorage.getItem(KEY);
    if (!raw) return;

    try {
      var data = JSON.parse(raw);
      if (!data || !data.url || !data.label) return;

      var wrap = document.getElementById("continue-reading-probability");
      var label = document.getElementById("continue-reading-probability-label");
      var btn = document.getElementById("continue-reading-probability-btn");
      if (!wrap || !label || !btn) return;

      label.innerHTML = 'You last visited: <strong>' + data.label + '</strong>';
      btn.href = data.url;
      wrap.style.display = "block";
    } catch (e) {}
  })();
</script>