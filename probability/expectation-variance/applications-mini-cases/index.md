---
layout: default
title: "6. Applications — Mini Cases"
description: "Integrated applications combining expectation, variance, covariance, correlation, and indicator variables in realistic probability modeling scenarios."
permalink: /probability/expectation-variance/applications-mini-cases/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem; letter-spacing:0.5px;">🚧 Lesson Under Construction</h2>
      <p style="margin:0; font-size:1.05rem; color:#5d4037; line-height:1.6;">
        Version 0 integrates all tools from Block 4 conceptually.
        Full numerical worked examples and simulations will be added later.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update last visited lesson -->
<script>
  (function () {
    var KEY = "esa_continue_probability_expectation_variance_lesson_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/probability/expectation-variance/applications-mini-cases/",
      label: "Lesson 6 — Applications: Mini Cases",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 4</span>
        <span class="badge">Lesson 6</span>
        <span class="badge">Applications</span>
        <span class="badge">Integration</span>
      </div>

      <h1>6. Applications — Mini Cases</h1>

      <p class="lead">
        This lesson integrates expectation, variance, covariance, correlation,
        and indicator variables into realistic modeling situations.
        The goal is structural understanding — not memorization.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/probability/expectation-variance/">Back to Block 4</a>
        <a class="btn btn-outline" href="/probability/">Probability home</a>
      </div>

      <p class="muted-mini">
        Modeling principle: break problems into components, then apply the right tool.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      By the end of this lesson, you should be able to identify which structural tool
      (linearity, variance rules, covariance, correlation, indicators)
      applies in a modeling scenario.
    </p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Mini Case 1 — Counting Successes</h2>
  </div>

  <div class="card">
    <p>
      Suppose multiple events may occur.
      Define indicator variables for each event.
      Write total count as:
    </p>

    <p style="font-size:1.1rem;">
      <strong>X = I₁ + I₂ + … + I_n</strong>
    </p>

    <p>
      Then:
      <strong>E[X] = Σ P(Aᵢ)</strong>
    </p>
  </div>

  <p class="muted-mini">
    Independence is not required. This is pure linearity.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>Mini Case 2 — Variability of a Sum</h2>
  </div>

  <div class="card">
    <p>
      For two variables:
    </p>

    <p style="font-size:1.1rem;">
      <strong>Var(X + Y) = Var(X) + Var(Y) + 2Cov(X,Y)</strong>
    </p>

    <p>
      If independent → covariance = 0 → variances add.
    </p>
  </div>

  <p class="muted-mini">
    Dependence influences spread, not expectation.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>Mini Case 3 — Portfolio Interpretation</h2>
  </div>

  <div class="card">
    <p>
      In finance-like models:
    </p>

    <ul class="bullets">
      <li>Expectation → average return</li>
      <li>Variance → risk</li>
      <li>Covariance → joint movement</li>
      <li>Correlation → standardized dependence</li>
    </ul>
  </div>

  <p class="muted-mini">
    This is the structural backbone of regression and machine learning.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>Mini Case 4 — Random Structure Modeling</h2>
  </div>

  <div class="card">
    <p>
      Complex quantities are often decomposed as:
    </p>

    <ul class="bullets">
      <li>Sum of components</li>
      <li>Function of random variables</li>
      <li>Combination of dependent parts</li>
    </ul>

    <p>
      The correct tool depends on structure:
    </p>

    <ul class="bullets">
      <li>Need mean only? → Linearity</li>
      <li>Need spread? → Variance rules</li>
      <li>Need joint behavior? → Covariance</li>
      <li>Need standardized dependence? → Correlation</li>
      <li>Need counting? → Indicators</li>
    </ul>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Structural takeaway</h2>
      <ul class="bullets">
        <li>Expectation is linear.</li>
        <li>Variance is quadratic.</li>
        <li>Dependence enters through covariance.</li>
        <li>Indicators turn events into algebra.</li>
        <li>All modeling starts with decomposition.</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of Block 4</h2>
      <ul class="bullets">
        <li>Confident use of linearity of expectation</li>
        <li>Correct application of variance rules</li>
        <li>Understanding covariance and correlation</li>
        <li>Mastery of indicator variable technique</li>
        <li>Readiness for Named Distributions (Block 5)</li>
      </ul>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Next block</div>
        <div class="mini-body">
          <a href="/probability/distributions/" style="color:#1a73e8; text-decoration:underline;">
            Block 5 — Common Distributions
          </a>
        </div>
      </div>
    </div>
  </div>
</section>