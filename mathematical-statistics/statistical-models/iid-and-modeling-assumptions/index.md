---
layout: default
title: "3. IID and Modeling Assumptions"
description: "Understand the IID assumption, independence vs identical distribution, and why modeling assumptions drive likelihood and inference."
permalink: /mathematical-statistics/statistical-models/iid-and-modeling-assumptions/
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
        Version 0 establishes the IID framework formally.
        Later versions will include time-series counterexamples,
        dependence structures, and graphical demonstrations.
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
        url: "/mathematical-statistics/statistical-models/iid-and-modeling-assumptions/",
        label: "Lesson 3 — IID and Modeling Assumptions",
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
        <span class="badge">Lesson 3</span>
        <span class="badge">IID</span>
        <span class="badge">Assumptions</span>
      </div>

      <h1>3. IID and Modeling Assumptions</h1>

      <p class="lead">
        Most estimation theory begins with the IID assumption.
        Understanding what it means — and what it does not mean —
        is essential.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/mathematical-statistics/statistical-models/">Back to Block 1</a>
        <a class="btn btn-outline" href="/mathematical-statistics/">Mathematical Statistics home</a>
      </div>

      <p class="muted-mini">
        Assumptions define the structure of likelihood.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      Understand independence, identical distribution, and how
      modeling assumptions determine the joint distribution of the data.
    </p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Independent and Identically Distributed (IID)</h2>
  </div>

  <div class="card">
    The IID assumption states that
    \[
    X_1, X_2, \dots, X_n
    \]
    are:
    <ul class="bullets">
      <li>Independent</li>
      <li>Identically distributed</li>
    </ul>
  </div>

  <p style="margin-top:.75rem;">
    Formally,
    \[
    P(X_1,\dots,X_n) = \prod_{i=1}^n P_\theta(X_i).
    \]
  </p>

  <p class="muted-mini">
    Independence allows factorization.
    Identical distribution ensures a common parameter.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Independence vs identical distribution</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Independence</h3>
      <p style="margin:0;">
        The joint distribution factors into a product of marginals.
      </p>
    </div>

    <div class="card">
      <h3>Identical distribution</h3>
      <p style="margin:0;">
        All observations share the same distribution and parameter.
      </p>
    </div>
  </div>

  <p class="muted-mini">
    You can have independence without identical distribution,
    and identical distribution without independence.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Why IID simplifies likelihood</h2>
  </div>

  <div class="card">
    Under IID,
    \[
    L(\theta)
    =
    \prod_{i=1}^n f(X_i \mid \theta),
    \]
    and therefore
    \[
    \log L(\theta)
    =
    \sum_{i=1}^n \log f(X_i \mid \theta).
    \]
  </div>

  <p style="margin-top:.75rem;">
    This additive structure makes estimation mathematically tractable.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) When IID fails</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Time series</h3>
      <p style="margin:0;">
        Observations depend on past values.
      </p>
    </div>

    <div class="card">
      <h3>Clustered data</h3>
      <p style="margin:0;">
        Within-group dependence violates independence.
      </p>
    </div>
  </div>

  <p class="muted-mini">
    In such cases, the joint distribution must be modeled differently.
  </p>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Understand independence formally</li>
        <li>Distinguish independence from identical distribution</li>
        <li>See how IID leads to product likelihood</li>
        <li>Recognize situations where IID is unrealistic</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next lesson</h2>
      <p style="margin:0;">
        We now examine concrete examples of parametric models.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/mathematical-statistics/statistical-models/examples-of-parametric-models/">
          Continue to Lesson 4 →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini">
        <div class="mini-title">Previous lesson</div>
        <div class="mini-body">
          <a href="/mathematical-statistics/statistical-models/parameter-space-and-identifiability/">
            Lesson 2: Parameter Space and Identifiability
          </a>
        </div>
      </div>
    </div>
  </div>
</section>