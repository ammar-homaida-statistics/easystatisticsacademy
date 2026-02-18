---
layout: default
title: Block 4 — Expectation & Variability
description: Deeper tools for summarizing random variables: expectation, variance, covariance, correlation, linearity, and indicator variables—core building blocks for inference and modeling.
permalink: /probability/expectation-variance/
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
        This block deepens your understanding of expectation and variability and introduces
        dependence tools (covariance/correlation) used everywhere in statistics.
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
      url: "/probability/expectation-variance/",
      label: "Block 4 — Expectation & Variability",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card hero-split">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 4</span>
        <span class="badge">Expectation</span>
        <span class="badge">Variability</span>
        <span class="badge">Dependence</span>
      </div>

      <h1>Block 4 — Expectation &amp; Variability</h1>
      <p class="lead">
        Block 3 defined random variables and basic summaries. This block goes deeper:
        expectation as an operator, variance as variability, and new dependence tools
        (covariance and correlation) that power inference, regression, and machine learning.
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
          <li style="margin:.35rem 0;"><strong>Linearity of expectation</strong><span class="meta">The most used rule in probability</span></li>
          <li style="margin:.35rem 0;"><strong>Variance rules</strong><span class="meta">Scaling, shifting, and sums</span></li>
          <li style="margin:.35rem 0;"><strong>Covariance</strong><span class="meta">How variables move together</span></li>
          <li style="margin:.35rem 0;"><strong>Correlation</strong><span class="meta">Standardized dependence</span></li>
          <li style="margin:.35rem 0;"><strong>Indicator variables</strong><span class="meta">Turning events into algebra</span></li>
          <li style="margin:.35rem 0;"><strong>Modeling intuition</strong><span class="meta">Why these tools matter for inference</span></li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="section" id="continue-reading-block4" style="display:none;">
  <div class="callout">
    <div class="callout-copy">
      <h2>Continue reading</h2>
      <p class="muted-mini" id="continue-reading-block4-label" style="margin:0 0 .75rem 0;"></p>
      <a class="btn" id="continue-reading-block4-btn" href="#">Continue</a>
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
      <h3><a href="/probability/expectation-variance/linearity-of-expectation/">1. Linearity of Expectation</a></h3>
      <p>The most important rule: how expectations combine, even without independence.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/probability/expectation-variance/linearity-of-expectation/">Open lesson</a>
      </div>
    </div>

    <!-- Lesson 2 -->
    <div class="card lesson-card">
      <h3><a href="/probability/expectation-variance/variance-rules-and-sums/">2. Variance Rules & Sums of Variables</a></h3>
      <p>Scaling and shifting; why Var(X+Y) needs covariance; when variances add.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/probability/expectation-variance/variance-rules-and-sums/">Open lesson</a>
      </div>
    </div>

    <!-- Lesson 3 -->
    <div class="card lesson-card">
      <h3><a href="/probability/expectation-variance/covariance/">3. Covariance</a></h3>
      <p>Definition, interpretation, and role in Var(X+Y) and dependence structure.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/probability/expectation-variance/covariance/">Open lesson</a>
      </div>
    </div>

    <!-- Lesson 4 -->
    <div class="card lesson-card">
      <h3><a href="/probability/expectation-variance/correlation/">4. Correlation</a></h3>
      <p>Standardized covariance; interpretation; limitations; correlation ≠ causation.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/probability/expectation-variance/correlation/">Open lesson</a>
      </div>
    </div>

    <!-- Lesson 5 -->
    <div class="card lesson-card">
      <h3><a href="/probability/expectation-variance/indicator-random-variables/">5. Indicator Random Variables</a></h3>
      <p>Convert events to algebra; powerful technique for counting and expectation.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/probability/expectation-variance/indicator-random-variables/">Open lesson</a>
      </div>
    </div>

    <!-- Lesson 6 -->
    <div class="card lesson-card">
      <h3><a href="/probability/expectation-variance/applications-mini-cases/">6. Applications: Mini Cases</a></h3>
      <p>Combine expectation, variance, and dependence tools in realistic modeling scenarios.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/probability/expectation-variance/applications-mini-cases/">Open lesson</a>
      </div>
    </div>

  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of Block 4</h2>
      <ul class="bullets">
        <li>Use linearity of expectation confidently (even without independence)</li>
        <li>Apply variance rules correctly and understand when variances add</li>
        <li>Interpret covariance and correlation and avoid common misreadings</li>
        <li>Use indicator variables to simplify counting and expectation problems</li>
        <li>Be ready for Named Distributions (Block 5)</li>
      </ul>
    </div>
    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Next block</div>
        <div class="mini-body">
          Continue to
          <a href="/probability/distributions/" style="color:#1a73e8; text-decoration:underline;">
            <strong>Block 5 — Common Distributions</strong>
          </a>.
        </div>
      </div>
    </div>
  </div>
</section>

<script>
  (function () {
    var KEY = "esa_continue_probability_expectation_variability_lesson_v0";

    var raw = localStorage.getItem(KEY);
    if (!raw) return;

    try {
      var data = JSON.parse(raw);
      if (!data || !data.url || !data.label) return;

      var wrap = document.getElementById("continue-reading-block4");
      var label = document.getElementById("continue-reading-block4-label");
      var btn = document.getElementById("continue-reading-block4-btn");
      if (!wrap || !label || !btn) return;

      label.innerHTML = 'You last visited: <strong>' + data.label + '</strong>';
      btn.href = data.url;
      wrap.style.display = "block";
    } catch (e) {}
  })();
</script>