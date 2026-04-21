---
layout: default
title: Probability & Theory
description: Build correct probability intuition: events, random variables, distributions, and the theory needed for statistical inference.
permalink: /probability/
sidebar: false
---

<!-- HERO -->
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
        Learn probability correctly: events, conditional probability, random variables,
        and distributions — the theoretical foundation of statistical inference.
      </p>

      <p class="muted-mini">
        7 structured blocks • Concept-first • Bridge to inference
      </p>

      <div class="hero-actions">
        <a class="btn" href="#blocks">Start Learning</a>
        <a class="btn btn-outline" href="/inference/">Next: Inference</a>
      </div>

      <div style="background:#fff3cd; border:1px solid #ffeeba; padding:12px 14px; margin:14px 0; border-radius:8px;">
        <strong>🚧 Under Construction</strong> — This unit is being developed block-by-block
        with deep conceptual explanations and practical examples.
      </div>

    </div>

    <div class="hero-panel">
      <div class="panel-card">

        <h2 class="panel-title">Suggested learning order</h2>

        <ol class="quickstart">
          <li>Probability basics</li>
          <li>Conditional probability</li>
          <li>Random variables</li>
          <li>Expectation & variance</li>
          <li>Distributions</li>
          <li>LLN & CLT</li>
          <li>Sampling distributions</li>
        </ol>

      </div>
    </div>

  </div>
</section>

<!-- BLOCKS -->
<section class="section" id="blocks">

  <div class="section-head">
    <h2>Blocks (Unit Structure)</h2>
    <p>
      Follow the blocks in order. Each block builds the theoretical foundation
      required for statistical inference.
    </p>
  </div>

  <!-- CONTINUE READING -->
  <div id="continue-reading-probability" style="display:none; margin-bottom:20px;">
    <div class="callout">
      <div class="callout-copy">
        <h2>Continue reading</h2>
        <p id="continue-reading-probability-label" class="muted-mini"></p>
        <a class="btn" id="continue-reading-probability-btn" href="#">Continue</a>
      </div>
    </div>
  </div>

  <div class="grid grid-2">

    <!-- BLOCK 1 -->
    <div class="card lesson-card">
      <h3><a href="/probability/basics/">Block 1 — Probability Basics</a></h3>
      <p>Events, rules, independence, and intuition about randomness.</p>
      <a class="btn btn-outline" href="/probability/basics/">Open block</a>
    </div>

    <!-- BLOCK 2 -->
    <div class="card lesson-card">
      <h3><a href="/probability/conditional/">Block 2 — Conditional Probability & Bayes</a></h3>
      <p>Conditional reasoning, total probability, and Bayes' theorem.</p>
      <a class="btn btn-outline" href="/probability/conditional/">Open block</a>
    </div>

    <!-- BLOCK 3 -->
    <div class="card lesson-card">
      <h3><a href="/probability/random-variables/">Block 3 — Random Variables</a></h3>
      <p>PMF, PDF, CDF, and understanding distributions correctly.</p>
      <a class="btn btn-outline" href="/probability/random-variables/">Open block</a>
    </div>

    <!-- BLOCK 4 -->
    <div class="card lesson-card">
      <h3><a href="/probability/expectation-variance/">Block 4 — Expectation & Variance</a></h3>
      <p>Mean, variance, covariance, and linearity properties.</p>
      <a class="btn btn-outline" href="/probability/expectation-variance/">Open block</a>
    </div>

    <!-- BLOCK 5 -->
    <div class="card lesson-card">
      <h3><a href="/probability/distributions/">Block 5 — Common Distributions</a></h3>
      <p>Binomial, Normal, Poisson, Exponential, and when to use them.</p>
      <a class="btn btn-outline" href="/probability/distributions/">Open block</a>
    </div>

    <!-- BLOCK 6 -->
    <div class="card lesson-card">
      <h3><a href="/probability/lln-clt/">Block 6 — LLN & CLT</a></h3>
      <p>Why averages stabilize and why normal approximation appears.</p>
      <a class="btn btn-outline" href="/probability/lln-clt/">Open block</a>
    </div>

    <!-- BLOCK 7 -->
    <div class="card lesson-card">
      <h3><a href="/probability/sampling-distributions/">Block 7 — Sampling Distributions</a></h3>
      <p>Bridge from probability to inference and statistical testing.</p>
      <a class="btn btn-outline" href="/probability/sampling-distributions/">Open block</a>
    </div>

  </div>
</section>

<!-- GOAL -->
<section class="section section-slim">
  <div class="callout">

    <div class="callout-copy">
      <h2>Goal of this unit</h2>
      <ul class="bullets">
        <li>Understand randomness correctly</li>
        <li>Work with probability rules and conditional reasoning</li>
        <li>Model uncertainty using distributions</li>
        <li>Prepare for statistical inference</li>
      </ul>
    </div>

    <div class="callout-side">
      <div class="mini">
        <div class="mini-title">Next</div>
        <div class="mini-body">
          Continue to <strong>Statistical Inference</strong>
        </div>
      </div>
      <div class="mini">
        <div class="mini-title">Note</div>
        <div class="mini-body">
          This is the theoretical core of statistics
        </div>
      </div>
    </div>

  </div>
</section>

<!-- CONTINUE READING SCRIPT -->
<script>
(function () {
  try {
    const KEY = "esa_continue_probability_last_block_v0";
    const raw = localStorage.getItem(KEY);
    if (!raw) return;

    const data = JSON.parse(raw);
    if (!data || !data.url || !data.label) return;

    const wrap = document.getElementById("continue-reading-probability");
    const label = document.getElementById("continue-reading-probability-label");
    const btn = document.getElementById("continue-reading-probability-btn");

    if (!wrap || !label || !btn) return;

    label.innerHTML = "You last visited: <strong>" + data.label + "</strong>";
    btn.href = data.url;
    wrap.style.display = "block";

  } catch (e) {}
})();
</script>