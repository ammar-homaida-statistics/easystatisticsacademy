---
layout: default
title: "9. Chi-Square Test of Independence"
description: "Conduct and interpret the chi-square test of independence to assess association between two categorical variables."
permalink: /inference/classical-tests/chi-square-independence-test/
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
        Version 0 establishes the formal structure of the chi-square test of independence.
        Worked contingency table examples and software demonstrations will be added later.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update continue-reading keys -->
<script>
  (function () {
    var KEY = "esa_continue_inference_classical_tests_lesson_v0";

    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/classical-tests/chi-square-independence-test/",
      label: "Lesson 9 — Chi-Square Test of Independence",
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
        <span class="badge">Lesson 9</span>
        <span class="badge">Categorical</span>
        <span class="badge">Association</span>
      </div>

      <h1>9. Chi-Square Test of Independence</h1>

      <p class="lead">
        The chi-square test of independence evaluates whether
        two categorical variables are statistically associated
        in a population.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/classical-tests/">Back to Block 4</a>
        <a class="btn btn-outline" href="/inference/">Statistical Inference home</a>
      </div>

      <p class="muted-mini">
        This test analyzes contingency tables.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      Formulate hypotheses for association between categorical variables,
      compute expected counts,
      and interpret the chi-square statistic.
    </p>
  </div>

  <div class="callout">
    <div class="callout-copy">
      <h2>When to use this test</h2>
      <p style="margin:0;">
        Use the independence test when:
        <br>
        • There are two categorical variables  
        • Data are arranged in a contingency table  
        • Observations are independent  
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
    H_0:\ \text{The variables are independent}
    \]
  </div>

  <div class="card" style="margin-top:1rem;">
    \[
    H_1:\ \text{The variables are associated}
    \]
  </div>

  <p class="muted-mini">
    Independence means that the distribution of one variable
    does not differ across levels of the other.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Expected counts</h2>
  </div>

  <div class="card">
    \[
    E_{ij} =
    \frac{(\text{Row Total}_i)(\text{Column Total}_j)}{\text{Grand Total}}
    \]
  </div>

  <p>
    Expected counts are computed assuming independence.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Test statistic</h2>
  </div>

  <div class="card">
    \[
    \chi^2 =
    \sum_{i}\sum_{j}
    \frac{(O_{ij} - E_{ij})^2}{E_{ij}}
    \]
  </div>

  <p class="muted-mini">
    \(O_{ij}\) = observed count  
    <br>
    \(E_{ij}\) = expected count  
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Degrees of freedom</h2>
  </div>

  <div class="card">
    \[
    df = (r - 1)(c - 1)
    \]
  </div>

  <p>
    Where:
    <br>
    • \(r\) = number of rows  
    • \(c\) = number of columns  
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Validity condition</h2>
  </div>

  <div class="card">
    All expected counts should satisfy:
    \[
    E_{ij} \ge 5
    \]
  </div>

  <p>
    Small expected counts weaken the chi-square approximation.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>6) Interpretation</h2>
  </div>

  <div class="card">
    A small p-value indicates that the pattern of counts
    differs from what would be expected under independence.
  </div>

  <p class="muted-mini">
    The test does not measure strength of association —
    only evidence of association.
  </p>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Formulate independence hypotheses</li>
        <li>Compute expected counts in contingency tables</li>
        <li>Calculate chi-square statistic</li>
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
        We now distinguish the independence test
        from the chi-square test of homogeneity.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/inference/classical-tests/chi-square-homogeneity-test/">
          Next lesson: 10. Chi-Square Homogeneity Test →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/inference/classical-tests/chi-square-goodness-of-fit/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 8: Chi-Square Goodness-of-Fit
          </a>
        </div>
      </div>
    </div>
  </div>
</section>