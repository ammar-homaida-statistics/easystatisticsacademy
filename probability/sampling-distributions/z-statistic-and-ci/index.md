---
layout: default
title: "3. z-Statistic & Confidence Intervals"
description: "Standardization with known σ: z-statistic, Normal sampling distribution of the mean, and confidence interval construction."
permalink: /probability/sampling-distributions/z-statistic-and-ci/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem;">🚧 Lesson Under Construction</h2>
      <p style="margin:0; font-size:1.05rem;">
        Version 0 introduces the z-statistic and the logic of confidence intervals under known variance.
        Worked examples and graphical illustrations will be added in Version 1.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Continue Reading Tracking -->
<script>
  (function () {
    var KEY = "esa_continue_probability_sampling_distributions_lesson_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/probability/sampling-distributions/z-statistic-and-ci/",
      label: "Lesson 3 — z-Statistic & Confidence Intervals",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 7</span>
        <span class="badge">Lesson 3</span>
        <span class="badge">z</span>
        <span class="badge">Confidence Intervals</span>
      </div>

      <h1>3. z-Statistic & Confidence Intervals</h1>

      <p class="lead">
        When the population variance \(\sigma^2\) is known (or the sample size is large),
        we can standardize the estimator and use the
        <strong>Normal distribution</strong> to perform inference.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/probability/sampling-distributions/">Back to Block 7</a>
        <a class="btn btn-outline" href="/probability/">Probability home</a>
      </div>

      <p class="muted-mini">
        Standardization transforms an estimator into a known reference distribution.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      By the end of this lesson, you should be able to derive the z-statistic,
      construct confidence intervals for a mean with known \(\sigma\),
      and interpret coverage probability correctly.
    </p>
  </div>

  <div class="callout">
    <div class="callout-copy">
      <h2>Key idea</h2>
      <p style="margin:0;">
        Inference = estimate ± (critical value × standard error).
        The z-statistic standardizes the estimator so that it follows \(N(0,1)\).
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Sampling distribution of the mean</h2>
  </div>

  <div class="card">
    <p style="margin:0;">
      If \(X_1,\dots,X_n\) are i.i.d. with mean \(\mu\) and variance \(\sigma^2\),
      then:
      \[
      \mathbb{E}[\overline{X}] = \mu,
      \qquad
      \operatorname{Var}(\overline{X}) = \frac{\sigma^2}{n}.
      \]
    </p>
  </div>

  <div class="card" style="margin-top:1rem;">
    <p style="margin:0;">
      If the population is Normal (or \(n\) is large),
      \[
      \overline{X} \sim N\!\left(\mu,\frac{\sigma^2}{n}\right).
      \]
    </p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) The z-statistic</h2>
  </div>

  <div class="card">
    <p style="margin:0; font-size:1.05rem;">
      \[
      Z=\frac{\overline{X}-\mu}{\sigma/\sqrt{n}}.
      \]
    </p>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    Under the assumptions above, \(Z \sim N(0,1)\).
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Confidence interval construction</h2>
  </div>

  <div class="card">
    <p style="margin:0;">
      A \(100(1-\alpha)\%\) confidence interval for \(\mu\) is:
      \[
      \overline{X} \pm z_{1-\alpha/2}\frac{\sigma}{\sqrt{n}}.
      \]
    </p>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Coverage meaning</h2>
      <p style="margin:0;">
        In repeated sampling, this procedure captures the true parameter
        approximately \(100(1-\alpha)\%\) of the time.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Hypothesis testing using z</h2>
  </div>

  <div class="card">
    <p style="margin:0;">
      To test \(H_0:\mu=\mu_0\), compute:
      \[
      Z=\frac{\overline{X}-\mu_0}{\sigma/\sqrt{n}}.
      \]
    </p>
  </div>

  <div class="card" style="margin-top:1rem;">
    <ul class="bullets">
      <li>Reject if \(|Z| > z_{1-\alpha/2}\) (two-sided test).</li>
      <li>\(\alpha\) controls Type I error.</li>
    </ul>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Derive and interpret the z-statistic</li>
        <li>Construct confidence intervals with known variance</li>
        <li>Understand long-run coverage logic</li>
        <li>Perform basic hypothesis testing with z</li>
        <li>Prepare for the t-distribution case (unknown \(\sigma\))</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">
        In practice, \(\sigma\) is usually unknown.
        Next, we introduce the <strong>t-distribution</strong>.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/probability/sampling-distributions/t-distribution-and-t-test/">
          Next lesson: 4. t-Distribution & the t-Statistic →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/probability/sampling-distributions/standard-error-and-estimators/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 2 — Standard Error & Estimators
          </a>
        </div>
      </div>
    </div>
  </div>
</section>