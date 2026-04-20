---
layout: default
title: Block 1 — Choosing the Right Method
permalink: /applied-statistics/method-selection/
sidebar: false
---

<!-- UNDER CONSTRUCTION -->
<section class="section section-slim">
  <div class="callout" style="background:#fff4e5; border:2px solid #ff9800; padding:2rem; border-radius:12px;">
    <div class="callout-copy">
      <h2 style="margin-top:0; color:#e65100; font-size:1.8rem;">
        🚧 This Block Is Under Construction
      </h2>
      <p style="margin:0; font-size:1.05rem; line-height:1.6;">
        This block builds the core decision-making framework of applied statistics:
        how to choose the correct method based on the research question, variable types,
        and study design—without relying on memorization.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update last visited block -->
<script>
(function () {
  localStorage.setItem("esa_continue_applied_last_block_v0", JSON.stringify({
    url: "/applied-statistics/method-selection/",
    label: "Block 1 — Choosing the Right Method",
    ts: Date.now()
  }));
})();
</script>

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card hero-split">

    <div class="hero-copy">

      <div class="badge-row">
        <span class="badge">Block 1</span>
        <span class="badge">Decision</span>
        <span class="badge">Methods</span>
        <span class="badge">Framework</span>
      </div>

      <h1>Block 1 — Choosing the Right Method</h1>

      <p class="lead">
        Applied statistics begins with choosing the correct method.
        This block teaches how statistical decisions are made by connecting
        research questions, variable types, and study design into a clear framework.
      </p>

      <div class="hero-actions">
        <a class="btn btn-outline" href="/applied-statistics/">Back to Applied Statistics</a>
        <a class="btn" href="#lessons">Open structure</a>
      </div>

      <p class="muted-mini">
        Version 0: structure is locked. Content will expand without changing URLs.
      </p>

    </div>

    <div class="hero-panel">
      <div class="panel-card">
        <h2 class="panel-title">What this block covers</h2>
        <ul class="quickstart" style="list-style:none; padding-left:0;">

          <li><strong>Research questions</strong><span class="meta">What are we trying to answer?</span></li>
          <li><strong>Variable types</strong><span class="meta">Categorical vs numerical</span></li>
          <li><strong>Comparisons vs relationships</strong><span class="meta">Different analytical goals</span></li>
          <li><strong>Choosing tests</strong><span class="meta">Matching method to situation</span></li>
          <li><strong>Decision frameworks</strong><span class="meta">Structured thinking over memorization</span></li>

        </ul>
      </div>
    </div>

  </div>
</section>

<!-- ✅ Continue Reading -->
<section class="section" id="continue-reading-method-selection" style="display:none;">
  <div class="callout">
    <div class="callout-copy">
      <h2>Continue reading</h2>
      <p class="muted-mini" id="continue-reading-method-selection-label" style="margin:0 0 .75rem 0;"></p>
      <a class="btn" id="continue-reading-method-selection-btn" href="#">Continue</a>
    </div>
  </div>
</section>

<!-- LESSONS -->
<section class="section" id="lessons">

  <div class="section-head">
    <h2>Lessons (Version 0)</h2>
    <p>
      Lessons are structured to build a complete decision-making framework.
      This structure will not change.
    </p>
  </div>

  <div class="grid grid-2">

    <div class="card lesson-card">
      <h3><a href="/applied-statistics/method-selection/research-questions/">1. Types of Research Questions</a></h3>
      <p>Understand different types of questions: comparison, association, prediction, and description.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/applied-statistics/method-selection/research-questions/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/applied-statistics/method-selection/variable-types/">2. Types of Variables</a></h3>
      <p>Classify variables correctly: categorical, numerical, discrete, continuous.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/applied-statistics/method-selection/variable-types/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/applied-statistics/method-selection/comparisons-vs-relationships/">3. Comparisons vs Relationships</a></h3>
      <p>Distinguish between comparing groups and studying relationships between variables.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/applied-statistics/method-selection/comparisons-vs-relationships/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/applied-statistics/method-selection/common-tests/">4. Overview of Common Statistical Tests</a></h3>
      <p>Understand when to use t-tests, chi-square, correlation, and ANOVA conceptually.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/applied-statistics/method-selection/common-tests/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/applied-statistics/method-selection/decision-framework/">5. Building a Decision Framework</a></h3>
      <p>Integrate question type, variables, and design into a structured method-selection process.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/applied-statistics/method-selection/decision-framework/">Open lesson</a>
      </div>
    </div>

  </div>
</section>

<!-- OUTCOME -->
<section class="section section-slim">
  <div class="callout">

    <div class="callout-copy">
      <h2>Outcome of Block 1</h2>
      <ul class="bullets">
        <li>Identify types of research questions correctly</li>
        <li>Classify variables accurately</li>
        <li>Distinguish comparisons vs relationships</li>
        <li>Select appropriate statistical methods conceptually</li>
        <li>Apply a structured decision framework</li>
      </ul>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Next block</div>
        <div class="mini-body">
          Continue to
          <a href="/applied-statistics/study-design/" style="color:#1a73e8; text-decoration:underline;">
            <strong>Block 2 — Study Design & Data Context</strong>
          </a>.
        </div>
      </div>
    </div>

  </div>
</section>

<!-- CONTINUE READING SCRIPT -->
<script>
(function () {
  var KEY = "esa_continue_applied_method-selection_lesson_v0";
  var raw = localStorage.getItem(KEY);
  if (!raw) return;

  try {
    var data = JSON.parse(raw);
    if (!data || !data.url || !data.label) return;

    var wrap = document.getElementById("continue-reading-method-selection");
    var label = document.getElementById("continue-reading-method-selection-label");
    var btn = document.getElementById("continue-reading-method-selection-btn");

    label.innerHTML = 'You last visited: <strong>' + data.label + '</strong>';
    btn.href = data.url;
    wrap.style.display = "block";

  } catch (e) {}
})();
</script>