---
layout: default
title: "6. F-Distribution & ANOVA Preview"
description: "Ratio of variances, F-distribution, degrees of freedom, and how it leads to ANOVA and regression testing."
permalink: /probability/sampling-distributions/f-distribution-and-anova-preview/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem;">🚧 Lesson Under Construction</h2>
      <p style="margin:0; font-size:1.05rem;">
        Version 0 introduces the F-distribution and explains how it compares variances.
        Full ANOVA derivations and regression connections will be added in Version 1.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Continue Reading Tracking -->
<script>
  (function () {
    var KEY = "esa_continue_probability_sampling_distributions_lesson_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/probability/sampling-distributions/f-distribution-and-anova-preview/",
      label: "Lesson 6 — F-Distribution & ANOVA Preview",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 7</span>
        <span class="badge">Lesson 6</span>
        <span class="badge">F</span>
        <span class="badge">ANOVA</span>
      </div>

      <h1>6. F-Distribution & ANOVA Preview</h1>

      <p class="lead">
        The <strong>F-distribution</strong> arises as the ratio of two independent
        chi-square variables divided by their degrees of freedom.
        It is the foundation of variance comparison and ANOVA.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/probability/sampling-distributions/">Back to Block 7</a>
        <a class="btn btn-outline" href="/probability/">Probability home</a>
      </div>

      <p class="muted-mini">
        F-tests compare variability across sources.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      By the end of this lesson, you should understand how the F-distribution is constructed
      and why it is used to compare variances and test group differences.
    </p>
  </div>

  <div class="callout">
    <div class="callout-copy">
      <h2>Key idea</h2>
      <p style="margin:0;">
        If \(U \sim \chi^2_{d_1}\) and \(V \sim \chi^2_{d_2}\) independently, then:
        \[
        F=\frac{(U/d_1)}{(V/d_2)} \sim F_{d_1,d_2}.
        \]
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Definition of the F-distribution</h2>
  </div>

  <div class="card">
    <p style="margin:0;">
      The F-distribution is a ratio of two scaled chi-square variables.
      It has two degrees of freedom:
      \[
      d_1 \text{ (numerator)}, \quad d_2 \text{ (denominator)}.
      \]
    </p>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    It is always positive and right-skewed.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Comparing two variances</h2>
  </div>

  <div class="card">
    <p style="margin:0;">
      Suppose two independent samples have variances \(S_1^2\) and \(S_2^2\).
      Then:
      \[
      F=\frac{S_1^2}{S_2^2}
      \]
      follows an F-distribution under Normality assumptions.
    </p>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Interpretation</h2>
      <p style="margin:0;">
        Large F values suggest unequal variances.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Connection to ANOVA</h2>
  </div>

  <div class="card">
    <p style="margin:0;">
      In one-way ANOVA:
      \[
      F = \frac{\text{Between-group variance}}{\text{Within-group variance}}.
      \]
    </p>
  </div>

  <div class="card" style="margin-top:1rem;">
    <ul class="bullets">
      <li>If group means are equal → ratio ≈ 1.</li>
      <li>If means differ → between variance increases → F large.</li>
    </ul>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Relation to regression</h2>
  </div>

  <div class="card">
    <p style="margin:0;">
      In linear regression, the overall significance test uses:
      \[
      F = \frac{\text{Explained variance}}{\text{Unexplained variance}}.
      \]
    </p>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    Thus, ANOVA and regression share the same distributional foundation.
  </p>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Understand construction of the F-distribution</li>
        <li>Interpret numerator and denominator degrees of freedom</li>
        <li>Compare variances using F-tests</li>
        <li>Preview ANOVA logic</li>
        <li>Recognize connection to regression</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Block 7 Complete</h2>
      <p style="margin:0;">
        You now understand the major sampling distributions:
        z, t, χ², and F.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/probability/">
          Return to Probability →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/probability/sampling-distributions/chi-square-and-variance/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 5 — Chi-Square Distribution
          </a>
        </div>
      </div>
    </div>
  </div>
</section>