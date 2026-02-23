---
layout: default
title: "13. Independence and Random Sampling: Why Inference Works"
description: "Understand why independence and random sampling are foundational assumptions for valid statistical inference, and what breaks when they fail."
permalink: /inference/foundations/independence-and-random-sampling/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem; letter-spacing:0.5px;">🚧 Lesson Under Construction</h2>
      <p style="margin:0; font-size:1.05rem; color:#5d4037; line-height:1.6;">
        Version 0 explains the structural assumptions behind inference.
        Case studies and applied diagnostics will be added later.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update "last visited lesson" -->
<script>
  (function () {
    var KEY = "esa_continue_inference_foundations_lesson_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/foundations/independence-and-random-sampling/",
      label: "Lesson 13 — Independence and Random Sampling",
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
        <span class="badge">Lesson 13</span>
        <span class="badge">Assumptions</span>
        <span class="badge">Design</span>
      </div>

      <h1>13. Independence and Random Sampling: Why Inference Works</h1>
      <p class="lead">
        Statistical inference depends not only on formulas,
        but on how data are collected.
        Independence and randomness are structural foundations.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/foundations/">Back to Block 1</a>
        <a class="btn btn-outline" href="/inference/">Statistical Inference home</a>
      </div>

      <p class="muted-mini">
        Version 0: conceptual foundations before diagnostics and corrections.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      By the end of this lesson, you should explain why independence and random sampling
      justify sampling distributions, standard errors, and probability-based inference.
    </p>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Key idea</h2>
      <p style="margin:0;">
        Inference works because randomness creates predictable long-run behavior.
        Without randomness, probability statements lose meaning.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) What is random sampling?</h2>
  </div>

  <div class="card">
    <p style="margin:0;">
      A random sample gives each unit in the population a known,
      non-zero probability of selection.
    </p>
  </div>

  <p style="margin-top:.75rem;">
    Random sampling ensures representativeness in expectation.
  </p>

  <p class="muted-mini">
    It justifies treating observations as draws from a probability model.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Independence</h2>
  </div>

  <div class="card">
    <p style="margin:0;">
      Observations are independent if knowing one observation
      does not change the probability distribution of another.
    </p>
  </div>

  <p style="margin-top:.75rem;">
    Independence simplifies variance calculations and
    enables central limit theorem results.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Why independence matters mathematically</h2>
  </div>

  <div class="card">
    <p style="margin:0;">
      For independent observations:
      \[
      \text{Var}(\bar{X}) = \frac{\sigma^2}{n}
      \]
    </p>
  </div>

  <p style="margin-top:.75rem;">
    If observations are correlated,
    this formula no longer holds.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) What breaks without independence?</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Standard errors become incorrect</h3>
      <p>Underestimated SE leads to false significance.</p>
    </div>

    <div class="card">
      <h3>Confidence intervals too narrow</h3>
      <p>Intervals may not achieve intended coverage.</p>
    </div>

    <div class="card">
      <h3>Invalid hypothesis tests</h3>
      <p>Type I error rates increase.</p>
    </div>

    <div class="card">
      <h3>Misleading conclusions</h3>
      <p>Dependence structures distort inference.</p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Random sampling vs random assignment</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Random sampling</h3>
      <p>Supports generalization to a population.</p>
    </div>

    <div class="card">
      <h3>Random assignment</h3>
      <p>Supports causal interpretation.</p>
    </div>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    These serve different inferential goals.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>6) Common misconceptions</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>“Large sample size fixes bias.”</h3>
      <p>
        Large n does not correct systematic sampling bias.
      </p>
    </div>

    <div class="card">
      <h3>“Random means arbitrary.”</h3>
      <p>
        Randomness means governed by probability, not careless selection.
      </p>
    </div>

    <div class="card">
      <h3>“Independence is always realistic.”</h3>
      <p>
        Many real datasets involve clustering or correlation.
      </p>
    </div>

    <div class="card">
      <h3>“Inference only depends on formulas.”</h3>
      <p>
        Design assumptions are equally important.
      </p>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Explain why randomness justifies inference</li>
        <li>Describe independence formally</li>
        <li>Recognize consequences of dependence</li>
        <li>Understand design vs model assumptions</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">
        Next, we distinguish between 
        <strong>sampling bias</strong> and 
        <strong>statistical bias</strong>.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/inference/foundations/sampling-bias-vs-statistical-bias/">
          Next lesson →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/inference/foundations/confidence-vs-significance-preview/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 12: Confidence vs Significance
          </a>
        </div>
      </div>
    </div>

  </div>
</section>