---
layout: default
title: 4. Confounding
permalink: /modeling/multiple-regression/confounding/
sidebar: false
---

<!-- UNDER CONSTRUCTION -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <h2 style="color:#e65100;">🚧 Lesson Under Construction</h2>
    <p>
      Version 0 focuses on understanding confounding conceptually.
      Formal causal frameworks will be added later.
    </p>
  </div>
</section>

<!-- ✅ Update last visited lesson -->
<script>
(function () {
  localStorage.setItem("esa_continue_modeling_mr_lesson_v0", JSON.stringify({
    url: "/modeling/multiple-regression/confounding/",
    label: "Lesson 4 — Confounding",
    ts: Date.now()
  }));
})();
</script>

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Block 3</span>
      <span class="badge">Lesson 4</span>
      <span class="badge">Confounding</span>
      <span class="badge">Bias</span>
    </div>

    <h1>4. Confounding</h1>

    <p class="lead">
      Confounding occurs when the relationship between a predictor and the outcome
      is distorted by another variable.
    </p>

    <div class="hero-actions">
      <a class="btn btn-outline" href="/modeling/multiple-regression/">Back to Block 3</a>
      <a class="btn" href="#lesson">Start lesson</a>
    </div>

    <p class="muted-mini">
      Version 0: conceptual understanding of confounding and its impact.
    </p>

  </div>
</section>

<!-- LESSON -->
<section class="section" id="lesson">

  <h2>Learning objective</h2>
  <p>
    By the end of this lesson, you should understand what confounding is,
    how it affects interpretation, and why multiple regression is needed to address it.
  </p>

  <div class="card">
    <h3>Key idea</h3>
    <p>
      A confounder is a variable that is related to both the predictor and the outcome,
      distorting their observed relationship.
    </p>
  </div>

  <h2>1) What is confounding?</h2>
  <div class="card">
    <p>
      Confounding happens when an observed relationship is influenced by a third variable.
    </p>
  </div>

  <h2>2) Example</h2>
  <div class="card">
    <p>
      Ice cream sales and drowning incidents may be positively related.
    </p>
    <p>
      Confounder: <strong>temperature</strong>
    </p>
    <p>
      Higher temperature increases both ice cream sales and swimming activity.
    </p>
  </div>

  <h2>3) Why it is a problem</h2>
  <div class="card">
    <p>
      Without accounting for the confounder,
      we may incorrectly interpret the relationship as direct.
    </p>
  </div>

  <h2>4) Connection to regression</h2>
  <div class="card">
    <p>
      In simple regression, confounding variables are omitted,
      which can bias coefficient estimates.
    </p>
  </div>

  <h2>5) How multiple regression helps</h2>
  <div class="card">
    <p>
      By including confounders in the model,
      we can estimate adjusted effects that isolate each variable’s contribution.
    </p>
  </div>

  <h2>6) Omitted variable bias</h2>
  <div class="card">
    <p>
      When a confounder is excluded, the estimated effect of a predictor
      can be biased (too large, too small, or even reversed).
    </p>
  </div>

  <h2>7) Sign reversal example</h2>
  <div class="card">
    <p>
      A predictor may appear to have a positive effect in simple regression,
      but a negative effect after adjusting for another variable.
    </p>
  </div>

  <h2>8) Important warning</h2>
  <div class="card">
    <ul>
      <li>Controlling for variables does not automatically imply causality</li>
      <li>Incorrect variable selection can introduce new bias</li>
    </ul>
  </div>

  <h2>9) Why this matters</h2>
  <div class="card">
    <p>
      Confounding is one of the main reasons why simple models can lead to incorrect conclusions.
    </p>
  </div>

  <div class="card">
    <h3>Outcome of this lesson</h3>
    <ul>
      <li>Define confounding correctly</li>
      <li>Identify confounders conceptually</li>
      <li>Understand omitted variable bias</li>
      <li>Understand why coefficients change across models</li>
      <li>Prepare for interpreting coefficients</li>
    </ul>
  </div>

  <div class="card">
    <h3>Next step</h3>
    <p>
      Now we interpret regression coefficients formally in the multiple regression setting.
    </p>
    <a class="btn" href="/modeling/multiple-regression/coefficients/">
      Next lesson: Coefficients →
    </a>
  </div>

</section>