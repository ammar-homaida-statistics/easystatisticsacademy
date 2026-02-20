---
layout: default
title: "2. Law of Large Numbers"
description: "The Law of Large Numbers explains why sample averages converge to the true expected value."
permalink: /probability/lln-clt/law-of-large-numbers/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem;">🚧 Lesson Under Construction</h2>
      <p style="margin:0; font-size:1.05rem;">
        Version 0 establishes the theorem statement and intuition.
        Formal proofs and simulations will be added in Version 1.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Tracking -->
<script>
  (function () {
    var KEY = "esa_continue_probability_lln_clt_lesson_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/probability/lln-clt/law-of-large-numbers/",
      label: "Lesson 2 — Law of Large Numbers",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 6</span>
        <span class="badge">Lesson 2</span>
        <span class="badge">LLN</span>
        <span class="badge">Convergence</span>
      </div>

      <h1>2. Law of Large Numbers</h1>
      <p class="lead">
        The Law of Large Numbers explains a fundamental phenomenon:
        <strong>averages stabilize as sample size grows.</strong>
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/probability/lln-clt/">Back to Block 6</a>
        <a class="btn btn-outline" href="/probability/">Probability home</a>
      </div>

      <p class="muted-mini">
        This theorem justifies estimation in statistics.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      By the end of this lesson, you should understand the statement of the LLN,
      interpret convergence in probability, and explain why sample averages stabilize.
    </p>
  </div>

  <div class="callout">
    <div class="callout-copy">
      <h2>Key idea</h2>
      <p style="margin:0;">
        If observations are independent and share the same mean,
        their average gets closer to that mean as the sample size increases.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Setup</h2>
    <p>
      Let \(X_1, X_2, \dots\) be independent and identically distributed (i.i.d.)
      random variables with:
    </p>
  </div>

  <div class="card">
    <p style="margin:0;">
      \[
      \mathbb{E}[X_i] = \mu,
      \quad
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
    <h2>2) Weak Law of Large Numbers (WLLN)</h2>
  </div>

  <div class="card">
    <p style="margin:0; font-size:1.1rem;">
      \[
      \overline{X}_n \xrightarrow{P} \mu.
      \]
    </p>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    Meaning:
  </p>

  <div class="card">
    <p style="margin:0;">
      For every \( \varepsilon > 0 \),
      \[
      \Pr\!\left(|\overline{X}_n - \mu| > \varepsilon\right)
      \to 0 \quad \text{as } n \to \infty.
      \]
    </p>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Interpretation</h2>
      <p style="margin:0;">
        The probability that the sample mean deviates from the true mean
        by more than a small amount becomes very small for large samples.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Why it works (intuition)</h2>
  </div>

  <div class="card">
    <ul class="bullets">
      <li>Each observation has mean μ.</li>
      <li>Noise cancels out as we average.</li>
      <li>Variance of the mean shrinks:</li>
    </ul>

    <p style="margin-top:1rem;">
      \[
      \operatorname{Var}(\overline{X}_n)
      =
      \frac{\sigma^2}{n}.
      \]
    </p>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    As \(n\) increases, variability decreases.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) What LLN does NOT say</h2>
  </div>

  <div class="card">
    <ul class="bullets">
      <li>It does NOT say the average equals μ exactly.</li>
      <li>It does NOT say convergence is fast.</li>
      <li>It requires finite expectation.</li>
    </ul>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Practical meaning</h2>
  </div>

  <div class="card">
    <ul class="bullets">
      <li>Justifies sample mean as estimator</li>
      <li>Explains stability in polling and surveys</li>
      <li>Foundation of frequentist statistics</li>
    </ul>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>State the Weak Law of Large Numbers</li>
        <li>Interpret convergence in probability</li>
        <li>Understand variance shrinking as \(1/n\)</li>
        <li>Connect LLN to estimation</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">
        There is a stronger version of convergence —
        <strong>almost sure convergence</strong>.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/probability/lln-clt/weak-vs-strong-lln/">
          Next lesson: 3. Weak vs Strong LLN →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini">
        <div class="mini-title">Previous lesson</div>
        <div class="mini-body">
          <a href="/probability/lln-clt/convergence-intuition/">
            Lesson 1 — Convergence Intuition
          </a>
        </div>
      </div>
    </div>
  </div>
</section>