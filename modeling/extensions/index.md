---
layout: default
title: Block 7 — Extensions
permalink: /modeling/extensions/
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
        This block introduces extensions beyond standard linear regression.
        It explains why some data require different modeling approaches,
        especially when outcomes are binary or relationships are not well
        handled by ordinary linear models.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update last visited block -->
<script>
(function () {
  localStorage.setItem("esa_continue_modeling_last_block_v0", JSON.stringify({
    url: "/modeling/extensions/",
    label: "Block 7 — Extensions",
    ts: Date.now()
  }));
})();
</script>

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card hero-split">

    <div class="hero-copy">

      <div class="badge-row">
        <span class="badge">Block 7</span>
        <span class="badge">Extensions</span>
        <span class="badge">Logistic</span>
        <span class="badge">GLM</span>
      </div>

      <h1>Block 7 — Extensions</h1>

      <p class="lead">
        Linear regression is powerful, but not universal.
        This block introduces extensions that handle new kinds of outcomes
        and broaden the modeling framework beyond ordinary least squares.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/modeling/">Back to Statistical Modeling</a>
        <a class="btn" href="#lessons">Open structure</a>
      </div>

      <p class="muted-mini">
        Version 0: structure is fixed. Lessons will expand without changing order.
      </p>

    </div>

    <div class="hero-panel">
      <div class="panel-card">
        <h2 class="panel-title">What this block covers</h2>
        <ul class="quickstart" style="list-style:none; padding-left:0;">

          <li><strong>Why extensions are needed</strong><span class="meta">Limits of linear regression</span></li>
          <li><strong>Logistic regression</strong><span class="meta">Modeling binary outcomes</span></li>
          <li><strong>Odds and log-odds</strong><span class="meta">Interpreting logistic models</span></li>
          <li><strong>Generalized linear models</strong><span class="meta">Broader modeling framework</span></li>
          <li><strong>Link functions</strong><span class="meta">Connecting predictors to outcomes</span></li>
          <li><strong>Transition thinking</strong><span class="meta">Bridge to more advanced modeling</span></li>

        </ul>
      </div>
    </div>

  </div>
</section>

<!-- ✅ Continue Reading -->
<section class="section" id="continue-reading-extensions" style="display:none;">
  <div class="callout">
    <div class="callout-copy">
      <h2>Continue reading</h2>
      <p class="muted-mini" id="continue-reading-extensions-label" style="margin:0 0 .75rem 0;"></p>
      <a class="btn" id="continue-reading-extensions-btn" href="#">Continue</a>
    </div>
  </div>
</section>

<!-- LESSONS -->
<section class="section" id="lessons">

  <div class="section-head">
    <h2>Lessons (Version 0)</h2>
    <p>
      This block introduces the logic of model extension: when linear regression
      is not enough, what changes, and how broader model families work.
    </p>
  </div>

  <div class="grid grid-2">

    <div class="card lesson-card">
      <h3><a href="/modeling/extensions/why-extensions/">1. Why Do We Need Extensions?</a></h3>
      <p>Why ordinary linear regression cannot handle every outcome or structure.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/modeling/extensions/why-extensions/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/modeling/extensions/logistic-regression/">2. Logistic Regression</a></h3>
      <p>Introducing regression for binary outcomes.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/modeling/extensions/logistic-regression/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/modeling/extensions/probability-vs-logit/">3. Probability, Logit, and the Need for Transformation</a></h3>
      <p>Why probabilities need a different modeling scale.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/modeling/extensions/probability-vs-logit/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/modeling/extensions/odds/">4. Odds Interpretation</a></h3>
      <p>Understanding odds and odds ratios in applied contexts.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/modeling/extensions/odds/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/modeling/extensions/interpreting-logistic-coefficients/">5. Interpreting Logistic Regression Coefficients</a></h3>
      <p>What coefficients mean in terms of log-odds and changes in risk.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/modeling/extensions/interpreting-logistic-coefficients/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/modeling/extensions/glm/">6. Generalized Linear Models</a></h3>
      <p>The broader family that includes linear and logistic regression.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/modeling/extensions/glm/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/modeling/extensions/link-functions/">7. Link Functions</a></h3>
      <p>How generalized models connect predictors to different outcome types.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/modeling/extensions/link-functions/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/modeling/extensions/comparing-linear-and-logistic/">8. Linear vs Logistic Regression</a></h3>
      <p>When each model is appropriate and how their interpretations differ.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/modeling/extensions/comparing-linear-and-logistic/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/modeling/extensions/bridge-to-machine-learning/">9. Bridge to Machine Learning</a></h3>
      <p>How model extensions prepare the way for more flexible predictive methods.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/modeling/extensions/bridge-to-machine-learning/">Open lesson</a>
      </div>
    </div>

  </div>
</section>

<!-- OUTCOME -->
<section class="section section-slim">
  <div class="callout">

    <div class="callout-copy">
      <h2>Outcome of Block 7</h2>
      <ul class="bullets">
        <li>Understand why linear regression has limits</li>
        <li>Explain the logic of logistic regression</li>
        <li>Interpret odds, log-odds, and logistic coefficients</li>
        <li>Understand the idea of generalized linear models</li>
        <li>See how statistical modeling extends toward broader frameworks</li>
      </ul>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Next section</div>
        <div class="mini-body">
          Continue to
          <a href="/applied-statistics/" style="color:#1a73e8; text-decoration:underline;">
            <strong>Applied Statistics</strong>
          </a>.
        </div>
      </div>
    </div>

  </div>
</section>

<!-- CONTINUE READING SCRIPT -->
<script>
(function () {
  var KEY = "esa_continue_modeling_extensions_lesson_v0";
  var raw = localStorage.getItem(KEY);
  if (!raw) return;

  try {
    var data = JSON.parse(raw);
    if (!data || !data.url || !data.label) return;

    var wrap = document.getElementById("continue-reading-extensions");
    var label = document.getElementById("continue-reading-extensions-label");
    var btn = document.getElementById("continue-reading-extensions-btn");

    label.innerHTML = 'You last visited: <strong>' + data.label + '</strong>';
    btn.href = data.url;
    wrap.style.display = "block";

  } catch (e) {}
})();
</script>