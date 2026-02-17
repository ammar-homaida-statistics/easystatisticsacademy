---
layout: default
title: "6. Independence vs Disjointness"
description: "Understand the crucial difference between independent events and mutually exclusive (disjoint) events."
permalink: /probability/basics/independence-vs-disjointness/
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
        Version 0 focuses on deep conceptual clarity. Visual demonstrations and simulations
        will be added later.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update last visited lesson -->
<script>
  (function () {
    var KEY = "esa_continue_probability_basics_lesson_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/probability/basics/independence-vs-disjointness/",
      label: "Lesson 6 — Independence vs Disjointness",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">

      <div class="badge-row">
        <span class="badge">Block 1</span>
        <span class="badge">Lesson 6</span>
        <span class="badge">Core clarity</span>
        <span class="badge">Logical distinction</span>
      </div>

      <h1>6. Independence vs Disjointness</h1>

      <p class="lead">
        These two concepts are often confused — but they are completely different.
        Understanding the difference prevents serious probability mistakes.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/probability/basics/equally-likely-and-counting-intuition/">
          ← Previous lesson: 5. Equally Likely Outcomes & Counting Intuition
        </a>
        <a class="btn btn-outline" href="/probability/basics/">Back to Block 1</a>
      </div>

      <p class="muted-mini">
        This distinction is fundamental for conditional probability and inference.
      </p>

    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
  </div>

  <ul class="bullets">
    <li>Define independence formally</li>
    <li>Define disjoint (mutually exclusive) events</li>
    <li>Understand why they are not the same</li>
    <li>Identify each concept correctly in applied problems</li>
  </ul>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Disjoint (Mutually Exclusive) Events</h2>
  </div>

  <div class="card">
    <p>
      Two events A and B are disjoint if they cannot occur together.
    </p>

    <p><strong>A ∩ B = ∅</strong></p>

    <p>
      This means:
    </p>

    <p><strong>P(A ∩ B) = 0</strong></p>
  </div>

  <div class="card">
    <h3>Example</h3>
    <ul class="bullets">
      <li>Rolling a die: “Roll a 2” and “Roll a 5”</li>
      <li>Single coin toss: “Head” and “Tail”</li>
    </ul>
  </div>

  <div class="callout">
    <div class="callout-copy">
      <h2>Key idea</h2>
      <p style="margin:0;">
        Disjoint events cannot happen at the same time.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Independent Events</h2>
  </div>

  <div class="card">
    <p>
      Two events A and B are independent if:
    </p>

    <p><strong>P(A ∩ B) = P(A) × P(B)</strong></p>

    <p>
      This means:
    </p>

    <p>
      Knowing that A occurred does not change the probability of B.
    </p>
  </div>

  <div class="card">
    <h3>Example</h3>
    <ul class="bullets">
      <li>Two separate coin tosses</li>
      <li>Rolling a die twice</li>
    </ul>
  </div>

  <div class="callout">
    <div class="callout-copy">
      <h2>Key idea</h2>
      <p style="margin:0;">
        Independence is about information — one event does not influence the other.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Why Disjoint ≠ Independent</h2>
  </div>

  <div class="card">
    <h3>Suppose A and B are disjoint</h3>
    <p>
      Then:
    </p>

    <p><strong>P(A ∩ B) = 0</strong></p>

    <p>
      But independence would require:
    </p>

    <p><strong>P(A ∩ B) = P(A) × P(B)</strong></p>

    <p>
      Therefore:
    </p>

    <p><strong>P(A) × P(B) = 0</strong></p>

    <p>
      This can only happen if:
    </p>

    <ul class="bullets">
      <li>P(A) = 0, or</li>
      <li>P(B) = 0</li>
    </ul>

    <p>
      So if both events have positive probability,
      they cannot be both disjoint and independent.
    </p>
  </div>

  <div class="callout">
    <div class="callout-copy">
      <h2>Important conclusion</h2>
      <p style="margin:0;">
        If A and B are disjoint and both have positive probability,
        then they are automatically dependent.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Intuition Comparison</h2>
  </div>

  <div class="grid grid-2">

    <div class="card">
      <h3>Disjoint</h3>
      <ul class="bullets">
        <li>Cannot happen together</li>
        <li>Overlap = 0</li>
        <li>About logical structure</li>
      </ul>
    </div>

    <div class="card">
      <h3>Independent</h3>
      <ul class="bullets">
        <li>Can happen together</li>
        <li>Overlap = product rule</li>
        <li>About informational influence</li>
      </ul>
    </div>

  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Common mistakes</h2>
      <ul class="bullets">
        <li>Thinking “cannot happen together” means independent</li>
        <li>Forgetting to check P(A ∩ B) = P(A)P(B)</li>
        <li>Confusing independence with “unrelated in real life”</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Clearly distinguish independence and disjointness</li>
        <li>Recognize logical contradiction if both assumed</li>
        <li>Prepare for conditional probability (next block)</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next lesson</h2>
      <p style="margin:0;">
        Before moving to conditional probability, we examine common language traps in probability reasoning.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/probability/basics/conditional-language-traps/">
          Next lesson: 7. Probability Language Traps →
        </a>
      </div>
    </div>
  </div>
</section>