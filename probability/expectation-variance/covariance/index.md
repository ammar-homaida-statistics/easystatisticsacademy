---
layout: default
title: "3. Covariance"
description: "Covariance measures joint variability and explains why Var(X+Y) is not always Var(X)+Var(Y)."
permalink: /probability/expectation-variability/covariance/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem; letter-spacing:0.5px;">🚧 Lesson Under Construction</h2>
      <p style="margin:0; font-size:1.05rem; color:#5d4037; line-height:1.6;">
        Version 0 is published first to lock the structure and the correct conceptual flow.
        Examples, graphs, and software demonstrations will be added later without changing the lesson order.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update "last visited lesson" for Probability Block 4 -->
<script>
  (function () {
    var KEY = "esa_continue_probability_expectation_variability_lesson_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/probability/expectation-variability/covariance/",
      label: "Lesson 3 — Covariance",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">

      <div class="badge-row">
        <span class="badge">Block 4</span>
        <span class="badge">Lesson 3</span>
        <span class="badge">Dependence</span>
        <span class="badge">Covariance</span>
      </div>

      <h1>3. Covariance</h1>

      <p class="lead">
        Covariance quantifies how two random variables vary together.
        It is the missing term that makes variance-of-sums correct under dependence.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/probability/expectation-variability/variance-rules-and-sums/">
          ← Previous lesson: 2. Variance Rules & Sums
        </a>
        <a class="btn btn-outline" href="/probability/expectation-variability/">Back to Block 4</a>
      </div>

      <p class="muted-mini">
        If you understand covariance, you understand uncertainty propagation.
      </p>

    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">
        Next, we standardize covariance into a unitless, interpretable measure: correlation.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/probability/expectation-variability/correlation/">
          Next lesson: 4. Correlation →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/probability/expectation-variability/variance-rules-and-sums/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 2: Variance Rules & Sums
          </a>
        </div>
      </div>
    </div>
  </div>
</section>