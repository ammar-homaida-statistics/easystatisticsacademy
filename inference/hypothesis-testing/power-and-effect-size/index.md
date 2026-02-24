---
layout: default
title: "7. Power and Effect Size"
description: "Define statistical power formally, understand its relationship with Type II error (β), and explain how effect size, sample size, variability, and α determine detectability."
permalink: /inference/hypothesis-testing/power-and-effect-size/
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
        Version 0 establishes the formal definitions of statistical power and effect size.
        Numerical examples and power-curve visualizations will be added later.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update continue-reading keys -->
<script>
  (function () {
    var KEY = "esa_continue_inference_hypothesis_testing_lesson_v0";

    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/hypothesis-testing/power-and-effect-size/",
      label: "Lesson 7 — Power and Effect Size",
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
        <span class="badge">Lesson 7</span>
        <span class="badge">Power</span>
        <span class="badge">Effect Size</span>
      </div>

      <h1>7. Power and Effect Size</h1>

      <p class="lead">
        Statistical power measures a test’s ability to detect real effects.
        It depends on the size of the true effect,
        the sample size,
        the variability,
        and the chosen significance level \( \alpha \).
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/hypothesis-testing/">Back to Block 3</a>
        <a class="btn btn-outline" href="/inference/">Statistical Inference home</a>
      </div>

      <p class="muted-mini">
        Detectability is a joint property of design and effect magnitude.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      Define statistical power formally,
      relate it to Type II error,
      and explain how design choices influence detectability.
    </p>
  </div>

  <div class="callout">
    <div class="callout-copy">
      <h2>Core definition</h2>
      <p style="margin:0;">
        Statistical power is the probability of correctly rejecting a false null hypothesis.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Formal definition</h2>
  </div>

  <div class="card">
    \[
    \text{Power} = P(\text{Reject } H_0 \mid H_0 \text{ is false})
    \]
  </div>

  <div class="card" style="margin-top:1rem;">
    \[
    \text{Power} = 1 - \beta
    \]
  </div>

  <p class="muted-mini">
    Here, \( \beta \) is the probability of a Type II error.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) What power represents</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>High power</h3>
      <p style="margin:0;">
        The test is likely to detect a real effect.
      </p>
    </div>

    <div class="card">
      <h3>Low power</h3>
      <p style="margin:0;">
        The test often misses real effects.
      </p>
    </div>
  </div>

  <p class="muted-mini">
    Power is evaluated under a specific alternative parameter value.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Effect size</h2>
    <p>
      Effect size quantifies how far the true parameter lies from the null value.
    </p>
  </div>

  <div class="card">
    \[
    \text{Effect size (raw)} = \theta_{\text{true}} - \theta_0
    \]
  </div>

  <div class="card" style="margin-top:1rem;">
    \[
    \text{Standardized effect size} =
    \frac{\theta_{\text{true}} - \theta_0}{\sigma}
    \]
  </div>

  <p class="muted-mini">
    Larger effect sizes increase power.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) What determines power?</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Effect size</h3>
      <p style="margin:0;">
        Larger effects are easier to detect.
      </p>
    </div>

    <div class="card">
      <h3>Sample size (n)</h3>
      <p style="margin:0;">
        Larger samples reduce standard error and increase power.
      </p>
    </div>

    <div class="card">
      <h3>Variability (σ)</h3>
      <p style="margin:0;">
        Greater variability reduces power.
      </p>
    </div>

    <div class="card">
      <h3>Significance level (α)</h3>
      <p style="margin:0;">
        Larger α increases power but raises Type I error risk.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Trade-offs</h2>
  </div>

  <div class="card">
    <p style="margin:0;">
      For fixed sample size:
      decreasing α reduces power.
    </p>
  </div>

  <div class="card" style="margin-top:1rem;">
    <p style="margin:0;">
      Increasing sample size improves power
      without increasing Type I error.
    </p>
  </div>

  <p class="muted-mini">
    Sample size is the main design tool for controlling power.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>6) Why power matters</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Scientific validity</h3>
      <p style="margin:0;">
        Low power increases false negatives.
      </p>
    </div>

    <div class="card">
      <h3>Replicability</h3>
      <p style="margin:0;">
        Underpowered studies produce unstable results.
      </p>
    </div>

    <div class="card">
      <h3>Ethical considerations</h3>
      <p style="margin:0;">
        Inadequate power may waste resources.
      </p>
    </div>

    <div class="card">
      <h3>Design planning</h3>
      <p style="margin:0;">
        Power analysis guides required sample size.
      </p>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Define power as \(1 - \beta\)</li>
        <li>Understand the role of effect size</li>
        <li>Explain how sample size affects detectability</li>
        <li>Recognize the α–β trade-off</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">
        Next, we compare one-sided and two-sided tests
        and examine their implications for power.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/inference/hypothesis-testing/one-sided-vs-two-sided/">
          Next lesson: 8. One-Sided vs Two-Sided Tests →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/inference/hypothesis-testing/type1-type2-errors/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 6: Type I and Type II Errors
          </a>
        </div>
      </div>
    </div>
  </div>
</section>