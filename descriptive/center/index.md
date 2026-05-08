---
layout: default
title: Block 4 — Measures of Center
description: Learn how to describe typical values correctly using mean, median, mode, weighted means, and robust measures of center.
permalink: /descriptive/center/
sidebar: false
---

<!-- SAVE LAST VISITED BLOCK -->
<script>
(function () {

  const KEY = "esa_continue_descriptive_last_block_v0";

  localStorage.setItem(KEY, JSON.stringify({
    url: "/descriptive/center/",
    label: "Block 4 — Measures of Center",
    ts: Date.now()
  }));

})();
</script>

<!-- HERO -->
<section class="hero hero-section">

  <div class="hero-card hero-split">

    <!-- LEFT -->
    <div class="hero-copy">

      <div class="badge-row">
        <span class="badge">Block 4</span>
        <span class="badge">Mean</span>
        <span class="badge">Median</span>
        <span class="badge">Robustness</span>
        <span class="badge">Interpretation</span>
      </div>

      <h1>Block 4 — Measures of Center</h1>

      <p class="lead">
        Measures of center attempt to describe a “typical” value in a dataset.
      </p>

      <p class="lead">
        This block teaches how to choose and interpret the correct measure of center:
        mean, median, mode, weighted mean, trimmed mean, and robust alternatives —
        while understanding how skewness and outliers change interpretation.
      </p>

      <div class="hero-actions">

        <a class="btn" href="#lessons">
          Start block
        </a>

        <a class="btn btn-outline" href="/descriptive/">
          Descriptive home
        </a>

      </div>

      <!-- BLOCK HIGHLIGHT -->
      <div class="hero-highlight">

        <div class="hero-highlight-icon">
          📍
        </div>

        <div>

          <strong>Why this block matters</strong>

          <p>
            “Average” is one of the most misunderstood ideas in statistics.
            Different measures of center can tell completely different stories
            about the same data.
          </p>

        </div>

      </div>

    </div>

    <!-- RIGHT -->
    <div class="hero-panel">

      <div class="panel-card">

        <h2 class="panel-title">
          What this block covers
        </h2>

        <ul class="block-summary-list">

          <li>
            Meaning of “center”
          </li>

          <li>
            Mean, median, and mode
          </li>

          <li>
            Skewness and outlier effects
          </li>

          <li>
            Weighted and trimmed means
          </li>

          <li>
            Winsorized means
          </li>

          <li>
            Center for ordinal variables
          </li>

          <li>
            Correct reporting and interpretation
          </li>

        </ul>

        <div class="panel-divider"></div>

        <div class="mini-progress">

          <div class="mini-progress-label">
            Core skill
          </div>

          <div class="mini-progress-text">
            Selecting and interpreting the correct “typical value” for data.
          </div>

          <div class="mini-progress-bar">
            <span style="width:56%;"></span>
          </div>

          <div class="mini-progress-text">
            Block 4 of 7 in Descriptive Statistics
          </div>

        </div>

      </div>

    </div>

  </div>

</section>

<!-- CONTINUE READING -->
<section class="section"
         id="continue-reading-block4"
         style="display:none;">

  <div class="callout">

    <div class="callout-copy">

      <h2>Continue reading</h2>

      <p class="muted-mini"
         id="continue-reading-block4-label"
         style="margin:0 0 .75rem 0;">
      </p>

      <a class="btn"
         id="continue-reading-block4-btn"
         href="#">
         Continue
      </a>

    </div>

  </div>

</section>

