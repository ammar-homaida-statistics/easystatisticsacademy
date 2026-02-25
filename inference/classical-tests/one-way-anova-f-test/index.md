---
layout: default
title: "11. One-Way ANOVA (F Test)"
description: "Conduct and interpret the one-way ANOVA F test to compare the means of three or more independent groups."
permalink: /inference/classical-tests/one-way-anova-f-test/
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
        Version 0 establishes the core ANOVA logic and F-statistic structure.
        Detailed numeric examples and software walkthroughs will be added later.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update continue-reading keys -->
<script>
  (function () {
    var KEY = "esa_continue_inference_classical_tests_lesson_v0";

    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/classical-tests/one-way-anova-f-test/",
      label: "Lesson 11 — One-Way ANOVA (F Test)",
      ts: Date.now()
    }));

    localStorage.setItem("esa_continue_inference_last_block_v0", JSON.stringify({
      url: "/inference/classical-tests/",
      label: "Block 4 — Classical Tests",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 4</span>
        <span class="badge">Lesson 11</span>
        <span class="badge">ANOVA</span>
        <span class="badge">F Test</span>
      </div>

      <h1>11. One-Way ANOVA (F Test)</h1>

      <p class="lead">
        One-way ANOVA tests whether three or more independent population means
        are equal by comparing variability <strong>between groups</strong>
        to variability <strong>within groups</strong>.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/classical-tests/">Back to Block 4</a>
        <a class="btn btn-outline" href="/inference/">Statistical Inference home</a>
      </div>

      <p class="muted-mini">
        ANOVA generalizes the two-sample t test to multiple groups.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      Formulate ANOVA hypotheses, compute the F statistic,
      and interpret the comparison of between-group and within-group variability.
    </p>
  </div>

  <div class="callout">
    <div class="callout-copy">
      <h2>When to use ANOVA</h2>
      <p style="margin:0;">
        Use one-way ANOVA when:
        <br>
        • There are three or more independent groups  
        • The response variable is quantitative  
        • Group membership defines a single categorical factor  
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Hypotheses</h2>
  </div>

  <div class="card">
    \[
    H_0: \mu_1 = \mu_2 = \dots = \mu_k
    \]
  </div>

  <div class="card" style="margin-top:1rem;">
    \[
    H_1:\ \text{At least one mean differs}
    \]
  </div>

  <p class="muted-mini">
    The alternative does not specify which means differ.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Variance decomposition</h2>
  </div>

  <div class="card">
    Total variability =
    <br><br>
    Between-group variability +
    Within-group variability
  </div>

  <p>
    ANOVA partitions the total sum of squares:
  </p>

  <div class="card">
    \[
    SS_{Total} = SS_{Between} + SS_{Within}
    \]
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Mean squares</h2>
  </div>

  <div class="card">
    \[
    MS_{Between} = \frac{SS_{Between}}{k - 1}
    \]
  </div>

  <div class="card" style="margin-top:1rem;">
    \[
    MS_{Within} = \frac{SS_{Within}}{n - k}
    \]
  </div>

  <p class="muted-mini">
    Where:
    <br>
    • \(k\) = number of groups  
    • \(n\) = total sample size  
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) F statistic</h2>
  </div>

  <div class="card">
    \[
    F =
    \frac{MS_{Between}}{MS_{Within}}
    \]
  </div>

  <p>
    Under \(H_0\):
    \[
    F \sim F_{k-1,\, n-k}
    \]
  </p>

  <p class="muted-mini">
    Large F values indicate greater between-group variation
    relative to within-group variation.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Assumptions</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Independence</h3>
      <p>Observations are independent within and across groups.</p>
    </div>

    <div class="card">
      <h3>Normality</h3>
      <p>Residuals are approximately normally distributed.</p>
    </div>

    <div class="card">
      <h3>Equal variances</h3>
      <p>Population variances are approximately equal across groups.</p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>6) Interpretation</h2>
  </div>

  <div class="card">
    A small p-value indicates that not all group means are equal.
  </div>

  <p class="muted-mini">
    ANOVA tells us that a difference exists —
    not which groups differ.
  </p>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Formulate ANOVA hypotheses</li>
        <li>Understand variance decomposition</li>
        <li>Compute and interpret the F statistic</li>
        <li>Recognize ANOVA assumptions</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next lesson</h2>
      <p style="margin:0;">
        If ANOVA is significant,
        we must determine which groups differ.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/inference/classical-tests/post-hoc-tests-and-multiple-comparisons-preview/">
          Next lesson: 12. Post-Hoc Tests & Multiple Comparisons →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/inference/classical-tests/chi-square-homogeneity-test/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 10: Chi-Square Homogeneity Test
          </a>
        </div>
      </div>
    </div>
  </div>
</section>