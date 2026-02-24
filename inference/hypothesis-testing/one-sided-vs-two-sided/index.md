---
layout: default
title: "8. One-Sided vs Two-Sided Tests"
description: "Compare one-sided and two-sided hypothesis tests, understand how they affect rejection regions and power, and learn when each is appropriate."
permalink: /inference/hypothesis-testing/one-sided-vs-two-sided/
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
        Version 0 establishes the formal distinction between one-sided and two-sided tests.
        Numerical examples and power comparisons will be added later.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update continue-reading keys -->
<script>
  (function () {
    var KEY = "esa_continue_inference_hypothesis_testing_lesson_v0";

    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/hypothesis-testing/one-sided-vs-two-sided/",
      label: "Lesson 8 — One-Sided vs Two-Sided Tests",
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
        <span class="badge">Lesson 8</span>
        <span class="badge">One-Sided</span>
        <span class="badge">Two-Sided</span>
      </div>

      <h1>8. One-Sided vs Two-Sided Tests</h1>

      <p class="lead">
        The direction of the alternative hypothesis determines
        how extremeness is defined and where the rejection region lies.
        Choosing between one-sided and two-sided testing
        affects power and interpretation.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/hypothesis-testing/">Back to Block 3</a>
        <a class="btn btn-outline" href="/inference/">Statistical Inference home</a>
      </div>

      <p class="muted-mini">
        Direction must be chosen before observing the data.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      Distinguish formally between one-sided and two-sided tests,
      understand how rejection regions differ,
      and explain their effect on power.
    </p>
  </div>

  <div class="callout">
    <div class="callout-copy">
      <h2>Core idea</h2>
      <p style="margin:0;">
        A two-sided test looks for any deviation from the null.
        A one-sided test looks for deviation in only one direction.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Hypothesis structure</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Two-sided test</h3>
      <p style="margin:0;">
        \[
        H_0:\ \theta = \theta_0
        \quad\text{vs}\quad
        H_1:\ \theta \ne \theta_0
        \]
      </p>
    </div>

    <div class="card">
      <h3>One-sided test (greater)</h3>
      <p style="margin:0;">
        \[
        H_0:\ \theta = \theta_0
        \quad\text{vs}\quad
        H_1:\ \theta > \theta_0
        \]
      </p>
    </div>

    <div class="card">
      <h3>One-sided test (smaller)</h3>
      <p style="margin:0;">
        \[
        H_0:\ \theta = \theta_0
        \quad\text{vs}\quad
        H_1:\ \theta < \theta_0
        \]
      </p>
    </div>

    <div class="card">
      <h3>Directionality rule</h3>
      <p style="margin:0;">
        The alternative must reflect the scientific question,
        not the observed data.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Rejection regions</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Two-sided (α split)</h3>
      <p style="margin:0;">
        \[
        \text{Reject if } |T| > t_{\alpha/2}
        \]
      </p>
      <p class="muted-mini">
        Probability α is split across two tails.
      </p>
    </div>

    <div class="card">
      <h3>One-sided (α in one tail)</h3>
      <p style="margin:0;">
        \[
        \text{Reject if } T > t_{\alpha}
        \]
      </p>
      <p class="muted-mini">
        Entire α lies in one tail.
      </p>
    </div>
  </div>

  <p class="muted-mini">
    For the same α, the one-sided critical value is smaller in magnitude,
    making rejection easier in that direction.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Effect on power</h2>
  </div>

  <div class="card">
    <p style="margin:0;">
      When the true effect is in the specified direction,
      a one-sided test has greater power than a two-sided test
      at the same α and sample size.
    </p>
  </div>

  <p style="margin-top:.75rem;">
    However, if the true effect is in the opposite direction,
    a one-sided test may completely miss it.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) When to use each?</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Use two-sided when</h3>
      <ul class="bullets">
        <li>Both increases and decreases matter</li>
        <li>No strong theoretical direction exists</li>
        <li>Conservative inference is preferred</li>
      </ul>
    </div>

    <div class="card">
      <h3>Use one-sided when</h3>
      <ul class="bullets">
        <li>Only one direction is meaningful</li>
        <li>Opposite direction is irrelevant or impossible</li>
        <li>Direction is pre-specified before data collection</li>
      </ul>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Common pitfalls</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Post-hoc direction choice</h3>
      <p style="margin:0;">
        Choosing one-sided after seeing the data invalidates error guarantees.
      </p>
    </div>

    <div class="card">
      <h3>Reporting inconsistency</h3>
      <p style="margin:0;">
        Using a two-sided confidence interval but a one-sided test creates confusion.
      </p>
    </div>

    <div class="card">
      <h3>Misinterpretation</h3>
      <p style="margin:0;">
        A one-sided test does not test for “any difference.”
      </p>
    </div>

    <div class="card">
      <h3>Ignoring context</h3>
      <p style="margin:0;">
        Direction must be justified by theory or design.
      </p>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Formally distinguish one-sided and two-sided tests</li>
        <li>Understand how α is allocated across tails</li>
        <li>Explain differences in power</li>
        <li>Avoid post-hoc directional testing</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">
        Next, we connect hypothesis tests and confidence intervals
        and show their mathematical equivalence.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/inference/hypothesis-testing/ci-and-test-connection/">
          Next lesson: 9. CI and Test Connection →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/inference/hypothesis-testing/power-and-effect-size/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 7: Power and Effect Size
          </a>
        </div>
      </div>
    </div>
  </div>
</section>