<!-- LESSONS -->
<section class="section" id="lessons">

  <div class="section-head">

    <h2>Lessons</h2>

    <p>
      Work through these lessons in order.
      Each lesson builds intuition for selecting and interpreting center responsibly.
    </p>

  </div>

  <div class="grid grid-2">

    <!-- LESSON 1 -->
    <div class="card lesson-card lesson-block-card">

      <div class="lesson-block-number">01</div>

      <h3>
        <a href="/descriptive/center/what-is-center/">
          What Is “Center” and Why “Average” Can Mislead
        </a>
      </h3>

      <p>
        Learn what statisticians mean by “typical value”
        and why “average” is often used incorrectly.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Foundations</span>
        <span class="pill">Interpretation</span>
      </div>

      <a class="btn btn-outline"
         href="/descriptive/center/what-is-center/">
         Open lesson
      </a>

    </div>

    <!-- LESSON 2 -->
    <div class="card lesson-card lesson-block-card">

      <div class="lesson-block-number">02</div>

      <h3>
        <a href="/descriptive/center/arithmetic-mean/">
          Arithmetic Mean (When It Works — When It Fails)
        </a>
      </h3>

      <p>
        Understand the arithmetic mean,
        its interpretation, and its sensitivity to outliers.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Mean</span>
        <span class="pill">Outliers</span>
      </div>

      <a class="btn btn-outline"
         href="/descriptive/center/arithmetic-mean/">
         Open lesson
      </a>

    </div>

    <!-- LESSON 3 -->
    <div class="card lesson-card lesson-block-card">

      <div class="lesson-block-number">03</div>

      <h3>
        <a href="/descriptive/center/median/">
          Median (Robust Center for Skewed Data)
        </a>
      </h3>

      <p>
        Learn why the median resists outliers
        and becomes preferable for skewed distributions.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Median</span>
        <span class="pill">Robustness</span>
      </div>

      <a class="btn btn-outline"
         href="/descriptive/center/median/">
         Open lesson
      </a>

    </div>

    <!-- LESSON 4 -->
    <div class="card lesson-card lesson-block-card">

      <div class="lesson-block-number">04</div>

      <h3>
        <a href="/descriptive/center/mode/">
          Mode (Most Frequent Value)
        </a>
      </h3>

      <p>
        Use the mode for categorical and discrete data,
        and understand multimodal distributions.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Mode</span>
        <span class="pill">Categorical data</span>
      </div>

      <a class="btn btn-outline"
         href="/descriptive/center/mode/">
         Open lesson
      </a>

    </div>

    <!-- LESSON 5 -->
    <div class="card lesson-card lesson-block-card">

      <div class="lesson-block-number">05</div>

      <h3>
        <a href="/descriptive/center/mean-vs-median/">
          Mean vs Median (Decision Rules)
        </a>
      </h3>

      <p>
        Learn how skewness and outliers determine
        whether mean or median is more appropriate.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Decision rules</span>
        <span class="pill">Skewness</span>
      </div>

      <a class="btn btn-outline"
         href="/descriptive/center/mean-vs-median/">
         Open lesson
      </a>

    </div>

    <!-- LESSON 6 -->
    <div class="card lesson-card lesson-block-card">

      <div class="lesson-block-number">06</div>

      <h3>
        <a href="/descriptive/center/weighted-mean/">
          Weighted Mean
        </a>
      </h3>

      <p>
        Understand weighted averages:
        survey weights, GPA calculations, and aggregated summaries.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Weights</span>
        <span class="pill">Applications</span>
      </div>

      <a class="btn btn-outline"
         href="/descriptive/center/weighted-mean/">
         Open lesson
      </a>

    </div>

    <!-- LESSON 7 -->
    <div class="card lesson-card lesson-block-card">

      <div class="lesson-block-number">07</div>

      <h3>
        <a href="/descriptive/center/trimmed-mean/">
          Trimmed Mean
        </a>
      </h3>

      <p>
        Remove extreme observations to stabilize the mean
        while preserving most of the data.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Robust statistics</span>
        <span class="pill">Trimmed mean</span>
      </div>

      <a class="btn btn-outline"
         href="/descriptive/center/trimmed-mean/">
         Open lesson
      </a>

    </div>

    <!-- LESSON 8 -->
    <div class="card lesson-card lesson-block-card">

      <div class="lesson-block-number">08</div>

      <h3>
        <a href="/descriptive/center/winsorized-mean/">
          Winsorized Mean
        </a>
      </h3>

      <p>
        Learn how winsorization reduces outlier influence
        without deleting observations entirely.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Winsorization</span>
        <span class="pill">Outlier control</span>
      </div>

      <a class="btn btn-outline"
         href="/descriptive/center/winsorized-mean/">
         Open lesson
      </a>

    </div>

    <!-- LESSON 9 -->
    <div class="card lesson-card lesson-block-card">

      <div class="lesson-block-number">09</div>

      <h3>
        <a href="/descriptive/center/center-for-ordinal-data/">
          Center for Ordinal Data
        </a>
      </h3>

      <p>
        Understand why median and mode are valid for ordinal scales —
        while means can become misleading.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Ordinal data</span>
        <span class="pill">Measurement scales</span>
      </div>

      <a class="btn btn-outline"
         href="/descriptive/center/center-for-ordinal-data/">
         Open lesson
      </a>

    </div>

    <!-- LESSON 10 -->
    <div class="card lesson-card lesson-block-card">

      <div class="lesson-block-number">10</div>

      <h3>
        <a href="/descriptive/center/reporting-center-properly/">
          Reporting Center Properly
        </a>
      </h3>

      <p>
        Learn how to report measures of center with context,
        units, sample size, and correct interpretation.
      </p>

      <div class="lesson-card-tags">
        <span class="pill">Reporting</span>
        <span class="pill">Interpretation</span>
      </div>

      <a class="btn btn-outline"
         href="/descriptive/center/reporting-center-properly/">
         Open lesson
      </a>

    </div>

  </div>

</section>

<!-- OUTCOME -->
<section class="section section-slim">

  <div class="callout">

    <div class="callout-copy">

      <h2>Outcome of Block 4</h2>

      <ul class="bullets">

        <li>Select appropriate measures of center based on variable type</li>

        <li>Understand how skewness and outliers affect “average” values</li>

        <li>Use robust alternatives responsibly</li>

        <li>Interpret mean, median, and mode correctly</li>

        <li>Report center clearly with context and limitations</li>

      </ul>

    </div>

    <div class="callout-side">

      <div class="mini">

        <div class="mini-title">
          Next block
        </div>

        <div class="mini-body">

          Continue to

          <a href="/descriptive/spread/">
            <strong>Block 5 — Measures of Spread</strong>
          </a>

        </div>

      </div>

      <div class="mini">

        <div class="mini-title">
          Key principle
        </div>

        <div class="mini-body">
          There is no universally “best” average —
          the correct measure depends on the data structure.
        </div>

      </div>

    </div>

  </div>

</section>

<!-- CONTINUE READING -->
<script>
(function () {

  try {

    const KEY =
      "esa_continue_descriptive_center_lesson_v0";

    const raw = localStorage.getItem(KEY);

    if (!raw) return;

    const data = JSON.parse(raw);

    if (!data || !data.url || !data.label) return;

    const wrap =
      document.getElementById("continue-reading-block4");

    const label =
      document.getElementById("continue-reading-block4-label");

    const btn =
      document.getElementById("continue-reading-block4-btn");

    if (!wrap || !label || !btn) return;

    label.innerHTML =
      'You last visited: <strong>' + data.label + '</strong>';

    btn.href = data.url;

    wrap.style.display = "block";

  } catch (e) {}

})();
</script>
