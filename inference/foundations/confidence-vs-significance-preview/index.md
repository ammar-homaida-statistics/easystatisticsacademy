---
layout: default
title: "12. Confidence Level vs Significance Level (Preview)"
description: "Clarify the difference between confidence level and significance level, and understand how they are mathematically linked but conceptually distinct."
permalink: /inference/foundations/confidence-vs-significance-preview/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem; letter-spacing:0.5px;">🚧 Lesson Under Construction</h2>
      <p style="margin:0; font-size:1.05rem; color:#5d4037; line-height:1.6;">
        Version 0 clarifies the logic linking confidence intervals and hypothesis tests.
        Detailed numerical demonstrations will be added later.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update "last visited lesson" -->
<script>
  (function () {
    var KEY = "esa_continue_inference_foundations_lesson_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/foundations/confidence-vs-significance-preview/",
      label: "Lesson 12 — Confidence vs Significance (Preview)",
      ts: Date.now()
    }));

    localStorage.setItem("esa_continue_inference_last_block_v0", JSON.stringify({
      url: "/inference/foundations/",
      label: "Block 1 — Inference Foundations",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 1</span>
        <span class="badge">Lesson 12</span>
        <span class="badge">Confidence</span>
        <span class="badge">Significance</span>
      </div>

      <h1>12. Confidence Level vs Significance Level (Preview)</h1>
      <p class="lead">
        Confidence level and significance level are mathematically connected,
        yet they answer different inferential questions.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/foundations/">Back to Block 1</a>
        <a class="btn btn-outline" href="/inference/">Statistical Inference home</a>
      </div>

      <p class="muted-mini">
        Version 0: conceptual alignment before formal hypothesis testing.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      By the end of this lesson, you should distinguish clearly between
      confidence level (1 − α) and significance level (α),
      and explain how they connect confidence intervals to hypothesis testing.
    </p>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Key idea</h2>
      <p style="margin:0;">
        <strong>Confidence level controls coverage.</strong><br>
        <strong>Significance level controls Type I error.</strong>
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Significance level (α)</h2>
  </div>

  <div class="card">
    <p style="margin:0;">
      The significance level α is the probability of rejecting a true null hypothesis:
    </p>
    <p style="margin-top:.5rem;">
      \[
      \alpha = P(\text{Reject } H_0 \mid H_0 \text{ is true})
      \]
    </p>
  </div>

  <p style="margin-top:.75rem;">
    It controls the long-run Type I error rate.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Confidence level (1 − α)</h2>
  </div>

  <div class="card">
    <p style="margin:0;">
      The confidence level represents the long-run proportion of intervals
      that capture the true parameter:
    </p>
    <p style="margin-top:.5rem;">
      \[
      1 - \alpha
      \]
    </p>
  </div>

  <p style="margin-top:.75rem;">
    For example, a 95% confidence level corresponds to α = 0.05.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Mathematical connection</h2>
  </div>

  <div class="card">
    <p style="margin:0;">
      In two-sided tests:
    </p>
    <p style="margin-top:.5rem;">
      A parameter value θ₀ is rejected at level α<br>
      <strong>if and only if</strong><br>
      θ₀ lies outside the (1 − α) confidence interval.
    </p>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    This is why confidence intervals and hypothesis tests are dual procedures.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Conceptual difference</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Significance level</h3>
      <ul class="bullets">
        <li>Decision-focused</li>
        <li>Error-rate control</li>
        <li>Binary outcome (reject / not reject)</li>
      </ul>
    </div>

    <div class="card">
      <h3>Confidence level</h3>
      <ul class="bullets">
        <li>Estimation-focused</li>
        <li>Uncertainty quantification</li>
        <li>Range of plausible values</li>
      </ul>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Common misconceptions</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>“95% confidence means 95% probability parameter is inside.”</h3>
      <p>
        The parameter is fixed; the interval is random.
      </p>
    </div>

    <div class="card">
      <h3>“α is the probability the null is true.”</h3>
      <p>
        α controls error under the assumption the null is true.
      </p>
    </div>

    <div class="card">
      <h3>“Confidence and significance are unrelated.”</h3>
      <p>
        They are numerically linked in standard procedures.
      </p>
    </div>

    <div class="card">
      <h3>“Changing α only affects tests.”</h3>
      <p>
        It also directly changes confidence interval width.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>6) Why this preview matters</h2>
  </div>

  <div class="card">
    <p style="margin:0;">
      Understanding this connection prevents:
    </p>
  </div>

  <ul class="bullets" style="margin-top:.75rem;">
    <li>Mechanical p-value interpretation</li>
    <li>Misunderstanding of CI meaning</li>
    <li>Confusion between estimation and testing logic</li>
  </ul>

  <p class="muted-mini">
    Next blocks formalize hypothesis testing in detail.
  </p>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Define α and 1 − α precisely</li>
        <li>Explain their long-run interpretations</li>
        <li>Describe the CI–test duality</li>
        <li>Prepare for formal hypothesis testing procedures</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">
        Next, we examine why <strong>independence and random sampling</strong>
        are foundational assumptions behind inference validity.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/inference/foundations/independence-and-random-sampling/">
          Next lesson →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/inference/foundations/point-vs-interval-estimation/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 11: Point vs Interval Estimation
          </a>
        </div>
      </div>
    </div>

  </div>
</section>