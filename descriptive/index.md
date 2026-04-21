---
layout: default
title: Descriptive Statistics
description: Summarize and explore data correctly using tables, plots, and clear numerical summaries.
permalink: /descriptive/
sidebar: false
---

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card hero-split">

    <div class="hero-copy">

      <div class="badge-row">
        <span class="badge">Descriptive</span>
        <span class="badge">EDA</span>
        <span class="badge">Visualization</span>
        <span class="badge">Summaries</span>
      </div>

      <h1>Descriptive Statistics</h1>

      <p class="lead">
        Learn how to summarize and explore data correctly using tables, graphs, and numerical measures —
        without misleading interpretation.
      </p>

      <p class="muted-mini">
        7 structured blocks • Concept-first • Built on Foundations
      </p>

      <div class="hero-actions">
        <a class="btn" href="#blocks">Start Learning</a>
        <a class="btn btn-outline" href="/probability/">Next: Probability</a>
      </div>

      <div style="background:#fff3cd; border:1px solid #ffeeba; padding:12px 14px; margin:14px 0; border-radius:8px;">
        <strong>🚧 Under Construction</strong> — This unit is being developed block-by-block
        with detailed explanations, examples, and software applications.
      </div>

    </div>

    <div class="hero-panel">
      <div class="panel-card">

        <h2 class="panel-title">Suggested learning order</h2>

        <ol class="quickstart">
          <li>Data & Variables</li>
          <li>Tables</li>
          <li>Visualization</li>
          <li>Center</li>
          <li>Spread</li>
          <li>Shape</li>
          <li>Reporting</li>
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
      This unit is organized into seven blocks. Follow them in order —
      each block builds on the previous one.
    </p>
  </div>

  <!-- CONTINUE READING -->
  <div id="continue-reading-descriptive" style="display:none; margin-bottom:20px;">
    <div class="callout">
      <div class="callout-copy">
        <h2>Continue reading</h2>
        <p id="continue-reading-descriptive-label" class="muted-mini"></p>
        <a class="btn" id="continue-reading-descriptive-btn" href="#">Continue</a>
      </div>
    </div>
  </div>

  <div class="grid grid-2">

    <!-- BLOCK 1 -->
    <div class="card lesson-card">
      <h3><a href="/descriptive/data-variables/">Block 1 — Data & Variables</a></h3>
      <p>Define variables, data types, structure, and measurement rules.</p>
      <a class="btn btn-outline" href="/descriptive/data-variables/">Open block</a>
    </div>

    <!-- BLOCK 2 -->
    <div class="card lesson-card">
      <h3><a href="/descriptive/tabular-summaries/">Block 2 — Tabular Summaries</a></h3>
      <p>Frequency tables, grouped data, and contingency tables.</p>
      <a class="btn btn-outline" href="/descriptive/tabular-summaries/">Open block</a>
    </div>

    <!-- BLOCK 3 -->
    <div class="card lesson-card">
      <h3><a href="/descriptive/visualization/">Block 3 — Visualization</a></h3>
      <p>Histograms, boxplots, scatterplots, and honest graphics.</p>
      <a class="btn btn-outline" href="/descriptive/visualization/">Open block</a>
    </div>

    <!-- BLOCK 4 -->
    <div class="card lesson-card">
      <h3><a href="/descriptive/center/">Block 4 — Measures of Center</a></h3>
      <p>Mean, median, mode, and when each is appropriate.</p>
      <a class="btn btn-outline" href="/descriptive/center/">Open block</a>
    </div>

    <!-- BLOCK 5 -->
    <div class="card lesson-card">
      <h3><a href="/descriptive/spread/">Block 5 — Measures of Spread</a></h3>
      <p>Variance, standard deviation, IQR, and variability concepts.</p>
      <a class="btn btn-outline" href="/descriptive/spread/">Open block</a>
    </div>

    <!-- BLOCK 6 -->
    <div class="card lesson-card">
      <h3><a href="/descriptive/shape/">Block 6 — Distribution Shape</a></h3>
      <p>Skewness, normality, and standardization.</p>
      <a class="btn btn-outline" href="/descriptive/shape/">Open block</a>
    </div>

    <!-- BLOCK 7 -->
    <div class="card lesson-card">
      <h3><a href="/descriptive/reporting/">Block 7 — Reporting</a></h3>
      <p>Interpret and communicate results correctly.</p>
      <a class="btn btn-outline" href="/descriptive/reporting/">Open block</a>
    </div>

  </div>
</section>

<!-- GOAL -->
<section class="section section-slim">
  <div class="callout">

    <div class="callout-copy">
      <h2>Goal of this unit</h2>
      <ul class="bullets">
        <li>Summarize data clearly and correctly</li>
        <li>Match methods to data type</li>
        <li>Avoid misleading interpretations</li>
        <li>Prepare for probability and inference</li>
      </ul>
    </div>

    <div class="callout-side">
      <div class="mini">
        <div class="mini-title">Next</div>
        <div class="mini-body">
          Continue to <strong>Probability</strong>
        </div>
      </div>
      <div class="mini">
        <div class="mini-title">Note</div>
        <div class="mini-body">
          Built progressively block-by-block
        </div>
      </div>
    </div>

  </div>
</section>

<!-- CONTINUE READING SCRIPT -->
<script>
(function () {
  try {
    const KEY = "esa_continue_descriptive_last_block_v0";
    const raw = localStorage.getItem(KEY);
    if (!raw) return;

    const data = JSON.parse(raw);
    if (!data || !data.url || !data.label) return;

    const wrap = document.getElementById("continue-reading-descriptive");
    const label = document.getElementById("continue-reading-descriptive-label");
    const btn = document.getElementById("continue-reading-descriptive-btn");

    if (!wrap || !label || !btn) return;

    label.innerHTML = "You last visited: <strong>" + data.label + "</strong>";
    btn.href = data.url;
    wrap.style.display = "block";

  } catch (e) {}
})();
</script>