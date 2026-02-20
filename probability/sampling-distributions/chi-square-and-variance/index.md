---
layout: default
title: "5. Chi-Square Distribution & Variance Inference"
description: "Sampling distribution of the sample variance, chi-square distribution, degrees of freedom, and inference for σ²."
permalink: /probability/sampling-distributions/chi-square-and-variance/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem;">🚧 Lesson Under Construction</h2>
      <p style="margin:0; font-size:1.05rem;">
        Version 0 introduces the chi-square distribution and explains
        how it governs inference for population variance.
        Examples and graphical intuition will be added in Version 1.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Continue Reading Tracking -->
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
        <span class="badge">Chi-Square</span>
        <span class="badge">Variance</span>
      </div>

      <h1>5. Chi-Square Distribution & Variance Inference</h1>

      <p class="lead">
        While the Normal and t-distributions govern inference for the mean,
        the <strong>chi-square distribution</strong> governs inference for variance.
        It emerges from squared standard Normal variables.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/probability/sampling-distributions/">Back to Block 7</a>
        <a class="btn btn-outline" href="/probability/">Probability home</a>
      </div>

      <p class="muted-mini">
        Variance inference requires a different reference distribution.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      By the end of this lesson, you should understand how the chi-square distribution arises
      and how it is used to construct confidence intervals and tests for σ².
    </p>
  </div>

  <div class="callout">
    <div class="callout-copy">
      <h2>Key idea</h2>
      <p style="margin:0;">
        If \(Z_1,\dots,Z_k \sim N(0,1)\) independently, then
        \[
        \sum_{i=1}^{k} Z_i^2 \sim \chi^2_k.
        \]
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Origin of the chi-square distribution</h2>
  </div>

  <div class="card">
    <p style="margin:0;">
      The chi-square distribution with \(k\) degrees of freedom
      is the sum of squares of \(k\) independent standard Normal variables.
    </p>
  </div>

  <div class="card" style="margin-top:1rem;">
    <p style="margin:0;">
      \[
      \chi^2_k = Z_1^2 + Z_2^2 + \dots + Z_k^2.
      \]
    </p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Sampling distribution of the sample variance</h2>
  </div>

  <div class="card">
    <p style="margin:0;">
      If \(X_1,\dots,X_n \sim N(\mu,\sigma^2)\), then:
      \[
      \frac{(n-1)S^2}{\sigma^2} \sim \chi^2_{n-1}.
      \]
    </p>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    This result holds only under Normality.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Shape and properties</h2>
  </div>

  <div class="card">
    <ul class="bullets">
      <li>Support: positive values only</li>
      <li>Right-skewed (especially for small df)</li>
      <li>Mean = \(k\)</li>
      <li>Variance = \(2k\)</li>
    </ul>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    As degrees of freedom increase, the distribution becomes more symmetric.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Confidence interval for variance</h2>
  </div>

  <div class="card">
    <p style="margin:0;">
      A \(100(1-\alpha)\%\) CI for \(\sigma^2\):
      \[
      \left(
      \frac{(n-1)S^2}{\chi^2_{1-\alpha/2,n-1}},
      \frac{(n-1)S^2}{\chi^2_{\alpha/2,n-1}}
      \right).
      \]
    </p>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    Note the reversal of critical values due to asymmetry.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Hypothesis test for variance</h2>
  </div>

  <div class="card">
    <p style="margin:0;">
      To test \(H_0:\sigma^2=\sigma_0^2\):
      \[
      \chi^2 = \frac{(n-1)S^2}{\sigma_0^2}.
      \]
    </p>
  </div>

  <div class="card" style="margin-top:1rem;">
    <ul class="bullets">
      <li>Compare with \(\chi^2_{n-1}\) critical values.</li>
      <li>One-sided or two-sided tests possible.</li>
    </ul>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Understand how χ² arises from squared Normals</li>
        <li>Derive sampling distribution of S²</li>
        <li>Construct confidence intervals for σ²</li>
        <li>Perform variance hypothesis tests</li>
        <li>Prepare for F-distribution</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">
        Next, we combine two chi-square variables to form the
        <strong>F-distribution</strong>, used in comparing variances and ANOVA.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/probability/sampling-distributions/f-distribution-and-anova-perview/">
          Next lesson: 6. F-Distribution & ANOVA →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/probability/sampling-distributions/t-distribution-and-t-test/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 4 — t-Distribution
          </a>
        </div>
      </div>
    </div>
  </div>
</section>