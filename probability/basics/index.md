---
layout: default
title: Block 1 — Probability Basics (Events & Rules)
description: Conceptual foundations for probability: sample spaces, events, probability rules, counting intuition, independence vs disjointness, and core reasoning patterns used everywhere in statistics.
permalink: /probability/basics/
sidebar: false
---

<!-- UNDER CONSTRUCTION NOTICE -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem; letter-spacing:0.5px;">
        🚧 This Section Is Under Construction
      </h2>
      <p style="margin:0; font-size:1.05rem; color:#5d4037; line-height:1.6;">
        This block is currently being developed. Lessons will be published in a fixed pedagogical order
        as part of the Probability unit.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update "last visited block" for Probability home -->
<script>
  (function () {
    var KEY = "esa_continue_probability_last_block_v0";

    localStorage.setItem(KEY, JSON.stringify({
      url: "/probability/basics/",
      label: "Block 1 — Probability Basics (Events & Rules)",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card hero-split">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 1</span>
        <span class="badge">Events</span>
        <span class="badge">Rules</span>
        <span class="badge">Intuition</span>
      </div>

      <h1>Block 1 — Probability Basics (Events &amp; Rules)</h1>
      <p class="lead">
        Correct probability starts with correct objects: sample spaces, events, and rules.
        This block builds the core reasoning skills used everywhere later—conditional probability,
        random variables, distributions, and statistical inference.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/probability/">Back to Probability</a>
        <a class="btn" href="#lessons">Open lessons</a>
      </div>

      <p class="muted-mini">
        Version 0: structure is locked. Lessons will be improved over time without changing the overall order.
      </p>
    </div>

    <div class="hero-panel">
      <div class="panel-card">
        <h2 class="panel-title">What this block covers</h2>
        <ul class="quickstart" style="list-style:none; padding-left:0; margin:0;">
          <li style="margin:.35rem 0;"><strong>Randomness & probability</strong><span class="meta">What probability is (and is not)</span></li>
          <li style="margin:.35rem 0;"><strong>Sample spaces & events</strong><span class="meta">Events as sets; outcomes vs events</span></li>
          <li style="margin:.35rem 0;"><strong>Rules & identities</strong><span class="meta">Complement, union, intersection, bounds</span></li>
          <li style="margin:.35rem 0;"><strong>Counting intuition</strong><span class="meta">When “equally likely” makes sense</span></li>
          <li style="margin:.35rem 0;"><strong>Independence vs disjointness</strong><span class="meta">Two common confusions</span></li>
          <li style="margin:.35rem 0;"><strong>Common traps</strong><span class="meta">Base-rate neglect, fallacies, wrong conditioning</span></li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="section" id="continue-reading-block1" style="display:none;">
  <div class="callout">
    <div class="callout-copy">
      <h2>Continue reading</h2>
      <p class="muted-mini" id="continue-reading-block1-label" style="margin:0 0 .75rem 0;"></p>
      <a class="btn" id="continue-reading-block1-btn" href="#">Continue</a>
    </div>
  </div>
</section>

<section class="section" id="lessons">
  <div class="section-head">
    <h2>Lessons (Version 0)</h2>
    <p>
      Work through these lessons in order. Each lesson page is active (even if still being developed),
      so you can navigate the full structure now.
    </p>
  </div>

  <div class="grid grid-2">

    <!-- Lesson 1 -->
    <div class="card lesson-card">
      <h3><a href="/probability/basics/what-is-probability/">1. What Is Probability (and What It Is Not)?</a></h3>
      <p>Probability as uncertainty quantification; long-run frequency vs belief; why probability is not “guarantee.”</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/probability/basics/what-is-probability/">Open lesson</a>
      </div>
    </div>

    <!-- Lesson 2 -->
    <div class="card lesson-card">
      <h3><a href="/probability/basics/outcomes-sample-spaces-events/">2. Outcomes, Sample Spaces &amp; Events</a></h3>
      <p>Outcomes vs events, events as sets, notation, and how defining the sample space prevents wrong answers.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/probability/basics/outcomes-sample-spaces-events/">Open lesson</a>
      </div>
    </div>

    <!-- Lesson 3 -->
    <div class="card lesson-card">
      <h3><a href="/probability/basics/probability-axioms-and-basic-rules/">3. Probability Axioms &amp; Basic Rules</a></h3>
      <p>Axioms, bounds, complement rule, union rule, and how rules reduce complex problems to simpler ones.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/probability/basics/probability-axioms-and-basic-rules/">Open lesson</a>
      </div>
    </div>

    <!-- Lesson 4 -->
    <div class="card lesson-card">
      <h3><a href="/probability/basics/union-intersection-and-venn-thinking/">4. Union, Intersection &amp; Venn Thinking</a></h3>
      <p>Translate words into set operations; “and” vs “or”; inclusive OR; disjoint events; avoiding language traps.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/probability/basics/union-intersection-and-venn-thinking/">Open lesson</a>
      </div>
    </div>

    <!-- Lesson 5 -->
    <div class="card lesson-card">
      <h3><a href="/probability/basics/equally-likely-and-counting-intuition/">5. Equally Likely Outcomes &amp; Counting Intuition</a></h3>
      <p>When “equally likely” is valid, counting basics, and why careless counting breaks probability reasoning.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/probability/basics/equally-likely-and-counting-intuition/">Open lesson</a>
      </div>
    </div>

    <!-- Lesson 6 -->
    <div class="card lesson-card">
      <h3><a href="/probability/basics/independence-vs-disjointness/">6. Independence vs Disjointness</a></h3>
      <p>Two different concepts often confused; tests, examples, and the correct mental model for each.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/probability/basics/independence-vs-disjointness/">Open lesson</a>
      </div>
    </div>

    <!-- Lesson 7 -->
    <div class="card lesson-card">
      <h3><a href="/probability/basics/conditional-language-traps/">7. Probability Language Traps (Common Mistakes)</a></h3>
      <p>Misreading “at least,” “given,” “either,” and “exactly”; fallacies and how to debug solutions.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/probability/basics/conditional-language-traps/">Open lesson</a>
      </div>
    </div>

    <!-- Lesson 8 -->
    <div class="card lesson-card">
      <h3><a href="/probability/basics/modeling-randomness-mini-cases/">8. Modeling Randomness: Mini Cases</a></h3>
      <p>Turn real situations into probability models: define events, assumptions, and compute probabilities responsibly.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/probability/basics/modeling-randomness-mini-cases/">Open lesson</a>
      </div>
    </div>

  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of Block 1</h2>
      <ul class="bullets">
        <li>Define sample spaces and events correctly (no ambiguous modeling)</li>
        <li>Use core probability rules reliably (complement/union/intersection)</li>
        <li>Distinguish independence from disjointness and avoid standard misconceptions</li>
        <li>Be ready for Block 2 (Conditional Probability &amp; Bayes)</li>
      </ul>
    </div>
    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Next block</div>
        <div class="mini-body">
          Continue to
          <a href="/probability/conditional/" style="color:#1a73e8; text-decoration:underline;">
            <strong>Block 2 — Conditional Probability &amp; Bayes</strong>
          </a>.
        </div>
      </div>
    </div>
  </div>
</section>

<script>
  (function () {
    // ✅ Unique key for Block 1 lessons only (isolated from everything else)
    var KEY = "esa_continue_probability_basics_lesson_v0";

    var raw = localStorage.getItem(KEY);
    if (!raw) return;

    try {
      var data = JSON.parse(raw);
      if (!data || !data.url || !data.label) return;

      var wrap = document.getElementById("continue-reading-block1");
      var label = document.getElementById("continue-reading-block1-label");
      var btn = document.getElementById("continue-reading-block1-btn");
      if (!wrap || !label || !btn) return;

      label.innerHTML = 'You last visited: <strong>' + data.label + '</strong>';
      btn.href = data.url;
      wrap.style.display = "block";
    } catch (e) {}
  })();
</script>