---
layout: default
title: Block 4 — Measures of Center
description: Learn how to describe “typical values” correctly using mean, median, mode, weighted and trimmed means, and how distribution shape and outliers change interpretation.
permalink: /descriptive/center/
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
      url: "/descriptive/center/",
      label: "Block 4 — Measures of Center",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card hero-split">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 4</span>
        <span class="badge">Center</span>
        <span class="badge">Robustness</span>
        <span class="badge">Interpretation</span>
      </div>

      <h1>Block 4 — Measures of Center</h1>
      <p class="lead">
        Measures of center describe a “typical” value, but the correct choice depends on the variable type,
        distribution shape, and presence of outliers. This block teaches mean, median, mode, weighted and trimmed means,
        and how to report center responsibly.
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
            <strong>Meaning of “center”</strong><br>
            <span class="meta">Typical value vs average; when “average” is misleading</span>
          </li>
          <li style="margin-bottom:.6rem;">
            <strong>Mean, median, mode</strong><br>
            <span class="meta">Definitions, strengths, and correct use cases</span>
          </li>
          <li style="margin-bottom:.6rem;">
            <strong>Robust alternatives</strong><br>
            <span class="meta">Trimmed mean, winsorization, weighted mean</span>
          </li>
          <li>
            <strong>Reporting</strong><br>
            <span class="meta">Choosing the right center + short interpretation</span>
          </li>
        </ul>
      </div>
    </div>
  </div>
</section>

<!-- 🔁 Continue Reading (Block 4 lessons only) -->
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
      Work through these lessons in order. Each lesson page is active (even if still being developed),
      so you can navigate the full structure now.
    </p>
  </div>

  <div class="grid grid-2">

    <!-- 1 -->
    <div class="card lesson-card">
      <h3><a href="/descriptive/center/what-is-center/">1. What Is “Center” and Why “Average” Can Mislead</a></h3>
      <p>What we mean by “typical value”, and why the word “average” is often used incorrectly.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/descriptive/center/what-is-center/">Open lesson</a>
      </div>
    </div>

    <!-- 2 -->
    <div class="card lesson-card">
      <h3><a href="/descriptive/center/arithmetic-mean/">2. Arithmetic Mean (When It Works — When It Fails)</a></h3>
      <p>Mean definition and interpretation, sensitivity to outliers, and correct contexts for use.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/descriptive/center/arithmetic-mean/">Open lesson</a>
      </div>
    </div>

    <!-- 3 -->
    <div class="card lesson-card">
      <h3><a href="/descriptive/center/median/">3. Median (Robust Center for Skewed Data)</a></h3>
      <p>Why median resists outliers, how it behaves under skewness, and when it is preferred.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/descriptive/center/median/">Open lesson</a>
      </div>
    </div>

    <!-- 4 -->
    <div class="card lesson-card">
      <h3><a href="/descriptive/center/mode/">4. Mode (Most Frequent Value, Categorical “Center”)</a></h3>
      <p>Mode for categorical and discrete data, multiple modes, and interpretation limits.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/descriptive/center/mode/">Open lesson</a>
      </div>
    </div>

    <!-- 5 -->
    <div class="card lesson-card">
      <h3><a href="/descriptive/center/mean-vs-median/">5. Mean vs Median (Skewness, Outliers, and Choice Rules)</a></h3>
      <p>Decision rules for choosing mean or median using distribution shape and outlier behavior.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/descriptive/center/mean-vs-median/">Open lesson</a>
      </div>
    </div>

    <!-- 6 -->
    <div class="card lesson-card">
      <h3><a href="/descriptive/center/weighted-mean/">6. Weighted Mean (When Not All Observations Are Equal)</a></h3>
      <p>How weights change interpretation; survey weights, grades/credits, and aggregated averages.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/descriptive/center/weighted-mean/">Open lesson</a>
      </div>
    </div>

    <!-- 7 -->
    <div class="card lesson-card">
      <h3><a href="/descriptive/center/trimmed-mean/">7. Trimmed Mean (Robust Alternative to Mean)</a></h3>
      <p>Trim extremes to stabilize the mean; when trimming is justified and how to report it.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/descriptive/center/trimmed-mean/">Open lesson</a>
      </div>
    </div>

    <!-- 8 -->
    <div class="card lesson-card">
      <h3><a href="/descriptive/center/winsorized-mean/">8. Winsorized Mean (Outlier Control Without Deletion)</a></h3>
      <p>Replace extremes rather than remove them; why winsorization is used and its limitations.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/descriptive/center/winsorized-mean/">Open lesson</a>
      </div>
    </div>

    <!-- 9 -->
    <div class="card lesson-card">
      <h3><a href="/descriptive/center/center-for-ordinal-data/">9. Center for Ordinal Data (What Is Valid?)</a></h3>
      <p>Median and mode as valid summaries; why mean can be invalid for ordinal scales.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/descriptive/center/center-for-ordinal-data/">Open lesson</a>
      </div>
    </div>

    <!-- 10 -->
    <div class="card lesson-card">
      <h3><a href="/descriptive/center/reporting-center/">10. Reporting Center Properly (With Context)</a></h3>
      <p>How to write center in reports: include units, sample size, distribution context, and avoid overclaiming.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/descriptive/center/reporting-center/">Open lesson</a>
      </div>
    </div>

  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of Block 4</h2>
      <ul class="bullets">
        <li>Choose a valid measure of center based on variable type and scale</li>
        <li>Understand how skewness and outliers change the meaning of “average”</li>
        <li>Use robust alternatives (median, trimmed, winsorized) responsibly</li>
        <li>Report center clearly with correct interpretation and context</li>
        <li>Be ready for Measures of Spread (Block 5)</li>
      </ul>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Next block</div>
        <div class="mini-body">
          Continue to <a href="/descriptive/spread/" style="color:#1a73e8; text-decoration:underline;"><strong>Block 5 — Measures of Spread</strong></a>.
        </div>
      </div>
    </div>
  </div>
</section>

<script>
  (function () {
    // ✅ Unique key for Block 4 lessons only
    var KEY = "esa_continue_descriptive_center_lesson_v0";

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