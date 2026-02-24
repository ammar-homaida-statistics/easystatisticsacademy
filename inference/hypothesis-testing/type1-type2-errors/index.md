---
layout: default
title: "6. Type I and Type II Errors"
description: "Define Type I and Type II errors formally, understand their probabilities (α and β), and explain their trade-off in hypothesis testing."
permalink: /inference/hypothesis-testing/type1-type2-errors/
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
        Version 0 establishes the formal definitions of Type I and Type II errors
        and their probabilistic interpretation. Power and effect size follow next.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update continue-reading keys -->
<script>
  (function () {
    var KEY = "esa_continue_inference_hypothesis_testing_lesson_v0";

    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/hypothesis-testing/type1-type2-errors/",
      label: "Lesson 6 — Type I and Type II Errors",
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
        <span class="badge">Lesson 6</span>
        <span class="badge">Type I</span>
        <span class="badge">Type II</span>
      </div>

      <h1>6. Type I and Type II Errors</h1>

      <p class="lead">
        Every hypothesis test carries two kinds of possible mistakes.
        A <strong>Type I error</strong> rejects a true null hypothesis.
        A <strong>Type II error</strong> fails to reject a false null hypothesis.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/hypothesis-testing/">Back to Block 3</a>
        <a class="btn btn-outline" href="/inference/">Statistical Inference home</a>
      </div>

      <p class="muted-mini">
        Statistical decisions always involve controlled risk.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      Define Type I and Type II errors formally,
      understand their probabilities,
      and explain the trade-off between them.
    </p>
  </div>

  <div class="callout">
    <div class="callout-copy">
      <h2>Core framework</h2>
      <p style="margin:0;">
        Decisions are made about \(H_0\),
        but reality may or may not match \(H_0\).
        Errors arise from the mismatch between decision and truth.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Decision vs truth table</h2>
  </div>

  <div class="card">
    <p style="margin:0;">
      <strong>Truth:</strong> either \(H_0\) is true or false.<br>
      <strong>Decision:</strong> reject \(H_0\) or fail to reject \(H_0\).
    </p>
  </div>

  <div class="card" style="margin-top:1rem;">
    <p style="margin:0;">
      If \(H_0\) is true and we reject → <strong>Type I error</strong><br>
      If \(H_0\) is false and we fail to reject → <strong>Type II error</strong>
    </p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Type I error (False Positive)</h2>
  </div>

  <div class="card">
    \[
    \alpha = P(\text{Reject } H_0 \mid H_0 \text{ true})
    \]
  </div>

  <p style="margin-top:.75rem;">
    This probability is controlled directly by the chosen significance level \( \alpha \).
  </p>

  <div class="callout">
    <div class="callout-copy">
      <h2>Interpretation</h2>
      <p style="margin:0;">
        In repeated experiments where \(H_0\) is true,
        about \(100\alpha\%\) of tests will incorrectly reject it.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Type II error (False Negative)</h2>
  </div>

  <div class="card">
    \[
    \beta = P(\text{Fail to reject } H_0 \mid H_0 \text{ false})
    \]
  </div>

  <p style="margin-top:.75rem;">
    Unlike α, β depends on the true parameter value under the alternative.
  </p>

  <div class="callout">
    <div class="callout-copy">
      <h2>Interpretation</h2>
      <p style="margin:0;">
        When a real effect exists,
        β is the probability that the test fails to detect it.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) The trade-off between α and β</h2>
  </div>

  <div class="card">
    <p style="margin:0;">
      For a fixed sample size,
      reducing α makes rejection harder,
      which typically increases β.
    </p>
  </div>

  <p style="margin-top:.75rem;">
    There is no way to minimize both errors simultaneously without increasing sample size.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Connection to power</h2>
  </div>

  <div class="card">
    \[
    \text{Power} = 1 - \beta
    \]
  </div>

  <p style="margin-top:.75rem;">
    Power is the probability of correctly rejecting a false null hypothesis.
  </p>

  <p class="muted-mini">
    Increasing power means reducing Type II error.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>6) Practical interpretation</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Type I error risk</h3>
      <p style="margin:0;">
        Claiming an effect that does not exist.
      </p>
    </div>

    <div class="card">
      <h3>Type II error risk</h3>
      <p style="margin:0;">
        Missing a real effect.
      </p>
    </div>

    <div class="card">
      <h3>Medical context</h3>
      <p style="margin:0;">
        False alarm vs missed diagnosis.
      </p>
    </div>

    <div class="card">
      <h3>Business context</h3>
      <p style="margin:0;">
        Acting on noise vs ignoring a profitable change.
      </p>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Define Type I and Type II errors formally</li>
        <li>Understand the roles of α and β</li>
        <li>Explain the error trade-off</li>
        <li>Recognize the link to statistical power</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">
        Next, we examine statistical power and effect size,
        and how they determine detectability.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/inference/hypothesis-testing/power-and-effect-size/">
          Next lesson: 7. Power and Effect Size →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/inference/hypothesis-testing/significance-level-alpha/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 5: Significance Level (α)
          </a>
        </div>
      </div>
    </div>
  </div>
</section>