---
layout: default
title: Block 4 — Effect Sizes & Interpretation
permalink: /applied-statistics/effect-sizes/
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
        This block focuses on interpreting statistical results meaningfully.
        It explains effect sizes, practical significance, and how to move beyond
        p-values when understanding results.
      </p>
    </div>
  </div>
</section>

<!-- ✅ Update last visited block -->
<script>
(function () {
  localStorage.setItem("esa_continue_applied_last_block_v0", JSON.stringify({
    url: "/applied-statistics/effect-sizes/",
    label: "Block 4 — Effect Sizes & Interpretation",
    ts: Date.now()
  }));
})();
</script>

<!-- HERO -->
<section class="hero hero-section">
  <div class="hero-card hero-split">

    <div class="hero-copy">

      <div class="badge-row">
        <span class="badge">Block 4</span>
        <span class="badge">Effect Size</span>
        <span class="badge">Interpretation</span>
        <span class="badge">Meaning</span>
      </div>

      <h1>Block 4 — Effect Sizes & Interpretation</h1>

      <p class="lead">
        Statistical significance does not equal importance.
        This block teaches how to interpret results using effect sizes,
        direction, magnitude, and practical meaning.
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

          <li><strong>Effect sizes</strong><span class="meta">Magnitude of relationships</span></li>
          <li><strong>Statistical vs practical significance</strong><span class="meta">Meaning vs detection</span></li>
          <li><strong>Direction and strength</strong><span class="meta">Understanding relationships</span></li>
          <li><strong>Confidence intervals</strong><span class="meta">Range of plausible values</span></li>
          <li><strong>Interpretation errors</strong><span class="meta">Common mistakes in reading results</span></li>

        </ul>
      </div>
    </div>

  </div>
</section>

<!-- ✅ Continue Reading -->
<section class="section" id="continue-reading-effect-sizes" style="display:none;">
  <div class="callout">
    <div class="callout-copy">
      <h2>Continue reading</h2>
      <p class="muted-mini" id="continue-reading-effect-sizes-label" style="margin:0 0 .75rem 0;"></p>
      <a class="btn" id="continue-reading-effect-sizes-btn" href="#">Continue</a>
    </div>
  </div>
</section>

<!-- LESSONS -->
<section class="section" id="lessons">

  <div class="section-head">
    <h2>Lessons (Version 0)</h2>
    <p>
      Lessons focus on interpreting results correctly and meaningfully,
      beyond simple significance testing.
    </p>
  </div>

  <div class="grid grid-2">

    <div class="card lesson-card">
      <h3><a href="/applied-statistics/effect-sizes/what-is-effect-size/">1. What Is an Effect Size?</a></h3>
      <p>Understand effect size as the magnitude of a relationship or difference.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/applied-statistics/effect-sizes/what-is-effect-size/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/applied-statistics/effect-sizes/statistical-vs-practical/">2. Statistical vs Practical Significance</a></h3>
      <p>Distinguish between detecting an effect and understanding its importance.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/applied-statistics/effect-sizes/statistical-vs-practical/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/applied-statistics/effect-sizes/direction-strength/">3. Direction and Strength of Effects</a></h3>
      <p>Interpret whether relationships are positive, negative, weak, or strong.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/applied-statistics/effect-sizes/direction-strength/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/applied-statistics/effect-sizes/confidence-intervals/">4. Confidence Intervals in Interpretation</a></h3>
      <p>Use confidence intervals to understand uncertainty and plausible values.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/applied-statistics/effect-sizes/confidence-intervals/">Open lesson</a>
      </div>
    </div>

    <div class="card lesson-card">
      <h3><a href="/applied-statistics/effect-sizes/common-interpretation-errors/">5. Common Interpretation Mistakes</a></h3>
      <p>Avoid misinterpretations of p-values, confidence intervals, and effect sizes.</p>
      <div class="pill-row">
        <a class="btn btn-outline" href="/applied-statistics/effect-sizes/common-interpretation-errors/">Open lesson</a>
      </div>
    </div>

  </div>
</section>

<!-- OUTCOME -->
<section class="section section-slim">
  <div class="callout">

    <div class="callout-copy">
      <h2>Outcome of Block 4</h2>
      <ul class="bullets">
        <li>Understand what effect sizes represent</li>
        <li>Distinguish statistical from practical significance</li>
        <li>Interpret direction and strength correctly</li>
        <li>Use confidence intervals conceptually</li>
        <li>Avoid common interpretation errors</li>
      </ul>
    </div>

    <div class="callout-side">
      <div class="mini" style="border-left:4px solid #1a73e8; padding-left:12px;">
        <div class="mini-title" style="color:#1a73e8;">Next block</div>
        <div class="mini-body">
          Continue to
          <a href="/applied-statistics/common-mistakes/" style="color:#1a73e8; text-decoration:underline;">
            <strong>Block 5 — Common Mistakes & Pitfalls</strong>
          </a>.
        </div>
      </div>
    </div>

  </div>
</section>

<!-- CONTINUE READING SCRIPT -->
<script>
(function () {
  var KEY = "esa_continue_applied_effect-sizes_lesson_v0";
  var raw = localStorage.getItem(KEY);
  if (!raw) return;

  try {
    var data = JSON.parse(raw);
    if (!data || !data.url || !data.label) return;

    var wrap = document.getElementById("continue-reading-effect-sizes");
    var label = document.getElementById("continue-reading-effect-sizes-label");
    var btn = document.getElementById("continue-reading-effect-sizes-btn");

    if (!wrap || !label || !btn) return;

    label.innerHTML = 'You last visited: <strong>' + data.label + '</strong>';
    btn.href = data.url;
    wrap.style.display = "block";

  } catch (e) {}
})();
</script>