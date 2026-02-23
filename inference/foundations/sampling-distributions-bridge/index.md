---
layout: default
title: "5. Sampling Distributions (Bridge From Probability)"
description: "Understand sampling distributions formally and conceptually. See how probability theory becomes the engine of inference through the distribution of estimators."
permalink: /inference/foundations/sampling-distributions-bridge/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem; letter-spacing:0.5px;">🚧 Lesson Under Construction</h2>
      <p style="margin:0; font-size:1.05rem; color:#5d4037; line-height:1.6;">
        Version 0 locks the conceptual bridge between probability and inference.
        Formal derivations, visual demonstrations, and software simulations will be added later.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update "last visited lesson" -->
<script>
  (function () {
    var KEY = "esa_continue_inference_foundations_lesson_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/foundations/sampling-distributions-bridge/",
      label: "Lesson 5 — Sampling Distributions (Bridge From Probability)",
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
        <span class="badge">Lesson 5</span>
        <span class="badge">Sampling</span>
        <span class="badge">Probability Bridge</span>
      </div>

      <h1>5. Sampling Distributions (Bridge From Probability)</h1>
      <p class="lead">
        Probability theory describes random variables.
        Inference applies probability to <strong>statistics</strong>.
        The sampling distribution is the bridge between these two worlds.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/foundations/">Back to Block 1</a>
        <a class="btn btn-outline" href="/inference/">Statistical Inference home</a>
      </div>

      <p class="muted-mini">
        Version 0: conceptual clarity first. Mathematical derivations will follow in later blocks.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      By the end of this lesson, you should be able to define a sampling distribution formally,
      explain its center and spread, and understand why it is the engine of confidence intervals and hypothesis tests.
    </p>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Key idea</h2>
      <p style="margin:0;">
        <strong>Inference is probability applied to estimators.</strong>
        The sampling distribution tells us how an estimator behaves across repeated samples.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Formal definition</h2>
    <p>
      Let \(\hat{\theta}\) be an estimator of a population parameter \(\theta\).
    </p>
  </div>

  <div class="card">
    <p style="margin:0;">
      The <strong>sampling distribution of \(\hat{\theta}\)</strong>
      is the probability distribution of \(\hat{\theta}\) induced by repeated sampling
      from the same population under the same design.
    </p>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    This definition depends critically on the sampling mechanism.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Center of the sampling distribution</h2>
    <p>
      The expected value of the estimator determines whether it is unbiased.
    </p>
  </div>

  <div class="card">
    <p style="margin:0;">
      If \(E(\hat{\theta}) = \theta\),
      the estimator is unbiased.
    </p>
  </div>

  <p style="margin-top:.75rem;">
    The center of the sampling distribution reflects systematic error (bias).
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Spread of the sampling distribution</h2>
    <p>
      The variance of the estimator determines its variability across samples.
    </p>
  </div>

  <div class="card">
    <p style="margin:0;">
      \(\text{Var}(\hat{\theta})\) measures how much the estimator fluctuates
      from one random sample to another.
    </p>
  </div>

  <p style="margin-top:.75rem;">
    The square root of this variance is the <strong>standard error (SE)</strong>.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Example: Sampling distribution of the mean</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Center</h3>
      <p>
        If the population mean is \(\mu\),
        then \(E(\bar{X}) = \mu\).
      </p>
    </div>

    <div class="card">
      <h3>Variance</h3>
      <p>
        If population variance is \(\sigma^2\),
        then  
        \(\text{Var}(\bar{X}) = \sigma^2/n\).
      </p>
    </div>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    Larger sample sizes reduce variability because averaging stabilizes noise.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Large-sample behavior (CLT preview)</h2>
    <p>
      Under mild conditions, the sampling distribution of many estimators
      becomes approximately normal as \(n\) increases.
    </p>
  </div>

  <div class="card">
    <p style="margin:0;">
      This is why normal-based inference (z and t procedures)
      works widely even when the original data are not normal.
    </p>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    The Central Limit Theorem will be formalized later.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>6) Why this is the bridge</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Probability world</h3>
      <p>
        We study distributions, expectations, variances, quantiles.
      </p>
    </div>

    <div class="card">
      <h3>Inference world</h3>
      <p>
        We apply those probability tools to estimators to build
        confidence intervals and hypothesis tests.
      </p>
    </div>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    Without sampling distributions, inference collapses into guesswork.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>7) Common misconceptions</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>“Sampling distribution = population distribution.”</h3>
      <p>
        These are different objects.
        One describes individuals; the other describes estimators.
      </p>
    </div>

    <div class="card">
      <h3>“Standard deviation = standard error.”</h3>
      <p>
        SD measures variability of observations;
        SE measures variability of an estimator.
      </p>
    </div>

    <div class="card">
      <h3>“Large n removes uncertainty.”</h3>
      <p>
        Larger n reduces SE but does not eliminate randomness.
      </p>
    </div>

    <div class="card">
      <h3>“One dataset shows the distribution.”</h3>
      <p>
        The sampling distribution is conceptual and defined by repeated sampling.
      </p>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Define sampling distribution formally</li>
        <li>Understand center (bias) and spread (variance/SE)</li>
        <li>Connect probability theory to inference procedures</li>
        <li>Prepare for formal introduction of standard error</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">
        Next, we focus specifically on the
        <strong>standard error</strong> as the quantitative measure of estimator uncertainty.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/inference/foundations/standard-error-unit-of-uncertainty/">
          Next lesson: 6. Standard Error — The Unit of Uncertainty →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/inference/foundations/estimators-vs-estimates/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 4: Estimators vs Estimates
          </a>
        </div>
      </div>
    </div>

  </div>
</section>