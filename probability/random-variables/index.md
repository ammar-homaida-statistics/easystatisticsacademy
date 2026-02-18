---
layout: default
title: Block 3 — Random Variables
description: From events to numerical quantities: discrete and continuous random variables, probability distributions, expectation, variance, and foundational probabilistic modeling.
permalink: /probability/random-variables/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem; letter-spacing:0.5px;">
        🚧 This Section Is Under Construction
      </h2>
      <p style="margin:0; font-size:1.05rem; color:#5d4037; line-height:1.6;">
        This block introduces random variables and probability distributions.
        Lessons are being published in fixed pedagogical order as part of the Probability unit.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update "last visited block" for Probability home -->
<script>
  (function () {
    var KEY = "esa_continue_probability_last_block_v0";

    localStorage.setItem(KEY, JSON.stringify({
      url: "/probability/random-variables/",
      label: "Block 3 — Random Variables",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card hero-split">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 3</span>
        <span class="badge">Random Variables</span>
        <span class="badge">Distributions</span>
        <span class="badge">Expectation</span>
      </div>

      <h1>Block 3 — Random Variables</h1>
      <p class="lead">
        A random variable assigns numbers to outcomes.
        This block transforms probability from set-based reasoning
        into quantitative modeling — the foundation of statistical inference.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/probability/">Back to Probability</a>
        <a class="btn" href="#lessons">Open lessons</a>
      </div>

      <p class="muted-mini">
        Version 0: structure is locked. Lessons will be refined without changing order.
      </p>
    </div>

    <div class="hero-panel">
      <div class="panel-card">
        <h2 class="panel-title">What this block covers</h2>
        <ul class="quickstart" style="list-style:none; padding-left:0; margin:0;">
          <li style="margin:.35rem 0;"><strong>Definition of random variables</strong><span class="meta">Mapping outcomes to numbers</span></li>
          <li style="margin:.35rem 0;"><strong>Discrete random variables</strong><span class="meta">PMF and summation</span></li>
          <li style="margin:.35rem 0;"><strong>Continuous random variables</strong><span class="meta">PDF and integration</span></li>
          <li style="margin:.35rem 0;"><strong>CDF</strong><span class="meta">Cumulative distribution function</span></li>
          <li style="margin:.35rem 0;"><strong>Expectation</strong><span class="meta">Weighted averages</span></li>
          <li style="margin:.35rem 0;"><strong>Variance</strong><span class="meta">Quantifying variability</span></li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="section" id="continue-reading-block3" style="display:none;">
  <div class="callout">
    <div class="callout-copy">
      <h2>Continue reading</h2>
      <p class="muted-mini" id="continue-reading-block3-label" style="margin:0 0 .75rem 0;"></p>
      <a class="btn" id="continue-reading-block3-btn" href="#">Continue</a>
    </div>
  </div>
</section>

<section class="section" id="lessons">
  <div class="section-head">
    <h2>Lessons (Version 0)</h2>
    <p>
      Work through these lessons in order. Each lesson page is active
      (even if still being developed), so you can navigate the full structure now.
    </p>
  </div>

  <div class="grid grid-2">

    <!-- Lesson 1 -->
    <div class="card lesson-card">
      <h3><a href="/probability/random-variables/what-is-a-random-variable/">1. What Is a Random Variable?</a></h3>
      <p>From events to numbers; formal definition; mapping outcomes to real values.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/probability/random-variables/what-is-a-random-variable/">Open lesson</a>
      </div>
    </div>

    <!-- Lesson 2 -->
    <div class="card lesson-card">
      <h3><a href="/probability/random-variables/discrete-random-variables/">2. Discrete Random Variables & PMF</a></h3>
      <p>Probability mass function, support, summation rules, and basic modeling.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/probability/random-variables/discrete-random-variables/">Open lesson</a>
      </div>
    </div>

    <!-- Lesson 3 -->
    <div class="card lesson-card">
      <h3><a href="/probability/random-variables/continuous-random-variables/">3. Continuous Random Variables & PDF</a></h3>
      <p>Density functions, integration, and why P(X = x) = 0 in continuous models.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/probability/random-variables/continuous-random-variables/">Open lesson</a>
      </div>
    </div>

    <!-- Lesson 4 -->
    <div class="card lesson-card">
      <h3><a href="/probability/random-variables/cumulative-distribution-function/">4. Cumulative Distribution Function (CDF)</a></h3>
      <p>Unifying discrete and continuous cases; properties and interpretation.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/probability/random-variables/cumulative-distribution-function/">Open lesson</a>
      </div>
    </div>

    <!-- Lesson 5 -->
    <div class="card lesson-card">
      <h3><a href="/probability/random-variables/expectation/">5. Expectation (Mean of a Random Variable)</a></h3>
      <p>Weighted averages, linearity of expectation, and interpretation.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/probability/random-variables/expectation/">Open lesson</a>
      </div>
    </div>

    <!-- Lesson 6 -->
    <div class="card lesson-card">
      <h3><a href="/probability/random-variables/variance-and-standard-deviation/">6. Variance & Standard Deviation</a></h3>
      <p>Measuring spread; variance formula; properties; connection to uncertainty.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/probability/random-variables/variance-and-standard-deviation/">Open lesson</a>
      </div>
    </div>

  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of Block 3</h2>
      <ul class="bullets">
        <li>Translate probabilistic experiments into random variables</li>
        <li>Work with PMF, PDF, and CDF correctly</li>
        <li>Compute expectation and variance</li>
        <li>Understand how probability distributions summarize uncertainty</li>
        <li>Be ready for deeper work on expectation, variability, and linearity (Block 4)</li>
      </ul>
    </div>
    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Next block</div>
        <div class="mini-body">
          Continue to
          <a href="/probability/expectation-variability/" style="color:#1a73e8; text-decoration:underline;">
            <strong>Block 4 — Expectation & Variability</strong>
          </a>.
        </div>
      </div>
    </div>
  </div>
</section>
<script>
  (function () {
    var KEY = "esa_continue_probability_random_variables_lesson_v0";

    var raw = localStorage.getItem(KEY);
    if (!raw) return;

    try {
      var data = JSON.parse(raw);
      if (!data || !data.url || !data.label) return;

      var wrap = document.getElementById("continue-reading-block3");
      var label = document.getElementById("continue-reading-block3-label");
      var btn = document.getElementById("continue-reading-block3-btn");
      if (!wrap || !label || !btn) return;

      label.innerHTML = 'You last visited: <strong>' + data.label + '</strong>';
      btn.href = data.url;
      wrap.style.display = "block";
    } catch (e) {}
  })();
</script>