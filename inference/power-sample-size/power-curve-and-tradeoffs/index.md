---
layout: default
title: "3. Power Curves and Trade-offs"
description: "Understand how power changes with sample size, effect size, and alpha, and interpret power curves for study design."
permalink: /inference/power-sample-size/power-curve-and-tradeoffs/
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
        Version 0 introduces power curves and the main design trade-offs.
        Graphical demonstrations and interactive simulations will be added later.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update continue-reading keys -->
<script>
  (function () {
    var KEY = "esa_continue_inference_power_sample_size_lesson_v0";

    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/power-sample-size/power-curve-and-tradeoffs/",
      label: "Lesson 3 — Power Curves and Trade-offs",
      ts: Date.now()
    }));

    localStorage.setItem("esa_continue_inference_last_block_v0", JSON.stringify({
      url: "/inference/power-sample-size/",
      label: "Block 5 — Power & Sample Size",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 5</span>
        <span class="badge">Lesson 3</span>
        <span class="badge">Power Curve</span>
        <span class="badge">Design Trade-offs</span>
      </div>

      <h1>3. Power Curves and Trade-offs</h1>

      <p class="lead">
        A power curve shows how the probability of rejecting the null hypothesis
        changes as the true effect size varies.
        It visualizes the trade-offs between sample size, alpha, and detectability.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/power-sample-size/">Back to Block 5</a>
        <a class="btn btn-outline" href="/inference/">Statistical Inference home</a>
      </div>

      <p class="muted-mini">
        Study design is a balance between sensitivity and error control.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      Interpret power curves and understand how alpha, sample size,
      and effect size interact in study planning.
    </p>
  </div>

  <div class="callout">
    <div class="callout-copy">
      <h2>Core idea</h2>
      <p style="margin:0;">
        Power is not fixed — it depends on the true effect size.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) What is a power curve?</h2>
  </div>

  <div class="card">
    For each possible true effect size δ:
    \[
    \text{Power}(\delta) = P(\text{Reject } H_0 \mid \delta \text{ is true})
    \]
  </div>

  <p>
    The curve typically increases as the true effect size moves farther
    from the null value.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Effect of sample size</h2>
  </div>

  <div class="card">
    Increasing n:
    <br><br>
    • Reduces standard error  
    • Increases separation between distributions  
    • Increases power  
  </div>

  <p class="muted-mini">
    Larger samples make smaller effects detectable.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Effect of alpha</h2>
  </div>

  <div class="card">
    Larger alpha:
    <br><br>
    • Expands rejection region  
    • Increases power  
    • Increases Type I error risk  
  </div>

  <p>
    Lower alpha protects against false positives
    but reduces power.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Effect of variability</h2>
  </div>

  <div class="card">
    Greater population variance:
    <br><br>
    • Increases standard error  
    • Reduces separation  
    • Reduces power  
  </div>

  <p class="muted-mini">
    Controlling variability increases detectability.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Design trade-offs</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>High alpha</h3>
      <p>More sensitive but higher false positive rate.</p>
    </div>

    <div class="card">
      <h3>Large n</h3>
      <p>More power but higher cost.</p>
    </div>

    <div class="card">
      <h3>Small variability</h3>
      <p>Improved precision through better measurement.</p>
    </div>

    <div class="card">
      <h3>Meaningful effect</h3>
      <p>Planning based on smallest relevant difference.</p>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Interpret power curves correctly</li>
        <li>Understand how n, alpha, and variability affect power</li>
        <li>Recognize trade-offs in study design</li>
        <li>Plan studies based on meaningful effect sizes</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next lesson</h2>
      <p style="margin:0;">
        We now derive the required sample size
        for detecting a mean difference.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/inference/power-sample-size/sample-size-for-mean/">
          Next lesson: 4. Sample Size for a Mean →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/inference/power-sample-size/effect-size-and-practical-importance/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 2: Effect Size & Practical Importance
          </a>
        </div>
      </div>
    </div>
  </div>
</section>