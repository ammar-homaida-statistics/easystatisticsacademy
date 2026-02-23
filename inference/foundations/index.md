<!-- =========================================================
BLOCK 1 — INFERENCE FOUNDATIONS
File: /inference/foundations/index.md
========================================================= -->
---
layout: default
title: Block 1 — Inference Foundations
description: Build the core logic of inference: parameters vs statistics, estimators, sampling variability, and standard error as the unit of uncertainty.
permalink: /inference/foundations/
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
        This block builds the foundation of statistical inference: what we estimate, why estimates vary,
        and how uncertainty is quantified using sampling distributions and standard errors.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update "last visited block" -->
<script>
  (function () {
    var KEY = "esa_continue_inference_last_block_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/foundations/",
      label: "Block 1 — Inference Foundations",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card hero-split">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 1</span>
        <span class="badge">Estimation</span>
        <span class="badge">Uncertainty</span>
        <span class="badge">Standard error</span>
      </div>

      <h1>Block 1 — Inference Foundations</h1>
      <p class="lead">
        Inference is the logic of reasoning from a sample to a population under uncertainty.
        This block defines the key objects (parameters, statistics, estimators) and explains
        why estimates vary across samples—introducing standard error as the uncertainty scale.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/">Back to Statistical Inference</a>
        <a class="btn" href="#lessons">Open structure</a>
      </div>

      <p class="muted-mini">
        Version 0: structure is locked. Content will expand without changing URLs or order.
      </p>
    </div>

    <div class="hero-panel">
      <div class="panel-card">
        <h2 class="panel-title">What this block covers</h2>
        <ul class="quickstart" style="list-style:none; padding-left:0; margin:0;">
          <li style="margin:.35rem 0;"><strong>Parameter vs statistic</strong><span class="meta">Target vs observed quantity</span></li>
          <li style="margin:.35rem 0;"><strong>Estimator</strong><span class="meta">Rule that maps data → estimate</span></li>
          <li style="margin:.35rem 0;"><strong>Sampling variability</strong><span class="meta">Why estimates change across samples</span></li>
          <li style="margin:.35rem 0;"><strong>Standard error</strong><span class="meta">Uncertainty scale of estimators</span></li>
          <li style="margin:.35rem 0;"><strong>Bias/variance intuition</strong><span class="meta">Accuracy vs stability</span></li>
          <li style="margin:.35rem 0;"><strong>Inference pipeline</strong><span class="meta">Estimator → SE → CI/test</span></li>
        </ul>
      </div>
    </div>
  </div>
</section>

<!-- ✅ Continue Reading (lesson-level placeholder key for this block) -->
<section class="section" id="continue-reading-block1" style="display:none;">
  <div class="callout">
    <div class="callout-copy">
      <h2>Continue reading</h2>
      <p class="muted-mini" id="continue-reading-block1-label" style="margin:0 0 .75rem 0;"></p>
      <a class="btn" id="continue-reading-block1-btn" href="#">Continue</a>
    </div>
  </div>
</section>

<section class="section" id="lessons">
  <div class="section-head">
    <h2>Lessons (Version 0)</h2>
    <p>
      This block will be expanded lesson-by-lesson. Lessons are published in order to keep the inference toolkit coherent.
      The list below is the permanent structure for this block.
    </p>
  </div>

  <div class="grid grid-2">

    <!-- Lesson 1 -->
    <div class="card lesson-card">
      <h3>1. What Is Statistical Inference?</h3>
      <p>Inference as reasoning under uncertainty: why we generalize from samples and what “uncertainty” means.</p>
      <div class="pill-row"><span class="badge">Coming soon</span></div>
    </div>

    <!-- Lesson 2 -->
    <div class="card lesson-card">
      <h3>2. Populations, Parameters, and the Target of Estimation</h3>
      <p>What a parameter is, why it is fixed (not random), and what “unknown” really means.</p>
      <div class="pill-row"><span class="badge">Coming soon</span></div>
    </div>

    <!-- Lesson 3 -->
    <div class="card lesson-card">
      <h3>3. Statistics as Random Variables</h3>
      <p>Why statistics have distributions: repeated sampling logic and the core idea behind standard error.</p>
      <div class="pill-row"><span class="badge">Coming soon</span></div>
    </div>

    <!-- Lesson 4 -->
    <div class="card lesson-card">
      <h3>4. Estimators vs Estimates</h3>
      <p>Distinguish the rule (estimator) from the realized number (estimate), and why the distinction matters.</p>
      <div class="pill-row"><span class="badge">Coming soon</span></div>
    </div>

    <!-- Lesson 5 -->
    <div class="card lesson-card">
      <h3>5. Sampling Distributions (Bridge From Probability)</h3>
      <p>Sampling distribution of the mean/proportion: where inference starts and why “n” stabilizes estimates.</p>
      <div class="pill-row"><span class="badge">Coming soon</span></div>
    </div>

    <!-- Lesson 6 -->
    <div class="card lesson-card">
      <h3>6. Standard Error: The Unit of Uncertainty</h3>
      <p>What SE measures, how it differs from SD, and why it scales with sample size.</p>
      <div class="pill-row"><span class="badge">Coming soon</span></div>
    </div>

    <!-- Lesson 7 -->
    <div class="card lesson-card">
      <h3>7. Standard Deviation vs Standard Error (Common Confusion)</h3>
      <p>Two different ideas: variability in data vs variability of an estimator; when each is used.</p>
      <div class="pill-row"><span class="badge">Coming soon</span></div>
    </div>

    <!-- Lesson 8 -->
    <div class="card lesson-card">
      <h3>8. Bias and Variance (Intuition First)</h3>
      <p>Accuracy vs stability: bias, variance, and why tradeoffs appear in real estimation problems.</p>
      <div class="pill-row"><span class="badge">Coming soon</span></div>
    </div>

    <!-- Lesson 9 -->
    <div class="card lesson-card">
      <h3>9. What Makes a “Good” Estimator?</h3>
      <p>Unbiasedness, consistency, efficiency (high-level), and what we actually care about in practice.</p>
      <div class="pill-row"><span class="badge">Coming soon</span></div>
    </div>

    <!-- Lesson 10 -->
    <div class="card lesson-card">
      <h3>10. The Estimator → SE → CI/Test Pipeline</h3>
      <p>The inference workflow: estimate a parameter, quantify uncertainty, then form intervals or decisions.</p>
      <div class="pill-row"><span class="badge">Coming soon</span></div>
    </div>

    <!-- Lesson 11 -->
    <div class="card lesson-card">
      <h3>11. Point Estimation vs Interval Estimation</h3>
      <p>Why a single number is incomplete, and why intervals are the natural output of inference.</p>
      <div class="pill-row"><span class="badge">Coming soon</span></div>
    </div>

    <!-- Lesson 12 -->
    <div class="card lesson-card">
      <h3>12. Confidence Level and Significance Level (Preview)</h3>
      <p>High-level meaning of 95% confidence and \(\alpha\): what these control and what they do not.</p>
      <div class="pill-row"><span class="badge">Coming soon</span></div>
    </div>

    <!-- Lesson 13 -->
    <div class="card lesson-card">
      <h3>13. Independence and Random Sampling (Why Inference Works)</h3>
      <p>The role of random sampling/assignment, dependence, and why design matters more than formulas.</p>
      <div class="pill-row"><span class="badge">Coming soon</span></div>
    </div>

    <!-- Lesson 14 -->
    <div class="card lesson-card">
      <h3>14. Sampling Bias vs Statistical Bias</h3>
      <p>Two different “bias” words: biased samples vs biased estimators; why confusing them ruins conclusions.</p>
      <div class="pill-row"><span class="badge">Coming soon</span></div>
    </div>

    <!-- Lesson 15 -->
    <div class="card lesson-card">
      <h3>15. Practical Inference Thinking: What Can We Claim?</h3>
      <p>Scope of generalization, uncertainty language, and avoiding over-claims (a bridge to reporting).</p>
      <div class="pill-row"><span class="badge">Coming soon</span></div>
    </div>

    <!-- Lesson 16 -->
    <div class="card lesson-card">
      <h3>16. Software Examples Later</h3>
      <p>SPSS / R / Python / Excel workflows will be added after the conceptual core is stable.</p>
      <div class="pill-row"><span class="badge">Planned</span></div>
    </div>

  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of Block 1</h2>
      <ul class="bullets">
        <li>Define parameters, statistics, and estimators precisely</li>
        <li>Explain why estimates vary across samples</li>
        <li>Interpret standard error as the uncertainty unit</li>
        <li>Describe the estimator → SE → CI/test pipeline</li>
      </ul>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Next block</div>
        <div class="mini-body">
          Continue to
          <a href="/inference/confidence-intervals/" style="color:#1a73e8; text-decoration:underline;">
            <strong>Block 2 — Confidence Intervals</strong>
          </a>.
        </div>
      </div>
    </div>

  </div>
</section>

<!-- ✅ Continue Reading Script (lesson-level) -->
<script>
  (function () {
    var KEY = "esa_continue_inference_foundations_lesson_v0";
    var raw = localStorage.getItem(KEY);
    if (!raw) return;

    try {
      var data = JSON.parse(raw);
      if (!data || !data.url || !data.label) return;

      var wrap = document.getElementById("continue-reading-block1");
      var label = document.getElementById("continue-reading-block1-label");
      var btn = document.getElementById("continue-reading-block1-btn");
      if (!wrap || !label || !btn) return;

      label.innerHTML = 'You last visited: <strong>' + data.label + '</strong>';
      btn.href = data.url;
      wrap.style.display = "block";
    } catch (e) {}
  })();
</script>