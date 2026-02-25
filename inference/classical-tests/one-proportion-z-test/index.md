---
layout: default
title: "6. One-Proportion z Test"
description: "Conduct and interpret a one-proportion z test to evaluate whether a population proportion differs from a hypothesized value."
permalink: /inference/classical-tests/one-proportion-z-test/
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
        Version 0 establishes the structure of the one-proportion z test.
        Full numerical examples and software walkthroughs will be added later.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update continue-reading keys -->
<script>
  (function () {
    var KEY = "esa_continue_inference_classical_tests_lesson_v0";

    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/classical-tests/one-proportion-z-test/",
      label: "Lesson 6 — One-Proportion z Test",
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
        <span class="badge">Lesson 6</span>
        <span class="badge">Proportion</span>
        <span class="badge">z Test</span>
      </div>

      <h1>6. One-Proportion z Test</h1>

      <p class="lead">
        The one-proportion z test evaluates whether a population proportion
        differs from a hypothesized value using the normal approximation
        to the binomial distribution.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/classical-tests/">Back to Block 4</a>
        <a class="btn btn-outline" href="/inference/">Statistical Inference home</a>
      </div>

      <p class="muted-mini">
        This test relies on large-sample normal approximation.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      Formulate hypotheses for a proportion,
      compute the z test statistic,
      check validity conditions,
      and interpret the p-value correctly.
    </p>
  </div>

  <div class="callout">
    <div class="callout-copy">
      <h2>When to use this test</h2>
      <p style="margin:0;">
        Use the one-proportion z test when:
        <br>
        • Data are counts of successes out of \( n \) trials  
        • Observations are independent  
        • The success–failure condition is satisfied
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
    \text{Parameter: } p
    \]
  </div>

  <div class="card" style="margin-top:1rem;">
    \[
    H_0: p = p_0
    \quad\text{vs}\quad
    H_1: p \ne p_0
    \]
  </div>

  <p class="muted-mini">
    One-sided alternatives are also possible when justified.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Sample proportion</h2>
  </div>

  <div class="card">
    \[
    \hat{p} = \frac{X}{n}
    \]
  </div>

  <p>
    Where \( X \) is the number of successes in the sample.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Test statistic</h2>
  </div>

  <div class="card">
    \[
    z =
    \frac{\hat{p} - p_0}
    {\sqrt{\frac{p_0(1-p_0)}{n}}}
    \]
  </div>

  <p class="muted-mini">
    Note: the standard error uses \( p_0 \) under the null hypothesis.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Validity condition</h2>
  </div>

  <div class="card">
    Success–failure condition under \(H_0\):
    \[
    n p_0 \ge 10
    \quad\text{and}\quad
    n(1-p_0) \ge 10
    \]
  </div>

  <p>
    If these conditions are not satisfied,
    the normal approximation may be unreliable.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Decision rule</h2>
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
    <h2>6) Interpretation</h2>
  </div>

  <div class="card">
    A small p-value indicates that the observed sample proportion
    would be unlikely if the true population proportion were \( p_0 \).
  </div>

  <p class="muted-mini">
    Statistical significance does not imply a large or practically important difference.
  </p>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Formulate hypotheses for a proportion</li>
        <li>Compute the one-proportion z statistic</li>
        <li>Check the success–failure condition</li>
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
        We now compare two independent proportions
        using the two-proportion z test.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/inference/classical-tests/two-proportion-z-test/">
          Next lesson: 7. Two-Proportion z Test →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/inference/classical-tests/two-sample-t-test-independent/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 5: Two-Sample t Test
          </a>
        </div>
      </div>
    </div>
  </div>
</section>