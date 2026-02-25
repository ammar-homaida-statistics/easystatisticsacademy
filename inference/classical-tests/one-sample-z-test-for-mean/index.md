---
layout: default
title: "2. One-Sample z Test for a Mean (σ Known)"
description: "Conduct and interpret a one-sample z test for a population mean when the population standard deviation is known."
permalink: /inference/classical-tests/one-sample-z-test-for-mean/
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
        Version 0 establishes the formal structure of the one-sample z test.
        This case is rare in practice but clarifies the logic of standardization.
        Numerical examples and software demonstrations will be added later.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update continue-reading keys -->
<script>
  (function () {
    var KEY = "esa_continue_inference_classical_tests_lesson_v0";

    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/classical-tests/one-sample-z-test-for-mean/",
      label: "Lesson 2 — One-Sample z Test for a Mean",
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
        <span class="badge">Lesson 2</span>
        <span class="badge">z Test</span>
        <span class="badge">σ Known</span>
      </div>

      <h1>2. One-Sample z Test for a Mean (σ Known)</h1>

      <p class="lead">
        The one-sample z test evaluates whether a sample mean
        differs from a hypothesized population mean
        when the population standard deviation \( \sigma \) is known.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/classical-tests/">Back to Block 4</a>
        <a class="btn btn-outline" href="/inference/">Statistical Inference home</a>
      </div>

      <p class="muted-mini">
        This test illustrates pure standardization.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      Formulate hypotheses for a mean,
      compute the z test statistic,
      and interpret the resulting p-value correctly.
    </p>
  </div>

  <div class="callout">
    <div class="callout-copy">
      <h2>When to use this test</h2>
      <p style="margin:0;">
        Use the z test when:
        <br>
        • The population standard deviation \( \sigma \) is known  
        • Observations are independent  
        • The population is normal or sample size is large
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
    One-sided alternatives are also possible depending on the research question.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Test statistic</h2>
  </div>

  <div class="card">
    \[
    z =
    \frac{\bar{X} - \mu_0}
    {\sigma / \sqrt{n}}
    \]
  </div>

  <p style="margin-top:.75rem;">
    This statistic measures how many standard errors
    the sample mean lies from the hypothesized mean.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Sampling distribution under \(H_0\)</h2>
  </div>

  <div class="card">
    \[
    z \sim N(0,1)
    \quad\text{if } H_0 \text{ is true}
    \]
  </div>

  <p class="muted-mini">
    This follows from standardization of the sample mean.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Decision rule</h2>
  </div>

  <div class="card">
    Reject \(H_0\) if:
    \[
    |z| > z_{\alpha/2}
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
    the observed mean is unlikely under \(H_0\),
    providing evidence against the null hypothesis.
  </div>

  <p class="muted-mini">
    The p-value does not measure the size of the effect.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>6) Connection to confidence interval</h2>
  </div>

  <div class="card">
    The corresponding \(100(1-\alpha)\%\) confidence interval is:
    \[
    \bar{X} \pm z_{\alpha/2} \frac{\sigma}{\sqrt{n}}
    \]
  </div>

  <p>
    Rejecting \(H_0\) is equivalent to
    the null value \( \mu_0 \) lying outside this interval.
  </p>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Formulate hypotheses for a mean</li>
        <li>Compute the z statistic correctly</li>
        <li>Use the standard normal distribution</li>
        <li>Interpret results responsibly</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next lesson</h2>
      <p style="margin:0;">
        In practice, the population standard deviation is rarely known.
        We now move to the one-sample t test.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/inference/classical-tests/one-sample-t-test-for-mean/">
          Next lesson: 3. One-Sample t Test for a Mean →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/inference/classical-tests/decision-framework-and-assumptions/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 1: Decision Framework and Assumptions
          </a>
        </div>
      </div>
    </div>
  </div>
</section>