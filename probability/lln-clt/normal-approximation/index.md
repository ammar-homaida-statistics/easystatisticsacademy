---
layout: default
title: "5. Normal Approximation"
description: "Using the Central Limit Theorem to approximate probabilities in practical problems."
permalink: /probability/lln-clt/normal-approximation/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem;">🚧 Lesson Under Construction</h2>
      <p style="margin:0; font-size:1.05rem;">
        Version 0 introduces practical use of normal approximation.
        Worked examples and software demonstrations will be added in Version 1.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Tracking -->
<script>
  (function () {
    var KEY = "esa_continue_probability_lln_clt_lesson_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/probability/lln-clt/normal-approximation/",
      label: "Lesson 5 — Normal Approximation",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 6</span>
        <span class="badge">Lesson 5</span>
        <span class="badge">Application</span>
        <span class="badge">Approximation</span>
      </div>

      <h1>5. Normal Approximation</h1>
      <p class="lead">
        The Central Limit Theorem allows us to replace complicated distributions
        with an approximate <strong>normal model</strong> for large samples.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/probability/lln-clt/">Back to Block 6</a>
        <a class="btn btn-outline" href="/probability/">Probability home</a>
      </div>

      <p class="muted-mini">
        This is the bridge from probability theory to statistical inference.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      By the end of this lesson, you should be able to apply normal approximation
      to sums and averages, and know when it is appropriate.
    </p>
  </div>

  <div class="callout">
    <div class="callout-copy">
      <h2>Key idea</h2>
      <p style="margin:0;">
        When sample size is large, the sampling distribution of the mean
        is approximately normal.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Approximation for sample mean</h2>
  </div>

  <div class="card">
    <p style="margin:0;">
      For large \( n \),
      \[
      \overline{X}_n \approx N\!\left(\mu, \frac{\sigma^2}{n}\right).
      \]
    </p>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    This follows directly from the CLT.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Probability approximation</h2>
  </div>

  <div class="card">
    <p>
      To approximate:
      \[
      \Pr(a < \overline{X}_n < b),
      \]
      standardize:
    </p>

    <p>
      \[
      Z = \frac{\overline{X}_n - \mu}{\sigma/\sqrt{n}}.
      \]
    </p>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    Then use standard normal tables or software.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Example (Binomial Approximation)</h2>
  </div>

  <div class="card">
    <p>
      If \( X \sim \text{Binomial}(n,p) \) and \( n \) is large,
      then:
    </p>

    <p>
      \[
      X \approx N(np, np(1-p)).
      \]
    </p>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Continuity correction</h2>
      <p style="margin:0;">
        For discrete-to-continuous approximation, adjust by ±0.5.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) When is approximation good?</h2>
  </div>

  <div class="card">
    <ul class="bullets">
      <li>Large sample size</li>
      <li>Finite variance</li>
      <li>Original distribution not extremely skewed</li>
      <li>For binomial: \( np \) and \( n(1-p) \) sufficiently large</li>
    </ul>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Limitations</h2>
  </div>

  <div class="card">
    <ul class="bullets">
      <li>Heavy-tailed distributions may converge slowly</li>
      <li>Small sample sizes may produce poor approximation</li>
      <li>Skewed distributions require larger n</li>
    </ul>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Apply normal approximation to sample means</li>
        <li>Use continuity correction correctly</li>
        <li>Recognize when approximation is appropriate</li>
        <li>Prepare for formal statistical inference</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">
        We now connect convergence theory to statistical inference:
        confidence intervals and hypothesis testing.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/probability/lln-clt/why-inference-works/">
          Next lesson: 6. Why Inference Works →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/probability/lln-clt/central-limit-theorem/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 4 — Central Limit Theorem
          </a>
        </div>
      </div>
    </div>
  </div>
</section>