---
layout: default
title: 1. What Is a Model?
permalink: /modeling/foundations/what-is-a-model/
sidebar: false
---

<!-- UNDER CONSTRUCTION -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <h2 style="color:#e65100;">🚧 Lesson Under Construction</h2>
    <p>
      Version 0 focuses on conceptual understanding of models.
      Examples, visuals, and software applications will be added later.
    </p>
  </div>
</section>

<!-- ✅ Update last visited lesson -->
<script>
(function () {
  localStorage.setItem("esa_continue_modeling_foundations_lesson_v0", JSON.stringify({
    url: "/modeling/foundations/what-is-a-model/",
    label: "Lesson 1 — What Is a Model?",
    ts: Date.now()
  }));
})();
</script>

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Block 1</span>
      <span class="badge">Lesson 1</span>
      <span class="badge">Modeling</span>
      <span class="badge">Foundations</span>
    </div>

    <h1>1. What Is a Model?</h1>

    <p class="lead">
      A statistical model is a simplified representation of reality.
      It captures relationships between variables in a structured way,
      allowing us to explain patterns and make predictions.
    </p>

    <div class="hero-actions">
      <a class="btn btn-outline" href="/modeling/foundations/">Back to Block 1</a>
      <a class="btn" href="#lesson">Start lesson</a>
    </div>

    <p class="muted-mini">
      Version 0: concept-first. Examples and applications will follow.
    </p>

  </div>
</section>

<!-- LESSON CONTENT -->
<section class="section" id="lesson">

  <h2>Learning objective</h2>
  <p>
    By the end of this lesson, you should understand what a model is,
    why models are necessary, and how they relate to data and reality.
  </p>

  <div class="card">
    <h3>Key idea</h3>
    <p>
      A model is not reality. It is a tool that approximates reality
      using mathematical structure to make reasoning possible.
    </p>
  </div>

  <h2>1) Why do we need models?</h2>
  <div class="card">
    <p>
      Real-world systems are complex. We cannot directly analyze everything at once.
      Models simplify reality so that we can understand patterns, relationships,
      and make decisions.
    </p>
  </div>

  <h2>2) Model = simplified structure</h2>
  <div class="card">
    <p>
      A statistical model typically expresses a relationship between variables:
    </p>
    <p><strong>Outcome = function(inputs) + error</strong></p>
    <p>
      The model explains part of the variation, while the rest remains unexplained (noise).
    </p>
  </div>

  <h2>3) Components of a model</h2>
  <div class="card">
    <ul>
      <li><strong>Inputs (predictors)</strong> — variables used to explain</li>
      <li><strong>Output (response)</strong> — variable we want to understand</li>
      <li><strong>Parameters</strong> — quantities that define the relationship</li>
      <li><strong>Error term</strong> — randomness not explained by the model</li>
    </ul>
  </div>

  <h2>4) Models are approximations</h2>
  <div class="card">
    <p>
      No model is perfectly true. Every model ignores some aspects of reality.
      The goal is not perfection, but usefulness.
    </p>
  </div>

  <h2>5) Two main goals of modeling</h2>
  <div class="card">
    <ul>
      <li><strong>Explanation</strong> — understand relationships</li>
      <li><strong>Prediction</strong> — forecast outcomes</li>
    </ul>
  </div>

  <h2>6) Example (intuitive)</h2>
  <div class="card">
    <p>
      Suppose we model house price using size:
    </p>
    <p><strong>Price = β₀ + β₁ × Size + error</strong></p>
    <p>
      The model captures the main trend, but many factors remain in the error term.
    </p>
  </div>

  <h2>7) Why this matters</h2>
  <div class="card">
    <p>
      Understanding what a model is prevents common mistakes:
      treating models as truth, over-interpreting results,
      or ignoring uncertainty.
    </p>
  </div>

  <div class="card">
    <h3>Outcome of this lesson</h3>
    <ul>
      <li>Define what a statistical model is</li>
      <li>Explain why models are needed</li>
      <li>Identify components of a model</li>
      <li>Understand models as approximations</li>
    </ul>
  </div>

  <div class="card">
    <h3>Next step</h3>
    <p>Next we define variables and how relationships are formed.</p>
    <a class="btn" href="/modeling/foundations/variables/">
      Next lesson: Variables and Relationships →
    </a>
  </div>

</section>