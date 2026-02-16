---
layout: default
title: Block 5 — Measures of Spread
description: Quantify variability correctly: range, interquartile range (IQR), variance, standard deviation, coefficient of variation, and robust measures of dispersion.
permalink: /descriptive/spread/
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
        This block is currently being developed. Lessons will be published in a fixed pedagogical order
        as part of the Descriptive Statistics unit.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update "last visited block" for Descriptive home -->
<script>
  (function () {
    var KEY = "esa_continue_descriptive_last_block_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/descriptive/spread/",
      label: "Block 5 — Measures of Spread",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card hero-split">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 5</span>
        <span class="badge">Variability</span>
        <span class="badge">Dispersion</span>
        <span class="badge">Interpretation</span>
      </div>

      <h1>Block 5 — Measures of Spread</h1>

      <p class="lead">
        Measures of center describe typical values.
        Measures of spread describe variability.
        This block explains how dispersed, stable, or volatile your data truly are.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/descriptive/">Back to Descriptive Statistics</a>
        <a class="btn" href="#lessons">Open lessons</a>
      </div>

      <p class="muted-mini">
        Version 0: structure is locked. Lessons will be improved over time without changing the overall order.
      </p>
    </div>

    <div class="hero-panel">
      <div class="panel-card">
        <h2 class="panel-title">What this block covers</h2>
        <ul class="quickstart" style="list-style:none; padding-left:0; margin:0;">
          <li style="margin-bottom:.6rem;">
            <strong>Basic dispersion</strong><br>
            <span class="meta">Range and variability concept</span>
          </li>
          <li style="margin-bottom:.6rem;">
            <strong>Robust spread</strong><br>
            <span class="meta">Interquartile range (IQR)</span>
          </li>
          <li style="margin-bottom:.6rem;">
            <strong>Variance & standard deviation</strong><br>
            <span class="meta">Core statistical dispersion measures</span>
          </li>
          <li>
            <strong>Relative variability</strong><br>
            <span class="meta">Coefficient of variation & interpretation</span>
          </li>
        </ul>
      </div>
    </div>
  </div>
</section>

<!-- 🔁 Continue Reading (Block 5 lessons only) -->
<section class="section" id="continue-reading-block5" style="display:none;">
  <div class="callout">
    <div class="callout-copy">
      <h2>Continue reading</h2>
      <p class="muted-mini" id="continue-reading-block5-label" style="margin:0 0 .75rem 0;"></p>
      <a class="btn" id="continue-reading-block5-btn" href="#">Continue</a>
    </div>
  </div>
</section>

<section class="section" id="lessons">
  <div class="section-head">
    <h2>Lessons (Version 0)</h2>
    <p>
      Work through these lessons in order. Each lesson page will become active as the block develops.
    </p>
  </div>

  <div class="grid grid-2">

    <!-- 1 -->
    <div class="card lesson-card">
      <h3><a href="/descriptive/spread/what-is-variability/">1. What Is Variability?</a></h3>
      <p>Why two datasets with the same mean can behave completely differently.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/descriptive/spread/what-is-variability/">Open lesson</a>
      </div>
    </div>

    <!-- 2 -->
    <div class="card lesson-card">
      <h3><a href="/descriptive/spread/range/">2. Range</a></h3>
      <p>The simplest dispersion measure — and why it is often insufficient.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/descriptive/spread/range/">Open lesson</a>
      </div>
    </div>

    <!-- 3 -->
    <div class="card lesson-card">
      <h3><a href="/descriptive/spread/interquartile-range/">3. Interquartile Range (IQR)</a></h3>
      <p>Robust measure of spread resistant to extreme values.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/descriptive/spread/interquartile-range/">Open lesson</a>
      </div>
    </div>

    <!-- 4 -->
    <div class="card lesson-card">
      <h3><a href="/descriptive/spread/variance/">4. Variance</a></h3>
      <p>Squared deviations and the mathematical foundation of variability.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/descriptive/spread/variance/">Open lesson</a>
      </div>
    </div>

    <!-- 5 -->
    <div class="card lesson-card">
      <h3><a href="/descriptive/spread/standard-deviation/">5. Standard Deviation</a></h3>
      <p>The most widely used measure of spread and how to interpret it correctly.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/descriptive/spread/standard-deviation/">Open lesson</a>
      </div>
    </div>

    <!-- 6 -->
    <div class="card lesson-card">
      <h3><a href="/descriptive/spread/coefficient-of-variation/">6. Coefficient of Variation</a></h3>
      <p>Comparing variability across different units or scales.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/descriptive/spread/coefficient-of-variation/">Open lesson</a>
      </div>
    </div>

    <!-- 7 -->
    <div class="card lesson-card">
      <h3><a href="/descriptive/spread/reporting-spread-properly/">7. Reporting Spread Properly</a></h3>
      <p>How to combine center and variability responsibly in reports.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/descriptive/spread/reporting-spread-properly/">Open lesson</a>
      </div>
    </div>

  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of Block 5</h2>
      <ul class="bullets">
        <li>Understand why variability is as important as center</li>
        <li>Choose the correct measure of dispersion</li>
        <li>Interpret variance and standard deviation correctly</li>
        <li>Compare variability across different datasets responsibly</li>
        <li>Prepare for Distribution Shape & Standardization (Block 6)</li>
      </ul>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Next block</div>
        <div class="mini-body">
          Continue to <a href="/descriptive/shape/" style="color:#1a73e8; text-decoration:underline;"><strong>Block 6 — Distribution Shape & Standardization</strong></a>.
        </div>
      </div>
    </div>
  </div>
</section>

<script>
  (function () {
    var KEY = "esa_continue_descriptive_spread_lesson_v0";
    var raw = localStorage.getItem(KEY);
    if (!raw) return;

    try {
      var data = JSON.parse(raw);
      if (!data || !data.url || !data.label) return;

      var wrap = document.getElementById("continue-reading-block5");
      var label = document.getElementById("continue-reading-block5-label");
      var btn = document.getElementById("continue-reading-block5-btn");
      if (!wrap || !label || !btn) return;

      label.innerHTML = 'You last visited: <strong>' + data.label + '</strong>';
      btn.href = data.url;
      wrap.style.display = "block";
    } catch (e) {}
  })();
</script>