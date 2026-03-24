---
layout: default
title: Block 3 — Multiple Regression
permalink: /modeling/multiple-regression/
sidebar: false
---

<!-- UNDER CONSTRUCTION -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem;">
        🚧 This Block Is Under Construction
      </h2>
      <p style="margin:0; font-size:1.05rem; line-height:1.6;">
        This block extends regression to multiple predictors.
        It introduces adjusted effects, confounding, and how interpretation
        changes when variables are considered together.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update last visited block -->
<script>
(function () {
  localStorage.setItem("esa_continue_modeling_last_block_v0", JSON.stringify({
    url: "/modeling/multiple-regression/",
    label: "Block 3 — Multiple Regression",
    ts: Date.now()
  }));
})();
</script>

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card hero-split">

    <div class="hero-copy">

      <div class="badge-row">
        <span class="badge">Block 3</span>
        <span class="badge">Multiple</span>
        <span class="badge">Adjustment</span>
        <span class="badge">Confounding</span>
      </div>

      <h1>Block 3 — Multiple Regression</h1>

      <p class="lead">
        Multiple regression allows us to model relationships while controlling
        for other variables. This is where interpretation becomes subtle:
        coefficients represent adjusted effects, not simple relationships.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/modeling/">Back to Statistical Modeling</a>
        <a class="btn" href="#lessons">Open structure</a>
      </div>

      <p class="muted-mini">
        Version 0: structure is locked. Lessons will expand without changing order.
      </p>

    </div>

    <div class="hero-panel">
      <div class="panel-card">
        <h2 class="panel-title">What this block covers</h2>
        <ul class="quickstart" style="list-style:none; padding-left:0;">

          <li><strong>Multiple predictors</strong><span class="meta">More realistic models</span></li>
          <li><strong>Adjusted effects</strong><span class="meta">Holding others constant</span></li>
          <li><strong>Confounding</strong><span class="meta">Why simple regression misleads</span></li>
          <li><strong>Interpretation</strong><span class="meta">Conditional meaning of coefficients</span></li>
          <li><strong>Multicollinearity</strong><span class="meta">Correlation among predictors</span></li>
          <li><strong>Categorical variables</strong><span class="meta">Dummy coding</span></li>
          <li><strong>Interactions</strong><span class="meta">When effects depend on other variables</span></li>

        </ul>
      </div>
    </div>

  </div>
</section>

<!-- ✅ Continue Reading -->
<section class="section" id="continue-reading-mr" style="display:none;">
  <div class="callout">
    <div class="callout-copy">
      <h2>Continue reading</h2>
      <p class="muted-mini" id="continue-reading-mr-label" style="margin:0 0 .75rem 0;"></p>
      <a class="btn" id="continue-reading-mr-btn" href="#">Continue</a>
    </div>
  </div>
</section>

<!-- LESSONS -->
<section class="section" id="lessons">

  <div class="section-head">
    <h2>Lessons (Version 0)</h2>
    <p>
      Lessons build from intuition (why multiple regression is needed)
      to careful interpretation and modeling challenges.
    </p>
  </div>

  <div class="grid grid-2">

    <div class="card lesson-card">
      <h3><a href="/modeling/multiple-regression/why-multiple/">1. Why Multiple Regression?</a></h3>
      <p>Why single-variable models are often misleading and incomplete.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/modeling/multiple-regression/why-multiple/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/modeling/multiple-regression/model-structure/">2. The Multiple Regression Model</a></h3>
      <p>Extending the regression equation to multiple predictors.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/modeling/multiple-regression/model-structure/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/modeling/multiple-regression/adjusted-effects/">3. Adjusted Effects</a></h3>
      <p>Interpreting coefficients while holding other variables constant.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/modeling/multiple-regression/adjusted-effects/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/modeling/multiple-regression/confounding/">4. Confounding</a></h3>
      <p>How omitted variables distort relationships and create bias.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/modeling/multiple-regression/confounding/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/modeling/multiple-regression/coefficients/">5. Interpreting Coefficients</a></h3>
      <p>Understanding meaning, units, and conditional interpretation.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/modeling/multiple-regression/coefficients/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/modeling/multiple-regression/multicollinearity/">6. Multicollinearity</a></h3>
      <p>When predictors are correlated and why it causes instability.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/modeling/multiple-regression/multicollinearity/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/modeling/multiple-regression/dummy-variables/">7. Dummy Variables (Categorical Data)</a></h3>
      <p>Encoding categories and interpreting baseline comparisons.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/modeling/multiple-regression/dummy-variables/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/modeling/multiple-regression/interactions/">8. Interaction Effects</a></h3>
      <p>When the effect of one variable depends on another.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/modeling/multiple-regression/interactions/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/modeling/multiple-regression/model-building/">9. Model Building Thinking</a></h3>
      <p>Choosing variables and thinking beyond automatic selection.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/modeling/multiple-regression/model-building/">Open lesson</a>
      </div>
    </div>

  </div>
</section>

<!-- OUTCOME -->
<section class="section section-slim">
  <div class="callout">

    <div class="callout-copy">
      <h2>Outcome of Block 3</h2>
      <ul class="bullets">
        <li>Understand why multiple regression is necessary</li>
        <li>Interpret adjusted effects correctly</li>
        <li>Recognize and explain confounding</li>
        <li>Understand multicollinearity and its consequences</li>
        <li>Work with categorical variables and interactions</li>
      </ul>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Next block</div>
        <div class="mini-body">
          Continue to
          <a href="/modeling/assumptions/" style="color:#1a73e8; text-decoration:underline;">
            <strong>Block 4 — Model Assumptions</strong>
          </a>.
        </div>
      </div>
    </div>

  </div>
</section>

<!-- CONTINUE READING SCRIPT -->
<script>
(function () {
  var KEY = "esa_continue_modeling_mr_lesson_v0";
  var raw = localStorage.getItem(KEY);
  if (!raw) return;

  try {
    var data = JSON.parse(raw);
    if (!data || !data.url || !data.label) return;

    var wrap = document.getElementById("continue-reading-mr");
    var label = document.getElementById("continue-reading-mr-label");
    var btn = document.getElementById("continue-reading-mr-btn");

    label.innerHTML = 'You last visited: <strong>' + data.label + '</strong>';
    btn.href = data.url;
    wrap.style.display = "block";

  } catch (e) {}
})();
</script>