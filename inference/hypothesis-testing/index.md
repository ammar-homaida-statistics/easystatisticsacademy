<!-- =========================================================
BLOCK 3 — HYPOTHESIS TESTING
File: /inference/hypothesis-testing/index.md
========================================================= -->
---
layout: default
title: Block 3 — Hypothesis Testing
description: Learn the logic of hypothesis testing: null models, test statistics, p-values, Type I and II errors, power, and decision-making under uncertainty.
permalink: /inference/hypothesis-testing/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem; letter-spacing:0.5px;">
        🚧 This Block Is Under Construction
      </h2>
      <p style="margin:0; font-size:1.05rem; color:#5d4037; line-height:1.6;">
        This block develops <strong>hypothesis testing</strong> from first principles:
        null models, test statistics, p-values, error types, and statistical power.
        The goal is conceptual clarity before formulas.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update last visited block -->
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
        <span class="badge">Testing</span>
        <span class="badge">p-value</span>
        <span class="badge">Decision</span>
      </div>

      <h1>Block 3 — Hypothesis Testing</h1>

      <p class="lead">
        Hypothesis testing formalizes decision-making under uncertainty.
        We compare observed data to a null model and quantify
        how surprising the data would be if that model were true.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/">Back to Statistical Inference</a>
        <a class="btn" href="#lessons">Open structure</a>
      </div>

      <p class="muted-mini">
        Version 0: conceptual structure locked. Lessons expand without changing order.
      </p>
    </div>

    <div class="hero-panel">
      <div class="panel-card">
        <h2 class="panel-title">What this block covers</h2>
        <ul class="quickstart" style="list-style:none; padding-left:0; margin:0;">
          <li style="margin:.35rem 0;"><strong>Null hypothesis</strong><span class="meta">Reference model</span></li>
          <li style="margin:.35rem 0;"><strong>Test statistic</strong><span class="meta">Signal measured in SE units</span></li>
          <li style="margin:.35rem 0;"><strong>p-value</strong><span class="meta">Tail probability under H₀</span></li>
          <li style="margin:.35rem 0;"><strong>Error types</strong><span class="meta">Type I and Type II</span></li>
          <li style="margin:.35rem 0;"><strong>Power</strong><span class="meta">Detecting real effects</span></li>
          <li style="margin:.35rem 0;"><strong>CI–Test link</strong><span class="meta">Two sides of same logic</span></li>
        </ul>
      </div>
    </div>
  </div>
</section>

<!-- Continue Reading placeholder -->
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
      The order below follows the logical structure of hypothesis testing.
    </p>
  </div>

  <div class="grid grid-2">

    <!-- Lesson 1 -->
    <div class="card lesson-card">
      <h3><a href="/inference/hypothesis-testing/what-is-a-hypothesis-test/">1. What Is a Hypothesis Test?</a></h3>
      <p>Testing as a structured decision rule under uncertainty.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/inference/hypothesis-testing/what-is-a-hypothesis-test/">Open lesson</a>
      </div>
    </div>

    <!-- Lesson 2 -->
    <div class="card lesson-card">
      <h3><a href="/inference/hypothesis-testing/null-and-alternative/">2. Null and Alternative Hypotheses</a></h3>
      <p>Equality in H₀, directional vs non-directional alternatives.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/inference/hypothesis-testing/null-and-alternative/">Open lesson</a>
      </div>
    </div>

    <!-- Lesson 3 -->
    <div class="card lesson-card">
      <h3><a href="/inference/hypothesis-testing/test-statistic-standardization/">3. Test Statistics and Standardization</a></h3>
      <p>Signal measured in standard error units.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/inference/hypothesis-testing/test-statistic-standardization/">Open lesson</a>
      </div>
    </div>

    <!-- Lesson 4 -->
    <div class="card lesson-card">
      <h3><a href="/inference/hypothesis-testing/p-value-meaning/">4. The p-Value: Meaning and Misinterpretation</a></h3>
      <p>What a p-value is — and what it is not.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/inference/hypothesis-testing/p-value-meaning/">Open lesson</a>
      </div>
    </div>

    <!-- Lesson 5 -->
    <div class="card lesson-card">
      <h3><a href="/inference/hypothesis-testing/significance-level-alpha/">5. Significance Level (α) and Decision Rules</a></h3>
      <p>Pre-specifying risk of false positives.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/inference/hypothesis-testing/significance-level-alpha/">Open lesson</a>
      </div>
    </div>

    <!-- Lesson 6 -->
    <div class="card lesson-card">
      <h3><a href="/inference/hypothesis-testing/type1-type2-errors/">6. Type I and Type II Errors</a></h3>
      <p>False positives, false negatives, and trade-offs.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/inference/hypothesis-testing/type1-type2-errors/">Open lesson</a>
      </div>
    </div>

    <!-- Lesson 7 -->
    <div class="card lesson-card">
      <h3><a href="/inference/hypothesis-testing/power-and-effect-size/">7. Power and Effect Size</a></h3>
      <p>Probability of detecting real effects.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/inference/hypothesis-testing/power-and-effect-size/">Open lesson</a>
      </div>
    </div>

    <!-- Lesson 8 -->
    <div class="card lesson-card">
      <h3><a href="/inference/hypothesis-testing/one-sided-vs-two-sided/">8. One-Sided vs Two-Sided Tests</a></h3>
      <p>Directional hypotheses and tail areas.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/inference/hypothesis-testing/one-sided-vs-two-sided/">Open lesson</a>
      </div>
    </div>

    <!-- Lesson 9 -->
    <div class="card lesson-card">
      <h3><a href="/inference/hypothesis-testing/ci-and-test-connection/">9. Connection Between CIs and Tests</a></h3>
      <p>Why exclusion of 0 corresponds to rejection of H₀.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/inference/hypothesis-testing/ci-and-test-connection/">Open lesson</a>
      </div>
    </div>

    <!-- Lesson 10 -->
    <div class="card lesson-card">
      <h3><a href="/inference/hypothesis-testing/practical-significance/">10. Statistical vs Practical Significance</a></h3>
      <p>Small p-values vs meaningful effects.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/inference/hypothesis-testing/practical-significance/">Open lesson</a>
      </div>
    </div>

  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of Block 3</h2>
      <ul class="bullets">
        <li>Understand hypothesis testing logic from first principles</li>
        <li>Interpret p-values correctly</li>
        <li>Explain error types and power</li>
        <li>Connect tests to confidence intervals</li>
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