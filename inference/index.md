---
layout: default
title: Statistical Inference
description: Learn inference correctly: sampling distributions, estimation, confidence intervals, hypothesis tests, p-values, power, and interpretation.
permalink: /inference/
sidebar: false
---

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card hero-split">

    <div class="hero-copy">

      <div class="badge-row">
        <span class="badge">Uncertainty</span>
        <span class="badge">Estimation</span>
        <span class="badge">Testing</span>
        <span class="badge">Interpretation</span>
      </div>

      <h1>Statistical Inference</h1>

      <p class="lead">
        Learn how we move from sample data to population conclusions — using estimation,
        confidence intervals, and hypothesis testing with correct interpretation.
      </p>

      <p class="muted-mini">
        7 structured blocks • Concept-first • Built on probability
      </p>

      <div class="hero-actions">
        <a class="btn" href="#blocks">Start Learning</a>
        <a class="btn btn-outline" href="/modeling/">Next: Modeling</a>
      </div>

      <div style="background:#fff3cd; border:1px solid #ffeeba; padding:12px 14px; margin:14px 0; border-radius:8px;">
        <strong>🚧 Under Construction</strong> — This unit is being developed block-by-block
        with strong emphasis on correct interpretation and avoiding common misconceptions.
      </div>

    </div>

    <div class="hero-panel">
      <div class="panel-card">

        <h2 class="panel-title">Suggested learning order</h2>

        <ol class="quickstart">
          <li>Inference foundations</li>
          <li>Confidence intervals</li>
          <li>Hypothesis testing</li>
          <li>Classical tests</li>
          <li>Power & sample size</li>
          <li>Interpretation</li>
          <li>Assumptions & robustness</li>
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
      Follow the blocks in order. Each block builds your ability to make valid conclusions
      from data under uncertainty.
    </p>
  </div>

  <!-- CONTINUE READING -->
  <div id="continue-reading-inference" style="display:none; margin-bottom:20px;">
    <div class="callout">
      <div class="callout-copy">
        <h2>Continue reading</h2>
        <p id="continue-reading-inference-label" class="muted-mini"></p>
        <a class="btn" id="continue-reading-inference-btn" href="#">Continue</a>
      </div>
    </div>
  </div>

  <div class="grid grid-2">

    <!-- BLOCK 1 -->
    <div class="card lesson-card">
      <h3><a href="/inference/foundations/">Block 1 — Inference Foundations</a></h3>
      <p>Parameters, estimators, standard error, and uncertainty.</p>
      <a class="btn btn-outline" href="/inference/foundations/">Open block</a>
    </div>

    <!-- BLOCK 2 -->
    <div class="card lesson-card">
      <h3><a href="/inference/confidence-intervals/">Block 2 — Confidence Intervals</a></h3>
      <p>Meaning, construction, and correct interpretation.</p>
      <a class="btn btn-outline" href="/inference/confidence-intervals/">Open block</a>
    </div>

    <!-- BLOCK 3 -->
    <div class="card lesson-card">
      <h3><a href="/inference/hypothesis-testing/">Block 3 — Hypothesis Testing</a></h3>
      <p>Null hypothesis, errors, p-values, and decisions.</p>
      <a class="btn btn-outline" href="/inference/hypothesis-testing/">Open block</a>
    </div>

    <!-- BLOCK 4 -->
    <div class="card lesson-card">
      <h3><a href="/inference/classical-tests/">Block 4 — Classical Tests</a></h3>
      <p>t-tests, proportion tests, and chi-square methods.</p>
      <a class="btn btn-outline" href="/inference/classical-tests/">Open block</a>
    </div>

    <!-- BLOCK 5 -->
    <div class="card lesson-card">
      <h3><a href="/inference/power-sample-size/">Block 5 — Power & Sample Size</a></h3>
      <p>Design thinking, effect size, and statistical power.</p>
      <a class="btn btn-outline" href="/inference/power-sample-size/">Open block</a>
    </div>

    <!-- BLOCK 6 -->
    <div class="card lesson-card">
      <h3><a href="/inference/interpretation-reporting/">Block 6 — Interpretation & Reporting</a></h3>
      <p>Effect sizes, evidence, and correct conclusions.</p>
      <a class="btn btn-outline" href="/inference/interpretation-reporting/">Open block</a>
    </div>

    <!-- BLOCK 7 -->
    <div class="card lesson-card">
      <h3><a href="/inference/assumptions-robustness/">Block 7 — Assumptions & Robustness</a></h3>
      <p>When methods fail and how to respond correctly.</p>
      <a class="btn btn-outline" href="/inference/assumptions-robustness/">Open block</a>
    </div>

  </div>
</section>

<!-- GOAL -->
<section class="section section-slim">
  <div class="callout">

    <div class="callout-copy">
      <h2>Goal of this unit</h2>
      <ul class="bullets">
        <li>Understand inference as reasoning under uncertainty</li>
        <li>Interpret confidence intervals and p-values correctly</li>
        <li>Avoid common statistical misconceptions</li>
        <li>Prepare for modeling and applied analysis</li>
      </ul>
    </div>

    <div class="callout-side">
      <div class="mini">
        <div class="mini-title">Next</div>
        <div class="mini-body">
          Continue to <strong>Statistical Modeling</strong>
        </div>
      </div>
      <div class="mini">
        <div class="mini-title">Note</div>
        <div class="mini-body">
          Focus on interpretation, not mechanical procedures
        </div>
      </div>
    </div>

  </div>
</section>

<!-- CONTINUE READING SCRIPT -->
<script>
(function () {
  try {
    const KEY = "esa_continue_inference_last_block_v0";
    const raw = localStorage.getItem(KEY);
    if (!raw) return;

    const data = JSON.parse(raw);
    if (!data || !data.url || !data.label) return;

    const wrap = document.getElementById("continue-reading-inference");
    const label = document.getElementById("continue-reading-inference-label");
    const btn = document.getElementById("continue-reading-inference-btn");

    if (!wrap || !label || !btn) return;

    label.innerHTML = "You last visited: <strong>" + data.label + "</strong>";
    btn.href = data.url;
    wrap.style.display = "block";

  } catch (e) {}
})();
</script>