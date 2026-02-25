---
layout: default
title: "4. Paired t Test (Mean of Differences)"
description: "Conduct and interpret a paired t test for matched or dependent samples by reducing the problem to a one-sample test on differences."
permalink: /inference/classical-tests/paired-t-test/
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
        Version 0 establishes the formal structure of the paired t test.
        Applied case studies and full software walkthroughs will be added later.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update continue-reading keys -->
<script>
  (function () {
    var KEY = "esa_continue_inference_classical_tests_lesson_v0";

    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/classical-tests/paired-t-test/",
      label: "Lesson 4 — Paired t Test",
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
        <span class="badge">Lesson 4</span>
        <span class="badge">Paired</span>
        <span class="badge">Dependent Samples</span>
      </div>

      <h1>4. Paired t Test (Mean of Differences)</h1>

      <p class="lead">
        The paired t test evaluates whether the mean difference
        between two related measurements is zero.
        It converts paired observations into a single variable:
        the difference within each pair.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/classical-tests/">Back to Block 4</a>
        <a class="btn btn-outline" href="/inference/">Statistical Inference home</a>
      </div>

      <p class="muted-mini">
        A paired problem is a one-sample problem in disguise.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      Transform paired data into differences,
      compute the paired t statistic,
      and interpret the result correctly.
    </p>
  </div>

  <div class="callout">
    <div class="callout-copy">
      <h2>When to use this test</h2>
      <p style="margin:0;">
        Use the paired t test when:
        <br>
        • Observations are naturally paired (before–after, matched units)  
        • Differences are independent across pairs  
        • Differences are approximately normal or sample size is moderate/large
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Define the differences</h2>
  </div>

  <div class="card">
    \[
    D_i = X_{1i} - X_{2i}
    \]
  </div>

  <p class="muted-mini">
    The parameter of interest is:
    \[
    \mu_D
    \]
    (the mean difference in the population).
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Hypotheses</h2>
  </div>

  <div class="card">
    \[
    H_0: \mu_D = 0
    \quad\text{vs}\quad
    H_1: \mu_D \ne 0
    \]
  </div>

  <p class="muted-mini">
    One-sided alternatives are possible when direction is specified in advance.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Test statistic</h2>
  </div>

  <div class="card">
    \[
    t =
    \frac{\bar{D}}
    {S_D / \sqrt{n}}
    \]
  </div>

  <p style="margin-top:.75rem;">
    Where:
    <br>
    • \( \bar{D} \) = mean of differences  
    • \( S_D \) = standard deviation of differences  
    • \( n \) = number of pairs
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Sampling distribution</h2>
  </div>

  <div class="card">
    \[
    t \sim t_{n-1}
    \quad\text{under } H_0
    \]
  </div>

  <p class="muted-mini">
    Degrees of freedom:
    \[
    df = n - 1
    \]
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Interpretation</h2>
  </div>

  <div class="card">
    A small p-value indicates that the observed average difference
    is unlikely if the true mean difference were zero.
  </div>

  <p class="muted-mini">
    If zero lies in the corresponding confidence interval,
    the null hypothesis is not rejected.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>6) Why not use two independent tests?</h2>
  </div>

  <div class="card">
    Treating paired data as independent ignores the pairing structure
    and inflates variability.
  </div>

  <div class="card" style="margin-top:1rem;">
    The paired design reduces variance by removing between-subject variability.
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Identify paired designs correctly</li>
        <li>Reduce paired data to differences</li>
        <li>Compute and interpret the paired t statistic</li>
        <li>Avoid treating paired data as independent</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next lesson</h2>
      <p style="margin:0;">
        We now compare two independent groups
        using the two-sample t test.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/inference/classical-tests/two-sample-t-test-independent/">
          Next lesson: 5. Two-Sample t Test (Independent Samples) →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/inference/classical-tests/one-sample-t-test-for-mean/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 3: One-Sample t Test
          </a>
        </div>
      </div>
    </div>
  </div>
</section>