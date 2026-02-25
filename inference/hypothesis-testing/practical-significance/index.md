---
layout: default
title: "10. Statistical Significance vs Practical Significance"
description: "Distinguish statistical significance from practical importance and learn how effect size and context determine real-world meaning."
permalink: /inference/hypothesis-testing/practical-significance/
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
        Version 0 clarifies the conceptual distinction between statistical significance
        and practical importance. Applied case studies and reporting templates will be added later.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update continue-reading keys -->
<script>
  (function () {
    var KEY = "esa_continue_inference_hypothesis_testing_lesson_v0";

    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/hypothesis-testing/practical-significance/",
      label: "Lesson 10 — Statistical vs Practical Significance",
      ts: Date.now()
    }));

    localStorage.setItem("esa_continue_inference_last_block_v0", JSON.stringify({
      url: "/inference/hypothesis-testing/",
      label: "Block 3 — Hypothesis Testing",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 3</span>
        <span class="badge">Lesson 10</span>
        <span class="badge">Effect Size</span>
        <span class="badge">Interpretation</span>
      </div>

      <h1>10. Statistical Significance vs Practical Significance</h1>

      <p class="lead">
        A small p-value tells us that the data are unlikely under the null model.
        It does <strong>not</strong> tell us whether the effect is large, meaningful,
        or important in practice.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/hypothesis-testing/">Back to Block 3</a>
        <a class="btn btn-outline" href="/inference/">Statistical Inference home</a>
      </div>

      <p class="muted-mini">
        Significance is about evidence. Importance is about magnitude and context.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      Distinguish statistical significance from practical significance,
      interpret effect sizes, and avoid misleading conclusions based solely on p-values.
    </p>
  </div>

  <div class="callout">
    <div class="callout-copy">
      <h2>Core distinction</h2>
      <p style="margin:0;">
        Statistical significance answers:
        “Is the effect likely nonzero?”
        <br><br>
        Practical significance answers:
        “Is the effect large enough to matter?”
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Why small effects become significant</h2>
  </div>

  <div class="card">
    \[
    \text{Test statistic}
    =
    \frac{\text{Effect size}}{\text{Standard Error}}
    \]
  </div>

  <p style="margin-top:.75rem;">
    As sample size \(n\) increases, the standard error decreases.
    Even very small effects can produce large test statistics
    and small p-values.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Effect size measures</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Mean difference</h3>
      <p style="margin:0;">
        Raw difference \( \bar{X}_1 - \bar{X}_2 \)
      </p>
    </div>

    <div class="card">
      <h3>Standardized effect</h3>
      <p style="margin:0;">
        Cohen’s \( d = \frac{\bar{X}_1 - \bar{X}_2}{S} \)
      </p>
    </div>

    <div class="card">
      <h3>Proportions</h3>
      <p style="margin:0;">
        Risk difference or risk ratio
      </p>
    </div>

    <div class="card">
      <h3>Regression</h3>
      <p style="margin:0;">
        Slope magnitude and standardized coefficients
      </p>
    </div>
  </div>

  <p class="muted-mini">
    Effect size quantifies magnitude independent of sample size.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Confidence intervals and importance</h2>
  </div>

  <div class="card">
    A confidence interval shows a range of plausible effect sizes.
    If the entire interval lies within a practically negligible range,
    the effect may be statistically significant but practically trivial.
  </div>

  <p class="muted-mini">
    Interpretation must consider both magnitude and uncertainty.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Large sample vs small sample scenarios</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Large sample</h3>
      <ul class="bullets">
        <li>Tiny effects may be significant</li>
        <li>Risk of overstating importance</li>
      </ul>
    </div>

    <div class="card">
      <h3>Small sample</h3>
      <ul class="bullets">
        <li>Moderate effects may not be significant</li>
        <li>Risk of missing meaningful differences</li>
      </ul>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Responsible reporting</h2>
  </div>

  <div class="card">
    A complete report should include:
    <ul class="bullets">
      <li>Estimated effect size</li>
      <li>Confidence interval</li>
      <li>p-value</li>
      <li>Contextual interpretation</li>
    </ul>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Distinguish statistical and practical significance</li>
        <li>Interpret effect sizes properly</li>
        <li>Understand sample size impact</li>
        <li>Report results responsibly</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next block</h2>
      <p style="margin:0;">
        Now we move from testing logic to
        specific classical hypothesis tests.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/inference/classical-tests/">
          Continue to Block 4 — Classical Tests →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/inference/hypothesis-testing/ci-and-test-connection/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 9: CI and Test Connection
          </a>
        </div>
      </div>
    </div>
  </div>
</section>