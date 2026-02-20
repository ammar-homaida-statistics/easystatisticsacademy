---
layout: default
title: "1. What Is a Sampling Distribution?"
description: "Sampling distributions: the distribution of a statistic under repeated sampling; variability, standard error idea, and why inference is possible."
permalink: /probability/sampling-distributions/what-is-a-sampling-distribution/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem; letter-spacing:0.5px;">🚧 Lesson Under Construction</h2>
      <p style="margin:0; font-size:1.05rem; color:#5d4037; line-height:1.6;">
        Version 0 is published first to lock the structure and the correct conceptual flow.
        Visual intuition, worked examples, and simulations will be added in Version 1.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update "last visited lesson" for Block 7 -->
<script>
  (function () {
    var KEY = "esa_continue_probability_sampling_distributions_lesson_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/probability/sampling-distributions/what-is-a-sampling-distribution/",
      label: "Lesson 1 — What Is a Sampling Distribution?",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 7</span>
        <span class="badge">Lesson 1</span>
        <span class="badge">Sampling</span>
        <span class="badge">Foundations</span>
      </div>

      <h1>1. What Is a Sampling Distribution?</h1>

      <p class="lead">
        A statistic (like \(\overline{X}\) or \(\hat{p}\)) is a random variable because it depends on a random sample.
        The <strong>sampling distribution</strong> describes how that statistic varies across repeated samples.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/probability/sampling-distributions/">Back to Block 7</a>
        <a class="btn btn-outline" href="/probability/">Probability home</a>
      </div>

      <p class="muted-mini">
        Inference works because sampling distributions create probability guarantees.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      By the end of this lesson, you should be able to define a sampling distribution,
      distinguish it from the population distribution, and explain why it is the engine of
      confidence intervals and hypothesis tests.
    </p>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Key idea</h2>
      <p style="margin:0;">
        The population distribution describes <strong>data values</strong>.
        The sampling distribution describes <strong>a statistic</strong> computed from data.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Population vs sample vs statistic</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Population model</h3>
      <p style="margin:0;">
        A random variable \(X\) has a population distribution, e.g.
        \(X \sim N(\mu,\sigma^2)\) or \(X \sim \text{Bernoulli}(p)\).
      </p>
    </div>

    <div class="card">
      <h3>Sample</h3>
      <p style="margin:0;">
        We observe \(X_1,\dots,X_n\) drawn from the same population model.
      </p>
    </div>
  </div>

  <div class="card" style="margin-top:1rem;">
    <h3>Statistic</h3>
    <p style="margin:0;">
      A statistic is any function of the sample:
      \[
      T=T(X_1,\dots,X_n).
      \]
      Examples: \(\overline{X}\), \(S^2\), \(\hat{p}\).
    </p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Definition of sampling distribution</h2>
    <p>
      Fix the population model (the “true” distribution). Now imagine repeating the sampling process many times.
      Each time we compute the statistic \(T\), we get a different value.
    </p>
  </div>

  <div class="card">
    <p style="margin:0; font-size:1.05rem;">
      The <strong>sampling distribution of \(T\)</strong> is the probability distribution of \(T\)
      across repeated samples of size \(n\) from the same population model.
    </p>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Short form</h2>
      <p style="margin:0;">
        Population distribution = distribution of <strong>data</strong>. <br/>
        Sampling distribution = distribution of a <strong>statistic</strong>.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Core example: the sample mean</h2>
    <p>
      The sample mean is
    </p>
  </div>

  <div class="card">
    <p style="margin:0; font-size:1.1rem;">
      \[
      \overline{X}=\frac{1}{n}\sum_{i=1}^n X_i.
      \]
    </p>
  </div>

  <div class="card" style="margin-top:1rem;">
    <p style="margin:0;">
      If \(X_1,\dots,X_n\) are i.i.d. with mean \(\mu\) and variance \(\sigma^2\), then:
      \[
      \mathbb{E}[\overline{X}] = \mu,
      \qquad
      \operatorname{Var}(\overline{X}) = \frac{\sigma^2}{n}.
      \]
    </p>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    This variance shrinkage is the mathematical reason why larger samples give more precise estimates.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Shape: exact vs approximate</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Exact sampling distribution</h3>
      <p style="margin:0;">
        Sometimes we can derive the exact distribution of \(T\)
        (e.g., Normal data → \(\overline{X}\) is Normal).
      </p>
    </div>

    <div class="card">
      <h3>Approximate sampling distribution</h3>
      <p style="margin:0;">
        Often we use the CLT:
        \[
        \frac{\overline{X}-\mu}{\sigma/\sqrt{n}}\approx N(0,1)
        \quad (\text{for large } n).
        \]
      </p>
    </div>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Why this matters</h2>
      <p style="margin:0;">
        Confidence intervals and hypothesis tests depend on knowing (exactly or approximately)
        the sampling distribution of the statistic you use.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Standard error (preview)</h2>
    <p>
      The standard deviation of a statistic’s sampling distribution is called its <strong>standard error</strong>.
    </p>
  </div>

  <div class="card">
    <p style="margin:0;">
      For the sample mean:
      \[
      \operatorname{SE}(\overline{X})=\sqrt{\operatorname{Var}(\overline{X})}=\frac{\sigma}{\sqrt{n}}.
      \]
    </p>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    In practice, \(\sigma\) is usually unknown and replaced by \(S\), leading to t-based inference later.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>6) Common confusion to avoid</h2>
  </div>

  <div class="card">
    <ul class="bullets">
      <li><strong>Histogram of data</strong> ≠ sampling distribution.</li>
      <li>The sampling distribution is about <strong>the statistic across samples</strong>, not the raw values in one sample.</li>
      <li>Changing \(n\) changes the sampling distribution (variance typically decreases as \(n\) increases).</li>
    </ul>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Define “sampling distribution” precisely</li>
        <li>Distinguish population distribution vs sampling distribution</li>
        <li>Know why \(\operatorname{Var}(\overline{X})=\sigma^2/n\) is fundamental</li>
        <li>Understand why inference relies on sampling distributions</li>
        <li>Prepare for standard error and estimator properties</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">
        Next, we define <strong>estimators</strong> and formalize uncertainty using <strong>standard error</strong>.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/probability/sampling-distributions/standard-error-and-estimators/">
          Next lesson: 2. Standard Error &amp; Estimators →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous block</div>
        <div class="mini-body">
          <a href="/probability/lln-clt/" style="color:#1a73e8; text-decoration:underline;">
            Block 6 — Law of Large Numbers &amp; CLT
          </a>
        </div>
      </div>
    </div>
  </div>
</section>