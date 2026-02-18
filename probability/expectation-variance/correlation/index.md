---
layout: default
title: "4. Correlation"
description: "Correlation rescales covariance into a unitless measure in [-1,1] and clarifies what 'strength of linear association' means."
permalink: /probability/expectation-variability/correlation/
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
      url: "/probability/expectation-variability/correlation/",
      label: "Lesson 4 — Correlation",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">

      <div class="badge-row">
        <span class="badge">Block 4</span>
        <span class="badge">Lesson 4</span>
        <span class="badge">Correlation</span>
        <span class="badge">Interpretation</span>
      </div>

      <h1>4. Correlation</h1>

      <p class="lead">
        Correlation measures the strength and direction of linear association.
        This lesson clarifies what correlation does (and does not) tell you — and why it is not causation.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/probability/expectation-variability/covariance/">
          ← Previous lesson: 3. Covariance
        </a>
        <a class="btn btn-outline" href="/probability/expectation-variability/">Back to Block 4</a>
      </div>

      <p class="muted-mini">
        Correlation is standardized covariance — unitless and comparable across variables.
      </p>

    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">
        Next, we use indicator random variables to simplify counting and probability problems (a key trick in expectation).
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/probability/expectation-variability/indicator-random-variables/">
          Next lesson: 5. Indicator Random Variables →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/probability/expectation-variability/covariance/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 3: Covariance
          </a>
        </div>
      </div>
    </div>
  </div>
</section>