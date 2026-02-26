---
layout: default
title: "7. Robust and Nonparametric Alternatives"
description: "Explore robust and nonparametric methods that reduce sensitivity to distributional assumptions, outliers, and variance violations."
permalink: /inference/assumptions-robustness/robust-alternatives-nonparametric/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem; letter-spacing:0.5px;">
        🚧 Lesson Under Construction
      </h2>
      <p style="margin:0; font-size:1.05rem; color:#5d4037; line-height:1.6;">
        Version 0 introduces robust estimators and nonparametric tests
        as principled responses to assumption violations.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update continue-reading keys -->
<script>
  (function () {
    var KEY = "esa_continue_inference_assumptions_robustness_lesson_v0";

    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/assumptions-robustness/robust-alternatives-nonparametric/",
      label: "Lesson 7 — Robust & Nonparametric Alternatives",
      ts: Date.now()
    }));

    localStorage.setItem("esa_continue_inference_last_block_v0", JSON.stringify({
      url: "/inference/assumptions-robustness/",
      label: "Block 7 — Assumptions & Robustness",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 7</span>
        <span class="badge">Lesson 7</span>
        <span class="badge">Robust</span>
        <span class="badge">Nonparametric</span>
      </div>

      <h1>7. Robust and Nonparametric Alternatives</h1>

      <p class="lead">
        When classical assumptions fail substantially,
        robust and nonparametric methods provide stable inference
        without relying heavily on normality or equal variances.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/assumptions-robustness/">Back to Block 7</a>
        <a class="btn btn-outline" href="/inference/">Statistical Inference home</a>
      </div>

      <p class="muted-mini">
        Robustness focuses on stability; nonparametrics focus on minimal assumptions.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      Understand the difference between robust and nonparametric approaches,
      and identify when alternative methods are preferable.
    </p>
  </div>

  <div class="callout">
    <div class="callout-copy">
      <h2>Core distinction</h2>
      <p style="margin:0;">
        Robust methods modify estimators or standard errors.  
        Nonparametric methods replace distributional assumptions entirely.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Robust estimators</h2>
  </div>

  <div class="card">
    Example: Median vs Mean  
    <br><br>
    Mean:
    \[
    \bar{X} = \frac{1}{n}\sum X_i
    \]
  </div>

  <div class="card" style="margin-top:1rem;">
    Median:
    <br><br>
    Resistant to extreme values.
  </div>

  <p>
    The median has a higher breakdown point than the mean.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Robust standard errors</h2>
  </div>

  <div class="card">
    Heteroscedasticity-robust variance:
    \[
    \widehat{Var}(\hat{\beta})_{\text{robust}}
    \]
  </div>

  <p>
    Adjusts inference without altering coefficient estimates.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Nonparametric tests</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Wilcoxon rank-sum</h3>
      <p>Alternative to two-sample t-test.</p>
    </div>

    <div class="card">
      <h3>Wilcoxon signed-rank</h3>
      <p>Alternative to paired t-test.</p>
    </div>

    <div class="card">
      <h3>Kruskal–Wallis</h3>
      <p>Alternative to one-way ANOVA.</p>
    </div>

    <div class="card">
      <h3>Spearman correlation</h3>
      <p>Rank-based correlation measure.</p>
    </div>
  </div>

  <p class="muted-mini">
    These methods rely on ranks rather than distributional form.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Trade-offs</h2>
  </div>

  <div class="card">
    Advantages:
    <br><br>
    • Less sensitive to outliers  
    • Fewer distributional assumptions  
  </div>

  <div class="card" style="margin-top:1rem;">
    Limitations:
    <br><br>
    • Sometimes lower power  
    • Harder parameter interpretation  
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Practical guideline</h2>
  </div>

  <div class="card">
    Recommended workflow:
    <br><br>
    1. Fit classical model  
    2. Diagnose assumptions  
    3. Compare with robust/nonparametric alternative  
    4. Evaluate stability of conclusions  
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Differentiate robust vs nonparametric approaches</li>
        <li>Understand rank-based alternatives</li>
        <li>Recognize breakdown point concept</li>
        <li>Apply alternative methods strategically</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next lesson</h2>
      <p style="margin:0;">
        We now examine the bootstrap —
        a flexible and powerful robustness tool.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/inference/assumptions-robustness/bootstrap-as-robust-tool/">
          Next lesson: 8. Bootstrap as a Robust Tool →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/inference/assumptions-robustness/outliers-and-influence/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 6: Outliers and Influence
          </a>
        </div>
      </div>
    </div>
  </div>
</section>