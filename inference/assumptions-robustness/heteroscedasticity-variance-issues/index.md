---
layout: default
title: "4. Independence and Dependence"
description: "Understand why independence is central to inference, how dependence arises, and how it distorts standard errors and conclusions."
permalink: /inference/assumptions-robustness/independence-and-dependence/
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
        Version 0 establishes why independence is one of the most critical assumptions
        in classical inference and what happens when it fails.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update continue-reading keys -->
<script>
  (function () {
    var KEY = "esa_continue_inference_assumptions_robustness_lesson_v0";

    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/assumptions-robustness/independence-and-dependence/",
      label: "Lesson 4 — Independence and Dependence",
      ts: Date.now()
    }));

    localStorage.setItem("esa_continue_inference_last_block_v0", JSON.stringify({
      url: "/inference/assumptions-robustness/",
      label: "Block 7 — Assumptions & Robustness",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 7</span>
        <span class="badge">Lesson 4</span>
        <span class="badge">Independence</span>
        <span class="badge">Dependence</span>
      </div>

      <h1>4. Independence and Dependence</h1>

      <p class="lead">
        Independence underlies the validity of standard errors,
        confidence intervals, and hypothesis tests.
        When independence fails, inference can collapse.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/assumptions-robustness/">Back to Block 7</a>
        <a class="btn btn-outline" href="/inference/">Statistical Inference home</a>
      </div>

      <p class="muted-mini">
        Violations of independence often cause more damage than mild non-normality.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      Understand what independence formally means, how dependence arises,
      and why it typically biases standard errors and test results.
    </p>
  </div>

  <div class="callout">
    <div class="callout-copy">
      <h2>Core idea</h2>
      <p style="margin:0;">
        Independence ensures that information accumulates linearly with sample size.
        Dependence inflates or deflates effective sample size.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) What is independence?</h2>
  </div>

  <div class="card">
    Two observations are independent if:
    \[
    P(X_i, X_j) = P(X_i)P(X_j)
    \quad \text{for } i \ne j
    \]
  </div>

  <p>
    In practice, independence means one observation does not influence another.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Why independence matters</h2>
  </div>

  <div class="card">
    Standard error of the mean:
    \[
    SE(\bar{X}) = \frac{\sigma}{\sqrt{n}}
    \]
  </div>

  <p>
    This formula assumes independence.
    If observations are positively correlated,
    the true standard error is larger.
  </p>

  <div class="card" style="margin-top:1rem;">
    With correlation ρ:
    \[
    Var(\bar{X}) = \frac{\sigma^2}{n}
    \left( 1 + (n-1)\rho \right)
    \]
  </div>

  <p class="muted-mini">
    Positive correlation inflates variance dramatically.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Common sources of dependence</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Clustered data</h3>
      <p>Students within schools, patients within hospitals.</p>
    </div>

    <div class="card">
      <h3>Repeated measures</h3>
      <p>Same subject measured multiple times.</p>
    </div>

    <div class="card">
      <h3>Time series</h3>
      <p>Autocorrelation across time.</p>
    </div>

    <div class="card">
      <h3>Social networks</h3>
      <p>Connected individuals influence each other.</p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Consequences of ignoring dependence</h2>
  </div>

  <div class="card">
    • Standard errors too small  
    • p-values too optimistic  
    • Type I error inflated  
    • False confidence in results  
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) What to do</h2>
  </div>

  <div class="card">
    Possible remedies:
    <br><br>
    • Use paired or repeated-measures models  
    • Apply cluster-robust standard errors  
    • Use mixed-effects models  
    • Model autocorrelation explicitly  
  </div>

  <p class="muted-mini">
    Adjusting the model is often required when dependence exists.
  </p>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Understand formal independence</li>
        <li>Recognize dependence patterns</li>
        <li>See how correlation inflates variance</li>
        <li>Know corrective strategies</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next lesson</h2>
      <p style="margin:0;">
        We now examine unequal variances —
        heteroscedasticity and its consequences.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/inference/assumptions-robustness/heteroscedasticity-variance-issues/">
          Next lesson: 5. Heteroscedasticity and Variance Issues →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/inference/assumptions-robustness/checking-normality-what-and-why/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 3: Checking Normality
          </a>
        </div>
      </div>
    </div>
  </div>
</section>