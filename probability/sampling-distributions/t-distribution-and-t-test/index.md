---
layout: default
title: "4. t-Distribution & the t-Statistic"
description: "Unknown σ: Student’s t distribution, degrees of freedom, and why t replaces z for inference about a mean."
permalink: /probability/sampling-distributions/t-distribution-and-t-test/
sidebar: false
---

<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem; letter-spacing:0.5px;">🚧 Lesson Under Construction</h2>
      <p style="margin:0; font-size:1.05rem; color:#5d4037; line-height:1.6;">
        Version 0 defines the t-statistic and degrees of freedom. Visual intuition and examples will be added later.
      </p>
    </div>
  </div>
</section>

<script>
  (function () {
    var KEY = "esa_continue_probability_sampling_distributions_lesson_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/probability/sampling-distributions/t-distribution-and-t-test/",
      label: "Lesson 4 — t-Distribution & the t-Statistic",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 7</span>
        <span class="badge">Lesson 4</span>
        <span class="badge">t</span>
        <span class="badge">df</span>
      </div>

      <h1>4. t-Distribution &amp; the t-Statistic</h1>
      <p class="lead">
        When \(\sigma\) is unknown, we estimate it using the sample standard deviation \(S\).
        This extra uncertainty changes the reference distribution from Normal to <strong>Student’s t</strong>.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/probability/sampling-distributions/">Back to Block 7</a>
        <a class="btn btn-outline" href="/probability/">Probability home</a>
      </div>

      <p class="muted-mini">
        Key message: t is wider than z for small samples; it approaches Normal as \(n\) grows.
      </p>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">
        Next, we study the \(\chi^2\) distribution and why it governs inference about <strong>variance</strong>.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/probability/sampling-distributions/chi-square-and-variance/">
          Next lesson: 5. Chi-Square Distribution &amp; Variance Inference →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/probability/sampling-distributions/z-statistic-and-ci/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 3 — z-Statistic &amp; Confidence Intervals
          </a>
        </div>
      </div>
    </div>
  </div>
</section>