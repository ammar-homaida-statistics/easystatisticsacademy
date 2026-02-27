---
layout: default
title: "1. What Is a Statistical Model?"
description: "Define a statistical model formally as a family of probability distributions indexed by a parameter."
permalink: /mathematical-statistics/statistical-models/what-is-a-statistical-model/
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
        Version 0 establishes the formal definition of a statistical model.
        Later versions will include geometric intuition, graphical illustrations,
        and applied modeling case studies.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update continue-reading keys -->
<script>
  (function () {

    /* Block key (Statistical Models block) */
    localStorage.setItem(
      "esa_continue_ms_statistical_models_last_lesson_v0",
      JSON.stringify({
        url: "/mathematical-statistics/statistical-models/what-is-a-statistical-model/",
        label: "Lesson 1 — What Is a Statistical Model?",
        ts: Date.now()
      })
    );

    /* Mathematical Statistics HOME key */
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
        <span class="badge">Lesson 1</span>
        <span class="badge">Model Definition</span>
        <span class="badge">Parametric Family</span>
      </div>

      <h1>1. What Is a Statistical Model?</h1>

      <p class="lead">
        A statistical model is not a formula.
        It is a structured mathematical description of how data are generated.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/mathematical-statistics/statistical-models/">Back to Block 1</a>
        <a class="btn btn-outline" href="/mathematical-statistics/">Mathematical Statistics home</a>
      </div>

      <p class="muted-mini">
        Every estimation procedure begins with a model.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      Understand formally what a statistical model is,
      how it relates to probability distributions,
      and why parameters define families of possible worlds.
    </p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Informal idea</h2>
  </div>

  <div class="card">
    A statistical model describes
    how data could have been generated.
  </div>

  <p style="margin-top:.75rem;">
    Instead of assuming one fixed distribution,
    we consider a <strong>family</strong> of possible distributions.
    Each member of the family corresponds to a different parameter value.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Formal definition</h2>
  </div>

  <div class="card">
    A statistical model is a collection of probability distributions
    \[
    \mathcal{P} = \{ P_\theta : \theta \in \Theta \}
    \]
    where:
    <ul class="bullets">
      <li>\(\Theta\) is the parameter space</li>
      <li>\(\theta\) is an unknown parameter</li>
      <li>\(P_\theta\) defines the distribution of the data</li>
    </ul>
  </div>

  <p class="muted-mini">
    The true data-generating process corresponds to one unknown parameter value.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Example: Normal model</h2>
  </div>

  <div class="card">
    If
    \[
    X_1, \dots, X_n \sim \mathcal{N}(\mu, \sigma^2),
    \]
    then the model is:
    \[
    \{ \mathcal{N}(\mu, \sigma^2) : \mu \in \mathbb{R},\ \sigma^2 > 0 \}.
    \]
  </div>

  <p style="margin-top:.75rem;">
    Each pair \((\mu, \sigma^2)\) defines a different distribution.
    The model is the entire family.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Why models matter</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Estimation depends on the model</h3>
      <p style="margin:0;">
        The likelihood function comes directly from the assumed distribution.
      </p>
    </div>

    <div class="card">
      <h3>Inference depends on assumptions</h3>
      <p style="margin:0;">
        If the model is wrong, conclusions may be misleading.
      </p>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Understand model as a family of distributions</li>
        <li>Recognize the role of the parameter space</li>
        <li>See how likelihood emerges from the model</li>
        <li>Prepare for identifiability and assumptions</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next lesson</h2>
      <p style="margin:0;">
        We now study the parameter space and identifiability.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/mathematical-statistics/statistical-models/parameter-space-and-identifiability/">
          Continue to Lesson 2 →
        </a>
      </div>
    </div>
  </div>
</section>