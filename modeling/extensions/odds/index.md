---
layout: default
title: 4. Odds
permalink: /modeling/extensions/odds/
sidebar: false
---

<!-- UNDER CONSTRUCTION -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <h2 style="color:#e65100;">🚧 Lesson Under Construction</h2>
    <p>
      Version 0 introduces odds conceptually and connects it to probability.
      Interpretation and applications will be expanded later.
    </p>
  </div>
</section>

<!-- ✅ Update last visited lesson -->
<script>
(function () {
  localStorage.setItem("esa_continue_modeling_extensions_lesson_v0", JSON.stringify({
    url: "/modeling/extensions/odds/",
    label: "Lesson 4 — Odds",
    ts: Date.now()
  }));
})();
</script>

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Block 7</span>
      <span class="badge">Lesson 4</span>
      <span class="badge">Odds</span>
      <span class="badge">Probability</span>
    </div>

    <h1>4. Odds</h1>

    <p class="lead">
      Odds express the likelihood of an event as a ratio.
      They provide the foundation for the logit transformation used in logistic regression.
    </p>

    <div class="hero-actions">
      <a class="btn btn-outline" href="/modeling/extensions/">Back to Block 7</a>
      <a class="btn" href="#lesson">Start lesson</a>
    </div>

    <p class="muted-mini">
      Version 0: conceptual understanding of odds before logit interpretation.
    </p>

  </div>
</section>

<!-- LESSON -->
<section class="section" id="lesson">

  <h2>Learning objective</h2>
  <p>
    By the end of this lesson, you should understand what odds are
    and how they relate to probabilities.
  </p>

  <div class="card">
    <h3>Key idea</h3>
    <p>
      Odds compare the probability of an event occurring
      to the probability of it not occurring.
    </p>
  </div>

  <h2>1) Definition of odds</h2>
  <div class="card">
    <p>
      Odds are defined as:
    </p>
    <p><strong>odds = p / (1 − p)</strong></p>
  </div>

  <h2>2) Example</h2>
  <div class="card">
    <p>
      If the probability of success is 0.75:
    </p>
    <ul>
      <li>p = 0.75</li>
      <li>1 − p = 0.25</li>
      <li>odds = 0.75 / 0.25 = 3</li>
    </ul>
    <p>
      This means the event is 3 times more likely to occur than not.
    </p>
  </div>

  <h2>3) Interpreting odds</h2>
  <div class="card">
    <ul>
      <li>odds = 1 → event equally likely as not</li>
      <li>odds > 1 → event more likely than not</li>
      <li>odds < 1 → event less likely than not</li>
    </ul>
  </div>

  <h2>4) Odds vs probability</h2>
  <div class="card">
    <ul>
      <li>Probability → bounded between 0 and 1</li>
      <li>Odds → range from 0 to ∞</li>
    </ul>
  </div>

  <h2>5) Why odds are useful</h2>
  <div class="card">
    <p>
      Odds can be transformed into a linear scale using the logit.
    </p>
  </div>

  <h2>6) Common misunderstanding</h2>
  <div class="card">
    <p>
      Odds are not the same as probability.
    </p>
  </div>

  <h2>7) Example comparison</h2>
  <div class="card">
    <ul>
      <li>p = 0.5 → odds = 1</li>
      <li>p = 0.8 → odds = 4</li>
      <li>p = 0.2 → odds = 0.25</li>
    </ul>
  </div>

  <h2>8) Why this matters</h2>
  <div class="card">
    <p>
      Logistic regression coefficients are interpreted in terms of odds,
      not probabilities directly.
    </p>
  </div>

  <h2>9) From odds to logit</h2>
  <div class="card">
    <p>
      The logit is the logarithm of odds.
    </p>
  </div>

  <h2>10) Big picture</h2>
  <div class="card">
    <p>
      Probability → Odds → Logit → Linear model
    </p>
  </div>

  <div class="card">
    <h3>Outcome of this lesson</h3>
    <ul>
      <li>Understand what odds represent</li>
      <li>Convert probability to odds</li>
      <li>Interpret odds correctly</li>
      <li>Distinguish odds from probability</li>
      <li>Prepare for coefficient interpretation</li>
    </ul>
  </div>

  <div class="card">
    <h3>Next step</h3>
    <p>
      We now interpret logistic regression coefficients
      using odds and log-odds.
    </p>
    <a class="btn" href="/modeling/extensions/interpreting-logistic-coefficients/">
      Next lesson: Interpreting Logistic Coefficients →
    </a>
  </div>

</section>