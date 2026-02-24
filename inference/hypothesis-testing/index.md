<!-- =========================================================
BLOCK 3 — HYPOTHESIS TESTING
File: /inference/hypothesis-testing/index.md
========================================================= -->
---
layout: default
title: Block 3 — Hypothesis Testing
description: Learn how statistical decisions are made using null hypotheses, test statistics, p-values, significance levels, and error control.
permalink: /inference/hypothesis-testing/
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
        This block develops <strong>hypothesis testing</strong> as a structured decision procedure:
        defining null and alternative hypotheses, computing test statistics,
        interpreting p-values, and controlling error rates.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update "last visited block" -->
<script>
  (function () {
    var KEY = "esa_continue_inference_last_block_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/hypothesis-testing/",
      label: "Block 3 — Hypothesis Testing",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card hero-split">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 3</span>
        <span class="badge">Testing</span>
        <span class="badge">p-values</span>
        <span class="badge">Decision rules</span>
      </div>

      <h1>Block 3 — Hypothesis Testing</h1>
      <p class="lead">
        Hypothesis testing formalizes statistical decision-making.
        This block teaches how to test claims about population parameters
        using structured logic, test statistics, and controlled error rates.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/">Back to Statistical Inference</a>
        <a class="btn" href="#lessons">Open structure</a>
      </div>

      <p class="muted-mini">
        Version 0: decision logic first. Computation and software added later.
      </p>
    </div>

    <div class="hero-panel">
      <div class="panel-card">
        <h2 class="panel-title">What this block covers</h2>
        <ul class="quickstart" style="list-style:none; padding-left:0; margin:0;">
          <li style="margin:.35rem 0;"><strong>Null & alternative</strong><span class="meta">Formal claim structure</span></li>
          <li style="margin:.35rem 0;"><strong>Test statistic</strong><span class="meta">Standardization logic</span></li>
          <li style="margin:.35rem 0;"><strong>p-value</strong><span class="meta">Tail probability under H₀</span></li>
          <li style="margin:.35rem 0;"><strong>α level</strong><span class="meta">Type I error control</span></li>
          <li style="margin:.35rem 0;"><strong>Error types</strong><span class="meta">Type I & Type II</span></li>
          <li style="margin:.35rem 0;"><strong>Connection to CIs</strong><span class="meta">Equivalence logic</span></li>
        </ul>
      </div>
    </div>
  </div>
</section>

<!-- Continue Reading -->
<section class="section" id="continue-reading-block3" style="display:none;">
  <div class="callout">
    <div class="callout-copy">
      <h2>Continue reading</h2>
      <p class="muted-mini" id="continue-reading-block3-label" style="margin:0 0 .75rem 0;"></p>
      <a class="btn" id="continue-reading-block3-btn" href="#">Continue</a>
    </div>
  </div>
</section>

<section class="section" id="lessons">
  <div class="section-head">
    <h2>Lessons (Version 0)</h2>
    <p>
      Lessons are ordered to build decision logic gradually.
      The structure below is permanent for this block.
    </p>
  </div>

  <div class="grid grid-2">

    <!-- 1 -->
    <div class="card lesson-card">
      <h3><a href="/inference/hypothesis-testing/what-is-a-hypothesis-test/">1. What Is a Hypothesis Test?</a></h3>
      <p>Decision-making under uncertainty: from interval estimation to formal testing.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/inference/hypothesis-testing/what-is-a-hypothesis-test/">Open lesson</a>
      </div>
    </div>

    <!-- 2 -->
    <div class="card lesson-card">
      <h3><a href="/inference/hypothesis-testing/null-and-alternative-hypotheses/">2. Null and Alternative Hypotheses</a></h3>
      <p>Equality in H₀, direction in H₁, and one- vs two-sided logic.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/inference/hypothesis-testing/null-and-alternative-hypotheses/">Open lesson</a>
      </div>
    </div>

    <!-- 3 -->
    <div class="card lesson-card">
      <h3><a href="/inference/hypothesis-testing/test-statistics-and-standardization/">3. Test Statistics and Standardization</a></h3>
      <p>Transforming an estimate into a standardized score.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/inference/hypothesis-testing/test-statistics-and-standardization/">Open lesson</a>
      </div>
    </div>

    <!-- 4 -->
    <div class="card lesson-card">
      <h3><a href="/inference/hypothesis-testing/p-value-meaning-and-logic/">4. The p-Value: Meaning and Logic</a></h3>
      <p>Probability of observing data at least as extreme under H₀.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/inference/hypothesis-testing/p-value-meaning-and-logic/">Open lesson</a>
      </div>
    </div>

    <!-- 5 -->
    <div class="card lesson-card">
      <h3><a href="/inference/hypothesis-testing/significance-level-and-decision-rule/">5. Significance Level (α) and Decision Rule</a></h3>
      <p>Reject vs fail to reject; critical region logic.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/inference/hypothesis-testing/significance-level-and-decision-rule/">Open lesson</a>
      </div>
    </div>

    <!-- 6 -->
    <div class="card lesson-card">
      <h3><a href="/inference/hypothesis-testing/type-i-and-type-ii-errors/">6. Type I and Type II Errors</a></h3>
      <p>Error probabilities, power, and trade-offs.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/inference/hypothesis-testing/type-i-and-type-ii-errors/">Open lesson</a>
      </div>
    </div>

    <!-- 7 -->
    <div class="card lesson-card">
      <h3><a href="/inference/hypothesis-testing/one-sample-tests-mean-and-proportion/">7. One-Sample Tests (Mean & Proportion)</a></h3>
      <p>z and t tests for μ and z tests for p.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/inference/hypothesis-testing/one-sample-tests-mean-and-proportion/">Open lesson</a>
      </div>
    </div>

    <!-- 8 -->
    <div class="card lesson-card">
      <h3><a href="/inference/hypothesis-testing/two-sample-tests-independent/">8. Two-Sample Tests (Independent)</a></h3>
      <p>Testing differences of means and proportions.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/inference/hypothesis-testing/two-sample-tests-independent/">Open lesson</a>
      </div>
    </div>

    <!-- 9 -->
    <div class="card lesson-card">
      <h3><a href="/inference/hypothesis-testing/paired-tests/">9. Paired Tests</a></h3>
      <p>Dependent designs and testing the mean difference.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/inference/hypothesis-testing/paired-tests/">Open lesson</a>
      </div>
    </div>

    <!-- 10 -->
    <div class="card lesson-card">
      <h3><a href="/inference/hypothesis-testing/connection-between-ci-and-tests/">10. Connection Between Confidence Intervals and Tests</a></h3>
      <p>Why 95% CI excluding 0 corresponds to α = 0.05 rejection.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/inference/hypothesis-testing/connection-between-ci-and-tests/">Open lesson</a>
      </div>
    </div>

  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of Block 3</h2>
      <ul class="bullets">
        <li>Formulate correct null and alternative hypotheses</li>
        <li>Compute and interpret test statistics and p-values</li>
        <li>Understand Type I and Type II errors</li>
        <li>Connect hypothesis tests to confidence intervals</li>
      </ul>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Next block</div>
        <div class="mini-body">
          Continue to
          <a href="/inference/applied-inference/" style="color:#1a73e8; text-decoration:underline;">
            <strong>Block 4 — Applied Inference</strong>
          </a>.
        </div>
      </div>
    </div>

  </div>
</section>

<script>
  (function () {
    var KEY = "esa_continue_inference_hypothesis_testing_lesson_v0";
    var raw = localStorage.getItem(KEY);
    if (!raw) return;

    try {
      var data = JSON.parse(raw);
      if (!data || !data.url || !data.label) return;

      var wrap = document.getElementById("continue-reading-block3");
      var label = document.getElementById("continue-reading-block3-label");
      var btn = document.getElementById("continue-reading-block3-btn");
      if (!wrap || !label || !btn) return;

      label.innerHTML = 'You last visited: <strong>' + data.label + '</strong>';
      btn.href = data.url;
      wrap.style.display = "block";
    } catch (e) {}
  })();
</script>