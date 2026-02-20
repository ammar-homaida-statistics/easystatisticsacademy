<!-- =========================================================
BLOCK 4 — CLASSICAL TESTS
File: /inference/classical-tests/index.md
========================================================= -->
---
layout: default
title: Block 4 — Classical Tests
description: Apply core inference tools: t-tests, proportion tests, and chi-square tests with assumptions and correct interpretation.
permalink: /inference/classical-tests/
sidebar: false
---

<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem; letter-spacing:0.5px;">
        🚧 This Block Is Under Construction
      </h2>
      <p style="margin:0; font-size:1.05rem; color:#5d4037; line-height:1.6;">
        This block collects the most common classical tests and ties each one to its assumptions,
        effect interpretation, and correct reporting—without turning inference into checklist behavior.
      </p>
    </div>
  </div>
</section>

<script>
  (function () {
    var KEY = "esa_continue_inference_last_block_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/classical-tests/",
      label: "Block 4 — Classical Tests",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card hero-split">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 4</span>
        <span class="badge">t</span>
        <span class="badge">\(\chi^2\)</span>
        <span class="badge">Proportions</span>
      </div>

      <h1>Block 4 — Classical Tests</h1>
      <p class="lead">
        This block covers the standard inference toolbox used in practice: t-tests, proportion inference,
        and chi-square tests. The focus is not just “how to compute,” but how to decide correctly and interpret results.
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
          <li style="margin:.35rem 0;"><strong>t-tests</strong><span class="meta">Mean inference for 1/2/paired samples</span></li>
          <li style="margin:.35rem 0;"><strong>Proportion inference</strong><span class="meta">One and two proportions</span></li>
          <li style="margin:.35rem 0;"><strong>\(\chi^2\) tests</strong><span class="meta">GOF and independence</span></li>
          <li style="margin:.35rem 0;"><strong>Assumptions</strong><span class="meta">Independence, variance, counts</span></li>
          <li style="margin:.35rem 0;"><strong>Effect interpretation</strong><span class="meta">Practical meaning, not only p</span></li>
          <li style="margin:.35rem 0;"><strong>Reporting</strong><span class="meta">Correct statements and limitations</span></li>
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
      <p>Workflows in SPSS/R/Python/Excel will be added after the conceptual core is stable.</p>
      <div class="pill-row"><span class="badge">Planned</span></div>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of Block 4</h2>
      <ul class="bullets">
        <li>Select an appropriate classical test for common study designs</li>
        <li>Check the key assumptions conceptually</li>
        <li>Interpret results with effect + uncertainty (not only p-values)</li>
        <li>Write correct reporting sentences</li>
      </ul>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Next block</div>
        <div class="mini-body">
          Continue to
          <a href="/inference/power-sample-size/" style="color:#1a73e8; text-decoration:underline;">
            <strong>Block 5 — Power & Sample Size</strong>
          </a>.
        </div>
      </div>
    </div>
  </div>
</section>

<script>
  (function () {
    var KEY = "esa_continue_inference_classical_tests_lesson_v0";
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