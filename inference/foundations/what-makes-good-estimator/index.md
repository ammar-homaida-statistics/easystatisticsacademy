---
layout: default
title: "9. What Makes an Estimator “Good”?"
description: "Examine the formal criteria used to evaluate estimators: unbiasedness, variance, efficiency, consistency, and mean squared error. Understand how these properties interact."
permalink: /inference/foundations/what-makes-good-estimator/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem; letter-spacing:0.5px;">🚧 Lesson Under Construction</h2>
      <p style="margin:0; font-size:1.05rem; color:#5d4037; line-height:1.6;">
        Version 0 focuses on evaluation criteria for estimators.
        Formal proofs and applied comparisons will be added later.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update "last visited lesson" -->
<script>
  (function () {
    var KEY = "esa_continue_inference_foundations_lesson_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/foundations/what-makes-good-estimator/",
      label: "Lesson 9 — What Makes an Estimator “Good”?",
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
        <span class="badge">Lesson 9</span>
        <span class="badge">Evaluation</span>
        <span class="badge">Estimator Properties</span>
      </div>

      <h1>9. What Makes an Estimator “Good”?</h1>
      <p class="lead">
        Not all estimators are equally desirable.
        This lesson defines the formal criteria used to evaluate estimators
        and explains how they guide methodological choices.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/foundations/">Back to Block 1</a>
        <a class="btn btn-outline" href="/inference/">Statistical Inference home</a>
      </div>

      <p class="muted-mini">
        Version 0: conceptual evaluation framework. Modeling implications come later.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      By the end of this lesson, you should identify the main criteria for evaluating estimators
      and explain how unbiasedness, variance, efficiency, consistency, and MSE interact.
    </p>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Key idea</h2>
      <p style="margin:0;">
        A “good” estimator balances <strong>accuracy</strong>, <strong>stability</strong>,
        and <strong>long-run reliability</strong>.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Unbiasedness</h2>
  </div>

  <div class="card">
    <p style="margin:0;">
      An estimator \(\hat{\theta}\) is unbiased if:
      \[
      E(\hat{\theta}) = \theta.
      \]
    </p>
  </div>

  <p style="margin-top:.75rem;">
    Unbiasedness ensures no systematic error in expectation.
  </p>

  <p class="muted-mini">
    However, unbiasedness alone does not guarantee small variability.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Variance</h2>
  </div>

  <div class="card">
    <p style="margin:0;">
      Lower variance means the estimator is more stable across samples.
    </p>
  </div>

  <p style="margin-top:.75rem;">
    Between two unbiased estimators, the one with smaller variance is preferred.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Efficiency</h2>
  </div>

  <div class="card">
    <p style="margin:0;">
      An estimator is more efficient if it has smaller variance among unbiased estimators.
    </p>
  </div>

  <p style="margin-top:.75rem;">
    In many models, certain estimators achieve minimum variance under assumptions
    (e.g., Gauss–Markov theorem in regression).
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Consistency</h2>
  </div>

  <div class="card">
    <p style="margin:0;">
      An estimator is consistent if:
      \[
      \hat{\theta} \xrightarrow{p} \theta \quad \text{as } n \to \infty.
      \]
    </p>
  </div>

  <p style="margin-top:.75rem;">
    Consistency ensures that increasing sample size improves accuracy.
  </p>

  <p class="muted-mini">
    Most classical estimators are consistent under regularity conditions.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Mean squared error (MSE)</h2>
  </div>

  <div class="card">
    <p style="margin:0;">
      \[
      MSE(\hat{\theta}) = \text{Var}(\hat{\theta}) + \text{Bias}(\hat{\theta})^2.
      \]
    </p>
  </div>

  <p style="margin-top:.75rem;">
    MSE combines accuracy and stability into a single measure.
  </p>

  <ul class="bullets">
    <li>Allows biased estimators to outperform unbiased ones if variance is much lower.</li>
    <li>Central in shrinkage and regularization methods.</li>
  </ul>
</section>

<section class="section">
  <div class="section-head">
    <h2>6) No universal “best” estimator</h2>
  </div>

  <div class="card">
    <p style="margin:0;">
      The optimal choice depends on:
    </p>
  </div>

  <ul class="bullets" style="margin-top:.75rem;">
    <li>Sample size</li>
    <li>Model assumptions</li>
    <li>Loss function</li>
    <li>Practical constraints</li>
  </ul>

  <p class="muted-mini">
    Inference is context-dependent.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>7) Common misconceptions</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>“Unbiased means optimal.”</h3>
      <p>
        Lower MSE may be more important than zero bias.
      </p>
    </div>

    <div class="card">
      <h3>“Consistency guarantees small error.”</h3>
      <p>
        Consistency is asymptotic; finite-sample behavior may still be poor.
      </p>
    </div>

    <div class="card">
      <h3>“Efficiency applies universally.”</h3>
      <p>
        Efficiency comparisons depend on model assumptions.
      </p>
    </div>

    <div class="card">
      <h3>“One estimator dominates in all settings.”</h3>
      <p>
        Trade-offs are unavoidable in realistic problems.
      </p>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Define unbiasedness, variance, efficiency, and consistency</li>
        <li>Understand MSE as a combined performance measure</li>
        <li>Recognize trade-offs in estimator selection</li>
        <li>Prepare for applied estimation decisions</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">
        Next, we formalize the inference workflow:
        <strong>Estimator → Standard Error → Confidence Interval / Test</strong>.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/inference/foundations/inference-pipeline-estimator-se-ci-test/">
          Next lesson: 10. The Estimator → SE → CI/Test Pipeline →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/inference/foundations/bias-and-variance-intuition/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 8: Bias and Variance
          </a>
        </div>
      </div>
    </div>

  </div>
</section>