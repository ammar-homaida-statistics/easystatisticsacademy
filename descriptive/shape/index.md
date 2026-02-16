---
layout: default
title: Block 6 — Distribution Shape & Standardization
description: Understand distribution shape (symmetry, skewness, tails), normal patterns, z-scores, and when standardization helps or misleads.
permalink: /descriptive/shape/
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
      url: "/descriptive/shape/",
      label: "Block 6 — Distribution Shape & Standardization",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card hero-split">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 6</span>
        <span class="badge">Shape</span>
        <span class="badge">Skewness</span>
        <span class="badge">Z-scores</span>
        <span class="badge">Standardization</span>
      </div>

      <h1>Block 6 — Distribution Shape &amp; Standardization</h1>

      <p class="lead">
        Center and spread are not enough. Two datasets can have the same mean and standard deviation
        but behave very differently. This block explains distribution shape (symmetry, skewness, tails),
        and introduces standardization (z-scores) as a tool for comparison.
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
            <strong>Shape basics</strong><br>
            <span class="meta">Symmetry, skewness, tails, outliers</span>
          </li>
          <li style="margin-bottom:.6rem;">
            <strong>Normal patterns</strong><br>
            <span class="meta">Bell shape, empirical rule, why “normal” is special</span>
          </li>
          <li style="margin-bottom:.6rem;">
            <strong>Standardization</strong><br>
            <span class="meta">Z-scores, interpretation, comparability across scales</span>
          </li>
          <li>
            <strong>Practical interpretation</strong><br>
            <span class="meta">When shape changes conclusions about center/spread</span>
          </li>
        </ul>
      </div>
    </div>
  </div>
</section>

<!-- 🔁 Continue Reading (Block 6 lessons only) -->
<section class="section" id="continue-reading-block6" style="display:none;">
  <div class="callout">
    <div class="callout-copy">
      <h2>Continue reading</h2>
      <p class="muted-mini" id="continue-reading-block6-label" style="margin:0 0 .75rem 0;"></p>
      <a class="btn" id="continue-reading-block6-btn" href="#">Continue</a>
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
      <h3><a href="/descriptive/shape/why-shape-matters/">1. Why Distribution Shape Matters</a></h3>
      <p>How shape changes interpretation even when mean and SD are the same.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/descriptive/shape/why-shape-matters/">Open lesson</a>
      </div>
    </div>

    <!-- 2 -->
    <div class="card lesson-card">
      <h3><a href="/descriptive/shape/symmetry-and-skewness/">2. Symmetry and Skewness</a></h3>
      <p>Right-skew vs left-skew, what “long tail” means, and how to recognize it.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/descriptive/shape/symmetry-and-skewness/">Open lesson</a>
      </div>
    </div>

    <!-- 3 -->
    <div class="card lesson-card">
      <h3><a href="/descriptive/shape/skewness-and-center-choice/">3. Skewness and Choosing Mean vs Median</a></h3>
      <p>Why skewness makes the mean unstable and when median is the safer summary.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/descriptive/shape/skewness-and-center-choice/">Open lesson</a>
      </div>
    </div>

    <!-- 4 -->
    <div class="card lesson-card">
      <h3><a href="/descriptive/shape/tails-outliers-and-extremes/">4. Tails, Outliers, and Extreme Values</a></h3>
      <p>Tails vs outliers, why extremes matter, and how they affect interpretation.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/descriptive/shape/tails-outliers-and-extremes/">Open lesson</a>
      </div>
    </div>

    <!-- 5 -->
    <div class="card lesson-card">
      <h3><a href="/descriptive/shape/normal-distribution-concept/">5. The Normal Distribution (Conceptual)</a></h3>
      <p>What “normal” means, why it appears often, and why it is used as a reference.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/descriptive/shape/normal-distribution-concept/">Open lesson</a>
      </div>
    </div>

    <!-- 6 -->
    <div class="card lesson-card">
      <h3><a href="/descriptive/shape/empirical-rule/">6. The Empirical Rule (68–95–99.7)</a></h3>
      <p>How to read “typical” ranges in bell-shaped data and what breaks the rule.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/descriptive/shape/empirical-rule/">Open lesson</a>
      </div>
    </div>

    <!-- 7 -->
    <div class="card lesson-card">
      <h3><a href="/descriptive/shape/z-scores/">7. Z-scores (Standardization)</a></h3>
      <p>Translate values into “how many SDs from the mean” for comparison across scales.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/descriptive/shape/z-scores/">Open lesson</a>
      </div>
    </div>

    <!-- 8 -->
    <div class="card lesson-card">
      <h3><a href="/descriptive/shape/standardization-when-and-when-not/">8. Standardization: When It Helps and When It Misleads</a></h3>
      <p>Good for comparability; dangerous when distributions differ or have outliers.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/descriptive/shape/standardization-when-and-when-not/">Open lesson</a>
      </div>
    </div>

    <!-- 9 -->
    <div class="card lesson-card">
      <h3><a href="/descriptive/shape/shape-in-reporting/">9. Reporting Shape Properly</a></h3>
      <p>How to describe skewness, tails, and outliers clearly in academic and business reports.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/descriptive/shape/shape-in-reporting/">Open lesson</a>
      </div>
    </div>

  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of Block 6</h2>
      <ul class="bullets">
        <li>Recognize and describe skewness, symmetry, and tails</li>
        <li>Understand how shape changes the meaning of mean and standard deviation</li>
        <li>Use z-scores to compare values across different scales</li>
        <li>Know when standardization is helpful and when it is misleading</li>
        <li>Prepare for Reporting & Practical Integration (Block 7)</li>
      </ul>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Next block</div>
        <div class="mini-body">
          Continue to <a href="/descriptive/reporting/" style="color:#1a73e8; text-decoration:underline;"><strong>Block 7 — Reporting & Practical Integration</strong></a>.
        </div>
      </div>
    </div>
  </div>
</section>

<script>
  (function () {
    var KEY = "esa_continue_descriptive_shape_lesson_v0";
    var raw = localStorage.getItem(KEY);
    if (!raw) return;

    try {
      var data = JSON.parse(raw);
      if (!data || !data.url || !data.label) return;

      var wrap = document.getElementById("continue-reading-block6");
      var label = document.getElementById("continue-reading-block6-label");
      var btn = document.getElementById("continue-reading-block6-btn");
      if (!wrap || !label || !btn) return;

      label.innerHTML = 'You last visited: <strong>' + data.label + '</strong>';
      btn.href = data.url;
      wrap.style.display = "block";
    } catch (e) {}
  })();
</script>