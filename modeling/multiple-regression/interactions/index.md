---
layout: default
title: 8. Interaction Effects
permalink: /modeling/multiple-regression/interactions/
sidebar: false
---

<!-- UNDER CONSTRUCTION -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <h2 style="color:#e65100;">🚧 Lesson Under Construction</h2>
    <p>
      Version 0 introduces interaction effects conceptually.
      Formal modeling and visualization will be expanded later.
    </p>
  </div>
</section>

<!-- ✅ Update last visited lesson -->
<script>
(function () {
  localStorage.setItem("esa_continue_modeling_mr_lesson_v0", JSON.stringify({
    url: "/modeling/multiple-regression/interactions/",
    label: "Lesson 8 — Interaction Effects",
    ts: Date.now()
  }));
})();
</script>

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Block 3</span>
      <span class="badge">Lesson 8</span>
      <span class="badge">Interactions</span>
      <span class="badge">Non-Additive Effects</span>
    </div>

    <h1>8. Interaction Effects</h1>

    <p class="lead">
      An interaction occurs when the effect of one predictor depends
      on the value of another predictor.
    </p>

    <div class="hero-actions">
      <a class="btn btn-outline" href="/modeling/multiple-regression/">Back to Block 3</a>
      <a class="btn" href="#lesson">Start lesson</a>
    </div>

    <p class="muted-mini">
      Version 0: conceptual understanding before formal modeling.
    </p>

  </div>
</section>

<!-- LESSON -->
<section class="section" id="lesson">

  <h2>Learning objective</h2>
  <p>
    By the end of this lesson, you should understand what interaction effects are
    and why they are important in modeling.
  </p>

  <div class="card">
    <h3>Key idea</h3>
    <p>
      The effect of one variable on the outcome can change depending on another variable.
    </p>
  </div>

  <h2>1) Additive vs interaction models</h2>
  <div class="card">
    <p>
      Additive model:
    </p>
    <p><strong>Y = β₀ + β₁X₁ + β₂X₂</strong></p>

    <p>
      Interaction model:
    </p>
    <p><strong>Y = β₀ + β₁X₁ + β₂X₂ + β₃(X₁ × X₂)</strong></p>
  </div>

  <h2>2) What does the interaction term mean?</h2>
  <div class="card">
    <p>
      The coefficient β₃ measures how the effect of X₁ changes
      as X₂ changes.
    </p>
  </div>

  <h2>3) Example</h2>
  <div class="card">
    <p>
      Study hours and tutoring:
    </p>
    <ul>
      <li>Hours studied may have a stronger effect when tutoring is present</li>
      <li>The effect is not constant</li>
    </ul>
  </div>

  <h2>4) Interpretation</h2>
  <div class="card">
    <p>
      With interaction, the effect of X₁ is no longer fixed —
      it depends on X₂.
    </p>
  </div>

  <h2>5) Graphical intuition</h2>
  <div class="card">
    <ul>
      <li>No interaction → parallel lines</li>
      <li>Interaction → lines with different slopes</li>
    </ul>
  </div>

  <h2>6) When interactions are important</h2>
  <div class="card">
    <ul>
      <li>Different groups behave differently</li>
      <li>Effects vary across conditions</li>
      <li>Relationships are not purely additive</li>
    </ul>
  </div>

  <h2>7) Common mistakes</h2>
  <div class="card">
    <ul>
      <li>Ignoring interactions when they exist</li>
      <li>Overfitting with unnecessary interactions</li>
      <li>Misinterpreting main effects when interaction is present</li>
    </ul>
  </div>

  <h2>8) Why this matters</h2>
  <div class="card">
    <p>
      Interaction effects allow models to represent more realistic relationships
      where effects depend on context.
    </p>
  </div>

  <div class="card">
    <h3>Outcome of this lesson</h3>
    <ul>
      <li>Define interaction effects</li>
      <li>Understand interaction terms</li>
      <li>Distinguish additive vs interaction models</li>
      <li>Interpret interaction conceptually</li>
      <li>Recognize when interactions are needed</li>
    </ul>
  </div>

  <div class="card">
    <h3>Next step</h3>
    <p>
      Now we bring everything together and learn how to build models in practice.
    </p>
    <a class="btn" href="/modeling/multiple-regression/model-building/">
      Next lesson: Model Building →
    </a>
  </div>

</section>