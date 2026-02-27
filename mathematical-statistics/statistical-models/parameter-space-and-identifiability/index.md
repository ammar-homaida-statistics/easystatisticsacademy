---
layout: default
title: "2. Parameter Space and Identifiability"
description: "Understand the parameter space, why identifiability is required, and when different parameters represent the same distribution."
permalink: /mathematical-statistics/statistical-models/parameter-space-and-identifiability/
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
        Version 0 establishes formal identifiability conditions.
        Later versions will include geometric visualizations and applied counterexamples.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update continue-reading keys -->
<script>
  (function () {

    localStorage.setItem(
      "esa_continue_ms_statistical_models_last_lesson_v0",
      JSON.stringify({
        url: "/mathematical-statistics/statistical-models/parameter-space-and-identifiability/",
        label: "Lesson 2 — Parameter Space and Identifiability",
        ts: Date.now()
      })
    );

    localStorage.setItem(
      "esa_continue_ms_last_block_v0",
      JSON.stringify({
        url: "/mathematical-statistics/statistical-models/",
        label: "Block 1 — Statistical Models",
        ts: Date.now()
      })
    );

  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">

      <div class="badge-row">
        <span class="badge">Block 1</span>
        <span class="badge">Lesson 2</span>
        <span class="badge">Parameter Space</span>
        <span class="badge">Identifiability</span>
      </div>

      <h1>2. Parameter Space and Identifiability</h1>

      <p class="lead">
        A statistical model must allow us to uniquely recover the parameter
        from the distribution it defines.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/mathematical-statistics/statistical-models/">Back to Block 1</a>
        <a class="btn btn-outline" href="/mathematical-statistics/">Mathematical Statistics home</a>
      </div>

      <p class="muted-mini">
        Without identifiability, estimation is meaningless.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      Understand the structure of the parameter space and why
      different parameter values must correspond to different distributions.
    </p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Parameter space</h2>
  </div>

  <div class="card">
    The parameter space is the set
    \[
    \Theta
    \]
    containing all admissible parameter values.
  </div>

  <p style="margin-top:.75rem;">
    Examples:
  </p>

  <ul class="bullets">
    <li>Bernoulli model: \( \Theta = (0,1) \)</li>
    <li>Normal mean known variance: \( \Theta = \mathbb{R} \)</li>
    <li>Normal model: \( \Theta = \{(\mu, \sigma^2) : \mu \in \mathbb{R}, \sigma^2 > 0\} \)</li>
  </ul>

  <p class="muted-mini">
    The parameter space must reflect mathematical and logical constraints.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Identifiability</h2>
  </div>

  <div class="card">
    A model is identifiable if:
    \[
    P_{\theta_1} = P_{\theta_2}
    \quad \Rightarrow \quad
    \theta_1 = \theta_2.
    \]
  </div>

  <p style="margin-top:.75rem;">
    This means different parameter values produce different probability distributions.
  </p>

  <p class="muted-mini">
    If two parameters generate the same distribution,
    the model cannot distinguish them.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Non-identifiable example</h2>
  </div>

  <div class="card">
    Suppose a model depends on \( \theta^2 \) instead of \( \theta \).
    Then:
    \[
    \theta \text{ and } -\theta
    \]
    produce identical distributions.
  </div>

  <p style="margin-top:.75rem;">
    The parameter is not identifiable because
    two distinct parameter values describe the same distribution.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Why identifiability matters</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Estimation</h3>
      <p style="margin:0;">
        Without identifiability, no estimator can consistently recover the true parameter.
      </p>
    </div>

    <div class="card">
      <h3>Interpretation</h3>
      <p style="margin:0;">
        Ambiguous parameters make scientific conclusions unreliable.
      </p>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Understand parameter space constraints</li>
        <li>Define identifiability formally</li>
        <li>Recognize non-identifiable structures</li>
        <li>See why identifiability is foundational</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next lesson</h2>
      <p style="margin:0;">
        We now examine IID assumptions and modeling structure.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/mathematical-statistics/statistical-models/iid-and-modeling-assumptions/">
          Continue to Lesson 3 →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini">
        <div class="mini-title">Previous lesson</div>
        <div class="mini-body">
          <a href="/mathematical-statistics/statistical-models/what-is-a-statistical-model/">
            Lesson 1: What Is a Statistical Model?
          </a>
        </div>
      </div>
    </div>
  </div>
</section>