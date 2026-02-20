---
layout: default
title: "4. t-Distribution & the t-Statistic"
description: "Inference when σ is unknown: Student’s t distribution, degrees of freedom, and why it replaces z in practical estimation."
permalink: /probability/sampling-distributions/t-distribution-and-t-test/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem;">🚧 Lesson Under Construction</h2>
      <p style="margin:0; font-size:1.05rem;">
        Version 0 introduces Student’s t distribution and its role in inference when σ is unknown.
        Worked examples and simulation-based intuition will be added in Version 1.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Continue Reading Tracking -->
<script>
  (function () {
    var KEY = "esa_continue_probability_sampling_distributions_lesson_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/probability/sampling-distributions/t-distribution-and-t-test/",
      label: "Lesson 4 — t-Distribution & the t-Statistic",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 7</span>
        <span class="badge">Lesson 4</span>
        <span class="badge">t</span>
        <span class="badge">Degrees of Freedom</span>
      </div>

      <h1>4. t-Distribution & the t-Statistic</h1>

      <p class="lead">
        In real applications, the population variance \(\sigma^2\) is usually unknown.
        Replacing \(\sigma\) with the sample standard deviation \(S\)
        introduces extra uncertainty.  
        That uncertainty changes the reference distribution from Normal to <strong>Student’s t</strong>.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/probability/sampling-distributions/">Back to Block 7</a>
        <a class="btn btn-outline" href="/probability/">Probability home</a>
      </div>

      <p class="muted-mini">
        The t-distribution accounts for estimating σ.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      By the end of this lesson, you should be able to derive the t-statistic,
      explain degrees of freedom, and construct confidence intervals and tests
      for a mean when σ is unknown.
    </p>
  </div>

  <div class="callout">
    <div class="callout-copy">
      <h2>Key idea</h2>
      <p style="margin:0;">
        Replacing \(\sigma\) with \(S\) increases uncertainty.
        The resulting standardized statistic follows a <strong>t-distribution</strong>.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Why z no longer works</h2>
  </div>

  <div class="card">
    <p style="margin:0;">
      Previously:
      \[
      Z = \frac{\overline{X}-\mu}{\sigma/\sqrt{n}}
      \sim N(0,1).
      \]
    </p>
  </div>

  <div class="card" style="margin-top:1rem;">
    <p style="margin:0;">
      But when \(\sigma\) is unknown, we estimate it using:
      \[
      S^2 = \frac{1}{n-1}\sum_{i=1}^n (X_i-\overline{X})^2.
      \]
    </p>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    Now both numerator and denominator are random.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) The t-statistic</h2>
  </div>

  <div class="card">
    <p style="margin:0; font-size:1.05rem;">
      \[
      T=\frac{\overline{X}-\mu}{S/\sqrt{n}}.
      \]
    </p>
  </div>

  <div class="card" style="margin-top:1rem;">
    <p style="margin:0;">
      If \(X_1,\dots,X_n\) are Normal, then:
      \[
      T \sim t_{n-1}.
      \]
    </p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Degrees of freedom</h2>
  </div>

  <div class="card">
    <p style="margin:0;">
      The t-distribution depends on degrees of freedom (df):
      \[
      \text{df} = n-1.
      \]
    </p>
  </div>

  <div class="callout" style="margin-top:1rem;">
    <div class="callout-copy">
      <h2>Interpretation</h2>
      <p style="margin:0;">
        One degree of freedom is lost because the sample mean is estimated first.
        Larger df → t approaches Normal.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Confidence interval (unknown σ)</h2>
  </div>

  <div class="card">
    <p style="margin:0;">
      A \(100(1-\alpha)\%\) confidence interval for \(\mu\):
      \[
      \overline{X} \pm t_{1-\alpha/2,\,n-1}\frac{S}{\sqrt{n}}.
      \]
    </p>
  </div>

  <p class="muted-mini" style="margin-top:.75rem;">
    Compare with z-interval: critical value is larger for small n.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Hypothesis testing</h2>
  </div>

  <div class="card">
    <p style="margin:0;">
      To test \(H_0:\mu=\mu_0\):
      \[
      T=\frac{\overline{X}-\mu_0}{S/\sqrt{n}}.
      \]
    </p>
  </div>

  <div class="card" style="margin-top:1rem;">
    <ul class="bullets">
      <li>Reject if \(|T| > t_{1-\alpha/2,n-1}\).</li>
      <li>Controls Type I error at level \(\alpha\).</li>
    </ul>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>6) Shape comparison: t vs Normal</h2>
  </div>

  <div class="card">
    <ul class="bullets">
      <li>t has heavier tails.</li>
      <li>More uncertainty for small samples.</li>
      <li>As \(n \to \infty\), \(t_{n-1} \to N(0,1)\).</li>
    </ul>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Derive the t-statistic</li>
        <li>Explain degrees of freedom</li>
        <li>Construct t-based confidence intervals</li>
        <li>Perform t hypothesis tests</li>
        <li>Understand why t → Normal as n increases</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">
        Next, we study the <strong>Chi-Square distribution</strong>,
        which governs inference about variance.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/probability/sampling-distributions/chi-square-and-variance/">
          Next lesson: 5. Chi-Square Distribution →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/probability/sampling-distributions/z-statistic-and-ci/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 3 — z-Statistic & Confidence Intervals
          </a>
        </div>
      </div>
    </div>
  </div>
</section>