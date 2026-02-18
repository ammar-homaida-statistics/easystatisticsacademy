---
layout: default
title: "7. Probability Language Traps (Common Mistakes)"
description: "Identify and avoid common probability errors caused by ambiguous language and hidden assumptions."
permalink: /probability/basics/conditional-language-traps/
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
        Version 0 focuses on reasoning clarity. Numerical examples,
        diagrams, and simulations will be added later.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update last visited lesson for basics block -->
<script>
  (function () {
    var KEY = "esa_continue_probability_basics_lesson_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/probability/basics/conditional-language-traps/",
      label: "Lesson 7 — Probability Language Traps",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">

      <div class="badge-row">
        <span class="badge">Block 1</span>
        <span class="badge">Lesson 7</span>
        <span class="badge">Reasoning</span>
      </div>

      <h1>7. Probability Language Traps</h1>

      <p class="lead">
        Many probability mistakes come from ambiguous wording,
        not from mathematics. This lesson strengthens logical translation skills.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/probability/basics/independence-vs-disjointness/">
          ← Previous lesson: 6. Independence vs Disjointness
        </a>
        <a class="btn btn-outline" href="/probability/basics/">
          Back to Block 1
        </a>
      </div>

      <p class="muted-mini">
        Clear definitions prevent wrong answers.
      </p>

    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
  </div>

  <ul class="bullets">
    <li>Translate ambiguous phrases into precise events</li>
    <li>Recognize hidden modeling assumptions</li>
    <li>Avoid common logical fallacies</li>
  </ul>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) “At least one”</h2>
  </div>

  <div class="card">
    <p>
      “At least one” means one or more.
    </p>

    <p><strong>P(at least one) = 1 − P(none)</strong></p>

    <p>
      Using the complement is often simpler and safer.
    </p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) “Exactly one”</h2>
  </div>

  <div class="card">
    <p>
      Exactly one means:
    </p>

    <p>
      (A ∩ Bᶜ) ∪ (Aᶜ ∩ B)
    </p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) “Either A or B”</h2>
  </div>

  <div class="card">
    <p>
      In probability, “or” is inclusive unless explicitly stated.
    </p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) “Given” — the conditioning signal</h2>
  </div>

  <div class="card">
    <p>
      The word “given” indicates conditional probability.
    </p>

    <p>
      Conditioning restricts the sample space.
    </p>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Hidden independence assumptions</h2>
  </div>

  <div class="card">
    <p>
      Do not multiply probabilities unless independence is justified.
    </p>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Common mistakes checklist</h2>
      <ul class="bullets">
        <li>Misreading “at least”</li>
        <li>Ignoring complement strategy</li>
        <li>Using exclusive OR without justification</li>
        <li>Multiplying without checking independence</li>
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
        <li>Translate ambiguous phrases correctly</li>
        <li>Recognize conditional language</li>
        <li>Avoid silent modeling assumptions</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next lesson</h2>
      <p style="margin:0;">
        We conclude Block 1 by applying all concepts in small modeling cases.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/probability/basics/modeling-randomness-mini-cases/">
          Next lesson: 8. Modeling Randomness: Mini Cases →
        </a>
      </div>
    </div>
  </div>
</section>