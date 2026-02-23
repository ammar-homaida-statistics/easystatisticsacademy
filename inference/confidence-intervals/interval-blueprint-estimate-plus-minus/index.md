---
layout: default
title: "2. CI Blueprint: Estimate ± Margin of Error"
description: "The universal structure of confidence intervals: estimate, standard error, critical value, and margin of error. One template that powers most intervals."
permalink: /inference/confidence-intervals/interval-blueprint-estimate-plus-minus/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem; letter-spacing:0.5px;">🚧 Lesson Under Construction</h2>
      <p style="margin:0; font-size:1.05rem; color:#5d4037; line-height:1.6;">
        Version 0 locks the structural blueprint of confidence intervals.
        Fully worked numeric examples and software demonstrations will be added later.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update "last visited lesson" for Inference Block 2 -->
<script>
  (function () {
    var KEY = "esa_continue_inference_confidence_intervals_lesson_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/confidence-intervals/interval-blueprint-estimate-plus-minus/",
      label: "Lesson 2 — CI Blueprint: Estimate ± Margin of Error",
      ts: Date.now()
    }));

    localStorage.setItem("esa_continue_inference_last_block_v0", JSON.stringify({
      url: "/inference/confidence-intervals/",
      label: "Block 2 — Confidence Intervals",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 2</span>
        <span class="badge">Lesson 2</span>
        <span class="badge">Margin of Error</span>
        <span class="badge">Standard Error</span>
      </div>

      <h1>2. CI Blueprint: Estimate ± Margin of Error</h1>
      <p class="lead">
        Most confidence intervals follow the same structure:
        <strong>estimate ± (critical value × standard error)</strong>.
        This lesson formalizes that universal template.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/confidence-intervals/">Back to Block 2</a>
        <a class="btn btn-outline" href="/inference/">Statistical Inference home</a>
      </div>

      <p class="muted-mini">
        Version 0: structure first. Distribution details come next.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      By the end of this lesson, you should be able to write the generic confidence interval formula,
      identify each of its components, and explain how they control uncertainty.
    </p>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Key idea</h2>
      <p style="margin:0;">
        A confidence interval always combines:
        (1) a point estimate,
        (2) a measure of variability (standard error),
        and (3) a multiplier (critical value) determined by the confidence level.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) The universal formula</h2>
  </div>

  <div class="card">
    <p style="font-size:1.15rem; margin:0;">
      <strong>Confidence Interval = Estimate ± (Critical Value × Standard Error)</strong>
    </p>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    This structure applies to means, proportions, differences, regression coefficients, and more.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Component 1 — The estimate</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Examples</h3>
      <ul class="bullets">
        <li>Sample mean: \(\bar{X}\)</li>
        <li>Sample proportion: \(\hat{p}\)</li>
        <li>Difference of means: \(\bar{X}_1 - \bar{X}_2\)</li>
        <li>Regression slope: \(\hat{\beta}\)</li>
      </ul>
    </div>

    <div class="card">
      <h3>Role</h3>
      <p>
        The estimate centers the interval.
        It represents the most plausible value based on observed data.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Component 2 — The standard error (SE)</h2>
    <p>
      The standard error measures the variability of the estimator across repeated samples.
    </p>
  </div>

  <div class="card">
    <p style="margin:0;">
      SE reflects how much the estimate would change if we drew another sample.
    </p>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    Larger sample sizes reduce SE. Higher variability increases SE.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Component 3 — The critical value</h2>
    <p>
      The critical value determines how many standard errors we move away from the estimate.
    </p>
  </div>

  <div class="card">
    <p style="margin:0;">
      For 95% confidence, the multiplier is chosen so that 95% of the sampling distribution
      lies within ± that value.
    </p>
  </div>

  <p style="margin-top:.75rem;">
    The exact value depends on:
    the distribution (z or t),
    the confidence level,
    and possibly degrees of freedom.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Margin of error (MOE)</h2>
  </div>

  <div class="card">
    <p style="font-size:1.1rem; margin:0;">
      <strong>Margin of Error = Critical Value × Standard Error</strong>
    </p>
  </div>

  <p style="margin-top:.75rem;">
    The margin of error determines the half-width of the interval.
    Larger MOE → wider interval → more uncertainty.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>6) What controls interval width?</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Sample size (n)</h3>
      <p>Increasing n decreases SE → narrower interval.</p>
    </div>

    <div class="card">
      <h3>Variability</h3>
      <p>More spread in data increases SE → wider interval.</p>
    </div>

    <div class="card">
      <h3>Confidence level</h3>
      <p>Higher confidence → larger critical value → wider interval.</p>
    </div>

    <div class="card">
      <h3>Distribution choice</h3>
      <p>t intervals are slightly wider than z intervals (extra uncertainty).</p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>7) Why this blueprint matters</h2>
  </div>

  <div class="card">
    <p style="margin:0;">
      Once you understand this template,
      every confidence interval becomes a matter of identifying:
      the correct estimate, the correct SE, and the correct critical value.
    </p>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Write the generic CI formula correctly</li>
        <li>Explain each component of the interval</li>
        <li>Understand how margin of error is formed</li>
        <li>See how width reflects uncertainty</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">
        Next we determine the correct multiplier:
        <strong>z vs t critical values</strong>.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/inference/confidence-intervals/critical-values-z-and-t/">
          Next lesson: 3. Critical Values →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/inference/confidence-intervals/what-is-a-confidence-interval/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 1: What Is a Confidence Interval?
          </a>
        </div>
      </div>
    </div>

  </div>
</section>