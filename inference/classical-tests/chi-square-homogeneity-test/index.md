---
layout: default
title: "10. Chi-Square Test of Homogeneity"
description: "Conduct and interpret the chi-square test of homogeneity to compare categorical distributions across multiple populations."
permalink: /inference/classical-tests/chi-square-homogeneity-test/
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
        Version 0 establishes the formal structure of the chi-square test of homogeneity.
        Worked multi-sample examples and software demonstrations will be added later.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update continue-reading keys -->
<script>
  (function () {
    var KEY = "esa_continue_inference_classical_tests_lesson_v0";

    localStorage.setItem(KEY, JSON.stringify({
      url: "/inference/classical-tests/chi-square-homogeneity-test/",
      label: "Lesson 10 — Chi-Square Homogeneity Test",
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
        <span class="badge">Lesson 10</span>
        <span class="badge">Categorical</span>
        <span class="badge">Homogeneity</span>
      </div>

      <h1>10. Chi-Square Test of Homogeneity</h1>

      <p class="lead">
        The chi-square test of homogeneity evaluates whether
        multiple populations share the same categorical distribution.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/inference/classical-tests/">Back to Block 4</a>
        <a class="btn btn-outline" href="/inference/">Statistical Inference home</a>
      </div>

      <p class="muted-mini">
        Structurally similar to the independence test,
        but conceptually different in design.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      Formulate hypotheses for comparing categorical distributions
      across independent populations,
      compute expected counts,
      and interpret the chi-square statistic.
    </p>
  </div>

  <div class="callout">
    <div class="callout-copy">
      <h2>When to use this test</h2>
      <p style="margin:0;">
        Use the homogeneity test when:
        <br>
        • There are two or more independent populations  
        • Each population is classified into the same categories  
        • Data consist of counts  
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
    H_0:\ \text{All populations have the same categorical distribution}
    \]
  </div>

  <div class="card" style="margin-top:1rem;">
    \[
    H_1:\ \text{At least one population differs in distribution}
    \]
  </div>

  <p class="muted-mini">
    The null states that category proportions are identical across groups.
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
    Expected counts are computed assuming equal distributions across populations.
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

  <p>
    The statistic aggregates deviations between observed and expected counts.
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
    • \(r\) = number of populations (rows)  
    • \(c\) = number of categories (columns)  
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
    If expected counts are small,
    consider combining categories or alternative methods.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>6) Interpretation</h2>
  </div>

  <div class="card">
    A small p-value suggests that
    at least one population distribution differs
    from the others.
  </div>

  <p class="muted-mini">
    The test identifies overall difference,
    not which specific groups differ.
  </p>
</section>

<section class="section">
  <div class="section-head">
    <h2>7) Homogeneity vs Independence</h2>
  </div>

  <div class="card">
    • Homogeneity: compares distributions across populations  
    <br>
    • Independence: tests association within one population  
  </div>

  <p>
    The computational formula is identical,
    but the study design and interpretation differ.
  </p>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Formulate homogeneity hypotheses</li>
        <li>Compute expected counts correctly</li>
        <li>Calculate chi-square statistic</li>
        <li>Distinguish homogeneity from independence</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next lesson</h2>
      <p style="margin:0;">
        We now move from categorical comparisons
        to comparing multiple means using ANOVA.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/inference/classical-tests/one-way-anova-f-test/">
          Next lesson: 11. One-Way ANOVA (F Test) →
        </a>
      </div>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Previous lesson</div>
        <div class="mini-body">
          <a href="/inference/classical-tests/chi-square-independence-test/" style="color:#1a73e8; text-decoration:underline;">
            Lesson 9: Chi-Square Test of Independence
          </a>
        </div>
      </div>
    </div>
  </div>
</section>