---
layout: default
title: "14. Sampling Bias vs Statistical Bias"
description: "Distinguish clearly between sampling bias (a data collection problem) and statistical bias (a property of an estimator). Understand why confusing them leads to serious inferential errors."
permalink: /inference/foundations/sampling-bias-vs-statistical-bias/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem; letter-spacing:0.5px;">🚧 Lesson Under Construction</h2>
      <p style="margin:0; font-size:1.05rem; color:#5d4037; line-height:1.6;">
        Version 0 clarifies two commonly confused meanings of “bias.”
        Applied examples and simulations will be added later.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update "last visited lesson" -->
<script>
  (function () {
    var KEY = "esa_continue_inference_foundations_lesson_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/foundations/sampling-bias-vs-statistical-bias/",
      label: "Lesson 14 — Sampling Bias vs Statistical Bias",
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
        <span class="badge">Lesson 14</span>
        <span class="badge">Bias</span>
        <span class="badge">Design vs Estimation</span>
      </div>

      <h1>14. Sampling Bias vs Statistical Bias</h1>
      <p class="lead">
        The word “bias” appears in two different contexts in statistics.
        One refers to flawed data collection.
        The other refers to properties of an estimator.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/foundations/">Back to Block 1</a>
        <a class="btn btn-outline" href="/inference/">Statistical Inference home</a>
      </div>

      <p class="muted-mini">
        Version 0: conceptual separation before applied corrections.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      By the end of this lesson, you should clearly distinguish between
      sampling bias and statistical bias, and explain why they are fundamentally different.
    </p>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Key idea</h2>
      <p style="margin:0;">
        <strong>Sampling bias is a data problem.</strong><br>
        <strong>Statistical bias is an estimator property.</strong>
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Sampling bias</h2>
  </div>

  <div class="card">
    <p style="margin:0;">
      Sampling bias occurs when the sample is systematically unrepresentative
      of the population.
    </p>
  </div>

  <ul class="bullets" style="margin-top:.75rem;">
    <li>Non-random selection</li>
    <li>Undercoverage of subgroups</li>
    <li>Self-selection bias</li>
    <li>Convenience sampling</li>
  </ul>

  <p class="muted-mini">
    Sampling bias affects external validity and generalization.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Statistical bias</h2>
  </div>

  <div class="card">
    <p style="margin:0;">
      Statistical bias refers to:
      \[
      \text{Bias}(\hat{\theta}) = E(\hat{\theta}) - \theta
      \]
    </p>
  </div>

  <p style="margin-top:.75rem;">
    It is a property of the estimator under repeated sampling.
  </p>

  <p class="muted-mini">
    It does not necessarily imply flawed data collection.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Why they are different</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Sampling bias</h3>
      <ul class="bullets">
        <li>Design problem</li>
        <li>Affects representativeness</li>
        <li>Large n does not fix it</li>
      </ul>
    </div>

    <div class="card">
      <h3>Statistical bias</h3>
      <ul class="bullets">
        <li>Estimator property</li>
        <li>Measured via expectation</li>
        <li>May shrink as n increases</li>
      </ul>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Interaction between the two</h2>
  </div>

  <div class="card">
    <p style="margin:0;">
      Even an unbiased estimator can produce misleading results
      if the data are collected with sampling bias.
    </p>
  </div>

  <p style="margin-top:.75rem;">
    Conversely, a biased estimator may still be useful
    when sampling is properly randomized.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Practical consequences</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Sampling bias consequences</h3>
      <p>
        Invalid generalization to the population.
      </p>
    </div>

    <div class="card">
      <h3>Statistical bias consequences</h3>
      <p>
        Systematic shift in repeated estimates.
      </p>
    </div>

    <div class="card">
      <h3>Correction methods</h3>
      <p>
        Weighting (design issue) vs estimator adjustment (model issue).
      </p>
    </div>

    <div class="card">
      <h3>Inference validity</h3>
      <p>
        Requires both proper sampling and appropriate estimator choice.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>6) Common misconceptions</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>“Large sample removes bias.”</h3>
      <p>
        Large n reduces variance, not sampling bias.
      </p>
    </div>

    <div class="card">
      <h3>“Bias always means bad statistics.”</h3>
      <p>
        Some biased estimators are optimal under MSE criteria.
      </p>
    </div>

    <div class="card">
      <h3>“If estimator is unbiased, inference is valid.”</h3>
      <p>
        Not if the sample is systematically distorted.
      </p>
    </div>

    <div class="card">
      <h3>“Sampling bias and estimator bias are interchangeable.”</h3>
      <p>
        They arise from completely different mechanisms.
      </p>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Distinguish sampling bias from statistical bias</li>
        <li>Explain design vs estimator sources of error</li>
        <li>Recognize when large sample size is insufficient</li>
        <li>Prepare for applied inference corrections</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">
        Next, we conclude Block 1 with 
        <strong>practical inference thinking: what can we claim?</strong>
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/inference/foundations/practical-inference-what-can-we-claim/">
          Next lesson →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/inference/foundations/independence-and-random-sampling/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 13: Independence & Random Sampling
          </a>
        </div>
      </div>
    </div>

  </div>
</section>