---
layout: default
title: "1. What Is a Confidence Interval?"
description: "Define confidence intervals precisely. Understand long-run coverage, interval variability, and why a 95% CI does not mean 95% probability for the parameter."
permalink: /inference/confidence-intervals/what-is-a-confidence-interval/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem; letter-spacing:0.5px;">🚧 Lesson Under Construction</h2>
      <p style="margin:0; font-size:1.05rem; color:#5d4037; line-height:1.6;">
        Version 0 is published first to lock the structure and conceptual interpretation.
        Worked examples, visuals, and software demonstrations will be added later without changing the lesson order.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update "last visited lesson" for Inference Block 2 -->
<script>
  (function () {
    var KEY = "esa_continue_inference_confidence_intervals_lesson_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/confidence-intervals/what-is-a-confidence-interval/",
      label: "Lesson 1 — What Is a Confidence Interval?",
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
        <span class="badge">Lesson 1</span>
        <span class="badge">Coverage</span>
        <span class="badge">Uncertainty</span>
      </div>

      <h1>1. What Is a Confidence Interval?</h1>
      <p class="lead">
        A confidence interval (CI) is a procedure that produces a range of plausible values
        for a population parameter based on sample data.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/confidence-intervals/">Back to Block 2</a>
        <a class="btn btn-outline" href="/inference/">Statistical Inference home</a>
      </div>

      <p class="muted-mini">
        Version 0: interpretation first. Computation comes next.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      By the end of this lesson, you should be able to define a confidence interval as a
      <strong>long-run coverage procedure</strong>, explain what “95% confidence” really means,
      and avoid the most common misinterpretations.
    </p>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Key idea</h2>
      <p style="margin:0;">
        A 95% confidence interval does <strong>not</strong> mean there is a 95% probability
        that the parameter lies inside the computed interval.
        It means that the procedure captures the true parameter in 95% of repeated samples.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) A confidence interval is a procedure</h2>
    <p>
      A confidence interval is not just the numbers you compute.
      It is a rule that maps data → interval.
    </p>
  </div>

  <div class="card">
    <p style="margin:0;">
      Each time you draw a new sample and apply the same rule,
      you obtain a different interval.
    </p>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    The parameter is fixed. The interval is random because it depends on the sample.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Long-run coverage interpretation</h2>
    <p>
      Suppose we repeatedly sample from the same population and compute a 95% CI each time.
    </p>
  </div>

  <div class="card">
    <p style="margin:0;">
      Approximately 95% of those intervals will contain the true parameter,
      and about 5% will miss it.
    </p>
  </div>

  <p style="margin-top:.75rem;">
      Confidence refers to the performance of the <strong>method</strong> across repetitions,
      not to uncertainty about a single fixed parameter.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) What a 95% CI does NOT mean</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Incorrect statement</h3>
      <p>
        “There is a 95% probability that μ is inside this interval.”
      </p>
    </div>

    <div class="card">
      <h3>Correct interpretation</h3>
      <p>
        “If we repeated this sampling process many times,
        95% of the intervals constructed this way would contain μ.”
      </p>
    </div>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    In the frequentist framework, μ is fixed. Probability statements apply to the interval procedure.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Why intervals are better than point estimates</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Point estimate</h3>
      <p>
        A single number (e.g., \(\bar{X}\)) gives no information about uncertainty.
      </p>
    </div>

    <div class="card">
      <h3>Confidence interval</h3>
      <p>
        Provides both an estimate and a measure of precision.
      </p>
    </div>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Interpretation</h2>
      <p style="margin:0;">
        An interval communicates not only what we believe is plausible,
        but also how precise our estimate is.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Width reflects uncertainty</h2>
    <p>
      Narrow intervals indicate higher precision.
      Wide intervals indicate greater uncertainty.
    </p>
  </div>

  <div class="card">
    <p style="margin:0;">
      Interval width depends on:
      sample size, variability, and confidence level.
    </p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>6) Common traps</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Trap A: Probability misinterpretation</h3>
      <p>Do not assign probability to a fixed parameter.</p>
    </div>

    <div class="card">
      <h3>Trap B: Thinking 95% means “almost certain”</h3>
      <p>5% of intervals miss the truth by design.</p>
    </div>

    <div class="card">
      <h3>Trap C: Ignoring assumptions</h3>
      <p>Coverage guarantees rely on model conditions.</p>
    </div>

    <div class="card">
      <h3>Trap D: Comparing overlapping intervals incorrectly</h3>
      <p>Overlap does not automatically imply non-significance.</p>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Define a confidence interval as a repeated-sampling procedure</li>
        <li>Explain long-run coverage correctly</li>
        <li>Avoid parameter-probability misinterpretation</li>
        <li>Understand why intervals are preferred to point estimates</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">
        Next we formalize the universal CI structure:
        <strong>Estimate ± Margin of Error</strong>.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/inference/confidence-intervals/interval-blueprint-estimate-plus-minus/">
          Next lesson: 2. CI Blueprint →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous block</div>
        <div class="mini-body">
          <a href="/inference/foundations/" style="color:#1a73e8; text-decoration:underline;">
            Block 1: Inference Foundations
          </a>
        </div>
      </div>
    </div>

  </div>
</section>