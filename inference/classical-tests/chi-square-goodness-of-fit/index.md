---
layout: default
title: "8. Chi-Square Goodness-of-Fit Test"
description: "Conduct and interpret the chi-square goodness-of-fit test to assess whether observed categorical frequencies match a specified distribution."
permalink: /inference/classical-tests/chi-square-goodness-of-fit/
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
        Version 0 establishes the formal structure of the chi-square goodness-of-fit test.
        Detailed examples and software demonstrations will be added later.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update continue-reading keys -->
<script>
  (function () {
    var KEY = "esa_continue_inference_classical_tests_lesson_v0";

    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/classical-tests/chi-square-goodness-of-fit/",
      label: "Lesson 8 — Chi-Square Goodness-of-Fit",
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
        <span class="badge">Lesson 8</span>
        <span class="badge">Categorical</span>
        <span class="badge">Chi-Square</span>
      </div>

      <h1>8. Chi-Square Goodness-of-Fit Test</h1>

      <p class="lead">
        The chi-square goodness-of-fit test evaluates whether
        the observed frequencies in categorical data
        are consistent with a specified probability distribution.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/classical-tests/">Back to Block 4</a>
        <a class="btn btn-outline" href="/inference/">Statistical Inference home</a>
      </div>

      <p class="muted-mini">
        This test compares observed counts to expected counts.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      Formulate hypotheses for categorical distributions,
      compute expected counts,
      and calculate the chi-square test statistic.
    </p>
  </div>

  <div class="callout">
    <div class="callout-copy">
      <h2>When to use this test</h2>
      <p style="margin:0;">
        Use the goodness-of-fit test when:
        <br>
        • Data are categorical counts  
        • There is one categorical variable  
        • A theoretical or specified distribution is provided
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
    H_0:\ \text{The population distribution matches the specified probabilities}
    \]
  </div>

  <div class="card" style="margin-top:1rem;">
    \[
    H_1:\ \text{The population distribution differs from the specified probabilities}
    \]
  </div>

  <p class="muted-mini">
    The null hypothesis fully specifies expected category proportions.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Expected counts</h2>
  </div>

  <div class="card">
    \[
    E_i = n \cdot p_i
    \]
  </div>

  <p>
    Where:
    <br>
    • \( n \) is the total sample size  
    • \( p_i \) is the specified probability for category \( i \)
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Test statistic</h2>
  </div>

  <div class="card">
    \[
    \chi^2 =
    \sum_{i=1}^{k}
    \frac{(O_i - E_i)^2}{E_i}
    \]
  </div>

  <p class="muted-mini">
    Where:
    <br>
    • \( O_i \) = observed count  
    • \( E_i \) = expected count  
    • \( k \) = number of categories
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Sampling distribution</h2>
  </div>

  <div class="card">
    \[
    \chi^2 \sim \chi^2_{k-1}
    \quad\text{under } H_0
    \]
  </div>

  <p>
    Degrees of freedom:
    \[
    df = k - 1
    \]
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Validity condition</h2>
  </div>

  <div class="card">
    All expected counts should satisfy:
    \[
    E_i \ge 5
    \]
  </div>

  <p>
    If expected counts are too small,
    the chi-square approximation may be unreliable.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>6) Interpretation</h2>
  </div>

  <div class="card">
    A small p-value indicates that the observed frequencies
    differ more from the expected frequencies
    than would be likely under the null hypothesis.
  </div>

  <p class="muted-mini">
    The test does not identify which categories differ most;
    it only detects overall deviation.
  </p>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Formulate hypotheses for categorical distributions</li>
        <li>Compute expected counts</li>
        <li>Calculate the chi-square statistic</li>
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
        We now examine the chi-square test of independence
        for two categorical variables.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/inference/classical-tests/chi-square-independence-test/">
          Next lesson: 9. Chi-Square Test of Independence →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/inference/classical-tests/two-proportion-z-test/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 7: Two-Proportion z Test
          </a>
        </div>
      </div>
    </div>
  </div>
</section>