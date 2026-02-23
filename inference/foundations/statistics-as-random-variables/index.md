---
layout: default
title: "3. Statistics as Random Variables"
description: "Understand why statistics are random variables, how sampling distributions arise, and why randomness belongs to estimators—not parameters."
permalink: /inference/foundations/statistics-as-random-variables/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem; letter-spacing:0.5px;">🚧 Lesson Under Construction</h2>
      <p style="margin:0; font-size:1.05rem; color:#5d4037; line-height:1.6;">
        Version 0 is published first to lock the structure and the correct conceptual flow. Examples, graphs,
        and software demonstrations will be added later without changing the lesson order.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update "last visited lesson" for Inference Block 1 -->
<script>
  (function () {
    var KEY = "esa_continue_inference_foundations_lesson_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/foundations/statistics-as-random-variables/",
      label: "Lesson 3 — Statistics as Random Variables",
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
        <span class="badge">Lesson 3</span>
        <span class="badge">Sampling</span>
        <span class="badge">Randomness</span>
      </div>

      <h1>3. Statistics as Random Variables</h1>
      <p class="lead">
        A statistic is not just a number — it is a <strong>random variable</strong>.
        Because the sample is random, any quantity computed from it varies across samples.
        This variability is the foundation of statistical inference.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/foundations/">Back to Block 1</a>
        <a class="btn btn-outline" href="/inference/">Statistical Inference home</a>
      </div>

      <p class="muted-mini">
        Version 0: structure first. Visuals and simulations will be added later.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      By the end of this lesson, you should be able to explain why statistics are random variables,
      describe the idea of repeated sampling, and define a <strong>sampling distribution</strong> conceptually.
    </p>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Key idea</h2>
      <p style="margin:0;">
        <strong>Randomness belongs to the sampling process.</strong>
        Because different random samples produce different estimates,
        the statistic itself has a probability distribution.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) From fixed data to random samples</h2>
    <p>
      When you compute a statistic from one observed dataset, it looks like a single number.
      But imagine repeating the sampling process many times.
    </p>
  </div>

  <div class="card">
    <p style="margin:0;">
      Each time you draw a new random sample from the same population,
      you would compute a new value of the statistic.
    </p>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    Even if the population parameter stays fixed, the sample mean, sample proportion,
    or regression slope would change from sample to sample.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Statistics are functions of random data</h2>
    <p>
      A statistic is a function of the sample:
    </p>
  </div>

  <div class="card">
    <p style="font-size:1.1rem; margin:0;">
      If the sample is \(X_1, X_2, \dots, X_n\), then  
      \(\bar{X} = \frac{1}{n}\sum_{i=1}^n X_i\)
    </p>
  </div>

  <p style="margin-top:.75rem;">
    Because the sample values \(X_i\) are random variables (under random sampling),
    any function of them — including \(\bar{X}\) — is also a random variable.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) The sampling distribution</h2>
    <p>
      The <strong>sampling distribution</strong> of a statistic describes
      how that statistic varies across repeated samples of the same size.
    </p>
  </div>

  <div class="card">
    <p style="margin:0;">
      Sampling distribution = probability distribution of a statistic.
    </p>
  </div>

  <div class="grid grid-2" style="margin-top:1rem;">
    <div class="card">
      <h3>Example: Sample mean</h3>
      <p>
        If you repeatedly sample size \(n\) and compute \(\bar{X}\),
        the values of \(\bar{X}\) form a distribution centered at \(\mu\).
      </p>
    </div>

    <div class="card">
      <h3>Example: Sample proportion</h3>
      <p>
        Repeated values of \(\hat{p}\) form a distribution centered at \(p\).
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Why this matters for inference</h2>
    <p>
      Inference depends on knowing (or approximating) the sampling distribution.
    </p>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Uncertainty measurement</h3>
      <p>
        The spread of the sampling distribution determines the
        <strong>standard error</strong>.
      </p>
    </div>

    <div class="card">
      <h3>Confidence intervals</h3>
      <p>
        Intervals are constructed using quantiles of the sampling distribution.
      </p>
    </div>

    <div class="card">
      <h3>Hypothesis tests</h3>
      <p>
        Test statistics compare observed values to their sampling distribution under an assumption.
      </p>
    </div>

    <div class="card">
      <h3>Large-sample logic</h3>
      <p>
        As sample size increases, sampling distributions often become approximately normal (CLT).
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Parameter vs statistic revisited</h2>
    <p>
      This is the central structural difference in inference:
    </p>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Parameter</h3>
      <ul class="bullets">
        <li>Belongs to the population</li>
        <li>Fixed (frequentist framework)</li>
        <li>Unknown</li>
      </ul>
    </div>

    <div class="card">
      <h3>Statistic</h3>
      <ul class="bullets">
        <li>Computed from sample</li>
        <li>Random variable</li>
        <li>Has sampling distribution</li>
      </ul>
    </div>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    Confusing these two leads to incorrect interpretations of standard errors and p-values.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>6) Common misconceptions</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>“We only have one sample, so nothing is random.”</h3>
      <p>
        Even with one observed sample, the conceptual sampling process defines the distribution.
      </p>
    </div>

    <div class="card">
      <h3>“The mean itself varies in the population.”</h3>
      <p>
        The population mean is fixed. The sample mean varies because the sample varies.
      </p>
    </div>

    <div class="card">
      <h3>“Randomness disappears for large n.”</h3>
      <p>
        Variability decreases as n increases, but it never becomes zero.
      </p>
    </div>

    <div class="card">
      <h3>“Sampling distribution = data distribution.”</h3>
      <p>
        The distribution of the statistic is different from the distribution of individual observations.
      </p>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Explain why statistics are random variables</li>
        <li>Define a sampling distribution conceptually</li>
        <li>Understand that randomness belongs to the sample, not the parameter</li>
        <li>Connect sampling distributions to SE, CI, and hypothesis testing</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">
        Next, we distinguish clearly between
        <strong>estimators</strong> (rules) and
        <strong>estimates</strong> (realized numbers).
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/inference/foundations/estimators-vs-estimates/">
          Next lesson: 4. Estimators vs Estimates →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/inference/foundations/populations-parameters-target/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 2: Populations, Parameters, and the Target of Estimation
          </a>
        </div>
      </div>
    </div>

  </div>
</section>