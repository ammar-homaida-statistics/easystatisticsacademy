---
layout: default
title: "3. Weak vs Strong Law of Large Numbers"
description: "Understanding the difference between convergence in probability and almost sure convergence."
permalink: /probability/lln-clt/weak-vs-strong-lln/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem;">🚧 Lesson Under Construction</h2>
      <p style="margin:0; font-size:1.05rem;">
        Version 0 introduces the conceptual and formal differences.
        Rigorous proofs and measure-theoretic details will be added later.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Tracking -->
<script>
  (function () {
    var KEY = "esa_continue_probability_lln_clt_lesson_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/probability/lln-clt/weak-vs-strong-lln/",
      label: "Lesson 3 — Weak vs Strong LLN",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 6</span>
        <span class="badge">Lesson 3</span>
        <span class="badge">WLLN</span>
        <span class="badge">SLLN</span>
      </div>

      <h1>3. Weak vs Strong Law of Large Numbers</h1>
      <p class="lead">
        Both versions of the Law of Large Numbers say the sample mean approaches the true mean —
        but they differ in <strong>how strong the convergence is.</strong>
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/probability/lln-clt/">Back to Block 6</a>
        <a class="btn btn-outline" href="/probability/">Probability home</a>
      </div>

      <p class="muted-mini">
        Convergence type matters in theoretical probability.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Recall: Weak Law (WLLN)</h2>
  </div>

  <div class="card">
    <p style="margin:0; font-size:1.05rem;">
      \[
      \overline{X}_n \xrightarrow{P} \mu
      \]
    </p>
    <p class="muted-mini" style="margin-top:.5rem;">
      Convergence in probability.
    </p>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    For every \( \varepsilon > 0 \),
    \[
    \Pr(|\overline{X}_n - \mu| > \varepsilon) \to 0.
    \]
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Strong Law (SLLN)</h2>
  </div>

  <div class="card">
    <p style="margin:0; font-size:1.05rem;">
      \[
      \overline{X}_n \xrightarrow{a.s.} \mu
      \]
    </p>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Meaning</h2>
      <p style="margin:0;">
        With probability 1, the sequence of sample means eventually stays arbitrarily close to μ.
      </p>
    </div>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    “Almost surely” means except on a probability-zero set.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Intuitive difference</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Weak Law</h3>
      <ul class="bullets">
        <li>Probability of large deviation goes to zero</li>
        <li>Focuses on distribution behavior</li>
        <li>Does not guarantee pathwise stability</li>
      </ul>
    </div>

    <div class="card">
      <h3>Strong Law</h3>
      <ul class="bullets">
        <li>Individual sample paths converge</li>
        <li>Stronger statement</li>
        <li>Implies Weak Law</li>
      </ul>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Relationship</h2>
  </div>

  <div class="card">
    <p style="margin:0;">
      \[
      \text{Almost sure convergence}
      \quad \Rightarrow \quad
      \text{Convergence in probability}
      \]
    </p>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    The converse is generally false.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Assumptions</h2>
  </div>

  <div class="card">
    <ul class="bullets">
      <li>i.i.d. observations</li>
      <li>Finite expectation</li>
      <li>Strong law may require slightly stronger technical conditions</li>
    </ul>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Differentiate WLLN and SLLN</li>
        <li>Interpret almost sure convergence</li>
        <li>Understand implication hierarchy</li>
        <li>Prepare for Central Limit Theorem</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">
        Even though averages converge to μ,
        their distribution around μ has structure —
        this leads to the <strong>Central Limit Theorem</strong>.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/probability/lln-clt/central-limit-theorem/">
          Next lesson: 4. Central Limit Theorem →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini">
        <div class="mini-title">Previous lesson</div>
        <div class="mini-body">
          <a href="/probability/lln-clt/law-of-large-numbers/">
            Lesson 2 — Law of Large Numbers
          </a>
        </div>
      </div>
    </div>
  </div>
</section>