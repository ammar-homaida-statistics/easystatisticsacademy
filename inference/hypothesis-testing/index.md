<!-- =========================================================
BLOCK 3 — HYPOTHESIS TESTING
File: /inference/hypothesis-testing/index.md
========================================================= -->
---
layout: default
title: Block 3 — Hypothesis Testing
description: Learn the logic of hypothesis tests: null/alternative, test statistics, Type I/II errors, p-values, and correct decision language.
permalink: /inference/hypothesis-testing/
sidebar: false
---

<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem; letter-spacing:0.5px;">
        🚧 This Block Is Under Construction
      </h2>
      <p style="margin:0; font-size:1.05rem; color:#5d4037; line-height:1.6;">
        This block explains hypothesis testing as a controlled decision framework under uncertainty.
        It focuses on correct definitions and interpretation—not p-value rituals.
      </p>
    </div>
  </div>
</section>

<script>
  (function () {
    var KEY = "esa_continue_inference_last_block_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/hypothesis-testing/",
      label: "Block 3 — Hypothesis Testing",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card hero-split">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 3</span>
        <span class="badge">p-values</span>
        <span class="badge">Errors</span>
        <span class="badge">Decisions</span>
      </div>

      <h1>Block 3 — Hypothesis Testing</h1>
      <p class="lead">
        Hypothesis testing answers: “If the null model were true, how surprising is the data (or something more extreme)?”
        This block formalizes H0/H1, test statistics, Type I/II errors, significance level, and correct reporting language.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/">Back to Statistical Inference</a>
        <a class="btn" href="#lessons">Open structure</a>
      </div>

      <p class="muted-mini">
        Version 0: structure is locked. Lessons will be refined without changing order.
      </p>
    </div>

    <div class="hero-panel">
      <div class="panel-card">
        <h2 class="panel-title">What this block covers</h2>
        <ul class="quickstart" style="list-style:none; padding-left:0; margin:0;">
          <li style="margin:.35rem 0;"><strong>Null vs alternative</strong><span class="meta">Model vs competing claim</span></li>
          <li style="margin:.35rem 0;"><strong>Test statistic</strong><span class="meta">Standardized evidence measure</span></li>
          <li style="margin:.35rem 0;"><strong>Type I / Type II</strong><span class="meta">False positives / false negatives</span></li>
          <li style="margin:.35rem 0;"><strong>p-value meaning</strong><span class="meta">Conditional on H0</span></li>
          <li style="margin:.35rem 0;"><strong>Decision language</strong><span class="meta">Evidence vs proof</span></li>
          <li style="margin:.35rem 0;"><strong>CI connection</strong><span class="meta">Duality intuition</span></li>
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
    <p>Lesson links will appear when published. The list and order will remain stable.</p>
  </div>

  <div class="grid grid-2">
    <div class="card lesson-card">
      <h3>Lesson placeholders</h3>
      <p>Coming soon. This area will contain the permanent lesson list for this block.</p>
      <div class="pill-row"><span class="badge">Coming soon</span></div>
    </div>

    <div class="card lesson-card">
      <h3>Software examples later</h3>
      <p>We will later map output in SPSS/R/Python/Excel to correct interpretation language.</p>
      <div class="pill-row"><span class="badge">Planned</span></div>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of Block 3</h2>
      <ul class="bullets">
        <li>Define H0/H1 and test statistics correctly</li>
        <li>Explain Type I/II errors and the role of \(\alpha\)</li>
        <li>Interpret p-values without common misconceptions</li>
        <li>Write correct “reject / fail to reject” conclusions</li>
      </ul>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Next block</div>
        <div class="mini-body">
          Continue to
          <a href="/inference/classical-tests/" style="color:#1a73e8; text-decoration:underline;">
            <strong>Block 4 — Classical Tests</strong>
          </a>.
        </div>
      </div>
    </div>

  </div>
</section>

<script>
  (function () {
    var KEY = "esa_continue_inference_hypothesis_testing_lesson_v0";
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