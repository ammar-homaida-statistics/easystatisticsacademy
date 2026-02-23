---
layout: default
title: "11. Point vs Interval Estimation"
description: "Understand the conceptual difference between point estimation and interval estimation, and why intervals are the natural language of statistical inference."
permalink: /inference/foundations/point-vs-interval-estimation/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem; letter-spacing:0.5px;">🚧 Lesson Under Construction</h2>
      <p style="margin:0; font-size:1.05rem; color:#5d4037; line-height:1.6;">
        Version 0 clarifies the conceptual distinction between point and interval estimation.
        Formal derivations and applied examples will be added later.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update "last visited lesson" -->
<script>
  (function () {
    var KEY = "esa_continue_inference_foundations_lesson_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/foundations/point-vs-interval-estimation/",
      label: "Lesson 11 — Point vs Interval Estimation",
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
        <span class="badge">Lesson 11</span>
        <span class="badge">Estimation</span>
        <span class="badge">Uncertainty</span>
      </div>

      <h1>11. Point vs Interval Estimation</h1>
      <p class="lead">
        A single number estimates a parameter — but it does not express uncertainty.
        Interval estimation expands that number into a range of plausible values.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/foundations/">Back to Block 1</a>
        <a class="btn btn-outline" href="/inference/">Statistical Inference home</a>
      </div>

      <p class="muted-mini">
        Version 0: conceptual clarity first. Computational examples come next.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      By the end of this lesson, you should clearly distinguish between
      point estimation and interval estimation, and explain why intervals
      are central to modern statistical inference.
    </p>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Key idea</h2>
      <p style="margin:0;">
        A point estimate answers <em>“What is our best guess?”</em><br>
        An interval estimate answers <em>“How uncertain is that guess?”</em>
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Point estimation</h2>
    <p>
      A point estimator produces a single numerical value from the sample.
    </p>
  </div>

  <div class="card">
    <p style="margin:0;">
      Examples:
      \[
      \bar{X}, \quad \hat{p}, \quad \hat{\beta}
      \]
    </p>
  </div>

  <p style="margin-top:.75rem;">
      The result is one number — the estimate.
  </p>

  <div class="card" style="margin-top:1rem;">
    <h3>Strength</h3>
    <p style="margin:0;">Simple, direct, easy to interpret.</p>
  </div>

  <div class="card" style="margin-top:1rem;">
    <h3>Limitation</h3>
    <p style="margin:0;">
      It hides uncertainty. Two samples may produce different estimates.
    </p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Why point estimates are incomplete</h2>
  </div>

  <div class="card">
    <p style="margin:0;">
      Every estimator has sampling variability.
      Reporting only a single value ignores this variability.
    </p>
  </div>

  <p style="margin-top:.75rem;">
    Without uncertainty information, we cannot judge:
  </p>

  <ul class="bullets">
    <li>Precision</li>
    <li>Reliability</li>
    <li>Statistical significance</li>
  </ul>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Interval estimation</h2>
    <p>
      An interval estimator produces a range:
    </p>
  </div>

  <div class="card">
    <p style="margin:0;">
      \[
      \hat{\theta} \pm (\text{critical value}) \times SE(\hat{\theta})
      \]
    </p>
  </div>

  <p style="margin-top:.75rem;">
    This range reflects sampling variability.
  </p>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Interpretation principle</h2>
      <p style="margin:0;">
        A 95% confidence interval means that the procedure captures
        the true parameter in 95% of repeated samples.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Comparing the two approaches</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Point estimation</h3>
      <ul class="bullets">
        <li>Single value</li>
        <li>No direct uncertainty information</li>
        <li>Easy but incomplete</li>
      </ul>
    </div>

    <div class="card">
      <h3>Interval estimation</h3>
      <ul class="bullets">
        <li>Range of plausible values</li>
        <li>Explicit uncertainty</li>
        <li>More informative</li>
      </ul>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Why intervals are central to inference</h2>
  </div>

  <div class="card">
    <p style="margin:0;">
      Intervals naturally connect to:
    </p>
  </div>

  <ul class="bullets" style="margin-top:.75rem;">
    <li>Hypothesis testing</li>
    <li>Effect size interpretation</li>
    <li>Scientific reporting</li>
    <li>Decision making</li>
  </ul>

  <p class="muted-mini">
    Modern reporting standards often emphasize confidence intervals over p-values.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>6) Common misconceptions</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>“The parameter lies in this interval with 95% probability.”</h3>
      <p>
        The parameter is fixed; the interval varies.
      </p>
    </div>

    <div class="card">
      <h3>“Narrow intervals mean high confidence.”</h3>
      <p>
        Confidence level and width are different concepts.
      </p>
    </div>

    <div class="card">
      <h3>“Point estimate becomes irrelevant.”</h3>
      <p>
        The point estimate is the center of the interval.
      </p>
    </div>

    <div class="card">
      <h3>“Intervals replace hypothesis tests.”</h3>
      <p>
        They are mathematically connected, not competing tools.
      </p>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Distinguish clearly between point and interval estimation</li>
        <li>Explain why intervals communicate uncertainty</li>
        <li>Understand long-run coverage interpretation</li>
        <li>Prepare for formal confidence interval construction</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">
        Next, we examine <strong>confidence level and significance level</strong>,
        clarifying what these probabilities actually control.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/inference/foundations/confidence-level-and-significance-level/">
          Next lesson →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/inference/foundations/inference-pipeline-estimator-se-ci-test/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 10: The Inference Pipeline
          </a>
        </div>
      </div>
    </div>

  </div>
</section>