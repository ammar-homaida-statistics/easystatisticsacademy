---
layout: default
title: "5. Equally Likely Outcomes & Counting Intuition"
description: "When equally likely reasoning is valid, when it is dangerous, and how counting determines probability."
permalink: /probability/basics/equally-likely-and-counting-intuition/
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
        Version 0 establishes disciplined counting logic. Visual diagrams and software simulations
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
      url: "/probability/basics/equally-likely-and-counting-intuition/",
      label: "Lesson 5 — Equally Likely Outcomes & Counting Intuition",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">

      <div class="badge-row">
        <span class="badge">Block 1</span>
        <span class="badge">Lesson 5</span>
        <span class="badge">Counting</span>
        <span class="badge">Modeling discipline</span>
      </div>

      <h1>5. Equally Likely Outcomes &amp; Counting Intuition</h1>

      <p class="lead">
        Many probability problems assume outcomes are equally likely.
        This lesson teaches when that assumption is valid — and when it is not.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/probability/basics/union-intersection-and-venn-thinking/">
          ← Previous lesson: 4. Union, Intersection & Venn Thinking
        </a>
        <a class="btn btn-outline" href="/probability/basics/">Back to Block 1</a>
      </div>

      <p class="muted-mini">
        Counting works only when modeling assumptions are correct.
      </p>

    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
  </div>

  <ul class="bullets">
    <li>Understand what “equally likely” really means</li>
    <li>Use counting to compute probabilities correctly</li>
    <li>Avoid hidden modeling mistakes</li>
  </ul>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) The equally likely formula</h2>
  </div>

  <div class="card">
    <p>
      If all outcomes in the sample space are equally likely:
    </p>

    <p><strong>P(A) = (number of favorable outcomes) / (total number of outcomes)</strong></p>

    <p>
      This formula only works when each outcome has the same probability.
    </p>
  </div>

  <div class="callout">
    <div class="callout-copy">
      <h2>Important condition</h2>
      <p style="margin:0;">
        You must justify why outcomes are equally likely.
        Never assume it silently.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Simple examples where counting works</h2>
  </div>

  <div class="grid grid-2">

    <div class="card">
      <h3>Example 1: Fair die</h3>
      <p>
        S = {1,2,3,4,5,6}
      </p>
      <p>
        Probability of rolling an even number:
      </p>
      <p>
        Favorable outcomes = {2,4,6} → 3  
        Total outcomes = 6  
        Probability = 3/6 = 1/2
      </p>
    </div>

    <div class="card">
      <h3>Example 2: Two coin tosses</h3>
      <p>
        S = {HH, HT, TH, TT}
      </p>
      <p>
        Probability of exactly one head:
      </p>
      <p>
        Favorable outcomes = {HT, TH} → 2  
        Total outcomes = 4  
        Probability = 2/4 = 1/2
      </p>
    </div>

  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) When counting goes wrong</h2>
  </div>

  <div class="card">
    <h3>Common mistake: Counting incorrectly</h3>
    <p>
      In the two-child example:
    </p>
    <p>
      Sample space should be:
      {BB, BG, GB, GG}
    </p>
    <p>
      If you forget ordering, you may incorrectly use:
      {BB, BG, GG}
    </p>
  </div>

  <div class="card">
    <h3>Common mistake: Assuming equal likelihood without justification</h3>
    <p>
      Example:
      Selecting a random person and asking for their birthday month.
      Are months equally likely? Not necessarily.
    </p>
  </div>

  <div class="callout">
    <div class="callout-copy">
      <h2>Lesson</h2>
      <p style="margin:0;">
        Counting works only if:
        <br>
        1) The sample space is correct  
        2) Outcomes are truly equally likely
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Ordered vs Unordered Outcomes</h2>
  </div>

  <div class="card">
    <p>
      Sometimes order matters.
      Sometimes it does not.
    </p>

    <ul class="bullets">
      <li>Two coin tosses → order matters (HT ≠ TH)</li>
      <li>Choosing two people from a group → order does not matter</li>
    </ul>
  </div>

  <div class="callout">
    <div class="callout-copy">
      <h2>Key modeling question</h2>
      <p style="margin:0;">
        Does the sequence of outcomes matter in this experiment?
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Why counting intuition matters</h2>
  </div>

  <div class="card">
    <p>
      Counting intuition prepares you for:
    </p>

    <ul class="bullets">
      <li>Combinations and permutations (later)</li>
      <li>Binomial probabilities</li>
      <li>Hypergeometric models</li>
      <li>Probability in real-world decision problems</li>
    </ul>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Common mistakes</h2>
      <ul class="bullets">
        <li>Forgetting to define the correct sample space</li>
        <li>Ignoring whether outcomes are equally likely</li>
        <li>Counting without checking order relevance</li>
        <li>Confusing combinations with permutations</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Know when counting applies</li>
        <li>Identify equally likely assumptions</li>
        <li>Model experiments correctly before computing</li>
        <li>Prepare for independence (next lesson)</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next lesson</h2>
      <p style="margin:0;">
        Now we clarify one of the most confused concepts in probability.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/probability/basics/independence-vs-disjointness/">
          Next lesson: 6. Independence vs Disjointness →
        </a>
      </div>
    </div>
  </div>
</section>