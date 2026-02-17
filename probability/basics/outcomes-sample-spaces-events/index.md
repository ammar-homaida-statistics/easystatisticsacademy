---
layout: default
title: "2. Outcomes, Sample Spaces & Events"
description: "Define outcomes, sample spaces, and events precisely to avoid ambiguous probability reasoning."
permalink: /probability/basics/outcomes-sample-spaces-events/
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
        Version 0 is published to lock conceptual clarity. Examples, visuals, and software demonstrations
        will be added later without changing the structure.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update last visited lesson for Block 1 -->
<script>
  (function () {
    var KEY = "esa_continue_probability_basics_lesson_v0";
    localStorage.setItem(KEY, JSON.stringify({
      url: "/probability/basics/outcomes-sample-spaces-events/",
      label: "Lesson 2 — Outcomes, Sample Spaces & Events",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card">
    <div class="hero-copy">

      <div class="badge-row">
        <span class="badge">Block 1</span>
        <span class="badge">Lesson 2</span>
        <span class="badge">Modeling</span>
        <span class="badge">Precision</span>
      </div>

      <h1>2. Outcomes, Sample Spaces &amp; Events</h1>

      <p class="lead">
        Probability works only when its basic objects are defined clearly.
        In this lesson, we define outcomes, sample spaces, and events with precision.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/probability/basics/what-is-probability/">
          ← Previous lesson: 1. What Is Probability (and What It Is Not)?
        </a>
        <a class="btn btn-outline" href="/probability/basics/">Back to Block 1</a>
      </div>

      <p class="muted-mini">
        Version 0: conceptual clarity first. Visual and applied examples will follow.
      </p>

    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>Learning objective</h2>
    <p>
      By the end of this lesson, you should be able to:
    </p>
  </div>

  <ul class="bullets">
    <li>Define an outcome correctly</li>
    <li>Construct a valid sample space</li>
    <li>Express events as subsets of a sample space</li>
    <li>Avoid ambiguous or incomplete modeling</li>
  </ul>
</section>

<section class="section">
  <div class="section-head">
    <h2>1) What is an outcome?</h2>
    <p>
      An <strong>outcome</strong> is a single possible result of a random process.
    </p>
  </div>

  <div class="card">
    <h3>Examples</h3>
    <ul class="bullets">
      <li>Coin toss → H or T</li>
      <li>Die roll → 1,2,3,4,5,6</li>
      <li>Survey response → Yes or No</li>
      <li>Exam score → 0 to 100</li>
    </ul>
  </div>

  <div class="callout">
    <div class="callout-copy">
      <h2>Important</h2>
      <p style="margin:0;">
        An outcome is the smallest level of resolution in your model.
        If you define outcomes poorly, everything that follows becomes incorrect.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>2) What is a sample space?</h2>
    <p>
      The <strong>sample space</strong> (usually denoted S or Ω) is the set of all possible outcomes.
    </p>
  </div>

  <div class="card">
    <h3>Examples</h3>
    <ul class="bullets">
      <li>Coin toss → S = {H, T}</li>
      <li>Die roll → S = {1,2,3,4,5,6}</li>
      <li>Two coin tosses → S = {HH, HT, TH, TT}</li>
    </ul>
  </div>

  <div class="callout">
    <div class="callout-copy">
      <h2>Modeling warning</h2>
      <p style="margin:0;">
        The sample space depends on how you define the experiment.
        Different definitions → different probabilities.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>3) What is an event?</h2>
    <p>
      An <strong>event</strong> is a subset of the sample space.
      It may contain one or more outcomes.
    </p>
  </div>

  <div class="card">
    <h3>Examples</h3>
    <ul class="bullets">
      <li>Rolling an even number → {2,4,6}</li>
      <li>At least one head in two tosses → {HH, HT, TH}</li>
      <li>Score above 80 → all outcomes > 80</li>
    </ul>
  </div>

  <div class="callout">
    <div class="callout-copy">
      <h2>Key insight</h2>
      <p style="margin:0;">
        Probability is assigned to events — not to vague descriptions.
        Always express events in terms of outcomes.
      </p>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-head">
    <h2>4) Why precision matters</h2>
    <p>
      Many probability mistakes come from unclear definitions.
    </p>
  </div>

  <div class="grid grid-2">

    <div class="card">
      <h3>Ambiguity example</h3>
      <p>
        “Probability that a family with two children has two boys.”
      </p>
      <p>
        Is the sample space {BB, BG, GB, GG}?
        Or does order not matter?
        The answer changes the probability.
      </p>
    </div>

    <div class="card">
      <h3>Lesson</h3>
      <p>
        Always define:
      </p>
      <ul class="bullets">
        <li>What counts as an outcome?</li>
        <li>Are outcomes equally likely?</li>
        <li>What exactly is the event?</li>
      </ul>
    </div>

  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of this lesson</h2>
      <ul class="bullets">
        <li>Define outcome, sample space, and event precisely</li>
        <li>Understand events as subsets</li>
        <li>Avoid ambiguous modeling</li>
        <li>Be ready for probability rules (next lesson)</li>
      </ul>
    </div>
  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Next lesson</h2>
      <p style="margin:0;">
        Now that we have defined events precisely, we can assign numbers to them using formal rules.
      </p>

      <div class="pill-row" style="margin-top:1rem;">
        <a class="btn" href="/probability/basics/probability-axioms-and-basic-rules/">
          Next lesson: 3. Probability Axioms & Basic Rules →
        </a>
      </div>
    </div>
  </div>
</section>