---
layout: default
title: "1. What Is Conditional Probability?"
description: "Understand how conditioning changes the sample space and how to compute conditional probability correctly."
permalink: /probability/conditional/what-is-conditional-probability/
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
        Version 0 establishes the correct conceptual foundation. Visual diagrams,
        simulations, and applied examples will be added later.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update last visited lesson (conditional block key) -->
<script>
  (function () {
    var KEY = "esa_continue_probability_conditional_lesson_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/probability/conditional/what-is-conditional-probability/",
      label: "Conditional Lesson 1 — What Is Conditional Probability?",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">

      <div class="badge-row">
        <span class="badge">Block 2</span>
        <span class="badge">Lesson 1</span>
        <span class="badge">Conditioning</span>
        <span class="badge">Core concept</span>
      </div>

      <h1>1. What Is Conditional Probability?</h1>

      <p class="lead">
        Conditional probability measures how probabilities change
        when new information becomes available.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/probability/basics/">
          ← Previous Block: Probability Basics
        </a>
        <a class="btn btn-outline" href="/probability/conditional/">
          Back to Conditional Block
        </a>
      </div>

      <p class="muted-mini">
        Conditioning changes the sample space.
      </p>

    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
  </div>

  <ul class="bullets">
    <li>Understand how conditioning restricts the sample space</li>
    <li>Define conditional probability formally</li>
    <li>Compute conditional probability correctly</li>
  </ul>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Intuition: Updating with information</h2>
  </div>

  <div class="card">
    <p>
      Suppose you roll a fair die.
    </p>

    <p>
      Probability of rolling a 4:
    </p>

    <p><strong>P(4) = 1/6</strong></p>

    <p>
      Now suppose you are told the result is even.
    </p>

    <p>
      The possible outcomes are now {2,4,6}.
    </p>

    <p>
      The probability of 4 changes:
    </p>

    <p><strong>P(4 | even) = 1/3</strong></p>
  </div>

  <div class="callout">
    <div class="callout-copy">
      <h2>Key insight</h2>
      <p style="margin:0;">
        Conditioning shrinks the sample space.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Formal Definition</h2>
  </div>

  <div class="card">
    <p>
      If P(B) > 0, then:
    </p>

    <p><strong>P(A | B) = P(A ∩ B) / P(B)</strong></p>

    <p>
      Read as:
      “Probability of A given B”
    </p>
  </div>

  <div class="card">
    <h3>Interpretation</h3>
    <p>
      Among cases where B occurs,
      what fraction also satisfy A?
    </p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Why this formula makes sense</h2>
  </div>

  <div class="card">
    <p>
      If we restrict attention only to B,
      the total probability mass becomes P(B).
    </p>

    <p>
      We then rescale probabilities within that restricted universe.
    </p>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Common mistakes</h2>
      <ul class="bullets">
        <li>Forgetting to divide by P(B)</li>
        <li>Ignoring that P(B) must be positive</li>
        <li>Confusing P(A|B) with P(B|A)</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Understand how new information changes probability</li>
        <li>Use the conditional probability formula correctly</li>
        <li>Prepare for multiplication rule next</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next lesson</h2>
      <p style="margin:0;">
        Now we derive the multiplication rule from conditional probability.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/probability/conditional/multiplication-rule/">
          Next lesson: 2. The Multiplication Rule →
        </a>
      </div>
    </div>
  </div>
</section>