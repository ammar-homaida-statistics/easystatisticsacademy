---
layout: default
title: "3. Probability Axioms & Basic Rules"
description: "The three probability axioms and the fundamental rules derived from them: complement, union, and bounds."
permalink: /probability/basics/probability-axioms-and-basic-rules/
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
        Version 0 focuses on conceptual correctness. Examples, visuals, and software demonstrations
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
      url: "/probability/basics/probability-axioms-and-basic-rules/",
      label: "Lesson 3 — Probability Axioms & Basic Rules",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">

      <div class="badge-row">
        <span class="badge">Block 1</span>
        <span class="badge">Lesson 3</span>
        <span class="badge">Rules</span>
        <span class="badge">Mathematical foundation</span>
      </div>

      <h1>3. Probability Axioms &amp; Basic Rules</h1>

      <p class="lead">
        Probability is not arbitrary. It follows three fundamental axioms.
        From these, all basic probability rules are derived.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/probability/basics/outcomes-sample-spaces-events/">
          ← Previous lesson: 2. Outcomes, Sample Spaces & Events
        </a>
        <a class="btn btn-outline" href="/probability/basics/">Back to Block 1</a>
      </div>

      <p class="muted-mini">
        These rules guarantee consistency. Violating them leads to logical contradictions.
      </p>

    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      By the end of this lesson, you should:
    </p>
  </div>

  <ul class="bullets">
    <li>Know the three probability axioms</li>
    <li>Use complement and union rules correctly</li>
    <li>Understand why probabilities must obey logical constraints</li>
  </ul>
</section>

<section class="section">
  <div class="section-head">
    <h2>The Three Probability Axioms</h2>
  </div>

  <div class="card">
    <h3>Axiom 1 — Non-negativity</h3>
    <p>
      For any event A:
    </p>
    <p><strong>P(A) ≥ 0</strong></p>
    <p>
      Probability cannot be negative.
    </p>
  </div>

  <div class="card">
    <h3>Axiom 2 — Total probability equals 1</h3>
    <p>
      The probability of the entire sample space S is:
    </p>
    <p><strong>P(S) = 1</strong></p>
    <p>
      Something in the sample space must happen.
    </p>
  </div>

  <div class="card">
    <h3>Axiom 3 — Additivity (for disjoint events)</h3>
    <p>
      If A and B cannot occur together (disjoint):
    </p>
    <p><strong>P(A ∪ B) = P(A) + P(B)</strong></p>
    <p>
      If events do not overlap, their probabilities add.
    </p>
  </div>

  <div class="callout">
    <div class="callout-copy">
      <h2>Important</h2>
      <p style="margin:0;">
        All probability rules you will ever use come from these three axioms.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Derived Rule 1 — Complement Rule</h2>
  </div>

  <div class="card">
    <p>
      The probability that event A does not occur is:
    </p>
    <p><strong>P(Aᶜ) = 1 − P(A)</strong></p>
    <p>
      This follows directly from Axiom 2.
    </p>
  </div>

  <div class="callout">
    <div class="callout-copy">
      <h2>Why this rule is powerful</h2>
      <p style="margin:0;">
        Sometimes it is easier to compute the probability of the opposite event.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Derived Rule 2 — General Addition Rule</h2>
  </div>

  <div class="card">
    <p>
      For any two events A and B:
    </p>
    <p><strong>P(A ∪ B) = P(A) + P(B) − P(A ∩ B)</strong></p>
    <p>
      We subtract the overlap because it was counted twice.
    </p>
  </div>

  <div class="card">
    <h3>Special case (disjoint events)</h3>
    <p>
      If A and B cannot happen together:
    </p>
    <p><strong>P(A ∪ B) = P(A) + P(B)</strong></p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Probability Bounds</h2>
  </div>

  <div class="card">
    <p>
      For any event A:
    </p>
    <p><strong>0 ≤ P(A) ≤ 1</strong></p>
  </div>

  <div class="card">
    <p>
      For any two events:
    </p>
    <p><strong>P(A ∩ B) ≤ P(A)</strong></p>
    <p>
      The probability of a more specific event cannot exceed the probability of a broader one.
    </p>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Common mistakes</h2>
      <ul class="bullets">
        <li>Forgetting to subtract the intersection in the union rule</li>
        <li>Adding probabilities of overlapping events directly</li>
        <li>Assigning probabilities greater than 1</li>
        <li>Ignoring whether events are disjoint</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Understand the three probability axioms</li>
        <li>Use complement and addition rules correctly</li>
        <li>Recognize logical consistency requirements</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next lesson</h2>
      <p style="margin:0;">
        Now we apply these rules using visual reasoning and Venn diagrams.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/probability/basics/union-intersection-and-venn-thinking/">
          Next lesson: 4. Union, Intersection & Venn Thinking →
        </a>
      </div>
    </div>
  </div>
</section>