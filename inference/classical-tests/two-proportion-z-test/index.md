---
layout: default
title: "7. Two-Proportion z Test"
description: "Conduct and interpret a two-proportion z test to compare proportions from two independent groups."
permalink: /inference/classical-tests/two-proportion-z-test/
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
        Version 0 establishes the formal structure of the two-proportion z test.
        Worked numerical examples and software walkthroughs will be added later.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update continue-reading keys -->
<script>
  (function () {
    var KEY = "esa_continue_inference_classical_tests_lesson_v0";

    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/classical-tests/two-proportion-z-test/",
      label: "Lesson 7 — Two-Proportion z Test",
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
        <span class="badge">Lesson 7</span>
        <span class="badge">Two Proportions</span>
        <span class="badge">z Test</span>
      </div>

      <h1>7. Two-Proportion z Test</h1>

      <p class="lead">
        The two-proportion z test evaluates whether two independent
        population proportions differ.
        It compares the observed difference in sample proportions
        to its standard error under the null hypothesis.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/classical-tests/">Back to Block 4</a>
        <a class="btn btn-outline" href="/inference/">Statistical Inference home</a>
      </div>

      <p class="muted-mini">
        Independence between groups is required.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      Formulate hypotheses for comparing two proportions,
      compute the pooled standard error,
      and interpret the test result correctly.
    </p>
  </div>

  <div class="callout">
    <div class="callout-copy">
      <h2>When to use this test</h2>
      <p style="margin:0;">
        Use the two-proportion z test when:
        <br>
        • Two groups are independent  
        • Data consist of counts of successes in each group  
        • Large-sample success–failure conditions are satisfied
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
    \text{Parameter: } p_1 - p_2
    \]
  </div>

  <div class="card" style="margin-top:1rem;">
    \[
    H_0: p_1 - p_2 = 0
    \quad\text{vs}\quad
    H_1: p_1 - p_2 \ne 0
    \]
  </div>

  <p class="muted-mini">
    One-sided alternatives may be used if justified beforehand.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Sample proportions</h2>
  </div>

  <div class="card">
    \[
    \hat{p}_1 = \frac{X_1}{n_1},
    \quad
    \hat{p}_2 = \frac{X_2}{n_2}
    \]
  </div>

  <p>
    Where \( X_1, X_2 \) are the numbers of successes
    in samples of size \( n_1, n_2 \).
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Pooled proportion under \(H_0\)</h2>
  </div>

  <div class="card">
    \[
    \hat{p} =
    \frac{X_1 + X_2}{n_1 + n_2}
    \]
  </div>

  <p class="muted-mini">
    Under \(H_0\), both samples estimate the same population proportion.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Test statistic</h2>
  </div>

  <div class="card">
    \[
    z =
    \frac{\hat{p}_1 - \hat{p}_2}
    {\sqrt{
    \hat{p}(1-\hat{p})
    \left(
    \frac{1}{n_1} + \frac{1}{n_2}
    \right)
    }}
    \]
  </div>

  <p>
    The denominator uses the pooled estimate because the null assumes equal proportions.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Validity condition</h2>
  </div>

  <div class="card">
    Success–failure condition (under \(H_0\)):
    <br><br>
    \( n_1 \hat{p} \ge 10 \),  
    \( n_1 (1-\hat{p}) \ge 10 \),  
    \( n_2 \hat{p} \ge 10 \),  
    \( n_2 (1-\hat{p}) \ge 10 \).
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>6) Decision rule</h2>
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
    Reject if \( p \le \alpha \).
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>7) Interpretation</h2>
  </div>

  <div class="card">
    A small p-value indicates that the observed difference
    between sample proportions would be unlikely
    if the true population proportions were equal.
  </div>

  <p class="muted-mini">
    Always interpret the magnitude of the difference alongside statistical significance.
  </p>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Formulate hypotheses for two proportions</li>
        <li>Compute the pooled proportion</li>
        <li>Calculate the two-proportion z statistic</li>
        <li>Interpret results correctly</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next lesson</h2>
      <p style="margin:0;">
        We now move to categorical data analysis
        using the chi-square goodness-of-fit test.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/inference/classical-tests/chi-square-goodness-of-fit/">
          Next lesson: 8. Chi-Square Goodness-of-Fit →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/inference/classical-tests/one-proportion-z-test/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 6: One-Proportion z Test
          </a>
        </div>
      </div>
    </div>
  </div>
</section>