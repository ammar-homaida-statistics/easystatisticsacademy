---
layout: default
title: 6. Train vs Test
permalink: /modeling/model-fit-comparison/train-vs-test/
sidebar: false
---

<!-- UNDER CONSTRUCTION -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <h2 style="color:#e65100;">🚧 Lesson Under Construction</h2>
    <p>
      Version 0 introduces the concept of training and test data.
      Cross-validation techniques will be added later.
    </p>
  </div>
</section>

<!-- ✅ Update last visited lesson -->
<script>
(function () {
  localStorage.setItem("esa_continue_modeling_model_fit_lesson_v0", JSON.stringify({
    url: "/modeling/model-fit-comparison/train-vs-test/",
    label: "Lesson 6 — Train vs Test",
    ts: Date.now()
  }));
})();
</script>

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card">

    <div class="badge-row">
      <span class="badge">Block 6</span>
      <span class="badge">Lesson 6</span>
      <span class="badge">Train/Test</span>
      <span class="badge">Generalization</span>
    </div>

    <h1>6. Train vs Test</h1>

    <p class="lead">
      A model must be evaluated on new data to assess its true performance.
      Training and test sets allow us to measure generalization.
    </p>

    <div class="hero-actions">
      <a class="btn btn-outline" href="/modeling/model-fit-comparison/">Back to Block 6</a>
      <a class="btn" href="#lesson">Start lesson</a>
    </div>

    <p class="muted-mini">
      Version 0: conceptual introduction to validation.
    </p>

  </div>
</section>

<!-- LESSON -->
<section class="section" id="lesson">

  <h2>Learning objective</h2>
  <p>
    By the end of this lesson, you should understand how training and test data
    are used to evaluate model performance.
  </p>

  <div class="card">
    <h3>Key idea</h3>
    <p>
      Good models perform well on new, unseen data — not just training data.
    </p>
  </div>

  <h2>1) What is training data?</h2>
  <div class="card">
    <p>
      Training data is used to build the model.
    </p>
  </div>

  <h2>2) What is test data?</h2>
  <div class="card">
    <p>
      Test data is used to evaluate the model’s performance on unseen data.
    </p>
  </div>

  <h2>3) Why we split data</h2>
  <div class="card">
    <p>
      Evaluating a model on the same data used to build it
      gives an overly optimistic result.
    </p>
  </div>

  <h2>4) Detecting overfitting</h2>
  <div class="card">
    <ul>
      <li>Good training performance</li>
      <li>Poor test performance</li>
    </ul>
  </div>

  <h2>5) Detecting underfitting</h2>
  <div class="card">
    <ul>
      <li>Poor training performance</li>
      <li>Poor test performance</li>
    </ul>
  </div>

  <h2>6) Ideal model behavior</h2>
  <div class="card">
    <ul>
      <li>Good training performance</li>
      <li>Good test performance</li>
    </ul>
  </div>

  <h2>7) Generalization</h2>
  <div class="card">
    <p>
      Generalization refers to how well a model performs on new data.
    </p>
  </div>

  <h2>8) Common mistake</h2>
  <div class="card">
    <p>
      Evaluating models only on training data.
    </p>
  </div>

  <h2>9) Limitations</h2>
  <div class="card">
    <p>
      A single train-test split can be unstable.
      More robust methods (e.g., cross-validation) are used later.
    </p>
  </div>

  <h2>10) Why this matters</h2>
  <div class="card">
    <p>
      Model evaluation must reflect real-world performance,
      not just performance on known data.
    </p>
  </div>

  <div class="card">
    <h3>Outcome of this lesson</h3>
    <ul>
      <li>Understand train vs test data</li>
      <li>Detect overfitting and underfitting</li>
      <li>Define generalization</li>
      <li>Avoid evaluation mistakes</li>
      <li>Prepare for model comparison</li>
    </ul>
  </div>

  <div class="card">
    <h3>Next step</h3>
    <p>
      We now compare multiple models
      to select the best one.
    </p>
    <a class="btn" href="/modeling/model-fit-comparison/model-comparison/">
      Next lesson: Model Comparison →
    </a>
  </div>

</section>