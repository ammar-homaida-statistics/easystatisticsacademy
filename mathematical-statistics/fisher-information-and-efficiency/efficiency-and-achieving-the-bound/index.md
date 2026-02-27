---
layout: default
title: "3. Efficiency and Achieving the Bound"
description: "Define efficiency and understand when an unbiased estimator attains the Cramér–Rao lower bound."
permalink: /mathematical-statistics/fisher-information-and-efficiency/efficiency-and-achieving-the-bound/
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
        Version 0 defines efficiency and explains what it means to achieve the CRLB.
        Later versions will include equality conditions and exponential-family examples.
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
        url: "/mathematical-statistics/fisher-information-and-efficiency/efficiency-and-achieving-the-bound/",
        label: "Lesson 3 — Efficiency and Achieving the Bound",
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
        <span class="badge">Lesson 3</span>
        <span class="badge">Efficiency</span>
        <span class="badge">CRLB</span>
      </div>

      <h1>3. Efficiency and Achieving the Bound</h1>

      <p class="lead">
        Efficiency measures how close an estimator’s variance is to the theoretical minimum
        given by the Cramér–Rao lower bound.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/mathematical-statistics/fisher-information-and-efficiency/">Back to Block 5</a>
        <a class="btn btn-outline" href="/mathematical-statistics/">Mathematical Statistics home</a>
      </div>

      <p class="muted-mini">
        Efficient estimators attain the CRLB.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      Define efficiency for unbiased estimators and understand what it means
      to achieve the Cramér–Rao lower bound.
    </p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Efficiency definition</h2>
  </div>

  <div class="card">
    For an unbiased estimator \(\hat{\theta}\), the CRLB states:
    \[
    \text{Var}(\hat{\theta})
    \ge
    \frac{1}{I(\theta)}.
    \]
  </div>

  <div class="card">
    Efficiency is defined as
    \[
    e(\hat{\theta})
    =
    \frac{\frac{1}{I(\theta)}}{\text{Var}(\hat{\theta})}
    \in (0,1].
    \]
  </div>

  <p class="muted-mini">
    Efficiency equals 1 if the estimator attains the bound.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) What does it mean to achieve the CRLB?</h2>
  </div>

  <div class="card">
    An unbiased estimator \(\hat{\theta}\) is called efficient if
    \[
    \text{Var}(\hat{\theta}) = \frac{1}{I(\theta)}.
    \]
  </div>

  <p style="margin-top:.75rem;">
    This means no unbiased estimator can have smaller variance.
  </p>

  <p class="muted-mini">
    Efficient estimators are “best possible” within unbiased estimators.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Equality case (preview)</h2>
  </div>

  <div class="card">
    In the proof of CRLB, equality happens when the estimator error is
    perfectly aligned with the score function:
    \[
    \hat{\theta}-\theta = a(\theta)\,U(\theta)
    \quad \text{for some } a(\theta).
    \]
  </div>

  <p class="muted-mini">
    This is a strong condition and does not always hold.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Example: Bernoulli proportion</h2>
  </div>

  <div class="card">
    For \(X_i \sim \text{Bernoulli}(p)\),
    the sample proportion
    \[
    \hat{p}=\bar{X}
    \]
    is unbiased and has variance
    \[
    \text{Var}(\hat{p}) = \frac{p(1-p)}{n}.
    \]
  </div>

  <div class="card">
    The CRLB is
    \[
    \frac{1}{I(p)} = \frac{p(1-p)}{n}.
    \]
  </div>

  <p class="muted-mini">
    So \(\hat{p}\) is efficient.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Important limitation</h2>
  </div>

  <div class="grid grid-2">

    <div class="card">
      <h3>Bound applies to unbiased estimators</h3>
      <p style="margin:0;">
        Biased estimators can have smaller MSE than any unbiased estimator.
      </p>
    </div>

    <div class="card">
      <h3>Not always attainable</h3>
      <p style="margin:0;">
        Some models do not admit any unbiased estimator achieving CRLB.
      </p>
    </div>

  </div>

  <p class="muted-mini">
    CRLB is a benchmark, not a guarantee.
  </p>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Define efficiency using the CRLB</li>
        <li>Understand what “attaining the bound” means</li>
        <li>See an efficient estimator example</li>
        <li>Prepare for information additivity</li>
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
        We now study how Fisher information scales with sample size
        under independence (additivity and IID).
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/mathematical-statistics/fisher-information-and-efficiency/information-additivity-and-iid/">
          Continue to Lesson 4 →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/mathematical-statistics/fisher-information-and-efficiency/cramer-rao-lower-bound/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 2: Cramér–Rao Lower Bound
          </a>
        </div>
      </div>
    </div>

  </div>
</section>