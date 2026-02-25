---
layout: default
title: "5. Multiple Testing and False Positives"
description: "Understand why multiple comparisons inflate Type I error, how false positives arise, and the logic behind adjustment methods."
permalink: /inference/interpretation-reporting/multiple-testing-and-false-positives/
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
        Version 0 explains why conducting many tests increases the probability
        of false positives and introduces the logic of correction methods.
        Applied demonstrations and simulations will be added later.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update continue-reading keys -->
<script>
  (function () {
    var KEY = "esa_continue_inference_interpretation_reporting_lesson_v0";

    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/interpretation-reporting/multiple-testing-and-false-positives/",
      label: "Lesson 5 — Multiple Testing & False Positives",
      ts: Date.now()
    }));

    localStorage.setItem("esa_continue_inference_last_block_v0", JSON.stringify({
      url: "/inference/interpretation-reporting/",
      label: "Block 6 — Interpretation & Reporting",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 6</span>
        <span class="badge">Lesson 5</span>
        <span class="badge">Multiple Testing</span>
        <span class="badge">Type I Error</span>
      </div>

      <h1>5. Multiple Testing and False Positives</h1>

      <p class="lead">
        When many hypotheses are tested,
        the probability of obtaining at least one false positive increases.
        This is known as the multiple testing problem.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/interpretation-reporting/">Back to Block 6</a>
        <a class="btn btn-outline" href="/inference/">Statistical Inference home</a>
      </div>

      <p class="muted-mini">
        Type I error control applies to single tests — not automatically to sets of tests.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      Understand how multiple comparisons inflate false positive rates
      and learn the basic logic behind correction procedures.
    </p>
  </div>

  <div class="callout">
    <div class="callout-copy">
      <h2>Core idea</h2>
      <p style="margin:0;">
        If each test has Type I error rate
        \[
        \alpha,
        \]
        the probability of at least one false positive increases
        as the number of tests grows.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Family-wise error rate (FWER)</h2>
  </div>

  <div class="card">
    For m independent tests:
    \[
    P(\text{at least one false positive})
    =
    1 - (1 - \alpha)^m
    \]
  </div>

  <p>
    Example:
    <br>
    If \( \alpha = 0.05 \) and \( m = 20 \),
    the overall false positive probability is much larger than 0.05.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Illustration</h2>
  </div>

  <div class="card">
    With 100 independent tests at \( \alpha = 0.05 \):
    <br><br>
    Expected false positives:
    \[
    100 \times 0.05 = 5
    \]
  </div>

  <p>
    Even when all null hypotheses are true,
    some significant results will appear by chance.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Correction logic</h2>
  </div>

  <div class="card">
    Bonferroni adjustment:
    \[
    \alpha_{adjusted} = \frac{\alpha}{m}
    \]
  </div>

  <p>
    This controls the probability of at least one false positive
    across the entire family of tests.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) False discovery rate (FDR)</h2>
  </div>

  <div class="card">
    FDR controls:
    <br><br>
    The expected proportion of false positives
    among rejected hypotheses.
  </div>

  <p>
    FDR methods (e.g., Benjamini–Hochberg)
    are often used in high-dimensional settings.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Practical implications</h2>
  </div>

  <div class="grid grid-2">
    <div class="card">
      <h3>Exploratory analysis</h3>
      <p>
        Multiple testing common; interpret cautiously.
      </p>
    </div>

    <div class="card">
      <h3>Confirmatory analysis</h3>
      <p>
        Pre-specify hypotheses and control error rates.
      </p>
    </div>
  </div>

  <p class="muted-mini">
    Transparency about number of tests performed is essential.
  </p>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Understand inflation of Type I error</li>
        <li>Compute family-wise error probability</li>
        <li>Explain Bonferroni logic</li>
        <li>Distinguish FWER from FDR</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next lesson</h2>
      <p style="margin:0;">
        We now focus on reporting results clearly and responsibly.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/inference/interpretation-reporting/reporting-results-clear-language/">
          Next lesson: 6. Reporting Results in Clear Language →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/inference/interpretation-reporting/interpreting-effect-sizes/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 4: Interpreting Effect Sizes
          </a>
        </div>
      </div>
    </div>
  </div>
</section>