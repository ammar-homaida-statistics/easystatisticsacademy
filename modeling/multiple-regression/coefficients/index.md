---
layout: default
title: 5. Interpreting Coefficients
permalink: /modeling/multiple-regression/coefficients/
sidebar: false
---

<!-- UNDER CONSTRUCTION -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <h2 style="color:#e65100;">🚧 Lesson Under Construction</h2>
    <p>
      Version 0 focuses on correct interpretation of coefficients in multiple regression.
      Statistical inference and significance will be added later.
    </p>
  </div>
</section>

<!-- ✅ Update last visited lesson -->
<script>
(function () {
  localStorage.setItem("esa_continue_modeling_mr_lesson_v0", JSON.stringify({
    url: "/modeling/multiple-regression/coefficients/",
    label: "Lesson 5 — Coefficients",
    ts: Date.now()
  }));
})();
</script>

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Block 3</span>
      <span class="badge">Lesson 5</span>
      <span class="badge">Coefficients</span>
      <span class="badge">Interpretation</span>
    </div>

    <h1>5. Interpreting Coefficients</h1>

    <p class="lead">
      Each coefficient represents the change in the response variable
      associated with a one-unit change in a predictor, holding all other variables constant.
    </p>

    <div class="hero-actions">
      <a class="btn btn-outline" href="/modeling/multiple-regression/">Back to Block 3</a>
      <a class="btn" href="#lesson">Start lesson</a>
    </div>

    <p class="muted-mini">
      Version 0: interpretation-first approach before statistical testing.
    </p>

  </div>
</section>

<!-- LESSON -->
<section class="section" id="lesson">

  <h2>Learning objective</h2>
  <p>
    By the end of this lesson, you should be able to interpret regression coefficients
    correctly in a multiple regression model.
  </p>

  <div class="card">
    <h3>Key idea</h3>
    <p>
      A coefficient measures the expected change in Y for a one-unit increase in a predictor,
      holding all other predictors constant.
    </p>
  </div>

  <h2>1) General form of interpretation</h2>
  <div class="card">
    <p>
      For coefficient β₁:
    </p>
    <p>
      “A one-unit increase in X₁ is associated with a β₁-unit change in Y,
      holding all other variables constant.”
    </p>
  </div>

  <h2>2) Example</h2>
  <div class="card">
    <p>
      Model:
    </p>
    <p><strong>Score = 40 + 3(Hours) + 2(Sleep)</strong></p>

    <p>
      Interpretation of Hours coefficient:
    </p>
    <p>
      Increasing study hours by one unit increases score by 3 units,
      <strong>holding sleep constant</strong>.
    </p>
  </div>

  <h2>3) Intercept interpretation</h2>
  <div class="card">
    <p>
      The intercept represents the expected value of Y when all predictors are zero.
    </p>
    <p>
      In practice, it may not always have meaningful interpretation.
    </p>
  </div>

  <h2>4) Continuous predictors</h2>
  <div class="card">
    <p>
      Interpretation is based on unit changes in the predictor.
    </p>
  </div>

  <h2>5) Units matter</h2>
  <div class="card">
    <p>
      The meaning of a coefficient depends on the units of the variables.
    </p>
  </div>

  <h2>6) Multiple predictors context</h2>
  <div class="card">
    <p>
      Coefficients must always be interpreted in the context of the other variables in the model.
    </p>
  </div>

  <h2>7) Common mistakes</h2>
  <div class="card">
    <ul>
      <li>Ignoring “holding others constant”</li>
      <li>Interpreting coefficients as causal effects</li>
      <li>Ignoring units of measurement</li>
      <li>Interpreting coefficients without context</li>
    </ul>
  </div>

  <h2>8) Why this matters</h2>
  <div class="card">
    <p>
      Correct interpretation of coefficients is essential for making valid conclusions
      in statistical modeling and applied analysis.
    </p>
  </div>

  <div class="card">
    <h3>Outcome of this lesson</h3>
    <ul>
      <li>Interpret coefficients in multiple regression</li>
      <li>Understand the role of units</li>
      <li>Interpret intercepts correctly</li>
      <li>Avoid common interpretation errors</li>
      <li>Prepare for multicollinearity issues</li>
    </ul>
  </div>

  <div class="card">
    <h3>Next step</h3>
    <p>
      Now we examine what happens when predictors are highly correlated
      and how it affects coefficient stability.
    </p>
    <a class="btn" href="/modeling/multiple-regression/multicollinearity/">
      Next lesson: Multicollinearity →
    </a>
  </div>

</section>