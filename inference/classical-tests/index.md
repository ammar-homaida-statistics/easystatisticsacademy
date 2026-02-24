<!-- =========================================================
BLOCK 4 — CLASSICAL TESTS
File: /inference/classical-tests/index.md
========================================================= -->
---
layout: default
title: Block 4 — Classical Tests
description: Learn the classical hypothesis tests used everywhere: z and t tests, chi-square tests, ANOVA (F tests), and the core assumptions and interpretations behind them.
permalink: /inference/classical-tests/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem; letter-spacing:0.5px;">
        🚧 This Block Is Under Construction
      </h2>
      <p style="margin:0; font-size:1.05rem; color:#5d4037; line-height:1.6;">
        This block covers the <strong>classical hypothesis tests</strong> that form the standard inference toolkit:
        tests for means and proportions (z/t), tests for categorical relationships (chi-square),
        and group comparisons via <strong>F tests</strong> (ANOVA). The emphasis is on correct assumptions,
        correct interpretation, and clean decision logic.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update "last visited block" -->
<script>
  (function () {
    var KEY = "esa_continue_inference_last_block_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/classical-tests/",
      label: "Block 4 — Classical Tests",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card hero-split">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 4</span>
        <span class="badge">z / t</span>
        <span class="badge">χ²</span>
        <span class="badge">F / ANOVA</span>
      </div>

      <h1>Block 4 — Classical Tests</h1>
      <p class="lead">
        Classical tests are standardized procedures with known sampling distributions.
        This block teaches the main tests used in research and practice and clarifies
        what each test answers, what it assumes, and how to interpret results responsibly.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/">Back to Statistical Inference</a>
        <a class="btn" href="#lessons">Open structure</a>
      </div>

      <p class="muted-mini">
        Version 0: structure is locked. Lessons will expand without changing URLs or order.
      </p>
    </div>

    <div class="hero-panel">
      <div class="panel-card">
        <h2 class="panel-title">What this block covers</h2>
        <ul class="quickstart" style="list-style:none; padding-left:0; margin:0;">
          <li style="margin:.35rem 0;"><strong>One-sample tests</strong><span class="meta">Mean, proportion, paired mean</span></li>
          <li style="margin:.35rem 0;"><strong>Two-sample tests</strong><span class="meta">Independent means, two proportions</span></li>
          <li style="margin:.35rem 0;"><strong>Chi-square tests</strong><span class="meta">GOF, independence, homogeneity</span></li>
          <li style="margin:.35rem 0;"><strong>ANOVA (F tests)</strong><span class="meta">Compare 3+ means</span></li>
          <li style="margin:.35rem 0;"><strong>Assumptions</strong><span class="meta">Independence, normality, equal variance</span></li>
          <li style="margin:.35rem 0;"><strong>Interpretation</strong><span class="meta">p-values, effect size, reporting</span></li>
        </ul>
      </div>
    </div>
  </div>
</section>

<!-- ✅ Continue Reading (lesson-level placeholder key for this block) -->
<section class="section" id="continue-reading-block4" style="display:none;">
  <div class="callout">
    <div class="callout-copy">
      <h2>Continue reading</h2>
      <p class="muted-mini" id="continue-reading-block4-label" style="margin:0 0 .75rem 0;"></p>
      <a class="btn" id="continue-reading-block4-btn" href="#">Continue</a>
    </div>
  </div>
</section>

<section class="section" id="lessons">
  <div class="section-head">
    <h2>Lessons (Version 0)</h2>
    <p>
      Lessons are published in a stable order to keep the toolkit coherent.
      The list below is the permanent structure for this block.
    </p>
  </div>

  <div class="grid grid-2">

    <!-- Lesson 1 -->
    <div class="card lesson-card">
      <h3><a href="/inference/classical-tests/decision-framework-and-assumptions/">1. Decision Framework and Assumptions (Quick Review)</a></h3>
      <p>How classical tests fit into H₀/H₁, test statistic, p-value, α, and the assumptions that make tests valid.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/inference/classical-tests/decision-framework-and-assumptions/">Open lesson</a>
      </div>
    </div>

    <!-- Lesson 2 -->
    <div class="card lesson-card">
      <h3><a href="/inference/classical-tests/one-sample-z-test-for-mean/">2. One-Sample z Test for a Mean (σ Known)</a></h3>
      <p>Rare but clarifying: testing a mean when σ is known; connects directly to the z interval.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/inference/classical-tests/one-sample-z-test-for-mean/">Open lesson</a>
      </div>
    </div>

    <!-- Lesson 3 -->
    <div class="card lesson-card">
      <h3><a href="/inference/classical-tests/one-sample-t-test-for-mean/">3. One-Sample t Test for a Mean (σ Unknown)</a></h3>
      <p>The standard mean test: t statistic, df = n−1, and interpretation beyond “significant/not”.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/inference/classical-tests/one-sample-t-test-for-mean/">Open lesson</a>
      </div>
    </div>

    <!-- Lesson 4 -->
    <div class="card lesson-card">
      <h3><a href="/inference/classical-tests/paired-t-test/">4. Paired t Test (Mean of Differences)</a></h3>
      <p>Matched/paired designs reduced to one-sample testing on difference scores.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/inference/classical-tests/paired-t-test/">Open lesson</a>
      </div>
    </div>

    <!-- Lesson 5 -->
    <div class="card lesson-card">
      <h3><a href="/inference/classical-tests/two-sample-t-test-independent/">5. Two-Sample t Test (Independent Samples)</a></h3>
      <p>Testing difference of means: Welch default vs pooled variance (preview), assumptions, interpretation.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/inference/classical-tests/two-sample-t-test-independent/">Open lesson</a>
      </div>
    </div>

    <!-- Lesson 6 -->
    <div class="card lesson-card">
      <h3><a href="/inference/classical-tests/one-proportion-z-test/">6. One-Proportion z Test</a></h3>
      <p>Testing a single proportion with normal approximation and the success–failure condition.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/inference/classical-tests/one-proportion-z-test/">Open lesson</a>
      </div>
    </div>

    <!-- Lesson 7 -->
    <div class="card lesson-card">
      <h3><a href="/inference/classical-tests/two-proportion-z-test/">7. Two-Proportion z Test</a></h3>
      <p>Compare two proportions; pooled proportion under H₀; conditions and interpretation.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/inference/classical-tests/two-proportion-z-test/">Open lesson</a>
      </div>
    </div>

    <!-- Lesson 8 -->
    <div class="card lesson-card">
      <h3><a href="/inference/classical-tests/chi-square-goodness-of-fit/">8. Chi-Square Goodness-of-Fit Test</a></h3>
      <p>Testing whether categorical counts match a hypothesized distribution; expected counts and validity rules.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/inference/classical-tests/chi-square-goodness-of-fit/">Open lesson</a>
      </div>
    </div>

    <!-- Lesson 9 -->
    <div class="card lesson-card">
      <h3><a href="/inference/classical-tests/chi-square-independence-test/">9. Chi-Square Test of Independence</a></h3>
      <p>Association between two categorical variables via contingency tables; expected counts and effect size (Cramér’s V).</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/inference/classical-tests/chi-square-independence-test/">Open lesson</a>
      </div>
    </div>

    <!-- Lesson 10 -->
    <div class="card lesson-card">
      <h3><a href="/inference/classical-tests/chi-square-homogeneity-test/">10. Chi-Square Test of Homogeneity</a></h3>
      <p>Compare categorical distributions across populations/groups; same statistic, different study design logic.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/inference/classical-tests/chi-square-homogeneity-test/">Open lesson</a>
      </div>
    </div>

    <!-- Lesson 11 -->
    <div class="card lesson-card">
      <h3><a href="/inference/classical-tests/one-way-anova-f-test/">11. One-Way ANOVA (F Test for 3+ Means)</a></h3>
      <p>Compare 3+ group means with F; between vs within variability; what ANOVA can and cannot conclude.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/inference/classical-tests/one-way-anova-f-test/">Open lesson</a>
      </div>
    </div>

    <!-- Lesson 12 -->
    <div class="card lesson-card">
      <h3><a href="/inference/classical-tests/post-hoc-tests-and-multiple-comparisons-preview/">12. Post-hoc Tests and Multiple Comparisons (Preview)</a></h3>
      <p>Why multiple comparisons inflate false positives; preview of adjustments (Bonferroni, Tukey) and interpretation.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/inference/classical-tests/post-hoc-tests-and-multiple-comparisons-preview/">Open lesson</a>
      </div>
    </div>

  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of Block 4</h2>
      <ul class="bullets">
        <li>Select the correct classical test for the question and data type</li>
        <li>State hypotheses correctly and identify the relevant sampling distribution</li>
        <li>Check conditions and interpret p-values responsibly</li>
        <li>Report results with context (effect size, direction, and limitations)</li>
      </ul>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Next block</div>
        <div class="mini-body">
          Continue to
          <a href="/inference/power-sample-size/" style="color:#1a73e8; text-decoration:underline;">
            <strong>Block 5 — Power and Sample Size</strong>
          </a>.
        </div>
      </div>
    </div>

  </div>
</section>

<!-- ✅ Continue Reading Script (lesson-level) -->
<script>
  (function () {
    var KEY = "esa_continue_inference_classical_tests_lesson_v0";
    var raw = localStorage.getItem(KEY);
    if (!raw) return;

    try {
      var data = JSON.parse(raw);
      if (!data || !data.url || !data.label) return;

      var wrap = document.getElementById("continue-reading-block4");
      var label = document.getElementById("continue-reading-block4-label");
      var btn = document.getElementById("continue-reading-block4-btn");
      if (!wrap || !label || !btn) return;

      label.innerHTML = 'You last visited: <strong>' + data.label + '</strong>';
      btn.href = data.url;
      wrap.style.display = "block";
    } catch (e) {}
  })();
</script>