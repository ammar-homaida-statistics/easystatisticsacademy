---
layout: default
title: "4. Estimators vs Estimates"
description: "Distinguish clearly between an estimator (a rule or formula) and an estimate (a realized number). Understand why this distinction is essential for inference."
permalink: /inference/foundations/estimators-vs-estimates/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem; letter-spacing:0.5px;">🚧 Lesson Under Construction</h2>
      <p style="margin:0; font-size:1.05rem; color:#5d4037; line-height:1.6;">
        Version 0 is published first to lock the structure and the correct conceptual flow.
        Worked examples, visuals, and software demonstrations will be added later without changing the lesson order.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update "last visited lesson" for Inference Block 1 -->
<script>
  (function () {
    var KEY = "esa_continue_inference_foundations_lesson_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/foundations/estimators-vs-estimates/",
      label: "Lesson 4 — Estimators vs Estimates",
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
        <span class="badge">Lesson 4</span>
        <span class="badge">Estimation</span>
        <span class="badge">Core Distinction</span>
      </div>

      <h1>4. Estimators vs Estimates</h1>
      <p class="lead">
        An <strong>estimator</strong> is a rule or formula applied to data.
        An <strong>estimate</strong> is the numerical result you obtain from one sample.
        Confusing the two leads to major interpretation errors in inference.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/foundations/">Back to Block 1</a>
        <a class="btn btn-outline" href="/inference/">Statistical Inference home</a>
      </div>

      <p class="muted-mini">
        Version 0: conceptual clarity first. Formal properties will follow in later lessons.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      By the end of this lesson, you should be able to define an estimator formally,
      distinguish it from an estimate, and explain why the estimator is treated as a random variable.
    </p>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Key idea</h2>
      <p style="margin:0;">
        <strong>Estimator = rule. Estimate = number.</strong>
        The estimator varies across samples; the estimate is one realized value.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) What is an estimator?</h2>
    <p>
      An estimator is a function of the sample used to estimate a population parameter.
      It is defined before observing the data.
    </p>
  </div>

  <div class="card">
    <p style="margin:0;">
      If the sample is \(X_1, X_2, \dots, X_n\), then  
      the sample mean estimator is  
      \(\bar{X} = \frac{1}{n}\sum_{i=1}^n X_i\).
    </p>
  </div>

  <p style="margin-top:.75rem;">
    Notice: this formula is defined independently of the specific values observed.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) What is an estimate?</h2>
    <p>
      Once you observe a specific dataset, you plug the values into the estimator formula.
      The resulting number is the estimate.
    </p>
  </div>

  <div class="card">
    <p style="margin:0;">
      If your observed data produce \(\bar{x} = 72.4\),  
      then 72.4 is the <strong>estimate</strong> of \(\mu\).
    </p>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    Lowercase letters (e.g., \(\bar{x}\)) are often used to denote realized values.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Why the distinction matters</h2>
    <p>
      The estimator has a sampling distribution.
      The estimate does not.
    </p>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Estimator (random)</h3>
      <ul class="bullets">
        <li>Depends on random sample</li>
        <li>Has expectation, variance</li>
        <li>Used to derive SE and CI</li>
      </ul>
    </div>

    <div class="card">
      <h3>Estimate (fixed number)</h3>
      <ul class="bullets">
        <li>Observed from one dataset</li>
        <li>No distribution by itself</li>
        <li>Used in reporting results</li>
      </ul>
    </div>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    Statements like “the estimate has variance” are technically incorrect.
    The estimator has variance; the estimate is one realized outcome.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Examples across common parameters</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Population mean</h3>
      <p>
        Parameter: \(\mu\)  
        Estimator: \(\bar{X}\)  
        Estimate: \(\bar{x}\)
      </p>
    </div>

    <div class="card">
      <h3>Population proportion</h3>
      <p>
        Parameter: \(p\)  
        Estimator: \(\hat{P}\)  
        Estimate: \(\hat{p}\)
      </p>
    </div>

    <div class="card">
      <h3>Regression slope</h3>
      <p>
        Parameter: \(\beta\)  
        Estimator: \(\hat{\beta}\)  
        Estimate: numeric value from sample
      </p>
    </div>

    <div class="card">
      <h3>Variance</h3>
      <p>
        Parameter: \(\sigma^2\)  
        Estimator: \(S^2\)  
        Estimate: observed \(s^2\)
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Properties apply to estimators, not estimates</h2>
    <p>
      When we discuss properties like unbiasedness, consistency, and efficiency,
      we are referring to the estimator as a random variable.
    </p>
  </div>

  <div class="card">
    <ul class="bullets">
      <li><strong>Unbiasedness:</strong> \(E(\hat{\theta}) = \theta\)</li>
      <li><strong>Variance:</strong> measures spread of estimator across samples</li>
      <li><strong>Consistency:</strong> estimator converges to parameter as \(n \to \infty\)</li>
    </ul>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    These properties cannot be evaluated from a single observed estimate alone.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>6) Common misconceptions</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>“The estimate is unbiased.”</h3>
      <p>
        Unbiasedness is a property of the estimator’s distribution,
        not of one realized estimate.
      </p>
    </div>

    <div class="card">
      <h3>“We can judge variance from one dataset.”</h3>
      <p>
        Variance refers to variability across repeated samples,
        not variability within one sample.
      </p>
    </div>

    <div class="card">
      <h3>“Estimator and statistic are different.”</h3>
      <p>
        In most contexts, an estimator is simply a statistic used for estimation.
      </p>
    </div>

    <div class="card">
      <h3>“More decimal places mean better estimation.”</h3>
      <p>
        Precision in reporting does not equal precision in inference.
        Precision is determined by the estimator’s variability.
      </p>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Define estimator as a rule and estimate as a realized value</li>
        <li>Explain why estimators are random variables</li>
        <li>Understand that inferential properties apply to estimators</li>
        <li>Prepare for formal discussion of sampling distributions and SE</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">
        Next, we formalize the concept of the
        <strong>sampling distribution</strong> as the bridge from estimation to uncertainty quantification.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/inference/foundations/sampling-distributions-bridge/">
          Next lesson: 5. Sampling Distributions (Bridge From Probability) →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/inference/foundations/statistics-as-random-variables/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 3: Statistics as Random Variables
          </a>
        </div>
      </div>
    </div>

  </div>
</section>