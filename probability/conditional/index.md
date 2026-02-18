---
layout: default
title: Block 2 — Conditional Probability & Bayes
description: Conditioning, multiplication rule, total probability, Bayes’ theorem, tree diagrams, and structured updating of uncertainty.
permalink: /probability/conditional/
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
        This block builds the machinery of conditional reasoning.
        Lessons are being published in fixed pedagogical order as part of the Probability unit.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update "last visited block" for Probability home -->
<script>
  (function () {
    var KEY = "esa_continue_probability_last_block_v0";

    localStorage.setItem(KEY, JSON.stringify({
      url: "/probability/conditional/",
      label: "Block 2 — Conditional Probability & Bayes",
      ts: Date.now()
    }));
  })();
</script>

<section class="hero hero-section">
  <div class="hero-card hero-split">
    <div class="hero-copy">
      <div class="badge-row">
        <span class="badge">Block 2</span>
        <span class="badge">Conditioning</span>
        <span class="badge">Updating</span>
        <span class="badge">Bayes</span>
      </div>

      <h1>Block 2 — Conditional Probability &amp; Bayes</h1>
      <p class="lead">
        Conditioning changes everything. This block formalizes how new information
        updates probabilities and builds the bridge toward statistical inference.
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
          <li style="margin:.35rem 0;"><strong>Conditional probability</strong><span class="meta">Sample space restriction</span></li>
          <li style="margin:.35rem 0;"><strong>Multiplication rule</strong><span class="meta">Joint probabilities</span></li>
          <li style="margin:.35rem 0;"><strong>Law of total probability</strong><span class="meta">Partitioning events</span></li>
          <li style="margin:.35rem 0;"><strong>Bayes’ theorem</strong><span class="meta">Reversing conditioning</span></li>
          <li style="margin:.35rem 0;"><strong>Tree diagrams</strong><span class="meta">Structured reasoning</span></li>
          <li style="margin:.35rem 0;"><strong>Base-rate logic</strong><span class="meta">Avoiding common fallacies</span></li>
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="section" id="continue-reading-block2" style="display:none;">
  <div class="callout">
    <div class="callout-copy">
      <h2>Continue reading</h2>
      <p class="muted-mini" id="continue-reading-block2-label" style="margin:0 0 .75rem 0;"></p>
      <a class="btn" id="continue-reading-block2-btn" href="#">Continue</a>
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
      <h3><a href="/probability/conditional/what-is-conditional-probability/">1. What Is Conditional Probability?</a></h3>
      <p>How conditioning restricts the sample space and why new information changes probabilities.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/probability/conditional/what-is-conditional-probability/">Open lesson</a>
      </div>
    </div>

    <!-- Lesson 2 -->
    <div class="card lesson-card">
      <h3><a href="/probability/conditional/multiplication-rule/">2. The Multiplication Rule</a></h3>
      <p>Deriving joint probabilities from conditional probability; structure of P(A ∩ B).</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/probability/conditional/multiplication-rule/">Open lesson</a>
      </div>
    </div>

    <!-- Lesson 3 -->
    <div class="card lesson-card">
      <h3><a href="/probability/conditional/law-of-total-probability/">3. Law of Total Probability</a></h3>
      <p>Partitioning the sample space and computing probabilities across mutually exclusive cases.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/probability/conditional/law-of-total-probability/">Open lesson</a>
      </div>
    </div>

    <!-- Lesson 4 -->
    <div class="card lesson-card">
      <h3><a href="/probability/conditional/bayes-theorem/">4. Bayes’ Theorem</a></h3>
      <p>Reversing conditioning; prior, likelihood, posterior; structured probability updating.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/probability/conditional/bayes-theorem/">Open lesson</a>
      </div>
    </div>

    <!-- Lesson 5 -->
    <div class="card lesson-card">
      <h3><a href="/probability/conditional/tree-diagrams/">5. Tree Diagrams & Structured Reasoning</a></h3>
      <p>Visual representation of sequential events and conditional branches.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/probability/conditional/tree-diagrams/">Open lesson</a>
      </div>
    </div>

    <!-- Lesson 6 -->
    <div class="card lesson-card">
      <h3><a href="/probability/conditional/base-rate-neglect-and-fallacies/">6. Base-Rate Neglect & Common Fallacies</a></h3>
      <p>Why intuitive reasoning fails; medical tests, rare events, and posterior misinterpretation.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/probability/conditional/base-rate-neglect-and-fallacies/">Open lesson</a>
      </div>
    </div>

  </div>
</section>

<section class="section section-slim">
  <div class="callout">
    <div class="callout-copy">
      <h2>Outcome of Block 2</h2>
      <ul class="bullets">
        <li>Compute conditional probabilities correctly</li>
        <li>Use multiplication and total probability rules reliably</li>
        <li>Apply Bayes’ theorem without confusion</li>
        <li>Recognize and correct base-rate fallacies</li>
        <li>Be ready for Random Variables (Block 3)</li>
      </ul>
    </div>
    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Next block</div>
        <div class="mini-body">
          Continue to
          <a href="/probability/random-variables/" style="color:#1a73e8; text-decoration:underline;">
            <strong>Block 3 — Random Variables</strong>
          </a>.
        </div>
      </div>
    </div>
  </div>
</section>

<script>
  (function () {
    var KEY = "esa_continue_probability_conditional_lesson_v0";

    var raw = localStorage.getItem(KEY);
    if (!raw) return;

    try {
      var data = JSON.parse(raw);
      if (!data || !data.url || !data.label) return;

      var wrap = document.getElementById("continue-reading-block2");
      var label = document.getElementById("continue-reading-block2-label");
      var btn = document.getElementById("continue-reading-block2-btn");
      if (!wrap || !label || !btn) return;

      label.innerHTML = 'You last visited: <strong>' + data.label + '</strong>';
      btn.href = data.url;
      wrap.style.display = "block";
    } catch (e) {}
  })();
</script>