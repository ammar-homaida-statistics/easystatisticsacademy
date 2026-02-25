---
layout: default
title: "5. Two-Sample t Test (Independent Samples)"
description: "Conduct and interpret a two-sample t test to compare the means of two independent groups."
permalink: /inference/classical-tests/two-sample-t-test-independent/
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
        Version 0 establishes the formal structure of the two-sample t test.
        Detailed examples (Welch vs pooled) and full software demonstrations will be added later.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update continue-reading keys -->
<script>
  (function () {
    var KEY = "esa_continue_inference_classical_tests_lesson_v0";

    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/classical-tests/two-sample-t-test-independent/",
      label: "Lesson 5 — Two-Sample t Test (Independent)",
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
        <span class="badge">Lesson 5</span>
        <span class="badge">Independent Samples</span>
        <span class="badge">Two Means</span>
      </div>

      <h1>5. Two-Sample t Test (Independent Samples)</h1>

      <p class="lead">
        The two-sample t test evaluates whether the means of two independent
        populations differ. It compares the difference of sample means
        to its estimated standard error.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/classical-tests/">Back to Block 4</a>
        <a class="btn btn-outline" href="/inference/">Statistical Inference home</a>
      </div>

      <p class="muted-mini">
        Independence between groups is the key structural assumption.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      Formulate hypotheses for comparing two means,
      compute the test statistic,
      and interpret results under independent sampling.
    </p>
  </div>

  <div class="callout">
    <div class="callout-copy">
      <h2>When to use this test</h2>
      <p style="margin:0;">
        Use the two-sample t test when:
        <br>
        • Two groups are independent  
        • Each group is approximately normal or sample sizes are moderate/large  
        • Population standard deviations are unknown
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Parameter and hypotheses</h2>
  </div>

  <div class="card">
    \[
    \text{Parameter: } \mu_1 - \mu_2
    \]
  </div>

  <div class="card" style="margin-top:1rem;">
    \[
    H_0: \mu_1 - \mu_2 = 0
    \quad\text{vs}\quad
    H_1: \mu_1 - \mu_2 \ne 0
    \]
  </div>

  <p class="muted-mini">
    One-sided alternatives are possible if justified in advance.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Test statistic (Welch version)</h2>
  </div>

  <div class="card">
    \[
    t =
    \frac{\bar{X}_1 - \bar{X}_2}
    {\sqrt{\frac{S_1^2}{n_1} + \frac{S_2^2}{n_2}}}
    \]
  </div>

  <p style="margin-top:.75rem;">
    Where:
    <br>
    • \( \bar{X}_1, \bar{X}_2 \) are sample means  
    • \( S_1, S_2 \) are sample standard deviations  
    • \( n_1, n_2 \) are sample sizes
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Degrees of freedom</h2>
  </div>

  <div class="card">
    Approximate (Welch–Satterthwaite):
    \[
    df \approx
    \frac{\left(\frac{S_1^2}{n_1} + \frac{S_2^2}{n_2}\right)^2}
    {\frac{\left(\frac{S_1^2}{n_1}\right)^2}{n_1-1}
    +
    \frac{\left(\frac{S_2^2}{n_2}\right)^2}{n_2-1}}
    \]
  </div>

  <p class="muted-mini">
    Welch's test does not assume equal variances and is typically preferred.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Equal variance (pooled) version</h2>
  </div>

  <div class="card">
    Pooled variance:
    \[
    S_p^2 =
    \frac{(n_1-1)S_1^2 + (n_2-1)S_2^2}
    {n_1 + n_2 - 2}
    \]
  </div>

  <div class="card" style="margin-top:1rem;">
    Test statistic:
    \[
    t =
    \frac{\bar{X}_1 - \bar{X}_2}
    {S_p \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}}
    \]
  </div>

  <p class="muted-mini">
    Degrees of freedom: \( n_1 + n_2 - 2 \)
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Interpretation</h2>
  </div>

  <div class="card">
    A small p-value indicates that the observed difference in sample means
    would be unlikely if the true population means were equal.
  </div>

  <p class="muted-mini">
    Statistical significance does not imply practical importance.
  </p>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Formulate hypotheses for two independent means</li>
        <li>Compute Welch and pooled t statistics</li>
        <li>Understand variance assumptions</li>
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
        We now move to inference for a single population proportion
        using the one-proportion z test.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/inference/classical-tests/one-proportion-z-test/">
          Next lesson: 6. One-Proportion z Test →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/inference/classical-tests/paired-t-test/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 4: Paired t Test
          </a>
        </div>
      </div>
    </div>
  </div>
</section>