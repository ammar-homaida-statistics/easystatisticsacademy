---
layout: default
title: "1. Decision Framework and Assumptions (Quick Review)"
description: "Review how classical tests fit into the hypothesis testing framework and clarify the core assumptions that make test results valid."
permalink: /inference/classical-tests/decision-framework-and-assumptions/
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
        Version 0 aligns classical tests with the hypothesis testing framework
        and clarifies the assumptions that justify their sampling distributions.
        Detailed worked examples will be added later.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update continue-reading keys -->
<script>
  (function () {
    var KEY = "esa_continue_inference_classical_tests_lesson_v0";

    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/classical-tests/decision-framework-and-assumptions/",
      label: "Lesson 1 — Decision Framework and Assumptions",
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
        <span class="badge">Lesson 1</span>
        <span class="badge">Framework</span>
        <span class="badge">Assumptions</span>
      </div>

      <h1>1. Decision Framework and Assumptions (Quick Review)</h1>

      <p class="lead">
        Classical tests are standardized hypothesis tests
        with known sampling distributions.
        This lesson connects the general testing logic
        to the specific procedures used in practice.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/classical-tests/">Back to Block 4</a>
        <a class="btn btn-outline" href="/inference/">Statistical Inference home</a>
      </div>

      <p class="muted-mini">
        All classical tests follow the same logical structure.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      Revisit the general hypothesis testing framework
      and identify the assumptions that justify classical test statistics.
    </p>
  </div>

  <div class="callout">
    <div class="callout-copy">
      <h2>Core structure</h2>
      <p style="margin:0;">
        Every classical test follows:
        Hypotheses → Test statistic → Sampling distribution → p-value → Decision.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) The universal testing structure</h2>
  </div>

  <div class="card">
    Step 1: State \(H_0\) and \(H_1\). <br>
    Step 2: Compute a test statistic \(T\). <br>
    Step 3: Determine its distribution under \(H_0\). <br>
    Step 4: Compute p-value. <br>
    Step 5: Compare to \( \alpha \) and conclude.
  </div>

  <p class="muted-mini">
    What differs across tests is the form of the test statistic and its distribution.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Sampling distributions used in Block 4</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>z distribution</h3>
      <p style="margin:0;">
        Used when variance is known or normal approximation applies.
      </p>
    </div>

    <div class="card">
      <h3>t distribution</h3>
      <p style="margin:0;">
        Used when variance is unknown and estimated from data.
      </p>
    </div>

    <div class="card">
      <h3>Chi-square distribution</h3>
      <p style="margin:0;">
        Used for categorical count data.
      </p>
    </div>

    <div class="card">
      <h3>F distribution</h3>
      <p style="margin:0;">
        Used for comparing multiple means (ANOVA).
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Core assumptions across tests</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Independence</h3>
      <p style="margin:0;">
        Observations must be independent within and across groups.
      </p>
    </div>

    <div class="card">
      <h3>Random sampling / assignment</h3>
      <p style="margin:0;">
        Ensures validity of probability statements.
      </p>
    </div>

    <div class="card">
      <h3>Normality (when required)</h3>
      <p style="margin:0;">
        Needed for small-sample mean tests.
      </p>
    </div>

    <div class="card">
      <h3>Equal variance (in some tests)</h3>
      <p style="margin:0;">
        Required for pooled two-sample t tests and ANOVA.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) What happens when assumptions fail?</h2>
  </div>

  <div class="card">
    If assumptions are violated,
    the sampling distribution of the test statistic may no longer be valid.
    This affects p-values and conclusions.
  </div>

  <p class="muted-mini">
    Later blocks address robustness and alternatives.
  </p>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Connect classical tests to general testing logic</li>
        <li>Identify relevant sampling distributions</li>
        <li>Recognize core assumptions</li>
        <li>Understand why assumptions matter</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next lesson</h2>
      <p style="margin:0;">
        We begin with the simplest classical test:
        the one-sample z test for a mean (σ known).
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/inference/classical-tests/one-sample-z-test-for-mean/">
          Next lesson: 2. One-Sample z Test for a Mean →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous block</div>
        <div class="mini-body">
          <a href="/inference/hypothesis-testing/" style="color:#1a73e8; text-decoration:underline;">
            Block 3 — Hypothesis Testing
          </a>
        </div>
      </div>
    </div>
  </div>
</section>