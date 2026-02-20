---
layout: default
title: "4. Central Limit Theorem"
description: "The Central Limit Theorem explains why sums and averages become approximately normal as sample size increases."
permalink: /probability/lln-clt/central-limit-theorem/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem;">🚧 Lesson Under Construction</h2>
      <p style="margin:0; font-size:1.05rem;">
        Version 0 presents the formal statement and core intuition.
        Proof sketches, simulations, and refinements will be added in Version 1.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Tracking -->
<script>
  (function () {
    var KEY = "esa_continue_probability_lln_clt_lesson_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/probability/lln-clt/central-limit-theorem/",
      label: "Lesson 4 — Central Limit Theorem",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 6</span>
        <span class="badge">Lesson 4</span>
        <span class="badge">CLT</span>
        <span class="badge">Normal Approximation</span>
      </div>

      <h1>4. Central Limit Theorem</h1>
      <p class="lead">
        The Central Limit Theorem explains a remarkable fact:
        <strong>no matter the original distribution, sums and averages tend toward normality.</strong>
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/probability/lln-clt/">Back to Block 6</a>
        <a class="btn btn-outline" href="/probability/">Probability home</a>
      </div>

      <p class="muted-mini">
        This theorem powers modern statistical inference.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      By the end of this lesson, you should understand the formal statement of the CLT,
      interpret standardization, and explain why normal distributions appear everywhere.
    </p>
  </div>

  <div class="callout">
    <div class="callout-copy">
      <h2>Key idea</h2>
      <p style="margin:0;">
        When independent observations are added or averaged,
        their standardized sum approaches a normal distribution.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Setup</h2>
    <p>
      Let \(X_1, X_2, \dots, X_n\) be i.i.d. random variables with:
    </p>
  </div>

  <div class="card">
    <p style="margin:0;">
      \[
      \mathbb{E}[X_i] = \mu,
      \qquad
      \operatorname{Var}(X_i) = \sigma^2 < \infty.
      \]
    </p>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    Define the sample mean:
  </p>

  <div class="card">
    <p style="margin:0;">
      \[
      \overline{X}_n = \frac{1}{n} \sum_{i=1}^n X_i.
      \]
    </p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) The Central Limit Theorem</h2>
  </div>

  <div class="card">
    <p style="margin:0; font-size:1.05rem;">
      \[
      \frac{\overline{X}_n - \mu}{\sigma / \sqrt{n}}
      \xrightarrow{d}
      N(0,1).
      \]
    </p>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    The standardized sample mean converges in distribution to the standard normal.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) What this means</h2>
  </div>

  <div class="card">
    <ul class="bullets">
      <li>The distribution of the sample mean becomes approximately normal.</li>
      <li>The approximation improves as \(n\) increases.</li>
      <li>The original distribution does not need to be normal.</li>
    </ul>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Important</h2>
      <p style="margin:0;">
        The CLT describes the distribution of the average —
        not the distribution of individual observations.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Standardization step</h2>
  </div>

  <div class="card">
    <p style="margin:0;">
      \[
      Z =
      \frac{\overline{X}_n - \mu}
      {\sigma / \sqrt{n}}.
      \]
    </p>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    This converts the sample mean into a standard normal variable approximately.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Why CLT is powerful</h2>
  </div>

  <div class="card">
    <ul class="bullets">
      <li>Justifies confidence intervals</li>
      <li>Justifies hypothesis testing</li>
      <li>Explains normal approximations (binomial → normal)</li>
      <li>Explains why measurement errors appear normal</li>
    </ul>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>State the CLT formally</li>
        <li>Understand convergence in distribution</li>
        <li>Standardize sample means correctly</li>
        <li>Explain why normal distributions dominate statistics</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">
        Next, we explore practical normal approximation
        and see how CLT is used in real problems.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/probability/lln-clt/normal-approximation/">
          Next lesson: 5. Normal Approximation →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini">
        <div class="mini-title">Previous lesson</div>
        <div class="mini-body">
          <a href="/probability/lln-clt/weak-vs-strong-lln/">
            Lesson 3 — Weak vs Strong LLN
          </a>
        </div>
      </div>
    </div>
  </div>
</section>