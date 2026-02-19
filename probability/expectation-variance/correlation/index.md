---
layout: default
title: "4. Correlation"
description: "Correlation is standardized covariance. It measures strength and direction of linear relationship and removes scale dependence."
permalink: /probability/expectation-variance/correlation/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem; letter-spacing:0.5px;">🚧 Lesson Under Construction</h2>
      <p style="margin:0; font-size:1.05rem; color:#5d4037; line-height:1.6;">
        Version 0 establishes the formal definition and interpretation of correlation.
        Visual intuition and real data examples will be added later.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update "last visited lesson" for Probability Block 4 -->
<script>
  (function () {
    var KEY = "esa_continue_probability_expectation_variance_lesson_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/probability/expectation-variance/correlation/",
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
        <span class="badge">Standardized</span>
      </div>

      <h1>4. Correlation</h1>
      <p class="lead">
        Covariance measures joint movement but depends on scale.
        Correlation removes scale and produces a standardized measure
        between −1 and 1.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/probability/expectation-variance/">Back to Block 4</a>
        <a class="btn btn-outline" href="/probability/">Probability home</a>
      </div>

      <p class="muted-mini">
        Key message: correlation measures strength and direction of linear relationship.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      By the end of this lesson, you should be able to define correlation,
      interpret its magnitude and sign, and understand its limitations.
    </p>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Key definition</h2>
      <p style="margin:0; font-size:1.1rem;">
        <strong>Corr(X,Y) = Cov(X,Y) / (σ_X σ_Y)</strong>
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Why standardize covariance?</h2>
    <p>
      Covariance depends on measurement units.
      If we change scale, covariance changes.
    </p>
  </div>

  <div class="card">
    <p>
      Correlation divides by standard deviations,
      making it unit-free and comparable across contexts.
    </p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Range of correlation</h2>
  </div>

  <div class="card">
    <p style="margin:0; font-size:1.1rem;">
      <strong>−1 ≤ Corr(X,Y) ≤ 1</strong>
    </p>
  </div>

  <div class="grid grid-3" style="margin-top:1rem;">
    <div class="card">
      <h3>Corr = 1</h3>
      <p>Perfect positive linear relationship.</p>
    </div>

    <div class="card">
      <h3>Corr = −1</h3>
      <p>Perfect negative linear relationship.</p>
    </div>

    <div class="card">
      <h3>Corr = 0</h3>
      <p>No linear relationship (not necessarily independence).</p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Interpretation of magnitude</h2>
  </div>

  <div class="card">
    <ul class="bullets">
      <li>Close to 1 → strong positive linear association</li>
      <li>Close to −1 → strong negative linear association</li>
      <li>Close to 0 → weak linear association</li>
    </ul>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    Correlation measures linear strength only.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Important warnings</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Correlation ≠ Causation</h3>
      <p>
        A high correlation does not imply that one variable causes the other.
      </p>
    </div>

    <div class="card">
      <h3>Zero correlation ≠ Independence</h3>
      <p>
        Variables may have nonlinear dependence even when correlation is zero.
      </p>
    </div>

    <div class="card">
      <h3>Sensitive to outliers</h3>
      <p>
        A single extreme observation can dramatically change correlation.
      </p>
    </div>

    <div class="card">
      <h3>Only linear structure</h3>
      <p>
        Strong nonlinear relationships can produce small correlation.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Structural role in variance</h2>
  </div>

  <div class="card">
    <p style="margin:0;">
      Using correlation, the variance of a sum becomes:
    </p>
    <p style="margin-top:.5rem; font-size:1.1rem;">
      <strong>Var(X+Y) = Var(X) + Var(Y) + 2ρσ_Xσ_Y</strong>
    </p>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    where ρ = Corr(X,Y).
  </p>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Common mistakes</h2>
      <ul class="bullets">
        <li>Confusing covariance and correlation</li>
        <li>Interpreting correlation as causation</li>
        <li>Ignoring nonlinear relationships</li>
        <li>Assuming zero correlation implies independence</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Define correlation formally</li>
        <li>Interpret magnitude and direction</li>
        <li>Understand its limits</li>
        <li>Be ready to use indicator variables next</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">
        Now we introduce indicator random variables —
        one of the most powerful tools for counting and modeling.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/probability/expectation-variance/indicator-random-variables/">
          Next lesson: 5. Indicator Random Variables →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/probability/expectation-variance/covariance/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 3: Covariance
          </a>
        </div>
      </div>
    </div>
  </div>
</section>