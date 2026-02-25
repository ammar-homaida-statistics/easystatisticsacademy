---
layout: default
title: "1. P-Values: What They Mean"
description: "Interpret p-values correctly. Understand what a p-value measures, what it does not measure, and how to report it responsibly."
permalink: /inference/interpretation-reporting/p-values-what-they-mean/
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
        Version 0 establishes the formal definition of the p-value
        and clarifies common misinterpretations.
        Applied examples and reporting templates will be expanded later.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update continue-reading keys -->
<script>
  (function () {
    var KEY = "esa_continue_inference_interpretation_reporting_lesson_v0";

    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/interpretation-reporting/p-values-what-they-mean/",
      label: "Lesson 1 — P-Values: What They Mean",
      ts: Date.now()
    }));

    localStorage.setItem("esa_continue_inference_last_block_v0", JSON.stringify({
      url: "/inference/interpretation-reporting/",
      label: "Block 6 — Interpretation & Reporting",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 6</span>
        <span class="badge">Lesson 1</span>
        <span class="badge">p-value</span>
        <span class="badge">Interpretation</span>
      </div>

      <h1>1. P-Values: What They Mean</h1>

      <p class="lead">
        The p-value measures how compatible the observed data are
        with the null hypothesis.
        It is frequently misinterpreted.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/interpretation-reporting/">Back to Block 6</a>
        <a class="btn btn-outline" href="/inference/">Statistical Inference home</a>
      </div>

      <p class="muted-mini">
        Interpretation errors often arise from confusing probability of data with probability of hypotheses.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      Define the p-value formally, interpret it correctly,
      and avoid common misconceptions.
    </p>
  </div>

  <div class="callout">
    <div class="callout-copy">
      <h2>Formal definition</h2>
      <p style="margin:0;">
        The p-value is:
        \[
        P(\text{Test statistic as extreme or more extreme than observed} \mid H_0 \text{ true})
        \]
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) What the p-value measures</h2>
  </div>

  <div class="card">
    For a two-sided test:
    \[
    p =
    P(|T| \ge |t_{obs}| \mid H_0)
    \]
  </div>

  <p>
    It quantifies how surprising the observed statistic is
    under the null model.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) What the p-value does NOT measure</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Not</h3>
      <p>
        P(H₀ is true)
      </p>
    </div>

    <div class="card">
      <h3>Not</h3>
      <p>
        Probability the result occurred "by chance"
      </p>
    </div>

    <div class="card">
      <h3>Not</h3>
      <p>
        Magnitude of the effect
      </p>
    </div>

    <div class="card">
      <h3>Not</h3>
      <p>
        Probability the result will replicate
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Relationship to alpha</h2>
  </div>

  <div class="card">
    Decision rule:
    \[
    p \le \alpha
    \Rightarrow
    \text{Reject } H_0
    \]
  </div>

  <p>
    The p-value is compared to a pre-specified threshold α.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Continuous measure of evidence</h2>
  </div>

  <div class="card">
    Smaller p-value → greater incompatibility with H₀.
  </div>

  <p>
    However, evidence is continuous —
    there is no sharp boundary between “true” and “false”.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Correct reporting language</h2>
  </div>

  <div class="card">
    Correct:
    <br><br>
    “The data provide evidence against H₀ (p = 0.02).”
  </div>

  <div class="card" style="margin-top:1rem;">
    Incorrect:
    <br><br>
    “There is a 2% probability that H₀ is true.”
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Define the p-value precisely</li>
        <li>Distinguish data probability from hypothesis probability</li>
        <li>Use correct reporting language</li>
        <li>Avoid common misinterpretations</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next lesson</h2>
      <p style="margin:0;">
        We now distinguish statistical significance
        from practical importance.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/inference/interpretation-reporting/statistical-vs-practical-significance/">
          Next lesson: 2. Statistical vs Practical Significance →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous block</div>
        <div class="mini-body">
          <a href="/inference/power-sample-size/" style="color:#1a73e8; text-decoration:underline;">
            Block 5: Power & Sample Size
          </a>
        </div>
      </div>
    </div>
  </div>
</section>