---
layout: default
title: "3. One-Sample t Test for a Mean (σ Unknown)"
description: "Conduct and interpret a one-sample t test for a population mean when the population standard deviation is unknown."
permalink: /inference/classical-tests/one-sample-t-test-for-mean/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem; letter-spacing:0.5px;">
        🚧 Lesson Under Construction
      </h2>
      <p style="margin:0; font-size:1.05rem; color:#5d4037; line-height:1.6;">
        Version 0 establishes the formal structure of the one-sample t test.
        Worked examples, diagnostic checks, and software demonstrations will be added later.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update continue-reading keys -->
<script>
  (function () {
    var KEY = "esa_continue_inference_classical_tests_lesson_v0";

    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/classical-tests/one-sample-t-test-for-mean/",
      label: "Lesson 3 — One-Sample t Test for a Mean",
      ts: Date.now()
    }));

    localStorage.setItem("esa_continue_inference_last_block_v0", JSON.stringify({
      url: "/inference/classical-tests/",
      label: "Block 4 — Classical Tests",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 4</span>
        <span class="badge">Lesson 3</span>
        <span class="badge">t Test</span>
        <span class="badge">σ Unknown</span>
      </div>

      <h1>3. One-Sample t Test for a Mean (σ Unknown)</h1>

      <p class="lead">
        The one-sample t test evaluates whether a sample mean
        differs from a hypothesized population mean
        when the population standard deviation is unknown
        and must be estimated from the sample.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/classical-tests/">Back to Block 4</a>
        <a class="btn btn-outline" href="/inference/">Statistical Inference home</a>
      </div>

      <p class="muted-mini">
        This is the standard test for a single mean in practice.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      Formulate hypotheses for a mean,
      compute the t statistic,
      determine degrees of freedom,
      and interpret the p-value correctly.
    </p>
  </div>

  <div class="callout">
    <div class="callout-copy">
      <h2>When to use this test</h2>
      <p style="margin:0;">
        Use the one-sample t test when:
        <br>
        • The population standard deviation is unknown  
        • Observations are independent  
        • The population is approximately normal or the sample size is moderate/large
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Hypotheses</h2>
  </div>

  <div class="card">
    \[
    H_0: \mu = \mu_0
    \quad\text{vs}\quad
    H_1: \mu \ne \mu_0
    \]
  </div>

  <p class="muted-mini">
    One-sided alternatives (greater or less) may also be used when justified.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Test statistic</h2>
  </div>

  <div class="card">
    \[
    t =
    \frac{\bar{X} - \mu_0}
    {S / \sqrt{n}}
    \]
  </div>

  <p style="margin-top:.75rem;">
    Here, \( S \) is the sample standard deviation.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Sampling distribution under \(H_0\)</h2>
  </div>

  <div class="card">
    \[
    t \sim t_{n-1}
    \quad\text{if } H_0 \text{ is true}
    \]
  </div>

  <p class="muted-mini">
    The degrees of freedom are:
    \[
    df = n - 1
    \]
  </p>

  <p>
    The t distribution has heavier tails than the normal distribution,
    accounting for additional uncertainty from estimating \( \sigma \).
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Decision rule</h2>
  </div>

  <div class="card">
    Reject \(H_0\) if:
    \[
    |t| > t_{\alpha/2,\,n-1}
    \]
  </div>

  <div class="card" style="margin-top:1rem;">
    Equivalent p-value rule:
    <br><br>
    Reject if \( p \le \alpha \)
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Interpretation</h2>
  </div>

  <div class="card">
    If the p-value is small,
    the observed sample mean is unlikely under \(H_0\),
    providing statistical evidence against the null hypothesis.
  </div>

  <p class="muted-mini">
    Failure to reject does not prove the null hypothesis.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>6) Connection to confidence interval</h2>
  </div>

  <div class="card">
    The corresponding \(100(1-\alpha)\%\) confidence interval is:
    \[
    \bar{X}
    \pm
    t_{\alpha/2,\,n-1}
    \frac{S}{\sqrt{n}}
    \]
  </div>

  <p>
    Rejecting \(H_0\) is equivalent to the null value \( \mu_0 \)
    lying outside this interval.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>7) Comparison with z test</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>z test</h3>
      <p style="margin:0;">
        Uses known \( \sigma \)  
        Standard normal distribution
      </p>
    </div>

    <div class="card">
      <h3>t test</h3>
      <p style="margin:0;">
        Uses sample \( S \)  
        t distribution with \( n-1 \) df
      </p>
    </div>
  </div>

  <p class="muted-mini">
    As \( n \) increases, the t distribution approaches the normal distribution.
  </p>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Formulate and test hypotheses for a mean</li>
        <li>Compute the t statistic correctly</li>
        <li>Determine degrees of freedom</li>
        <li>Interpret p-values and intervals responsibly</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next lesson</h2>
      <p style="margin:0;">
        We now examine the paired t test,
        which reduces matched data to a one-sample test on differences.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/inference/classical-tests/paired-t-test/">
          Next lesson: 4. Paired t Test →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/inference/classical-tests/one-sample-z-test-for-mean/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 2: One-Sample z Test
          </a>
        </div>
      </div>
    </div>
  </div>
</section>