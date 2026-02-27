---
layout: default
title: "4. Information Additivity and IID"
description: "Understand how Fisher information adds under independence and why it scales with sample size."
permalink: /mathematical-statistics/fisher-information-and-efficiency/information-additivity-and-iid/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#eef5ff; border:2px solid #3f51b5; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#1a237e; font-size:1.8rem; letter-spacing:0.5px;">
        🚧 Lesson Under Construction
      </h2>
      <p style="margin:0; font-size:1.05rem; color:#283593; line-height:1.6;">
        Version 0 explains why Fisher information is additive under independence.
        Later versions will include dependent-data extensions.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update continue-reading keys -->
<script>
  (function () {

    localStorage.setItem(
      "esa_continue_ms_information_last_lesson_v0",
      JSON.stringify({
        url: "/mathematical-statistics/fisher-information-and-efficiency/information-additivity-and-iid/",
        label: "Lesson 4 — Information Additivity and IID",
        ts: Date.now()
      })
    );

    localStorage.setItem(
      "esa_continue_ms_last_block_v0",
      JSON.stringify({
        url: "/mathematical-statistics/fisher-information-and-efficiency/",
        label: "Block 5 — Fisher Information & Efficiency",
        ts: Date.now()
      })
    );

  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">

      <div class="badge-row">
        <span class="badge">Block 5</span>
        <span class="badge">Lesson 4</span>
        <span class="badge">Additivity</span>
        <span class="badge">IID</span>
      </div>

      <h1>4. Information Additivity and IID</h1>

      <p class="lead">
        Under independence, Fisher information from each observation adds.
        This explains why precision improves with sample size.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/mathematical-statistics/fisher-information-and-efficiency/">Back to Block 5</a>
        <a class="btn btn-outline" href="/mathematical-statistics/">Mathematical Statistics home</a>
      </div>

      <p class="muted-mini">
        Information grows linearly with n under IID sampling.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      Understand why Fisher information adds across independent observations
      and why it typically scales with sample size.
    </p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Log-likelihood for IID data</h2>
  </div>

  <div class="card">
    For IID observations:
    \[
    \ell(\theta)
    =
    \sum_{i=1}^n \log f(X_i;\theta).
    \]
  </div>

  <p class="muted-mini">
    The total log-likelihood is a sum.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Score additivity</h2>
  </div>

  <div class="card">
    The score becomes
    \[
    U(\theta)
    =
    \sum_{i=1}^n U_i(\theta).
    \]
  </div>

  <p>
    Under independence:
    \[
    \text{Var}(U(\theta))
    =
    \sum_{i=1}^n \text{Var}(U_i(\theta)).
    \]
  </p>

  <p class="muted-mini">
    Independence eliminates cross-covariance terms.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Information additivity</h2>
  </div>

  <div class="card">
    Since
    \[
    I(\theta) = \mathbb{E}[U(\theta)^2],
    \]
    we obtain
    \[
    I_n(\theta)
    =
    n I_1(\theta).
    \]
  </div>

  <p class="muted-mini">
    Information grows linearly with sample size.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Consequence for CRLB</h2>
  </div>

  <div class="card">
    The CRLB becomes
    \[
    \text{Var}(\hat{\theta})
    \ge
    \frac{1}{n I_1(\theta)}.
    \]
  </div>

  <p>
    As \(n\) increases, the lower bound decreases.
  </p>

  <p class="muted-mini">
    Precision improves at rate \(1/n\).
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Intuition</h2>
  </div>

  <div class="grid grid-2">

    <div class="card">
      <h3>More data → more curvature</h3>
      <p style="margin:0;">
        Log-likelihood becomes sharper.
      </p>
    </div>

    <div class="card">
      <h3>More data → smaller variance</h3>
      <p style="margin:0;">
        Variance shrinks proportionally to \(1/n\).
      </p>
    </div>

    <div class="card">
      <h3>Independence matters</h3>
      <p style="margin:0;">
        Dependence changes additivity.
      </p>
    </div>

    <div class="card">
      <h3>Foundation for asymptotics</h3>
      <p style="margin:0;">
        Leads to normal approximations later.
      </p>
    </div>

  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Understand why information adds under independence</li>
        <li>See linear scaling with sample size</li>
        <li>Connect additivity to shrinking variance</li>
        <li>Prepare for asymptotic MLE theory</li>
      </ul>
    </div>
  </div>
</section>

<!-- ✅ Next + Previous navigation -->
<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next lesson</h2>
      <p style="margin:0;">
        We now preview how Fisher information determines
        the asymptotic variance of the MLE.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/mathematical-statistics/fisher-information-and-efficiency/information-and-mle-connection-preview/">
          Continue to Lesson 5 →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/mathematical-statistics/fisher-information-and-efficiency/efficiency-and-achieving-the-bound/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 3: Efficiency
          </a>
        </div>
      </div>
    </div>

  </div>
</section>