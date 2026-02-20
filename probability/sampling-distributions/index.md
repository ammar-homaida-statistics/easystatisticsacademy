---
layout: default
title: Block 7 — Sampling Distributions
description: Understand sampling distributions and why statistics have distributions: the sample mean, sample variance, z/t statistics, chi-square and F families, and the foundation of estimation and inference.
permalink: /probability/sampling-distributions/
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
        This block introduces <strong>sampling distributions</strong> — the probability distributions of statistics
        (like \(\overline{X}\), \(S^2\), and test statistics).
        These ideas turn probability theory into practical inference tools: estimation, confidence intervals, and hypothesis tests.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update "last visited block" -->
<script>
  (function () {
    var KEY = "esa_continue_probability_last_block_v0";

    localStorage.setItem(KEY, JSON.stringify({
      url: "/probability/sampling-distributions/",
      label: "Block 7 — Sampling Distributions",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card hero-split">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 7</span>
        <span class="badge">Sampling</span>
        <span class="badge">Estimation</span>
        <span class="badge">Inference</span>
      </div>

      <h1>Block 7 — Sampling Distributions</h1>
      <p class="lead">
        A statistic is a random variable.  
        This block explains how and why statistics have distributions, how standard errors appear,
        and where the famous families (<strong>t</strong>, <strong>\(\chi^2\)</strong>, <strong>F</strong>) come from.
        This is the bridge from probability results (LLN/CLT) to formal inference procedures.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/probability/">Back to Probability</a>
        <a class="btn" href="#lessons">Open lessons</a>
      </div>

      <p class="muted-mini">
        Version 0: structure is locked. Lessons will be refined without changing order.
      </p>
    </div>

    <div class="hero-panel">
      <div class="panel-card">
        <h2 class="panel-title">What this block covers</h2>
        <ul class="quickstart" style="list-style:none; padding-left:0; margin:0;">
          <li style="margin:.35rem 0;"><strong>Sampling distribution</strong><span class="meta">Distribution of a statistic</span></li>
          <li style="margin:.35rem 0;"><strong>Standard error</strong><span class="meta">Uncertainty scale of estimators</span></li>
          <li style="margin:.35rem 0;"><strong>z vs t</strong><span class="meta">Known vs unknown \(\sigma\)</span></li>
          <li style="margin:.35rem 0;"><strong>\(\chi^2\) and variance</strong><span class="meta">Where variance inference comes from</span></li>
          <li style="margin:.35rem 0;"><strong>F and ratios</strong><span class="meta">Comparing variances; ANOVA preview</span></li>
          <li style="margin:.35rem 0;"><strong>Practical pipeline</strong><span class="meta">Estimator → SE → CI/test</span></li>
        </ul>
      </div>
    </div>
  </div>
</section>

<!-- ✅ Continue Reading -->
<section class="section" id="continue-reading-block7" style="display:none;">
  <div class="callout">
    <div class="callout-copy">
      <h2>Continue reading</h2>
      <p class="muted-mini" id="continue-reading-block7-label" style="margin:0 0 .75rem 0;"></p>
      <a class="btn" id="continue-reading-block7-btn" href="#">Continue</a>
    </div>
  </div>
</section>

<section class="section" id="lessons">
  <div class="section-head">
    <h2>Lessons (Version 0)</h2>
    <p>
      Follow the order carefully. Each lesson builds the formal inference toolkit:
      sampling distributions → standardization → t/\(\chi^2\)/F families → confidence intervals and tests.
    </p>
  </div>

  <div class="grid grid-2">

    <!-- Lesson 1 -->
    <div class="card lesson-card">
      <h3><a href="/probability/sampling-distributions/what-is-a-sampling-distribution/">1. What Is a Sampling Distribution?</a></h3>
      <p>Statistics are random variables: repeated sampling, variability, and the meaning of “distribution of a statistic”.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/probability/sampling-distributions/what-is-a-sampling-distribution/">Open lesson</a>
      </div>
    </div>

    <!-- Lesson 2 -->
    <div class="card lesson-card">
      <h3><a href="/probability/sampling-distributions/standard-error-and-estimators/">2. Standard Error & Estimators</a></h3>
      <p>Bias vs variance, consistency, and why standard error is the uncertainty unit of estimation.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/probability/sampling-distributions/standard-error-and-estimators/">Open lesson</a>
      </div>
    </div>

    <!-- Lesson 3 -->
    <div class="card lesson-card">
      <h3><a href="/probability/sampling-distributions/z-statistic-and-ci/">3. z-Statistic & Confidence Intervals</a></h3>
      <p>When \(\sigma\) is known: standardization, z-scores, and building confidence intervals from Normal logic.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/probability/sampling-distributions/z-statistic-and-ci/">Open lesson</a>
      </div>
    </div>

    <!-- Lesson 4 -->
    <div class="card lesson-card">
      <h3><a href="/probability/sampling-distributions/t-distribution-and-t-test/">4. t-Distribution & the t-Statistic</a></h3>
      <p>When \(\sigma\) is unknown: Student’s t, degrees of freedom, and why t replaces z in practice.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/probability/sampling-distributions/t-distribution-and-t-test/">Open lesson</a>
      </div>
    </div>

    <!-- Lesson 5 -->
    <div class="card lesson-card">
      <h3><a href="/probability/sampling-distributions/chi-square-and-variance/">5. Chi-Square Distribution & Variance Inference</a></h3>
      <p>Distribution of scaled sample variance; confidence intervals and tests for \(\sigma^2\).</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/probability/sampling-distributions/chi-square-and-variance/">Open lesson</a>
      </div>
    </div>

    <!-- Lesson 6 -->
    <div class="card lesson-card">
      <h3><a href="/probability/sampling-distributions/f-distribution-and-anova-preview/">6. F Distribution & ANOVA Preview</a></h3>
      <p>Ratios of variances; comparing spread; how this leads to ANOVA and regression testing later.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/probability/sampling-distributions/f-distribution-and-anova-preview/">Open lesson</a>
      </div>
    </div>

  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of Block 7</h2>
      <ul class="bullets">
        <li>Explain what a sampling distribution is and why it matters</li>
        <li>Use standard error as the uncertainty scale of estimators</li>
        <li>Build confidence intervals using z and t logic</li>
        <li>Understand \(\chi^2\) for variance inference</li>
        <li>Understand F as a ratio distribution (ANOVA/regression preview)</li>
      </ul>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Next block</div>
        <div class="mini-body">
          Continue to
          <a href="/inference/" style="color:#1a73e8; text-decoration:underline;">
            <strong>Next block — Statistical Inference</strong>
          </a>.
        </div>
      </div>
    </div>

  </div>
</section>

<!-- ✅ Continue Reading Script -->
<script>
  (function () {
    var KEY = "esa_continue_probability_sampling_distributions_lesson_v0";

    var raw = localStorage.getItem(KEY);
    if (!raw) return;

    try {
      var data = JSON.parse(raw);
      if (!data || !data.url || !data.label) return;

      var wrap = document.getElementById("continue-reading-block7");
      var label = document.getElementById("continue-reading-block7-label");
      var btn = document.getElementById("continue-reading-block7-btn");
      if (!wrap || !label || !btn) return;

      label.innerHTML = 'You last visited: <strong>' + data.label + '</strong>';
      btn.href = data.url;
      wrap.style.display = "block";
    } catch (e) {}
  })();
</script>