---
layout: default
title: "9. Confidence Intervals and Hypothesis Tests: The Connection"
description: "Understand the mathematical equivalence between confidence intervals and hypothesis tests and learn how decisions correspond across both frameworks."
permalink: /inference/hypothesis-testing/ci-and-test-connection/
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
        Version 0 establishes the formal equivalence between two-sided hypothesis tests
        and confidence intervals at the same significance level.
        Numerical demonstrations and visual proofs will be added later.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update continue-reading keys -->
<script>
  (function () {
    var KEY = "esa_continue_inference_hypothesis_testing_lesson_v0";

    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/hypothesis-testing/ci-and-test-connection/",
      label: "Lesson 9 — CI and Test Connection",
      ts: Date.now()
    }));

    localStorage.setItem("esa_continue_inference_last_block_v0", JSON.stringify({
      url: "/inference/hypothesis-testing/",
      label: "Block 3 — Hypothesis Testing",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 3</span>
        <span class="badge">Lesson 9</span>
        <span class="badge">Confidence Interval</span>
        <span class="badge">Hypothesis Test</span>
      </div>

      <h1>9. Confidence Intervals and Hypothesis Tests: The Connection</h1>

      <p class="lead">
        Confidence intervals and hypothesis tests are two perspectives
        on the same underlying sampling distribution.
        For two-sided tests, they produce identical decisions
        when confidence level and significance level match.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/hypothesis-testing/">Back to Block 3</a>
        <a class="btn btn-outline" href="/inference/">Statistical Inference home</a>
      </div>

      <p class="muted-mini">
        Same mathematics — different interpretation focus.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      Demonstrate the equivalence between two-sided hypothesis tests
      at level \( \alpha \)
      and \(100(1-\alpha)\%\) confidence intervals.
    </p>
  </div>

  <div class="callout">
    <div class="callout-copy">
      <h2>Core result</h2>
      <p style="margin:0;">
        A two-sided hypothesis test at level \( \alpha \)
        rejects \(H_0\) if and only if
        the corresponding \(100(1-\alpha)\%\) confidence interval
        does not contain the null value.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) The hypothesis test decision rule</h2>
  </div>

  <div class="card">
    \[
    \text{Reject } H_0 \text{ if }
    \left|
    \frac{\hat{\theta} - \theta_0}{SE}
    \right|
    >
    z_{\alpha/2}
    \]
  </div>

  <p class="muted-mini">
    (Using z for illustration; same logic applies for t.)
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) The confidence interval formula</h2>
  </div>

  <div class="card">
    \[
    \hat{\theta}
    \pm
    z_{\alpha/2} \cdot SE
    \]
  </div>

  <p style="margin-top:.75rem;">
    This interval contains all parameter values
    that would not be rejected by the test.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Algebraic equivalence</h2>
  </div>

  <div class="card">
    \[
    \left|
    \frac{\hat{\theta} - \theta_0}{SE}
    \right|
    \le
    z_{\alpha/2}
    \quad
    \Longleftrightarrow
    \quad
    \theta_0
    \text{ lies inside the CI}
    \]
  </div>

  <p class="muted-mini">
    Rejection corresponds exactly to exclusion from the interval.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Interpretation difference</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Hypothesis test</h3>
      <p style="margin:0;">
        Focuses on decision:
        reject or fail to reject \(H_0\).
      </p>
    </div>

    <div class="card">
      <h3>Confidence interval</h3>
      <p style="margin:0;">
        Focuses on estimation:
        plausible values for the parameter.
      </p>
    </div>
  </div>

  <p class="muted-mini">
    The test gives a binary decision;
    the interval gives a range of plausible values.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Special cases</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Difference of means</h3>
      <p style="margin:0;">
        If 0 lies in the CI,
        the two-sided test fails to reject.
      </p>
    </div>

    <div class="card">
      <h3>Proportions</h3>
      <p style="margin:0;">
        Same principle applies:
        null value inside CI → not significant.
      </p>
    </div>

    <div class="card">
      <h3>Regression slope</h3>
      <p style="margin:0;">
        If 0 excluded from CI,
        slope is statistically significant.
      </p>
    </div>

    <div class="card">
      <h3>Matching α and CI level</h3>
      <p style="margin:0;">
        α = 0.05 corresponds to 95% CI.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>6) Important caveat</h2>
  </div>

  <div class="card">
    <p style="margin:0;">
      The equivalence holds directly for two-sided tests.
      One-sided tests correspond to one-sided confidence bounds,
      not symmetric intervals.
    </p>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Prove the equivalence algebraically</li>
        <li>Connect α to confidence level</li>
        <li>Interpret exclusion of null value correctly</li>
        <li>Distinguish decision vs estimation perspectives</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next step</h2>
      <p style="margin:0;">
        Next, we examine practical significance
        and how statistical significance differs from real-world importance.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/inference/hypothesis-testing/practical-significance/">
          Next lesson: 10. Practical Significance →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/inference/hypothesis-testing/one-sided-vs-two-sided/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 8: One-Sided vs Two-Sided Tests
          </a>
        </div>
      </div>
    </div>
  </div>
</section>