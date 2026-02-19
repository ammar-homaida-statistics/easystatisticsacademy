---
layout: default
title: "11. Normal Distribution"
description: "The Normal distribution: bell-shaped symmetry, mean and variance, standardization, and why it dominates statistical theory."
permalink: /probability/distributions/normal-distribution/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem;">🚧 Lesson Under Construction</h2>
      <p style="margin:0; font-size:1.05rem;">
        Version 0 establishes the formal definition and key properties.
        Graphical intuition, applications, and software demonstrations will be added next.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Continue Reading Tracking -->
<script>
  (function () {
    var KEY = "esa_continue_probability_distributions_lesson_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/probability/distributions/normal-distribution/",
      label: "Lesson 11 — Normal Distribution",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 5</span>
        <span class="badge">Lesson 11</span>
        <span class="badge">Continuous</span>
        <span class="badge">Bell Curve</span>
      </div>

      <h1>11. Normal Distribution</h1>

      <p class="lead">
        The Normal distribution is the most important continuous distribution in statistics.
        It models natural variation, measurement error, and appears everywhere through the
        Central Limit Theorem.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/probability/distributions/">Back to Block 5</a>
        <a class="btn btn-outline" href="/probability/">Probability home</a>
      </div>

      <p class="muted-mini">
        Symmetric, bell-shaped, and mathematically central to inference.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Definition</h2>
  </div>

  <div class="card">
    <p>
      A random variable <strong>X</strong> follows a Normal distribution with mean <strong>&mu;</strong> and variance
      <strong>&sigma;²</strong> if its probability density function is:
    </p>

    <p style="font-size:1.1rem; margin:0;">
      $$
      f(x)=\frac{1}{\sigma\sqrt{2\pi}}
      \exp\!\left(-\frac{(x-\mu)^2}{2\sigma^2}\right),
      \quad -\infty<x<\infty.
      $$
    </p>

    <p class="muted-mini" style="margin-top:.75rem;">
      Notation: $$X\sim \mathcal{N}(\mu,\sigma^2).$$
    </p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Key properties</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Mean and variance</h3>
      <p style="margin:0;">
        $$
        \mathbb{E}[X]=\mu,
        \qquad
        \mathrm{Var}(X)=\sigma^2.
        $$
      </p>
      <p class="muted-mini" style="margin-top:.5rem;">
        &mu; shifts the center. &sigma; controls spread.
      </p>
    </div>

    <div class="card">
      <h3>Shape facts</h3>
      <ul class="bullets">
        <li>Symmetric around &mu;</li>
        <li>Mean = median = mode = &mu;</li>
        <li>Tails extend to &plusmn;&infin; (but probability mass stays 1)</li>
        <li>Always unimodal (single peak)</li>
      </ul>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Standard normal and standardization</h2>
  </div>

  <div class="card">
    <p style="margin:0;">
      The <strong>standard normal</strong> distribution is:
      $$
      Z\sim \mathcal{N}(0,1).
      $$
    </p>
  </div>

  <div class="card" style="margin-top:1rem;">
    <h3>Z-score (standardization)</h3>
    <p style="margin:0;">
      If $$X\sim \mathcal{N}(\mu,\sigma^2),$$ then
      $$
      Z=\frac{X-\mu}{\sigma}\sim \mathcal{N}(0,1).
      $$
    </p>
    <p class="muted-mini" style="margin-top:.5rem;">
      This is how we compute Normal probabilities using standard normal tables (or software).
    </p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) The 68–95–99.7 rule (empirical rule)</h2>
    <p>
      For a Normal distribution, most probability mass lies within a few standard deviations of the mean.
    </p>
  </div>

  <div class="card">
    <ul class="bullets">
      <li>About <strong>68%</strong> of values lie in $$[\mu-\sigma,\ \mu+\sigma]$$</li>
      <li>About <strong>95%</strong> of values lie in $$[\mu-2\sigma,\ \mu+2\sigma]$$</li>
      <li>About <strong>99.7%</strong> of values lie in $$[\mu-3\sigma,\ \mu+3\sigma]$$</li>
    </ul>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    These are approximations, but very useful for quick checks and intuition.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Why the Normal distribution dominates statistics</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Central Limit Theorem (preview)</h3>
      <p>
        Sums/averages of many small independent effects often become approximately Normal,
        even if the original variables are not Normal.
      </p>
      <p class="muted-mini" style="margin-top:.5rem;">
        This explains why Normal-based inference works so often.
      </p>
    </div>

    <div class="card">
      <h3>Modeling and inference</h3>
      <ul class="bullets">
        <li>Measurement and instrument noise</li>
        <li>Sampling distributions of estimators</li>
        <li>Confidence intervals and hypothesis tests</li>
        <li>Regression errors (classical linear model)</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Define $$\mathcal{N}(\mu,\sigma^2)$$ formally</li>
        <li>Interpret the roles of &mu; and &sigma;</li>
        <li>Standardize using $$Z=(X-\mu)/\sigma$$</li>
        <li>Use the 68–95–99.7 rule as a quick diagnostic</li>
      </ul>
    </div>
  </div>
</section>

<!-- ✅ Next lesson placeholder: Lognormal -->
<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">
        Next, we study the <strong>Lognormal distribution</strong>, which models positive-valued quantities
        created by exponentiating a Normal variable.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/probability/distributions/lognormal-distribution/">
          Next lesson: 12. Lognormal Distribution →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/probability/distributions/beta-distribution/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 10 — Beta Distribution
          </a>
        </div>
      </div>
    </div>
  </div>
</section>