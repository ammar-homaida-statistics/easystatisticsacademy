---
layout: default
title: "8. Modeling Randomness: Mini Cases"
description: "Apply probability concepts to small real-world scenarios using structured modeling."
permalink: /probability/basics/modeling-randomness-mini-cases/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem;">
        🚧 Lesson Under Construction
      </h2>
      <p style="margin:0; font-size:1.05rem; line-height:1.6;">
        Version 0 consolidates all concepts from Block 1.
        Numerical simulations, diagrams, and software examples will be added later.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update last visited lesson for basics -->
<script>
  (function () {
    var KEY = "esa_continue_probability_basics_lesson_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/probability/basics/modeling-randomness-mini-cases/",
      label: "Lesson 8 — Modeling Randomness: Mini Cases",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">

      <div class="badge-row">
        <span class="badge">Block 1</span>
        <span class="badge">Lesson 8</span>
        <span class="badge">Application</span>
        <span class="badge">Modeling</span>
      </div>

      <h1>8. Modeling Randomness: Mini Cases</h1>

      <p class="lead">
        Probability is not about formulas — it is about modeling.
        This lesson applies all previous concepts in small structured examples.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/probability/basics/conditional-language-traps/">
          ← Previous lesson: 7. Probability Language Traps
        </a>
        <a class="btn btn-outline" href="/probability/basics/">
          Back to Block 1
        </a>
      </div>

      <p class="muted-mini">
        Good probability = good modeling + correct rules.
      </p>

    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
  </div>

  <ul class="bullets">
    <li>Translate real-world descriptions into probability models</li>
    <li>Define sample space explicitly</li>
    <li>Identify events precisely</li>
    <li>Apply correct rules without hidden assumptions</li>
  </ul>
</section>

<section class="section">
  <div class="section-head">
    <h2>Mini Case 1 — Coin and Die</h2>
  </div>

  <div class="card">
    <p>
      A fair coin is tossed and a fair die is rolled.
    </p>

    <p><strong>Step 1: Define sample space</strong></p>

    <p>
      Outcomes are ordered pairs:
      (H,1), (H,2), ..., (T,6)
    </p>

    <p>Total outcomes = 12</p>

    <p><strong>Step 2: Define event</strong></p>

    <p>
      Event A = “Head and even number”
    </p>

    <p>Favorable outcomes = (H,2), (H,4), (H,6)</p>

    <p><strong>Step 3: Compute probability</strong></p>

    <p>P(A) = 3 / 12 = 1/4</p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Mini Case 2 — At Least One Success</h2>
  </div>

  <div class="card">
    <p>
      Two independent machines each fail with probability 0.1.
    </p>

    <p><strong>Question:</strong> What is the probability at least one fails?</p>

    <p><strong>Step 1: Use complement</strong></p>

    <p>
      Probability none fail:
      (0.9 × 0.9) = 0.81
    </p>

    <p><strong>Step 2:</strong></p>

    <p>
      P(at least one fails) = 1 − 0.81 = 0.19
    </p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Mini Case 3 — Disjoint vs Independent</h2>
  </div>

  <div class="card">
    <p>
      Roll a fair die.
    </p>

    <p>
      A = “Even number”
      B = “Number greater than 3”
    </p>

    <p>
      A = {2,4,6}
      B = {4,5,6}
    </p>

    <p>
      A ∩ B = {4,6}
    </p>

    <p>
      They overlap → not disjoint.
    </p>

    <p>
      Check independence:
    </p>

    <p>
      P(A) = 3/6  
      P(B) = 3/6  
      P(A ∩ B) = 2/6
    </p>

    <p>
      P(A)P(B) = (3/6)(3/6) = 9/36 = 1/4  
      P(A ∩ B) = 2/6 = 1/3
    </p>

    <p>
      Since 1/3 ≠ 1/4 → not independent.
    </p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Modeling Checklist</h2>
  </div>

  <div class="card">
    <ul class="bullets">
      <li>What is the experiment?</li>
      <li>What are the possible outcomes?</li>
      <li>Are outcomes equally likely?</li>
      <li>What is the exact event definition?</li>
      <li>Are events independent or disjoint?</li>
      <li>Can complement simplify the calculation?</li>
    </ul>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of Block 1</h2>
      <ul class="bullets">
        <li>Define events precisely</li>
        <li>Use axioms and rules correctly</li>
        <li>Translate language into set logic</li>
        <li>Model simple random experiments</li>
        <li>Recognize independence and disjointness</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next Block</h2>
      <p style="margin:0;">
        Now we move to Block 2: Conditional Probability.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/probability/conditional/">
          Continue to Conditional Probability →
        </a>
      </div>
    </div>
  </div>
</section>