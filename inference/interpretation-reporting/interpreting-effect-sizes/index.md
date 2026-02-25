---
layout: default
title: "4. Interpreting Effect Sizes"
description: "Understand how to interpret effect sizes, distinguish magnitude from significance, and explain practical meaning clearly."
permalink: /inference/interpretation-reporting/interpreting-effect-sizes/
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
        Version 0 introduces effect size interpretation across common test types.
        Context-based examples and applied reporting templates will be added later.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update continue-reading keys -->
<script>
  (function () {
    var KEY = "esa_continue_inference_interpretation_reporting_lesson_v0";

    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/interpretation-reporting/interpreting-effect-sizes/",
      label: "Lesson 4 — Interpreting Effect Sizes",
      ts: Date.now()
    }));

    localStorage.setItem("esa_continue_inference_last_block_v0", JSON.stringify({
      url: "/inference/interpretation-reporting/",
      label: "Block 6 — Interpretation & Reporting",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 6</span>
        <span class="badge">Lesson 4</span>
        <span class="badge">Effect Size</span>
        <span class="badge">Magnitude</span>
      </div>

      <h1>4. Interpreting Effect Sizes</h1>

      <p class="lead">
        Effect size quantifies the magnitude of a difference or association.
        It answers “How large is the effect?” — not merely “Is it detectable?”
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/interpretation-reporting/">Back to Block 6</a>
        <a class="btn btn-outline" href="/inference/">Statistical Inference home</a>
      </div>

      <p class="muted-mini">
        Magnitude interpretation requires context, not only numeric thresholds.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      Identify common effect size measures,
      interpret their magnitude correctly,
      and connect them to substantive meaning.
    </p>
  </div>

  <div class="callout">
    <div class="callout-copy">
      <h2>Core principle</h2>
      <p style="margin:0;">
        Statistical significance depends on sample size.  
        Effect size reflects magnitude independent of sample size.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Mean differences</h2>
  </div>

  <div class="card">
    Raw difference:
    \[
    \Delta = \mu_1 - \mu_2
    \]
  </div>

  <div class="card" style="margin-top:1rem;">
    Standardized effect size (Cohen's d):
    \[
    d = \frac{\mu_1 - \mu_2}{\sigma}
    \]
  </div>

  <p>
    Interpretation depends on domain context.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Proportion differences</h2>
  </div>

  <div class="card">
    Absolute difference:
    \[
    \Delta = p_1 - p_2
    \]
  </div>

  <div class="card" style="margin-top:1rem;">
    Risk ratio:
    \[
    RR = \frac{p_1}{p_2}
    \]
  </div>

  <p>
    Relative measures may appear large even if absolute differences are small.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Association measures</h2>
  </div>

  <div class="card">
    Correlation:
    \[
    r \in [-1, 1]
    \]
  </div>

  <div class="card" style="margin-top:1rem;">
    Chi-square effect size (Cramér's V):
    \[
    V = \sqrt{\frac{\chi^2}{n(k-1)}}
    \]
  </div>

  <p>
    Effect sizes quantify strength of association, not causality.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Avoid mechanical thresholds</h2>
  </div>

  <div class="card">
    Generic labels such as:
    <br><br>
    small, medium, large
  </div>

  <p>
    are rough conventions and should not replace contextual judgment.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Practical interpretation</h2>
  </div>

  <div class="card">
    Better reporting example:
    <br><br>
    “The intervention increased average test scores by 4 points,
    representing approximately 0.5 standard deviations.”
  </div>

  <p>
    Always explain magnitude in real-world units whenever possible.
  </p>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Identify common effect size measures</li>
        <li>Separate magnitude from significance</li>
        <li>Avoid mechanical threshold thinking</li>
        <li>Interpret effect sizes in context</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next lesson</h2>
      <p style="margin:0;">
        We now examine the problem of multiple testing
        and false positives.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/inference/interpretation-reporting/multiple-testing-and-false-positives/">
          Next lesson: 5. Multiple Testing & False Positives →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/inference/interpretation-reporting/interpreting-confidence-intervals/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 3: Interpreting Confidence Intervals
          </a>
        </div>
      </div>
    </div>
  </div>
</section>