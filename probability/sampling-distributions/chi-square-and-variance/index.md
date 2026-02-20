---
layout: default
title: "5. Chi-Square Distribution & Variance Inference"
description: "Chi-square as the distribution of scaled sample variance; confidence intervals and tests for σ² under Normal assumptions."
permalink: /probability/sampling-distributions/chi-square-and-variance/
sidebar: false
---

<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem; letter-spacing:0.5px;">🚧 Lesson Under Construction</h2>
      <p style="margin:0; font-size:1.05rem; color:#5d4037; line-height:1.6;">
        Version 0 introduces \(\chi^2\) and its role in variance inference. Visuals and worked variance-CI examples will be added later.
      </p>
    </div>
  </div>
</section>

<script>
  (function () {
    var KEY = "esa_continue_probability_sampling_distributions_lesson_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/probability/sampling-distributions/chi-square-and-variance/",
      label: "Lesson 5 — Chi-Square Distribution & Variance Inference",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 7</span>
        <span class="badge">Lesson 5</span>
        <span class="badge">χ²</span>
        <span class="badge">Variance</span>
      </div>

      <h1>5. Chi-Square Distribution &amp; Variance Inference</h1>
      <p class="lead">
        The \(\chi^2\) distribution appears when studying the variability of Normal data.
        It explains why the sample variance has a known distribution and how we build
        <strong>confidence intervals for \(\sigma^2\)</strong>.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/probability/sampling-distributions/">Back to Block 7</a>
        <a class="btn btn-outline" href="/probability/">Probability home</a>
      </div>

      <p class="muted-mini">
        Key message: scaled sample variance follows a \(\chi^2\) distribution under Normal assumptions.
      </p>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">
        Next, we study the <strong>F distribution</strong>, built from a ratio of two \(\chi^2\) variables,
        and preview ANOVA/regression testing logic.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/probability/sampling-distributions/f-distribution-and-anova-preview/">
          Next lesson: 6. F Distribution &amp; ANOVA Preview →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/probability/sampling-distributions/t-distribution-and-t-test/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 4 — t-Distribution &amp; the t-Statistic
          </a>
        </div>
      </div>
    </div>
  </div>
</section>