---
layout: default
title: "4. Union, Intersection & Venn Thinking"
description: "Translate language into probability using set logic: union, intersection, disjoint events, and visual reasoning."
permalink: /probability/basics/union-intersection-and-venn-thinking/
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
        Version 0 establishes correct reasoning patterns. Diagrams, software visuals,
        and interactive examples will be added later.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update last visited lesson -->
<script>
  (function () {
    var KEY = "esa_continue_probability_basics_lesson_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/probability/basics/union-intersection-and-venn-thinking/",
      label: "Lesson 4 — Union, Intersection & Venn Thinking",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">

      <div class="badge-row">
        <span class="badge">Block 1</span>
        <span class="badge">Lesson 4</span>
        <span class="badge">Visual reasoning</span>
        <span class="badge">Logic</span>
      </div>

      <h1>4. Union, Intersection &amp; Venn Thinking</h1>

      <p class="lead">
        Most probability errors are language errors.  
        This lesson teaches you how to translate words like “and”, “or”, and “at least”
        into precise mathematical events.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/probability/basics/probability-axioms-and-basic-rules/">
          ← Previous lesson: 3. Probability Axioms & Basic Rules
        </a>
        <a class="btn btn-outline" href="/probability/basics/">Back to Block 1</a>
      </div>

      <p class="muted-mini">
        Precision in language = precision in probability.
      </p>

    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
  </div>

  <ul class="bullets">
    <li>Translate verbal statements into events</li>
    <li>Understand union (∪) and intersection (∩)</li>
    <li>Recognize disjoint vs overlapping events</li>
    <li>Avoid common language-based probability mistakes</li>
  </ul>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) Intersection (A ∩ B) — “AND”</h2>
    <p>
      The intersection of two events means both occur.
    </p>
  </div>

  <div class="card">
    <h3>Examples</h3>
    <ul class="bullets">
      <li>“Roll an even number AND greater than 3” → {4,6}</li>
      <li>“Student is female AND passed the exam”</li>
      <li>“Customer buys product A AND product B”</li>
    </ul>
  </div>

  <div class="callout">
    <div class="callout-copy">
      <h2>Key idea</h2>
      <p style="margin:0;">
        Intersection reduces the number of outcomes.
        It makes the event more specific.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) Union (A ∪ B) — “OR”</h2>
    <p>
      The union of two events means at least one occurs.
    </p>
  </div>

  <div class="card">
    <h3>Important clarification</h3>
    <p>
      In probability, “OR” is inclusive — meaning:
    </p>
    <ul class="bullets">
      <li>A occurs</li>
      <li>B occurs</li>
      <li>Both occur</li>
    </ul>
  </div>

  <div class="card">
    <h3>Examples</h3>
    <ul class="bullets">
      <li>“Roll a 2 OR a 4” → {2,4}</li>
      <li>“Student passed OR received extra credit”</li>
    </ul>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) Disjoint (Mutually Exclusive) Events</h2>
  </div>

  <div class="card">
    <p>
      Two events are disjoint if they cannot happen together.
    </p>
    <p><strong>A ∩ B = ∅</strong></p>
  </div>

  <div class="card">
    <h3>Example</h3>
    <ul class="bullets">
      <li>Rolling a 2 AND rolling a 5 (single die roll)</li>
    </ul>
  </div>

  <div class="callout">
    <div class="callout-copy">
      <h2>Warning</h2>
      <p style="margin:0;">
        Disjoint does NOT mean independent.
        (You will revisit this in Lesson 6.)
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Translating Common Phrases</h2>
  </div>

  <div class="grid grid-2">

    <div class="card">
      <h3>“At least one”</h3>
      <p>
        Means 1 or more.
        Often easier to compute using the complement rule.
      </p>
    </div>

    <div class="card">
      <h3>“Exactly one”</h3>
      <p>
        Means one occurs AND the other does not.
      </p>
    </div>

    <div class="card">
      <h3>“Either A or B”</h3>
      <p>
        Usually inclusive OR unless explicitly stated otherwise.
      </p>
    </div>

    <div class="card">
      <h3>“Neither A nor B”</h3>
      <p>
        Complement of (A ∪ B).
      </p>
    </div>

  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>5) Why Venn Thinking Helps</h2>
  </div>

  <div class="card">
    <p>
      Visualizing events as overlapping regions prevents:
    </p>
    <ul class="bullets">
      <li>Double-counting probabilities</li>
      <li>Forgetting intersections</li>
      <li>Confusing AND with OR</li>
    </ul>
  </div>

  <div class="callout">
    <div class="callout-copy">
      <h2>Golden rule</h2>
      <p style="margin:0;">
        Always rewrite a verbal statement as:
        <br><br>
        “Let A be …”  
        “Let B be …”
        <br><br>
        Then express the event using ∪, ∩, or complement.
      </p>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Common mistakes</h2>
      <ul class="bullets">
        <li>Interpreting “or” as exclusive when it is inclusive</li>
        <li>Adding probabilities without checking overlap</li>
        <li>Ignoring whether events can occur together</li>
        <li>Failing to define A and B explicitly</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Translate language into mathematical events</li>
        <li>Use union and intersection correctly</li>
        <li>Recognize disjoint events</li>
        <li>Prepare for counting-based probability next</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next lesson</h2>
      <p style="margin:0;">
        Now we examine when outcomes are equally likely and how counting determines probability.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/probability/basics/equally-likely-and-counting-intuition/">
          Next lesson: 5. Equally Likely Outcomes & Counting Intuition →
        </a>
      </div>
    </div>
  </div>
</section>