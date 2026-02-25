---
layout: default
title: "3. Interpreting Confidence Intervals"
description: "Understand what a confidence interval means, how to interpret it correctly, and how interval width communicates precision."
permalink: /inference/interpretation-reporting/interpreting-confidence-intervals/
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
        Version 0 clarifies the formal meaning of confidence intervals,
        common interpretation errors, and how interval width reflects precision.
        Applied examples and visuals will be expanded later.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update continue-reading keys -->
<script>
  (function () {
    var KEY = "esa_continue_inference_interpretation_reporting_lesson_v0";

    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/interpretation-reporting/interpreting-confidence-intervals/",
      label: "Lesson 3 — Interpreting Confidence Intervals",
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
        <span class="badge">Lesson 3</span>
        <span class="badge">Confidence Interval</span>
        <span class="badge">Precision</span>
      </div>

      <h1>3. Interpreting Confidence Intervals</h1>

      <p class="lead">
        A confidence interval provides a range of plausible values
        for a population parameter.
        Its interpretation is often misunderstood.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/interpretation-reporting/">Back to Block 6</a>
        <a class="btn btn-outline" href="/inference/">Statistical Inference home</a>
      </div>

      <p class="muted-mini">
        Confidence refers to the procedure, not to the specific interval after it is computed.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      Interpret confidence intervals correctly,
      understand their long-run meaning,
      and connect interval width to statistical precision.
    </p>
  </div>

  <div class="callout">
    <div class="callout-copy">
      <h2>Formal definition</h2>
      <p style="margin:0;">
        A 95% confidence interval is constructed by a method that,
        over repeated sampling,
        captures the true parameter in 95% of samples.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) What a CI means</h2>
  </div>

  <div class="card">
    Example form:
    \[
    \hat{\theta}
    \pm
    z_{\alpha/2} \cdot SE
    \]
  </div>

  <p>
    After computation, we say:
    <br><br>
    “The data are compatible with parameter values between
    the lower and upper bounds.”
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) What a CI does NOT mean</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Not</h3>
      <p>
        “There is a 95% probability that the true parameter lies in this interval.”
      </p>
    </div>

    <div class="card">
      <h3>Not</h3>
      <p>
        “The parameter moves randomly inside the interval.”
      </p>
    </div>
  </div>

  <p class="muted-mini">
    The parameter is fixed; the interval is random before sampling.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) CI width and precision</h2>
  </div>

  <div class="card">
    Width:
    \[
    2 \cdot z_{\alpha/2} \cdot SE
    \]
  </div>

  <div class="card" style="margin-top:1rem;">
    Since:
    \[
    SE = \frac{\sigma}{\sqrt{n}}
    \]
  </div>

  <p>
    Increasing n → smaller SE → narrower interval → greater precision.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Connection to hypothesis testing</h2>
  </div>

  <div class="card">
    If the null value lies outside the CI:
    <br><br>
    \[
    \text{Reject } H_0 \text{ at level } \alpha
    \]
  </div>

  <p>
    Confidence intervals provide more information than a binary test decision.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Reporting guidance</h2>
  </div>

  <div class="card">
    Recommended reporting:
    <br><br>
    Estimate = 2.4  
    95% CI: (1.1, 3.7)  
    Interpretation in context  
  </div>

  <p>
    Always interpret in substantive terms, not only statistical terms.
  </p>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Interpret confidence intervals correctly</li>
        <li>Understand long-run coverage meaning</li>
        <li>Relate width to precision</li>
        <li>Connect CI to hypothesis testing</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next lesson</h2>
      <p style="margin:0;">
        We now focus on interpreting effect sizes responsibly.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/inference/interpretation-reporting/interpreting-effect-sizes/">
          Next lesson: 4. Interpreting Effect Sizes →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/inference/interpretation-reporting/statistical-vs-practical-significance/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 2: Statistical vs Practical Significance
          </a>
        </div>
      </div>
    </div>
  </div>
</section>