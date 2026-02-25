---
layout: default
title: "12. Post-Hoc Tests and Multiple Comparisons (Preview)"
description: "Understand why post-hoc tests are needed after ANOVA and how multiple comparisons affect Type I error."
permalink: /inference/classical-tests/post-hoc-tests-and-multiple-comparisons-preview/
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
        Version 0 introduces the logic of post-hoc testing and multiple-comparison control.
        Detailed procedures and software demonstrations will be added later.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update continue-reading keys -->
<script>
  (function () {
    var KEY = "esa_continue_inference_classical_tests_lesson_v0";

    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/classical-tests/post-hoc-tests-and-multiple-comparisons-preview/",
      label: "Lesson 12 — Post-Hoc Tests & Multiple Comparisons",
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
        <span class="badge">Lesson 12</span>
        <span class="badge">ANOVA</span>
        <span class="badge">Multiple Comparisons</span>
      </div>

      <h1>12. Post-Hoc Tests and Multiple Comparisons (Preview)</h1>

      <p class="lead">
        When ANOVA rejects the null hypothesis,
        we know that not all means are equal —
        but we do not yet know <strong>which</strong> means differ.
        Post-hoc procedures address this question
        while controlling error rates.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/classical-tests/">Back to Block 4</a>
        <a class="btn btn-outline" href="/inference/">Statistical Inference home</a>
      </div>

      <p class="muted-mini">
        Multiple testing inflates Type I error if not controlled.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      Understand why post-hoc tests are necessary,
      how multiple comparisons inflate Type I error,
      and how adjustment procedures control it.
    </p>
  </div>

  <div class="callout">
    <div class="callout-copy">
      <h2>Core problem</h2>
      <p style="margin:0;">
        Performing many pairwise t tests increases
        the probability of at least one false positive.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Why ANOVA is not enough</h2>
  </div>

  <div class="card">
    ANOVA tests:
    <br><br>
    \[
    H_0: \mu_1 = \mu_2 = \dots = \mu_k
    \]
  </div>

  <p>
    A significant F statistic indicates that
    at least one mean differs,
    but does not specify which pair(s) differ.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Multiple comparisons problem</h2>
  </div>

  <div class="card">
    If k groups exist,
    the number of pairwise comparisons is:
    <br><br>
    \[
    \frac{k(k-1)}{2}
    \]
  </div>

  <p>
    Each additional test increases
    the overall probability of a Type I error
    across the family of tests.
  </p>

  <div class="card" style="margin-top:1rem;">
    Familywise error rate (FWER):
    <br><br>
    Probability of at least one false rejection.
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Adjustment strategies</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Bonferroni correction</h3>
      <p>
        Use adjusted significance level:
        <br>
        \[
        \alpha^* = \frac{\alpha}{m}
        \]
        where m = number of comparisons.
      </p>
    </div>

    <div class="card">
      <h3>Tukey’s HSD</h3>
      <p>
        Designed for pairwise comparisons
        while maintaining overall error control.
      </p>
    </div>

    <div class="card">
      <h3>Holm method</h3>
      <p>
        Sequential adjustment
        less conservative than Bonferroni.
      </p>
    </div>

    <div class="card">
      <h3>False discovery rate</h3>
      <p>
        Controls expected proportion of false discoveries
        among rejected hypotheses.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Interpretation</h2>
  </div>

  <div class="card">
    Post-hoc tests identify
    which specific group means differ
    while maintaining control over error rates.
  </div>

  <p class="muted-mini">
    Choice of adjustment depends on research goals
    and tolerance for Type I error.
  </p>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Recognize the multiple testing problem</li>
        <li>Understand familywise error rate</li>
        <li>Know major adjustment methods</li>
        <li>Understand the role of post-hoc tests after ANOVA</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next block</h2>
      <p style="margin:0;">
        We now move to planning studies:
        statistical power and required sample size.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/inference/power-sample-size/">
          Next block: Block 5 — Power & Sample Size →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/inference/classical-tests/one-way-anova-f-test/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 11: One-Way ANOVA (F Test)
          </a>
        </div>
      </div>
    </div>
  </div>
</section>